import sys
from kafka import KafkaProducer
import time
import random
import datetime
import json
import csv

THROUGHPUT_INTERVAL = 1

throughput_performance_measurements_file = open("throughput_measurements.csv", "w", newline='')
throughput_csv_writer = csv.writer(throughput_performance_measurements_file)
throughput_csv_header = ["current_time", "start_time", "throughput_records", "throughput_bytes", "throughput_interval"]
throughput_csv_writer.writerow(throughput_csv_header)

producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

with open('openconfig-cisco-xrv9-notification.json', 'r') as file:
    data_r1 = json.load(file)

start_interval = time.perf_counter_ns() / 1e9
start_interval_datetime = datetime.datetime.now(datetime.timezone.utc)
processed_count = 0
msg_iteration_size = 0
while True:
    for i in range(0, 48):
        current_time = time.time_ns()
        current_datetime = datetime.datetime.now(datetime.timezone.utc)

        data_r1[0]['timestamp'] = current_time
        data_r1[0]['tags']['interface_name'] = "GigabitEthernet0/0/0/" + str(i)

        producer.send('interfaces-state-notifications', value=json.dumps(data_r1).encode('utf-8'))
        producer.flush()
        msg_size = len(json.dumps(data_r1).encode('utf-8'))
        msg_iteration_size = msg_iteration_size + msg_size

        print("NOTIFICATION DATA R1 interface " + "GigabitEthernet0/0/0/" + str(i) + ": " + str(json.dumps(data_r1)) + "\n")
        print("NOTIFICATION TIMESTAMP R1 interface " + "GigabitEthernet0/0/0/" + str(i) + ": " + current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
        
        processed_count += 1
        now_time = time.perf_counter_ns() / 1e9
        if now_time - start_interval >= THROUGHPUT_INTERVAL:
            now_datetime = datetime.datetime.now(datetime.timezone.utc)
            throughput_records = processed_count / (now_time - start_interval) 
            throughput_bytes = msg_iteration_size / (now_time - start_interval)
            
            throughput_csv_data = [start_interval_datetime, now_datetime, throughput_records, throughput_bytes, now_time - start_interval]
            throughput_csv_writer.writerow(throughput_csv_data)
            throughput_performance_measurements_file.flush()

            processed_count = 0
            msg_iteration_size = 0
            start_interval = now_time
            start_interval_datetime = now_datetime