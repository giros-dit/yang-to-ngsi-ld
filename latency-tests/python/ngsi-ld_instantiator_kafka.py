import os
import logging
import logging.config
import pdb
import yaml
import json

from confluent_kafka import Consumer

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

def create_ngsi_ld_entity(entity):
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

    api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

    entity_input = entity.to_dict()

    logger.info("Entity object representation: %s\n" % Entity.from_dict(entity_input))
    logger.info("QueryEntity200ResponseInner object representation: %s\n" % QueryEntity200ResponseInner.from_dict(entity_input))

    query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)

    try:
        # Create NGSI-LD entity of type Sensor: POST /entities
        api_instance.create_entity(query_entity200_response_inner=query_entity_input)
    except Exception as e:
        logger.exception("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)

'''
Consume from the 'dictionary-buffers' Kafka topic, identify NGSI-LD Entities, create their instances
and upsert them to the Orion-LD broker.
'''

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['dictionary-buffers'])

while True:
    message = consumer.poll()

    if message is None:
        continue
    if message.error():
        print("Consumer error: {}".format(message.error()))
        continue

    dict_buffers = json.loads(message.value().decode('utf-8'))

    for dict_buffer in dict_buffers:
        type = dict_buffer['type']
        if type == 'Interface':
            interface = Interface.from_dict(dict_buffer)
            create_ngsi_ld_entity(interface)
        if type == 'InterfaceStatistics':
            interface_statistics = InterfaceStatistics.from_dict(dict_buffer)
            create_ngsi_ld_entity(interface_statistics)
        if type == 'InterfaceIpv4':
            interface_ipv4 = InterfaceIpv4.from_dict(dict_buffer)
            create_ngsi_ld_entity(interface_ipv4)
        if type == 'InterfaceIpv4Address':
            interface_ipv4_address = InterfaceIpv4Address.from_dict(dict_buffer)
            create_ngsi_ld_entity(interface_ipv4_address)
        if type == 'InterfaceIpv4Neighbor':
            interface_ipv4_neighbor = InterfaceIpv4Neighbor.from_dict(dict_buffer)
            create_ngsi_ld_entity(interface_ipv4_neighbor)
        if type == 'InterfaceIpv6':
            interface_ipv6 = InterfaceIpv6.from_dict(dict_buffer)
            create_ngsi_ld_entity(interface_ipv6)
        if type == 'InterfaceIpv6Address':
            interface_ipv6_address = InterfaceIpv6Address.from_dict(dict_buffer)
            create_ngsi_ld_entity(interface_ipv6_address)
        if type == 'InterfaceIpv6Autoconf':
            interface_ipv6_autoconf = InterfaceIpv6Autoconf.from_dict(dict_buffer)
            create_ngsi_ld_entity(interface_ipv6_autoconf)
        if type == 'InterfaceIpv6Neighbor':
            interface_ipv6_neighbor = InterfaceIpv6Neighbor.from_dict(dict_buffer)
            create_ngsi_ld_entity(interface_ipv6_neighbor)
