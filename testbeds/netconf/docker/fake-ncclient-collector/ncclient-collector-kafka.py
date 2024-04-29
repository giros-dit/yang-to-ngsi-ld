import sys
from kafka import KafkaProducer
import xml.etree.ElementTree as et
import time
import datetime


producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

original_data_r1_eth2 = et.parse('xe-csr1000v-notification-r1-eth2.xml')
root = original_data_r1_eth2.getroot()
from_device_r1_eth2 = et.SubElement(root, 'fromDevice')
from_device_r1_eth2.text = str(sys.argv[1])

original_data_r1_eth3 = et.parse('xe-csr1000v-notification-r1-eth3.xml')
root = original_data_r1_eth3.getroot()
from_device_r1_eth3 = et.SubElement(root, 'fromDevice')
from_device_r1_eth3.text = str(sys.argv[1])

original_data_r2_eth2 = et.parse('xe-csr1000v-notification-r2-eth2.xml')
root = original_data_r2_eth2.getroot()
from_device_r2_eth2 = et.SubElement(root, 'fromDevice')
from_device_r2_eth2.text = str(sys.argv[1])

original_data_r2_eth3 = et.parse('xe-csr1000v-notification-r2-eth3.xml')
root = original_data_r2_eth3.getroot()
from_device_r2_eth3 = et.SubElement(root, 'fromDevice')
from_device_r2_eth3.text = str(sys.argv[1])

while True:    
    data = original_data_r1_eth2
    root = data.getroot()

    current_datetime = datetime.datetime.now(datetime.timezone.utc)

    eventTime = root.find(".//{urn:ietf:params:xml:ns:netconf:notification:1.0}eventTime")
    eventTime.text = current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    notification_xml = et.tostring(root, encoding='unicode')

    producer.send('interfaces-state-subscriptions', value=notification_xml.encode('utf-8'))
    producer.flush()

    print("NOTIFICATION DATA R1 Ethernet2: " + str(notification_xml) + "\n")
    print("NOTIFICATION TIMESTAMP R1 Ethernet2: " + current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")

    data = original_data_r1_eth3
    root = data.getroot()

    current_datetime = datetime.datetime.now(datetime.timezone.utc)

    eventTime = root.find(".//{urn:ietf:params:xml:ns:netconf:notification:1.0}eventTime")
    eventTime.text = current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    notification_xml = et.tostring(root, encoding='unicode')

    producer.send('interfaces-state-subscriptions', value=notification_xml.encode('utf-8'))
    producer.flush()

    print("NOTIFICATION DATA R1 Ethernet3: " + str(notification_xml) + "\n")
    print("NOTIFICATION TIMESTAMP R1 Ethernet3: " + current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")

    data = original_data_r2_eth2
    root = data.getroot()

    current_datetime = datetime.datetime.now(datetime.timezone.utc)

    eventTime = root.find(".//{urn:ietf:params:xml:ns:netconf:notification:1.0}eventTime")
    eventTime.text = current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    notification_xml = et.tostring(root, encoding='unicode')

    producer.send('interfaces-state-subscriptions', value=notification_xml.encode('utf-8'))
    producer.flush()

    print("NOTIFICATION DATA R2 Ethernet2: " + str(notification_xml) + "\n")
    print("NOTIFICATION TIMESTAMP R2 Ethernet2: " + current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")

    data = original_data_r2_eth3
    root = data.getroot()

    current_datetime = datetime.datetime.now(datetime.timezone.utc)

    eventTime = root.find(".//{urn:ietf:params:xml:ns:netconf:notification:1.0}eventTime")
    eventTime.text = current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    notification_xml = et.tostring(root, encoding='unicode')

    producer.send('interfaces-state-subscriptions', value=notification_xml.encode('utf-8'))
    producer.flush()

    print("NOTIFICATION DATA R2 Ethernet3: " + str(notification_xml) + "\n")
    print("NOTIFICATION TIMESTAMP R2 Ethernet3: " + current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")

    time.sleep(int(sys.argv[2]))