import sys

from kafka import KafkaProducer

from ncclient import manager
from ncclient.xml_ import to_ele

import xml.etree.ElementTree as et

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

print("Hello, this is the ncclient-collector for " + container_name)

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

while True:
    sub_data = session.take_notification()
    print("I have received a notification!")
    #print(str(sub_data.notification_xml).encode('utf-8'))
    if (sub_data != None):
        notification_xml = str(sub_data.notification_xml)
        root = et.fromstring(notification_xml)
        # A new subelement is added to the NETCONF notification: fromDevice.
        # It is the name of the device that is sending the notification.
        # WARNING: This is not defined in the specification.
        from_device = et.SubElement(root, 'fromDevice')
        from_device.text = container_name
        eventTime = root[0].text
        notification_xml = et.tostring(root, encoding='unicode')
        producer.send('interfaces-state-subscriptions', value=notification_xml.encode('utf-8'))
        print("I have sent it to a Kafka topic named interfaces-state-subscriptions")
        print("The eventTime element of the notification is: " + eventTime)
    producer.flush()
