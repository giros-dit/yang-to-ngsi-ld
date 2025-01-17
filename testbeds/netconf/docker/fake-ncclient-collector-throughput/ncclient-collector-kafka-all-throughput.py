import sys
from kafka import KafkaProducer
import xml.etree.ElementTree as et
import random
import time
import datetime
import csv

THROUGHPUT_INTERVAL = 1

throughput_performance_measurements_file = open("throughput_measurements.csv", "w", newline='')
throughput_csv_writer = csv.writer(throughput_performance_measurements_file)
throughput_csv_header = ["current_time", "start_time", "throughput_records", "throughput_bytes", "throughput_interval"]
throughput_csv_writer.writerow(throughput_csv_header)

producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

original_data_r1 = et.parse('xe-csr1000v-notification-48ifaces.xml')
root = original_data_r1.getroot()
from_device_r1 = et.SubElement(root, 'fromDevice')
from_device_r1.text = str(sys.argv[1])

start_interval = time.perf_counter_ns() / 1e9
start_interval_datetime = datetime.datetime.now(datetime.timezone.utc)
processed_count = 0
msg_iteration_size = 0
while True:
    data = original_data_r1
    root = data.getroot()

    current_datetime = datetime.datetime.now(datetime.timezone.utc)

    eventTime = root.find(".//{urn:ietf:params:xml:ns:netconf:notification:1.0}eventTime")
    eventTime.text = current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    notification_xml = et.tostring(root, encoding='unicode')

    producer.send('interfaces-state-subscriptions', value=notification_xml.encode('utf-8'))
    producer.flush()
    msg_size = len(notification_xml.encode('utf-8'))
    msg_iteration_size = msg_iteration_size + msg_size
    print("NOTIFICATION DATA R1: " + str(notification_xml) + "\n")
    print("NOTIFICATION TIMESTAMP R1: " + current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
    processed_count += 1
    now_time = time.perf_counter_ns() / 1e9
    now_datetime = datetime.datetime.now(datetime.timezone.utc)
    if now_time - start_interval >= THROUGHPUT_INTERVAL:
        throughput_records = processed_count / (now_time - start_interval) 
        throughput_bytes = msg_iteration_size / (now_time - start_interval)
        
        throughput_csv_data = [start_interval_datetime, now_datetime, throughput_records, throughput_bytes, now_time - start_interval]
        throughput_csv_writer.writerow(throughput_csv_data)
        throughput_performance_measurements_file.flush()

        processed_count = 0
        msg_iteration_size = 0
        start_interval = now_time
        start_interval_datetime = now_datetime