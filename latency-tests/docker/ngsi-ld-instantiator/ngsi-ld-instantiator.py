import os
import logging
import logging.config
import pdb
import yaml
import json

from kafka import KafkaConsumer

from dateutil import parser

import ngsi_ld_client

from ngsi_ld_models.models.interface import Interface
from ngsi_ld_models.models.interface_statistics import InterfaceStatistics
from ngsi_ld_models.models.interface_ipv4 import InterfaceIpv4
from ngsi_ld_models.models.interface_ipv4_address import InterfaceIpv4Address
from ngsi_ld_models.models.interface_ipv4_neighbor import InterfaceIpv4Neighbor
from ngsi_ld_models.models.interface_ipv6 import InterfaceIpv6
from ngsi_ld_models.models.interface_ipv6_address import InterfaceIpv6Address
from ngsi_ld_models.models.interface_ipv6_autoconf import InterfaceIpv6Autoconf
from ngsi_ld_models.models.interface_ipv6_neighbor import InterfaceIpv6Neighbor
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
    if type == 'Interface':
        entity = Interface.from_dict(dict_buffer)
    if type == 'InterfaceStatistics':
        entity = InterfaceStatistics.from_dict(dict_buffer)
    if type == 'InterfaceIpv4':
        entity = InterfaceIpv4.from_dict(dict_buffer)
    if type == 'InterfaceIpv4Address':
        entity = InterfaceIpv4Address.from_dict(dict_buffer)
    if type == 'InterfaceIpv4Neighbor':
        entity = InterfaceIpv4Neighbor.from_dict(dict_buffer)
    if type == 'InterfaceIpv6':
        entity = InterfaceIpv6.from_dict(dict_buffer)
    if type == 'InterfaceIpv6Address':
        entity = InterfaceIpv6Address.from_dict(dict_buffer)
    if type == 'InterfaceIpv6Autoconf':
        entity = InterfaceIpv6Autoconf.from_dict(dict_buffer)
    if type == 'InterfaceIpv6Neighbor':
        entity = InterfaceIpv6Neighbor.from_dict(dict_buffer)
    return entity

## -- END AUXILIARY FUNCTIONS -- ##

print("Hello, I am the NGSI-LD instantiator")

print("I will consume messages (dictionary buffers/NGSI-LD data structures) from a Kafka topic named dictionary-buffers")

consumer = KafkaConsumer('dictionary-buffers', bootstrap_servers=['kafka:9092'])

print("I will process every single dictionary buffer and create/update NGSI-LD entities")
print("These entities will be uploaded to the NGSI-LD broker")

print("Initializing the NGSI-LD client...")

ngsi_ld = init_ngsi_ld_client()

print("Done!")

while True:
    for message in consumer:
        print("I have consumed a new set of dictionary buffers!")

        dict_buffers = json.loads(message.value.decode('utf-8'))

        for dict_buffer in dict_buffers:
            entity_id = dict_buffer['id']
            print('\n')
            print(dict_buffer)
            print('\n')
            entity = get_entity_class_object_by_type(dict_buffer)
            print('\n')
            print(entity)
            print('\n')
            print(entity.to_dict())
            print('\n')

            print("Dictionary buffers contain information for entity " + entity_id)

            exists = retrieve_ngsi_ld_entity(ngsi_ld, entity_id)
            if exists == False:
                print("Entity " + entity_id + " DOES NOT exist. Trying to create it...")
                created = create_ngsi_ld_entity(ngsi_ld, entity)
                if created == False:
                    print("Entity " + entity_id + " COULD NOT be created")
                else:
                    print("Entity " + entity_id + " was successfully created")
            else:
                print("Entity " + entity_id + " DOES exist. Trying to update it...")
                updated = update_ngsi_ld_entity(ngsi_ld, entity_id, entity)
                if updated == False:
                    print("Entity " + entity_id + " COULD NOT be updated")
                else:
                    print("Entity " + entity_id + " was successfully updated")
        
        print("Iteration done! Waiting for the next set of dictionary buffers...")
