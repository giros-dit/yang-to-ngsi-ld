import sys
from kafka import KafkaProducer
import time
import random
import datetime
import json

exec_times = []

producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

with open('netflow-v9.json', 'r') as file:
    data_flows = json.load(file)

system_uptime = 774518
data_flows['netflow-v9:netflow']['export-packet']['count'] = 10
while True:
    start_time = time.perf_counter_ns()
    start_datetime = datetime.datetime.now(datetime.timezone.utc)
    for i in range(1, 11):
        current_time_s = time.time()
        current_time_ns = time.time_ns()
        current_datetime = datetime.datetime.now(datetime.timezone.utc)

        data_flows['netflow-v9:netflow']['export-packet']['unix-seconds'] = int(current_time_s)
        data_flows['netflow-v9:netflow']['export-packet']['system-uptime'] = system_uptime
        data_flows['netflow-v9:netflow']['collector-goflow2']['time-received'] = int(current_time_ns/1e3)
        data_flows['netflow-v9:netflow']['export-packet']['flow-data-record'][0]['flow-id'] = i

        producer.send('netflow-driver-output', value=json.dumps(data_flows).encode('utf-8'))
        producer.flush()

        print("NOTIFICATION DATA network flow " + str(i) + ": " + str(json.dumps(data_flows)) + "\n")
        print("NOTIFICATION TIMESTAMP network flow " + str(i) + ": " + current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")

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