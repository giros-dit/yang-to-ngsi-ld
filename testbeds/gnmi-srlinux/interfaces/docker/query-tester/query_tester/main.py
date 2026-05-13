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
    title="query Tester API",
    version="1.0.0")

@app.on_event("startup")
async def startup_event():
    
    # Check if Scorpio API is up
    ngsi_ld_health_info_api.check_scorpio_status()

    # Check Scorpio build info
    ngsi_ld_health_info_api.check_scorpio_info()

    api_instance_consumption = ngsi_ld_client.ContextInformationConsumptionApi(ngsi_ld)
    
    last_modified_at = None

    while True:
        entity = None
        try:
            # Retrieve NGSI-LD Entity by id: GET /entities/{entityId}
            api_response = api_instance_consumption.retrieve_entity.__wrapped__(api_instance_consumption,
                                                                              entity_id='urn:ngsi-ld:Interface:srlinux-testbed:r1:ethernet-1/1',
                                                                              options=['sysAttrs']) # pasar directamente la representación primitiva
            #api_response = api_instance_consumption.retrieve_entity(entity_id='urn:ngsi-ld:Interface:srlinux-testbed:r1:ethernet-1/1')
            
            # Query NGSI-LD entities of type Interface: GET /entities
            #api_response = api_instance_consumption.query_entity(type='Interface')
            
            if api_response:
                '''
                interface_entities = api_response
                for interface_entity in interface_entities:
                    logger.info(interface_entity.to_dict())
                    entity = interface_entity.to_dict()
                '''
                entity = api_response.to_dict()
                logger.info("Entity query response: %s\n" %entity)

                if "observedAt" in entity["name"] and "modifiedAt" in entity["name"]:
                    if last_modified_at is not None and last_modified_at == entity["name"]["modifiedAt"]:
                        logger.info("No new entity values. Retrying in 10 seconds...")
                        sleep(5)
                    else:
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
                        last_modified_at = entity["name"]["modifiedAt"]
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