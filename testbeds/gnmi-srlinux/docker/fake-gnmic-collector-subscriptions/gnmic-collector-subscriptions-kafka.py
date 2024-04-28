import sys
from kafka import KafkaProducer
import time
import datetime
import json

producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

with open('srl-nokia-notification.json', 'r') as file:
    data = json.load(file)

while True:
    current_time = time.time_ns()
    current_datetime = datetime.datetime.now(datetime.timezone.utc)

    data[0]['timestamp'] = current_time

    print("NOTIFICATION DATA: " + str(json.dumps(data)) + "\n")
    print("NOTIFICATION TIMESTAMP: " + current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")

    producer.send('interfaces-state-notifications', value=json.dumps(data).encode('utf-8'))
    producer.flush()
    
    time.sleep(int(sys.argv[1]))