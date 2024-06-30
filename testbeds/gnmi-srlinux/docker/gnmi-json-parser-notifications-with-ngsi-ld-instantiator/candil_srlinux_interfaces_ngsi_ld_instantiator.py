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

from candil_srlinux_interfaces_json_parser_notifications import parse_gnmi_notification

import ngsi_ld_client

from ngsi_ld_models.models.interface import Interface
from ngsi_ld_models.models.interface_statistics import InterfaceStatistics

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

def get_entity_class_object_by_type(dict_buffer: dict):
    type = dict_buffer['type']
    if type == 'Interface':
        entity = Interface.from_dict(dict_buffer)
    elif type == 'InterfaceStatistics':
        entity = InterfaceStatistics.from_dict(dict_buffer)
    else:
        entity = None
    return entity

## -- END AUXILIARY FUNCTIONS -- ##

exec_times = []

print("Hello, I am the JSON parser for gNMI notifications and the NGSI-LD instantiator")

print("I will consume messages (gNMI notifications) from a Kafka topic named interfaces-state-notifications")

consumer = KafkaConsumer('interfaces-state-notifications', bootstrap_servers=['kafka:9092'], value_deserializer=lambda x: json.loads(x.decode('utf-8')))

print("I will process every single notification, parse them and create/update NGSI-LD entities accordingly")
print("These entities will be uploaded to the NGSI-LD broker")

print("Initializing the NGSI-LD client...")

ngsi_ld = init_ngsi_ld_client()

print("Done!")

performance_measurements_file = open("performance_measurements.csv", "w", newline='')
csv_writer = csv.writer(performance_measurements_file)
csv_header = ["observed_at", "iteration_started_at", "iteration_finished_at", "processing_time_since_observed_at", 
              "iteration_execution_time", "mean_execution_time", "min_execution_time", "max_execution_time", "processed_notifications"]
csv_writer.writerow(csv_header)

while True:
    for message in consumer:
        start_time = time.perf_counter_ns()
        start_datetime = datetime.datetime.now(datetime.timezone.utc)
        
        print("I have consumed a new notification!")

        event_time, dict_buffers = parse_gnmi_notification(message)

        print("I have parsed the JSON and created the associated NGSI-LD-compliant data structures/dictionary buffers")

        print("I will now create the NGSI-LD entities from the data structures/dictionary buffers")

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
        
        stop_time = time.perf_counter_ns()
        stop_datetime = datetime.datetime.now(datetime.timezone.utc)
        
        exec_time = stop_time - start_time
        exec_times.append(exec_time)

        print("Iteration done! Waiting for the next notification...\n")

        print("--- PERFORMANCE MEASUREMENTS ---\n")
        print("NOTIFICATIONS PROCESSED SO FAR: " + str(len(exec_times)) + "\n")
        print("NOTIFICATION EVENT TIME/OBSERVED AT: " + event_time + "\n")
        print("ITERATION STARTED AT: " + start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
        print("ITERATION FINISHED AT: " + stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
        print(f"TOTAL PROCESSING TIME SO FAR SINCE NOTIFICATION EVENT TIME/OBSERVED AT: {(stop_datetime - parser.parse(event_time)).total_seconds() * 1e3} ms\n")
        print(f"ITERATION EXECUTION TIME: {exec_time/1e6} ms\n")
        print(f"MEAN EXECUTION TIME SO FAR: {(sum(exec_times)/len(exec_times))/1e6} ms\n")
        print(f"MIN EXECUTION TIME SO FAR: {min(exec_times)/1e6} ms\n")
        print(f"MAX EXECUTION TIME SO FAR: {max(exec_times)/1e6} ms\n")
        print("--- PERFORMANCE MEASUREMENTS ---")

        csv_data = [event_time, start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                    str((stop_datetime - parser.parse(event_time)).total_seconds() * 1e3) + " ms",
                    str(exec_time/1e6) + " ms", str((sum(exec_times)/len(exec_times))/1e6) + " ms",
                    str(min(exec_times)/1e6) + " ms", str(max(exec_times)/1e6) + " ms", str(len(exec_times))]
        csv_writer.writerow(csv_data)
        performance_measurements_file.flush()