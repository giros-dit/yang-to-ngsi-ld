import logging
import os
from time import sleep
import time
from fastapi import FastAPI, HTTPException, Request, status
import json
import csv
import datetime
import ngsi_ld_client
from ngsi_ld_client.models.create_subscription_request import CreateSubscriptionRequest
from ngsi_ld_client.models.subscription_on_change import SubscriptionOnChange
from ngsi_ld_client.models.subscription_periodic import SubscriptionPeriodic
from ngsi_ld_client.models.notification_params import NotificationParams
from ngsi_ld_client.models.endpoint import Endpoint
from ngsi_ld_client.api_client import ApiClient as NGSILDClient
from ngsi_ld_client.configuration import Configuration as NGSILDConfiguration
from notifier_tester_virtualization_on_change_context_source.check_client import NGSILDHealthInfoClient
#from datetime import datetime,timezone
from dateutil import parser
import gzip

from ngsi_ld_client.models.entity import Entity
from ngsi_ld_client.models.model_property import ModelProperty
from ngsi_ld_client.models.query_entity200_response_inner import QueryEntity200ResponseInner

from ngsi_ld_models_netconf_client_data_virtualization.models.netconf import NETCONF
from ngsi_ld_models_netconf_client_data_virtualization.models.subscription_mode import SubscriptionMode
from ngsi_ld_models_netconf_client_data_virtualization.models.period import Period

delta_times = []
notification_delta_times = []

logger = logging.getLogger(__name__)

# NGSI-LD Context Broker
#BROKER_URI = os.getenv("BROKER_URI", "http://orion:1026/ngsi-ld/v1")
BROKER_URI = os.getenv("BROKER_URI", "http://scorpio:9090/ngsi-ld/v1")
CONTEXT_SOURCE_URI = os.getenv("BROKER_URI", "http://network-controller-virtualization:8089/ngsi-ld/v1")

# Context Catalog
CONTEXT_CATALOG_URI = os.getenv("CONTEXT_CATALOG_URI",
                                "http://context-catalog:8080/context.jsonld")

# Notifier
NOTIFIER_URI = os.getenv("NOTIFIER_URI", "http://notifier-tester-virtualization-on-change-context-source:8082/notify")

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

performance_measurements_file = open("/opt/notifier-tester-virtualization-on-change-context-source/notifier_tester_virtualization_on_change_context_source/performance_measurements.csv", "w", newline='')
csv_writer = csv.writer(performance_measurements_file)
csv_header = ["observed_at", "modified_at", "evaluation_time", "mean_evaluation_time",
              "min_evaluation_time", "max_evaluation_time", "notifications_received"]
csv_writer.writerow(csv_header)  

notification_performance_measurements_file = open("/opt/notifier-tester-virtualization-on-change-context-source/notifier_tester_virtualization_on_change_context_source/notification_performance_measurements.csv", "w", newline='')
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

    api_instance_csource = ngsi_ld_client.ContextSourceDiscoveryApi(ngsi_ld)

    sleep(1)
    
    api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

    subs_mode_instance = SubscriptionMode(
        type="Property",
        value="periodic",
        period=Period.from_dict({"type": "Property", "value": 5})
    )

    netconf_client_instance = NETCONF(
        id="urn:ngsi-ld:NETCONF:r1",
        type="NETCONF",
        host={"type":"Property", "value": "clab-telemetry-ixiac-lab-r1"},
        port={"type":"Property", "value": 830},
        username={"type":"Property", "value": "admin"},
        password={"type":"Property", "value": "admin"},
        hostFamily={"type":"Property", "value": "csr"},
        hostKeyVerify={"type":"Property", "value": False},
        xpath={"type":"Property", "value": "/interfaces-state/interface[name='GigabitEthernet2']"},
        subscriptionMode=subs_mode_instance
    )

    entity_input = netconf_client_instance.to_dict()
    query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)
    try:
        # Create NGSI-LD entity of type NETCONF: POST /entities
        api_instance.create_entity(query_entity200_response_inner=query_entity_input)
    except Exception as e:
        logger.exception("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)
        
    csources = api_instance_csource.query_csr(type="InterfaceStatistics")
    print(csources)
    if csources != []:
        for csource in csources:
            csource_endpoint = csource.to_dict()["endpoint"]+"/ngsi-ld/v1"
            ngsi_ld_configuration_csource = NGSILDConfiguration(host=csource_endpoint)
            ngsi_ld_configuration_csource.debug = True
            ngsi_ld_csource = NGSILDClient(configuration=ngsi_ld_configuration_csource)

            endpoint = Endpoint(
                uri = NOTIFIER_URI,
                accept="application/json"
            )

            # Periodic Subscriptions
            '''
            notification_params = NotificationParams (
                endpoint=endpoint,
                format="normalized",
                #attributes=["inOctets"],
                sysAttrs=True
            )

            subs_request = CreateSubscriptionRequest (
                id="urn:ngsi-ld:Subscription:Periodic:{0}".format(entity),
                type="Subscription",
                entities=[
                    {
                        "type": entity
                    }
                ],
                description="Periodic subscription to InterfaceStatistics entities.",
                timeInterval= 10,
                notification=notification_params
            )
            '''

            # On-Change Subscriptions
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
                        "type": "InterfaceStatistics",
                        "id": "urn:ngsi-ld:InterfaceStatistics:clab-telemetry-ixiac-lab-r1:GigabitEthernet2"
                    }
                ],
                description="On-change subscription to InterfaceStatistics entities.",
                #watchedAttributes=["inOctets"],
                notification=notification_params
            )
            
            api_instance = ngsi_ld_client.ContextInformationSubscriptionApi(ngsi_ld_csource)
            api_instance.create_subscription(create_subscription_request=subs_request)
    

@app.post("/notify",
          status_code=status.HTTP_200_OK)
async def receiveNotification(request: Request):
    #notification = await request.json()
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
            if entity["type"] == "InterfaceStatistics" or entity["type"] == "Interface" :
                logger.info("Entity notification: %s\n" % entity)
                current_datetime = datetime.datetime.now(datetime.timezone.utc)
                notification_datetime = current_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
                logger.info("Entity notification datetime : %s\n" % notification_datetime)
                if (entity["type"] == "InterfaceStatistics" and "observedAt" in entity["inOctets"] and "modifiedAt" in entity["inOctets"]) or (entity["type"] == "Interface" and "observedAt" in entity["name"] and "modifiedAt" in entity["name"]) :
                    #current_time = datetime.utcnow().replace(tzinfo=timezone.utc).isoformat()
                    #logger.info(f"Current time: {parser.parse(current_time)}") 
                    #current_datetime = datetime.fromisoformat(current_time)   
                    #logger.info(f"Current time: {current_datetime}") 

                    if entity["type"] == "InterfaceStatistics":
                        observed_at = parser.parse(entity["inOctets"]["observedAt"])
                        modified_at = parser.parse(entity["inOctets"]["modifiedAt"])
                    elif entity["type"] == "Interface":
                        observed_at = parser.parse(entity["name"]["observedAt"])
                        modified_at = parser.parse(entity["name"]["modifiedAt"])

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

                elif (entity["type"] == "InterfaceStatistics" and "observedAt" in entity["inOctets"]) or (entity["type"] == "Interface" and "observedAt" in entity["name"]):
                    #current_time = datetime.utcnow().replace(tzinfo=timezone.utc).isoformat()
                    #logger.info(f"Current time: {parser.parse(current_time)}") 
                    #current_datetime = datetime.fromisoformat(current_time)   
                    #logger.info(f"Current time: {current_datetime}") 

                    if entity["type"] == "InterfaceStatistics":
                        observed_at = parser.parse(entity["inOctets"]["observedAt"])
                    elif entity["type"] == "Interface":
                        observed_at = parser.parse(entity["name"]["observedAt"])
                    notification_delta_time = (current_datetime - observed_at).total_seconds()
                    notification_delta_times.append(notification_delta_time)
                    logger.info("--- PERFORMANCE MEASUREMENTS ---\n")
                    logger.info("OBSERVED AT: " + observed_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
                    logger.info("NOTIFIED AT: " + notification_datetime + "\n") 
                    logger.info("NOTIFICATIONS RECEIVED SO FAR: " + str(len(notification_delta_times)) + "\n")
                    logger.info(f"EVALUATION TIME: {notification_delta_time * 1e3} ms\n")
                    mean_evaluation_time = sum(notification_delta_times)/len(notification_delta_times)
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
