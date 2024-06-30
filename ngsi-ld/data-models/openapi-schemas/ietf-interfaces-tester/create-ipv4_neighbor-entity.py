import logging
import logging.config
import yaml
import os
import json
import pdb

import ngsi_ld_client

from ngsi_ld_models.models.interface_ipv4_neighbor import InterfaceIpv4Neighbor
from ngsi_ld_client.models.entity import Entity
from ngsi_ld_client.models.query_entity200_response_inner import QueryEntity200ResponseInner

from ngsi_ld_client.api_client import ApiClient as NGSILDClient
from ngsi_ld_client.configuration import Configuration as NGSILDConfiguration
from ngsi_ld_client.exceptions import ApiException

#assuming the log config file name is logging.yaml
with open('logging.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)

#read the file to logging config
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)

# NGSI-LD Context Broker
BROKER_URI = os.getenv("BROKER_URI", "http://localhost:1026/ngsi-ld/v1")
# Context Catalog
CONTEXT_CATALOG_URI = os.getenv("CONTEXT_CATALOG_URI",
                                "http://context-catalog:8080/context.jsonld")

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

ipv4_neighbor = InterfaceIpv4Neighbor(
    id="urn:ngsi-ld:InterfaceIpv4Neighbor:GigabitEthernet0.3.7:11.40.1.12",
    type="InterfaceIpv4Neighbor",
    isPartOf={"type": "Relationship", "object": "urn:ngsi-ld:InterfaceIpv4:GigabitEthernet0.3.7"},
    ip={"type": "Property", "value": "11.40.1.12"},
    linkLayerAddress={"type": "Property", "value": "3C:15:FB:E7:04:78"},
    origin={"type": "Property", "value": "other"}
)

api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

entity_input = ipv4_neighbor.to_dict()

logger.info("InterfaceIpv4Neighbor object representation: %s\n" % entity_input)

logger.info("Entity object representation: %s\n" % Entity.from_dict(entity_input))

logger.info("QueryEntity200ResponseInner object representation: %s\n" % QueryEntity200ResponseInner.from_dict(entity_input))

query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)

try:
    # Create NGSI-LD entity of type Sensor: POST /entities
    api_instance.create_entity(query_entity200_response_inner=query_entity_input.from_dict(entity_input))
except Exception as e:
    logger.exception("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)

