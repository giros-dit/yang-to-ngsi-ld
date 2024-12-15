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
from query_tester_materialization_context_broker.check_client import NGSILDHealthInfoClient
#from datetime import datetime,timezone
from dateutil import parser
import gzip

from ngsi_ld_client.models.entity import Entity
from ngsi_ld_client.models.model_property import ModelProperty
from ngsi_ld_client.models.query_entity200_response_inner import QueryEntity200ResponseInner

from ngsi_ld_models_netconf_client_data_materialization.models.netconf import NETCONF
from ngsi_ld_models_netconf_client_data_materialization.models.operation import Operation
from ngsi_ld_models_netconf_client_data_materialization.models.subscription_mode import SubscriptionMode
from ngsi_ld_models_netconf_client_data_materialization.models.period import Period

query_delta_times = []
query_responses_delta_times = []

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

performance_measurements_file = open("/opt/query-tester-materialization-context-broker/query_tester_materialization_context_broker/performance_measurements.csv", "w", newline='')
csv_writer = csv.writer(performance_measurements_file)
csv_header = ["observed_at", "iteration_started_at", "iteration_finished_at", "processing_time_since_observed_at", "mean_processing_time_since_observed_at", "min_processing_time_since_observed_at",
              "max_processing_time_since_observed_at", "query_execution_time", "mean_execution_time", "min_execution_time", "max_execution_time", "notifications_received"]
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
    
    sleep(2)

    api_instance_provision = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

    operation = Operation(
        value="GET",
        xpath={"type":"Property", "value": "/interfaces-state/interface[name='GigabitEthernet2']"},
        getOption={"type":"Property", "value":"state"}
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
        operation=operation
    )

    entity_input = netconf_client_instance.to_dict()
    query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)
    api_instance_consumption = ngsi_ld_client.ContextInformationConsumptionApi(ngsi_ld)

    while True:
        try:
            start_datetime = datetime.datetime.now(datetime.timezone.utc)
            # Create NGSI-LD entity of type NETCONF: POST /entities
            api_instance_provision.create_entity(query_entity200_response_inner=query_entity_input)
        except Exception as e:
            logger.exception("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)
        
        while True:

            try:
                # Retrieve NGSI-LD Entity by id: GET /entities/{entityId}
                api_response = api_instance_consumption.retrieve_entity(entity_id='urn:ngsi-ld:Interface:clab-telemetry-ixiac-lab-r1:GigabitEthernet2')
                
                # Query NGSI-LD entities of type Interface: GET /entities
                # api_response = api_instance_consumption.query_entity(type='Interface')
                '''
                interface_entities = api_response
                for interface_entity in interface_entities:
                    logger.info(interface_entity.to_dict())
                '''
                break
                
            except Exception as e:
                if "404" in str(e):
                    logger.warning("Entity not found (404). Retrying...")
                else:
                    logger.exception("Unexpected exception when calling ContextInformationConsumptionApi->retrieve_entity: %s\n" % e)
                    raise

        logger.info(api_response.to_dict())
        stop_datetime = datetime.datetime.now(datetime.timezone.utc)
        query_delta_time = (stop_datetime - start_datetime).total_seconds()
        query_delta_times.append(query_delta_time)
        observedAt = parser.parse(api_response.to_dict()["name"]["observedAt"])
        query_datetime = stop_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        query_response_delta_time = (stop_datetime - observedAt).total_seconds()
        query_responses_delta_times.append(query_response_delta_time)

        logger.info("--- PERFORMANCE MEASUREMENTS ---")
        logger.info("QUERIES PROCESSED SO FAR: " + str(len(query_delta_times)) + "\n")
        logger.info("ITERATION STARTED AT: " + start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
        logger.info("ITERATION FINISHED AT: " + query_datetime + "\n")
        logger.info(f"QUERY EXECUTION TIME: {query_delta_time * 1e3} ms\n")
        mean_execution_time = sum(query_delta_times)/len(query_delta_times)
        min_execution_time = min(query_delta_times)
        max_execution_time = max(query_delta_times)
        logger.info(f"MEAN QUERY EXECUTION TIME: {mean_execution_time * 1e3} ms\n")
        logger.info(f"MIN QUERY EXECUTION TIME: {min_execution_time * 1e3} ms\n")
        logger.info(f"MAX QUERY EXECUTION TIME VALUE: {max_execution_time * 1e3} ms\n")
        if observedAt != None:
            logger.info("NOTIFICATION EVENT TIME/OBSERVED AT: " + observedAt.strftime("%Y-%m-%dT%H:%M:%S.%fZ") + "\n")
            logger.info(f"TOTAL PROCESSING TIME SO FAR SINCE QUERY REPLY EVENT TIME/OBSERVED AT: {query_response_delta_time * 1e3} ms\n")
            mean_query_reply_time = sum(query_responses_delta_times)/len(query_responses_delta_times)
            min_query_reply_time = min(query_responses_delta_times)
            max_query_reply_time = max(query_responses_delta_times)
            logger.info(f"MEAN QUERY REPLY EXECUTION TIME: {mean_query_reply_time * 1e3} ms\n")
            logger.info(f"MIN QUERY REPLY EXECUTION TIME: {min_query_reply_time * 1e3} ms\n")
            logger.info(f"MAX QUERY REPLY EXECUTION TIME VALUE: {max_query_reply_time * 1e3} ms\n")
        logger.info("--- PERFORMANCE MEASUREMENTS ---")

        csv_data = [observedAt.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), query_datetime, 
                    str(query_response_delta_time * 1e3) + " ms", str((sum(query_responses_delta_times)/len(query_responses_delta_times)) * 1e3) + " ms",
                    str(min(query_responses_delta_times) * 1e3) + " ms", str(max(query_responses_delta_times) * 1e3) + " ms",
                    str(query_delta_time * 1e3) + " ms", str((sum(query_delta_times)/len(query_delta_times)) * 1e3) + " ms",
                    str(min(query_delta_times) * 1e3) + " ms", str(max(query_delta_times) * 1e3) + " ms", str(len(query_delta_times))]
        csv_writer.writerow(csv_data)
        performance_measurements_file.flush()
        try:
            # Delete NGSI-LD Entity by id: DELETE /entities/{entityId}
            api_instance_provision.delete_entity(entity_id='urn:ngsi-ld:Interface:clab-telemetry-ixiac-lab-r1:GigabitEthernet2')
        except Exception as e:
            logger.exception("Exception when calling ContextInformationProvisionApi->delete_entity: %s\n" % e)
        sleep(5)