import sys
import json
import xml.etree.ElementTree as et
from kafka import KafkaConsumer, KafkaProducer

xml = sys.argv[1]
tree = et.parse(xml)
root = tree.getroot()
dict_buffers = []

for network in root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-network}network"):
    network_dict_buffer = {}
    network_dict_buffer["id"] = "urn:ngsi-ld:Network:"
    network_dict_buffer["type"] = "Network"
    networkId = network.find(".//{urn:ietf:params:xml:ns:yang:ietf-network}network-id")
    if networkId is not None:
        element_text = networkId.text
        if element_text is not None:
            network_dict_buffer["id"] = network_dict_buffer["id"] + element_text
            network_dict_buffer["networkId"] = {}
            network_dict_buffer["networkId"]["type"] = "Property"
            network_dict_buffer["networkId"]["value"] = element_text
    for supporting_network in network.findall(".//{urn:ietf:params:xml:ns:yang:ietf-network}supporting-network"):
        network_supporting_network_dict_buffer = {}
        network_supporting_network_dict_buffer["id"] = "urn:ngsi-ld:NetworkSupportingNetwork:" + network_dict_buffer["id"].split(":")[-1] + ":"
        network_supporting_network_dict_buffer["type"] = "NetworkSupportingNetwork"
        network_supporting_network_dict_buffer["isPartOf"] = {}
        network_supporting_network_dict_buffer["isPartOf"]["type"] = "Relationship"
        network_supporting_network_dict_buffer["isPartOf"]["object"] = network_dict_buffer["id"]
        dict_buffers.append(network_supporting_network_dict_buffer)
    for node in network.findall(".//{urn:ietf:params:xml:ns:yang:ietf-network}node"):
        network_node_dict_buffer = {}
        network_node_dict_buffer["id"] = "urn:ngsi-ld:NetworkNode:" + network_dict_buffer["id"].split(":")[-1] + ":"
        network_node_dict_buffer["type"] = "NetworkNode"
        network_node_dict_buffer["isPartOf"] = {}
        network_node_dict_buffer["isPartOf"]["type"] = "Relationship"
        network_node_dict_buffer["isPartOf"]["object"] = network_dict_buffer["id"]
        nodeId = node.find(".//{urn:ietf:params:xml:ns:yang:ietf-network}node-id")
        if nodeId is not None:
            element_text = nodeId.text
            if element_text is not None:
                network_node_dict_buffer["id"] = network_node_dict_buffer["id"] + element_text
                network_node_dict_buffer["nodeId"] = {}
                network_node_dict_buffer["nodeId"]["type"] = "Property"
                network_node_dict_buffer["nodeId"]["value"] = element_text
        for supporting_node in node.findall(".//{urn:ietf:params:xml:ns:yang:ietf-network}supporting-node"):
            network_node_supporting_node_dict_buffer = {}
            network_node_supporting_node_dict_buffer["id"] = "urn:ngsi-ld:NetworkNodeSupportingNode:" + network_node_dict_buffer["id"].split(":")[-1] + ":"
            network_node_supporting_node_dict_buffer["type"] = "NetworkNodeSupportingNode"
            network_node_supporting_node_dict_buffer["isPartOf"] = {}
            network_node_supporting_node_dict_buffer["isPartOf"]["type"] = "Relationship"
            network_node_supporting_node_dict_buffer["isPartOf"]["object"] = network_node_dict_buffer["id"]
            dict_buffers.append(network_node_supporting_node_dict_buffer)
        for termination_point in node.findall(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}termination-point"):
            network_node_termination_point_dict_buffer = {}
            network_node_termination_point_dict_buffer["id"] = "urn:ngsi-ld:NetworkNodeTerminationPoint:" + network_node_dict_buffer["id"].split(":")[-1] + ":"
            network_node_termination_point_dict_buffer["type"] = "NetworkNodeTerminationPoint"
            network_node_termination_point_dict_buffer["isPartOf"] = {}
            network_node_termination_point_dict_buffer["isPartOf"]["type"] = "Relationship"
            network_node_termination_point_dict_buffer["isPartOf"]["object"] = network_node_dict_buffer["id"]
            tpId = termination_point.find(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}tp-id")
            if tpId is not None:
                element_text = tpId.text
                if element_text is not None:
                    network_node_termination_point_dict_buffer["id"] = network_node_termination_point_dict_buffer["id"] + element_text
                    network_node_termination_point_dict_buffer["tpId"] = {}
                    network_node_termination_point_dict_buffer["tpId"]["type"] = "Property"
                    network_node_termination_point_dict_buffer["tpId"]["value"] = element_text
            for supporting_termination_point in termination_point.findall(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}supporting-termination-point"):
                network_node_termination_point_supporting_termination_point_dict_buffer = {}
                network_node_termination_point_supporting_termination_point_dict_buffer["id"] = "urn:ngsi-ld:NetworkNodeTerminationPointSupportingTerminationPoint:" + network_node_termination_point_dict_buffer["id"].split(":")[-1] + ":"
                network_node_termination_point_supporting_termination_point_dict_buffer["type"] = "NetworkNodeTerminationPointSupportingTerminationPoint"
                network_node_termination_point_supporting_termination_point_dict_buffer["isPartOf"] = {}
                network_node_termination_point_supporting_termination_point_dict_buffer["isPartOf"]["type"] = "Relationship"
                network_node_termination_point_supporting_termination_point_dict_buffer["isPartOf"]["object"] = network_node_termination_point_dict_buffer["id"]
                dict_buffers.append(network_node_termination_point_supporting_termination_point_dict_buffer)
            dict_buffers.append(network_node_termination_point_dict_buffer)
        dict_buffers.append(network_node_dict_buffer)
    for link in network.findall(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}link"):
        network_link_dict_buffer = {}
        network_link_dict_buffer["id"] = "urn:ngsi-ld:NetworkLink:" + network_dict_buffer["id"].split(":")[-1] + ":"
        network_link_dict_buffer["type"] = "NetworkLink"
        network_link_dict_buffer["isPartOf"] = {}
        network_link_dict_buffer["isPartOf"]["type"] = "Relationship"
        network_link_dict_buffer["isPartOf"]["object"] = network_dict_buffer["id"]
        linkId = link.find(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}link-id")
        if linkId is not None:
            element_text = linkId.text
            if element_text is not None:
                network_link_dict_buffer["id"] = network_link_dict_buffer["id"] + element_text
                network_link_dict_buffer["linkId"] = {}
                network_link_dict_buffer["linkId"]["type"] = "Property"
                network_link_dict_buffer["linkId"]["value"] = element_text
        for source in link.findall(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}source"):
            network_link_source_dict_buffer = {}
            network_link_source_dict_buffer["id"] = "urn:ngsi-ld:NetworkLinkSource:" + network_link_dict_buffer["id"].split(":")[-1] + ":"
            network_link_source_dict_buffer["type"] = "NetworkLinkSource"
            network_link_source_dict_buffer["isPartOf"] = {}
            network_link_source_dict_buffer["isPartOf"]["type"] = "Relationship"
            network_link_source_dict_buffer["isPartOf"]["object"] = network_link_dict_buffer["id"]
            dict_buffers.append(network_link_source_dict_buffer)
        for destination in link.findall(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}destination"):
            network_link_destination_dict_buffer = {}
            network_link_destination_dict_buffer["id"] = "urn:ngsi-ld:NetworkLinkDestination:" + network_link_dict_buffer["id"].split(":")[-1] + ":"
            network_link_destination_dict_buffer["type"] = "NetworkLinkDestination"
            network_link_destination_dict_buffer["isPartOf"] = {}
            network_link_destination_dict_buffer["isPartOf"]["type"] = "Relationship"
            network_link_destination_dict_buffer["isPartOf"]["object"] = network_link_dict_buffer["id"]
            dict_buffers.append(network_link_destination_dict_buffer)
        for supporting_link in link.findall(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}supporting-link"):
            network_link_supporting_link_dict_buffer = {}
            network_link_supporting_link_dict_buffer["id"] = "urn:ngsi-ld:NetworkLinkSupportingLink:" + network_link_dict_buffer["id"].split(":")[-1] + ":"
            network_link_supporting_link_dict_buffer["type"] = "NetworkLinkSupportingLink"
            network_link_supporting_link_dict_buffer["isPartOf"] = {}
            network_link_supporting_link_dict_buffer["isPartOf"]["type"] = "Relationship"
            network_link_supporting_link_dict_buffer["isPartOf"]["object"] = network_link_dict_buffer["id"]
            dict_buffers.append(network_link_supporting_link_dict_buffer)
        dict_buffers.append(network_link_dict_buffer)
    dict_buffers.append(network_dict_buffer)

print(json.dumps(dict_buffers[::-1], indent=4))
