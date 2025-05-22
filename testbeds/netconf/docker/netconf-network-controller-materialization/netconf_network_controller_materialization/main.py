import logging
import os
import re
from time import sleep
import time
from typing import Optional
from fastapi import FastAPI, Request, status, HTTPException
from fastapi.responses import JSONResponse
import json
import csv
import ngsi_ld_client
import ngsi_ld_models_ietf_interfaces
import ngsi_ld_models_mdt_client_data_materialization
from ngsi_ld_client.models.create_subscription_request import CreateSubscriptionRequest
from ngsi_ld_client.models.subscription_on_change import SubscriptionOnChange
from ngsi_ld_client.models.subscription_periodic import SubscriptionPeriodic
from ngsi_ld_client.models.notification_params import NotificationParams
from ngsi_ld_client.models.endpoint import Endpoint
from ngsi_ld_client.api_client import ApiClient as NGSILDClient
from ngsi_ld_client.configuration import Configuration as NGSILDConfiguration
from ngsi_ld_client.exceptions import NotFoundException
from pydantic import ValidationError
from netconf_network_controller_materialization.check_client import NGSILDHealthInfoClient
from netconf_network_controller_materialization.context_client import ContextCatalogClient
from netconf_network_controller_materialization.ncclient_collector import get_operation, set_operation, get_xpath_in_context_catalog, get_xpath_with_keys, discover_config_entity_by_uri
from ngsi_ld_models_mdt_client_data_materialization.models.protocol import Protocol
from ngsi_ld_models_mdt_client_data_materialization.models.rpc_operation import RpcOperation
from ngsi_ld_models_mdt_client_data_materialization.models.credentials import Credentials

from ngsi_ld_models_ietf_interfaces.models.interface_config import InterfaceConfig
from ngsi_ld_models_ietf_interfaces.models.interface_config_ipv4 import InterfaceConfigIpv4
from ngsi_ld_models_ietf_interfaces.models.interface_config_ipv4_address import InterfaceConfigIpv4Address
from ngsi_ld_models_ietf_interfaces.models.interface_config_ipv6 import InterfaceConfigIpv6
from ngsi_ld_models_ietf_interfaces.models.interface_config_ipv6_address import InterfaceConfigIpv6Address
from ngsi_ld_models_ietf_interfaces.models.interface_config_ipv6_autoconf import InterfaceConfigIpv6Autoconf
from ngsi_ld_models_ietf_interfaces.models.interface_config_ipv6_neighbor import InterfaceConfigIpv6Neighbor

import datetime
#from datetime import datetime,timezone
from dateutil import parser
import asyncio
import threading
import jinja2
from jinja2 import Template

from kafka import KafkaProducer

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

# Dictionary to maintain the threads of execution associated with each NGSI-LD NETCONF entity
subscription_threads = {}

# ncclient parameters
host = ""
port = ""
username = ""
password = ""
family = ""
entityType = ""
entityId = ""
hostKeyVerify = ""

# NGSI-LD Context Broker
#BROKER_URI = os.getenv("BROKER_URI", "http://orion:1026/ngsi-ld/v1")
BROKER_URI = os.getenv("BROKER_URI", "http://scorpio:9090/ngsi-ld/v1")

# Context Catalog
CONTEXT_CATALOG_URI = os.getenv("CONTEXT_CATALOG_URI",
                                "http://context-catalog:8080/context.jsonld")

# Notifier
NOTIFIER_URI = os.getenv("NOTIFIER_URI", "http://netconf-network-controller-materialization:8089/notify")

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

LIST_ENTITIES = [
    "Protocol",
    "Credentials",
    "RpcOperation"
]
    
# Init FastAPI server
app = FastAPI(
    title="NETCONF Network Controller Materializaton API",
    version="1.0.0")

'''
Startup function for subscribing to the NGSI-LD Entity type called NETCONF that defines the NETCONF client parameters.
In addition, this fuctions discover all the key-value pairs included within the context catalog microservice for declaring
the NGSI-LD @context.
'''
@app.on_event("startup")
async def startup_event():
    global all_context_data
    global all_context_registries
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
Function for subscribe to NGSI-LD entities. This is useful for subscribing to NGSI-LD entities when triggering the NETCONF
Get/Get-Config RPC operations in order to support NETCONF Set RPC operations.
'''
async def subscribe_to_entity(entity: str, entity_id: str):
    endpoint = Endpoint(
        uri = NOTIFIER_URI,
        accept="application/json"
    )

    entity_type_short = get_entity_type_short_in_context_catalog(entity, all_context_data)

    # On-Change Subscriptions
    notification_params = NotificationParams (
        endpoint=endpoint,
        format="normalized",
        #attributes=[""],
        sysAttrs=False
    )

    entity_dict = {"type": entity}

    '''
    BLOCKED!
    Currently, subscription operations to NGSI-LD entities by indicating their ID are not supported by Scorpio Context Broker.
    There is an issue recently opened on GitHub: https://github.com/ScorpioBroker/ScorpioBroker/issues/621
    '''
    '''
    if entity_id is not None:
        entity_dict["id"] = entity_id
        entity_id_split = entity_id.split(":")
        entity_id_start_index = entity_id_split.index(entity) + 1
    
    if entity_id is not None:
        id = "urn:ngsi-ld:Subscription:{0}:{1}".format(entity, ":".join(entity_id_split[entity_id_start_index:]))
        description="On-change subscription to " + entity + " entity with ID " + entity_id + "."
    '''

    #else:
    id = "urn:ngsi-ld:Subscription:{0}".format(entity_type_short)
    description="On-change subscription to " + entity_type_short + " entity."

    subs_request = CreateSubscriptionRequest (
        id=id,
        type="Subscription",
        entities=[entity_dict],
        description=description,
        #watchedAttributes=[""],
        notificationTrigger=['entityCreated', 'entityUpdated', 'attributeCreated', 'attributeUpdated'],
        #notificationTrigger=['entityCreated', 'entityUpdated', 'entityDeleted', 'attributeCreated', 'attributeUpdated', 'attributeDeleted'],
        notification=notification_params
    )

    ngsi_ld_api_instance_subscription.create_subscription(create_subscription_request=subs_request)

'''
Main function for controlling the lifecycle of the NETCONF RPC operations by using the NGSI-LD API by 
defining the customize NGSI-LD information model for NETCONF clients. The network controller is based on 
a data materialization approach and supports all the RPC operations defined by the NETCONF management protocol.
'''
@app.post("/notify",
          status_code=status.HTTP_200_OK)
async def receiveNotification(request: Request):
    global host
    global port
    global username
    global password
    global family
    global entityType
    global entityId
    global hostKeyVerify 
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
        elif entity["type"] == "RpcOperation":
            try:
                entity_match = RpcOperation.from_dict(entity)
                entity_input = entity_match.to_dict()
                logger.info("Entity object representation: %s\n" % Entity.from_dict(entity_input))
                logger.info("Entity notification: %s\n" % entity)
                entity_id = entity["id"]
                family = "csr"
                hostKeyVerify = False
                entity_id = entity["id"]

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
                
                if api_response != None:
                '''
                if "GET" in entity["operation"]["value"] and "deletedAt" not in entity:
                    if "getOption" in entity["operation"]:
                        option = entity["operation"]["getOption"]["value"]

                        if "entityType" in entity["operation"]:
                            entityType = entity["operation"]["entityType"]["value"]
                        else:
                            entityType = None

                        if "entityId" in entity["operation"]:
                            entityId = entity["operation"]["entityId"]["value"]
                        else:
                            entityId = None
                
                        if search_entity_type_short_in_context_catalog_given_long_version(entityType, all_context_data):
                            
                            entity_type_short_ocurrences = get_ocurrences_entity_type_short_in_context_catalog(entityType, all_context_data, all_context_registries)
                            config = discover_config_entity_by_uri(entityType, all_context_registries)

                            if (entity_type_short_ocurrences == 1 and config == True and (option == "config" or option == "edit-config")) or (entity_type_short_ocurrences == 1 and config == False and option == "state") or (entity_type_short_ocurrences == 2 and (option == "config" or option == "edit-config" or option == "state")):

                                get_operation(host, port, username, password, family, entityType, entityId, option, all_context_data, hostKeyVerify, all_context_registries)
                            
                                if option == "edit-config":
                                    subs_entity = entityType
                                    new_entity_id = None
                                    attemps = 0
                                    while True:
                                        try:
                                            attemps = attemps + 1
                                            entities = ngsi_ld_api_instance_consumption.query_entity(type=subs_entity)
                                            if entities != []:
                                                if entityId is not None:
                                                    entityId_items = entityId.split(":")[4:]
                                                    for entity in entities:
                                                        segmented_entity_id = entity.to_dict()["id"].split(":")[4:]
                                                        aux_new_entity_id = ""
                                                        matched = False
                                                        if len(segmented_entity_id) == len(entityId_items):
                                                            for entityId_item, segmented_entity_id_item in zip(entityId_items, segmented_entity_id):
                                                                if segmented_entity_id_item == entityId_item:
                                                                    matched = True
                                                                    aux_new_entity_id = aux_new_entity_id + ":" + segmented_entity_id_item
                                                                else:
                                                                    matched = False
                                                                    break
                                                        if matched:
                                                            new_entity_id = str(":".join(entity.to_dict()["id"].split(":")[:4])) + aux_new_entity_id
                                                            break
                                                    if new_entity_id is not None:
                                                        logger.info("Create NGSI-LD subscription to Entity of type " + subs_entity + " with id " + new_entity_id + " for NETCONF SET RPC operation...")
                                                        asyncio.create_task(subscribe_to_entity(subs_entity, new_entity_id))
                                                        break
                                                    else:
                                                        if entityId is not None:
                                                            entityId_items = entityId.split(":")[4:]
                                                            aux_new_entity_id = ""
                                                            for entityId_item in entityId_items:
                                                                aux_new_entity_id = aux_new_entity_id + ":" + entityId_item
                                                            if aux_new_entity_id != "":
                                                                new_entity_id = "urn:ngsi-ld:" + subs_entity + ":" + host + aux_new_entity_id
                                                            if new_entity_id is not None:
                                                                logger.info("Create NGSI-LD subscription to Entity of type " + subs_entity + " with id " + new_entity_id + " for NETCONF SET RPC operation...")
                                                                asyncio.create_task(subscribe_to_entity(subs_entity, new_entity_id))
                                                            break
                                                        else: 
                                                            logger.info("Create NGSI-LD subscription to Entity of type " + subs_entity + " for NETCONF SET RPC operation...")
                                                            asyncio.create_task(subscribe_to_entity(subs_entity, new_entity_id))
                                                            break
                                                else:
                                                    logger.info("Create NGSI-LD subscription to Entity of type " + subs_entity + " for NETCONF SET RPC operation...")
                                                    asyncio.create_task(subscribe_to_entity(subs_entity, new_entity_id))
                                                    break
                                            elif attemps < 3:
                                                sleep(0.5)
                                                continue
                                            else:
                                                if entityId is not None:
                                                    entityId_items = entityId.split(":")[4:]
                                                    aux_new_entity_id = ""
                                                    for entityId_item in entityId_items:
                                                        aux_new_entity_id = aux_new_entity_id + ":" + entityId_item
                                                    if aux_new_entity_id != "":
                                                        new_entity_id = "urn:ngsi-ld:" + subs_entity + ":" + host + aux_new_entity_id
                                                    if new_entity_id is not None:
                                                        logger.info("Create NGSI-LD subscription to Entity of type " + subs_entity + " with id " + new_entity_id + " for NETCONF SET RPC operation...")
                                                        asyncio.create_task(subscribe_to_entity(subs_entity, new_entity_id))
                                                    break
                                                else: 
                                                    logger.info("Create NGSI-LD subscription to Entity of type " + subs_entity + " for NETCONF SET RPC operation...")
                                                    asyncio.create_task(subscribe_to_entity(subs_entity, new_entity_id))
                                                    break                              
                                        except Exception as e:
                                            logger.exception("Exception when calling ContextInformationConsumptionApi->query_entity: %s\n" % e)
                            
                    # Delete NGSI-LD Entity by id: DELETE /entities/{entityId}
                    try:
                        ngsi_ld_api_instance_provision.delete_entity(entity_id=entity_id)
                    except Exception as e:
                        logger.error("Exception when calling ContextInformationProvisionApi->delete_entity: %s\n" % e)    
                elif "SUBSCRIBE" in entity["operation"]["value"] and "ON" in entity["operation"]["subscriptionState"]["value"] and "deletedAt" not in entity:
                    entityType= entity["operation"]["entityType"]["value"]
                    entityId= entity["operation"]["entityId"]["value"]
                    subscriptionMode = entity["operation"]["subscriptionMode"]["value"]
                    if subscriptionMode == "periodic":
                        period = entity["operation"]["subscriptionMode"]["period"]["value"]

                    if search_entity_type_short_in_context_catalog_given_long_version(entityType, all_context_data):
                        # Check if there is already a subscription associated with this entity and stop it
                        if entity_id in subscription_threads:
                            logger.info(f"Restarting subscription for {entity_id}")
                            subscription_threads[entity_id]["stop_event"].set()  
                            subscription_threads[entity_id]["thread"].join() # Wait for the previous thread to finish
                            subscription_threads[entity_id]["stop_event"].clear()

                        # Create a new subscription
                        logger.info(f"Starting new subscription for {entity_id}")
                        asyncio.create_task(subscribe_operation(host, port, username, password, family, entityType, entityId, subscriptionMode, period, entity_id, all_context_data, hostKeyVerify, all_context_registries))

                elif "SUBSCRIBE" in entity["operation"]["value"] and "IDLE" in entity["operation"]["subscriptionState"]["value"] and "deletedAt" not in entity:
                    # If an "idle" message arrives, we stop the loop
                    # Check if there is already a subscription associated with this entity and stop it
                    if entity_id in subscription_threads:
                        logger.info(f"Stopping pre-subscription for {entity_id}")
                        subscription_threads[entity_id]["stop_event"].set()  
                        subscription_threads[entity_id]["thread"].join() # Esperar a que termine el hilo anterior
                        # Remove from the subscription thread dictionary
                        del subscription_threads[entity_id]
                
                elif "SUBSCRIBE" in entity["operation"]["value"] and "OFF" in entity["operation"]["subscriptionState"]["value"] and "deletedAt" not in entity:
                    # If an "off" message arrives, we stop the loop and delete the entity
                    # Check if there is already a subscription associated with this entity and stop it
                    if entity_id in subscription_threads:
                        logger.info(f"Stopping pre-subscription for {entity_id}")
                        subscription_threads[entity_id]["stop_event"].set()  
                        subscription_threads[entity_id]["thread"].join() # Esperar a que termine el hilo anterior
                        # Remove from the subscription thread dictionary
                        del subscription_threads[entity_id]
                    
                    # Delete NGSI-LD Entity by id: DELETE /entities/{entityId}
                    try:
                        ngsi_ld_api_instance_provision.delete_entity(entity_id=entity_id)
                    except Exception as e:
                        logger.exception("Exception when calling ContextInformationProvisionApi->delete_entity: %s\n" % e)  
                elif "SUBSCRIBE" in entity["operation"]["value"] and entity["deletedAt"] is not None:
                    # If we delete the NETCONF entity, we stop the loop
                    # Check if there is already a subscription associated with this entity and stop it
                    if entity_id in subscription_threads:
                        logger.info(f"Stopping pre-subscription for {entity_id}")
                        subscription_threads[entity_id]["stop_event"].set()  
                        if subscription_threads[entity_id]["thread"] is not None:
                            subscription_threads[entity_id]["thread"].join() # Esperar a que termine el hilo anterior
                        # Remove from the subscription thread dictionary
                        del subscription_threads[entity_id]
                '''
                else:
                    logger.info("Entity of type RpcOperation with id " + entity_id + " has not a valid protocol associated!")
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
        else:
            try:
                entity_match = get_entity_class_object_by_type(entity)
                entity_input = entity_match.to_dict()
                logger.info("Entity object representation: %s\n" % Entity.from_dict(entity_input))
                logger.info("Entity notification: %s\n" % entity)
                entityId = entity["id"]

                subscriptions = ngsi_ld_api_instance_subscription.query_subscription()
                for subscription in subscriptions:
                   if str(subscription.to_dict()["id"]).startswith("urn:ngsi-ld:Subscription:"+str(entity["type"])):
                       ngsi_ld_api_instance_subscription.delete_subscription(subscription_id=str(subscription.to_dict()["id"]))
                set_operation(host=host, port=port, username=username, password=password, family=family, instance=entity_match, entity_type=entityType, entity_id=entityId, all_context_data=all_context_data, all_context_registries=all_context_registries)
            except ValidationError as e:
                logger.error("Validation error: %s\n" % e)

'''
Function for triggering NETCONF RPC YANG-Push subscriptions with needed parameters.
'''
async def subscribe_operation(host: str, port: str, username: str, password: str, family: str, entityType: str, entityId: str, subscriptionMode: str, period: str, entity_id: str, all_context_data: Optional[dict] = None, hostKeyVerify: Optional[bool] = False, all_context_registries: Optional[list] = None):
    # Each subscription will have its own stop event
    stop_event = asyncio.Event()

    # Save the event and thread in the global dictionary to control this subscription
    subscription_threads[entity_id] = {"stop_event": stop_event, "thread": None}

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
    
    xpath, entity_type_short  = get_xpath_in_context_catalog(entity_type=entityType, all_context_data=all_context_data)

    if entity_id != None:
        xpath = get_xpath_with_keys(xpath=xpath, entity_id=entityId, all_context_registries=all_context_registries)
    
    # Try first a get RPC operation:
    try:
        # Execute the get RPC
        reply = session.get(filter=('xpath', xpath))
        logger.info("\nInterface operational status of network device " + host + ": \n")
        logger.info(reply)
        data_element = et.fromstring(str(reply)).find('.//{urn:ietf:params:xml:ns:netconf:base:1.0}data')
        if data_element is None or len(data_element) == 0:
            logger.info("\nThe Xpath is incorrect or not supported by the network device " + host + ".")
            try:
                ngsi_ld_api_instance_provision.delete_entity(entity_id=entity_id)
            except Exception as e:
                logger.exception("Exception when calling ContextInformationProvisionApi->delete_entity: %s\n" % e)  
            session.close_session()
            return

    except Exception as e:
        logger.exception(f"Error for establishing the Get Config operation: {e}")
        # Delete NGSI-LD Entity by id: DELETE /entities/{entityId}
        try:
            ngsi_ld_api_instance_provision.delete_entity(entity_id=entity_id)
        except Exception as e:
            logger.exception("Exception when calling ContextInformationProvisionApi->delete_entity: %s\n" % e)  
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
    subscription_template = Template(open('./netconf_network_controller_materialization/jinja2-templates/yang-push-subscriptions.xml').read())
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
        # Delete NGSI-LD Entity by id: DELETE /entities/{entityId}
        try:
            ngsi_ld_api_instance_provision.delete_entity(entity_id=entity_id)
        except Exception as e:
            logger.exception("Exception when calling ContextInformationProvisionApi->delete_entity: %s\n" % e)  
        session.close_session()
        return

    producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

    # Run the receive notification function in a separate thread
    notification_thread = threading.Thread(target=get_notifications, args=(session, producer, host, entity_id))
    subscription_threads[entity_id]["thread"] = notification_thread
    notification_thread.start()

    # Wait until the stop event is triggered
    await stop_event.wait()

    # Once the event is triggered, stop the thread
    notification_thread.join()
    session.close_session()

    logger.info(f"Stopped subscription for {host}")

'''
Function for receiving notifications of previously triggered NETCONF RPC YANG-Push subscription operations.
'''
def get_notifications(session, producer, host, entity_id):
    stop_event = subscription_threads[entity_id]["stop_event"]
    while not stop_event.is_set():
        try:
            # Here you can modify the timeout if it is supported
            sub_data = session.take_notification(timeout=10)
            if sub_data is not None:
                logger.info("\nI have received a notification!\n")
                notification_xml = str(sub_data.notification_xml)
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
                producer.send('interfaces-state-subscriptions', value=notification_xml.encode('utf-8'))
                logger.info("I have sent it to a Kafka topic named interfaces-state-subscriptions")
                logger.info("The new eventTime element of the notification is: " + current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))

                producer.flush()
            else:
                logger.info("No notification received in this cycle")
        except Exception as e:
            logger.exception(f"Error receiving notification: {str(e)}")

    logger.info("Notification thread has been stopped")

'''
Search short version of Entity type (i.e., type name) given the long version (i.e., type URI) by searching along the context registries within from Context Catalog:
'''
def search_entity_type_short_in_context_catalog_given_long_version(entity_type_long: str, all_context_data: Optional[dict]) -> bool:

    entity_type_short_founded = False
    for key, value in all_context_data.items():
        if value == entity_type_long:
            entity_type_short = key
            logger.info(f"NGSI-LD Entity type name {entity_type_short} relative to NGSI-LD Entity type URI {entity_type_long} was founded!")
            entity_type_short_founded = True
            break
    if entity_type_short_founded == False:
        logger.info(f"NGSI-LD Entity type name relative to NGSI-LD Entity type URI {entity_type_long} was not founded!")

    return entity_type_short_founded

'''
Get short version of Entity type (i.e., type name) given the long version (i.e., type URI) by searching along the context registries within from Context Catalog:
'''
def get_entity_type_short_in_context_catalog(entity_type_long: str, all_context_data: Optional[dict]) -> str:

    entity_type_short = ""
    for key, value in all_context_data.items():
        if value == entity_type_long:
            entity_type_short = key
            logger.info(f"NGSI-LD Entity type name {entity_type_short} relative to NGSI-LD Entity type URI {entity_type_long} was founded!")
            break
    if entity_type_short == "":
        logger.info(f"NGSI-LD Entity type name relative to NGSI-LD Entity type URI {entity_type_long} was not founded!")

    return entity_type_short

'''
Get ocurrences of short version of Entity type (i.e., type name) given the long version (i.e., type URI) by searching along the context registries within from Context Catalog:
'''
def get_ocurrences_entity_type_short_in_context_catalog(entity_type_long: str, all_context_data: Optional[dict], all_context_registries: Optional[list]) -> int:

    entity_type_short = ""
    entity_type_short_ocurrences = 0
    for key, value in all_context_data.items():
        if value == entity_type_long:
            entity_type_short = key
            for context_registry in all_context_registries:
                if entity_type_short in context_registry["@context"].keys():
                     entity_type_short_ocurrences += 1
            
            logger.info(f"NGSI-LD Entity type name {entity_type_short} relative to NGSI-LD Entity type URI {entity_type_long} was founded " + str(entity_type_short_ocurrences) + " times!")
            break
    if entity_type_short == "":
        logger.info(f"NGSI-LD Entity type name relative to NGSI-LD Entity type URI {entity_type_long} was not founded!")

    return entity_type_short_ocurrences

'''
Get the entity type name of a NGSI-LD Entity provided as a Python dictionary:
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
