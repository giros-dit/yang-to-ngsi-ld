import os
import logging
import logging.config
import pdb
import json
import yaml
import time
import datetime
import csv

from kafka import KafkaConsumer, KafkaProducer

from dateutil import parser

from candil_openconfig_interfaces_json_parser_notifications import parse_gnmi_notification, update_nested_keys

import ngsi_ld_client

from ngsi_ld_models.models.interface import Interface
from ngsi_ld_models.models.interface_config import InterfaceConfig
from ngsi_ld_models.models.interface_state import InterfaceState
from ngsi_ld_models.models.interface_state_counters import InterfaceStateCounters

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
#BROKER_URI = os.getenv("BROKER_URI", "http://orion:1026/ngsi-ld/v1")

producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

# Context Catalog:
CONTEXT_CATALOG_URI = os.getenv("CONTEXT_CATALOG_URI", "http://context-catalog:8080/context.jsonld")

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

def upsert_ngsi_ld_entity(ngsi_ld, entity) -> bool:
    result = False
    
    api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

    entity_input = entity.to_dict()

    logger.info("Entity object representation: %s\n" % Entity.from_dict(entity_input))
    logger.info("QueryEntity200ResponseInner object representation: %s\n" % QueryEntity200ResponseInner.from_dict(entity_input))

    query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)

    entities_input = []

    entities_input.append(query_entity_input)

    total_size = sum(len(query_entity_input.model_dump_json().encode('utf-8')) for query_entity_input in entities_input)
    print(f"Tamaño exacto del JSON: {total_size} bytes")

    try:
        # Create NGSI-LD entities of type Interface and Sensor: POST /entityOperations/upsert
        api_response = api_instance.upsert_batch(query_entity200_response_inner=entities_input)
        #logger.info(api_response.to_dict())
        result = True
    except Exception as e:
        logger.exception("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)
        result = False

def get_entity_class_object_by_type(dict_buffer: dict):
    type = dict_buffer['type']
    if type == 'Interface':
        entity = Interface.from_dict(dict_buffer)
    elif type == 'InterfaceConfig':
        entity = InterfaceConfig.from_dict(dict_buffer)
    elif type == 'InterfaceState':
        entity = InterfaceState.from_dict(dict_buffer)
    elif type == 'InterfaceStateCounters':
        entity = InterfaceStateCounters.from_dict(dict_buffer)
    else:
        entity = None
    return entity

## -- END AUXILIARY FUNCTIONS -- ##

exec_times = []

parsing_exec_times = []

print("Hello, I am the JSON parser for gNMI notifications and the NGSI-LD instantiator")

print("I will consume messages (gNMI notifications) from a Kafka topic named interfaces-state-notifications")

consumer = KafkaConsumer('interfaces-state-notifications', bootstrap_servers=['kafka:9092'], value_deserializer=lambda x: json.loads(x.decode('utf-8')))

print("I will process every single notification, parse them and create/update NGSI-LD entities accordingly")
print("These entities will be uploaded to the NGSI-LD broker")

print("Initializing the NGSI-LD client...")

ngsi_ld = init_ngsi_ld_client()

print("Done!")

parsing_performance_measurements_file = open("performance_measurements_parsing.csv", "w", newline='')
parsing_csv_writer = csv.writer(parsing_performance_measurements_file)
parsing_csv_header = ["observed_at", "iteration_started_at", "iteration_finished_at", "processing_time_since_observed_at", 
              "iteration_execution_time", "mean_execution_time", "min_execution_time", "max_execution_time", "processed_notifications"]
parsing_csv_writer.writerow(parsing_csv_header)

while True:
    for message in consumer:
        start_time = time.perf_counter_ns()
        start_datetime = datetime.datetime.now(datetime.timezone.utc)
        
        print("I have consumed a new notification!")

        sysAttrs, event_time, dict_buffers = parse_gnmi_notification(message)
        
        filtered_dict_buffers = []
        for dict_buffer in dict_buffers:
            
            if sysAttrs == "True":
                dict_buffer["createdAt"] = start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") 
                dict_buffer["modifiedAt"] = start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") 

                update_nested_keys(obj=dict_buffer, datetime=start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
                
            try:
                entity = get_entity_class_object_by_type(dict_buffer)
                if entity != None:
                    filtered_dict_buffers.append(dict_buffer)
            except Exception as e:
                logger.exception(f"Failed to validate entity: {e}")

        parsing_stop_datetime = datetime.datetime.now(datetime.timezone.utc)
        parsing_exec_time = (parsing_stop_datetime - start_datetime).total_seconds()
        parsing_exec_times.append(parsing_exec_time)

        print("I have parsed the JSON and created the associated NGSI-LD-compliant data structures/dictionary buffers")

        print("I will now create the NGSI-LD entities from the data structures/dictionary buffers")

        producer.send('interface-statistics-dictionary-buffers', value=json.dumps(filtered_dict_buffers).encode('utf-8'))
        producer.flush()
        
        if event_time is not None:
            print("Iteration done! Waiting for the next notification...\n")

            print("--- PERFORMANCE MEASUREMENTS ---\n")
            print("NOTIFICATIONS PROCESSED SO FAR: " + str(len(parsing_exec_times)) + "\n")
            print("NOTIFICATION EVENT TIME/OBSERVED AT: " + event_time + "\n")
            print("ITERATION STARTED AT: " + start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
            print("PARSER ITERATION FINISHED AT: " + parsing_stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
            print(f"PARSER ITERATION EXECUTION TIME: {parsing_exec_time * 1e3} ms\n")
            print(f"TOTAL PROCESSING TIME SO FAR SINCE NOTIFICATION EVENT TIME/OBSERVED AT: {(parsing_stop_datetime - parser.parse(event_time)).total_seconds() * 1e3} ms\n")
            print(f"PARSER MEAN EXECUTION TIME SO FAR: {(sum(parsing_exec_times)/len(parsing_exec_times)) * 1e3} ms\n")
            print(f"PARSER MIN EXECUTION TIME SO FAR: {min(parsing_exec_times) * 1e3} ms\n")
            print(f"PARSER MAX EXECUTION TIME SO FAR: {max(parsing_exec_times) * 1e3} ms\n")
            print("--- PERFORMANCE MEASUREMENTS ---")

            parsing_csv_data = [event_time, start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), parsing_stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                        str((parsing_stop_datetime - parser.parse(event_time)).total_seconds() * 1e3) + " ms",
                        str(parsing_exec_time * 1e3) + " ms", str((sum(parsing_exec_times)/len(parsing_exec_times)) * 1e3) + " ms",
                        str(min(parsing_exec_times) * 1e3) + " ms", str(max(parsing_exec_times) * 1e3) + " ms", str(len(parsing_exec_times))]
            parsing_csv_writer.writerow(parsing_csv_data)
            parsing_performance_measurements_file.flush()

        print("Iteration done! Waiting for the next notification...\n")