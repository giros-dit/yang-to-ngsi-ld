import logging
import os
from time import sleep
import time
from typing import Optional
from fastapi import FastAPI, Request, status, HTTPException
from fastapi.responses import JSONResponse
import json
import csv
import ngsi_ld_client
import ngsi_ld_models_ietf_interfaces
import ngsi_ld_models_netconf_client_data_materialization
from ngsi_ld_client.models.create_subscription_request import CreateSubscriptionRequest
from ngsi_ld_client.models.subscription_on_change import SubscriptionOnChange
from ngsi_ld_client.models.subscription_periodic import SubscriptionPeriodic
from ngsi_ld_client.models.notification_params import NotificationParams
from ngsi_ld_client.models.endpoint import Endpoint
from ngsi_ld_client.api_client import ApiClient as NGSILDClient
from ngsi_ld_client.configuration import Configuration as NGSILDConfiguration
from pydantic import ValidationError
from network_controller_materialization.check_client import NGSILDHealthInfoClient
from network_controller_materialization.context_client import ContextCatalogClient
from network_controller_materialization.ncclient_collector import get_operation, set_operation
from ngsi_ld_models_netconf_client_data_materialization.models.netconf import NETCONF
from ngsi_ld_models_ietf_interfaces.models.interface_config import InterfaceConfig
from ngsi_ld_models_ietf_interfaces.models.interface_config_ipv4_address import InterfaceConfigIpv4Address

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
xpath = ""
hostKeyVerify = ""

# NGSI-LD Context Broker
#BROKER_URI = os.getenv("BROKER_URI", "http://orion:1026/ngsi-ld/v1")
BROKER_URI = os.getenv("BROKER_URI", "http://scorpio:9090/ngsi-ld/v1")

# Context Catalog
CONTEXT_CATALOG_URI = os.getenv("CONTEXT_CATALOG_URI",
                                "http://context-catalog:8080/context.jsonld")

# Notifier
NOTIFIER_URI = os.getenv("NOTIFIER_URI", "http://network-controller-materialization:8089/notify")

# Init NGSI-LD Client
configuration = NGSILDConfiguration(host=BROKER_URI)
configuration.debug = True
ngsi_ld = NGSILDClient(configuration=configuration)
all_context_data = None

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
    "NETCONF"
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
    context_urls = context_client.fetch_data()
    if context_urls:
        context_client.search_context_urls(context_urls)
        all_context_data = context_client.search_context_data(context_urls)
    
    print("Key and value for each context URL:")
    for key, value in all_context_data.items():
        print(f"{key}: {value}")

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
            description="On-change subscription to NETCONF entity.",
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

    # On-Change Subscriptions
    notification_params = NotificationParams (
        endpoint=endpoint,
        format="normalized",
        #attributes=["inOctets"],
        sysAttrs=False
    )

    entity_dict = {"type": entity}
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
    id = "urn:ngsi-ld:Subscription:{0}".format(entity)
    description="On-change subscription to " + entity + " entity."

    subs_request = CreateSubscriptionRequest (
        id=id,
        type="Subscription",
        entities=[entity_dict],
        description=description,
        #watchedAttributes=["inOctets"],
        #notificationTrigger=['entityCreated', 'entityUpdated', 'attributeCreated', 'attributeUpdated'],
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
    global xpath
    global hostKeyVerify 
    global all_context_data
    notification = await request.json()
    for entity in notification["data"]:
        if entity["type"] == "NETCONF":
            try:
                entity_match = NETCONF.from_dict(entity)
                entity_input = entity_match.to_dict()
                logger.info("Entity object representation: %s\n" % Entity.from_dict(entity_input))
                logger.info("Entity notification: %s\n" % entity)
                host = entity["host"]["value"]
                port = entity["port"]["value"]
                username = entity["username"]["value"]
                password = entity["password"]["value"]
                family = entity["hostFamily"]["value"]
                
                if "hostKeyVerify" in entity:
                    hostKeyVerify = entity["hostKeyVerify"]["value"]
                else:
                    hostKeyVerify = False
                
                entity_id = entity["id"]

                if "GET" in entity["operation"]["value"] and "deletedAt" not in entity:
                    if "getOption" in entity["operation"]:
                        option = entity["operation"]["getOption"]["value"]
                        if "xpath" in entity["operation"]:
                            xpath = entity["operation"]["xpath"]["value"]
                        else:
                            xpath = None
                
                        get_operation(host, port, username, password, family, xpath, option, all_context_data, hostKeyVerify)
                        
                        if option == "edit-config":

                            processed_all_context_data = {}
                            for key, value in all_context_data.items():
                                if isinstance(value, str):  
                                    if ":" in value and not value.startswith(("urn:", "http:", "https:")):
                                        processed_all_context_data[key] = "/" + value.split(":", 1)[1]
                                    else:
                                        processed_all_context_data[key] = value
                                elif isinstance(value, list): 
                                    processed_all_context_data[key] = [
                                        ("/" + v.split(":", 1)[1] if ":" in v and not v.startswith(("urn:", "http:", "https:")) else v) 
                                        if isinstance(v, str) else v 
                                        for v in value
                                    ]
                                else: 
                                    processed_all_context_data[key] = value

                            is_match = False
                            match_key = None
                            if "[" in xpath and "]" in xpath:
                                xpath_filter = xpath.split('[')[0]+xpath.split(']')[1]
                            else:
                                xpath_filter = xpath
                            for key, value in processed_all_context_data.items():
                                if isinstance(value, str):
                                    if value == xpath_filter:
                                        is_match = True
                                        match_key = key
                                        break
                                elif isinstance(value, list): 
                                    for v in value:
                                        if v == xpath_filter:
                                            is_match = True
                                            match_key = key
                                            break

                            if is_match:
                                subs_entity = match_key
                                new_entity_id = None
                                attemps = 0
                                while True:
                                    try:
                                        attemps = attemps + 1
                                        entities = ngsi_ld_api_instance_consumption.query_entity(type=subs_entity)

                                        if entities != []:
                                        
                                            xpath_components = xpath.strip("/").split("/")
                                            xpath_item = ""
                                            for xpath_component in xpath_components:
                                                if "[" in xpath_component and "]" in xpath_component:
                                                    xpath_item = xpath_component
                                                    break
                                            if "[" in xpath_item and "]" in xpath_item:
                                                tag, condition = xpath_item.split('[')
                                                tag = tag.strip()
                                                condition = condition.strip(']').split('=')
                                                #attr_name = condition[0].strip()
                                                attr_value = condition[1].strip().strip("'")     
                                                for entity in entities:
                                                    if entity.to_dict()["id"].split(":")[-1] == attr_value:
                                                        new_entity_id = entity.to_dict()["id"]
                                                        break
                                                if new_entity_id is not None:
                                                    asyncio.create_task(subscribe_to_entity(subs_entity, new_entity_id))
                                                    break
                                                else:
                                                    break
                                            else:
                                                asyncio.create_task(subscribe_to_entity(subs_entity, new_entity_id))
                                                break
                                            
                                        elif attemps < 2:
                                            sleep(0.5)
                                            continue
                                        else:
                                            break
                                        
                                    except Exception as e:
                                        logger.exception("Exception when calling ContextInformationConsumptionApi->query_entity: %s\n" % e)
                        
                    # Delete NGSI-LD Entity by id: DELETE /entities/{entityId}
                    try:
                        ngsi_ld_api_instance_provision.delete_entity(entity_id=entity_id)
                    except Exception as e:
                        logger.exception("Exception when calling ContextInformationProvisionApi->delete_entity: %s\n" % e)    
                elif "SUBSCRIBE" in entity["operation"]["value"] and "ON" in entity["operation"]["state"]["value"] and "deletedAt" not in entity:
                    xpath = entity["operation"]["xpath"]["value"]
                    subscriptionMode = entity["operation"]["subscriptionMode"]["value"]
                    if subscriptionMode == "periodic":
                        period = entity["operation"]["subscriptionMode"]["period"]["value"]

                    # Check if there is already a subscription associated with this entity and stop it
                    if entity_id in subscription_threads:
                        logger.info(f"Restarting subscription for {entity_id}")
                        subscription_threads[entity_id]["stop_event"].set()  
                        subscription_threads[entity_id]["thread"].join() # Wait for the previous thread to finish
                        subscription_threads[entity_id]["stop_event"].clear()

                    # Create a new subscription
                    logger.info(f"Starting new subscription for {entity_id}")
                    asyncio.create_task(subscribe_operation(host, port, username, password, family, xpath, subscriptionMode, period, entity_id, hostKeyVerify))

                elif "SUBSCRIBE" in entity["operation"]["value"] and "IDLE" in entity["operation"]["state"]["value"] and "deletedAt" not in entity:
                    # If an "idle" message arrives, we stop the loop
                    # Check if there is already a subscription associated with this entity and stop it
                    if entity_id in subscription_threads:
                        logger.info(f"Stopping pre-subscription for {entity_id}")
                        subscription_threads[entity_id]["stop_event"].set()  
                        subscription_threads[entity_id]["thread"].join() # Esperar a que termine el hilo anterior
                        # Remove from the subscription thread dictionary
                        del subscription_threads[entity_id]
                
                elif "SUBSCRIBE" in entity["operation"]["value"] and "OFF" in entity["operation"]["state"]["value"] and "deletedAt" not in entity:
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
            except ValidationError as e:
                logger.error("Validation error: %s\n" % e)
                # Delete NGSI-LD Entity by id: DELETE /entities/{entityId}
                try:
                    ngsi_ld_api_instance_provision.delete_entity(entity_id=entity_id)
                except Exception as e:
                    logger.exception("Exception when calling ContextInformationProvisionApi->delete_entity: %s\n" % e)  
        elif entity["type"] == "InterfaceConfig":
            try:
                entity_match = InterfaceConfig.from_dict(entity)
                entity_input = entity_match.to_dict()
                logger.info("Entity object representation: %s\n" % Entity.from_dict(entity_input))
                logger.info("Entity notification: %s\n" % entity)
                entity_id = entity["id"]

                subscriptions = ngsi_ld_api_instance_subscription.query_subscription()
                for subscription in subscriptions:
                   if str(subscription.to_dict()["id"]).startswith("urn:ngsi-ld:Subscription:InterfaceConfig"):
                       ngsi_ld_api_instance_subscription.delete_subscription(subscription_id=str(subscription.to_dict()["id"]))

                set_operation(host=host, port=port, username=username, password=password, family=family, instance=entity_match, xpath=xpath, all_context_data=all_context_data)
            except ValidationError as e:
                logger.error("Validation error: %s\n" % e)
        elif entity["type"] == "InterfaceConfigIpv4Address":
            try:
                entity_match = InterfaceConfigIpv4Address.from_dict(entity)
                entity_input = entity_match.to_dict()
                logger.info("Entity object representation: %s\n" % Entity.from_dict(entity_input))
                logger.info("Entity notification: %s\n" % entity)
                entity_id = entity["id"]

                subscriptions = ngsi_ld_api_instance_subscription.query_subscription()
                for subscription in subscriptions:
                   if str(subscription.to_dict()["id"]).startswith("urn:ngsi-ld:Subscription:InterfaceConfigIpv4Address"):
                       ngsi_ld_api_instance_subscription.delete_subscription(subscription_id=str(subscription.to_dict()["id"]))

                set_operation(host=host, port=port, username=username, password=password, family=family, instance=entity_match, xpath=xpath, all_context_data=all_context_data)
            except ValidationError as e:
                logger.error("Validation error: %s\n" % e)

'''
Function for triggering NETCONF RPC YANG-Push subscriptions with needed parameters.
'''
async def subscribe_operation(host: str, port: str, username: str, password: str, family: str, xpath: str, subscriptionMode: str, period: str, entity_id: str, hostKeyVerify: Optional[bool] = False):
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
    
    xpath = xpath

    # Try first a get RPC operation:
    try:
        # Execute the get RPC
        reply = session.get(filter=('xpath', xpath))
        logger.info("\nInterface operational status of network device " + host + ": \n")
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
    subscription_template = Template(open('./network_controller_materialization/jinja2-templates/yang-push-subscriptions.xml').read())
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