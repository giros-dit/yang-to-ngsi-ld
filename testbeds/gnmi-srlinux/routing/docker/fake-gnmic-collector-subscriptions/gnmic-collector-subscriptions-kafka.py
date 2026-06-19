import sys
from kafka import KafkaProducer
import time
import datetime
import json

producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

sample_files = [
    "routing-stats-icmp-mix.json",
    "routing-stats-icmp-total.json",
    "routing-stats-icmp-type.json",
    "routing-stats-ipv4-unicast.json",
    "routing-stats-ipv6-unicast.json",
    "routing-stats-ospf-sample1.json",
    "routing-stats-tcp.json",
    "routing-stats-udp.json"
]

sample_data = [
    json.load(open(f)) for f in sample_files
]

sample_index = 0

while True:

    data = sample_data[sample_index]

    current_time = time.time_ns()
    current_datetime = datetime.datetime.now(datetime.timezone.utc)

    for item in data:
        item['timestamp'] = current_time

    producer.send('routing-state-notifications', value=json.dumps(data).encode('utf-8'))
    producer.flush()

    print("NOTIFICATION FILE: " + str(sample_files[sample_index]))
    print("NOTIFICATION DATA: " + str(json.dumps(data)) + "\n")
    print("NOTIFICATION TIMESTAMP: " + current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
    
    sample_index = (sample_index + 1) % len(sample_files)

    time.sleep(int(sys.argv[1]))