import sys
from kafka import KafkaProducer
import time
import datetime
import json

producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

with open('openconfig-cisco-xrv9-query.json', 'r') as file:
    data_r1 = json.load(file)

with open('openconfig-arista-ceos-query.json', 'r') as file:
    data_r2 = json.load(file)

with open('openconfig-nokia-srl-query.json', 'r') as file:
    data_r3 = json.load(file)

while True:
    current_time = time.time_ns()
    current_datetime = datetime.datetime.now(datetime.timezone.utc)

    data_r1[0]['timestamp'] = current_time
    data_r1[0]['time'] = str(current_datetime)

    print("QUERY DATA R1: " + str(json.dumps(data_r1)) + "\n")
    print("QUERY TIMESTAMP R1: " + current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")

    producer.send('interfaces-state-queries', value=json.dumps(data_r1).encode('utf-8'))
    producer.flush()

    current_time = time.time_ns()
    current_datetime = datetime.datetime.now(datetime.timezone.utc)

    data_r2[0]['timestamp'] = current_time
    data_r2[0]['time'] = str(current_datetime)

    print("QUERY DATA R2: " + str(json.dumps(data_r2)) + "\n")
    print("QUERY TIMESTAMP R2: " + current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")

    producer.send('interfaces-state-queries', value=json.dumps(data_r2).encode('utf-8'))
    producer.flush()
    
    current_time = time.time_ns()
    current_datetime = datetime.datetime.now(datetime.timezone.utc)

    data_r3[0]['timestamp'] = current_time
    data_r3[0]['time'] = str(current_datetime)

    print("QUERY DATA R3: " + str(json.dumps(data_r3)) + "\n")
    print("QUERY TIMESTAMP R3: " + current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")

    producer.send('interfaces-state-queries', value=json.dumps(data_r3).encode('utf-8'))
    producer.flush()

    time.sleep(int(sys.argv[1]))