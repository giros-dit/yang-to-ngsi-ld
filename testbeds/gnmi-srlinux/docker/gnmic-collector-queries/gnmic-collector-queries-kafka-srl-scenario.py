import subprocess
from kafka import KafkaProducer
import time
import sys

while True:
    # Get Query RPC to get all the information about openconfig-interfaces YANG model from SRLinux routers:
    query = subprocess.run(["gnmic", "get", "--config", "gnmic-request-srl1.yaml"], capture_output=True, text=True)

    producer = KafkaProducer(bootstrap_servers=['kafka-remote:9094'])
    producer.send('interfaces-state-queries', value=query.stdout.strip().encode('utf-8'))
    producer.flush()

    query = subprocess.run(["gnmic", "get", "--config", "gnmic-request-srl2.yaml"], capture_output=True, text=True)

    producer = KafkaProducer(bootstrap_servers=['kafka-remote:9094'])
    producer.send('interfaces-state-queries', value=query.stdout.strip().encode('utf-8'))
    producer.flush()
    time.sleep(int(sys.argv[1]))

# Subscribe RPC to get all the counters information about openconfig-interfaces YANG model from SRLinux routers:
# subprocess.run(["gnmic", "subscribe", "--config", "gnmic-subs-srl-srl.yaml", "--target", "clab-telemetry-testbed-srl-srl-4hosts-r1"])
