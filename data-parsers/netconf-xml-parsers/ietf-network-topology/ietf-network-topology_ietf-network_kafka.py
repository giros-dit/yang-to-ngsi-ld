import json
import xml.etree.ElementTree as et
from kafka import KafkaConsumer
from kafka import KafkaProducer

dict_buffers = []
consumer = KafkaConsumer('interfaces-state-subscriptions', bootstrap_servers=['localhost:9092'])
while True:
    for message in consumer:
        xml = str(message.value.decode('utf-8'))
        root = et.fromstring(xml)
        text = root[0].text
        observed_at = text.strip() if text and text.strip() else None

        for network in root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-network}network"):
            network_dict_buffer = {}
            network_dict_buffer["id"] = "urn:ngsi-ld:Network"
            network_dict_buffer["type"] = "Network"
            networkId = network.find(".//{urn:ietf:params:xml:ns:yang:ietf-network}network-id")
            if networkId is not None:
                element_text = networkId.text
                if element_text is not None:
                    network_dict_buffer["id"] = network_dict_buffer["id"] + ":" + element_text
                    network_dict_buffer["networkId"] = {}
                    network_dict_buffer["networkId"]["type"] = "Property"
                    network_dict_buffer["networkId"]["value"] = element_text
                    if observed_at is not None:
                        network_dict_buffer["networkId"]["observedAt"] = observed_at
                    network_dict_buffer["networkId"]["datasetId"] = "urn:ngsi-ld:configuration"
            for supporting_network in network.findall(".//{urn:ietf:params:xml:ns:yang:ietf-network}supporting-network"):
                network_supporting_network_dict_buffer = {}
                network_supporting_network_dict_buffer["id"] = "urn:ngsi-ld:NetworkSupportingNetwork:" + ":".join(network_dict_buffer["id"].split(":")[3:])
                network_supporting_network_dict_buffer["type"] = "NetworkSupportingNetwork"
                network_supporting_network_dict_buffer["isPartOf"] = {}
                network_supporting_network_dict_buffer["isPartOf"]["type"] = "Relationship"
                network_supporting_network_dict_buffer["isPartOf"]["object"] = network_dict_buffer["id"]
                if observed_at is not None:
                    network_supporting_network_dict_buffer["isPartOf"]["observedAt"] = observed_at
                networkRef = supporting_network.find(".//{urn:ietf:params:xml:ns:yang:ietf-network}network-ref")
                if networkRef is not None:
                    element_text = networkRef.text
                    if element_text is not None:
                        network_supporting_network_dict_buffer["networkRef"] = {}
                        network_supporting_network_dict_buffer["networkRef"]["type"] = "Relationship"
                        network_supporting_network_dict_buffer["networkRef"]["object"] = "urn:ngsi-ld:Network" + ":" + element_text
                        if observed_at is not None:
                            network_supporting_network_dict_buffer["networkRef"]["observedAt"] = observed_at
                        network_supporting_network_dict_buffer["networkRef"]["datasetId"] = "urn:ngsi-ld:configuration"
                dict_buffers.append(network_supporting_network_dict_buffer)
            for node in network.findall(".//{urn:ietf:params:xml:ns:yang:ietf-network}node"):
                network_node_dict_buffer = {}
                network_node_dict_buffer["id"] = "urn:ngsi-ld:NetworkNode:" + ":".join(network_dict_buffer["id"].split(":")[3:])
                network_node_dict_buffer["type"] = "NetworkNode"
                network_node_dict_buffer["isPartOf"] = {}
                network_node_dict_buffer["isPartOf"]["type"] = "Relationship"
                network_node_dict_buffer["isPartOf"]["object"] = network_dict_buffer["id"]
                if observed_at is not None:
                    network_node_dict_buffer["isPartOf"]["observedAt"] = observed_at
                nodeId = node.find(".//{urn:ietf:params:xml:ns:yang:ietf-network}node-id")
                if nodeId is not None:
                    element_text = nodeId.text
                    if element_text is not None:
                        network_node_dict_buffer["id"] = network_node_dict_buffer["id"] + ":" + element_text
                        network_node_dict_buffer["nodeId"] = {}
                        network_node_dict_buffer["nodeId"]["type"] = "Property"
                        network_node_dict_buffer["nodeId"]["value"] = element_text
                        if observed_at is not None:
                            network_node_dict_buffer["nodeId"]["observedAt"] = observed_at
                        network_node_dict_buffer["nodeId"]["datasetId"] = "urn:ngsi-ld:configuration"
                for supporting_node in node.findall(".//{urn:ietf:params:xml:ns:yang:ietf-network}supporting-node"):
                    network_node_supporting_node_dict_buffer = {}
                    network_node_supporting_node_dict_buffer["id"] = "urn:ngsi-ld:NetworkNodeSupportingNode:" + ":".join(network_node_dict_buffer["id"].split(":")[3:])
                    network_node_supporting_node_dict_buffer["type"] = "NetworkNodeSupportingNode"
                    network_node_supporting_node_dict_buffer["isPartOf"] = {}
                    network_node_supporting_node_dict_buffer["isPartOf"]["type"] = "Relationship"
                    network_node_supporting_node_dict_buffer["isPartOf"]["object"] = network_node_dict_buffer["id"]
                    if observed_at is not None:
                        network_node_supporting_node_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    networkRef = supporting_node.find(".//{urn:ietf:params:xml:ns:yang:ietf-network}network-ref")
                    if networkRef is not None:
                        element_text = networkRef.text
                        if element_text is not None:
                            network_node_supporting_node_dict_buffer["networkRef"] = {}
                            network_node_supporting_node_dict_buffer["networkRef"]["type"] = "Relationship"
                            network_node_supporting_node_dict_buffer["networkRef"]["object"] = "urn:ngsi-ld:NetworkSupportingNetwork" + ":" + element_text
                            if observed_at is not None:
                                network_node_supporting_node_dict_buffer["networkRef"]["observedAt"] = observed_at
                            network_node_supporting_node_dict_buffer["networkRef"]["datasetId"] = "urn:ngsi-ld:configuration"
                    nodeRef = supporting_node.find(".//{urn:ietf:params:xml:ns:yang:ietf-network}node-ref")
                    if nodeRef is not None:
                        element_text = nodeRef.text
                        if element_text is not None:
                            network_node_supporting_node_dict_buffer["nodeRef"] = {}
                            network_node_supporting_node_dict_buffer["nodeRef"]["type"] = "Relationship"
                            network_node_supporting_node_dict_buffer["nodeRef"]["object"] = "urn:ngsi-ld:NetworkNode" + ":" + element_text
                            if observed_at is not None:
                                network_node_supporting_node_dict_buffer["nodeRef"]["observedAt"] = observed_at
                            network_node_supporting_node_dict_buffer["nodeRef"]["datasetId"] = "urn:ngsi-ld:configuration"
                    dict_buffers.append(network_node_supporting_node_dict_buffer)
                for termination_point in node.findall(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}termination-point"):
                    network_node_termination_point_dict_buffer = {}
                    network_node_termination_point_dict_buffer["id"] = "urn:ngsi-ld:NetworkNodeTerminationPoint:" + ":".join(network_node_dict_buffer["id"].split(":")[3:])
                    network_node_termination_point_dict_buffer["type"] = "NetworkNodeTerminationPoint"
                    network_node_termination_point_dict_buffer["isPartOf"] = {}
                    network_node_termination_point_dict_buffer["isPartOf"]["type"] = "Relationship"
                    network_node_termination_point_dict_buffer["isPartOf"]["object"] = network_node_dict_buffer["id"]
                    if observed_at is not None:
                        network_node_termination_point_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    tpId = termination_point.find(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}tp-id")
                    if tpId is not None:
                        element_text = tpId.text
                        if element_text is not None:
                            network_node_termination_point_dict_buffer["id"] = network_node_termination_point_dict_buffer["id"] + ":" + element_text
                            network_node_termination_point_dict_buffer["tpId"] = {}
                            network_node_termination_point_dict_buffer["tpId"]["type"] = "Property"
                            network_node_termination_point_dict_buffer["tpId"]["value"] = element_text
                            if observed_at is not None:
                                network_node_termination_point_dict_buffer["tpId"]["observedAt"] = observed_at
                            network_node_termination_point_dict_buffer["tpId"]["datasetId"] = "urn:ngsi-ld:configuration"
                    for supporting_termination_point in termination_point.findall(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}supporting-termination-point"):
                        network_node_termination_point_supporting_termination_point_dict_buffer = {}
                        network_node_termination_point_supporting_termination_point_dict_buffer["id"] = "urn:ngsi-ld:NetworkNodeTerminationPointSupportingTerminationPoint:" + ":".join(network_node_termination_point_dict_buffer["id"].split(":")[3:])
                        network_node_termination_point_supporting_termination_point_dict_buffer["type"] = "NetworkNodeTerminationPointSupportingTerminationPoint"
                        network_node_termination_point_supporting_termination_point_dict_buffer["isPartOf"] = {}
                        network_node_termination_point_supporting_termination_point_dict_buffer["isPartOf"]["type"] = "Relationship"
                        network_node_termination_point_supporting_termination_point_dict_buffer["isPartOf"]["object"] = network_node_termination_point_dict_buffer["id"]
                        if observed_at is not None:
                            network_node_termination_point_supporting_termination_point_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        networkRef = supporting_termination_point.find(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}network-ref")
                        if networkRef is not None:
                            element_text = networkRef.text
                            if element_text is not None:
                                network_node_termination_point_supporting_termination_point_dict_buffer["networkRef"] = {}
                                network_node_termination_point_supporting_termination_point_dict_buffer["networkRef"]["type"] = "Relationship"
                                network_node_termination_point_supporting_termination_point_dict_buffer["networkRef"]["object"] = "urn:ngsi-ld:NetworkNodeSupportingNode" + ":" + element_text
                                if observed_at is not None:
                                    network_node_termination_point_supporting_termination_point_dict_buffer["networkRef"]["observedAt"] = observed_at
                                network_node_termination_point_supporting_termination_point_dict_buffer["networkRef"]["datasetId"] = "urn:ngsi-ld:configuration"
                        nodeRef = supporting_termination_point.find(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}node-ref")
                        if nodeRef is not None:
                            element_text = nodeRef.text
                            if element_text is not None:
                                network_node_termination_point_supporting_termination_point_dict_buffer["nodeRef"] = {}
                                network_node_termination_point_supporting_termination_point_dict_buffer["nodeRef"]["type"] = "Relationship"
                                network_node_termination_point_supporting_termination_point_dict_buffer["nodeRef"]["object"] = "urn:ngsi-ld:NetworkNodeSupportingNode" + ":" + element_text
                                if observed_at is not None:
                                    network_node_termination_point_supporting_termination_point_dict_buffer["nodeRef"]["observedAt"] = observed_at
                                network_node_termination_point_supporting_termination_point_dict_buffer["nodeRef"]["datasetId"] = "urn:ngsi-ld:configuration"
                        tpRef = supporting_termination_point.find(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}tp-ref")
                        if tpRef is not None:
                            element_text = tpRef.text
                            if element_text is not None:
                                network_node_termination_point_supporting_termination_point_dict_buffer["tpRef"] = {}
                                network_node_termination_point_supporting_termination_point_dict_buffer["tpRef"]["type"] = "Relationship"
                                network_node_termination_point_supporting_termination_point_dict_buffer["tpRef"]["object"] = "urn:ngsi-ld:NetworkNodeTerminationPoint" + ":" + element_text
                                if observed_at is not None:
                                    network_node_termination_point_supporting_termination_point_dict_buffer["tpRef"]["observedAt"] = observed_at
                                network_node_termination_point_supporting_termination_point_dict_buffer["tpRef"]["datasetId"] = "urn:ngsi-ld:configuration"
                        dict_buffers.append(network_node_termination_point_supporting_termination_point_dict_buffer)
                    dict_buffers.append(network_node_termination_point_dict_buffer)
                dict_buffers.append(network_node_dict_buffer)
            for link in network.findall(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}link"):
                network_link_dict_buffer = {}
                network_link_dict_buffer["id"] = "urn:ngsi-ld:NetworkLink:" + ":".join(network_dict_buffer["id"].split(":")[3:])
                network_link_dict_buffer["type"] = "NetworkLink"
                network_link_dict_buffer["isPartOf"] = {}
                network_link_dict_buffer["isPartOf"]["type"] = "Relationship"
                network_link_dict_buffer["isPartOf"]["object"] = network_dict_buffer["id"]
                if observed_at is not None:
                    network_link_dict_buffer["isPartOf"]["observedAt"] = observed_at
                linkId = link.find(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}link-id")
                if linkId is not None:
                    element_text = linkId.text
                    if element_text is not None:
                        network_link_dict_buffer["id"] = network_link_dict_buffer["id"] + ":" + element_text
                        network_link_dict_buffer["linkId"] = {}
                        network_link_dict_buffer["linkId"]["type"] = "Property"
                        network_link_dict_buffer["linkId"]["value"] = element_text
                        if observed_at is not None:
                            network_link_dict_buffer["linkId"]["observedAt"] = observed_at
                        network_link_dict_buffer["linkId"]["datasetId"] = "urn:ngsi-ld:configuration"
                for source in link.findall(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}source"):
                    network_link_source_dict_buffer = {}
                    network_link_source_dict_buffer["id"] = "urn:ngsi-ld:NetworkLinkSource:" + ":".join(network_link_dict_buffer["id"].split(":")[3:])
                    network_link_source_dict_buffer["type"] = "NetworkLinkSource"
                    network_link_source_dict_buffer["isPartOf"] = {}
                    network_link_source_dict_buffer["isPartOf"]["type"] = "Relationship"
                    network_link_source_dict_buffer["isPartOf"]["object"] = network_link_dict_buffer["id"]
                    if observed_at is not None:
                        network_link_source_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    sourceNode = source.find(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}source-node")
                    if sourceNode is not None:
                        element_text = sourceNode.text
                        if element_text is not None:
                            network_link_source_dict_buffer["sourceNode"] = {}
                            network_link_source_dict_buffer["sourceNode"]["type"] = "Relationship"
                            network_link_source_dict_buffer["sourceNode"]["object"] = "urn:ngsi-ld:NetworkNode" + ":" + element_text
                            if observed_at is not None:
                                network_link_source_dict_buffer["sourceNode"]["observedAt"] = observed_at
                            network_link_source_dict_buffer["sourceNode"]["datasetId"] = "urn:ngsi-ld:configuration"
                    sourceTp = source.find(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}source-tp")
                    if sourceTp is not None:
                        element_text = sourceTp.text
                        if element_text is not None:
                            network_link_source_dict_buffer["sourceTp"] = {}
                            network_link_source_dict_buffer["sourceTp"]["type"] = "Relationship"
                            network_link_source_dict_buffer["sourceTp"]["object"] = "urn:ngsi-ld:NetworkNodeTerminationPoint" + ":" + element_text
                            if observed_at is not None:
                                network_link_source_dict_buffer["sourceTp"]["observedAt"] = observed_at
                            network_link_source_dict_buffer["sourceTp"]["datasetId"] = "urn:ngsi-ld:configuration"
                    dict_buffers.append(network_link_source_dict_buffer)
                for destination in link.findall(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}destination"):
                    network_link_destination_dict_buffer = {}
                    network_link_destination_dict_buffer["id"] = "urn:ngsi-ld:NetworkLinkDestination:" + ":".join(network_link_dict_buffer["id"].split(":")[3:])
                    network_link_destination_dict_buffer["type"] = "NetworkLinkDestination"
                    network_link_destination_dict_buffer["isPartOf"] = {}
                    network_link_destination_dict_buffer["isPartOf"]["type"] = "Relationship"
                    network_link_destination_dict_buffer["isPartOf"]["object"] = network_link_dict_buffer["id"]
                    if observed_at is not None:
                        network_link_destination_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    destNode = destination.find(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}dest-node")
                    if destNode is not None:
                        element_text = destNode.text
                        if element_text is not None:
                            network_link_destination_dict_buffer["destNode"] = {}
                            network_link_destination_dict_buffer["destNode"]["type"] = "Relationship"
                            network_link_destination_dict_buffer["destNode"]["object"] = "urn:ngsi-ld:NetworkNode" + ":" + element_text
                            if observed_at is not None:
                                network_link_destination_dict_buffer["destNode"]["observedAt"] = observed_at
                            network_link_destination_dict_buffer["destNode"]["datasetId"] = "urn:ngsi-ld:configuration"
                    destTp = destination.find(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}dest-tp")
                    if destTp is not None:
                        element_text = destTp.text
                        if element_text is not None:
                            network_link_destination_dict_buffer["destTp"] = {}
                            network_link_destination_dict_buffer["destTp"]["type"] = "Relationship"
                            network_link_destination_dict_buffer["destTp"]["object"] = "urn:ngsi-ld:NetworkNodeTerminationPoint" + ":" + element_text
                            if observed_at is not None:
                                network_link_destination_dict_buffer["destTp"]["observedAt"] = observed_at
                            network_link_destination_dict_buffer["destTp"]["datasetId"] = "urn:ngsi-ld:configuration"
                    dict_buffers.append(network_link_destination_dict_buffer)
                for supporting_link in link.findall(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}supporting-link"):
                    network_link_supporting_link_dict_buffer = {}
                    network_link_supporting_link_dict_buffer["id"] = "urn:ngsi-ld:NetworkLinkSupportingLink:" + ":".join(network_link_dict_buffer["id"].split(":")[3:])
                    network_link_supporting_link_dict_buffer["type"] = "NetworkLinkSupportingLink"
                    network_link_supporting_link_dict_buffer["isPartOf"] = {}
                    network_link_supporting_link_dict_buffer["isPartOf"]["type"] = "Relationship"
                    network_link_supporting_link_dict_buffer["isPartOf"]["object"] = network_link_dict_buffer["id"]
                    if observed_at is not None:
                        network_link_supporting_link_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    networkRef = supporting_link.find(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}network-ref")
                    if networkRef is not None:
                        element_text = networkRef.text
                        if element_text is not None:
                            network_link_supporting_link_dict_buffer["networkRef"] = {}
                            network_link_supporting_link_dict_buffer["networkRef"]["type"] = "Relationship"
                            network_link_supporting_link_dict_buffer["networkRef"]["object"] = "urn:ngsi-ld:NetworkSupportingNetwork" + ":" + element_text
                            if observed_at is not None:
                                network_link_supporting_link_dict_buffer["networkRef"]["observedAt"] = observed_at
                            network_link_supporting_link_dict_buffer["networkRef"]["datasetId"] = "urn:ngsi-ld:configuration"
                    linkRef = supporting_link.find(".//{urn:ietf:params:xml:ns:yang:ietf-network-topology}link-ref")
                    if linkRef is not None:
                        element_text = linkRef.text
                        if element_text is not None:
                            network_link_supporting_link_dict_buffer["linkRef"] = {}
                            network_link_supporting_link_dict_buffer["linkRef"]["type"] = "Relationship"
                            network_link_supporting_link_dict_buffer["linkRef"]["object"] = "urn:ngsi-ld:NetworkLink" + ":" + element_text
                            if observed_at is not None:
                                network_link_supporting_link_dict_buffer["linkRef"]["observedAt"] = observed_at
                            network_link_supporting_link_dict_buffer["linkRef"]["datasetId"] = "urn:ngsi-ld:configuration"
                    dict_buffers.append(network_link_supporting_link_dict_buffer)
                dict_buffers.append(network_link_dict_buffer)
            dict_buffers.append(network_dict_buffer)

        producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
        producer.send('dictionary-buffers', value=json.dumps(dict_buffers[::-1], indent=4).encode('utf-8'))
        producer.flush()
        dict_buffers.clear()
