import sys
from kafka import KafkaProducer
import time
import datetime
import json

producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

with open('openconfig-cisco-xrv9-notification.json', 'r') as file:
    data_r1 = json.load(file)

with open('openconfig-arista-ceos-notification.json', 'r') as file:
    data_r2 = json.load(file)

with open('openconfig-nokia-srl-notification.json', 'r') as file:
    data_r3 = json.load(file)

while True:
    current_time = time.time_ns()
    current_datetime = datetime.datetime.now(datetime.timezone.utc)

    data_r1[0]['timestamp'] = current_time

    producer.send('interfaces-state-notifications', value=json.dumps(data_r1).encode('utf-8'))
    producer.flush()

    print("NOTIFICATION DATA R1: " + str(json.dumps(data_r1)) + "\n")
    print("NOTIFICATION TIMESTAMP R1: " + current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")

    current_time = time.time_ns()
    current_datetime = datetime.datetime.now(datetime.timezone.utc)

    data_r2[0]['timestamp'] = current_time

    producer.send('interfaces-state-notifications', value=json.dumps(data_r2).encode('utf-8'))
    producer.flush()

    print("NOTIFICATION DATA R2: " + str(json.dumps(data_r2)) + "\n")
    print("NOTIFICATION TIMESTAMP R2: " + current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")

    current_time = time.time_ns()
    current_datetime = datetime.datetime.now(datetime.timezone.utc)

    data_r3[0]['timestamp'] = current_time

    producer.send('interfaces-state-notifications', value=json.dumps(data_r3).encode('utf-8'))
    producer.flush()

    print("NOTIFICATION DATA R3: " + str(json.dumps(data_r3)) + "\n")
    print("NOTIFICATION TIMESTAMP R3: " + current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
    
    time.sleep(int(sys.argv[1]))