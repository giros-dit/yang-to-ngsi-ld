import logging
import os
from time import sleep
import time
from fastapi import FastAPI, Request, status
import json
import ngsi_ld_client
from ngsi_ld_client.models.create_subscription_request import CreateSubscriptionRequest
from ngsi_ld_client.models.subscription_on_change import SubscriptionOnChange
from ngsi_ld_client.models.subscription_periodic import SubscriptionPeriodic
from ngsi_ld_client.models.notification_params import NotificationParams
from ngsi_ld_client.models.endpoint import Endpoint
from ngsi_ld_client.api_client import ApiClient as NGSILDClient
from ngsi_ld_client.configuration import Configuration as NGSILDConfiguration
from notifier_tester.check_client import NGSILDHealthInfoClient
from datetime import datetime,timezone
from dateutil import parser

TOTAL_ITERATIONS = 10
CURRENT_ITERATION = 0
evaluation_delta_times = []

logger = logging.getLogger(__name__)

# NGSI-LD Context Broker
#BROKER_URI = os.getenv("BROKER_URI", "http://orion:1026/ngsi-ld/v1")
BROKER_URI = os.getenv("BROKER_URI", "http://scorpio:9090/ngsi-ld/v1")

# Context Catalog
CONTEXT_CATALOG_URI = os.getenv("CONTEXT_CATALOG_URI",
                                "http://context-catalog:8080/context.jsonld")

# Notifier
NOTIFIER_URI = os.getenv("NOTIFIER_URI", "http://notifier-tester:8082/notify")

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

def calculate_delta(delta_times, current_iteration):
    if current_iteration == TOTAL_ITERATIONS:
        global CURRENT_ITERATION
        CURRENT_ITERATION = 0
        logger.info(f"EVALUATION TIMES - SUMMARY (OVER {len(delta_times)} ITERATIONS)")
        evaluation_mean_exec_time = sum(delta_times)/len(delta_times)
        evaluation_min_exec_time = min(delta_times)
        evaluation_max_exec_time = max(delta_times)
        evaluation_total_exec_time = sum(delta_times)
        logger.info(f"MEAN VALUE: {evaluation_mean_exec_time} s | {evaluation_mean_exec_time*1e3} ms | {evaluation_mean_exec_time*1e6} µs")
        logger.info(f"MIN VALUE: {evaluation_min_exec_time} s | {evaluation_min_exec_time*1e3} ms | {evaluation_min_exec_time*1e6} µs")
        logger.info(f"MAX VALUE: {evaluation_max_exec_time} s | {evaluation_max_exec_time*1e3} ms | {evaluation_max_exec_time*1e6} µs")
        logger.info(f"TOTAL EXECUTION TIME: {evaluation_total_exec_time} s | {evaluation_total_exec_time*1e3} ms | {evaluation_total_exec_time*1e6} µs")
    
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

    for entity in LIST_ENTITIES:
        endpoint = Endpoint(
            uri = NOTIFIER_URI,
            accept="application/json"
        )

        # Periodic Subscriptions
        notification_params = NotificationParams (
            endpoint=endpoint,
            format="normalized",
            attributes=["inOctets"],
            sysAttrs=True
        )

        subs_request = CreateSubscriptionRequest (
            id="urn:ngsi-ld:Subscription:Periodic:{0}".format(entity),
            type="Subscription",
            entities=[{ "type": entity, "id": "urn:ngsi-ld:InterfaceStatistics:GigabitEthernet1" }],
            description="Periodic subscription to InterfaceStatistics entities.",
            timeInterval= 10,
            notification=notification_params
        )

        # On-Change Subscriptions        
        """
        notification_params = NotificationParams (
            endpoint=endpoint,
            format="normalized",
            # attributes=["temperature"],
            sysAttrs=True
            #showChanges=True
        )

        subs_request = CreateSubscriptionRequest (
            id="urn:ngsi-ld:Subscription:{0}".format(entity),
            type="Subscription",
            entities=[{ "type": entity }],
            description="On-change subscription to TemperatureSensor entities for changes within temperature property.",
            watchedAttributes=["temperature"],
            notification=notification_params
        )
        """
        api_instance = ngsi_ld_client.ContextInformationSubscriptionApi(ngsi_ld)
        api_instance.create_subscription(create_subscription_request=subs_request)

@app.post("/notify",
          status_code=status.HTTP_200_OK)
async def receiveNotification(request: Request):
    global CURRENT_ITERATION
    notification = await request.json()
    for entity in notification["data"]:
        if entity["type"] == "InterfaceStatistics":
            CURRENT_ITERATION += 1
            logger.info("Entity notification: %s\n" % entity)
            if "observedAt" in entity["inOctets"] and "modifiedAt" in entity:
                #current_time = datetime.utcnow().replace(tzinfo=timezone.utc).isoformat()
                #logger.info(f"Current time: {parser.parse(current_time)}") 
                #current_datetime = datetime.fromisoformat(current_time)   
                #logger.info(f"Current time: {current_datetime}") 

                observedAt = parser.parse(entity["observedAt"])
                logger.info(f"observedAt time: {observedAt}") 
                modifiedAt = parser.parse(entity["modifiedAt"])
                logger.info(f"modifiedAt time: {modifiedAt}") 

                delta_time = (modifiedAt - observedAt).total_seconds()
                print(f"Delta time: {delta_time}")
                evaluation_delta_times.append(delta_time)
                
                logger.info(f"ITERATION #{CURRENT_ITERATION} DELTA TIME: {delta_time} s | {delta_time*1e3} ms | {delta_time*1e6} µs\n")
                calculate_delta(evaluation_delta_times, CURRENT_ITERATION)
