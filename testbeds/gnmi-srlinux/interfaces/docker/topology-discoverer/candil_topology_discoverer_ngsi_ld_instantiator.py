import os
import logging
import logging.config
import pdb
import json
import yaml
import time
import datetime
import csv

from kafka import KafkaConsumer

from dateutil import parser

from candil_network_topology_json_parser import parse_topology

import ngsi_ld_client

from ngsi_ld_models.models.yang_identity import YANGIdentity
from ngsi_ld_models.models.network import Network
from ngsi_ld_models.models.network_link import NetworkLink
from ngsi_ld_models.models.network_link_source import NetworkLinkSource
from ngsi_ld_models.models.network_link_destination import NetworkLinkDestination
from ngsi_ld_models.models.network_node import NetworkNode
from ngsi_ld_models.models.network_node_termination_point import NetworkNodeTerminationPoint


from ngsi_ld_client.models.entity import Entity
from ngsi_ld_client.models.query_entity200_response_inner import QueryEntity200ResponseInner

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
BROKER_URI = os.getenv("BROKER_URI", "http://scorpio:9090/ngsi-ld/v1")

# Context Catalog:
CONTEXT_CATALOG_URI = os.getenv("CONTEXT_CATALOG_URI", "http://context-catalog:8080/context.jsonld")

## -- END CONSTANTS DECLARATION -- ##

## -- BEGIN AUXILIARY FUNCTIONS -- ##

def init_ngsi_ld_client():
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

    return ngsi_ld

def create_ngsi_ld_entity(ngsi_ld, entity) -> bool:
    result = False
    
    api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

    entity_input = entity.to_dict()

    logger.info("Entity object representation: %s\n" % Entity.from_dict(entity_input))
    logger.info("QueryEntity200ResponseInner object representation: %s\n" % QueryEntity200ResponseInner.from_dict(entity_input))

    query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)

    try:
        # Create NGSI-LD entity of type Sensor: POST /entities
        api_response = api_instance.create_entity(query_entity200_response_inner=query_entity_input)
        #logger.info(api_response.to_dict())
        result = True
    except Exception as e:
        logger.exception("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)
        result = False

    return result

def retrieve_ngsi_ld_entity(ngsi_ld, entity_id: str) -> bool:
    result = False

    api_instance = ngsi_ld_client.ContextInformationConsumptionApi(ngsi_ld)

    try:
        # Retrieve NGSI-LD Entity by id: GET /entities/{entityId}
        api_response = api_instance.retrieve_entity(entity_id)
        #logger.info(api_response.to_dict())
        result = True
    except Exception as e:
        logger.exception("Exception when calling ContextInformationConsumptionApi->retrieve_entity: %s\n" % e)
        result = False
    
    return result

def update_ngsi_ld_entity(ngsi_ld, entity_id: str, entity) -> bool:
    result = False

    api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

    entity_input = entity.to_dict()

    #logger.info("Entity object representation: %s\n" % Entity.from_dict(entity_input))

    try:
        # Update NGSI-LD Entity by id: PATCH /entities/{entityId}/attrs
        api_response = api_instance.update_entity(entity_id, entity=Entity.from_dict(entity_input))
        #logger.info(api_response.to_dict())
        result = True
    except Exception as e:
        logger.exception("Exception when calling ContextInformationProvisionApi->update_entity: %s\n" % e)
        result = False

    return result

def get_entity_class_object_by_type(dict_buffer: dict):
    type = dict_buffer['type']
    if type == 'Network':
        entity = Network.from_dict(dict_buffer)
    elif type == 'NetworkLink':
        entity = NetworkLink.from_dict(dict_buffer)
    elif type == 'NetworkLinkSource':
        entity = NetworkLinkSource.from_dict(dict_buffer)
    elif type == 'NetworkLinkDestination':
        entity = NetworkLinkDestination.from_dict(dict_buffer)
    elif type == 'NetworkNode':
        entity = NetworkNode.from_dict(dict_buffer)
    elif type == 'NetworkNodeTerminationPoint':
        entity = NetworkNodeTerminationPoint.from_dict(dict_buffer)
    else:
        entity = None
    return entity

## -- END AUXILIARY FUNCTIONS -- ##

exec_times = []

print("Hello, I am the JSON parser for network topologies and the NGSI-LD instantiator")

print("I will consume messages from a JSON file named topology-data-compliant-yang.json")
print("I will process every single notification, parse them and create/update NGSI-LD entities accordingly")
print("These entities will be uploaded to the NGSI-LD broker")

print("Initializing the NGSI-LD client...")

ngsi_ld = init_ngsi_ld_client()

print("Done!")

with open("topology-data-compliant-yang.json", 'r') as file:
    topology_data = json.load(file)

dict_buffers = parse_topology(topology_data)

for dict_buffer in dict_buffers:
    entity_id = dict_buffer['id']
    
    entity = get_entity_class_object_by_type(dict_buffer)

    if entity != None:

        print("Dictionary buffer contains information for entity " + entity_id)

        exists = retrieve_ngsi_ld_entity(ngsi_ld, entity_id)
        if exists == False:
            print("Entity " + entity_id + " DOES NOT EXIST. Trying to create it...")
            created = create_ngsi_ld_entity(ngsi_ld, entity)
            if created == False:
                print("Entity " + entity_id + " COULD NOT BE CREATED")
            else:
                print("Entity " + entity_id + " WAS SUCCESSFULLY CREATED")
        else:
            print("Entity " + entity_id + " DOES EXIST. Trying to update it...")
            updated = update_ngsi_ld_entity(ngsi_ld, entity_id, entity)
            if updated == False:
                print("Entity " + entity_id + " COULD NOT BE UPDATED")
            else:
                print("Entity " + entity_id + " WAS SUCCESSFULLY UPDATED")