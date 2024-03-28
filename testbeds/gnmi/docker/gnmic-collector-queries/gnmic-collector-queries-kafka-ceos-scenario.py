import subprocess
from kafka import KafkaProducer
import time
import sys

while True:
    # Get Query RPC to get all the information about openconfig-interfaces YANG model from cEOS routers:
    query = subprocess.run(["gnmic", "get", "--config", "gnmic-request-ceos1.yaml"], capture_output=True, text=True)

    producer = KafkaProducer(bootstrap_servers=['kafka:9092'])
    producer.send('interfaces-state-queries', value=query.stdout.strip().encode('utf-8'))
    producer.flush()

    query = subprocess.run(["gnmic", "get", "--config", "gnmic-request-ceos2.yaml"], capture_output=True, text=True)

    producer = KafkaProducer(bootstrap_servers=['kafka:9092'])
    producer.send('interfaces-state-queries', value=query.stdout.strip().encode('utf-8'))
    producer.flush()
    time.sleep(int(sys.argv[1]))

# Subscribe RPC to get all the counters information about openconfig-interfaces YANG model from cEOS routers:
# subprocess.run(["gnmic", "subscribe", "--config", "gnmic-subs-ceos-ceos.yaml", "--target", "ceos1"])
