import sys
from kafka import KafkaProducer
import xml.etree.ElementTree as et
import random
import time
import datetime


producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

original_data_r1 = et.parse('xe-csr1000v-notification-48ifaces.xml')
root = original_data_r1.getroot()
from_device_r1 = et.SubElement(root, 'fromDevice')
from_device_r1.text = str(sys.argv[1])

while True:    
    data = original_data_r1
    root = data.getroot()

    current_datetime = datetime.datetime.now(datetime.timezone.utc)

    eventTime = root.find(".//{urn:ietf:params:xml:ns:netconf:notification:1.0}eventTime")
    eventTime.text = current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    notification_xml = et.tostring(root, encoding='unicode')

    producer.send('interfaces-state-subscriptions', value=notification_xml.encode('utf-8'))
    producer.flush()

    print("NOTIFICATION DATA R1: " + str(notification_xml) + "\n")
    print("NOTIFICATION TIMESTAMP R1: " + current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")

    timeout = random.uniform(4.5, float(sys.argv[2]))
    print("Time sleep of: " + str(timeout) + " seconds \n")
    
    time.sleep(timeout)