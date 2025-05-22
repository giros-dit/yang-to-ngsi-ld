import logging
import os
from time import sleep
import time
from fastapi import FastAPI, HTTPException, Request, status
import json
import csv
import ngsi_ld_client
from ngsi_ld_client.models.create_subscription_request import CreateSubscriptionRequest
from ngsi_ld_client.models.subscription_on_change import SubscriptionOnChange
from ngsi_ld_client.models.subscription_periodic import SubscriptionPeriodic
from ngsi_ld_client.models.notification_params import NotificationParams
from ngsi_ld_client.models.endpoint import Endpoint
from ngsi_ld_client.api_client import ApiClient as NGSILDClient
from ngsi_ld_client.configuration import Configuration as NGSILDConfiguration
from netconf_notifier_tester_virtualization_periodic_context_broker.check_client import NGSILDHealthInfoClient
#from datetime import datetime,timezone
import datetime
from dateutil import parser
import gzip

from ngsi_ld_client.models.query_entity200_response_inner import QueryEntity200ResponseInner

from ngsi_ld_models_mdt_client_data_virtualization.models.protocol import Protocol
from ngsi_ld_models_mdt_client_data_virtualization.models.name import Name
from ngsi_ld_models_mdt_client_data_virtualization.models.address import Address
from ngsi_ld_models_mdt_client_data_virtualization.models.port import Port
from ngsi_ld_models_mdt_client_data_virtualization.models.username import Username
from ngsi_ld_models_mdt_client_data_virtualization.models.password import Password

from ngsi_ld_models_mdt_client_data_virtualization.models.credentials import Credentials
from ngsi_ld_models_mdt_client_data_virtualization.models.subscribe_rpc_template import SubscribeRpcTemplate
from ngsi_ld_models_mdt_client_data_virtualization.models.subscription_mode import SubscriptionMode
from ngsi_ld_models_mdt_client_data_virtualization.models.period import Period

delta_times = []
notification_delta_times = []

logger = logging.getLogger(__name__)

# NGSI-LD Context Broker
#BROKER_URI = os.getenv("BROKER_URI", "http://orion:1026/ngsi-ld/v1")
BROKER_URI = os.getenv("BROKER_URI", "http://scorpio:9090/ngsi-ld/v1")

# Context Catalog
CONTEXT_CATALOG_URI = os.getenv("CONTEXT_CATALOG_URI",
                                "http://context-catalog:8080/context.jsonld")

# Notifier
NOTIFIER_URI = os.getenv("NOTIFIER_URI", "http://netconf-notifier-tester-virtualization-periodic:8082/notify")

# Init NGSI-LD Client
configuration = NGSILDConfiguration(host=BROKER_URI)
configuration.debug = True
ngsi_ld = NGSILDClient(configuration=configuration)

ngsi_ld_health_info_api = NGSILDHealthInfoClient(
    url="http://scorpio:9090",
    headers={"Accept": "application/json"},
    context="http://context-catalog:8080/context.jsonld")

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

LIST_ENTITIES = [
    "InterfaceStatistics"
]

performance_measurements_file = open("/opt/netconf-notifier-tester-virtualization-periodic-context-broker/netconf_notifier_tester_virtualization_periodic_context_broker/performance_measurements.csv", "w", newline='')
csv_writer = csv.writer(performance_measurements_file)
csv_header = ["observed_at", "modified_at", "evaluation_time", "mean_evaluation_time",
              "min_evaluation_time", "max_evaluation_time", "notifications_received"]
csv_writer.writerow(csv_header)  
    
notification_performance_measurements_file = open("/opt/netconf-notifier-tester-virtualization-periodic-context-broker/netconf_notifier_tester_virtualization_periodic_context_broker/notification_performance_measurements.csv", "w", newline='')
notification_csv_writer = csv.writer(notification_performance_measurements_file)
notification_csv_header = ["observed_at", "notified_at", "evaluation_time", "mean_evaluation_time",
              "min_evaluation_time", "max_evaluation_time", "notifications_received"]
notification_csv_writer.writerow(notification_csv_header)  

# Init FastAPI server
app = FastAPI(
    title="Notifier Tester API",
    version="1.0.0")

@app.on_event("startup")
async def startup_event():
    
    # Check if Scorpio API is up
    ngsi_ld_health_info_api.check_scorpio_status()

    # Check Scorpio build info
    ngsi_ld_health_info_api.check_scorpio_info()

    sleep(1)

    api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

    protocol_instance = Protocol(
        type="Protocol",
        id="urn:ngsi-ld:Protocol:r1",
        name=Name.from_dict({"type": "Property", "value": "netconf"}),
        address=Address.from_dict({"type": "Property", "value": "clab-telemetry-ixiac-lab-r1"}),
        port=Port.from_dict({"type": "Property", "value": 830}),
        hasCredentials={"type": "Relationship", "object": "urn:ngsi-ld:Credentials:r1"}
    )

    entity_input = protocol_instance.to_dict()
    query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)
    try:
        # Create NGSI-LD entity of type Protocol: POST /entities
        api_instance.create_entity(query_entity200_response_inner=query_entity_input)
    except Exception as e:
        logger.exception("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)
        

    credentials_instance = Credentials(
        type="Credentials",
        id="urn:ngsi-ld:Credentials:r1",
        username=Username.from_dict({"type": "Property", "value":"admin"}),
        password=Password.from_dict({"type": "Property", "value":"admin"})
    )

    entity_input = credentials_instance.to_dict()
    query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)
    try:
        # Create NGSI-LD entity of type Credentials: POST /entities
        api_instance.create_entity(query_entity200_response_inner=query_entity_input)
    except Exception as e:
        logger.exception("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)
        
    subs_mode_instance = SubscriptionMode(
        type="Property",
        value="periodic",
        period=Period.from_dict({"type": "Property", "value": 5})
    )

    subscribe_rpc_template_instance = SubscribeRpcTemplate(
        type="SubscribeRpcTemplate",
        id="urn:ngsi-ld:SubscribeRpcTemplate:r1",
        subscriptionMode=subs_mode_instance,
        subscriptionState={"type": "Property", "value": "ON"},
        usesProtocol={"type": "Relationship", "object": "urn:ngsi-ld:Protocol:r1"}
    )

    entity_input = subscribe_rpc_template_instance.to_dict()
    query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)
    try:
        # Create NGSI-LD entity of type SubscribeRpcTemplate: POST /entities
        api_instance.create_entity(query_entity200_response_inner=query_entity_input)
    except Exception as e:
        logger.exception("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)
        
    endpoint = Endpoint(
        uri = NOTIFIER_URI,
        accept="application/json"
    )

    # Periodic Subscriptions
    notification_params = NotificationParams (
        endpoint=endpoint,
        format="normalized",
        #attributes=["inOctets"],
        sysAttrs=True
    )

    subs_request = CreateSubscriptionRequest (
        id="urn:ngsi-ld:Subscription:InterfaceStatistics",
        type="Subscription",
        entities=[
            {
                "type": "ietf-interfaces:interfaces-state/interface/statistics",
                "id": "urn:ngsi-ld:InterfaceStatistics:r1:GigabitEthernet2"
            }
        ],
        description="Periodic subscription to InterfaceStatistics entities.",
        timeInterval=5,
        notification=notification_params
    )
    

    # On-Change Subscriptions
    '''
    notification_params = NotificationParams (
        endpoint=endpoint,
        format="normalized",
        #attributes=["inOctets"],
        #sysAttrs=True
    )

    subs_request = CreateSubscriptionRequest (
        id="urn:ngsi-ld:Subscription:{0}".format(entity),
        type="Subscription",
        entities=[
            {
                "type": entity,
            }
        ],
        description="On-change subscription to InterfaceStatistics entities.",
        #watchedAttributes=["inOctets"],
        notification=notification_params
    )
    '''

    api_instance = ngsi_ld_client.ContextInformationSubscriptionApi(ngsi_ld)
    api_instance.create_subscription(create_subscription_request=subs_request)
    

@app.post("/notify",
          status_code=status.HTTP_200_OK)
async def receiveNotification(request: Request):
    logger.info(f"Headers: {request.headers}")
    content_encoding = request.headers.get("content-encoding", "").lower()
    try:
        body = await request.body()
        if content_encoding == "gzip":
            decompressed_body = gzip.decompress(body)
            notification = json.loads(decompressed_body.decode("utf-8"))
        else:
            notification = await request.json()
        logger.info("New notification: %s\n" % str(notification))
        for entity in notification["data"]:
            if entity["type"] == "InterfaceStatistics" or entity["type"] == "InterfaceConfig":
                logger.info("Entity notification: %s\n" % entity)
                current_datetime = datetime.datetime.now(datetime.timezone.utc)
                notification_datetime = current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
                logger.info("Entity notification datetime : %s\n" % notification_datetime)

                if (entity["type"] == "InterfaceStatistics" and "observedAt" in entity["inOctets"] and "modifiedAt" in entity["inOctets"]) or (entity["type"] == "InterfaceConfig" and "observedAt" in entity["enabled"] and "modifiedAt" in entity["enabled"]):
                    #current_time = datetime.utcnow().replace(tzinfo=timezone.utc).isoformat()
                    #logger.info(f"Current time: {parser.parse(current_time)}") 
                    #current_datetime = datetime.fromisoformat(current_time)   
                    #logger.info(f"Current time: {current_datetime}") 
                    if (entity["type"] == "InterfaceStatistics" and "observedAt" in entity["inOctets"] and "modifiedAt" in entity["inOctets"]):
                        observed_at = parser.parse(entity["inOctets"]["observedAt"])
                        modified_at = parser.parse(entity["inOctets"]["modifiedAt"])
                    elif (entity["type"] == "InterfaceConfig" and "observedAt" in entity["enabled"] and "modifiedAt" in entity["enabled"]):
                        observed_at = parser.parse(entity["enabled"]["observedAt"])
                        modified_at = parser.parse(entity["enabled"]["modifiedAt"])

                    delta_time = (modified_at - observed_at).total_seconds()
                    delta_times.append(delta_time)

                    logger.info("--- PERFORMANCE MEASUREMENTS ---\n")
                    logger.info("OBSERVED AT: " + observed_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
                    logger.info("MODIFIED AT: " + modified_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n") 
                    logger.info("NOTIFICATIONS RECEIVED SO FAR: " + str(len(delta_times)) + "\n")
                    logger.info(f"EVALUATION TIME: {delta_time * 1e3} ms\n")
                    mean_evaluation_time = sum(delta_times)/len(delta_times)
                    min_evaluation_time = min(delta_times)
                    max_evaluation_time = max(delta_times)
                    logger.info(f"MEAN EVALUATION TIME: {mean_evaluation_time * 1e3} ms\n")
                    logger.info(f"MIN EVALUATION TIME: {min_evaluation_time * 1e3} ms\n")
                    logger.info(f"MAX EVALUATION TIME VALUE: {max_evaluation_time * 1e3} ms\n")
                    logger.info("--- PERFORMANCE MEASUREMENTS ---")
                    
                    csv_data = [observed_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), modified_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                                str(delta_time * 1e3) + " ms", str(mean_evaluation_time * 1e3) + " ms",
                                str(min_evaluation_time * 1e3) + " ms", str(max_evaluation_time * 1e3) + " ms",
                                str(len(delta_times))]
                    csv_writer.writerow(csv_data)
                    performance_measurements_file.flush()

                    notification_delta_time = (current_datetime - observed_at).total_seconds()
                    notification_delta_times.append(notification_delta_time)
                    logger.info("--- PERFORMANCE MEASUREMENTS ---\n")
                    logger.info("OBSERVED AT: " + observed_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
                    logger.info("NOTIFIED AT: " + notification_datetime + "\n") 
                    logger.info("NOTIFICATIONS RECEIVED SO FAR: " + str(len(notification_delta_times)) + "\n")
                    logger.info(f"EVALUATION TIME: {notification_delta_time * 1e3} ms\n")
                    mean_evaluation_time = sum(notification_delta_times)/len(delta_times)
                    min_evaluation_time = min(notification_delta_times)
                    max_evaluation_time = max(notification_delta_times)
                    logger.info(f"MEAN EVALUATION TIME: {mean_evaluation_time * 1e3} ms\n")
                    logger.info(f"MIN EVALUATION TIME: {min_evaluation_time * 1e3} ms\n")
                    logger.info(f"MAX EVALUATION TIME VALUE: {max_evaluation_time * 1e3} ms\n")
                    logger.info("--- PERFORMANCE MEASUREMENTS ---")

                    notification_csv_data = [observed_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), notification_datetime,
                                str(notification_delta_time * 1e3) + " ms", str(mean_evaluation_time * 1e3) + " ms",
                                str(min_evaluation_time * 1e3) + " ms", str(max_evaluation_time * 1e3) + " ms",
                                str(len(notification_delta_times))]
                    notification_csv_writer.writerow(notification_csv_data)
                    notification_performance_measurements_file.flush()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid request: {str(e)}")