import sys
from kafka import KafkaProducer
import random
import time
import datetime
import json

producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

with open('openconfig-cisco-xrv9-query-36ifaces.json', 'r') as file:
    data_r1 = json.load(file)

while True:
    current_time = time.time_ns()
    current_datetime = datetime.datetime.now(datetime.timezone.utc)

    data_r1[0]['timestamp'] = current_time
    data_r1[0]['time'] = str(current_datetime)

    producer.send('interfaces-state-queries', value=json.dumps(data_r1).encode('utf-8'))
    producer.flush()

    print("QUERY DATA R1: " + str(json.dumps(data_r1)) + "\n")
    print("QUERY TIMESTAMP R1: " + current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")

    timeout = random.uniform(100, float(sys.argv[1]))
    print("Time sleep of: " + str(timeout) + " seconds \n")

    time.sleep(timeout)