import logging
import logging.config
import yaml
import os
import json
import pdb

import ngsi_ld_client
from ngsi_ld_models.models.network import Network
from ngsi_ld_models.models.network_node import NetworkNode
from ngsi_ld_models.models.network_link import NetworkLink
from ngsi_ld_models.models.network_link_source import NetworkLinkSource
from ngsi_ld_models.models.network_link_destination import NetworkLinkDestination
from ngsi_ld_models.models.network_node_termination_point import NetworkNodeTerminationPoint
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

network = Network(
    id="urn:ngsi-ld:Network:telemetry-testbed-l3-topology",
    type="Network",
    networkId={"type":"Property", "value": "telemetry-testbed-l3-topology"}
)

node1 = NetworkNode(
    id="urn:ngsi-ld:NetworkNode:telemetry-testbed-l3-topology:pc11",
    type="NetworkNode",
    nodeId={"type":"Property", "value": "pc11"},
    isPartOf={"type": "Relationship", "object": "urn:ngsi-ld:Network:telemetry-testbed-l3-topology"}
)

termination_point1 = NetworkNodeTerminationPoint(
    id="urn:ngsi-ld:NetworkNodeTerminationPoint:pc11:eth1",
    type="NetworkNodeTerminationPoint",
    tpId={"type":"Property", "value": "eth1"},
    isPartOf={"type": "Relationship", "object": "urn:ngsi-ld:NetworkNode:telemetry-testbed-l3-topology:pc11"}
)

node2 = NetworkNode(
    id="urn:ngsi-ld:NetworkNode:telemetry-testbed-l3-topology:s1",
    type="Node",
    nodeId={"type":"Property", "value": "s1"},
    isPartOf={"type": "Relationship", "object": "urn:ngsi-ld:Network:telemetry-testbed-l3-topology"}
)

termination_point2 = NetworkNodeTerminationPoint(
    id="urn:ngsi-ld:NetworkNodeTerminationPoint:s1:eth1",
    type="NetworkNodeTerminationPoint",
    tpId={"type":"Property", "value": "eth1"},
    isPartOf={"type": "Relationship", "object": "urn:ngsi-ld:NetworkNode:telemetry-testbed-l3-topology:s1"}
)

link = NetworkLink(
    id="urn:ngsi-ld:NetworkLink:telemetry-testbed-l3-topology:pc11-eth1-s1-eth1",
    type="NetworkLink",
    linkId={"type":"Property", "value": "pc11-eth1-s1-eth1"},
    isPartOf={"type": "Relationship", "object": "urn:ngsi-ld:Network:telemetry-testbed-l3-topology"}    
)

source = NetworkLinkSource(
    id="urn:ngsi-ld:NetworkLinkSource:pc11-eth1-s1-eth1:",
    type="NetworkLinkSource",
    sourceNode={"type": "Relationship", "object": "urn:ngsi-ld:NetworkNode:telemetry-testbed-l3-topology:pc11"},
    sourceTp={"type": "Relationship", "object": "urn:ngsi-ld:NetworkNode:telemetry-testbed-l3-topology:pc11:eth1"},
    isPartOf={"type": "Relationship", "object": "urn:ngsi-ld:NetworkLink:telemetry-testbed-l3-topology:pc11-eth1-s1-eth1"}    
)

destination = NetworkLinkDestination(
    id="urn:ngsi-ld:NetworkLinkDestination:pc11-eth1-s1-eth1:",
    type="NetworkLinkDestination",
    destNode={"type": "Relationship", "object": "urn:ngsi-ld:NetworkNode:telemetry-testbed-l3-topology:s1"},
    destTp={"type": "Relationship", "object": "urn:ngsi-ld:NetworkNode:telemetry-testbed-l3-topology:s1:eth1"},
    isPartOf={"type": "Relationship", "object": "urn:ngsi-ld:NetworkLink:telemetry-testbed-l3-topology:pc11-eth1-s1-eth1"}    
)

api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)


network_entity_input = network.to_dict()

logger.info("Network object representation: %s\n" % network_entity_input)

logger.info("Entity object representation for Network object: %s\n" % Entity.from_dict(network_entity_input))

entities_input.append(QueryEntity200ResponseInner.from_dict(network_entity_input))


node1_entity_input = node1.to_dict()

logger.info("NetworkNode object representation: %s\n" % node1_entity_input)

logger.info("Entity object representation for NetowrNode object: %s\n" % Entity.from_dict(node1_entity_input))

entities_input.append(QueryEntity200ResponseInner.from_dict(node1_entity_input))


node2_entity_input = node2.to_dict()

logger.info("NetworkNode object representation: %s\n" % node2_entity_input)

logger.info("Entity object representation for NetworkNode object: %s\n" % Entity.from_dict(node2_entity_input))

entities_input.append(QueryEntity200ResponseInner.from_dict(node2_entity_input))


tp1_entity_input = termination_point1.to_dict()

logger.info("NetworkNodeTerminationPoint object representation: %s\n" % tp1_entity_input)

logger.info("Entity object representation for NetworkNodeTerminationPoint object: %s\n" % Entity.from_dict(tp1_entity_input))

entities_input.append(QueryEntity200ResponseInner.from_dict(tp1_entity_input))


tp2_entity_input = termination_point2.to_dict()

logger.info("NetworkNodeTerminationPoint object representation: %s\n" % tp2_entity_input)

logger.info("Entity object representation for NetworkNodeTerminationPoint object: %s\n" % Entity.from_dict(tp2_entity_input))

entities_input.append(QueryEntity200ResponseInner.from_dict(tp2_entity_input))


link_entity_input = link.to_dict()

logger.info("NetworkLink object representation: %s\n" % link_entity_input)

logger.info("Entity object representation for NetworkLink object: %s\n" % Entity.from_dict(link_entity_input))

entities_input.append(QueryEntity200ResponseInner.from_dict(link_entity_input))


source_entity_input = source.to_dict()

logger.info("NetworkLinkSource object representation: %s\n" % source_entity_input)

logger.info("Entity object representation for NetworkLinkSource object: %s\n" % Entity.from_dict(source_entity_input))

entities_input.append(QueryEntity200ResponseInner.from_dict(source_entity_input))


destination_entity_input = destination.to_dict()

logger.info("NetworkLinkDestination object representation: %s\n" % destination_entity_input)

logger.info("Entity object representation for NetworkLinkDestination object: %s\n" % Entity.from_dict(destination_entity_input))

entities_input.append(QueryEntity200ResponseInner.from_dict(destination_entity_input))

try:
    # Create NGSI-LD entities of type Interface and Sensor: POST /entityOperations/upsert
    api_response = api_instance.upsert_batch(query_entity200_response_inner=entities_input)
    logger.info("The response of ContextInformationProvisionApi->upsert_batch: %s\n" % api_response)
except (Exception, UserWarning) as e:
    logger.exception("Exception when calling ContextInformationProvisionApi->upsert_batch: %s\n" % e)

