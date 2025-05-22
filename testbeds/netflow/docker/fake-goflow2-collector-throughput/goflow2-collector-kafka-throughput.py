import sys
from kafka import KafkaProducer
import time
import random
import datetime
import json
import csv

THROUGHPUT_INTERVAL = 1

#exec_times = []

throughput_performance_measurements_file = open("throughput_measurements.csv", "w", newline='')
throughput_csv_writer = csv.writer(throughput_performance_measurements_file)
throughput_csv_header = ["current_time", "start_time", "throughput_records", "throughput_bytes", "throughput_interval"]
throughput_csv_writer.writerow(throughput_csv_header)

producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

with open('netflow-v9.json', 'r') as file:
    data_flows = json.load(file)

system_uptime = 774518
data_flows['netflow-v9:netflow']['export-packet']['count'] = 1
number_flow = 1

start_interval = time.perf_counter_ns() / 1e9
start_interval_datetime = datetime.datetime.now(datetime.timezone.utc)
processed_count = 0
msg_iteration_size = 0

while True:
    start_time = time.perf_counter_ns()
    start_datetime = datetime.datetime.now(datetime.timezone.utc)

    current_time_s = time.time()
    current_time_ns = time.time_ns()
    current_datetime = datetime.datetime.now(datetime.timezone.utc)

    data_flows['netflow-v9:netflow']['export-packet']['unix-seconds'] = int(current_time_s)
    data_flows['netflow-v9:netflow']['export-packet']['system-uptime'] = system_uptime
    data_flows['netflow-v9:netflow']['collector-goflow2']['time-received'] = int(current_time_ns/1e6)
    data_flows['netflow-v9:netflow']['export-packet']['flow-data-record'][0]['flow-id'] = number_flow

    size_exact = len(json.dumps(data_flows).encode('utf-8'))
    print(f"Tamaño exacto del JSON en bytes: {size_exact}")

    producer.send('netflow-driver-output', value=json.dumps(data_flows).encode('utf-8'))
    producer.flush()

    msg_size = len(json.dumps(data_flows).encode('utf-8'))
    msg_iteration_size = msg_iteration_size + msg_size

    print("NOTIFICATION DATA network flow " + str(number_flow) + ": " + str(json.dumps(data_flows)) + "\n")
    print("NOTIFICATION TIMESTAMP network flow " + str(number_flow) + ": " + current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")

    number_flow += 1
    processed_count += 1
    now_time = time.perf_counter_ns() / 1e9
    if now_time - start_interval >= THROUGHPUT_INTERVAL:
        now_datetime = datetime.datetime.now(datetime.timezone.utc)
        throughput_records = processed_count / (now_time - start_interval) 
        throughput_bytes = msg_iteration_size / (now_time - start_interval)
        
        throughput_csv_data = [start_interval_datetime, now_datetime, throughput_records, throughput_bytes, now_time - start_interval]
        throughput_csv_writer.writerow(throughput_csv_data)
        throughput_performance_measurements_file.flush()

        number_flow = 1
        processed_count = 0
        msg_iteration_size = 0
        start_interval = now_time
        start_interval_datetime = now_datetime

    '''    
    stop_time = time.perf_counter_ns()
    stop_datetime = datetime.datetime.now(datetime.timezone.utc)
    exec_time = stop_time - start_time
    exec_times.append(exec_time)
    
    print(f"NOTIFICATIONS ITERATION TIME: {exec_time/1e6} ms\n")
    print(f"NOTIFICATIONS ITERATION MEAN TIME SO FAR: {(sum(exec_times)/len(exec_times))/1e6} ms\n")
    
    timeout = random.uniform(4.5, float(sys.argv[1]))
    system_uptime = system_uptime + int(timeout * 1000)
    print("Time sleep of: " + str(timeout) + " seconds \n")

    time.sleep(timeout)
    '''