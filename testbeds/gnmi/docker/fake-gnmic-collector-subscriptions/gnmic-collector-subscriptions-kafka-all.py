import sys
from kafka import KafkaProducer
import time
import random
import datetime
import json

exec_times = []

producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

with open('openconfig-cisco-xrv9-notification.json', 'r') as file:
    data_r1 = json.load(file)

while True:
    start_time = time.perf_counter_ns()
    start_datetime = datetime.datetime.now(datetime.timezone.utc)
    for i in range(0, 36):
        current_time = time.time_ns()
        current_datetime = datetime.datetime.now(datetime.timezone.utc)

        data_r1[0]['timestamp'] = current_time
        data_r1[0]['tags']['interface_name'] = "GigabitEthernet0/0/0/" + str(i)

        producer.send('interfaces-state-notifications', value=json.dumps(data_r1).encode('utf-8'))
        producer.flush()

        print("NOTIFICATION DATA R1 interface " + "GigabitEthernet0/0/0/" + str(i) + ": " + str(json.dumps(data_r1)) + "\n")
        print("NOTIFICATION TIMESTAMP R1 interface " + "GigabitEthernet0/0/0/" + str(i) + ": " + current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")

    stop_time = time.perf_counter_ns()
    stop_datetime = datetime.datetime.now(datetime.timezone.utc)
    exec_time = stop_time - start_time
    exec_times.append(exec_time)
    
    print(f"NOTIFICATIONS ITERATION TIME: {exec_time/1e6} ms\n")
    print(f"NOTIFICATIONS ITERATION MEAN TIME SO FAR: {(sum(exec_times)/len(exec_times))/1e6} ms\n")
    
    timeout = random.uniform(4.5, float(sys.argv[1]))
    print("Time sleep of: " + str(timeout) + " seconds \n")

    time.sleep(timeout)
