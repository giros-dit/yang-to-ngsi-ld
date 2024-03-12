import logging
import os
from time import sleep
import time
from fastapi import FastAPI, Request, status
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
from notifier_tester.check_client import NGSILDHealthInfoClient
from datetime import datetime,timezone
from dateutil import parser

delta_times = []

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

performance_measurements_file = open("/opt/notifier-tester/notifier_tester/performance_measurements.csv", "w", newline='')
csv_writer = csv.writer(performance_measurements_file)
csv_header = ["observed_at", "modified_at", "evaluation_time", "mean_evaluation_time",
              "min_evaluation_time", "max_evaluation_time", "notifications_received"]
csv_writer.writerow(csv_header)  
    
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
        '''
        notification_params = NotificationParams (
            endpoint=endpoint,
            format="normalized",
            attributes=["inOctets"],
            sysAttrs=True
        )

        subs_request = CreateSubscriptionRequest (
            id="urn:ngsi-ld:Subscription:Periodic:{0}".format(entity),
            type="Subscription",
            entities=[
                {
                    "type": entity,
                    "id": "urn:ngsi-ld:InterfaceStatistics:clab-telemetry-ixiac-lab-r1_GigabitEthernet2"
                },
                {
                    "type": entity,
                    "id": "urn:ngsi-ld:InterfaceStatistics:clab-telemetry-ixiac-lab-r1_GigabitEthernet3"
                },
                {
                    "type": entity,
                    "id": "urn:ngsi-ld:InterfaceStatistics:clab-telemetry-ixiac-lab-r2_GigabitEthernet2"
                },
                {
                    "type": entity,
                    "id": "urn:ngsi-ld:InterfaceStatistics:clab-telemetry-ixiac-lab-r2_GigabitEthernet3"
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
            #showChanges=True
        )

        subs_request = CreateSubscriptionRequest (
            id="urn:ngsi-ld:Subscription:{0}".format(entity),
            type="Subscription",
            entities=[
                {
                    "type": entity,
                    "id": "urn:ngsi-ld:InterfaceStatistics:clab-telemetry-ixiac-lab-r1_GigabitEthernet2"
                },
                {
                    "type": entity,
                    "id": "urn:ngsi-ld:InterfaceStatistics:clab-telemetry-ixiac-lab-r1_GigabitEthernet3"
                },
                {
                    "type": entity,
                    "id": "urn:ngsi-ld:InterfaceStatistics:clab-telemetry-ixiac-lab-r2_GigabitEthernet2"
                },
                {
                    "type": entity,
                    "id": "urn:ngsi-ld:InterfaceStatistics:clab-telemetry-ixiac-lab-r2_GigabitEthernet3"
                }
            ],
            description="On-change subscription to InterfaceStatistics entities for changes within inOctets property.",
            watchedAttributes=["inOctets"],
            notification=notification_params
        )

        api_instance = ngsi_ld_client.ContextInformationSubscriptionApi(ngsi_ld)
        api_instance.create_subscription(create_subscription_request=subs_request)

@app.post("/notify",
          status_code=status.HTTP_200_OK)
async def receiveNotification(request: Request):
    notification = await request.json()
    for entity in notification["data"]:
        if entity["type"] == "InterfaceStatistics":
            logger.info("Entity notification: %s\n" % entity)
            if "observedAt" in entity["inOctets"] and "modifiedAt" in entity["inOctets"]:
                #current_time = datetime.utcnow().replace(tzinfo=timezone.utc).isoformat()
                #logger.info(f"Current time: {parser.parse(current_time)}") 
                #current_datetime = datetime.fromisoformat(current_time)   
                #logger.info(f"Current time: {current_datetime}") 

                observed_at = parser.parse(entity["inOctets"]["observedAt"])
                modified_at = parser.parse(entity["inOctets"]["modifiedAt"])

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
