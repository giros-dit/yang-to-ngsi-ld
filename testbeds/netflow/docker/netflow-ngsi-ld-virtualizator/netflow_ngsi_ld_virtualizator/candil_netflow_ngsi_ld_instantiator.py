import os
import logging
import logging.config
import pdb
import json
from fastapi import HTTPException
import yaml
import time
import datetime
import csv
import gzip
import httpx
from uuid import uuid4
from kafka import KafkaConsumer, KafkaProducer

from dateutil import parser
from netflow_ngsi_ld_virtualizator.candil_netflow_json_parser import parse_netflow
#from netflow_ngsi_ld_virtualizator.main import delete_subscriptions
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

'''
with open('logging.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)'
'''
logger = logging.getLogger(__name__)

## -- END LOGGING CONFIGURATION -- ##

## -- BEGIN CONSTANTS DECLARATION -- ##

# NGSI-LD Context Broker:
BROKER_URI = os.getenv("BROKER_URI", "http://scorpio:9090/ngsi-ld/v1")

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

def update_nested_keys_observedAt(obj, datetime):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, dict):
                value["observedAt"] = datetime
                update_nested_keys(value, datetime)
            elif isinstance(value, list):
                for item in value:
                    update_nested_keys(item, datetime)

async def ngsi_ld_instantiator(subscription_threads, subscription_id, sysAttrs, notification_endpoint, entity_type, entity_id):

    exec_times = []
    parsing_exec_times = []
    instantiation_exec_times = []

    print("Hello, I am the JSON parser for NetFlow and the NGSI-LD instantiator")

    print("I will consume messages (NetFlow data records) from a Kafka topic named netflow-driver-output")

    consumer = KafkaConsumer('netflow-driver-output', bootstrap_servers=['kafka:9092'], value_deserializer=lambda x: json.loads(x.decode('utf-8')))

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

    performance_measurements_file = open("/opt/netflow-ngsi-ld-virtualizator/netflow_ngsi_ld_virtualizator/performance_measurements_instantiation.csv", "w", newline='')
    csv_writer = csv.writer(performance_measurements_file)
    csv_header = ["observed_at", "iteration_started_at", "iteration_finished_at", "processing_time_since_observed_at", 
                "iteration_execution_time", "mean_execution_time", "min_execution_time", "max_execution_time", "processed_notifications"]
    csv_writer.writerow(csv_header)
    limits = httpx.Limits(max_keepalive_connections=5, max_connections=10)
    timeout = httpx.Timeout(10.0, read=10.0, write=10.0)

    stop_event = subscription_threads[subscription_id]["stop_event"]
    try:
        client = httpx.AsyncClient(http2=True, limits=limits, timeout=timeout)
        while not stop_event.is_set():
            try:
                for message in consumer:
                    if stop_event.is_set():
                        break

                    #start_time = time.perf_counter_ns()
                    #start_datetime = datetime.datetime.now(datetime.timezone.utc)
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
                        #current_datetime = datetime.datetime.now(datetime.timezone.utc)
                        #update_nested_keys_observedAt(obj=dict_buffer, datetime=current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
                        #update_nested_keys_observedAt(obj=dict_buffer, datetime=parsing_start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))

                        if sysAttrs:
                            dict_buffer["createdAt"] = parsing_start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") 
                            dict_buffer["modifiedAt"] = parsing_start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") 

                            update_nested_keys(obj=dict_buffer, datetime=parsing_start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
                        try:
                            entity = get_entity_class_object_by_type(dict_buffer)
                            if entity != None: #and dict_buffer['type'] == 'ExportPacketFlowDataRecord':
                                filtered_dict_buffers.append(dict_buffer)
                        except Exception as e:
                            logger.exception(f"Failed to validate entity: {e}")
                    
                    #stop_time = time.perf_counter_ns()
                    #exec_time = stop_time - start_time
                    #exec_times.append(exec_time)
                    #stop_datetime
                    '''
                    parsing_stop_datetime = datetime.datetime.now(datetime.timezone.utc)
                    parsing_exec_time = (parsing_stop_datetime - parsing_start_datetime).total_seconds()
                    parsing_exec_times.append(parsing_exec_time)
                    '''
                    
                    ##materialization
                    #upserted = batch_upsert_ngsi_ld_entities(ngsi_ld, dict_buffers)
                    #if upserted == False:
                    #    print("ENTITIES COULD NOT BE UPSERTED")
                    #else:
                    #    print("ENTITIES WAS SUCCESSFULLY UPSERTED")

                    
                    #instantiation_stop_datetime = datetime.datetime.now(datetime.timezone.utc)
                    #instantiation_exec_time = (instantiation_stop_datetime - parsing_start_datetime).total_seconds()
                    #instantiation_exec_times.append(instantiation_exec_time)

                    ##virtualization for data adquisition
                    '''
                    for dict_buffer in filtered_dict_buffers:
                        dict_buffer["time"] = parsing_exec_time
                    producer.send('netflow-subscriptions-dictionary-buffers', value=json.dumps(filtered_dict_buffers).encode('utf-8'))
                    producer.flush()
                    '''
                    #producer.send('netflow-subscriptions-dictionary-buffers', value=json.dumps(filtered_dict_buffers).encode('utf-8'))
                    #producer.flush()
                    kafka_message_json = filtered_dict_buffers
                    start_datetime = None
                    new_kafka_message = []
                    
                    if entity_id is not None:
                        message = [obj for obj in kafka_message_json if obj.get("type") == entity_type and obj.get("id") == entity_id]
                    else:
                        message = [obj for obj in kafka_message_json if obj.get("type") == entity_type]
                    
                    logging.info(f"Kafka message for {subscription_id} after filter is: {message}")

                    observedAt = get_observed_at(message)
                    current_datetime = datetime.datetime.now(datetime.timezone.utc)
                    ngsi_ld_entity_datetime = current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

                    # Generates the notification id and the current date
                    notification_id = f"notification:{uuid4().int}"
                    notified_at = ngsi_ld_entity_datetime
                    for entity in message:
                        if "createdAt" in entity:
                            start_datetime = entity["createdAt"]
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
                    compressed_notification_data = gzip.compress(json.dumps(notification_data).encode("utf-8"))
                    
                    # Send the notification to the endpoint specified in the subscription
                    try:
                        response = await client.post(
                            notification_endpoint,
                            content=compressed_notification_data,
                            headers={"Link": '<{0}>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"', "Accept": "application/json", "Content-Type": "application/json", "Content-Encoding": "gzip"}
                        )

                        response.raise_for_status()
                        
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
                        '''
                        if "_" in subscription_id:
                            await delete_subscriptions(subscriptionId=str(subscription_id.split("_")[0]))
                        else:
                            await delete_subscriptions(subscriptionId=subscription_id)
                        '''
                        raise HTTPException(status_code=503, detail=f"Cannot connect to notification endpoint: {notification_endpoint}")
                    except httpx.RequestError as e:
                        raise HTTPException(status_code=500, detail=f"Failed to send notification: {str(e)}")
                    except httpx.HTTPStatusError as e:
                        raise HTTPException(status_code=response.status_code, detail=f"Notification failed: {str(e)}")
                    
                    logger.info("Restarting HTTP client...")
                    await client.aclose() 
                    client = httpx.AsyncClient(http2=True, limits=limits, timeout=timeout) 


                    print("Iteration done! Waiting for the next notification...\n")

                    print("--- PERFORMANCE MEASUREMENTS ---\n")
                    print("NOTIFICATIONS PROCESSED SO FAR: " + str(len(parsing_exec_times)) + "\n")
                    print("NOTIFICATION EVENT TIME/OBSERVED AT: " + event_time + "\n")
                    print("ITERATION STARTED AT: " + parsing_start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
                    print("ITERATION FINISHED AT: " + parsing_stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
                    print(f"PARSER ITERATION EXECUTION TIME: {parsing_exec_time * 1e3} ms\n")
                    #print(f"INSTANTIATION ITERATION EXECUTION TIME: {instantiation_exec_time * 1e3} ms\n")
                    print(f"TOTAL PROCESSING TIME SO FAR SINCE NOTIFICATION EVENT TIME/OBSERVED AT: {(parsing_stop_datetime - parser.parse(event_time)).total_seconds() * 1e3} ms\n")
                    print(f"MEAN EXECUTION TIME SO FAR: {(sum(parsing_exec_times)/len(parsing_exec_times)) * 1e3} ms\n")
                    print(f"MIN EXECUTION TIME SO FAR: {min(parsing_exec_times) * 1e3} ms\n")
                    print(f"MAX EXECUTION TIME SO FAR: {max(parsing_exec_times) * 1e3} ms\n")
                    print("--- PERFORMANCE MEASUREMENTS ---")

                    csv_data = [event_time, parsing_start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), parsing_stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                                str((parsing_stop_datetime - parser.parse(event_time)).total_seconds() * 1e3) + " ms",
                                str(parsing_exec_time  * 1e3) + " ms", str((sum(parsing_exec_times)/len(parsing_exec_times)) * 1e3) + " ms",
                                str(min(parsing_exec_times)  * 1e3) + " ms", str(max(parsing_exec_times) * 1e3) + " ms", str(len(parsing_exec_times))]
                    parsing_csv_writer.writerow(csv_data)
                    parsing_performance_measurements_file.flush()

            except Exception as e:
                logger.exception(f"Error consuming from Kafka: {str(e)}")

    finally:
        await client.aclose()
        consumer.close()
        parsing_performance_measurements_file.close()
        logging.info("Kafka Consumer from NGSI-LD instantiator is closed!")
        logger.info("Kafka consumer thread from NGSI-LD instantiator has been stopped!")

def ngsi_ld_instantiator_old(subscription_threads, subscription_id, sysAttrs):

    #exec_times = []
    parsing_exec_times = []
    instantiation_exec_times = []

    print("Hello, I am the JSON parser for NetFlow and the NGSI-LD instantiator")

    print("I will consume messages (NetFlow data records) from a Kafka topic named netflow-driver-output")

    consumer = KafkaConsumer('netflow-driver-output', bootstrap_servers=['kafka:9092'], value_deserializer=lambda x: json.loads(x.decode('utf-8')))

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

    stop_event = subscription_threads[subscription_id]["stop_event"]
    try:
        while not stop_event.is_set():
            try:
                for message in consumer:
                    if stop_event.is_set():
                        break

                    #start_time = time.perf_counter_ns()
                    #start_datetime = datetime.datetime.now(datetime.timezone.utc)
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
                        #current_datetime = datetime.datetime.now(datetime.timezone.utc)
                        #update_nested_keys_observedAt(obj=dict_buffer, datetime=current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
                        #update_nested_keys_observedAt(obj=dict_buffer, datetime=parsing_start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))

                        if sysAttrs:
                            dict_buffer["createdAt"] = parsing_start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") 
                            dict_buffer["modifiedAt"] = parsing_start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") 

                            update_nested_keys(obj=dict_buffer, datetime=parsing_start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
                        try:
                            entity = get_entity_class_object_by_type(dict_buffer)
                            if entity != None and dict_buffer['type'] == 'ExportPacketFlowDataRecord':
                                filtered_dict_buffers.append(dict_buffer)
                        except Exception as e:
                            logger.exception(f"Failed to validate entity: {e}")
                    
                    #stop_time = time.perf_counter_ns()
                    #exec_time = stop_time - start_time
                    #exec_times.append(exec_time)
                    #stop_datetime
                    '''
                    parsing_stop_datetime = datetime.datetime.now(datetime.timezone.utc)
                    parsing_exec_time = (parsing_stop_datetime - parsing_start_datetime).total_seconds()
                    parsing_exec_times.append(parsing_exec_time)
                    '''
                    
                    ##materialization
                    #upserted = batch_upsert_ngsi_ld_entities(ngsi_ld, dict_buffers)
                    #if upserted == False:
                    #    print("ENTITIES COULD NOT BE UPSERTED")
                    #else:
                    #    print("ENTITIES WAS SUCCESSFULLY UPSERTED")

                    
                    #instantiation_stop_datetime = datetime.datetime.now(datetime.timezone.utc)
                    #instantiation_exec_time = (instantiation_stop_datetime - parsing_start_datetime).total_seconds()
                    #instantiation_exec_times.append(instantiation_exec_time)

                    ##virtualization for data adquisition
                    '''
                    for dict_buffer in filtered_dict_buffers:
                        dict_buffer["time"] = parsing_exec_time
                    producer.send('netflow-subscriptions-dictionary-buffers', value=json.dumps(filtered_dict_buffers).encode('utf-8'))
                    producer.flush()
                    '''
                    producer.send('netflow-subscriptions-dictionary-buffers', value=json.dumps(filtered_dict_buffers).encode('utf-8'))
                    producer.flush()

                    print("Iteration done! Waiting for the next notification...\n")

                    print("--- PERFORMANCE MEASUREMENTS ---\n")
                    print("NOTIFICATIONS PROCESSED SO FAR: " + str(len(parsing_exec_times)) + "\n")
                    print("NOTIFICATION EVENT TIME/OBSERVED AT: " + event_time + "\n")
                    print("ITERATION STARTED AT: " + parsing_start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
                    print("ITERATION FINISHED AT: " + parsing_stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
                    print(f"PARSER ITERATION EXECUTION TIME: {parsing_exec_time * 1e3} ms\n")
                    #print(f"INSTANTIATION ITERATION EXECUTION TIME: {instantiation_exec_time * 1e3} ms\n")
                    print(f"TOTAL PROCESSING TIME SO FAR SINCE NOTIFICATION EVENT TIME/OBSERVED AT: {(parsing_stop_datetime - parser.parse(event_time)).total_seconds() * 1e3} ms\n")
                    print(f"MEAN EXECUTION TIME SO FAR: {(sum(parsing_exec_times)/len(parsing_exec_times)) * 1e3} ms\n")
                    print(f"MIN EXECUTION TIME SO FAR: {min(parsing_exec_times) * 1e3} ms\n")
                    print(f"MAX EXECUTION TIME SO FAR: {max(parsing_exec_times) * 1e3} ms\n")
                    print("--- PERFORMANCE MEASUREMENTS ---")

                    csv_data = [event_time, parsing_start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), parsing_stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                                str((parsing_stop_datetime - parser.parse(event_time)).total_seconds() * 1e3) + " ms",
                                str(parsing_exec_time  * 1e3) + " ms", str((sum(parsing_exec_times)/len(parsing_exec_times)) * 1e3) + " ms",
                                str(min(parsing_exec_times)  * 1e3) + " ms", str(max(parsing_exec_times) * 1e3) + " ms", str(len(parsing_exec_times))]
                    parsing_csv_writer.writerow(csv_data)
                    parsing_performance_measurements_file.flush()

            except Exception as e:
                logger.exception(f"Error consuming from Kafka: {str(e)}")

    finally:
        consumer.close()
        parsing_performance_measurements_file.close()
        logging.info("Kafka Consumer from NGSI-LD instantiator is closed!")
        logger.info("Kafka consumer thread from NGSI-LD instantiator has been stopped!")

        
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