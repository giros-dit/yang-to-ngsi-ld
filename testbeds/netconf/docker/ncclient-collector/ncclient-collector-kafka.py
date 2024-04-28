import sys

from kafka import KafkaProducer

from ncclient import manager
from ncclient.xml_ import to_ele

import xml.etree.ElementTree as et

import time
import datetime
from dateutil import parser

import csv

if len(sys.argv) < 4:
    print("Error - Incorrect arguments")
    print('Usage: python ncclient-collector-kafka.py <container_name> <interface_name> <period_in_cs>')
    print('Example: python ncclient-collector-kafka.py clab-telemetry-ixiac-lab-r1 GigabitEthernet1 1000')
    exit(1)
else:
    container_name = sys.argv[1]

r = {
    "host": container_name,
    "port": 830,
    "username": "admin",
    "password": "admin",
    "hostkey_verify": False,
    "device_params": {"name": "csr"}
}

performance_measurements_file = open("performance_measurements-"+container_name+".csv", "w", newline='')
csv_writer = csv.writer(performance_measurements_file)
csv_header = ["evenTime", "start_datetime", "evaluation_time", "mean_evaluation_time",
              "min_evaluation_time", "max_evaluation_time", "notifications_received"]
csv_writer.writerow(csv_header)  

print("Hello, this is the ncclient-collector for " + container_name + " interface " + sys.argv[2])

session = manager.connect(**r)

print("I have successfully established a session with ID# " + session.session_id)

xpath = "/interfaces-state/interface[name=\'" + sys.argv[2] + "\']"
subscription = "period"
period = sys.argv[3]


# When building the RPC request XML, use dampening-period for on-change notifications (when supported).
# Otherwise, use period and specify an integer value for the time in centiseconds.

rpc = """

    <establish-subscription xmlns="urn:ietf:params:xml:ns:yang:ietf-event-notifications"
    xmlns:yp="urn:ietf:params:xml:ns:yang:ietf-yang-push">
        <stream>yp:yang-push</stream>
        <yp:xpath-filter>{0}</yp:xpath-filter>
        <yp:{1}>{2}</yp:{1}>
    </establish-subscription>

""".format(xpath, subscription, period)

request = session.dispatch(to_ele(rpc))

#print(request)

producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

print("I have subscribed myself to get periodic YANG-Push notifications for X-Path " + xpath + " of network device " + container_name)
delta_times = []

while True:
    sub_data = session.take_notification()
    print("\nI have received a notification!" + "\n")
    #print(str(sub_data.notification_xml).encode('utf-8'))
    if (sub_data != None):
        notification_xml = str(sub_data.notification_xml)
        start_datetime = datetime.datetime.now(datetime.timezone.utc)
        root = et.fromstring(notification_xml)
        # A new subelement is added to the NETCONF notification: fromDevice.
        # It is the name of the device that is sending the notification.
        # WARNING: This is not defined in the specification.
        from_device = et.SubElement(root, 'fromDevice')
        from_device.text = container_name
        eventTime = root[0].text
        delta_time = (start_datetime - parser.parse(eventTime)).total_seconds()
        delta_times.append(delta_time)
        print("--- PERFORMANCE MEASUREMENTS ---\n")
        print("EVENT TIME: " + parser.parse(eventTime).strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")           
        print("NOTIFICATION RECEIVED AT: " + start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
        print("NOTIFICATIONS RECEIVED SO FAR: " + str(len(delta_times)) + "\n")
        mean_evaluation_time = sum(delta_times)/len(delta_times)
        min_evaluation_time = min(delta_times)
        max_evaluation_time = max(delta_times)
        print(f"ITERATION EXECUTION TIME: {delta_time * 1e3} ms\n")
        print(f"MEAN EVALUATION TIME: {mean_evaluation_time * 1e3} ms\n")
        print(f"MIN EVALUATION TIME: {min_evaluation_time * 1e3} ms\n")
        print(f"MAX EVALUATION TIME VALUE: {max_evaluation_time * 1e3} ms\n")
        print("--- PERFORMANCE MEASUREMENTS ---\n")
        csv_data = [parser.parse(eventTime).strftime("%Y-%m-%dT%H:%M:%S.%fZ"), start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                    str(delta_time * 1e3) + " ms", str(mean_evaluation_time * 1e3) + " ms",
                    str(min_evaluation_time * 1e3) + " ms", str(max_evaluation_time * 1e3) + " ms",
                    str(len(delta_times))]
        csv_writer.writerow(csv_data)
        performance_measurements_file.flush()
        notification_xml = et.tostring(root, encoding='unicode')
        producer.send('interfaces-state-subscriptions', value=notification_xml.encode('utf-8'))
        print("I have sent it to a Kafka topic named interfaces-state-subscriptions")
        print("The eventTime element of the notification is: " + eventTime)
        producer.flush()
