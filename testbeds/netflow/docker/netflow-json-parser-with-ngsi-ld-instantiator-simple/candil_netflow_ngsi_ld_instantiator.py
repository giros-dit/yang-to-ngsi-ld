import os
import logging
import logging.config
import pdb
import json
import yaml
import time
import datetime
import csv

from kafka import KafkaConsumer

from dateutil import parser
from flink_api import FlinkAPI
from candil_netflow_json_parser import parse_netflow

import ngsi_ld_client

from ngsi_ld_models.models.collector_goflow2 import CollectorGoflow2
from ngsi_ld_models.models.export_packet import ExportPacket
from ngsi_ld_models.models.export_packet_flow_data_record import ExportPacketFlowDataRecord
from ngsi_ld_models.models.export_packet_flow_data_record_vlan import ExportPacketFlowDataRecordVlan
from ngsi_ld_models.models.export_packet_flow_data_record_bgp import ExportPacketFlowDataRecordBgp
from ngsi_ld_models.models.export_packet_flow_data_record_mpls import ExportPacketFlowDataRecordMpls
from ngsi_ld_models.models.export_packet_flow_data_record_ipv4 import ExportPacketFlowDataRecordIpv4
from ngsi_ld_models.models.export_packet_flow_data_record_ipv6 import ExportPacketFlowDataRecordIpv6

from ngsi_ld_client.models.entity import Entity
from ngsi_ld_client.models.query_entity200_response_inner import QueryEntity200ResponseInner

from ngsi_ld_client.api_client import ApiClient as NGSILDClient
from ngsi_ld_client.configuration import Configuration as NGSILDConfiguration
from ngsi_ld_client.exceptions import ApiException
## -- BEGIN LOGGING CONFIGURATION -- ##

with open('logging.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)

## -- END LOGGING CONFIGURATION -- ##

## -- BEGIN CONSTANTS DECLARATION -- ##

# NGSI-LD Context Broker:
BROKER_URI = os.getenv("BROKER_URI", "http://scorpio:9090/ngsi-ld/v1")

# Context Catalog:
CONTEXT_CATALOG_URI = os.getenv("CONTEXT_CATALOG_URI", "http://context-catalog:8080/context.jsonld")


# Flink Job Managers:
FLINK_MANAGER_URI = os.getenv("FLINK_MANAGER_URI", "http://flink-jobmanager:8081")

# Flink JAR files:
FLINK_JARS = ["netflow-driver-1.0.jar"]

## -- END CONSTANTS DECLARATION -- ##

## -- BEGIN AUXILIARY FUNCTIONS -- ##

def init_ngsi_ld_client():
    configuration = NGSILDConfiguration(host=BROKER_URI)
    configuration.debug = True
    ngsi_ld = NGSILDClient(configuration=configuration)

    ngsi_ld.set_default_header(
        header_name="Link",
        header_value='<{0}>; '
                    'rel="http://www.w3.org/ns/json-ld#context"; '
                    'type="application/ld+json"'.format(CONTEXT_CATALOG_URI)
    )

    ngsi_ld.set_default_header(
        header_name="Accept",
        header_value="application/json"
    )

    return ngsi_ld

def create_ngsi_ld_entity(ngsi_ld, entity) -> bool:
    result = False
    
    api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

    entity_input = entity.to_dict()

    logger.info("Entity object representation: %s\n" % Entity.from_dict(entity_input))
    logger.info("QueryEntity200ResponseInner object representation: %s\n" % QueryEntity200ResponseInner.from_dict(entity_input))

    query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)

    try:
        # Create NGSI-LD entity of type Sensor: POST /entities
        api_response = api_instance.create_entity(query_entity200_response_inner=query_entity_input)
        #logger.info(api_response.to_dict())
        result = True
    except Exception as e:
        logger.exception("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)
        result = False

    return result

def retrieve_ngsi_ld_entity(ngsi_ld, entity_id: str) -> bool:
    result = False

    api_instance = ngsi_ld_client.ContextInformationConsumptionApi(ngsi_ld)

    try:
        # Retrieve NGSI-LD Entity by id: GET /entities/{entityId}
        api_response = api_instance.retrieve_entity(entity_id)
        #logger.info(api_response.to_dict())
        result = True
    except Exception as e:
        logger.exception("Exception when calling ContextInformationConsumptionApi->retrieve_entity: %s\n" % e)
        result = False
    
    return result

def update_ngsi_ld_entity(ngsi_ld, entity_id: str, entity) -> bool:
    result = False

    api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

    entity_input = entity.to_dict()

    #logger.info("Entity object representation: %s\n" % Entity.from_dict(entity_input))

    try:
        # Update NGSI-LD Entity by id: PATCH /entities/{entityId}/attrs
        api_response = api_instance.update_entity(entity_id, entity=Entity.from_dict(entity_input))
        #logger.info(api_response.to_dict())
        result = True
    except Exception as e:
        logger.exception("Exception when calling ContextInformationProvisionApi->update_entity: %s\n" % e)
        result = False

    return result

def batch_upsert_ngsi_ld_entities(ngsi_ld, dict_buffers) -> bool:
    result = False
    
    api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

    query_entity_inputs = []

    test_start_time = time.perf_counter_ns()
    test_start_datetime = datetime.datetime.now(datetime.timezone.utc)
    
    for dict_buffer in dict_buffers:
        #type = dict_buffer['type']
        #if type != 'Interface':
        try:
            entity = get_entity_class_object_by_type(dict_buffer)
            entity_input = entity.to_dict()
            query_entity_inputs.append(QueryEntity200ResponseInner.from_dict(entity_input))
        except Exception as e:
            logger.exception(f"Failed to validate entity: {e}")
        #entity_input = entity.to_dict()
        ##logger.info("Entity object representation: %s\n" % Entity.from_dict(entity_input))
        ##logger.info("QueryEntity200ResponseInner object representation: %s\n" % QueryEntity200ResponseInner.from_dict(entity_input))
        #query_entity_inputs.append(QueryEntity200ResponseInner.from_dict(entity_input))

    test_stop_time = time.perf_counter_ns()
    test_stop_datetime = datetime.datetime.now(datetime.timezone.utc)
    test_exec_time = test_stop_time - test_start_time
    print("UPSERT ITERATION PHASE 1 STARTED AT: " + test_start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
    print("UPSERT ITERATION PHASE 1 FINISHED AT: " + test_stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
    print(f"UPSERT ITERATION PHASE 1 EXECUTION TIME: {test_exec_time/1e6} ms\n")
    try:
        # Create NGSI-LD entities of type Interface: POST /entityOperations/upsert
        test_start_time = time.perf_counter_ns()
        test_start_datetime = datetime.datetime.now(datetime.timezone.utc)
        api_response = api_instance.upsert_batch(query_entity200_response_inner=query_entity_inputs)
        test_stop_time = time.perf_counter_ns()
        test_stop_datetime = datetime.datetime.now(datetime.timezone.utc)
        test_exec_time = test_stop_time - test_start_time
        print("UPSERT ITERATION PHASE 2 STARTED AT: " + test_start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
        print("UPSERT ITERATION PHASE 2 FINISHED AT: " + test_stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
        print(f"UPSERT ITERATION PHASE 2 EXECUTION TIME: {test_exec_time/1e6} ms\n")
        #logger.info(api_response.to_dict())
        result = True
    except Exception as e:
        logger.exception("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)
        result = False 

def get_entity_class_object_by_type(dict_buffer: dict):
    type = dict_buffer['type']
    if type == 'CollectorGoflow2':
        entity = CollectorGoflow2.from_dict(dict_buffer)
    elif type == 'ExportPacket':
        entity = ExportPacket.from_dict(dict_buffer)
    elif type == 'ExportPacketFlowDataRecord':
        entity = ExportPacketFlowDataRecord.from_dict(dict_buffer)
    elif type == 'ExportPacketFlowDataRecordIpv4':
        entity = ExportPacketFlowDataRecordIpv4.from_dict(dict_buffer)
    elif type == 'ExportPacketFlowDataRecordIpv6':
        entity = ExportPacketFlowDataRecordIpv6.from_dict(dict_buffer)    
    elif type == 'ExportPacketFlowDataRecordMpls':
        entity = ExportPacketFlowDataRecordMpls.from_dict(dict_buffer)    
    elif type == 'ExportPacketFlowDataRecordBgp':
        entity = ExportPacketFlowDataRecordBgp.from_dict(dict_buffer)   
    elif type == 'ExportPacketFlowDataRecordVlan':
        entity = ExportPacketFlowDataRecordVlan.from_dict(dict_buffer)    
    else:
        entity = None
    return entity

## -- END AUXILIARY FUNCTIONS -- ##

exec_times = []

parsing_exec_times = []

print("Hello, I am the JSON parser for NetFlow and the NGSI-LD instantiator")

print("I will consume messages (NetFlow data records) from a Kafka topic named netflow-driver-output")

consumer = KafkaConsumer('netflow-driver-output', bootstrap_servers=['kafka:9092'], value_deserializer=lambda x: json.loads(x.decode('utf-8')))

print("I will process every single notification, parse them and create/update NGSI-LD entities accordingly")
print("These entities will be uploaded to the NGSI-LD broker")

print("Initializing the NGSI-LD client...")

ngsi_ld = init_ngsi_ld_client()

print("Done!")

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

performance_measurements_file = open("performance_measurements_instantiation.csv", "w", newline='')
csv_writer = csv.writer(performance_measurements_file)
csv_header = ["observed_at", "iteration_started_at", "iteration_finished_at", "processing_time_since_observed_at", 
              "iteration_execution_time", "mean_execution_time", "min_execution_time", "max_execution_time", "processed_notifications"]
csv_writer.writerow(csv_header)

parsing_performance_measurements_file = open("performance_measurements_parsing.csv", "w", newline='')
parsing_csv_writer = csv.writer(parsing_performance_measurements_file)
parsing_csv_header = ["observed_at", "iteration_started_at", "iteration_finished_at", "processing_time_since_observed_at", 
              "iteration_execution_time", "mean_execution_time", "min_execution_time", "max_execution_time", "processed_notifications"]
parsing_csv_writer.writerow(parsing_csv_header)

while True:
    for message in consumer:
        start_time = time.perf_counter_ns()
        start_datetime = datetime.datetime.now(datetime.timezone.utc)
        
        print("I have consumed a new notification! ")

        event_time, dict_buffers = parse_netflow(message)
       
        parsing_stop_time = time.perf_counter_ns()
        parsing_stop_datetime = datetime.datetime.now(datetime.timezone.utc)
        parsing_exec_time = parsing_stop_time - start_time
        parsing_exec_times.append(parsing_exec_time)

        print("I have parsed the JSON and created the associated NGSI-LD-compliant data structures/dictionary buffers")

        print("I will now create the NGSI-LD entities from the data structures/dictionary buffers")

        '''
        for dict_buffer in dict_buffers:
            entity_id = dict_buffer['id']
            
            entity = get_entity_class_object_by_type(dict_buffer)

            if entity != None:

                print("Dictionary buffer contains information for entity " + entity_id)

                exists = retrieve_ngsi_ld_entity(ngsi_ld, entity_id)
                if exists == False:
                    print("Entity " + entity_id + " DOES NOT EXIST. Trying to create it...")
                    created = create_ngsi_ld_entity(ngsi_ld, entity)
                    if created == False:
                        print("Entity " + entity_id + " COULD NOT BE CREATED")
                    else:
                        print("Entity " + entity_id + " WAS SUCCESSFULLY CREATED")
                else:
                    print("Entity " + entity_id + " DOES EXIST. Trying to update it...")
                    updated = update_ngsi_ld_entity(ngsi_ld, entity_id, entity)
                    if updated == False:
                        print("Entity " + entity_id + " COULD NOT BE UPDATED")
                    else:
                        print("Entity " + entity_id + " WAS SUCCESSFULLY UPDATED")
        '''

        upserted = batch_upsert_ngsi_ld_entities(ngsi_ld, dict_buffers)
        if upserted == False:
            print("ENTITIES COULD NOT BE UPSERTED")
        else:
            print("ENTITIES WAS SUCCESSFULLY UPSERTED")

        if event_time is not None:
            stop_time = time.perf_counter_ns()
            stop_datetime = datetime.datetime.now(datetime.timezone.utc)
            
            exec_time = stop_time - start_time
            exec_times.append(exec_time)

            print("Iteration done! Waiting for the next notification...\n")

            print("--- PERFORMANCE MEASUREMENTS ---\n")
            print("NOTIFICATIONS PROCESSED SO FAR: " + str(len(exec_times)) + "\n")
            print("NOTIFICATION EVENT TIME/OBSERVED AT: " + event_time + "\n")
            print("ITERATION STARTED AT: " + start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
            print("PARSER ITERATION FINISHED AT: " + parsing_stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
            print("PARSER AND INSTANTIATION ITERATION FINISHED AT: " + stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
            print(f"PARSER ITERATION EXECUTION TIME: {parsing_exec_time/1e6} ms\n")
            print(f"PARSER AND INSTANTIATION ITERATION EXECUTION TIME: {exec_time/1e6} ms\n")
            #print("ITERATION FINISHED AT: " + stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
            print(f"TOTAL PROCESSING TIME SO FAR SINCE NOTIFICATION EVENT TIME/OBSERVED AT: {(stop_datetime - parser.parse(event_time)).total_seconds() * 1e3} ms\n")
            #print(f"ITERATION EXECUTION TIME: {exec_time/1e6} ms\n")
            print(f"PARSER MEAN EXECUTION TIME SO FAR: {(sum(parsing_exec_times)/len(parsing_exec_times))/1e6} ms\n")
            print(f"PARSER MIN EXECUTION TIME SO FAR: {min(parsing_exec_times)/1e6} ms\n")
            print(f"PARSER MAX EXECUTION TIME SO FAR: {max(parsing_exec_times)/1e6} ms\n")
            print(f"PARSER AND INSTANTIATION MEAN EXECUTION TIME SO FAR: {(sum(exec_times)/len(exec_times))/1e6} ms\n")
            print(f"PARSER AND INSTANTIATION MIN EXECUTION TIME SO FAR: {min(exec_times)/1e6} ms\n")
            print(f"PARSER AND INSTANTIATION MAX EXECUTION TIME SO FAR: {max(exec_times)/1e6} ms\n")
            print("--- PERFORMANCE MEASUREMENTS ---")

            csv_data = [event_time, start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                        str((stop_datetime - parser.parse(event_time)).total_seconds() * 1e3) + " ms",
                        str(exec_time/1e6) + " ms", str((sum(exec_times)/len(exec_times))/1e6) + " ms",
                        str(min(exec_times)/1e6) + " ms", str(max(exec_times)/1e6) + " ms", str(len(exec_times))]
            csv_writer.writerow(csv_data)
            performance_measurements_file.flush()

            parsing_csv_data = [event_time, start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), parsing_stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                        str((stop_datetime - parser.parse(event_time)).total_seconds() * 1e3) + " ms",
                        str(parsing_exec_time/1e6) + " ms", str((sum(parsing_exec_times)/len(parsing_exec_times))/1e6) + " ms",
                        str(min(parsing_exec_times)/1e6) + " ms", str(max(parsing_exec_times)/1e6) + " ms", str(len(parsing_exec_times))]
            parsing_csv_writer.writerow(parsing_csv_data)
            parsing_performance_measurements_file.flush()