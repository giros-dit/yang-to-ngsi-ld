import logging
import os
from time import sleep
import time
from fastapi import FastAPI, Request, status
import json
import csv
import datetime
import ngsi_ld_client
from ngsi_ld_client.models.query_entity200_response_inner import QueryEntity200ResponseInner
from ngsi_ld_client.api_client import ApiClient as NGSILDClient
from ngsi_ld_client.configuration import Configuration as NGSILDConfiguration
from query_tester.check_client import NGSILDHealthInfoClient
#from datetime import datetime,timezone
from dateutil import parser
from ngsi_ld_client.exceptions import NotFoundException

delta_times = []

logger = logging.getLogger(__name__)

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

performance_measurements_file = open("/opt/query-tester/query_tester/performance_measurements.csv", "w", newline='')
csv_writer = csv.writer(performance_measurements_file)
csv_header = ["observed_at", "modified_at", "evaluation_time", "mean_evaluation_time",
              "min_evaluation_time", "max_evaluation_time", "notifications_received"]
csv_writer.writerow(csv_header)  
    
# Init FastAPI server
app = FastAPI(
    title="Query Tester API",
    version="1.0.0")

@app.on_event("startup")
async def startup_event():
    # Check if Scorpio API is up
    ngsi_ld_health_info_api.check_scorpio_status()

    # Check Scorpio build info
    ngsi_ld_health_info_api.check_scorpio_info()

    api_instance_consumption = ngsi_ld_client.ContextInformationConsumptionApi(ngsi_ld)
    
    last_observed_at = None

    while True:
        entity = None
        try:
            # Retrieve NGSI-LD Entity by id: GET /entities/{entityId} (e.g., urn:ngsi-ld:NetworkInstanceStaticRoutesRoute:routing-testbed:r1:default:192.168.2.0/24)
            #api_response = api_instance_consumption.retrieve_entity.__wrapped__(api_instance_consumption, entity_id='urn:ngsi-ld:NetworkInstanceStaticRoutesRoute:routing-testbed:r1:default:192.168.2.0/24', options=['sysAttrs']) # pasar directamente la representación primitiva            
            
            # Query NGSI-LD entities of type NetworkInstanceStaticRoutesRoute: GET /entities
            #api_response = api_instance_consumption.query_entity(type='NetworkInstanceStaticRoutesRoute')
            api_response = api_instance_consumption.query_entity.__wrapped__(api_instance_consumption, type='NetworkInstanceStaticRoutesRoute', options=['sysAttrs']) # pasar directamente la representación primitiva            
            
            if api_response:
                #entity = api_response.to_dict()
                #logger.info("Entity query response: %s\n" %entity)
                entities = api_response
                logger.info("Entities query response: %s\n" %entities)
                for i, entity in enumerate(entities):
                    entity = entity.to_dict()
                    if "observedAt" in entity["prefix"] and "modifiedAt" in entity["prefix"]:
                        if last_observed_at is not None and last_observed_at == parser.parse(entity["prefix"]["observedAt"]):
                            if i == len(entities) - 1:
                                logger.info("No new entity values. Retrying in 10 seconds...")
                        else:
                            logger.info("Entity info: %s\n" %entity)
                            observed_at = parser.parse(entity["prefix"]["observedAt"])
                            modified_at = parser.parse(entity["prefix"]["modifiedAt"])

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

                            if i == len(entities) - 1:
                                last_observed_at = observed_at

            else:
                logger.info("No entity found. Retrying in 10 seconds...")
            
            sleep(10)
        except NotFoundException as e:
            logger.info("Entity not found (404). Retrying in 10 seconds: %s", e)
            sleep(10)
            continue
        except Exception as e:
            logger.exception("Unexpected exception when calling ContextInformationConsumptionApi->query_entity: %s\n" % e)
            raise