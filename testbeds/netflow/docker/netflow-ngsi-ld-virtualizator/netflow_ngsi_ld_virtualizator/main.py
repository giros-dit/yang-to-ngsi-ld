import logging
import os
import socket
from time import sleep
import time
from typing import Optional
from uuid import uuid4
from fastapi import FastAPI, Request, Response, status, HTTPException
from fastapi.responses import JSONResponse
import json
import csv
import gzip
import ngsi_ld_client
import ngsi_ld_models

from ngsi_ld_client.models.create_subscription_request import CreateSubscriptionRequest
from ngsi_ld_client.models.subscription_on_change import SubscriptionOnChange
from ngsi_ld_client.models.subscription_periodic import SubscriptionPeriodic
from ngsi_ld_client.models.create_csr_request import CreateCSRRequest
from ngsi_ld_client.models.registration_info import RegistrationInfo
from ngsi_ld_client.models.entity_info import EntityInfo
from ngsi_ld_client.models.entity_info_type import EntityInfoType
from ngsi_ld_client.models.notification_params import NotificationParams
from ngsi_ld_client.models.endpoint import Endpoint
from ngsi_ld_client.api_client import ApiClient as NGSILDClient
from ngsi_ld_client.configuration import Configuration as NGSILDConfiguration
from pydantic import ValidationError
from netflow_ngsi_ld_virtualizator.check_client import NGSILDHealthInfoClient
from netflow_ngsi_ld_virtualizator.context_client import ContextCatalogClient
from ngsi_ld_models.models.export_packet import ExportPacket
from ngsi_ld_models.models.export_packet_flow_data_record import ExportPacketFlowDataRecord
from netflow_ngsi_ld_virtualizator.candil_netflow_ngsi_ld_instantiator import ngsi_ld_instantiator, get_entity_class_object_by_type
from netflow_ngsi_ld_virtualizator.candil_netflow_json_parser import parse_netflow

#from datetime import datetime,timezone
import datetime
from dateutil import parser
import asyncio
import threading
import jinja2
from jinja2 import Template
import time
import numpy as np
import httpx
import snappy
from kafka import KafkaProducer, KafkaConsumer

from ngsi_ld_client.models.entity import Entity
from ngsi_ld_client.models.model_property import ModelProperty
from ngsi_ld_client.models.query_entity200_response_inner import QueryEntity200ResponseInner

delta_times = []

logger = logging.getLogger(__name__)

# Event to control the execution of the infinite loop
stop_event = asyncio.Event()
stop_event_kafka = asyncio.Event()

# Dictionary to maintain the threads of execution associated with each NGSI-LD NETCONF entity
subscription_threads = {}
kafka_consumer_threads = {}

# ncclient parameters
host = ""
port = ""
username = ""
password = ""
family = ""
hostKeyVerify = False
subscriptionMode = ""
period = 0

kafka_message = None
ngsi_ld_subscriptions = []

# NGSI-LD Context Broker
#BROKER_URI = os.getenv("BROKER_URI", "http://orion:1026/ngsi-ld/v1")
BROKER_URI = os.getenv("BROKER_URI", "http://scorpio:9090/ngsi-ld/v1")

# Context Catalog
CONTEXT_CATALOG_URI = os.getenv("CONTEXT_CATALOG_URI",
                                "http://context-catalog:8080/context.jsonld")

# Init NGSI-LD Client
configuration = NGSILDConfiguration(host=BROKER_URI)
configuration.debug = True
ngsi_ld = NGSILDClient(configuration=configuration)

all_context_data = None
all_context_registries = None

ngsi_ld_health_info_api = NGSILDHealthInfoClient(
    url="http://scorpio:9090",
    headers={"Accept": "application/json"},
    context="http://context-catalog:8080/context.jsonld")

context_client = ContextCatalogClient("http://context-catalog:8080")

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

ngsi_ld_api_instance_provision = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

ngsi_ld_api_instance_consumption = ngsi_ld_client.ContextInformationConsumptionApi(ngsi_ld)

ngsi_ld_api_instance_subscription = ngsi_ld_client.ContextInformationSubscriptionApi(ngsi_ld)

ngsi_ld_api_instance_csourceregistration = ngsi_ld_client.ContextSourceRegistrationApi(ngsi_ld)

    
# Init FastAPI server
app = FastAPI(
    title="NetFlow Virtualization API",
    version="1.0.0")

'''
Startup function for registering the network controller as NGSI-LD Context Source and for subscribing to the NGSI-LD Entity 
type called NETCONF that defines the NETCONF client parameters. In addition, this fuctions discover all the key-value pairs 
included within the context catalog microservice for declaring the NGSI-LD @context.
'''
@app.on_event("startup")
async def startup_event():
    global all_context_data
    global all_context_registries
    context_urls = context_client.fetch_data()
    if context_urls:
        context_client.search_context_urls(context_urls)
        all_context_data = context_client.search_context_data(context_urls)
        all_context_registries = context_client.store_metadata_registries_in_list(context_urls) #context_client.store_context_registries_in_list(context_urls)
    
    logger.info("Key and value for each context URL:")
    for key, value in all_context_data.items():
        logger.info(f"{key}: {value}")

    logger.info("Context registries:")
    for context_registry in all_context_registries:
        logger.info(context_registry)

    # Check if Scorpio API is up
    ngsi_ld_health_info_api.check_scorpio_status()

    # Check Scorpio build info
    ngsi_ld_health_info_api.check_scorpio_info()

    export_packet_entity_info = EntityInfo(
        type=EntityInfoType("ExportPacket")
    )

    flow_data_record_config_entity_info = EntityInfo(
        type=EntityInfoType("ExportPacketFlowDataRecord")
    )


    context_source_registration_info = RegistrationInfo(
        entities=[
           export_packet_entity_info,
           flow_data_record_config_entity_info
        ]
    )

    context_source_request = CreateCSRRequest(
        id="urn:ngsi-ld:ContextSource:{0}".format("NetFlow"),
        type="ContextSourceRegistration",
        description="Context Source Registration for entities ExportPacket and ExportPacketFlowDataRecord ",
        information=[
            context_source_registration_info
        ],
        endpoint="http://netflow-ngsi-ld-virtualizator:8089"
    )
    
    try:
        ngsi_ld_api_instance_csourceregistration.create_csr(create_csr_request=context_source_request)          
    except Exception as e:
        logger.exception("Exception when calling ContextSourceRegistrationApi->create_csr: %s\n" % e) 
 
'''
Function for triggering subscriptions with needed parameters.
'''
async def subscribe_operation(notification_endpoint: str, entity_type: str, entity_id: str, subscription_id: str, all_context_data: Optional[dict] = None, all_context_registries: Optional[list] = None, sysAttrs: Optional[bool] = False):
    # Each subscription will have its own stop event
    stop_event = asyncio.Event()

    # Save the event and thread in the global dictionary to control this subscription
    subscription_threads[subscription_id] = {"stop_event": stop_event, "task": None}

    #consumer = KafkaConsumer('netflow-driver-output', bootstrap_servers=['kafka:9092'], value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    
    # Run the receive notification function in a separate thread
    #notification_thread = threading.Thread(target=ngsi_ld_instantiator, args=(consumer))
    #notification_thread = threading.Thread(target=ngsi_ld_instantiator, args=(subscription_threads, subscription_id, sysAttrs))
    #notification_thread = threading.Thread(target=ngsi_ld_instantiator, args=(subscription_threads, subscription_id, sysAttrs, notification_endpoint, entity_type, entity_id))
    #subscription_threads[subscription_id]["thread"] = notification_thread
    #notification_thread.start()

    # Crea una tarea asíncrona para ejecutar ngsi_ld_instantiator
    subscription_threads[subscription_id]["task"] = asyncio.create_task(
        ngsi_ld_instantiator(
            subscription_threads,
            subscription_id,
            sysAttrs,
            notification_endpoint,
            entity_type,
            entity_id
        )
    )

    # Wait until the stop event is triggered
    await stop_event.wait()

    # Once the event is triggered, stop the thread
    #notification_thread.join()

    # Una vez que el evento sea activado, cancela la tarea
    subscription_threads[subscription_id]["task"].cancel()
    try:
        await subscription_threads[subscription_id]["task"]
    except asyncio.CancelledError:
        logger.info(f"Task for subscription {subscription_id} was cancelled.")

    logger.info(f"Stopped subscription for id {subscription_id}!")

async def subscribe_operation_old(notification_endpoint: str, entity_type: str, entity_id: str, subscription_id: str, all_context_data: Optional[dict] = None, all_context_registries: Optional[list] = None, sysAttrs: Optional[bool] = False):
    # Each subscription will have its own stop event
    stop_event = asyncio.Event()

    # Save the event and thread in the global dictionary to control this subscription
    subscription_threads[subscription_id] = {"stop_event": stop_event, "thread": None}

    #consumer = KafkaConsumer('netflow-driver-output', bootstrap_servers=['kafka:9092'], value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    
    # Run the receive notification function in a separate thread
    #notification_thread = threading.Thread(target=ngsi_ld_instantiator, args=(consumer))
    #notification_thread = threading.Thread(target=ngsi_ld_instantiator, args=(subscription_threads, subscription_id, sysAttrs))
    notification_thread = threading.Thread(target=ngsi_ld_instantiator, args=(subscription_threads, subscription_id, sysAttrs, notification_endpoint, entity_type, entity_id))
    subscription_threads[subscription_id]["thread"] = notification_thread
    notification_thread.start()

    # Wait until the stop event is triggered
    await stop_event.wait()

    # Once the event is triggered, stop the thread
    notification_thread.join()

    logger.info(f"Stopped subscription for id {subscription_id}!")


'''
Function for starting a Kafka Consumer for processing notifications coming from NETCONF Subcription RPC operations.
'''
async def listen_to_kafka_subscriptions(notification_endpoint, subscription_id, entity_type, entity_id = None, sysAttrs: Optional[bool] = False): 

    print("Hello, I am the JSON parser for NetFlow and the NGSI-LD instantiator")

    print("I will consume messages (NetFlow data records) from a Kafka topic named netflow-driver-output")

    logger.info(f"Starting new Kafka Consumer for {subscription_id}") 

    consumer = KafkaConsumer('netflow-driver-output', bootstrap_servers=['kafka:9092'], value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    stop_event_kafka = kafka_consumer_threads[subscription_id]["stop_event"]
    
    parsing_exec_times = []
    exec_times = []
   

    parsing_performance_measurements_file = open("/opt/netflow-ngsi-ld-virtualizator/netflow_ngsi_ld_virtualizator/performance_measurements_parsing.csv", "w", newline='')
    parsing_csv_writer = csv.writer(parsing_performance_measurements_file)
    parsing_csv_header = ["observed_at", "iteration_started_at", "iteration_finished_at", "processing_time_since_observed_at", 
                "iteration_execution_time", "mean_execution_time", "min_execution_time", "max_execution_time", "processed_notifications"]
    parsing_csv_writer.writerow(parsing_csv_header)

    performance_measurements_file = open("/opt/netflow-ngsi-ld-virtualizator/netflow_ngsi_ld_virtualizator/performance_measurements_instantiation.csv", "w", newline='')
    csv_writer = csv.writer(performance_measurements_file)
    csv_header = ["observed_at", "iteration_started_at", "iteration_finished_at", "processing_time_since_observed_at", 
                "iteration_execution_time", "mean_execution_time", "min_execution_time", "max_execution_time", "processed_notifications"]
    csv_writer.writerow(csv_header)
    limits = httpx.Limits(max_keepalive_connections=5, max_connections=10)
    timeout = httpx.Timeout(10.0, read=10.0, write=10.0)
    try:
        #async with httpx.AsyncClient(http2=True, limits=limits, timeout=timeout) as client:
        client = httpx.AsyncClient(http2=True, limits=limits, timeout=timeout)
        while not stop_event_kafka.is_set(): # True:

            for message in consumer:
                start_datetime = None
                time_parsing = None
                # if data acquisition
                # instantiation_start_datetime = datetime.datetime.now(datetime.timezone.utc)

                if stop_event_kafka.is_set():
                    break

                parsing_start_datetime = datetime.datetime.now(datetime.timezone.utc)
                    
                print("I have consumed a new notification! ")

                event_time, dict_buffers = parse_netflow(message, parsing_start_datetime)

                parsing_stop_datetime = datetime.datetime.now(datetime.timezone.utc)
                parsing_exec_time = (parsing_stop_datetime - parsing_start_datetime).total_seconds()
                parsing_exec_times.append(parsing_exec_time)
            
                print("I have parsed the JSON and created the associated NGSI-LD-compliant data structures/dictionary buffers")

                print("I will now create the NGSI-LD entities from the data structures/dictionary buffers")
                
                filtered_dict_buffers = []

                
                for dict_buffer in dict_buffers:
                    '''
                    if sysAttrs:
                            dict_buffer["createdAt"] = parsing_start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") 
                            dict_buffer["modifiedAt"] = parsing_start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") 

                            update_nested_keys(obj=dict_buffer, datetime=parsing_start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
                    '''
                    try:
                        entity = get_entity_class_object_by_type(dict_buffer)
                        if entity != None and dict_buffer['type'] == 'ExportPacketFlowDataRecord':
                            filtered_dict_buffers.append(dict_buffer)
                    except Exception as e:
                        logger.exception(f"Failed to validate entity: {e}")

                kafka_message_json = filtered_dict_buffers #json.loads(message.value.decode('utf-8'))    
                
                logging.info(f"Kafka message for {subscription_id} is: {kafka_message_json}")

                if entity_id is not None:
                    kafka_message = [obj for obj in kafka_message_json if obj.get("type") == entity_type and obj.get("id") == entity_id]
                else:
                    kafka_message = [obj for obj in kafka_message_json if obj.get("type") == entity_type]

                logging.info(f"Kafka message for {subscription_id} after filter is: {kafka_message}")

                if str(kafka_message) != "[]":
                    new_kafka_message = []
                    start_datetime = parsing_start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
                    observedAt = event_time
                    '''
                    for entity in kafka_message:
            
                        # if data acquisition
                        #if "time" in entity:
                        #    time_parsing = entity["time"]
                        #    del entity["time"]
                        #
                        if "createdAt" in entity:
                            start_datetime = entity["createdAt"]
                            break
                    
                    observedAt = get_observed_at(kafka_message)
                    ''' 

                    current_datetime = datetime.datetime.now(datetime.timezone.utc)
                    ngsi_ld_entity_datetime = current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

                    # Generates the notification id and the current date
                    notification_id = f"notification:{uuid4().int}"
                    notified_at = ngsi_ld_entity_datetime
                    for entity in kafka_message:
                        if sysAttrs: #if "createdAt" in entity:
                            entity["createdAt"] = ngsi_ld_entity_datetime
                            entity["modifiedAt"] = ngsi_ld_entity_datetime
                            update_nested_keys(obj=entity, datetime=ngsi_ld_entity_datetime)
                            new_kafka_message.append(entity)

                    # Create notification data
                    notification_data = {
                        "id": notification_id,
                        "type": "Notification",
                        "subscriptionId": subscription_id,
                        "notifiedAt": notified_at,
                        "data": new_kafka_message
                    }

                    logger.info(f"Notification data: {notification_data}")
                    
                    pre_http_post_datetime = datetime.datetime.now(datetime.timezone.utc)
                
                    compressed_notification_data = gzip.compress(json.dumps(notification_data).encode("utf-8"))
                    start = time.perf_counter()

                    # Send the notification to the endpoint specified in the subscription
                    try:
                        response = await client.post(
                            notification_endpoint,
                            content=compressed_notification_data,
                            headers={"Link": '<{0}>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"', "Accept": "application/json", "Content-Type": "application/json", "Content-Encoding": "gzip"}
                        )

                        response.raise_for_status()
                        end = time.perf_counter()
                        print(f"HTTP Request Latency: {end - start} seconds")
                        
                        if start_datetime != None:
                            stop_datetime = datetime.datetime.now(datetime.timezone.utc)
                            stop_datetime_format = stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
                            # if data acquisition
                            # exec_time = (stop_datetime - instantiation_start_datetime).total_seconds() + time_parsing
                            exec_time = (stop_datetime - datetime.datetime.strptime(start_datetime, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=datetime.timezone.utc)).total_seconds()
                            exec_times.append(exec_time)

                            print("--- PERFORMANCE MEASUREMENTS FOR PARSING ---\n")
                            print("NOTIFICATIONS PROCESSED SO FAR: " + str(len(parsing_exec_times)) + "\n")
                            print("NOTIFICATION EVENT TIME/OBSERVED AT: " + event_time + "\n")
                            print("ITERATION STARTED AT: " + parsing_start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
                            print("ITERATION FINISHED AT: " + parsing_stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
                            print(f"PARSER ITERATION EXECUTION TIME: {parsing_exec_time * 1e3} ms\n")
                            print(f"TOTAL PROCESSING TIME SO FAR SINCE NOTIFICATION EVENT TIME/OBSERVED AT: {(parsing_stop_datetime - parser.parse(event_time)).total_seconds() * 1e3} ms\n")
                            print(f"MEAN EXECUTION TIME SO FAR: {(sum(parsing_exec_times)/len(parsing_exec_times)) * 1e3} ms\n")
                            print(f"MIN EXECUTION TIME SO FAR: {min(parsing_exec_times) * 1e3} ms\n")
                            print(f"MAX EXECUTION TIME SO FAR: {max(parsing_exec_times) * 1e3} ms\n")
                            print("--- PERFORMANCE MEASUREMENTS FOR PARSING ---")
                            parsing_csv_data = [event_time, parsing_start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), parsing_stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                                str((parsing_stop_datetime - parser.parse(event_time)).total_seconds() * 1e3) + " ms",
                                str(parsing_exec_time  * 1e3) + " ms", str((sum(parsing_exec_times)/len(parsing_exec_times)) * 1e3) + " ms",
                                str(min(parsing_exec_times)  * 1e3) + " ms", str(max(parsing_exec_times) * 1e3) + " ms", str(len(parsing_exec_times))]
                            parsing_csv_writer.writerow(parsing_csv_data)
                            parsing_performance_measurements_file.flush()

                            logger.info("--- PERFORMANCE MEASUREMENTS FOR INSTANTIATION ---")
                            logger.info("NOTIFICATIONS PROCESSED SO FAR: " + str(len(exec_times)) + "\n")
                            if observedAt != None:
                                logger.info("NOTIFICATION EVENT TIME/OBSERVED AT: " + observedAt + "\n")
                                logger.info(f"TOTAL PROCESSING TIME SO FAR SINCE NOTIFICATION EVENT TIME/OBSERVED AT: {(stop_datetime - parser.parse(observedAt)).total_seconds() * 1e3} ms\n")
                            logger.info("NOTIFIED AT (CreatedAt and ModifiedAt parameters): " +  ngsi_ld_entity_datetime + "\n")
                            logger.info("ITERATION STARTED AT: " + start_datetime + "\n")
                            logger.info("PRE HTTP POST WAS AT: " + pre_http_post_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
                            logger.info("ITERATION FINISHED AT: " + stop_datetime_format + "\n")
                            logger.info(f"EXECUTION TIME: {exec_time * 1e3} ms\n")
                            mean_evaluation_time = sum(exec_times)/len(exec_times)
                            min_evaluation_time = min(exec_times)
                            max_evaluation_time = max(exec_times)
                            logger.info(f"MEAN EXECUTION TIME: {mean_evaluation_time * 1e3} ms\n")
                            logger.info(f"MIN EXECUTION TIME: {min_evaluation_time * 1e3} ms\n")
                            logger.info(f"MAX EXECUTION TIME VALUE: {max_evaluation_time * 1e3} ms\n")
                            logger.info("--- PERFORMANCE MEASUREMENTS FOR INSTANTIATION ---")
                            csv_data = [observedAt, start_datetime, stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), 
                                        str((stop_datetime - parser.parse(observedAt)).total_seconds() * 1e3) + " ms",
                                        str(exec_time * 1e3) + " ms", str((sum(exec_times)/len(exec_times)) * 1e3) + " ms",
                                        str(min(exec_times) * 1e3) + " ms", str(max(exec_times) * 1e3) + " ms", str(len(exec_times))]
                            csv_writer.writerow(csv_data)
                            performance_measurements_file.flush()

                    except httpx.ConnectError:
                        logger.info(f"Cannot connect to notification endpoint: {notification_endpoint}")
                        if "_" in subscription_id:
                            await delete_subscriptions(subscriptionId=str(subscription_id.split("_")[0]))
                        else:
                            await delete_subscriptions(subscriptionId=subscription_id)
                        raise HTTPException(status_code=503, detail=f"Cannot connect to notification endpoint: {notification_endpoint}")
                    except httpx.RequestError as e:
                        raise HTTPException(status_code=500, detail=f"Failed to send notification: {str(e)}")
                    except httpx.HTTPStatusError as e:
                        raise HTTPException(status_code=response.status_code, detail=f"Notification failed: {str(e)}")
                    
                    logger.info("Restarting HTTP client...")
                    await client.aclose() 
                    client = httpx.AsyncClient(http2=True, limits=limits, timeout=timeout) 
    finally:
        await client.aclose()
        consumer.close()
        performance_measurements_file.close()
        logging.info("Kafka Consumer closed!")

'''
Function for starting a Kafka Consumer for processing notifications coming from NETCONF Subcription RPC operations.
'''
async def listen_to_kafka_subscriptions_old(notification_endpoint, subscription_id, entity_type, entity_id = None):
    #consumer = KafkaConsumer('interfaces-state-subscriptions-dictionary-buffers', bootstrap_servers=['kafka:9092'], value_deserializer=lambda v: json.loads(v.decode('utf-8')))
    consumer = KafkaConsumer('netflow-subscriptions-dictionary-buffers', bootstrap_servers=['kafka:9092'])
    logger.info(f"Starting new Kafka Consumer for {subscription_id}") 
    stop_event_kafka = kafka_consumer_threads[subscription_id]["stop_event"]
    exec_times = []
    performance_measurements_file = open("/opt/netflow-ngsi-ld-virtualizator/netflow_ngsi_ld_virtualizator/performance_measurements_instantiation.csv", "w", newline='')
    csv_writer = csv.writer(performance_measurements_file)
    csv_header = ["observed_at", "iteration_started_at", "iteration_finished_at", "processing_time_since_observed_at", 
                "iteration_execution_time", "mean_execution_time", "min_execution_time", "max_execution_time", "processed_notifications"]
    csv_writer.writerow(csv_header)
    limits = httpx.Limits(max_keepalive_connections=5, max_connections=10)
    timeout = httpx.Timeout(10.0, read=10.0, write=10.0)
    try:
        #async with httpx.AsyncClient(http2=True, limits=limits, timeout=timeout) as client:
        client = httpx.AsyncClient(http2=True, limits=limits, timeout=timeout)
        while not stop_event_kafka.is_set(): # True:

            for message in consumer:
                start_datetime = None
                time_parsing = None
                # if data acquisition
                # instantiation_start_datetime = datetime.datetime.now(datetime.timezone.utc)

                if stop_event_kafka.is_set():
                    break

                kafka_message_json = json.loads(message.value.decode('utf-8'))    
                
                logging.info(f"Kafka message for {subscription_id} is: {kafka_message_json}")

                if entity_id is not None:
                    kafka_message = [obj for obj in kafka_message_json if obj.get("type") == entity_type and obj.get("id") == entity_id]
                else:
                    kafka_message = [obj for obj in kafka_message_json if obj.get("type") == entity_type]

                logging.info(f"Kafka message for {subscription_id} after filter is: {kafka_message}")

                if str(kafka_message) != "[]":
                    new_kafka_message = []
                    for entity in kafka_message:
            
                        ''' if data acquisition
                        if "time" in entity:
                            time_parsing = entity["time"]
                            del entity["time"]
                        '''
                        if "createdAt" in entity:
                            start_datetime = entity["createdAt"]
                            break

                    observedAt = get_observed_at(kafka_message)

                    current_datetime = datetime.datetime.now(datetime.timezone.utc)
                    ngsi_ld_entity_datetime = current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

                    # Generates the notification id and the current date
                    notification_id = f"notification:{uuid4().int}"
                    notified_at = ngsi_ld_entity_datetime
                    for entity in kafka_message:
                        if "createdAt" in entity:
                            entity["createdAt"] = ngsi_ld_entity_datetime
                            entity["modifiedAt"] = ngsi_ld_entity_datetime
                            update_nested_keys(obj=entity, datetime=ngsi_ld_entity_datetime)
                            new_kafka_message.append(entity)

                    # Create notification data
                    notification_data = {
                        "id": notification_id,
                        "type": "Notification",
                        "subscriptionId": subscription_id,
                        "notifiedAt": notified_at,
                        "data": kafka_message
                    }

                    logger.info(f"Notification data: {notification_data}")
                    
                    pre_http_post_datetime = datetime.datetime.now(datetime.timezone.utc)
                
                    compressed_notification_data = gzip.compress(json.dumps(notification_data).encode("utf-8"))
                    start = time.perf_counter()

                    # Send the notification to the endpoint specified in the subscription
                    try:
                        response = await client.post(
                            notification_endpoint,
                            content=compressed_notification_data,
                            headers={"Link": '<{0}>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"', "Accept": "application/json", "Content-Type": "application/json", "Content-Encoding": "gzip"}
                        )

                        response.raise_for_status()
                        end = time.perf_counter()
                        print(f"HTTP Request Latency: {end - start} seconds")
                        
                        if start_datetime != None:
                            stop_datetime = datetime.datetime.now(datetime.timezone.utc)
                            stop_datetime_format = stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
                            # if data acquisition
                            # exec_time = (stop_datetime - instantiation_start_datetime).total_seconds() + time_parsing
                            exec_time = (stop_datetime - datetime.datetime.strptime(start_datetime, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=datetime.timezone.utc)).total_seconds()
                            exec_times.append(exec_time)
                            logger.info("--- PERFORMANCE MEASUREMENTS ---")
                            logger.info("NOTIFICATIONS PROCESSED SO FAR: " + str(len(exec_times)) + "\n")
                            if observedAt != None:
                                logger.info("NOTIFICATION EVENT TIME/OBSERVED AT: " + observedAt + "\n")
                                logger.info(f"TOTAL PROCESSING TIME SO FAR SINCE NOTIFICATION EVENT TIME/OBSERVED AT: {(stop_datetime - parser.parse(observedAt)).total_seconds() * 1e3} ms\n")
                            logger.info("NOTIFIED AT (CreatedAt and ModifiedAt parameters): " +  ngsi_ld_entity_datetime + "\n")
                            logger.info("ITERATION STARTED AT: " + start_datetime + "\n")
                            logger.info("PRE HTTP POST WAS AT: " + pre_http_post_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
                            logger.info("ITERATION FINISHED AT: " + stop_datetime_format + "\n")
                            logger.info(f"EXECUTION TIME: {exec_time * 1e3} ms\n")
                            mean_evaluation_time = sum(exec_times)/len(exec_times)
                            min_evaluation_time = min(exec_times)
                            max_evaluation_time = max(exec_times)
                            logger.info(f"MEAN EXECUTION TIME: {mean_evaluation_time * 1e3} ms\n")
                            logger.info(f"MIN EXECUTION TIME: {min_evaluation_time * 1e3} ms\n")
                            logger.info(f"MAX EXECUTION TIME VALUE: {max_evaluation_time * 1e3} ms\n")
                            logger.info("--- PERFORMANCE MEASUREMENTS ---")
                            csv_data = [observedAt, start_datetime, stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), 
                                        str((stop_datetime - parser.parse(observedAt)).total_seconds() * 1e3) + " ms",
                                        str(exec_time * 1e3) + " ms", str((sum(exec_times)/len(exec_times)) * 1e3) + " ms",
                                        str(min(exec_times) * 1e3) + " ms", str(max(exec_times) * 1e3) + " ms", str(len(exec_times))]
                            csv_writer.writerow(csv_data)
                            performance_measurements_file.flush()

                    except httpx.ConnectError:
                        logger.info(f"Cannot connect to notification endpoint: {notification_endpoint}")
                        if "_" in subscription_id:
                            await delete_subscriptions(subscriptionId=str(subscription_id.split("_")[0]))
                        else:
                            await delete_subscriptions(subscriptionId=subscription_id)
                        raise HTTPException(status_code=503, detail=f"Cannot connect to notification endpoint: {notification_endpoint}")
                    except httpx.RequestError as e:
                        raise HTTPException(status_code=500, detail=f"Failed to send notification: {str(e)}")
                    except httpx.HTTPStatusError as e:
                        raise HTTPException(status_code=response.status_code, detail=f"Notification failed: {str(e)}")
                    
                    logger.info("Restarting HTTP client...")
                    await client.aclose() 
                    client = httpx.AsyncClient(http2=True, limits=limits, timeout=timeout) 
    finally:
        await client.aclose()
        consumer.close()
        performance_measurements_file.close()
        logging.info("Kafka Consumer closed!")

def update_nested_keys(obj, datetime):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, dict):
                value["createdAt"] = datetime
                value["modifiedAt"] = datetime
                update_nested_keys(value, datetime)
            elif isinstance(value, list):
                for item in value:
                    update_nested_keys(item, datetime)

def get_observed_at(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "observedAt":
                return value  
            if isinstance(value, (dict, list)):
                nested_result = get_observed_at(value)
                if nested_result is not None:
                    return nested_result
    elif isinstance(obj, list):
        for item in obj:
            nested_result = get_observed_at(item)
            if nested_result is not None:
                return nested_result
    return None 

'''
Function for running asynchronous threads to open Kafka consumers for processing notifications coming from NETCONF subscription RPC operations.
'''
def run_asyncio_in_thread(notification_endpoint, subscription_id, entity_type, entity_id = None, sysAttrs: Optional[bool] = False):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(listen_to_kafka_subscriptions(notification_endpoint, subscription_id, entity_type, entity_id, sysAttrs))

'''
Endpoint for deleting NGSI-LD subscriptions by its id. 
This endpoint triggers the clearing of previous subscription operations.
'''
@app.delete("/ngsi-ld/v1/subscriptions/{subscriptionId}")
async def delete_subscriptions(subscriptionId: str):
    global ngsi_ld_subscriptions
    subscription_match = False
    matched_threads_id = []
    try:

        if len(kafka_consumer_threads) == 0: #if len(subscription_threads) == 0:
            raise HTTPException(status_code=404, detail="Subscription not found.")

        for key in kafka_consumer_threads: #subscription_threads:
            if key.startswith(subscriptionId + "_") or key == subscriptionId:
                matched_threads_id.append(key)
                subscription_match = True

        if subscription_match == False:
            raise HTTPException(status_code=404, detail="Subscription not found.")

        for thread_id in matched_threads_id:
            # Check if there is already a subscription and Kafka Consumer associated with this entity and stop it
            if thread_id in kafka_consumer_threads: #if thread_id in subscription_threads and thread_id in kafka_consumer_threads:

                logger.info(f"Stopping Kafka consumer for {thread_id} ...") 

                kafka_consumer_threads[thread_id]["stop_event"].set()  
                del kafka_consumer_threads[thread_id]
                logger.info(f"Kafka Consumer {thread_id} stopped!")

                '''
                logger.info(f"Stopping subscription for {thread_id} ...")
                
                subscription_threads[thread_id]["stop_event"].set()  
                del subscription_threads[thread_id]
                logger.info(f"Subscription {thread_id} stopped!")
                '''

        for ngsi_ld_subscription in ngsi_ld_subscriptions:
            if ngsi_ld_subscription.get("id") == subscriptionId:
                ngsi_ld_subscriptions.remove(ngsi_ld_subscription)

        return Response(status_code=204)

    except HTTPException as e:
        logging.error(f"HTTPException: {e}")
        raise e 

    except ValueError as e:
        logging.error(f"ValueError: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
    
'''
Endpoint for subcribing to NGSI-LD entities. 
This endpoint triggers the subscription operation.
'''
@app.post("/ngsi-ld/v1/subscriptions")
async def post_subscriptions(subscription: dict):
    sysAttrs = False
    try:
        response =  JSONResponse(status_code=201, content={"message": "Subscription created!"})
        ngsi_ld_subscriptions.append(subscription)
        entities = subscription.get("entities", [])
        #watched_attributes = subscription.get("watchedAttributes", [])
        
        notification = subscription.get("notification", {})
        notification_endpoint = notification.get("endpoint", {}).get("uri")
        subscription_id = str(subscription.get("id"))

        if not notification_endpoint:
            raise HTTPException(status_code=400, detail="Notification endpoint URI is missing")

        if "sysAttrs" in notification:
            if notification.get("sysAttrs") == True:
                sysAttrs = True
            else:
                sysAttrs = False

        for entity in entities:
            entity_type = None
            entity_id = None
            if "type" in entity and "id" not in entity: 
                id = subscription_id
                find = discover_entity(entity["type"], all_context_registries)
                if find == False:
                    entity_type = entity["type"]
                    # Check if there is already subscription and Kafka Consumer associated with this entity and stop it
                    if subscription_id in subscription_threads and id in kafka_consumer_threads:
                        logger.info(f"Restarting subscription for {subscription_id} ...")
                        subscription_threads[subscription_id]["stop_event"].set()  
                        #await subscription_threads[subscription_id]["task"].join()
                        subscription_threads[subscription_id]["thread"].join() # Wait for the previous thread to finish
                        subscription_threads[subscription_id]["stop_event"].clear()
                        # Remove from the subscription thread dictionary
                        del subscription_threads[subscription_id]
                        logger.info(f"Subscription {subscription_id} stopped!")


                    # Create a new NETCONF Subscription RPC
                    logger.info(f"Starting new subscription for {id}")      
                    #asyncio.create_task(subscribe_operation(notification_endpoint=notification_endpoint, entity_type=entity_type, entity_id=None, subscription_id=subscription_id, all_context_data=all_context_data, all_context_registries=all_context_registries, sysAttrs=sysAttrs))
                    stop_event_kafka = threading.Event()
                    kafka_thread = threading.Thread(
                        target=run_asyncio_in_thread,
                        args=(notification_endpoint, id, entity_type, entity_id, sysAttrs),
                        daemon=True
                    )
                    
                    # Save the event and thread in the global dictionary to control this subscription
                    kafka_consumer_threads[id] = {"stop_event": stop_event_kafka, "thread": None}
                    kafka_consumer_threads[id]["thread"] = kafka_thread
                    kafka_thread.start()

            elif "id" in entity:
                id = subscription_id + "_" + str(entity["id"])
                find = discover_entity(entity["type"], all_context_registries)
                if find == False:
                    entity_type = entity["type"]
                    entity_id = entity["id"]
                    # Check if there is already a subscription and Kafka Consumer associated with this entity and stop it
                    if id in subscription_threads and id in kafka_consumer_threads:
                        logger.info(f"Restarting subscription for {id} ...")
                        subscription_threads[id]["stop_event"].set() 
                        #await subscription_threads[subscription_id]["task"]
                        subscription_threads[id]["thread"].join() # Wait for the previous thread to finish
                        subscription_threads[id]["stop_event"].clear()
                        # Remove from the subscription thread dictionary
                        del subscription_threads[id]
                        logger.info(f"Subscription {id} stopped!")

                    # Create a new NETCONF Subscription RPC
                    logger.info(f"Starting new subscription for {id}")
                    #asyncio.create_task(subscribe_operation(notification_endpoint=notification_endpoint, entity_type=entity_type, entity_id=entity_id, subscription_id=id, all_context_data=all_context_data, all_context_registries=all_context_registries, sysAttrs=sysAttrs))  
                    stop_event_kafka = threading.Event()
                    kafka_thread = threading.Thread(
                        target=run_asyncio_in_thread,
                        args=(notification_endpoint, id, entity_type, entity_id, sysAttrs),
                        daemon=True
                    )
                    
                    # Save the event and thread in the global dictionary to control this subscription
                    kafka_consumer_threads[id] = {"stop_event": stop_event_kafka, "thread": None}
                    kafka_consumer_threads[id]["thread"] = kafka_thread
                    kafka_thread.start()

            '''
            stop_event_kafka = threading.Event()
            kafka_thread = threading.Thread(
                target=run_asyncio_in_thread,
                args=(notification_endpoint, id, entity_type, entity_id),
                daemon=True
            )
            
            # Save the event and thread in the global dictionary to control this subscription
            kafka_consumer_threads[id] = {"stop_event": stop_event_kafka, "thread": None}
            kafka_consumer_threads[id]["thread"] = kafka_thread
            kafka_thread.start()
            '''
        return response

    except HTTPException as e:
        logging.error(f"HTTPException: {e}")
        raise e 
    
    except ValueError as e:
        logging.error(f"ValueError: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")

'''   
Endpoint for getting NGSI-LD subscriptions.
'''
@app.get("/ngsi-ld/v1/subscriptions")
async def get_subscriptions():
    global ngsi_ld_subscriptions
    try:
        if len(ngsi_ld_subscriptions) != 0:
            return JSONResponse(content=ngsi_ld_subscriptions, status_code=200, headers={"Content-Type": "application/json", "Link": '<{0}>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'.format(CONTEXT_CATALOG_URI)})
        else:
            return JSONResponse(content=[], status_code=200, headers={"Content-Type": "application/json", "Link": '<{0}>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'.format(CONTEXT_CATALOG_URI)})
    
    except HTTPException as e:
        logging.error(f"HTTPException: {e}")
        raise e 
    except ValueError as e:
        logging.error(f"ValueError: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")

'''   
Endpoint for getting NGSI-LD subscriptions by id.
'''
@app.get("/ngsi-ld/v1/subscriptions/{subscriptionId}")
async def get_subscription(subscriptionId: str):
    global ngsi_ld_subscriptions
    subscription_match = False
    try:
        if len(ngsi_ld_subscriptions) != 0:
            for ngsi_ld_subscription in ngsi_ld_subscriptions:
                if ngsi_ld_subscription.get("id") == subscriptionId:
                    subscription_match = True
                    return JSONResponse(content=ngsi_ld_subscription, status_code=200, headers={"Content-Type": "application/json", "Link": '<{0}>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'.format(CONTEXT_CATALOG_URI)})
            if subscription_match == False:
                raise HTTPException(status_code=404, detail={"type":"https://uri.etsi.org/ngsi-ld/errors/ResourceNotFound","title":"Resource not found.","detail":"subscription not found","status":404}, headers={"Content-Type": "application/json", "Link": '<{0}>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'.format(CONTEXT_CATALOG_URI)})
        else:
            return JSONResponse(content={"type":"https://uri.etsi.org/ngsi-ld/errors/ResourceNotFound","title":"Resource not found.","detail":"subscription not found","status":404}, status_code=404, headers={"Content-Type": "application/json", "Link": '<{0}>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'.format(CONTEXT_CATALOG_URI)})
    
    except HTTPException as e:
        logging.error(f"HTTPException: {e}")
        raise e 
    
    except ValueError as e:
        logging.error(f"ValueError: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
    
def discover_entity(entity_type: str, all_context_registries: Optional[list]) -> bool:
    
    find = False

    for context_registry in all_context_registries:
        if entity_type in context_registry["@context"].keys():
            find = True
            logger.info("Entity type " + entity_type + " founded!")

    if find == False:
        logger.info("Entity type " + entity_type + " not found!")

    return find