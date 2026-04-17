import subprocess
from kafka import KafkaProducer
import time
import sys

while True:
    # Get Query RPC to get all the information about srl_linux-network-instance YANG model from SRLinux routers:
    query = subprocess.run(["gnmic", "get", "--type", "state", "--config", "gnmic-request-srl1.yaml"], capture_output=True, text=True)

    producer = KafkaProducer(bootstrap_servers=['kafka:9092'])
    producer.send('routing-state-queries', value=query.stdout.strip().encode('utf-8'))
    producer.flush()

    query = subprocess.run(["gnmic", "get", "--type", "state", "--config", "gnmic-request-srl2.yaml"], capture_output=True, text=True)

    producer = KafkaProducer(bootstrap_servers=['kafka:9092'])
    producer.send('routing-state-queries', value=query.stdout.strip().encode('utf-8'))
    producer.flush()

    time.sleep(int(sys.argv[1]))