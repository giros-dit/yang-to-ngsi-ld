import logging
import logging.config
import yaml
import os
import json
import pdb

import ngsi_ld_client

from ngsi_ld_models.models.interface import Interface
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

interface = Interface(
    id="urn:ngsi-ld:Interface:GigabitEthernet0.3.7",
    type="Interface",
    name={"type":"Property", "value": "GigabitEthernet0.3.7"},
    description={"type": "Property", "value": "GigabitEthernet0.3.7 interface"},
    enabled={"type": "Property", "value": True},
    linkUpDownTrapEnable={"type": "Property", "value": "enabled"},
    adminStatus={"type": "Property", "value": "up"},
    operStatus={"type": "Property", "value": "down"},
    lastChange={"type": "Property", "value": "2022-10-20T16:47:16Z"},
    ifIndex={"type": "Property", "value": 18},
    physAddress={"type": "Property", "value": "3C:15:FB:E7:04:77"},
    speed={"type": "Property", "value": 1000000000}
)

api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

entity_input = interface.to_dict()

logger.info("Interface object representation: %s\n" % entity_input)

logger.info("Entity object representation: %s\n" % Entity.from_dict(entity_input))

logger.info("QueryEntity200ResponseInner object representation: %s\n" % QueryEntity200ResponseInner.from_dict(entity_input))

query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)

try:
    # Create NGSI-LD entity of type Sensor: POST /entities
    api_instance.create_entity(query_entity200_response_inner=query_entity_input)
except Exception as e:
    logger.exception("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)

