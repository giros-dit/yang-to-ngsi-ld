import sys
import os
import logging
import logging.config
import pdb
import yaml

import ngsi_ld_client

from ngsi_ld_models.models.interface import Interface
from ngsi_ld_models.models.statistics import Statistics
from ngsi_ld_models.models.ipv4 import Ipv4
from ngsi_ld_models.models.ipv4_address import Ipv4Address
from ngsi_ld_models.models.ipv4_neighbor import Ipv4Neighbor
from ngsi_ld_models.models.ipv6 import Ipv6
from ngsi_ld_models.models.ipv6_address import Ipv6Address
from ngsi_ld_models.models.ipv6_autoconf import Ipv6Autoconf
from ngsi_ld_models.models.ipv6_neighbor import Ipv6Neighbor
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
BROKER_URI = os.getenv("BROKER_URI", "http://localhost:1026/ngsi-ld/v1")

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
Read from the 'dictionary-buffers' file, identify NGSI-LD Entities, create their instances
and upsert them to the Orion-LD broker.
'''

dict_buffers_file = sys.argv[1]
input_file = open(dict_buffers_file, 'r')
dict_buffers = eval(input_file.read())
input_file.close()

for dict_buffer in dict_buffers:
    type = dict_buffer['type']
    if type == 'Interface':
        interface = Interface.from_dict(dict_buffer)
        create_ngsi_ld_entity(interface)
    if type == 'Statistics':
        statistics = Statistics.from_dict(dict_buffer)
        create_ngsi_ld_entity(statistics)
    if type == 'Ipv4':
        ipv4 = Ipv4.from_dict(dict_buffer)
        create_ngsi_ld_entity(ipv4)
    if type == 'Ipv4Address':
        ipv4Address = Ipv4Address.from_dict(dict_buffer)
        create_ngsi_ld_entity(ipv4Address)
    if type == 'Ipv4Neighbor':
        ipv4Neighbor = Ipv4Neighbor.from_dict(dict_buffer)
        create_ngsi_ld_entity(ipv4Neighbor)
    if type == 'Ipv6':
        ipv6 = Ipv6.from_dict(dict_buffer)
        create_ngsi_ld_entity(ipv6)
    if type == 'Ipv6Address':
        ipv6Address = Ipv6Address.from_dict(dict_buffer)
        create_ngsi_ld_entity(ipv6Address)
    if type == 'Ipv6Autoconf':
        ipv6Autoconf = Ipv6Autoconf.from_dict(dict_buffer)
        create_ngsi_ld_entity(ipv6Autoconf)
    if type == 'Ipv6Neighbor':
        ipv6Neighbor = Ipv6Neighbor.from_dict(dict_buffer)
        create_ngsi_ld_entity(ipv6Neighbor)
