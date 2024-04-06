import json
import numpy as np
from datetime import datetime
import sys

json_payload = sys.argv[1]
dict_buffers = []
with open(json_payload) as f:
    data = json.load(f)
if data.get("networks")is not None:
    networks = data.get("networks")
elif data.get("ietf-network:networks")is not None:
    networks = data.get("ietf-network:networks")
if networks is not None and len(networks) != 0:
    if "network" in list(networks.keys()):
        networks = networks.get("network")
    elif "ietf-network:network" in list(networks.keys()):
        networks = networks.get("ietf-network:network")
    for network in networks:
        if network is not None and len(network) != 0:
            network_dict_buffer = {}
            network_dict_buffer["id"] = "urn:ngsi-ld:Network"
            network_dict_buffer["type"] = "Network"
            networkId = network.get("network-id")
            if networkId is not None:
                element_text = networkId
                if network_dict_buffer["id"].split(":")[-1] != element_text:
                    network_dict_buffer["id"] = network_dict_buffer["id"] + ":" + str(element_text)
                network_dict_buffer["networkId"] = {}
                network_dict_buffer["networkId"]["type"] = "Property"
                network_dict_buffer["networkId"]["value"] = element_text
            network_supporting_network = network.get("supporting-network")
            if network_supporting_network is not None and len(network_supporting_network) != 0:
                for supporting_network in network_supporting_network:
                    network_supporting_network_dict_buffer = {}
                    network_supporting_network_dict_buffer["id"] = "urn:ngsi-ld:NetworkSupportingNetwork:" + ":".join(network_dict_buffer["id"].split(":")[3:])
                    network_supporting_network_dict_buffer["type"] = "NetworkSupportingNetwork"
                    network_supporting_network_dict_buffer["isPartOf"] = {}
                    network_supporting_network_dict_buffer["isPartOf"]["type"] = "Relationship"
                    network_supporting_network_dict_buffer["isPartOf"]["object"] = network_dict_buffer["id"]
                    networkRef = supporting_network.get("network-ref")
                    if networkRef is not None:
                        element_text = networkRef
                    dict_buffers.append(network_supporting_network_dict_buffer)
            network_node = network.get("node")
            if network_node is not None and len(network_node) != 0:
                for node in network_node:
                    network_node_dict_buffer = {}
                    network_node_dict_buffer["id"] = "urn:ngsi-ld:NetworkNode:" + ":".join(network_dict_buffer["id"].split(":")[3:])
                    network_node_dict_buffer["type"] = "NetworkNode"
                    network_node_dict_buffer["isPartOf"] = {}
                    network_node_dict_buffer["isPartOf"]["type"] = "Relationship"
                    network_node_dict_buffer["isPartOf"]["object"] = network_dict_buffer["id"]
                    nodeId = node.get("node-id")
                    if nodeId is not None:
                        element_text = nodeId
                        if network_node_dict_buffer["id"].split(":")[-1] != element_text:
                            network_node_dict_buffer["id"] = network_node_dict_buffer["id"] + ":" + str(element_text)
                        network_node_dict_buffer["nodeId"] = {}
                        network_node_dict_buffer["nodeId"]["type"] = "Property"
                        network_node_dict_buffer["nodeId"]["value"] = element_text
                    node_supporting_node = node.get("supporting-node")
                    if node_supporting_node is not None and len(node_supporting_node) != 0:
                        for supporting_node in node_supporting_node:
                            network_node_supporting_node_dict_buffer = {}
                            network_node_supporting_node_dict_buffer["id"] = "urn:ngsi-ld:NetworkNodeSupportingNode:" + ":".join(network_node_dict_buffer["id"].split(":")[3:])
                            network_node_supporting_node_dict_buffer["type"] = "NetworkNodeSupportingNode"
                            network_node_supporting_node_dict_buffer["isPartOf"] = {}
                            network_node_supporting_node_dict_buffer["isPartOf"]["type"] = "Relationship"
                            network_node_supporting_node_dict_buffer["isPartOf"]["object"] = network_node_dict_buffer["id"]
                            networkRef = supporting_node.get("network-ref")
                            if networkRef is not None:
                                element_text = networkRef
                            nodeRef = supporting_node.get("node-ref")
                            if nodeRef is not None:
                                element_text = nodeRef
                            dict_buffers.append(network_node_supporting_node_dict_buffer)
                    node_termination_point = node.get("ietf-network-topology:termination-point")
                    if node_termination_point is not None and len(node_termination_point) != 0:
                        for termination_point in node_termination_point:
                            network_node_termination_point_dict_buffer = {}
                            network_node_termination_point_dict_buffer["id"] = "urn:ngsi-ld:NetworkNodeTerminationPoint:" + ":".join(network_node_dict_buffer["id"].split(":")[3:])
                            network_node_termination_point_dict_buffer["type"] = "NetworkNodeTerminationPoint"
                            network_node_termination_point_dict_buffer["isPartOf"] = {}
                            network_node_termination_point_dict_buffer["isPartOf"]["type"] = "Relationship"
                            network_node_termination_point_dict_buffer["isPartOf"]["object"] = network_node_dict_buffer["id"]
                            tpId = termination_point.get("tp-id")
                            if tpId is not None:
                                element_text = tpId
                                if network_node_termination_point_dict_buffer["id"].split(":")[-1] != element_text:
                                    network_node_termination_point_dict_buffer["id"] = network_node_termination_point_dict_buffer["id"] + ":" + str(element_text)
                                network_node_termination_point_dict_buffer["tpId"] = {}
                                network_node_termination_point_dict_buffer["tpId"]["type"] = "Property"
                                network_node_termination_point_dict_buffer["tpId"]["value"] = element_text
                            termination_point_supporting_termination_point = termination_point.get("supporting-termination-point")
                            if termination_point_supporting_termination_point is not None and len(termination_point_supporting_termination_point) != 0:
                                for supporting_termination_point in termination_point_supporting_termination_point:
                                    network_node_termination_point_supporting_termination_point_dict_buffer = {}
                                    network_node_termination_point_supporting_termination_point_dict_buffer["id"] = "urn:ngsi-ld:NetworkNodeTerminationPointSupportingTerminationPoint:" + ":".join(network_node_termination_point_dict_buffer["id"].split(":")[3:])
                                    network_node_termination_point_supporting_termination_point_dict_buffer["type"] = "NetworkNodeTerminationPointSupportingTerminationPoint"
                                    network_node_termination_point_supporting_termination_point_dict_buffer["isPartOf"] = {}
                                    network_node_termination_point_supporting_termination_point_dict_buffer["isPartOf"]["type"] = "Relationship"
                                    network_node_termination_point_supporting_termination_point_dict_buffer["isPartOf"]["object"] = network_node_termination_point_dict_buffer["id"]
                                    networkRef = supporting_termination_point.get("network-ref")
                                    if networkRef is not None:
                                        element_text = networkRef
                                    nodeRef = supporting_termination_point.get("node-ref")
                                    if nodeRef is not None:
                                        element_text = nodeRef
                                    tpRef = supporting_termination_point.get("tp-ref")
                                    if tpRef is not None:
                                        element_text = tpRef
                                    dict_buffers.append(network_node_termination_point_supporting_termination_point_dict_buffer)
                            dict_buffers.append(network_node_termination_point_dict_buffer)
                    dict_buffers.append(network_node_dict_buffer)
            network_link = network.get("ietf-network-topology:link")
            if network_link is not None and len(network_link) != 0:
                for link in network_link:
                    network_link_dict_buffer = {}
                    network_link_dict_buffer["id"] = "urn:ngsi-ld:NetworkLink:" + ":".join(network_dict_buffer["id"].split(":")[3:])
                    network_link_dict_buffer["type"] = "NetworkLink"
                    network_link_dict_buffer["isPartOf"] = {}
                    network_link_dict_buffer["isPartOf"]["type"] = "Relationship"
                    network_link_dict_buffer["isPartOf"]["object"] = network_dict_buffer["id"]
                    linkId = link.get("link-id")
                    if linkId is not None:
                        element_text = linkId
                        if network_link_dict_buffer["id"].split(":")[-1] != element_text:
                            network_link_dict_buffer["id"] = network_link_dict_buffer["id"] + ":" + str(element_text)
                        network_link_dict_buffer["linkId"] = {}
                        network_link_dict_buffer["linkId"]["type"] = "Property"
                        network_link_dict_buffer["linkId"]["value"] = element_text
                    source = link.get("source")
                    if source is not None and len(source) != 0:
                        network_link_source_dict_buffer = {}
                        network_link_source_dict_buffer["id"] = "urn:ngsi-ld:NetworkLinkSource:" + ":".join(network_link_dict_buffer["id"].split(":")[3:])
                        network_link_source_dict_buffer["type"] = "NetworkLinkSource"
                        network_link_source_dict_buffer["isPartOf"] = {}
                        network_link_source_dict_buffer["isPartOf"]["type"] = "Relationship"
                        network_link_source_dict_buffer["isPartOf"]["object"] = network_link_dict_buffer["id"]
                        sourceNode = source.get("source-node")
                        if sourceNode is not None:
                            element_text = sourceNode
                            if network_link_source_dict_buffer["id"].split(":")[-1] != element_text:
                                network_link_source_dict_buffer["id"] = network_link_source_dict_buffer["id"] + ":" + element_text
                            network_link_source_dict_buffer["sourceNode"] = {}
                            network_link_source_dict_buffer["sourceNode"]["type"] = "Relationship"
                            network_link_source_dict_buffer["sourceNode"]["object"] = "urn:ngsi-ld:NetworkNode:" + ":".join(network_link_source_dict_buffer["id"].split(":")[3:])
                        sourceTp = source.get("source-tp")
                        if sourceTp is not None:
                            element_text = sourceTp
                            if network_link_source_dict_buffer["id"].split(":")[-1] != element_text:
                                network_link_source_dict_buffer["id"] = network_link_source_dict_buffer["id"] + ":" + element_text
                            network_link_source_dict_buffer["sourceTp"] = {}
                            network_link_source_dict_buffer["sourceTp"]["type"] = "Relationship"
                            network_link_source_dict_buffer["sourceTp"]["object"] = "urn:ngsi-ld:NetworkNodeTerminationPoint:" + ":".join(network_link_source_dict_buffer["id"].split(":")[3:])
                        dict_buffers.append(network_link_source_dict_buffer)
                    destination = link.get("destination")
                    if destination is not None and len(destination) != 0:
                        network_link_destination_dict_buffer = {}
                        network_link_destination_dict_buffer["id"] = "urn:ngsi-ld:NetworkLinkDestination:" + ":".join(network_link_dict_buffer["id"].split(":")[3:])
                        network_link_destination_dict_buffer["type"] = "NetworkLinkDestination"
                        network_link_destination_dict_buffer["isPartOf"] = {}
                        network_link_destination_dict_buffer["isPartOf"]["type"] = "Relationship"
                        network_link_destination_dict_buffer["isPartOf"]["object"] = network_link_dict_buffer["id"]
                        destNode = destination.get("dest-node")
                        if destNode is not None:
                            element_text = destNode
                            if network_link_destination_dict_buffer["id"].split(":")[-1] != element_text:
                                network_link_destination_dict_buffer["id"] = network_link_destination_dict_buffer["id"] + ":" + element_text
                            network_link_destination_dict_buffer["destNode"] = {}
                            network_link_destination_dict_buffer["destNode"]["type"] = "Relationship"
                            network_link_destination_dict_buffer["destNode"]["object"] = "urn:ngsi-ld:NetworkNode:" + ":".join(network_link_destination_dict_buffer["id"].split(":")[3:])
                        destTp = destination.get("dest-tp")
                        if destTp is not None:
                            element_text = destTp
                            if network_link_destination_dict_buffer["id"].split(":")[-1] != element_text:
                                network_link_destination_dict_buffer["id"] = network_link_destination_dict_buffer["id"] + ":" + element_text
                            network_link_destination_dict_buffer["destTp"] = {}
                            network_link_destination_dict_buffer["destTp"]["type"] = "Relationship"
                            network_link_destination_dict_buffer["destTp"]["object"] = "urn:ngsi-ld:NetworkNodeTerminationPoint:" + ":".join(network_link_destination_dict_buffer["id"].split(":")[3:])
                        dict_buffers.append(network_link_destination_dict_buffer)
                    link_supporting_link = link.get("supporting-link")
                    if link_supporting_link is not None and len(link_supporting_link) != 0:
                        for supporting_link in link_supporting_link:
                            network_link_supporting_link_dict_buffer = {}
                            network_link_supporting_link_dict_buffer["id"] = "urn:ngsi-ld:NetworkLinkSupportingLink:" + ":".join(network_link_dict_buffer["id"].split(":")[3:])
                            network_link_supporting_link_dict_buffer["type"] = "NetworkLinkSupportingLink"
                            network_link_supporting_link_dict_buffer["isPartOf"] = {}
                            network_link_supporting_link_dict_buffer["isPartOf"]["type"] = "Relationship"
                            network_link_supporting_link_dict_buffer["isPartOf"]["object"] = network_link_dict_buffer["id"]
                            networkRef = supporting_link.get("network-ref")
                            if networkRef is not None:
                                element_text = networkRef
                            linkRef = supporting_link.get("link-ref")
                            if linkRef is not None:
                                element_text = linkRef
                            dict_buffers.append(network_link_supporting_link_dict_buffer)
                    dict_buffers.append(network_link_dict_buffer)
            dict_buffers.append(network_dict_buffer)

output_file = open("dict_buffers.json", 'w')
output_file.write(json.dumps(dict_buffers[::-1], indent=4))
output_file.close()
dict_buffers.clear()
