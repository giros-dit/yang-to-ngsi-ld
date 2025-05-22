import os
import logging
import logging.config
import pdb
import json
import yaml
import time

#from kafka import KafkaConsumer

from flink_api import FlinkAPI

## -- BEGIN LOGGING CONFIGURATION -- ##

with open('logging.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)

## -- END LOGGING CONFIGURATION -- ##

## -- BEGIN CONSTANTS DECLARATION -- ##

# Flink Job Managers:
FLINK_MANAGER_URI = os.getenv("FLINK_MANAGER_URI", "http://flink-jobmanager:8081")

# Flink JAR files:
FLINK_JARS = ["netflow-driver-1.0.jar"]

## -- END CONSTANTS DECLARATION -- ##

## -- BEGIN AUXILIARY FUNCTIONS -- ##


## -- END AUXILIARY FUNCTIONS -- ##

exec_times = []

print("Hello, I am the NetFlow YANG converter")

'''
print("I will consume messages (NetFlow data records) from a Kafka topic named netflow-driver-output")

consumer = KafkaConsumer('netflow-driver-output', bootstrap_servers=['kafka:9092'], value_deserializer=lambda x: json.loads(x.decode('utf-8')))

print("I will process every single notification, parse them and normalize according the YANG model")
'''

print("Initializing the Apache Flink client to upload the NetFlow driver JAR executable and submit the Java app to translate NetFlow raw data to YANG-modelled data...")

# Init Flink REST API Client
flink_api = FlinkAPI(url=FLINK_MANAGER_URI,debug=False)

"""
Infinite loop that checks every 5 seconds
until Flink REST API becomes available.
"""
while True:
    if flink_api.checkFlinkHealth():
        logger.info(
            "Successfully connected to Flink REST API!")
        break
    else:
        logger.warning("Could not connect to Flink REST API. "
                        "Retrying in 5 seconds ...")
        time.sleep(5)
        continue

flink_jar_ids = []

for flink_jar in FLINK_JARS:

    _ = flink_api.uploadJar(flink_jar)

    dict_jars = flink_api.getFlinkAppJars()

    for file in dict_jars['files']:
        if file['name'] == flink_jar:
            flink_jar_ids.append(file['id'])
            break

for flink_jar_id in flink_jar_ids:
    if "netflow-driver" in flink_jar_id:
        flink_api.submitJob(jarId=flink_jar_id, programArg="kafka:9092,network-flows,netflow-driver-output")

print("Done!")

while True:
    print("Checking Apache Flink job overview...")
    
    job_overview = flink_api.getFlinkJobsOverview()
    print(f"Job overview: {job_overview}")

    time.sleep(5)