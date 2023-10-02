import logging
import logging.config
import yaml
import os
import json
import pdb

import ngsi_ld_client
from ngsi_ld_models.models.interface import Interface
from ngsi_ld_models.models.statistics import Statistics
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

entities_input = []

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
    speed={"type": "Property", "value": 1000000000},
    higherLayerIf={"type": "Relationship", "object": "urn:ngsi-ld:Interface:GigabitEthernet0.3.7.123"}
)

interface_statistics = Statistics(
    id="urn:ngsi-ld:Statistics:GigabitEthernet0.3.7",
    type="Statistics",
    isPartOf={"type": "Relationship", "object": "urn:ngsi-ld:Interface:GigabitEthernet0.3.7"},
    discontinuityTime={"type": "Property", "value": "2022-07-13T17:22:06Z"},
    inOctets={"type": "Property", "value": 30547004},
    inUnicastPkts={"type": "Property", "value": 40919},
    inBroadcastPkts={"type": "Property", "value": 35163},
    inMulticastPkts={"type": "Property", "value": 891},
    inDiscards={"type": "Property", "value": 0},
    inErrors={"type": "Property", "value": 0},
    inUnknownProtos={"type": "Property", "value": 0},
    outOctets={"type": "Property", "value": 28448416},
    outUnicastPkts={"type": "Property", "value": 40983},
    outBroadcastPkts={"type": "Property", "value": 8819},
    outMulticastPkts={"type": "Property", "value": 896},
    outDiscards={"type": "Property", "value": 0},
    outErrors={"type": "Property", "value": 0}
)

subinterface = Interface(
    id="urn:ngsi-ld:Interface:GigabitEthernet0.3.7.123",
    type="Interface",
    name={"type":"Property", "value": "GigabitEthernet0.3.7.123"},
    description={"type": "Property", "value": "GigabitEthernet0.3.7.123 interface"},
    enabled={"type": "Property", "value": True},
    linkUpDownTrapEnable={"type": "Property", "value": "enabled"},
    adminStatus={"type": "Property", "value": "up"},
    operStatus={"type": "Property", "value": "down"},
    lastChange={"type": "Property", "value": "2022-10-20T16:47:16Z"},
    ifIndex={"type": "Property", "value": 61},
    physAddress={"type": "Property", "value": "3C:15:FB:E7:04:77"},
    speed={"type": "Property", "value": 1000000000},
    lowerLayerIf={"type": "Relationship", "object": "urn:ngsi-ld:Interface:GigabitEthernet0.3.7"}
)

subinterface_statistics = Statistics(
    id="urn:ngsi-ld:Statistics:GigabitEthernet0.3.7.123",
    type="Statistics",
    isPartOf={"type": "Relationship", "object": "urn:ngsi-ld:Interface:GigabitEthernet0.3.7.123"},
    discontinuityTime={"type": "Property", "value": "2022-07-13T17:22:06Z"},
    inOctets={"type": "Property", "value": 0},
    inUnicastPkts={"type": "Property", "value": 0},
    inBroadcastPkts={"type": "Property", "value": 0},
    inMulticastPkts={"type": "Property", "value": 0},
    inDiscards={"type": "Property", "value": 0},
    inErrors={"type": "Property", "value": 0},
    inUnknownProtos={"type": "Property", "value": 0},
    outOctets={"type": "Property", "value": 0},
    outUnicastPkts={"type": "Property", "value": 0},
    outBroadcastPkts={"type": "Property", "value": 0},
    outMulticastPkts={"type": "Property", "value": 0},
    outDiscards={"type": "Property", "value": 0},
    outErrors={"type": "Property", "value": 0}
)

api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

interface_entity_input = interface.to_dict()

logger.info("Interface object representation: %s\n" % interface_entity_input)

logger.info("Entity object representation for Interface object: %s\n" % Entity.from_dict(interface_entity_input))

entities_input.append(QueryEntity200ResponseInner.from_dict(interface_entity_input))

interface_statistics_entity_input = interface_statistics.to_dict()

logger.info("Statistics object representation: %s\n" % interface_statistics_entity_input)

logger.info("Entity object representation for Statistics object: %s\n" % Entity.from_dict(interface_statistics_entity_input))

entities_input.append(QueryEntity200ResponseInner.from_dict(interface_statistics_entity_input))

subinterface_entity_input = subinterface.to_dict()

logger.info("Interface object representation: %s\n" % subinterface_entity_input)

logger.info("Entity object representation for Interface object: %s\n" % Entity.from_dict(subinterface_entity_input))

entities_input.append(QueryEntity200ResponseInner.from_dict(subinterface_entity_input))

subinterface_statistics_entity_input = subinterface_statistics.to_dict()

logger.info("Statistics object representation: %s\n" % subinterface_statistics_entity_input)

logger.info("Entity object representation for Statistics object: %s\n" % Entity.from_dict(subinterface_statistics_entity_input))

entities_input.append(QueryEntity200ResponseInner.from_dict(subinterface_statistics_entity_input))

try:
    # Create NGSI-LD entities of type Interface and Sensor: POST /entityOperations/upsert
    api_instance.upsert_batch(query_entity200_response_inner=entities_input)
except Exception as e:
    logger.exception("Exception when calling ContextInformationProvisionApi->upsert_batch: %s\n" % e)

