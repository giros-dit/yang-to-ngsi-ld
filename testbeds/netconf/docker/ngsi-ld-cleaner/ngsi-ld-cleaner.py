import os
import sys
import logging
import logging.config
import pdb
import yaml
import json
import time
import datetime

import xml.etree.ElementTree as et

from dateutil import parser

import ngsi_ld_client

from ngsi_ld_client.api_client import ApiClient as NGSILDClient
from ngsi_ld_client.configuration import Configuration as NGSILDConfiguration
from ngsi_ld_client.exceptions import ApiException

## -- BEGIN LOGGING CONFIGURATION -- ##

with open('logging.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)

## -- END LOGGING CONFIGURATION -- ##

## -- BEGIN CONSTANTS DECLARATION -- ##

# NGSI-LD Context Broker:
BROKER_URI = os.getenv("BROKER_URI", "http://localhost:9090/ngsi-ld/v1")
#BROKER_URI = os.getenv("BROKER_URI", "http://orion:1026/ngsi-ld/v1")
#BROKER_URI = os.getenv("BROKER_URI", "http://stellio-api-gateway:8080/ngsi-ld/v1")

# Context Catalog:
CONTEXT_CATALOG_URI = os.getenv("CONTEXT_CATALOG_URI", "http://context-catalog:8080/context.jsonld")

# Init NGSI-LD Client
configuration = NGSILDConfiguration(host=BROKER_URI)
configuration.debug = True
ngsi_ld = NGSILDClient(configuration=configuration)

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

api_instance_ngsi_ld_consumption = ngsi_ld_client.ContextInformationConsumptionApi(ngsi_ld)

api_instance_ngsi_ld_provision = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

api_instance_ngsi_ld_provision_temporal = ngsi_ld_client.TemporalContextInformationProvisionApi(ngsi_ld)

while True:
    entity_types = []
    entity_ids = []
    time.sleep(1)

    try:
        # Retrieve Available Entity Types.
        entity_types_response = api_instance_ngsi_ld_consumption.retrieve_entity_types()
        for entity_type_response in entity_types_response.to_dict()["typeList"]:
            if entity_type_response != "NETCONF" and entity_type_response != "YANGIdentity":
                entity_types.append(entity_type_response)

    except Exception as e:
        logger.exception("Exception when calling ContextInformationConsumptionApi->retrieve_entity_types: %s\n" % e)

    try:
        # Query NGSI-LD entities:
        if entity_types != []:
            for entity_type in entity_types:
                entities = api_instance_ngsi_ld_consumption.query_entity(type=str(entity_type), limit=300)
                for entity in entities:
                    logger.info(entity.to_dict())
                    entity_ids.append(entity.to_dict()["id"])

    except Exception as e:
        logger.exception("Exception when calling ContextInformationConsumptionApi->query_entity: %s\n" % e)

    try:
        if entity_ids != []:
            # Delete NGSI-LD Entity by id: DELETE /entities/{entityId}
            for entity_id in entity_ids:
                api_instance_ngsi_ld_provision.delete_entity(entity_id=str(entity_id))
    except Exception as e:
        logger.exception("Exception when calling ContextInformationProvisionApi->delete_entity: %s\n" % e)

    try:
        if entity_ids != []:
            # Temporal Representation of Entity deletion by id: DELETE /temporal/entities/{entityId}
            for entity_id in entity_ids:
                api_instance_ngsi_ld_provision_temporal.delete_temporal(entity_id=str(entity_id))
    except Exception as e:
        logger.exception("Exception when calling TemporalContextInformationProvisionApi->delete_temporal: %s\n" % e)

    time.sleep(int(sys.argv[1]))