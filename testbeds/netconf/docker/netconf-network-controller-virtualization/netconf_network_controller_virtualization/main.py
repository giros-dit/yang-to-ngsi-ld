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
import ngsi_ld_client_1_8_1
import ngsi_ld_models_1_8_1
import ngsi_ld_models_ietf_interfaces
import ngsi_ld_models_mdt_client_data_virtualization
from ngsi_ld_client.models.create_subscription_request import CreateSubscriptionRequest
from ngsi_ld_client.models.subscription_on_change import SubscriptionOnChange
from ngsi_ld_client.models.subscription_periodic import SubscriptionPeriodic
from ngsi_ld_client_1_8_1.models.create_csr_request import CreateCSRRequest
from ngsi_ld_client_1_8_1.models.registration_info import RegistrationInfo
from ngsi_ld_client_1_8_1.models.key_value_pair import KeyValuePair
from ngsi_ld_client_1_8_1.models.entity_info import EntityInfo
from ngsi_ld_client_1_8_1.models.entity_info_type import EntityInfoType
from ngsi_ld_models_1_8_1.models.entity_map import EntityMap
from ngsi_ld_client.models.notification_params import NotificationParams
from ngsi_ld_client.models.endpoint import Endpoint
from ngsi_ld_client.api_client import ApiClient as NGSILDClient
from ngsi_ld_client.configuration import Configuration as NGSILDConfiguration
from ngsi_ld_client_1_8_1.api_client import ApiClient as NGSILDClient_1_8_1
from ngsi_ld_client_1_8_1.configuration import Configuration as NGSILDConfiguration_1_8_1
from ngsi_ld_client.exceptions import NotFoundException
from pydantic import ValidationError
from netconf_network_controller_virtualization.check_client import NGSILDHealthInfoClient
from netconf_network_controller_virtualization.context_client import ContextCatalogClient
from netconf_network_controller_virtualization.ncclient_collector import get_operation, set_operation, get_xpath_in_context_catalog, get_xpath_with_keys, discover_config_entity_by_name, discover_config_entity_by_uri
from ngsi_ld_models_mdt_client_data_virtualization.models.protocol import Protocol
from ngsi_ld_models_mdt_client_data_virtualization.models.subscribe_rpc_template import SubscribeRpcTemplate
from ngsi_ld_models_mdt_client_data_virtualization.models.credentials import Credentials

from ngsi_ld_models_ietf_interfaces.models.interface_config import InterfaceConfig
from ngsi_ld_models_ietf_interfaces.models.interface_config_ipv4 import InterfaceConfigIpv4
from ngsi_ld_models_ietf_interfaces.models.interface_config_ipv4_address import InterfaceConfigIpv4Address
from ngsi_ld_models_ietf_interfaces.models.interface_config_ipv6 import InterfaceConfigIpv6
from ngsi_ld_models_ietf_interfaces.models.interface_config_ipv6_address import InterfaceConfigIpv6Address
from ngsi_ld_models_ietf_interfaces.models.interface_config_ipv6_autoconf import InterfaceConfigIpv6Autoconf
from ngsi_ld_models_ietf_interfaces.models.interface_config_ipv6_neighbor import InterfaceConfigIpv6Neighbor

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

from ncclient import manager
from ncclient.xml_ import to_ele

import xml.etree.ElementTree as et

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

# Notifier
NOTIFIER_URI = os.getenv("NOTIFIER_URI", "http://netconf-network-controller-virtualization:8089/notify")

# Init NGSI-LD Client
configuration = NGSILDConfiguration(host=BROKER_URI)
configuration.debug = True
ngsi_ld = NGSILDClient(configuration=configuration)

configuration_1_8_1 = NGSILDConfiguration_1_8_1(host=BROKER_URI)
configuration_1_8_1.debug = True
ngsi_ld_1_8_1 = NGSILDClient_1_8_1(configuration=configuration_1_8_1)

all_context_data = None
all_context_registries = None
scorpio_ip_address = ""

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

ngsi_ld_1_8_1.set_default_header(
    header_name="Link",
    header_value='<{0}>; '
                 'rel="http://www.w3.org/ns/json-ld#context"; '
                 'type="application/ld+json"'.format(CONTEXT_CATALOG_URI)
)

ngsi_ld_1_8_1.set_default_header(
    header_name="Accept",
    header_value="application/json"
)

ngsi_ld_api_instance_provision = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

ngsi_ld_api_instance_consumption = ngsi_ld_client.ContextInformationConsumptionApi(ngsi_ld)

ngsi_ld_api_instance_subscription = ngsi_ld_client.ContextInformationSubscriptionApi(ngsi_ld)

ngsi_ld_api_instance_csourceregistration = ngsi_ld_client_1_8_1.ContextSourceRegistrationApi(ngsi_ld_1_8_1)

LIST_ENTITIES = [
    "Protocol",
    "Credentials",
    "SubscribeRpcTemplate"
]
    
# Init FastAPI server
app = FastAPI(
    title="NETCONF Network Controller Virtualization API",
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
    global scorpio_ip_address

    context_urls = context_client.fetch_data()
    if context_urls:
        context_client.search_context_urls(context_urls)
        all_context_data = context_client.search_context_data(context_urls)
        all_context_registries = context_client.store_metadata_registries_in_list(context_urls)
    
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

    # Resolve Scorpio IP address
    try:
        scorpio_ip_address = socket.gethostbyname("scorpio")
        logger.info(f"Scorpio IP address: {scorpio_ip_address}")
    except Exception as e:
        logger.exception(f"Error resolving Scorpio IP address: {e}")

    interface_entity_info = EntityInfo(
        type=EntityInfoType("ietf-interfaces:interfaces-state/interface")
    )

    interface_config_entity_info = EntityInfo(
        type=EntityInfoType("ietf-interfaces:interfaces/interface")
    )

    interface_stats_entity_info = EntityInfo(
        type=EntityInfoType("ietf-interfaces:interfaces-state/interface/statistics")
    )

    interface_ipv4_entity_info = EntityInfo(
        type=EntityInfoType("ietf-interfaces:interfaces-state/interface/ietf-ip:ipv4")
    )

    interface_ipv4_address_entity_info = EntityInfo(
        type=EntityInfoType("ietf-interfaces:interfaces-state/interface/ietf-ip:ipv4/address")
    )

    interface_ipv4_config_entity_info = EntityInfo(
        type=EntityInfoType("ietf-interfaces:interfaces/interface/ietf-ip:ipv4")
    )

    interface_ipv4_address_config_entity_info = EntityInfo(
        type=EntityInfoType("ietf-interfaces:interfaces/interface/ietf-ip:ipv4/address")
    )

    context_source_registration_info = RegistrationInfo(
        entities=[
           interface_entity_info,
           interface_config_entity_info,
           interface_stats_entity_info,
           interface_ipv4_entity_info,
           interface_ipv4_address_entity_info, 
           interface_ipv4_config_entity_info,
           interface_ipv4_address_config_entity_info 
        ]
    )

    '''
    BLOCKED!
    Currently, context source registration operations do not properly support the datasetId and contextSourceInfo parameters.
    There are issues recently opened on GitHub: 
    - https://github.com/ScorpioBroker/ScorpioBroker/issues/625
    - https://github.com/ScorpioBroker/ScorpioBroker/issues/626
    '''
    '''
    key_value_pairs = []
    key_value_pair_operation = KeyValuePair(
        key="operation",
        value="urn:ngsi-ld:request"
    )
    key_value_pairs.append(key_value_pair_operation)
    '''

    context_source_request = CreateCSRRequest(
        id="urn:ngsi-ld:ContextSource:{0}".format("Interfaces"),
        type="ContextSourceRegistration",
        description="Context Source Registration for NGSI-LD entities relative to ietf-interfaces and ietf-ip YANG models.",
        #context_source_info = key_value_pairs,
        dataset_id = ["urn:yang:configuration", "urn:yang:operational"],
        information=[
            context_source_registration_info
        ],
        endpoint="http://netconf-network-controller-virtualization:8089"
    )
    
    try:
        ngsi_ld_api_instance_csourceregistration.create_csr(create_csr_request=context_source_request)          
    except Exception as e:
        logger.exception("Exception when calling ContextSourceRegistrationApi->create_csr: %s\n" % e) 
    
    for entity in LIST_ENTITIES:
        endpoint = Endpoint(
            uri = NOTIFIER_URI,
            accept="application/json"
        )

        # On-Change Subscriptions
        notification_params = NotificationParams (
            endpoint=endpoint,
            format="normalized",
            sysAttrs=True
        )

        subs_request = CreateSubscriptionRequest (
            id="urn:ngsi-ld:Subscription:{0}".format(entity),
            type="Subscription",
            entities=[
                {
                    "type": entity
                }
            ],
            description="On-change subscription to {0} entity.".format(entity),
            notificationTrigger=['entityCreated', 'entityUpdated', 'entityDeleted', 'attributeCreated', 'attributeUpdated', 'attributeDeleted'],
            notification=notification_params
        )

        ngsi_ld_api_instance_subscription.create_subscription(create_subscription_request=subs_request)

'''
Function to initiialize the custom NGSI-LD information model for NETCONF clients to manage the network controller 
automation operations. The network controller is based on a data virtualization approach and supports all the RPC 
operations defined by the NETCONF management protocol.
'''
@app.post("/notify",
          status_code=status.HTTP_200_OK)
async def receiveNotification(request: Request):
    global host
    global port
    global username
    global password
    global family
    global hostKeyVerify
    global subscriptionMode
    global period
    global all_context_data
    global all_context_registries
    notification = await request.json()
    for entity in notification["data"]:
        if entity["type"] == "Protocol" and entity["name"]["value"] == "netconf":
            try:
                entity_match = Protocol.from_dict(entity)
                logger.info("Entity object representation: %s\n" % entity_match)
                entity_input = entity_match.to_dict()
                logger.info("Entity object representation: %s\n" % Entity.from_dict(entity_input))
                logger.info("Entity notification: %s\n" % entity)
                host = entity["address"]["value"]
                port = entity["port"]["value"]
                entity_id = entity["id"]
                family = "csr"
                hostKeyVerify = False

            except ValidationError as e:
                logger.error("Validation error: %s\n" % e)
                # Delete NGSI-LD Entity by id: DELETE /entities/{entityId}
                try:
                    ngsi_ld_api_instance_provision.delete_entity(entity_id=entity_id)
                except Exception as e:
                    logger.exception("Exception when calling ContextInformationProvisionApi->delete_entity: %s\n" % e) 
        elif entity["type"] == "Credentials":
            try:
                entity_match = Credentials.from_dict(entity)
                entity_input = entity_match.to_dict()
                logger.info("Entity object representation: %s\n" % Entity.from_dict(entity_input))
                logger.info("Entity notification: %s\n" % entity)
                username = entity["username"]["value"]
                password = entity["password"]["value"]
                entity_id = entity["id"]

            except ValidationError as e:
                logger.error("Validation error: %s\n" % e)
                # Delete NGSI-LD Entity by id: DELETE /entities/{entityId}
                try:
                    ngsi_ld_api_instance_provision.delete_entity(entity_id=entity_id)
                except Exception as e:
                    logger.exception("Exception when calling ContextInformationProvisionApi->delete_entity: %s\n" % e) 
        elif entity["type"] == "SubscribeRpcTemplate":
            try:
                entity_match = SubscribeRpcTemplate.from_dict(entity)
                entity_input = entity_match.to_dict()
                logger.info("Entity object representation: %s\n" % Entity.from_dict(entity_input))
                logger.info("Entity notification: %s\n" % entity)
                entity_id = entity["id"]
                if "subscriptionMode" in entity:
                    subscriptionMode = entity["subscriptionMode"]["value"]
                    if subscriptionMode == "periodic":
                        period = entity["subscriptionMode"]["period"]["value"]
                
                '''
                usesProtocol = entity["usesProtocol"]["object"]
                api_response = None
                try:
                    # Retrieve NGSI-LD Entity of type Protocol by its id: GET /entities/{entityId}
                    api_response = ngsi_ld_api_instance_consumption.retrieve_entity(entity_id=usesProtocol)
                    logger.info(api_response.to_dict())
                except NotFoundException as nfe:
                    logger.error("NotFoundException when calling ContextInformationConsumptionApi->retrieve_entity: %s\n" % nfe)
                except Exception as e:
                    logger.error("Exception when calling ContextInformationConsumptionApi->retrieve_entity: %s\n" % e)

                if api_response == None:
                    logger.info("Entity of type SubscribeRpcTemplate with id " + entity_id + " has not a valid protocol associated!")
                    # Delete NGSI-LD Entity by id: DELETE /entities/{entityId}
                    try:
                        ngsi_ld_api_instance_provision.delete_entity(entity_id=entity_id)
                    except NotFoundException as e:
                        logger.error("NotFoundException when calling ContextInformationProvisionApi->delete_entity: %s\n" % e)
                    except Exception as e:
                        logger.error("Exception when calling ContextInformationConsumptionApi->delete_entity: %s\n" % e)
                '''
            except ValidationError as e:
                logger.error("Validation error: %s\n" % e)
                # Delete NGSI-LD Entity by id: DELETE /entities/{entityId}
                try:
                    ngsi_ld_api_instance_provision.delete_entity(entity_id=entity_id)
                except Exception as e:
                    logger.exception("Exception when calling ContextInformationProvisionApi->delete_entity: %s\n" % e) 
'''
Function for triggering NETCONF RPC YANG-Push subscriptions with needed parameters.
'''
async def subscribe_operation(host: str, port: str, username: str, password: str, family: str, entity_type: str, entity_id: str, subscriptionMode: str, period: str, subscription_id: str, all_context_data: Optional[dict] = None, hostKeyVerify: Optional[bool] = False, sysAttrs: Optional[bool] = False, all_context_registries: Optional[list] = None):
    # Each subscription will have its own stop event
    stop_event = asyncio.Event()

    # Save the event and thread in the global dictionary to control this subscription
    subscription_threads[subscription_id] = {"stop_event": stop_event, "thread": None}

    r = {
        "host": host,
        "port": port,
        "username": username,
        "password": password,
        "hostkey_verify": hostKeyVerify,
        "device_params": {"name": family}
    }

    logger.info("Hello, this is the ncclient-collector for " + host + " for subscriptions...")

    session = manager.connect(**r)

    logger.info("I have successfully established a session with ID# " + session.session_id)

    if subscriptionMode == "periodic":
        subscription = "period"
        period = period
    else:
        subscription = "dampening-period"
        period = 0
    
    xpath = get_xpath_in_context_catalog(entity_type=entity_type, all_context_data=all_context_data)

    if entity_id != None:
        xpath = get_xpath_with_keys(xpath=xpath, entity_id=entity_id, all_context_registries=all_context_registries)

    # Try first a get RPC operation:
    try:
        # Execute the get RPC
        reply = session.get(filter=('xpath', xpath))
        logger.info("\nInterface operational status of network device " + host + ": \n")
        logger.info(reply)
        data_element = et.fromstring(str(reply)).find('.//{urn:ietf:params:xml:ns:netconf:base:1.0}data')
        if data_element is None or len(data_element) == 0:
            logger.info("\nThe Xpath is incorrect or not supported by the network device " + host + ".")
            if "_" in subscription_id:
                subscription_id = subscription_id.split("_")[0]

            # Delete NGSI-LD Subscription by id: DELETE  /subscriptions/{subscriptionId}
            await delete_subscriptions(subscriptionId=subscription_id)

            session.close_session()
            return
    except Exception as e:
        logger.exception(f"Error for establishing the Get operation: {e}")
        if "_" in subscription_id:
                subscription_id = subscription_id.split("_")[0]
        
        # Delete NGSI-LD Subscription by id: DELETE  /subscriptions/{subscriptionId}
        await delete_subscriptions(subscriptionId=subscription_id)

        session.close_session()
        return

    # When building the RPC request XML, use dampening-period for on-change notifications (when supported).
    # Otherwise, use period and specify an integer value for the time in centiseconds.
    '''
    rpc = """

        <establish-subscription xmlns="urn:ietf:params:xml:ns:yang:ietf-event-notifications"
        xmlns:yp="urn:ietf:params:xml:ns:yang:ietf-yang-push">
            <stream>yp:yang-push</stream>
            <yp:xpath-filter>{0}</yp:xpath-filter>
            <yp:{1}>{2}</yp:{1}>
        </establish-subscription>

    """.format(xpath, subscription, period)
    '''
    # Render a Jinja template for the Subscription RPC
    subscription_template = Template(open('./netconf_network_controller_virtualization/jinja2-templates/yang-push-subscriptions.xml').read())
    rpc = subscription_template.render(
        XPATH = xpath,
        SUBS_TYPE = subscription,
        SUBS_PERIOD = period
    )

    try:
        request = session.dispatch(to_ele(rpc))
        logger.info("I have subscribed myself to get periodic YANG-Push notifications for X-Path " + xpath + " of network device " + host)
        logger.info(request)
    except Exception as e:
        logger.error(f"Error for establishing the YANG-Push subscription: {str(e)}")
        if "_" in subscription_id:
            subscription_id = subscription_id.split("_")[0]
        
        # Delete NGSI-LD Subscription by id: DELETE  /subscriptions/{subscriptionId}
        await delete_subscriptions(subscriptionId=subscription_id)

        session.close_session()
        return

    producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

    # Run the receive notification function in a separate thread
    notification_thread = threading.Thread(target=get_notifications, args=(session, producer, host, subscription_id, sysAttrs))
    subscription_threads[subscription_id]["thread"] = notification_thread
    notification_thread.start()

    # Wait until the stop event is triggered
    await stop_event.wait()

    # Once the event is triggered, stop the thread
    notification_thread.join()
    session.close_session()

    logger.info(f"Stopped subscription for {host} and id {subscription_id}!")

    '''
    logger.info(f"Stopping Kafka consumer for {subscription_id} ...") 
    kafka_consumer_threads[subscription_id]["stop_event"].set()  
    if kafka_consumer_threads[subscription_id]["thread"] is not None:
        kafka_consumer_threads[subscription_id]["thread"].join() # Esperar a que termine el hilo anterior
    # Remove from the kafka consumer thread dictionary
    del kafka_consumer_threads[subscription_id]
    logger.info(f"Kafka Consumer {subscription_id} stopped!")
    '''

'''
Function for receiving notifications of previously triggered NETCONF RPC YANG-Push subscription operations.
'''
def get_notifications(session, producer, host, subscription_id, sysAttrs):
    stop_event = subscription_threads[subscription_id]["stop_event"]
    while not stop_event.is_set():
        try:
            # Here you can modify the timeout if it is supported
            sub_data = session.take_notification(timeout=10)
            if sub_data is not None:
                logger.info("\nI have received a notification!\n")
                notification_xml = str(sub_data.notification_xml)
                logger.info(notification_xml)
                root = et.fromstring(notification_xml)

                # A new subelement is added to the NETCONF notification: fromDevice.
                # It is the name of the device that is sending the notification.
                # WARNING: This is not defined in the specification.
                from_device = et.SubElement(root, 'fromDevice')
                from_device.text = host
                
                # A new subelement is added to the NETCONF notification: operation.
                # It is the name of the operation.
                # WARNING: This is not defined in the specification.
                operation = et.SubElement(root, 'operation')
                operation.text = "subscribe"

                # A new subelement is added to the NETCONF notification: sysAttrs.
                # It is the system-attribute parameter value.
                # WARNING: This is not defined in the specification.
                sys_attrs = et.SubElement(root, 'sysAttrs')
                sys_attrs.text = str(sysAttrs)
                
                eventTime = root[0].text
                logger.info("The original eventTime element of the notification is: " + eventTime)

                '''
                notification_xml = et.tostring(root, encoding='unicode')
                producer.send('interfaces-state-subscriptions', value=notification_xml.encode('utf-8'))
                logger.info("I have sent it to a Kafka topic named interfaces-state-subscriptions")
                logger.info("The eventTime element of the notification is: " + eventTime)
                '''
                
                new_eventTime = root.find(".//{urn:ietf:params:xml:ns:netconf:notification:1.0}eventTime")
                current_datetime = datetime.datetime.now(datetime.timezone.utc)
                new_eventTime.text = current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
                notification_xml = et.tostring(root, encoding='unicode')
                logger.info(notification_xml)
                producer.send('interfaces-state-subscriptions', value=notification_xml.encode('utf-8'))
                logger.info("I have sent it to a Kafka topic named interfaces-state-subscriptions")
                logger.info("The new eventTime element of the notification is: " + current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))

                producer.flush()
            else:
                logger.info("No notification received in this cycle")
        except Exception as e:
            logger.exception(f"Error receiving notification: {str(e)}")

    logger.info("Notification thread has been stopped!")

'''
Function for starting a Kafka Consumer for processing query responses coming from NETCONF Get/Get-Config RPC operations.
'''
def listen_to_kafka_queries():
    global kafka_message
    # Kafka Consumer for processing query responses coming from NETCONF Get/Get-Config RPC operations
    consumer = KafkaConsumer('interfaces-state-subscriptions-dictionary-buffers', bootstrap_servers=['kafka:9092'], auto_offset_reset='latest')
    for message in consumer:
        kafka_message =  str(message.value.decode('utf-8')) #json.loads(message.value.decode('utf-8'))
        #kafka_message = str(message.value)
        break 

    consumer.close()

'''
Function for starting a Kafka Consumer for processing notifications coming from NETCONF Subcription RPC operations.
'''
async def listen_to_kafka_subscriptions(notification_endpoint, subscription_id, entity_type, entity_id = None):
    #consumer = KafkaConsumer('interfaces-state-subscriptions-dictionary-buffers', bootstrap_servers=['kafka:9092'], value_deserializer=lambda v: json.loads(v.decode('utf-8')))
    consumer = KafkaConsumer('interfaces-state-subscriptions-dictionary-buffers', bootstrap_servers=['kafka:9092'])
    logger.info(f"Starting new Kafka Consumer for {subscription_id}") 
    stop_event_kafka = kafka_consumer_threads[subscription_id]["stop_event"]
    exec_times = []
    performance_measurements_file = open("/opt/netconf-network-controller-virtualization/netconf_network_controller_virtualization/performance_measurements.csv", "w", newline='')
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

                if stop_event_kafka.is_set():
                    break

                kafka_message_json = json.loads(message.value.decode('utf-8'))    
                #kafka_message_json = json.loads(message.value)    
                
                logging.info(f"Kafka message for {subscription_id} is: {kafka_message_json}")

                if entity_id is not None:
                    kafka_message = [obj for obj in kafka_message_json if obj.get("type") == entity_type and obj.get("id") == entity_id]
                else:
                    kafka_message = [obj for obj in kafka_message_json if obj.get("type") == entity_type]

                logging.info(f"Kafka message for {subscription_id} after filter is: {kafka_message}")

                if str(kafka_message) != "[]":
                    new_kafka_message = []
                    for entity in kafka_message:
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
                        logger.info(f"HTTP Request Latency: {end - start} seconds")
                        
                        if start_datetime != None:
                            stop_datetime = datetime.datetime.now(datetime.timezone.utc)
                            stop_datetime_format = stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
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
def run_asyncio_in_thread(notification_endpoint, subscription_id, entity_type, entity_id = None):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(listen_to_kafka_subscriptions(notification_endpoint, subscription_id, entity_type, entity_id))

'''
Endpoint for deleting NGSI-LD subscriptions by its id. 
This endpoint triggers the clearing of previous NETCONF Subcription RPC operations.
'''
@app.delete("/ngsi-ld/v1/subscriptions/{subscriptionId}")
async def delete_subscriptions(subscriptionId: str):
    global ngsi_ld_subscriptions
    subscription_match = False
    matched_threads_id = []
    try:

        if len(subscription_threads) == 0:
            raise HTTPException(status_code=404, detail="Subscription not found.")

        for key in subscription_threads:
            if key.startswith(subscriptionId + "_") or key == subscriptionId:
                matched_threads_id.append(key)
                subscription_match = True

        if subscription_match == False:
            raise HTTPException(status_code=404, detail="Subscription not found.")

        for thread_id in matched_threads_id:
            # Check if there is already a subscription and Kafka Consumer associated with this entity and stop it
            if thread_id in subscription_threads and thread_id in kafka_consumer_threads:

                logger.info(f"Stopping Kafka consumer for {thread_id} ...") 

                kafka_consumer_threads[thread_id]["stop_event"].set()  
                #if kafka_consumer_threads[thread_id]["thread"] is not None:
                #    kafka_consumer_threads[thread_id]["thread"].join() # Esperar a que termine el hilo anterior
                # Remove from the kafka consumer thread dictionary
                del kafka_consumer_threads[thread_id]
                logger.info(f"Kafka Consumer {thread_id} stopped!")

                logger.info(f"Stopping subscription for {thread_id} ...")
                
                subscription_threads[thread_id]["stop_event"].set()  
                #if subscription_threads[thread_id]["thread"] is not None:
                #    subscription_threads[thread_id]["thread"].join() # Esperar a que termine el hilo anterior
                # Remove from the subscription thread dictionary
                del subscription_threads[thread_id]
                logger.info(f"Subscription {thread_id} stopped!")

                '''
                logger.info(f"Stopping Kafka consumer for {thread_id} ...") 
                kafka_consumer_threads[thread_id]["stop_event"].set()  
                if kafka_consumer_threads[thread_id]["thread"] is not None:
                    kafka_consumer_threads[thread_id]["thread"].join() # Esperar a que termine el hilo anterior
                # Remove from the kafka consumer thread dictionary
                del kafka_consumer_threads[thread_id] 
                logger.info(f"Kafka Consumer {thread_id} stopped!")
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
Endpoint for creating NGSI-LD entities. 
This endpoint triggers the NETCONF Set RPC operations.
'''
@app.post("/ngsi-ld/v1/entities")
async def post_entities(entity: dict):
    try:
        response =  JSONResponse(status_code=201, content={"message": "Entity created!"})
        entity_match = None
        if "type" in entity:
            aux_entity = entity.copy()
            entity_type_short = get_entity_type_short_in_context_catalog(entity["type"], all_context_data)
            if entity_type_short != None:
                aux_entity["type"] = entity_type_short
                entity_match = get_entity_class_object_by_type(aux_entity)
                set_operation(host=host, port=port, username=username, password=password, family=family, instance=entity_match, entity_type=entity["type"], entity_id=entity["id"], all_context_data=all_context_data, all_context_registries=all_context_registries)

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
Endpoint for subcribing to NGSI-LD entities. 
This endpoint triggers the NETCONF Subcription RPC operation.
'''
@app.post("/ngsi-ld/v1/subscriptions")
async def post_subscriptions(subscription: dict, request: Request):
    sysAttrs = False
    try:
        client_host = request.client.host
        logging.info(f"Client host: {client_host}")
        response =  JSONResponse(status_code=201, content={"message": "Subscription created!"})
        ngsi_ld_subscriptions.append(subscription)
        entities = subscription.get("entities", [])
        #watched_attributes = subscription.get("watchedAttributes", [])
        if subscription.get("timeInterval"):
            timeInterval = subscription.get("timeInterval")*100
        else:
            if subscriptionMode == "periodic":
                timeInterval = period * 100
        
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
            entity_type_short = None
            entity_type = None
            entity_id = None
            
            if "type" in entity and "id" not in entity: 
                id = subscription_id
                entity_type_short = get_entity_type_short_in_context_catalog(entity["type"], all_context_data)
                if entity_type_short != None:
                    if client_host == scorpio_ip_address:
                        config = discover_config_entity_by_name(entity["type"], all_context_registries)
                        entity_type = get_entity_type_long_in_context_catalog(entity["type"], all_context_data, config, all_context_registries)
                    else:
                        entity_type = entity["type"]
                    # Check if there is already subscription and Kafka Consumer associated with this entity and stop it
                    if subscription_id in subscription_threads and id in kafka_consumer_threads:
                        logger.info(f"Restarting subscription for {subscription_id} ...")
                        subscription_threads[subscription_id]["stop_event"].set()  
                        subscription_threads[subscription_id]["thread"].join() # Wait for the previous thread to finish
                        subscription_threads[subscription_id]["stop_event"].clear()
                        # Remove from the subscription thread dictionary
                        del subscription_threads[subscription_id]
                        logger.info(f"Subscription {subscription_id} stopped!")

                        '''
                        logger.info(f"Restarting Kafka consumer for {subscription_id} ...") 
                        kafka_consumer_threads[subscription_id]["stop_event"].set()  
                        if kafka_consumer_threads[subscription_id]["thread"] is not None:
                            kafka_consumer_threads[subscription_id]["thread"].join() # Esperar a que termine el hilo anterior
                        # Remove from the kafka consumer thread dictionary
                        del kafka_consumer_threads[subscription_id]
                        logger.info(f"Kafka Consumer {subscription_id} stopped!")
                        '''

                    # Create a new NETCONF Subscription RPC
                    logger.info(f"Starting new subscription for {id}")      
                    asyncio.create_task(subscribe_operation(host=host, port=port, username=username, password=password, family=family, entity_type=entity_type, entity_id=None, subscriptionMode="periodic", period=timeInterval, subscription_id=subscription_id, all_context_data=all_context_data, hostKeyVerify=hostKeyVerify, sysAttrs=sysAttrs, all_context_registries=all_context_registries))

            elif "id" in entity:

                id = subscription_id + "_" + str(entity["id"])
                
                entity_type_short = get_entity_type_short_in_context_catalog(entity["type"], all_context_data)
                if entity_type_short != None: 
                    if client_host == scorpio_ip_address:
                        config = discover_config_entity_by_name(entity["type"], all_context_registries)
                        entity_type = get_entity_type_long_in_context_catalog(entity["type"], all_context_data, config, all_context_registries)
                    else:
                        entity_type = entity["type"]
                    entity_id = entity["id"]
                    # Check if there is already a subscription and Kafka Consumer associated with this entity and stop it
                    if id in subscription_threads and id in kafka_consumer_threads:
                        logger.info(f"Restarting subscription for {id} ...")
                        subscription_threads[id]["stop_event"].set()  
                        subscription_threads[id]["thread"].join() # Wait for the previous thread to finish
                        subscription_threads[id]["stop_event"].clear()
                        # Remove from the subscription thread dictionary
                        del subscription_threads[id]
                        logger.info(f"Subscription {id} stopped!")

                        '''
                        logger.info(f"Restarting Kafka consumer for {id} ...") 
                        kafka_consumer_threads[id]["stop_event"].set()  
                        if kafka_consumer_threads[id]["thread"] is not None:
                            kafka_consumer_threads[id]["thread"].join() # Esperar a que termine el hilo anterior
                        # Remove from the kafka consumer thread dictionary
                        del kafka_consumer_threads[id]
                        logger.info(f"Kafka Consumer {id} stopped!")
                        '''

                    # Create a new NETCONF Subscription RPC
                    logger.info(f"Starting new subscription for {id}")
                    asyncio.create_task(subscribe_operation(host=host, port=port, username=username, password=password, family=family, entity_type=entity_type, entity_id=entity_id, subscriptionMode="periodic", period=timeInterval, subscription_id=id, all_context_data=all_context_data, hostKeyVerify=hostKeyVerify, sysAttrs=sysAttrs, all_context_registries=all_context_registries))  

            stop_event_kafka = threading.Event()
            kafka_thread = threading.Thread(
                target=run_asyncio_in_thread,
                args=(notification_endpoint, id, entity_type_short, entity_id),
                daemon=True
            )
            
            # Save the event and thread in the global dictionary to control this subscription
            kafka_consumer_threads[id] = {"stop_event": stop_event_kafka, "thread": None}
            kafka_consumer_threads[id]["thread"] = kafka_thread
            kafka_thread.start()
        
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
    

'''
Endpoint for getting the list of NGSI-LD entities provided by a Context Source.
This endpoint allows to discover the type of NGSI-LD entities before commiting the 
NETCONF Get/Get-Config RPC operation.
'''
@app.get("/ngsi-ld/v1/entityMap")
async def get_entitymap(request: Request):
    global kafka_message
    sysAttrs = False
    try:
        params = dict(request.query_params)  
        logging.info(f"Received query parameters: {params}") 
        client_host = request.client.host
        logging.info(f"Client host: {client_host}")

        kafka_message = None
        response_data = {}

        execute_operation = True

        config = False

        if "type" in params:
            if search_entity_type_short_in_context_catalog(params["type"], all_context_data) == True:
                execute_operation = True
            else:
                execute_operation = False

            config = discover_config_entity_by_name(params["type"], all_context_registries)
        elif "id" in params:
            urn_split = params["id"].split(":")
            if search_entity_type_short_in_context_catalog(urn_split[2], all_context_data) == True:
                execute_operation = True
            else:
                execute_operation = False

            config = discover_config_entity_by_name(urn_split[2], all_context_registries)
        else: 
            execute_operation = True
        
        if execute_operation == True:

            if "options" in params:
                if params["options"] == "sysAttrs":
                    sysAttrs = True
                else:
                    sysAttrs = False

            consumer_thread = threading.Thread(target=listen_to_kafka_queries)
            consumer_thread.start()

            entity_type = ""
            entity_type_short = ""

            if "type" in params and "id" not in params:
                entity_type_short = params["type"]
                entity_type = get_entity_type_long_in_context_catalog(entity_type_short, all_context_data, config, all_context_registries)
                if config == True: 
                    get_operation(host=host, port=port, username=username, password=password, family=family, entity_type=entity_type, entity_id=None, option="config", all_context_data=all_context_data, hostKeyVerify=hostKeyVerify, sysAttrs=sysAttrs, all_context_registries=all_context_registries)
                else:
                    get_operation(host=host, port=port, username=username, password=password, family=family, entity_type=entity_type, entity_id=None, option="state", all_context_data=all_context_data, hostKeyVerify=hostKeyVerify, sysAttrs=sysAttrs, all_context_registries=all_context_registries)
            elif "id" in params:
                urn_split = params["id"].split(":")
                if "type" in params:
                    entity_type_short = params["type"]
                else:
                    entity_type_short = urn_split[2]
                entity_type = get_entity_type_long_in_context_catalog(entity_type_short, all_context_data, config, all_context_registries)
                if config == True: 
                    get_operation(host=host, port=port, username=username, password=password, family=family, entity_type=entity_type, entity_id=params["id"], option="config", all_context_data=all_context_data, hostKeyVerify=hostKeyVerify, sysAttrs=sysAttrs, all_context_registries=all_context_registries)
                else:
                    get_operation(host=host, port=port, username=username, password=password, family=family, entity_type=entity_type, entity_id=params["id"], option="state", all_context_data=all_context_data, hostKeyVerify=hostKeyVerify, sysAttrs=sysAttrs, all_context_registries=all_context_registries)
            
            consumer_thread.join()

            if kafka_message is not None:
                if isinstance(kafka_message, str):
                    kafka_message_json = json.loads(kafka_message)
                elif isinstance(kafka_message, list):
                    kafka_message_json = kafka_message

                if "type" in params and "id" not in params:
                    entity_ids  = [item["id"] for item in kafka_message_json if item["type"] == entity_type_short]
                    kafka_message = [obj for obj in kafka_message_json if obj.get("type") == entity_type_short]
                elif "id" in params:
                    entity_ids  = [params["id"]] 
                    kafka_message = [obj for obj in kafka_message_json if obj.get("type") == entity_type_short and obj.get("id") == params["id"]]
                
                current_time = time.time_ns()
                logger.info(f"Current time in nanoseconds in epoch time format: {current_time}") 
                datetime_ns = np.datetime64(current_time, 'ns')
                logger.info(f"Current date time in nanoseconds: {datetime_ns}")
                expired_at = str(datetime_ns.astype('datetime64[ms]')) + 'Z'
                logger.info(f"Current data time in nanoseconds in Zulu format: {expired_at}")

                logger.info(f"Entity ids: {entity_ids}")

                entity_maps = {entity_id: ["@none"] for entity_id in entity_ids}

                entityMapInstance = EntityMap(
                    id="urn:ngsi-ld:entitymap:Interface",
                    type="EntityMap",
                    entity_map=entity_maps,
                    expires_at=expired_at
                )

                response_data = entityMapInstance.to_dict()
                response_data['expiresAt'] = response_data['expiresAt'].isoformat()
                response_data['entityMap'] = entity_maps
                logger.info(f"Response data: {response_data}")

            return JSONResponse(content=response_data, status_code=200, headers={"Content-Type": "application/json"})

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
Endpoint for getting NGSI-LD entities by its type or identifier. 
This endpoint triggers the NETCONF Get/Get-Config RPC operations.
'''
@app.get("/ngsi-ld/v1/entities")
async def get_entities(request: Request):
    global kafka_message
    sysAttrs = False
    try:
        params = dict(request.query_params) 
        logging.info(f"Received query parameters: {params}")
        client_host = request.client.host
        logging.info(f"Client host: {client_host}")

        kafka_message = []
        
        execute_operation = True

        config = False

        if "type" in params:
            if client_host == scorpio_ip_address:
                if search_entity_type_short_in_context_catalog(params["type"], all_context_data) == True:
                    execute_operation = True
                    config = discover_config_entity_by_name(params["type"], all_context_registries)
                else:
                    execute_operation = False
            else:
                if search_entity_type_short_in_context_catalog_given_long_version(params["type"], all_context_data) == True:
                    execute_operation = True
                    config = discover_config_entity_by_uri(params["type"], all_context_registries)
                else:
                    execute_operation = False

        elif "id" in params and "type" not in params:   
            urn_split = params["id"].split(":")
            if search_entity_type_short_in_context_catalog(urn_split[2], all_context_data) == True:
                execute_operation = True  
                config = discover_config_entity_by_name(urn_split[2], all_context_registries)
        else: 
            execute_operation = True
        
        if execute_operation == True:

            if "options" in params:
                if params["options"] == "sysAttrs":
                    sysAttrs = True
                else:
                    sysAttrs = False

            consumer_thread = threading.Thread(target=listen_to_kafka_queries)
            consumer_thread.start()

            if "type" in params and ("id" not in params or len(params["id"].split(",")) > 1):
                if client_host == scorpio_ip_address:
                    entity_type_requested = get_entity_type_long_in_context_catalog(params["type"], all_context_data, config, all_context_registries)
                else:
                    entity_type_requested = params["type"]
                if config == True: 
                    get_operation(host=host, port=port, username=username, password=password, family=family, entity_type=entity_type_requested, entity_id=None, option="config", all_context_data=all_context_data, hostKeyVerify=hostKeyVerify, sysAttrs=sysAttrs, all_context_registries=all_context_registries)
                else: 
                    get_operation(host=host, port=port, username=username, password=password, family=family, entity_type=entity_type_requested, entity_id=None, option="state", all_context_data=all_context_data, hostKeyVerify=hostKeyVerify, sysAttrs=sysAttrs, all_context_registries=all_context_registries)
            elif "id" in params and len(params["id"].split(",")) == 1:
                urn_split = params["id"].split(":")
                if "type" in params and client_host != scorpio_ip_address:
                    entity_type = params["type"]
                    entity_type_requested = entity_type
                else:
                    entity_type = urn_split[2]
                    entity_type_requested = get_entity_type_long_in_context_catalog(entity_type, all_context_data, config, all_context_registries)

                if config == True:
                    get_operation(host=host, port=port, username=username, password=password, family=family, entity_type=entity_type_requested, entity_id=params["id"], option="config", all_context_data=all_context_data, hostKeyVerify=hostKeyVerify, sysAttrs=sysAttrs, all_context_registries=all_context_registries)
                else:
                    get_operation(host=host, port=port, username=username, password=password, family=family, entity_type=entity_type_requested, entity_id=params["id"], option="state", all_context_data=all_context_data, hostKeyVerify=hostKeyVerify, sysAttrs=sysAttrs, all_context_registries=all_context_registries)

            consumer_thread.join()

            if isinstance(kafka_message, str):
                kafka_message_json = json.loads(kafka_message)
            elif isinstance(kafka_message, list):
                kafka_message_json = kafka_message
            if "type" in params and "id" not in params:
                if client_host == scorpio_ip_address:
                    entity_type_short = params["type"]
                else:
                    entity_type_short = get_entity_type_short_in_context_catalog(params["type"], all_context_data)
                kafka_message = [obj for obj in kafka_message_json if obj.get("type") == entity_type_short]
            elif "id" in params and len(params["id"].split(",")) == 1:
                if client_host == scorpio_ip_address:
                    entity_type_short = entity_type
                else:
                    entity_type_short = get_entity_type_short_in_context_catalog(entity_type, all_context_data)
                kafka_message = [obj for obj in kafka_message_json if obj.get("type") == entity_type_short and obj.get("id") == params["id"]]
            elif "id" in params and len(params["id"].split(",")) > 1:
                entity_ids = params["id"].split(",")
                kafka_message = []
                if client_host == scorpio_ip_address:
                    entity_type_short = params["type"]
                else:
                    entity_type_short = get_entity_type_short_in_context_catalog(params["type"], all_context_data)
                for obj in kafka_message_json:
                    for entity_id in entity_ids:
                        if obj.get("type") == entity_type_short and obj.get("id") == entity_id:
                            kafka_message.append(obj)
        if client_host == scorpio_ip_address:
            if "type" in params:
                return JSONResponse(content=kafka_message, status_code=200, headers={"Content-Type": "application/json", "Link": '<{0}>; rel="http://www.w3.org/ns/json-ld#context"; NGSILD-EntityMap: urn:ngsi-ld:entitymap:{1}'.format(CONTEXT_CATALOG_URI, params["type"])})
            elif "id" in params: 
                return JSONResponse(content=kafka_message, status_code=200, headers={"Content-Type": "application/json", "Link": '<{0}>; rel="http://www.w3.org/ns/json-ld#context"; NGSILD-EntityMap: urn:ngsi-ld:entitymap:{1}'.format(CONTEXT_CATALOG_URI, params["id"].split(":")[2])})
        else:
            return JSONResponse(content=kafka_message, status_code=200, headers={"Content-Type": "application/json", "Link": '<{0}>; rel="http://www.w3.org/ns/json-ld#context"'.format(CONTEXT_CATALOG_URI)})
           
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
Endpoint for getting NGSI-LD entities by its identifier. 
This endpoint triggers the NETCONF Get/Get-Config RPC operations.
'''
@app.get("/ngsi-ld/v1/entities/{id}")
async def get_entities(id: str, request: Request):
    global kafka_message
    sysAttrs = False
    try:
        entity_type = ""
        params = ""
        if request.query_params:
            params = dict(request.query_params) 
            logging.info(f"Received query parameters: {params}")  
        
        client_host = request.client.host
        logging.info(f"Client host: {client_host}")

        kafka_message = {}

        execute_operation = True

        config = False
        
        urn_split = id.split(":")

        if request.query_params and "type" in params:
            entity_type = params["type"]
        else:
            entity_type = urn_split[2]

        if entity_type != "":
            if client_host == scorpio_ip_address:
                if search_entity_type_short_in_context_catalog(entity_type, all_context_data) == True:
                    execute_operation = True
                    config = discover_config_entity_by_name(entity_type, all_context_registries)
                else:
                    execute_operation = False
            else:
                if request.query_params and "type" in params:
                    if search_entity_type_short_in_context_catalog_given_long_version(entity_type, all_context_data) == True:
                        execute_operation = True
                        config = discover_config_entity_by_uri(entity_type, all_context_registries)
                    else:
                        execute_operation = False
                else:
                    if search_entity_type_short_in_context_catalog(entity_type, all_context_data) == True:
                        execute_operation = True
                        config = discover_config_entity_by_name(entity_type, all_context_registries)
                    else:
                        execute_operation = False
        else: 
            execute_operation = True
        
        if execute_operation == True:

            if request.query_params and "options" in params:
                if params["options"] == "sysAttrs":
                    sysAttrs = True
                else:
                    sysAttrs = False

            consumer_thread = threading.Thread(target=listen_to_kafka_queries)
            consumer_thread.start()

            if client_host == scorpio_ip_address:
                entity_type = get_entity_type_long_in_context_catalog(entity_type, all_context_data, config, all_context_registries)
            else:
                if request.query_params and "type" in params:
                    entity_type = entity_type
                else:
                    entity_type = get_entity_type_long_in_context_catalog(entity_type, all_context_data, config, all_context_registries)

            if config:
                get_operation(host=host, port=port, username=username, password=password, family=family, entity_type=entity_type, entity_id=id, option="config", all_context_data=all_context_data, hostKeyVerify=hostKeyVerify, sysAttrs=sysAttrs, all_context_registries=all_context_registries)
            else:
                get_operation(host=host, port=port, username=username, password=password, family=family, entity_type=entity_type, entity_id=id, option="state", all_context_data=all_context_data, hostKeyVerify=hostKeyVerify, sysAttrs=sysAttrs, all_context_registries=all_context_registries)
                
            consumer_thread.join()

            if isinstance(kafka_message, str):
                kafka_message_json = json.loads(kafka_message)
            elif isinstance(kafka_message, list):
                kafka_message_json = kafka_message

            for obj in kafka_message_json:
                if obj.get("id") == id:
                    kafka_message = obj
            
        if client_host == scorpio_ip_address:
            if "type" in params:
                return JSONResponse(content=kafka_message, status_code=200, headers={"Content-Type": "application/json", "Link": '<{0}>; rel="http://www.w3.org/ns/json-ld#context"; NGSILD-EntityMap: urn:ngsi-ld:entitymap:{1}'.format(CONTEXT_CATALOG_URI, params["type"])})
            else: 
                return JSONResponse(content=kafka_message, status_code=200, headers={"Content-Type": "application/json", "Link": '<{0}>; rel="http://www.w3.org/ns/json-ld#context"; NGSILD-EntityMap: urn:ngsi-ld:entitymap:{1}'.format(CONTEXT_CATALOG_URI, id.split(":")[2])})
        else:
            return JSONResponse(content=kafka_message, status_code=200, headers={"Content-Type": "application/json", "Link": '<{0}>; rel="http://www.w3.org/ns/json-ld#context"'.format(CONTEXT_CATALOG_URI)})
        
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
Get short version of Entity type (i.e., type name) given the long version (i.e., type URI) by searching along the context registries within from Context Catalog:
'''
def get_entity_type_short_in_context_catalog(entity_type_long: str, all_context_data: Optional[dict]) -> str:

    entity_type_short = ""
    entity_type_short_founded = False
    for key, value in all_context_data.items():
        if isinstance(value, list):
            for v in value:
                if v == entity_type_long:
                    entity_type_short = key
                    logger.info(f"NGSI-LD Entity type name {entity_type_short} relative to NGSI-LD Entity type URI {entity_type_long} was founded!")
                    entity_type_short_founded = True
                    break
            if entity_type_short_founded:
                break
        else:
            if value == entity_type_long:
                entity_type_short = key
                logger.info(f"NGSI-LD Entity type name {entity_type_short} relative to NGSI-LD Entity type URI {entity_type_long} was founded!")
                break
    if entity_type_short == "":
        logger.info(f"NGSILD Entity type name relative to NGSI-LD Entity type URI {entity_type_long} was not founded!")

    return entity_type_short

'''
Get long version of Entity type (i.e., type URI) given the short version (i.e., type name) by searching along the context registries within from Context Catalog:
'''
def get_entity_type_long_in_context_catalog(entity_type_short: str, all_context_data: Optional[dict], config: bool, all_context_registries: Optional[list]) -> str:

    entity_type_long = ""
    entity_type_short_ocurrences = 0
    for key, value in all_context_data.items():
        if key == entity_type_short:

            #entity_type_long = value
            #logger.info(f"NGSI-LD Entity type URI {entity_type_long} relative to NGSI-LD Entity type value {entity_type_short} was founded!")
            #break

            for context_registry in all_context_registries:
                if key in context_registry["@context"].keys():
                     entity_type_short_ocurrences += 1

            if entity_type_short_ocurrences == 2:
                for context_registry in all_context_registries:
                    if value in context_registry["@context"].values():
                        if config == True:
                            if "config" in context_registry.keys():
                                entity_type_long = value
                        else:
                            if "config" not in context_registry.keys():
                                entity_type_long = value
                        break
            elif entity_type_short_ocurrences == 1:
                for context_registry in all_context_registries:
                    if value in context_registry["@context"].values():
                        entity_type_long = value
                break
            if entity_type_long != "":
                logger.info(f"NGSI-LD Entity type URI {entity_type_long} relative to NGSI-LD Entity type name {entity_type_short} was founded " + str(entity_type_short_ocurrences) + " times!")
                break
    if entity_type_long == "":
        logger.info(f"NGSI-LD Entity type URI relative to NGSI-LD Entity type name {entity_type_short} was not founded!")

    return entity_type_long

'''
Search short version of Entity type (i.e., type name) given the long version (i.e., type URI) by searching along the context registries within from Context Catalog:
'''
def search_entity_type_short_in_context_catalog_given_long_version(entity_type_long: str, all_context_data: Optional[dict]) -> bool:

    entity_type_short_founded = False
    for key, value in all_context_data.items():
        if isinstance(value, list):
            for v in value:
                if v == entity_type_long:
                    entity_type_short = key
                    logger.info(f"NGSI-LD Entity type name {entity_type_short} relative to NGSI-LD Entity type URI {entity_type_long} was founded!")
                    entity_type_short_founded = True
                    break
            if entity_type_short_founded:
                break
        else:
            if value == entity_type_long:
                entity_type_short = key
                logger.info(f"NGSI-LD Entity type name {entity_type_short} relative to NGSI-LD Entity type URI {entity_type_long} was founded!")
                entity_type_short_founded = True
                break
    if entity_type_short_founded == False:
        logger.info(f"NGSI-LD Entity type name relative to NGSI-LD Entity type URI {entity_type_long} was not founded!")

    return entity_type_short_founded

'''
Search short version of Entity type (i.e., type name) by searching along the context registries within from Context Catalog:
'''
def search_entity_type_short_in_context_catalog(entity_type_short: str, all_context_data: Optional[dict]) -> bool:

    entity_type_short_founded = False
    if str(entity_type_short) in all_context_data:
        logger.info(f"NGSI-LD Entity type name {entity_type_short} was founded!")
        entity_type_short_founded = True
    else:
        logger.info(f"NGSI-LD Entity type name was not founded!")

    return entity_type_short_founded

'''
Get the entity type name of a NGSI-LD Entity provided as a Python dictionary:
'''
'''
def get_entity_class_object_by_type(entity: dict):
    type = entity['type']
    if type == 'Interface':
        entity = InterfaceConfig.from_dict(entity)
    if type == 'InterfaceIpv4':
        entity = InterfaceConfigIpv4.from_dict(entity)
    if type == 'InterfaceIpv4Address':
        entity = InterfaceConfigIpv4Address.from_dict(entity)
    if type == 'InterfaceIpv6':
        entity = InterfaceConfigIpv6.from_dict(entity)
    if type == 'InterfaceIpv6Address':
        entity = InterfaceConfigIpv6Address.from_dict(entity)
    if type == 'InterfaceIpv6Autoconf':
        entity = InterfaceConfigIpv6Autoconf.from_dict(entity)
    if type == 'InterfaceIpv6Neighbor':
        entity = InterfaceConfigIpv6Neighbor.from_dict(entity)
    return entity
'''

def get_entity_class_object_by_type(entity: dict):
    type = entity['type']
    if type == 'InterfaceConfig':
        entity = InterfaceConfig.from_dict(entity)
    if type == 'InterfaceConfigIpv4':
        entity = InterfaceConfigIpv4.from_dict(entity)
    if type == 'InterfaceConfigIpv4Address':
        entity = InterfaceConfigIpv4Address.from_dict(entity)
    if type == 'InterfaceConfigIpv6':
        entity = InterfaceConfigIpv6.from_dict(entity)
    if type == 'InterfaceConfigIpv6Address':
        entity = InterfaceConfigIpv6Address.from_dict(entity)
    if type == 'InterfaceConfigIpv6Autoconf':
        entity = InterfaceConfigIpv6Autoconf.from_dict(entity)
    if type == 'InterfaceConfigIpv6Neighbor':
        entity = InterfaceConfigIpv6Neighbor.from_dict(entity)
    return entity
