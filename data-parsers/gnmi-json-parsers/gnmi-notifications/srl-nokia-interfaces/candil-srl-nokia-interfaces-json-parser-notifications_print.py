import json
import numpy as np
from collections import defaultdict
import sys

json_payload = sys.argv[1]
dict_buffers = []

with open(json_payload) as f:
    data = json.load(f)

for item in data:
    parent_paths = []
    child_nodes = []
    values = []
    iteration_keys = {}
    for key, value in item['values'].items():
        parent_paths.append(key.split("/")[1:-1])
        child_nodes.append(key.split("/")[-1])
        values.append(value)
    source = "-".join(item['tags']['source'].split("-")[1:-1]) + ":" + str(item['tags']['source'].split("-")[-1])
    timestamp_data = int(item['timestamp'])
    datetime_ns = np.datetime64(timestamp_data, 'ns')
    observed_at = str(datetime_ns.astype('datetime64[ms]')) + 'Z'
    for i_key, i_value in item['tags'].items():
        if i_key != 'source' and i_key != 'subscription-name':
            iteration_keys[i_key] = i_value

    for element_text, child_node, parent_path in zip(values, child_nodes, parent_paths):
        if parent_path[0] == "interface" or parent_path[0] == "srl_nokia-interfaces:interface":
            interface_dict_buffer = {}
            if "interface_name" in iteration_keys:
                interface_dict_buffer["id"] = "urn:ngsi-ld:Interface:" + source + ":" +  iteration_keys.get("interface_name")
            interface_dict_buffer["type"] = "Interface"
        if child_node == "name":
            if interface_dict_buffer["id"].split(":")[-1] != element_text:
                interface_dict_buffer["id"] = interface_dict_buffer["id"] + ":" + element_text
            interface_dict_buffer["name"] = {}
            interface_dict_buffer["name"]["type"] = "Property"
            interface_dict_buffer["name"]["value"] = element_text
            interface_dict_buffer["name"]["observedAt"] = observed_at
        if child_node == "description":
            interface_dict_buffer["description"] = {}
            interface_dict_buffer["description"]["type"] = "Property"
            interface_dict_buffer["description"]["value"] = element_text
            interface_dict_buffer["description"]["observedAt"] = observed_at
        if child_node == "admin-state":
            interface_dict_buffer["adminState"] = {}
            interface_dict_buffer["adminState"]["type"] = "Property"
            interface_dict_buffer["adminState"]["value"] = element_text
            interface_dict_buffer["adminState"]["observedAt"] = observed_at
        if parent_path[1] == "breakout-mode":
            interface_breakout_mode_dict_buffer = {}
            interface_breakout_mode_dict_buffer["id"] = "urn:ngsi-ld:InterfaceBreakoutMode:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
            interface_breakout_mode_dict_buffer["type"] = "InterfaceBreakoutMode"
            if len(parent_path) - 1 == 1 or len(parent_path) - 1 == 2:
                interface_breakout_mode_dict_buffer["isPartOf"] = {}
                interface_breakout_mode_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_breakout_mode_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                interface_breakout_mode_dict_buffer["isPartOf"]["observedAt"] = observed_at
                if child_node == "num-breakout-ports":
                    interface_breakout_mode_dict_buffer["numBreakoutPorts"] = {}
                    interface_breakout_mode_dict_buffer["numBreakoutPorts"]["type"] = "Property"
                    interface_breakout_mode_dict_buffer["numBreakoutPorts"]["value"] = element_text
                    interface_breakout_mode_dict_buffer["numBreakoutPorts"]["observedAt"] = observed_at
                if child_node == "breakout-port-speed":
                    interface_breakout_mode_dict_buffer["breakoutPortSpeed"] = {}
                    interface_breakout_mode_dict_buffer["breakoutPortSpeed"]["type"] = "Property"
                    interface_breakout_mode_dict_buffer["breakoutPortSpeed"]["value"] = element_text
                    interface_breakout_mode_dict_buffer["breakoutPortSpeed"]["observedAt"] = observed_at
                if len(parent_path) - 1 == 1:
                    dict_buffers.append(interface_breakout_mode_dict_buffer)
        if child_node == "mtu":
            interface_dict_buffer["mtu"] = {}
            interface_dict_buffer["mtu"]["type"] = "Property"
            interface_dict_buffer["mtu"]["value"] = int(element_text)
            interface_dict_buffer["mtu"]["observedAt"] = observed_at
        if child_node == "ifindex":
            interface_dict_buffer["ifindex"] = {}
            interface_dict_buffer["ifindex"]["type"] = "Property"
            interface_dict_buffer["ifindex"]["value"] = int(element_text)
            interface_dict_buffer["ifindex"]["observedAt"] = observed_at
        if child_node == "oper-state":
            interface_dict_buffer["operState"] = {}
            interface_dict_buffer["operState"]["type"] = "Property"
            interface_dict_buffer["operState"]["value"] = element_text
            interface_dict_buffer["operState"]["observedAt"] = observed_at
        if child_node == "oper-down-reason":
            interface_dict_buffer["operDownReason"] = {}
            interface_dict_buffer["operDownReason"]["type"] = "Property"
            interface_dict_buffer["operDownReason"]["value"] = element_text
            interface_dict_buffer["operDownReason"]["observedAt"] = observed_at
        if child_node == "last-change":
            interface_dict_buffer["lastChange"] = {}
            interface_dict_buffer["lastChange"]["type"] = "Property"
            interface_dict_buffer["lastChange"]["value"] = element_text
            interface_dict_buffer["lastChange"]["observedAt"] = observed_at
        if len(parent_path) - 1 == 0 or len(parent_path) - 1 == 1:
            interface_dict_buffer["linecard"] = {}
            interface_dict_buffer["linecard"]["type"] = "Relationship"
            interface_dict_buffer["linecard"]["object"] = "urn:ngsi-ld:Linecard:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
            interface_dict_buffer["linecard"]["observedAt"] = observed_at
        if len(parent_path) - 1 == 0 or len(parent_path) - 1 == 1:
            interface_dict_buffer["forwardingComplex"] = {}
            interface_dict_buffer["forwardingComplex"]["type"] = "Relationship"
            interface_dict_buffer["forwardingComplex"]["object"] = "urn:ngsi-ld:ForwardingComplex:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
            interface_dict_buffer["forwardingComplex"]["observedAt"] = observed_at
        if child_node == "phy-group-members":
            interface_dict_buffer["phyGroupMembers"] = {}
            interface_dict_buffer["phyGroupMembers"]["type"] = "Property"
            interface_dict_buffer["phyGroupMembers"]["value"] = element_text
            interface_dict_buffer["phyGroupMembers"]["observedAt"] = observed_at
        if parent_path[1] == "statistics":
            interface_statistics_dict_buffer = {}
            interface_statistics_dict_buffer["id"] = "urn:ngsi-ld:InterfaceStatistics:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
            interface_statistics_dict_buffer["type"] = "InterfaceStatistics"
            if len(parent_path) - 1 == 1 or len(parent_path) - 1 == 2:
                interface_statistics_dict_buffer["isPartOf"] = {}
                interface_statistics_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_statistics_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                interface_statistics_dict_buffer["isPartOf"]["observedAt"] = observed_at
                if child_node == "in-packets":
                    interface_statistics_dict_buffer["inPackets"] = {}
                    interface_statistics_dict_buffer["inPackets"]["type"] = "Property"
                    interface_statistics_dict_buffer["inPackets"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["inPackets"]["observedAt"] = observed_at
                if child_node == "in-octets":
                    interface_statistics_dict_buffer["inOctets"] = {}
                    interface_statistics_dict_buffer["inOctets"]["type"] = "Property"
                    interface_statistics_dict_buffer["inOctets"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["inOctets"]["observedAt"] = observed_at
                if child_node == "in-unicast-packets":
                    interface_statistics_dict_buffer["inUnicastPackets"] = {}
                    interface_statistics_dict_buffer["inUnicastPackets"]["type"] = "Property"
                    interface_statistics_dict_buffer["inUnicastPackets"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["inUnicastPackets"]["observedAt"] = observed_at
                if child_node == "in-broadcast-packets":
                    interface_statistics_dict_buffer["inBroadcastPackets"] = {}
                    interface_statistics_dict_buffer["inBroadcastPackets"]["type"] = "Property"
                    interface_statistics_dict_buffer["inBroadcastPackets"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["inBroadcastPackets"]["observedAt"] = observed_at
                if child_node == "in-multicast-packets":
                    interface_statistics_dict_buffer["inMulticastPackets"] = {}
                    interface_statistics_dict_buffer["inMulticastPackets"]["type"] = "Property"
                    interface_statistics_dict_buffer["inMulticastPackets"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["inMulticastPackets"]["observedAt"] = observed_at
                if child_node == "in-discarded-packets":
                    interface_statistics_dict_buffer["inDiscardedPackets"] = {}
                    interface_statistics_dict_buffer["inDiscardedPackets"]["type"] = "Property"
                    interface_statistics_dict_buffer["inDiscardedPackets"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["inDiscardedPackets"]["observedAt"] = observed_at
                if child_node == "in-error-packets":
                    interface_statistics_dict_buffer["inErrorPackets"] = {}
                    interface_statistics_dict_buffer["inErrorPackets"]["type"] = "Property"
                    interface_statistics_dict_buffer["inErrorPackets"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["inErrorPackets"]["observedAt"] = observed_at
                if child_node == "in-fcs-error-packets":
                    interface_statistics_dict_buffer["inFcsErrorPackets"] = {}
                    interface_statistics_dict_buffer["inFcsErrorPackets"]["type"] = "Property"
                    interface_statistics_dict_buffer["inFcsErrorPackets"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["inFcsErrorPackets"]["observedAt"] = observed_at
                if child_node == "out-packets":
                    interface_statistics_dict_buffer["outPackets"] = {}
                    interface_statistics_dict_buffer["outPackets"]["type"] = "Property"
                    interface_statistics_dict_buffer["outPackets"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["outPackets"]["observedAt"] = observed_at
                if child_node == "out-octets":
                    interface_statistics_dict_buffer["outOctets"] = {}
                    interface_statistics_dict_buffer["outOctets"]["type"] = "Property"
                    interface_statistics_dict_buffer["outOctets"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["outOctets"]["observedAt"] = observed_at
                if child_node == "out-mirror-octets":
                    interface_statistics_dict_buffer["outMirrorOctets"] = {}
                    interface_statistics_dict_buffer["outMirrorOctets"]["type"] = "Property"
                    interface_statistics_dict_buffer["outMirrorOctets"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["outMirrorOctets"]["observedAt"] = observed_at
                if child_node == "out-unicast-packets":
                    interface_statistics_dict_buffer["outUnicastPackets"] = {}
                    interface_statistics_dict_buffer["outUnicastPackets"]["type"] = "Property"
                    interface_statistics_dict_buffer["outUnicastPackets"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["outUnicastPackets"]["observedAt"] = observed_at
                if child_node == "out-broadcast-packets":
                    interface_statistics_dict_buffer["outBroadcastPackets"] = {}
                    interface_statistics_dict_buffer["outBroadcastPackets"]["type"] = "Property"
                    interface_statistics_dict_buffer["outBroadcastPackets"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["outBroadcastPackets"]["observedAt"] = observed_at
                if child_node == "out-multicast-packets":
                    interface_statistics_dict_buffer["outMulticastPackets"] = {}
                    interface_statistics_dict_buffer["outMulticastPackets"]["type"] = "Property"
                    interface_statistics_dict_buffer["outMulticastPackets"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["outMulticastPackets"]["observedAt"] = observed_at
                if child_node == "out-discarded-packets":
                    interface_statistics_dict_buffer["outDiscardedPackets"] = {}
                    interface_statistics_dict_buffer["outDiscardedPackets"]["type"] = "Property"
                    interface_statistics_dict_buffer["outDiscardedPackets"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["outDiscardedPackets"]["observedAt"] = observed_at
                if child_node == "out-error-packets":
                    interface_statistics_dict_buffer["outErrorPackets"] = {}
                    interface_statistics_dict_buffer["outErrorPackets"]["type"] = "Property"
                    interface_statistics_dict_buffer["outErrorPackets"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["outErrorPackets"]["observedAt"] = observed_at
                if child_node == "out-mirror-packets":
                    interface_statistics_dict_buffer["outMirrorPackets"] = {}
                    interface_statistics_dict_buffer["outMirrorPackets"]["type"] = "Property"
                    interface_statistics_dict_buffer["outMirrorPackets"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["outMirrorPackets"]["observedAt"] = observed_at
                if child_node == "carrier-transitions":
                    interface_statistics_dict_buffer["carrierTransitions"] = {}
                    interface_statistics_dict_buffer["carrierTransitions"]["type"] = "Property"
                    interface_statistics_dict_buffer["carrierTransitions"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["carrierTransitions"]["observedAt"] = observed_at
                if child_node == "last-clear":
                    interface_statistics_dict_buffer["lastClear"] = {}
                    interface_statistics_dict_buffer["lastClear"]["type"] = "Property"
                    interface_statistics_dict_buffer["lastClear"]["value"] = element_text
                    interface_statistics_dict_buffer["lastClear"]["observedAt"] = observed_at
                if len(parent_path) - 1 == 1:
                    dict_buffers.append(interface_statistics_dict_buffer)
        if parent_path[1] == "traffic-rate":
            interface_traffic_rate_dict_buffer = {}
            interface_traffic_rate_dict_buffer["id"] = "urn:ngsi-ld:InterfaceTrafficRate:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
            interface_traffic_rate_dict_buffer["type"] = "InterfaceTrafficRate"
            if len(parent_path) - 1 == 1 or len(parent_path) - 1 == 2:
                interface_traffic_rate_dict_buffer["isPartOf"] = {}
                interface_traffic_rate_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_traffic_rate_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                interface_traffic_rate_dict_buffer["isPartOf"]["observedAt"] = observed_at
                if child_node == "in-bps":
                    interface_traffic_rate_dict_buffer["inBps"] = {}
                    interface_traffic_rate_dict_buffer["inBps"]["type"] = "Property"
                    interface_traffic_rate_dict_buffer["inBps"]["value"] = int(element_text)
                    interface_traffic_rate_dict_buffer["inBps"]["observedAt"] = observed_at
                if child_node == "out-bps":
                    interface_traffic_rate_dict_buffer["outBps"] = {}
                    interface_traffic_rate_dict_buffer["outBps"]["type"] = "Property"
                    interface_traffic_rate_dict_buffer["outBps"]["value"] = int(element_text)
                    interface_traffic_rate_dict_buffer["outBps"]["observedAt"] = observed_at
                if len(parent_path) - 1 == 1:
                    dict_buffers.append(interface_traffic_rate_dict_buffer)
        if parent_path[1] == "adapter":
            interface_adapter_dict_buffer = {}
            interface_adapter_dict_buffer["id"] = "urn:ngsi-ld:InterfaceAdapter:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
            interface_adapter_dict_buffer["type"] = "InterfaceAdapter"
            if len(parent_path) - 1 == 1 or len(parent_path) - 1 == 2:
                interface_adapter_dict_buffer["isPartOf"] = {}
                interface_adapter_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_adapter_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                interface_adapter_dict_buffer["isPartOf"]["observedAt"] = observed_at
                if child_node == "model-number":
                    interface_adapter_dict_buffer["modelNumber"] = {}
                    interface_adapter_dict_buffer["modelNumber"]["type"] = "Property"
                    interface_adapter_dict_buffer["modelNumber"]["value"] = element_text
                    interface_adapter_dict_buffer["modelNumber"]["observedAt"] = observed_at
                if child_node == "type":
                    interface_adapter_dict_buffer["type"] = {}
                    interface_adapter_dict_buffer["type"]["type"] = "Property"
                    interface_adapter_dict_buffer["type"]["value"] = element_text
                    interface_adapter_dict_buffer["type"]["observedAt"] = observed_at
                if child_node == "vendor-manufacture-date":
                    interface_adapter_dict_buffer["vendorManufactureDate"] = {}
                    interface_adapter_dict_buffer["vendorManufactureDate"]["type"] = "Property"
                    interface_adapter_dict_buffer["vendorManufactureDate"]["value"] = element_text
                    interface_adapter_dict_buffer["vendorManufactureDate"]["observedAt"] = observed_at
                if child_node == "vendor-oui":
                    interface_adapter_dict_buffer["vendorOui"] = {}
                    interface_adapter_dict_buffer["vendorOui"]["type"] = "Property"
                    interface_adapter_dict_buffer["vendorOui"]["value"] = element_text
                    interface_adapter_dict_buffer["vendorOui"]["observedAt"] = observed_at
                if child_node == "vendor-part-number":
                    interface_adapter_dict_buffer["vendorPartNumber"] = {}
                    interface_adapter_dict_buffer["vendorPartNumber"]["type"] = "Property"
                    interface_adapter_dict_buffer["vendorPartNumber"]["value"] = element_text
                    interface_adapter_dict_buffer["vendorPartNumber"]["observedAt"] = observed_at
                if child_node == "vendor-serial-number":
                    interface_adapter_dict_buffer["vendorSerialNumber"] = {}
                    interface_adapter_dict_buffer["vendorSerialNumber"]["type"] = "Property"
                    interface_adapter_dict_buffer["vendorSerialNumber"]["value"] = element_text
                    interface_adapter_dict_buffer["vendorSerialNumber"]["observedAt"] = observed_at
                if len(parent_path) - 1 == 1:
                    dict_buffers.append(interface_adapter_dict_buffer)
        if parent_path[1] == "transceiver":
            interface_transceiver_dict_buffer = {}
            interface_transceiver_dict_buffer["id"] = "urn:ngsi-ld:InterfaceTransceiver:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
            interface_transceiver_dict_buffer["type"] = "InterfaceTransceiver"
            if len(parent_path) - 1 == 1 or len(parent_path) - 1 == 2:
                interface_transceiver_dict_buffer["isPartOf"] = {}
                interface_transceiver_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_transceiver_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                interface_transceiver_dict_buffer["isPartOf"]["observedAt"] = observed_at
                if child_node == "tx-laser":
                    interface_transceiver_dict_buffer["txLaser"] = {}
                    interface_transceiver_dict_buffer["txLaser"]["type"] = "Property"
                    interface_transceiver_dict_buffer["txLaser"]["value"] = eval(str(element_text).capitalize())
                    interface_transceiver_dict_buffer["txLaser"]["observedAt"] = observed_at
                if child_node == "oper-state":
                    interface_transceiver_dict_buffer["operState"] = {}
                    interface_transceiver_dict_buffer["operState"]["type"] = "Property"
                    interface_transceiver_dict_buffer["operState"]["value"] = element_text
                    interface_transceiver_dict_buffer["operState"]["observedAt"] = observed_at
                if child_node == "oper-down-reason":
                    interface_transceiver_dict_buffer["operDownReason"] = {}
                    interface_transceiver_dict_buffer["operDownReason"]["type"] = "Property"
                    interface_transceiver_dict_buffer["operDownReason"]["value"] = element_text
                    interface_transceiver_dict_buffer["operDownReason"]["observedAt"] = observed_at
                if child_node == "ddm-events":
                    interface_transceiver_dict_buffer["ddmEvents"] = {}
                    interface_transceiver_dict_buffer["ddmEvents"]["type"] = "Property"
                    interface_transceiver_dict_buffer["ddmEvents"]["value"] = eval(str(element_text).capitalize())
                    interface_transceiver_dict_buffer["ddmEvents"]["observedAt"] = observed_at
                if child_node == "forward-error-correction":
                    interface_transceiver_dict_buffer["forwardErrorCorrection"] = {}
                    interface_transceiver_dict_buffer["forwardErrorCorrection"]["type"] = "Property"
                    interface_transceiver_dict_buffer["forwardErrorCorrection"]["value"] = element_text
                    interface_transceiver_dict_buffer["forwardErrorCorrection"]["observedAt"] = observed_at
                if child_node == "form-factor":
                    interface_transceiver_dict_buffer["formFactor"] = {}
                    interface_transceiver_dict_buffer["formFactor"]["type"] = "Property"
                    interface_transceiver_dict_buffer["formFactor"]["value"] = element_text
                    interface_transceiver_dict_buffer["formFactor"]["observedAt"] = observed_at
                if child_node == "ethernet-pmd":
                    interface_transceiver_dict_buffer["ethernetPmd"] = {}
                    interface_transceiver_dict_buffer["ethernetPmd"]["type"] = "Property"
                    interface_transceiver_dict_buffer["ethernetPmd"]["value"] = element_text
                    interface_transceiver_dict_buffer["ethernetPmd"]["observedAt"] = observed_at
                if child_node == "connector-type":
                    interface_transceiver_dict_buffer["connectorType"] = {}
                    interface_transceiver_dict_buffer["connectorType"]["type"] = "Property"
                    interface_transceiver_dict_buffer["connectorType"]["value"] = element_text
                    interface_transceiver_dict_buffer["connectorType"]["observedAt"] = observed_at
                if child_node == "vendor":
                    interface_transceiver_dict_buffer["vendor"] = {}
                    interface_transceiver_dict_buffer["vendor"]["type"] = "Property"
                    interface_transceiver_dict_buffer["vendor"]["value"] = element_text
                    interface_transceiver_dict_buffer["vendor"]["observedAt"] = observed_at
                if child_node == "vendor-part-number":
                    interface_transceiver_dict_buffer["vendorPartNumber"] = {}
                    interface_transceiver_dict_buffer["vendorPartNumber"]["type"] = "Property"
                    interface_transceiver_dict_buffer["vendorPartNumber"]["value"] = element_text
                    interface_transceiver_dict_buffer["vendorPartNumber"]["observedAt"] = observed_at
                if child_node == "vendor-revision":
                    interface_transceiver_dict_buffer["vendorRevision"] = {}
                    interface_transceiver_dict_buffer["vendorRevision"]["type"] = "Property"
                    interface_transceiver_dict_buffer["vendorRevision"]["value"] = element_text
                    interface_transceiver_dict_buffer["vendorRevision"]["observedAt"] = observed_at
                if child_node == "vendor-lot-number":
                    interface_transceiver_dict_buffer["vendorLotNumber"] = {}
                    interface_transceiver_dict_buffer["vendorLotNumber"]["type"] = "Property"
                    interface_transceiver_dict_buffer["vendorLotNumber"]["value"] = element_text
                    interface_transceiver_dict_buffer["vendorLotNumber"]["observedAt"] = observed_at
                if child_node == "serial-number":
                    interface_transceiver_dict_buffer["serialNumber"] = {}
                    interface_transceiver_dict_buffer["serialNumber"]["type"] = "Property"
                    interface_transceiver_dict_buffer["serialNumber"]["value"] = element_text
                    interface_transceiver_dict_buffer["serialNumber"]["observedAt"] = observed_at
                if child_node == "date-code":
                    interface_transceiver_dict_buffer["dateCode"] = {}
                    interface_transceiver_dict_buffer["dateCode"]["type"] = "Property"
                    interface_transceiver_dict_buffer["dateCode"]["value"] = element_text
                    interface_transceiver_dict_buffer["dateCode"]["observedAt"] = observed_at
                if child_node == "fault-condition":
                    interface_transceiver_dict_buffer["faultCondition"] = {}
                    interface_transceiver_dict_buffer["faultCondition"]["type"] = "Property"
                    interface_transceiver_dict_buffer["faultCondition"]["value"] = eval(str(element_text).capitalize())
                    interface_transceiver_dict_buffer["faultCondition"]["observedAt"] = observed_at
                if child_node == "wavelength":
                    interface_transceiver_dict_buffer["wavelength"] = {}
                    interface_transceiver_dict_buffer["wavelength"]["type"] = "Property"
                    interface_transceiver_dict_buffer["wavelength"]["value"] = float(element_text)
                    interface_transceiver_dict_buffer["wavelength"]["observedAt"] = observed_at
                if parent_path[2] == "temperature":
                    interface_transceiver_temperature_dict_buffer = {}
                    interface_transceiver_temperature_dict_buffer["id"] = "urn:ngsi-ld:InterfaceTransceiverTemperature:" + ":".join(interface_transceiver_dict_buffer["id"].split(":")[3:])
                    interface_transceiver_temperature_dict_buffer["type"] = "InterfaceTransceiverTemperature"
                    if len(parent_path) - 1 == 2 or len(parent_path) - 1 == 3:
                        interface_transceiver_temperature_dict_buffer["isPartOf"] = {}
                        interface_transceiver_temperature_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_transceiver_temperature_dict_buffer["isPartOf"]["object"] = interface_transceiver_dict_buffer["id"]
                        interface_transceiver_temperature_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "latest-value":
                            interface_transceiver_temperature_dict_buffer["latestValue"] = {}
                            interface_transceiver_temperature_dict_buffer["latestValue"]["type"] = "Property"
                            interface_transceiver_temperature_dict_buffer["latestValue"]["value"] = int(element_text)
                            interface_transceiver_temperature_dict_buffer["latestValue"]["observedAt"] = observed_at
                        if child_node == "maximum":
                            interface_transceiver_temperature_dict_buffer["maximum"] = {}
                            interface_transceiver_temperature_dict_buffer["maximum"]["type"] = "Property"
                            interface_transceiver_temperature_dict_buffer["maximum"]["value"] = int(element_text)
                            interface_transceiver_temperature_dict_buffer["maximum"]["observedAt"] = observed_at
                        if child_node == "maximum-time":
                            interface_transceiver_temperature_dict_buffer["maximumTime"] = {}
                            interface_transceiver_temperature_dict_buffer["maximumTime"]["type"] = "Property"
                            interface_transceiver_temperature_dict_buffer["maximumTime"]["value"] = element_text
                            interface_transceiver_temperature_dict_buffer["maximumTime"]["observedAt"] = observed_at
                        if child_node == "high-alarm-condition":
                            interface_transceiver_temperature_dict_buffer["highAlarmCondition"] = {}
                            interface_transceiver_temperature_dict_buffer["highAlarmCondition"]["type"] = "Property"
                            interface_transceiver_temperature_dict_buffer["highAlarmCondition"]["value"] = eval(str(element_text).capitalize())
                            interface_transceiver_temperature_dict_buffer["highAlarmCondition"]["observedAt"] = observed_at
                        if child_node == "high-alarm-threshold":
                            interface_transceiver_temperature_dict_buffer["highAlarmThreshold"] = {}
                            interface_transceiver_temperature_dict_buffer["highAlarmThreshold"]["type"] = "Property"
                            interface_transceiver_temperature_dict_buffer["highAlarmThreshold"]["value"] = int(element_text)
                            interface_transceiver_temperature_dict_buffer["highAlarmThreshold"]["observedAt"] = observed_at
                        if child_node == "low-alarm-condition":
                            interface_transceiver_temperature_dict_buffer["lowAlarmCondition"] = {}
                            interface_transceiver_temperature_dict_buffer["lowAlarmCondition"]["type"] = "Property"
                            interface_transceiver_temperature_dict_buffer["lowAlarmCondition"]["value"] = eval(str(element_text).capitalize())
                            interface_transceiver_temperature_dict_buffer["lowAlarmCondition"]["observedAt"] = observed_at
                        if child_node == "low-alarm-threshold":
                            interface_transceiver_temperature_dict_buffer["lowAlarmThreshold"] = {}
                            interface_transceiver_temperature_dict_buffer["lowAlarmThreshold"]["type"] = "Property"
                            interface_transceiver_temperature_dict_buffer["lowAlarmThreshold"]["value"] = int(element_text)
                            interface_transceiver_temperature_dict_buffer["lowAlarmThreshold"]["observedAt"] = observed_at
                        if child_node == "high-warning-condition":
                            interface_transceiver_temperature_dict_buffer["highWarningCondition"] = {}
                            interface_transceiver_temperature_dict_buffer["highWarningCondition"]["type"] = "Property"
                            interface_transceiver_temperature_dict_buffer["highWarningCondition"]["value"] = eval(str(element_text).capitalize())
                            interface_transceiver_temperature_dict_buffer["highWarningCondition"]["observedAt"] = observed_at
                        if child_node == "high-warning-threshold":
                            interface_transceiver_temperature_dict_buffer["highWarningThreshold"] = {}
                            interface_transceiver_temperature_dict_buffer["highWarningThreshold"]["type"] = "Property"
                            interface_transceiver_temperature_dict_buffer["highWarningThreshold"]["value"] = int(element_text)
                            interface_transceiver_temperature_dict_buffer["highWarningThreshold"]["observedAt"] = observed_at
                        if child_node == "low-warning-condition":
                            interface_transceiver_temperature_dict_buffer["lowWarningCondition"] = {}
                            interface_transceiver_temperature_dict_buffer["lowWarningCondition"]["type"] = "Property"
                            interface_transceiver_temperature_dict_buffer["lowWarningCondition"]["value"] = eval(str(element_text).capitalize())
                            interface_transceiver_temperature_dict_buffer["lowWarningCondition"]["observedAt"] = observed_at
                        if child_node == "low-warning-threshold":
                            interface_transceiver_temperature_dict_buffer["lowWarningThreshold"] = {}
                            interface_transceiver_temperature_dict_buffer["lowWarningThreshold"]["type"] = "Property"
                            interface_transceiver_temperature_dict_buffer["lowWarningThreshold"]["value"] = int(element_text)
                            interface_transceiver_temperature_dict_buffer["lowWarningThreshold"]["observedAt"] = observed_at
                        if len(parent_path) - 1 == 2:
                            dict_buffers.append(interface_transceiver_temperature_dict_buffer)
                if parent_path[2] == "voltage":
                    interface_transceiver_voltage_dict_buffer = {}
                    interface_transceiver_voltage_dict_buffer["id"] = "urn:ngsi-ld:InterfaceTransceiverVoltage:" + ":".join(interface_transceiver_dict_buffer["id"].split(":")[3:])
                    interface_transceiver_voltage_dict_buffer["type"] = "InterfaceTransceiverVoltage"
                    if len(parent_path) - 1 == 2 or len(parent_path) - 1 == 3:
                        interface_transceiver_voltage_dict_buffer["isPartOf"] = {}
                        interface_transceiver_voltage_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_transceiver_voltage_dict_buffer["isPartOf"]["object"] = interface_transceiver_dict_buffer["id"]
                        interface_transceiver_voltage_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "latest-value":
                            interface_transceiver_voltage_dict_buffer["latestValue"] = {}
                            interface_transceiver_voltage_dict_buffer["latestValue"]["type"] = "Property"
                            interface_transceiver_voltage_dict_buffer["latestValue"]["value"] = float(element_text)
                            interface_transceiver_voltage_dict_buffer["latestValue"]["observedAt"] = observed_at
                        if child_node == "high-alarm-condition":
                            interface_transceiver_voltage_dict_buffer["highAlarmCondition"] = {}
                            interface_transceiver_voltage_dict_buffer["highAlarmCondition"]["type"] = "Property"
                            interface_transceiver_voltage_dict_buffer["highAlarmCondition"]["value"] = eval(str(element_text).capitalize())
                            interface_transceiver_voltage_dict_buffer["highAlarmCondition"]["observedAt"] = observed_at
                        if child_node == "high-alarm-threshold":
                            interface_transceiver_voltage_dict_buffer["highAlarmThreshold"] = {}
                            interface_transceiver_voltage_dict_buffer["highAlarmThreshold"]["type"] = "Property"
                            interface_transceiver_voltage_dict_buffer["highAlarmThreshold"]["value"] = float(element_text)
                            interface_transceiver_voltage_dict_buffer["highAlarmThreshold"]["observedAt"] = observed_at
                        if child_node == "low-alarm-condition":
                            interface_transceiver_voltage_dict_buffer["lowAlarmCondition"] = {}
                            interface_transceiver_voltage_dict_buffer["lowAlarmCondition"]["type"] = "Property"
                            interface_transceiver_voltage_dict_buffer["lowAlarmCondition"]["value"] = eval(str(element_text).capitalize())
                            interface_transceiver_voltage_dict_buffer["lowAlarmCondition"]["observedAt"] = observed_at
                        if child_node == "low-alarm-threshold":
                            interface_transceiver_voltage_dict_buffer["lowAlarmThreshold"] = {}
                            interface_transceiver_voltage_dict_buffer["lowAlarmThreshold"]["type"] = "Property"
                            interface_transceiver_voltage_dict_buffer["lowAlarmThreshold"]["value"] = float(element_text)
                            interface_transceiver_voltage_dict_buffer["lowAlarmThreshold"]["observedAt"] = observed_at
                        if child_node == "high-warning-condition":
                            interface_transceiver_voltage_dict_buffer["highWarningCondition"] = {}
                            interface_transceiver_voltage_dict_buffer["highWarningCondition"]["type"] = "Property"
                            interface_transceiver_voltage_dict_buffer["highWarningCondition"]["value"] = eval(str(element_text).capitalize())
                            interface_transceiver_voltage_dict_buffer["highWarningCondition"]["observedAt"] = observed_at
                        if child_node == "high-warning-threshold":
                            interface_transceiver_voltage_dict_buffer["highWarningThreshold"] = {}
                            interface_transceiver_voltage_dict_buffer["highWarningThreshold"]["type"] = "Property"
                            interface_transceiver_voltage_dict_buffer["highWarningThreshold"]["value"] = float(element_text)
                            interface_transceiver_voltage_dict_buffer["highWarningThreshold"]["observedAt"] = observed_at
                        if child_node == "low-warning-condition":
                            interface_transceiver_voltage_dict_buffer["lowWarningCondition"] = {}
                            interface_transceiver_voltage_dict_buffer["lowWarningCondition"]["type"] = "Property"
                            interface_transceiver_voltage_dict_buffer["lowWarningCondition"]["value"] = eval(str(element_text).capitalize())
                            interface_transceiver_voltage_dict_buffer["lowWarningCondition"]["observedAt"] = observed_at
                        if child_node == "low-warning-threshold":
                            interface_transceiver_voltage_dict_buffer["lowWarningThreshold"] = {}
                            interface_transceiver_voltage_dict_buffer["lowWarningThreshold"]["type"] = "Property"
                            interface_transceiver_voltage_dict_buffer["lowWarningThreshold"]["value"] = float(element_text)
                            interface_transceiver_voltage_dict_buffer["lowWarningThreshold"]["observedAt"] = observed_at
                        if len(parent_path) - 1 == 2:
                            dict_buffers.append(interface_transceiver_voltage_dict_buffer)
                if parent_path[2] == "channel":
                    interface_transceiver_channel_dict_buffer = {}
                    if "interface_transceiver_channel_index" in iteration_keys:
                        interface_transceiver_channel_dict_buffer["id"] = "urn:ngsi-ld:InterfaceTransceiverChannel:" + source + ":" + iteration_keys.get("interface_transceiver_channel_index")
                    interface_transceiver_channel_dict_buffer["type"] = "InterfaceTransceiverChannel"
                    if len(parent_path) - 1 == 2 or len(parent_path) - 1 == 3:
                        interface_transceiver_channel_dict_buffer["isPartOf"] = {}
                        interface_transceiver_channel_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_transceiver_channel_dict_buffer["isPartOf"]["object"] = interface_transceiver_dict_buffer["id"]
                        interface_transceiver_channel_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "index":
                            if "." + str(element_text) not in interface_transceiver_channel_dict_buffer["id"].split(":")[-1]:
                                interface_transceiver_channel_dict_buffer["id"] = interface_transceiver_channel_dict_buffer["id"] + "." + str(element_text)
                            interface_transceiver_channel_dict_buffer["index"] = {}
                            interface_transceiver_channel_dict_buffer["index"]["type"] = "Property"
                            interface_transceiver_channel_dict_buffer["index"]["value"] = int(element_text)
                            interface_transceiver_channel_dict_buffer["index"]["observedAt"] = observed_at
                        if child_node == "wavelength":
                            interface_transceiver_channel_dict_buffer["wavelength"] = {}
                            interface_transceiver_channel_dict_buffer["wavelength"]["type"] = "Property"
                            interface_transceiver_channel_dict_buffer["wavelength"]["value"] = float(element_text)
                            interface_transceiver_channel_dict_buffer["wavelength"]["observedAt"] = observed_at
                        if len(parent_path) - 1 == 2:
                            dict_buffers.append(interface_transceiver_channel_dict_buffer)
                if len(parent_path) - 1 == 1:
                    dict_buffers.append(interface_transceiver_dict_buffer)
        if parent_path[1] == "ethernet":
            interface_ethernet_dict_buffer = {}
            interface_ethernet_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernet:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
            interface_ethernet_dict_buffer["type"] = "InterfaceEthernet"
            if len(parent_path) - 1 == 1 or len(parent_path) - 1 == 2:
                interface_ethernet_dict_buffer["isPartOf"] = {}
                interface_ethernet_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_ethernet_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                interface_ethernet_dict_buffer["isPartOf"]["observedAt"] = observed_at
                if len(parent_path) - 1 == 1 or len(parent_path) - 1 == 2:
                    if interface_ethernet_dict_buffer["id"].split(":")[-1] != element_text:
                        interface_ethernet_dict_buffer["id"] = interface_ethernet_dict_buffer["id"] + ":" + element_text
                    interface_ethernet_dict_buffer["aggregateId"] = {}
                    interface_ethernet_dict_buffer["aggregateId"]["type"] = "Relationship"
                    interface_ethernet_dict_buffer["aggregateId"]["object"] = "urn:ngsi-ld:Interface:" + ":".join(interface_ethernet_dict_buffer["id"].split(":")[3:])
                    interface_ethernet_dict_buffer["aggregateId"]["observedAt"] = observed_at
                if child_node == "forwarding-viable":
                    interface_ethernet_dict_buffer["forwardingViable"] = {}
                    interface_ethernet_dict_buffer["forwardingViable"]["type"] = "Property"
                    interface_ethernet_dict_buffer["forwardingViable"]["value"] = eval(str(element_text).capitalize())
                    interface_ethernet_dict_buffer["forwardingViable"]["observedAt"] = observed_at
                if child_node == "auto-negotiate":
                    interface_ethernet_dict_buffer["autoNegotiate"] = {}
                    interface_ethernet_dict_buffer["autoNegotiate"]["type"] = "Property"
                    interface_ethernet_dict_buffer["autoNegotiate"]["value"] = eval(str(element_text).capitalize())
                    interface_ethernet_dict_buffer["autoNegotiate"]["observedAt"] = observed_at
                if child_node == "duplex-mode":
                    interface_ethernet_dict_buffer["duplexMode"] = {}
                    interface_ethernet_dict_buffer["duplexMode"]["type"] = "Property"
                    interface_ethernet_dict_buffer["duplexMode"]["value"] = element_text
                    interface_ethernet_dict_buffer["duplexMode"]["observedAt"] = observed_at
                if child_node == "dac-link-training":
                    interface_ethernet_dict_buffer["dacLinkTraining"] = {}
                    interface_ethernet_dict_buffer["dacLinkTraining"]["type"] = "Property"
                    interface_ethernet_dict_buffer["dacLinkTraining"]["value"] = eval(str(element_text).capitalize())
                    interface_ethernet_dict_buffer["dacLinkTraining"]["observedAt"] = observed_at
                if parent_path[2] == "flow-control":
                    interface_ethernet_flow_control_dict_buffer = {}
                    interface_ethernet_flow_control_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetFlowControl:" + ":".join(interface_ethernet_dict_buffer["id"].split(":")[3:])
                    interface_ethernet_flow_control_dict_buffer["type"] = "InterfaceEthernetFlowControl"
                    if len(parent_path) - 1 == 2 or len(parent_path) - 1 == 3:
                        interface_ethernet_flow_control_dict_buffer["isPartOf"] = {}
                        interface_ethernet_flow_control_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_ethernet_flow_control_dict_buffer["isPartOf"]["object"] = interface_ethernet_dict_buffer["id"]
                        interface_ethernet_flow_control_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "receive":
                            interface_ethernet_flow_control_dict_buffer["receive"] = {}
                            interface_ethernet_flow_control_dict_buffer["receive"]["type"] = "Property"
                            interface_ethernet_flow_control_dict_buffer["receive"]["value"] = eval(str(element_text).capitalize())
                            interface_ethernet_flow_control_dict_buffer["receive"]["observedAt"] = observed_at
                        if child_node == "transmit":
                            interface_ethernet_flow_control_dict_buffer["transmit"] = {}
                            interface_ethernet_flow_control_dict_buffer["transmit"]["type"] = "Property"
                            interface_ethernet_flow_control_dict_buffer["transmit"]["value"] = eval(str(element_text).capitalize())
                            interface_ethernet_flow_control_dict_buffer["transmit"]["observedAt"] = observed_at
                        if len(parent_path) - 1 == 2:
                            dict_buffers.append(interface_ethernet_flow_control_dict_buffer)
                if child_node == "lacp-port-priority":
                    interface_ethernet_dict_buffer["lacpPortPriority"] = {}
                    interface_ethernet_dict_buffer["lacpPortPriority"]["type"] = "Property"
                    interface_ethernet_dict_buffer["lacpPortPriority"]["value"] = int(element_text)
                    interface_ethernet_dict_buffer["lacpPortPriority"]["observedAt"] = observed_at
                if child_node == "port-speed":
                    interface_ethernet_dict_buffer["portSpeed"] = {}
                    interface_ethernet_dict_buffer["portSpeed"]["type"] = "Property"
                    interface_ethernet_dict_buffer["portSpeed"]["value"] = element_text
                    interface_ethernet_dict_buffer["portSpeed"]["observedAt"] = observed_at
                if child_node == "hw-mac-address":
                    interface_ethernet_dict_buffer["hwMacAddress"] = {}
                    interface_ethernet_dict_buffer["hwMacAddress"]["type"] = "Property"
                    interface_ethernet_dict_buffer["hwMacAddress"]["value"] = element_text
                    interface_ethernet_dict_buffer["hwMacAddress"]["observedAt"] = observed_at
                if child_node == "mac-address":
                    interface_ethernet_dict_buffer["macAddress"] = {}
                    interface_ethernet_dict_buffer["macAddress"]["type"] = "Property"
                    interface_ethernet_dict_buffer["macAddress"]["value"] = element_text
                    interface_ethernet_dict_buffer["macAddress"]["observedAt"] = observed_at
                if child_node == "physical-medium":
                    interface_ethernet_dict_buffer["physicalMedium"] = {}
                    interface_ethernet_dict_buffer["physicalMedium"]["type"] = "Property"
                    interface_ethernet_dict_buffer["physicalMedium"]["value"] = element_text
                    interface_ethernet_dict_buffer["physicalMedium"]["observedAt"] = observed_at
                if child_node == "ptp-asymmetry":
                    interface_ethernet_dict_buffer["ptpAsymmetry"] = {}
                    interface_ethernet_dict_buffer["ptpAsymmetry"]["type"] = "Property"
                    interface_ethernet_dict_buffer["ptpAsymmetry"]["value"] = int(element_text)
                    interface_ethernet_dict_buffer["ptpAsymmetry"]["observedAt"] = observed_at
                if child_node == "standby-signaling":
                    interface_ethernet_dict_buffer["standbySignaling"] = {}
                    interface_ethernet_dict_buffer["standbySignaling"]["type"] = "Property"
                    interface_ethernet_dict_buffer["standbySignaling"]["value"] = element_text
                    interface_ethernet_dict_buffer["standbySignaling"]["observedAt"] = observed_at
                if child_node == "reload-delay":
                    interface_ethernet_dict_buffer["reloadDelay"] = {}
                    interface_ethernet_dict_buffer["reloadDelay"]["type"] = "Property"
                    interface_ethernet_dict_buffer["reloadDelay"]["value"] = int(element_text)
                    interface_ethernet_dict_buffer["reloadDelay"]["observedAt"] = observed_at
                if child_node == "reload-delay-expires":
                    interface_ethernet_dict_buffer["reloadDelayExpires"] = {}
                    interface_ethernet_dict_buffer["reloadDelayExpires"]["type"] = "Property"
                    interface_ethernet_dict_buffer["reloadDelayExpires"]["value"] = element_text
                    interface_ethernet_dict_buffer["reloadDelayExpires"]["observedAt"] = observed_at
                if parent_path[2] == "hold-time":
                    interface_ethernet_hold_time_dict_buffer = {}
                    interface_ethernet_hold_time_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetHoldTime:" + ":".join(interface_ethernet_dict_buffer["id"].split(":")[3:])
                    interface_ethernet_hold_time_dict_buffer["type"] = "InterfaceEthernetHoldTime"
                    if len(parent_path) - 1 == 2 or len(parent_path) - 1 == 3:
                        interface_ethernet_hold_time_dict_buffer["isPartOf"] = {}
                        interface_ethernet_hold_time_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_ethernet_hold_time_dict_buffer["isPartOf"]["object"] = interface_ethernet_dict_buffer["id"]
                        interface_ethernet_hold_time_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "up":
                            interface_ethernet_hold_time_dict_buffer["up"] = {}
                            interface_ethernet_hold_time_dict_buffer["up"]["type"] = "Property"
                            interface_ethernet_hold_time_dict_buffer["up"]["value"] = int(element_text)
                            interface_ethernet_hold_time_dict_buffer["up"]["observedAt"] = observed_at
                        if child_node == "up-expires":
                            interface_ethernet_hold_time_dict_buffer["upExpires"] = {}
                            interface_ethernet_hold_time_dict_buffer["upExpires"]["type"] = "Property"
                            interface_ethernet_hold_time_dict_buffer["upExpires"]["value"] = element_text
                            interface_ethernet_hold_time_dict_buffer["upExpires"]["observedAt"] = observed_at
                        if child_node == "down":
                            interface_ethernet_hold_time_dict_buffer["down"] = {}
                            interface_ethernet_hold_time_dict_buffer["down"]["type"] = "Property"
                            interface_ethernet_hold_time_dict_buffer["down"]["value"] = int(element_text)
                            interface_ethernet_hold_time_dict_buffer["down"]["observedAt"] = observed_at
                        if child_node == "down-expires":
                            interface_ethernet_hold_time_dict_buffer["downExpires"] = {}
                            interface_ethernet_hold_time_dict_buffer["downExpires"]["type"] = "Property"
                            interface_ethernet_hold_time_dict_buffer["downExpires"]["value"] = element_text
                            interface_ethernet_hold_time_dict_buffer["downExpires"]["observedAt"] = observed_at
                        if len(parent_path) - 1 == 2:
                            dict_buffers.append(interface_ethernet_hold_time_dict_buffer)
                if parent_path[2] == "crc-monitor":
                    interface_ethernet_crc_monitor_dict_buffer = {}
                    interface_ethernet_crc_monitor_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetCrcMonitor:" + ":".join(interface_ethernet_dict_buffer["id"].split(":")[3:])
                    interface_ethernet_crc_monitor_dict_buffer["type"] = "InterfaceEthernetCrcMonitor"
                    if len(parent_path) - 1 == 2 or len(parent_path) - 1 == 3:
                        interface_ethernet_crc_monitor_dict_buffer["isPartOf"] = {}
                        interface_ethernet_crc_monitor_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_ethernet_crc_monitor_dict_buffer["isPartOf"]["object"] = interface_ethernet_dict_buffer["id"]
                        interface_ethernet_crc_monitor_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "admin-state":
                            interface_ethernet_crc_monitor_dict_buffer["adminState"] = {}
                            interface_ethernet_crc_monitor_dict_buffer["adminState"]["type"] = "Property"
                            interface_ethernet_crc_monitor_dict_buffer["adminState"]["value"] = element_text
                            interface_ethernet_crc_monitor_dict_buffer["adminState"]["observedAt"] = observed_at
                        if child_node == "window-size":
                            interface_ethernet_crc_monitor_dict_buffer["windowSize"] = {}
                            interface_ethernet_crc_monitor_dict_buffer["windowSize"]["type"] = "Property"
                            interface_ethernet_crc_monitor_dict_buffer["windowSize"]["value"] = int(element_text)
                            interface_ethernet_crc_monitor_dict_buffer["windowSize"]["observedAt"] = observed_at
                        if parent_path[3] == "signal-degrade":
                            interface_ethernet_crc_monitor_signal_degrade_dict_buffer = {}
                            interface_ethernet_crc_monitor_signal_degrade_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetCrcMonitorSignalDegrade:" + ":".join(interface_ethernet_crc_monitor_dict_buffer["id"].split(":")[3:])
                            interface_ethernet_crc_monitor_signal_degrade_dict_buffer["type"] = "InterfaceEthernetCrcMonitorSignalDegrade"
                            if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                                interface_ethernet_crc_monitor_signal_degrade_dict_buffer["isPartOf"] = {}
                                interface_ethernet_crc_monitor_signal_degrade_dict_buffer["isPartOf"]["type"] = "Relationship"
                                interface_ethernet_crc_monitor_signal_degrade_dict_buffer["isPartOf"]["object"] = interface_ethernet_crc_monitor_dict_buffer["id"]
                                interface_ethernet_crc_monitor_signal_degrade_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                if child_node == "exponent":
                                    interface_ethernet_crc_monitor_signal_degrade_dict_buffer["exponent"] = {}
                                    interface_ethernet_crc_monitor_signal_degrade_dict_buffer["exponent"]["type"] = "Property"
                                    interface_ethernet_crc_monitor_signal_degrade_dict_buffer["exponent"]["value"] = int(element_text)
                                    interface_ethernet_crc_monitor_signal_degrade_dict_buffer["exponent"]["observedAt"] = observed_at
                                if child_node == "multiplier":
                                    interface_ethernet_crc_monitor_signal_degrade_dict_buffer["multiplier"] = {}
                                    interface_ethernet_crc_monitor_signal_degrade_dict_buffer["multiplier"]["type"] = "Property"
                                    interface_ethernet_crc_monitor_signal_degrade_dict_buffer["multiplier"]["value"] = int(element_text)
                                    interface_ethernet_crc_monitor_signal_degrade_dict_buffer["multiplier"]["observedAt"] = observed_at
                                if len(parent_path) - 1 == 3:
                                    dict_buffers.append(interface_ethernet_crc_monitor_signal_degrade_dict_buffer)
                        if parent_path[3] == "signal-failure":
                            interface_ethernet_crc_monitor_signal_failure_dict_buffer = {}
                            interface_ethernet_crc_monitor_signal_failure_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetCrcMonitorSignalFailure:" + ":".join(interface_ethernet_crc_monitor_dict_buffer["id"].split(":")[3:])
                            interface_ethernet_crc_monitor_signal_failure_dict_buffer["type"] = "InterfaceEthernetCrcMonitorSignalFailure"
                            if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                                interface_ethernet_crc_monitor_signal_failure_dict_buffer["isPartOf"] = {}
                                interface_ethernet_crc_monitor_signal_failure_dict_buffer["isPartOf"]["type"] = "Relationship"
                                interface_ethernet_crc_monitor_signal_failure_dict_buffer["isPartOf"]["object"] = interface_ethernet_crc_monitor_dict_buffer["id"]
                                interface_ethernet_crc_monitor_signal_failure_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                if child_node == "exponent":
                                    interface_ethernet_crc_monitor_signal_failure_dict_buffer["exponent"] = {}
                                    interface_ethernet_crc_monitor_signal_failure_dict_buffer["exponent"]["type"] = "Property"
                                    interface_ethernet_crc_monitor_signal_failure_dict_buffer["exponent"]["value"] = int(element_text)
                                    interface_ethernet_crc_monitor_signal_failure_dict_buffer["exponent"]["observedAt"] = observed_at
                                if child_node == "multiplier":
                                    interface_ethernet_crc_monitor_signal_failure_dict_buffer["multiplier"] = {}
                                    interface_ethernet_crc_monitor_signal_failure_dict_buffer["multiplier"]["type"] = "Property"
                                    interface_ethernet_crc_monitor_signal_failure_dict_buffer["multiplier"]["value"] = int(element_text)
                                    interface_ethernet_crc_monitor_signal_failure_dict_buffer["multiplier"]["observedAt"] = observed_at
                                if len(parent_path) - 1 == 3:
                                    dict_buffers.append(interface_ethernet_crc_monitor_signal_failure_dict_buffer)
                        if child_node == "current-alarms":
                            interface_ethernet_crc_monitor_dict_buffer["currentAlarms"] = {}
                            interface_ethernet_crc_monitor_dict_buffer["currentAlarms"]["type"] = "Property"
                            interface_ethernet_crc_monitor_dict_buffer["currentAlarms"]["value"] = element_text
                            interface_ethernet_crc_monitor_dict_buffer["currentAlarms"]["observedAt"] = observed_at
                        if len(parent_path) - 1 == 2:
                            dict_buffers.append(interface_ethernet_crc_monitor_dict_buffer)
                if parent_path[2] == "symbol-monitor":
                    interface_ethernet_symbol_monitor_dict_buffer = {}
                    interface_ethernet_symbol_monitor_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetSymbolMonitor:" + ":".join(interface_ethernet_dict_buffer["id"].split(":")[3:])
                    interface_ethernet_symbol_monitor_dict_buffer["type"] = "InterfaceEthernetSymbolMonitor"
                    if len(parent_path) - 1 == 2 or len(parent_path) - 1 == 3:
                        interface_ethernet_symbol_monitor_dict_buffer["isPartOf"] = {}
                        interface_ethernet_symbol_monitor_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_ethernet_symbol_monitor_dict_buffer["isPartOf"]["object"] = interface_ethernet_dict_buffer["id"]
                        interface_ethernet_symbol_monitor_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "admin-state":
                            interface_ethernet_symbol_monitor_dict_buffer["adminState"] = {}
                            interface_ethernet_symbol_monitor_dict_buffer["adminState"]["type"] = "Property"
                            interface_ethernet_symbol_monitor_dict_buffer["adminState"]["value"] = element_text
                            interface_ethernet_symbol_monitor_dict_buffer["adminState"]["observedAt"] = observed_at
                        if child_node == "window-size":
                            interface_ethernet_symbol_monitor_dict_buffer["windowSize"] = {}
                            interface_ethernet_symbol_monitor_dict_buffer["windowSize"]["type"] = "Property"
                            interface_ethernet_symbol_monitor_dict_buffer["windowSize"]["value"] = int(element_text)
                            interface_ethernet_symbol_monitor_dict_buffer["windowSize"]["observedAt"] = observed_at
                        if parent_path[3] == "signal-degrade":
                            interface_ethernet_symbol_monitor_signal_degrade_dict_buffer = {}
                            interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetSymbolMonitorSignalDegrade:" + ":".join(interface_ethernet_symbol_monitor_dict_buffer["id"].split(":")[3:])
                            interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["type"] = "InterfaceEthernetSymbolMonitorSignalDegrade"
                            if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                                interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["isPartOf"] = {}
                                interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["isPartOf"]["type"] = "Relationship"
                                interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["isPartOf"]["object"] = interface_ethernet_symbol_monitor_dict_buffer["id"]
                                interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                if child_node == "exponent":
                                    interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["exponent"] = {}
                                    interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["exponent"]["type"] = "Property"
                                    interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["exponent"]["value"] = int(element_text)
                                    interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["exponent"]["observedAt"] = observed_at
                                if child_node == "multiplier":
                                    interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["multiplier"] = {}
                                    interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["multiplier"]["type"] = "Property"
                                    interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["multiplier"]["value"] = int(element_text)
                                    interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["multiplier"]["observedAt"] = observed_at
                                if len(parent_path) - 1 == 3:
                                    dict_buffers.append(interface_ethernet_symbol_monitor_signal_degrade_dict_buffer)
                        if parent_path[3] == "signal-failure":
                            interface_ethernet_symbol_monitor_signal_failure_dict_buffer = {}
                            interface_ethernet_symbol_monitor_signal_failure_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetSymbolMonitorSignalFailure:" + ":".join(interface_ethernet_symbol_monitor_dict_buffer["id"].split(":")[3:])
                            interface_ethernet_symbol_monitor_signal_failure_dict_buffer["type"] = "InterfaceEthernetSymbolMonitorSignalFailure"
                            if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                                interface_ethernet_symbol_monitor_signal_failure_dict_buffer["isPartOf"] = {}
                                interface_ethernet_symbol_monitor_signal_failure_dict_buffer["isPartOf"]["type"] = "Relationship"
                                interface_ethernet_symbol_monitor_signal_failure_dict_buffer["isPartOf"]["object"] = interface_ethernet_symbol_monitor_dict_buffer["id"]
                                interface_ethernet_symbol_monitor_signal_failure_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                if child_node == "exponent":
                                    interface_ethernet_symbol_monitor_signal_failure_dict_buffer["exponent"] = {}
                                    interface_ethernet_symbol_monitor_signal_failure_dict_buffer["exponent"]["type"] = "Property"
                                    interface_ethernet_symbol_monitor_signal_failure_dict_buffer["exponent"]["value"] = int(element_text)
                                    interface_ethernet_symbol_monitor_signal_failure_dict_buffer["exponent"]["observedAt"] = observed_at
                                if child_node == "multiplier":
                                    interface_ethernet_symbol_monitor_signal_failure_dict_buffer["multiplier"] = {}
                                    interface_ethernet_symbol_monitor_signal_failure_dict_buffer["multiplier"]["type"] = "Property"
                                    interface_ethernet_symbol_monitor_signal_failure_dict_buffer["multiplier"]["value"] = int(element_text)
                                    interface_ethernet_symbol_monitor_signal_failure_dict_buffer["multiplier"]["observedAt"] = observed_at
                                if len(parent_path) - 1 == 3:
                                    dict_buffers.append(interface_ethernet_symbol_monitor_signal_failure_dict_buffer)
                        if child_node == "current-alarms":
                            interface_ethernet_symbol_monitor_dict_buffer["currentAlarms"] = {}
                            interface_ethernet_symbol_monitor_dict_buffer["currentAlarms"]["type"] = "Property"
                            interface_ethernet_symbol_monitor_dict_buffer["currentAlarms"]["value"] = element_text
                            interface_ethernet_symbol_monitor_dict_buffer["currentAlarms"]["observedAt"] = observed_at
                        if len(parent_path) - 1 == 2:
                            dict_buffers.append(interface_ethernet_symbol_monitor_dict_buffer)
                if parent_path[2] == "storm-control":
                    interface_ethernet_storm_control_dict_buffer = {}
                    interface_ethernet_storm_control_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetStormControl:" + ":".join(interface_ethernet_dict_buffer["id"].split(":")[3:])
                    interface_ethernet_storm_control_dict_buffer["type"] = "InterfaceEthernetStormControl"
                    if len(parent_path) - 1 == 2 or len(parent_path) - 1 == 3:
                        interface_ethernet_storm_control_dict_buffer["isPartOf"] = {}
                        interface_ethernet_storm_control_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_ethernet_storm_control_dict_buffer["isPartOf"]["object"] = interface_ethernet_dict_buffer["id"]
                        interface_ethernet_storm_control_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "units":
                            interface_ethernet_storm_control_dict_buffer["units"] = {}
                            interface_ethernet_storm_control_dict_buffer["units"]["type"] = "Property"
                            interface_ethernet_storm_control_dict_buffer["units"]["value"] = element_text
                            interface_ethernet_storm_control_dict_buffer["units"]["observedAt"] = observed_at
                        if child_node == "broadcast-rate":
                            interface_ethernet_storm_control_dict_buffer["broadcastRate"] = {}
                            interface_ethernet_storm_control_dict_buffer["broadcastRate"]["type"] = "Property"
                            interface_ethernet_storm_control_dict_buffer["broadcastRate"]["value"] = int(element_text)
                            interface_ethernet_storm_control_dict_buffer["broadcastRate"]["observedAt"] = observed_at
                        if child_node == "multicast-rate":
                            interface_ethernet_storm_control_dict_buffer["multicastRate"] = {}
                            interface_ethernet_storm_control_dict_buffer["multicastRate"]["type"] = "Property"
                            interface_ethernet_storm_control_dict_buffer["multicastRate"]["value"] = int(element_text)
                            interface_ethernet_storm_control_dict_buffer["multicastRate"]["observedAt"] = observed_at
                        if child_node == "unknown-unicast-rate":
                            interface_ethernet_storm_control_dict_buffer["unknownUnicastRate"] = {}
                            interface_ethernet_storm_control_dict_buffer["unknownUnicastRate"]["type"] = "Property"
                            interface_ethernet_storm_control_dict_buffer["unknownUnicastRate"]["value"] = int(element_text)
                            interface_ethernet_storm_control_dict_buffer["unknownUnicastRate"]["observedAt"] = observed_at
                        if child_node == "operational-broadcast-rate":
                            interface_ethernet_storm_control_dict_buffer["operationalBroadcastRate"] = {}
                            interface_ethernet_storm_control_dict_buffer["operationalBroadcastRate"]["type"] = "Property"
                            interface_ethernet_storm_control_dict_buffer["operationalBroadcastRate"]["value"] = int(element_text)
                            interface_ethernet_storm_control_dict_buffer["operationalBroadcastRate"]["observedAt"] = observed_at
                        if child_node == "operational-multicast-rate":
                            interface_ethernet_storm_control_dict_buffer["operationalMulticastRate"] = {}
                            interface_ethernet_storm_control_dict_buffer["operationalMulticastRate"]["type"] = "Property"
                            interface_ethernet_storm_control_dict_buffer["operationalMulticastRate"]["value"] = int(element_text)
                            interface_ethernet_storm_control_dict_buffer["operationalMulticastRate"]["observedAt"] = observed_at
                        if child_node == "operational-unknown-unicast-rate":
                            interface_ethernet_storm_control_dict_buffer["operationalUnknownUnicastRate"] = {}
                            interface_ethernet_storm_control_dict_buffer["operationalUnknownUnicastRate"]["type"] = "Property"
                            interface_ethernet_storm_control_dict_buffer["operationalUnknownUnicastRate"]["value"] = int(element_text)
                            interface_ethernet_storm_control_dict_buffer["operationalUnknownUnicastRate"]["observedAt"] = observed_at
                        if len(parent_path) - 1 == 2:
                            dict_buffers.append(interface_ethernet_storm_control_dict_buffer)
                if parent_path[2] == "synce":
                    if parent_path[3] == "ssm":
                        interface_ethernet_ssm_dict_buffer = {}
                        interface_ethernet_ssm_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetSynceSsm:" + ":".join(interface_ethernet_dict_buffer["id"].split(":")[3:])
                        interface_ethernet_ssm_dict_buffer["type"] = "InterfaceEthernetSynceSsm"
                        if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                            interface_ethernet_ssm_dict_buffer["isPartOf"] = {}
                            interface_ethernet_ssm_dict_buffer["isPartOf"]["type"] = "Relationship"
                            interface_ethernet_ssm_dict_buffer["isPartOf"]["object"] = interface_ethernet_dict_buffer["id"]
                            interface_ethernet_ssm_dict_buffer["isPartOf"]["observedAt"] = observed_at
                            if child_node == "admin-state":
                                interface_ethernet_ssm_dict_buffer["adminState"] = {}
                                interface_ethernet_ssm_dict_buffer["adminState"]["type"] = "Property"
                                interface_ethernet_ssm_dict_buffer["adminState"]["value"] = element_text
                                interface_ethernet_ssm_dict_buffer["adminState"]["observedAt"] = observed_at
                            if len(parent_path) - 1 == 3:
                                dict_buffers.append(interface_ethernet_ssm_dict_buffer)
                if parent_path[2] == "statistics":
                    interface_ethernet_statistics_dict_buffer = {}
                    interface_ethernet_statistics_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetStatistics:" + ":".join(interface_ethernet_dict_buffer["id"].split(":")[3:])
                    interface_ethernet_statistics_dict_buffer["type"] = "InterfaceEthernetStatistics"
                    if len(parent_path) - 1 == 2 or len(parent_path) - 1 == 3:
                        interface_ethernet_statistics_dict_buffer["isPartOf"] = {}
                        interface_ethernet_statistics_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_ethernet_statistics_dict_buffer["isPartOf"]["object"] = interface_ethernet_dict_buffer["id"]
                        interface_ethernet_statistics_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "in-mac-pause-frames":
                            interface_ethernet_statistics_dict_buffer["inMacPauseFrames"] = {}
                            interface_ethernet_statistics_dict_buffer["inMacPauseFrames"]["type"] = "Property"
                            interface_ethernet_statistics_dict_buffer["inMacPauseFrames"]["value"] = int(element_text)
                            interface_ethernet_statistics_dict_buffer["inMacPauseFrames"]["observedAt"] = observed_at
                        if child_node == "in-oversize-frames":
                            interface_ethernet_statistics_dict_buffer["inOversizeFrames"] = {}
                            interface_ethernet_statistics_dict_buffer["inOversizeFrames"]["type"] = "Property"
                            interface_ethernet_statistics_dict_buffer["inOversizeFrames"]["value"] = int(element_text)
                            interface_ethernet_statistics_dict_buffer["inOversizeFrames"]["observedAt"] = observed_at
                        if child_node == "in-jabber-frames":
                            interface_ethernet_statistics_dict_buffer["inJabberFrames"] = {}
                            interface_ethernet_statistics_dict_buffer["inJabberFrames"]["type"] = "Property"
                            interface_ethernet_statistics_dict_buffer["inJabberFrames"]["value"] = int(element_text)
                            interface_ethernet_statistics_dict_buffer["inJabberFrames"]["observedAt"] = observed_at
                        if child_node == "in-fragment-frames":
                            interface_ethernet_statistics_dict_buffer["inFragmentFrames"] = {}
                            interface_ethernet_statistics_dict_buffer["inFragmentFrames"]["type"] = "Property"
                            interface_ethernet_statistics_dict_buffer["inFragmentFrames"]["value"] = int(element_text)
                            interface_ethernet_statistics_dict_buffer["inFragmentFrames"]["observedAt"] = observed_at
                        if child_node == "in-crc-error-frames":
                            interface_ethernet_statistics_dict_buffer["inCrcErrorFrames"] = {}
                            interface_ethernet_statistics_dict_buffer["inCrcErrorFrames"]["type"] = "Property"
                            interface_ethernet_statistics_dict_buffer["inCrcErrorFrames"]["value"] = int(element_text)
                            interface_ethernet_statistics_dict_buffer["inCrcErrorFrames"]["observedAt"] = observed_at
                        if child_node == "out-mac-pause-frames":
                            interface_ethernet_statistics_dict_buffer["outMacPauseFrames"] = {}
                            interface_ethernet_statistics_dict_buffer["outMacPauseFrames"]["type"] = "Property"
                            interface_ethernet_statistics_dict_buffer["outMacPauseFrames"]["value"] = int(element_text)
                            interface_ethernet_statistics_dict_buffer["outMacPauseFrames"]["observedAt"] = observed_at
                        if child_node == "in-64b-frames":
                            interface_ethernet_statistics_dict_buffer["in64bFrames"] = {}
                            interface_ethernet_statistics_dict_buffer["in64bFrames"]["type"] = "Property"
                            interface_ethernet_statistics_dict_buffer["in64bFrames"]["value"] = int(element_text)
                            interface_ethernet_statistics_dict_buffer["in64bFrames"]["observedAt"] = observed_at
                        if child_node == "in-65b-to-127b-frames":
                            interface_ethernet_statistics_dict_buffer["in65bTo127bFrames"] = {}
                            interface_ethernet_statistics_dict_buffer["in65bTo127bFrames"]["type"] = "Property"
                            interface_ethernet_statistics_dict_buffer["in65bTo127bFrames"]["value"] = int(element_text)
                            interface_ethernet_statistics_dict_buffer["in65bTo127bFrames"]["observedAt"] = observed_at
                        if child_node == "in-128b-to-255b-frames":
                            interface_ethernet_statistics_dict_buffer["in128bTo255bFrames"] = {}
                            interface_ethernet_statistics_dict_buffer["in128bTo255bFrames"]["type"] = "Property"
                            interface_ethernet_statistics_dict_buffer["in128bTo255bFrames"]["value"] = int(element_text)
                            interface_ethernet_statistics_dict_buffer["in128bTo255bFrames"]["observedAt"] = observed_at
                        if child_node == "in-256b-to-511b-frames":
                            interface_ethernet_statistics_dict_buffer["in256bTo511bFrames"] = {}
                            interface_ethernet_statistics_dict_buffer["in256bTo511bFrames"]["type"] = "Property"
                            interface_ethernet_statistics_dict_buffer["in256bTo511bFrames"]["value"] = int(element_text)
                            interface_ethernet_statistics_dict_buffer["in256bTo511bFrames"]["observedAt"] = observed_at
                        if child_node == "in-512b-to-1023b-frames":
                            interface_ethernet_statistics_dict_buffer["in512bTo1023bFrames"] = {}
                            interface_ethernet_statistics_dict_buffer["in512bTo1023bFrames"]["type"] = "Property"
                            interface_ethernet_statistics_dict_buffer["in512bTo1023bFrames"]["value"] = int(element_text)
                            interface_ethernet_statistics_dict_buffer["in512bTo1023bFrames"]["observedAt"] = observed_at
                        if child_node == "in-1024b-to-1518b-frames":
                            interface_ethernet_statistics_dict_buffer["in1024bTo1518bFrames"] = {}
                            interface_ethernet_statistics_dict_buffer["in1024bTo1518bFrames"]["type"] = "Property"
                            interface_ethernet_statistics_dict_buffer["in1024bTo1518bFrames"]["value"] = int(element_text)
                            interface_ethernet_statistics_dict_buffer["in1024bTo1518bFrames"]["observedAt"] = observed_at
                        if child_node == "in-1519b-or-longer-frames":
                            interface_ethernet_statistics_dict_buffer["in1519bOrLongerFrames"] = {}
                            interface_ethernet_statistics_dict_buffer["in1519bOrLongerFrames"]["type"] = "Property"
                            interface_ethernet_statistics_dict_buffer["in1519bOrLongerFrames"]["value"] = int(element_text)
                            interface_ethernet_statistics_dict_buffer["in1519bOrLongerFrames"]["observedAt"] = observed_at
                        if child_node == "out-64b-frames":
                            interface_ethernet_statistics_dict_buffer["out64bFrames"] = {}
                            interface_ethernet_statistics_dict_buffer["out64bFrames"]["type"] = "Property"
                            interface_ethernet_statistics_dict_buffer["out64bFrames"]["value"] = int(element_text)
                            interface_ethernet_statistics_dict_buffer["out64bFrames"]["observedAt"] = observed_at
                        if child_node == "out-65b-to-127b-frames":
                            interface_ethernet_statistics_dict_buffer["out65bTo127bFrames"] = {}
                            interface_ethernet_statistics_dict_buffer["out65bTo127bFrames"]["type"] = "Property"
                            interface_ethernet_statistics_dict_buffer["out65bTo127bFrames"]["value"] = int(element_text)
                            interface_ethernet_statistics_dict_buffer["out65bTo127bFrames"]["observedAt"] = observed_at
                        if child_node == "out-128b-to-255b-frames":
                            interface_ethernet_statistics_dict_buffer["out128bTo255bFrames"] = {}
                            interface_ethernet_statistics_dict_buffer["out128bTo255bFrames"]["type"] = "Property"
                            interface_ethernet_statistics_dict_buffer["out128bTo255bFrames"]["value"] = int(element_text)
                            interface_ethernet_statistics_dict_buffer["out128bTo255bFrames"]["observedAt"] = observed_at
                        if child_node == "out-256b-to-511b-frames":
                            interface_ethernet_statistics_dict_buffer["out256bTo511bFrames"] = {}
                            interface_ethernet_statistics_dict_buffer["out256bTo511bFrames"]["type"] = "Property"
                            interface_ethernet_statistics_dict_buffer["out256bTo511bFrames"]["value"] = int(element_text)
                            interface_ethernet_statistics_dict_buffer["out256bTo511bFrames"]["observedAt"] = observed_at
                        if child_node == "out-512b-to-1023b-frames":
                            interface_ethernet_statistics_dict_buffer["out512bTo1023bFrames"] = {}
                            interface_ethernet_statistics_dict_buffer["out512bTo1023bFrames"]["type"] = "Property"
                            interface_ethernet_statistics_dict_buffer["out512bTo1023bFrames"]["value"] = int(element_text)
                            interface_ethernet_statistics_dict_buffer["out512bTo1023bFrames"]["observedAt"] = observed_at
                        if child_node == "out-1024b-to-1518b-frames":
                            interface_ethernet_statistics_dict_buffer["out1024bTo1518bFrames"] = {}
                            interface_ethernet_statistics_dict_buffer["out1024bTo1518bFrames"]["type"] = "Property"
                            interface_ethernet_statistics_dict_buffer["out1024bTo1518bFrames"]["value"] = int(element_text)
                            interface_ethernet_statistics_dict_buffer["out1024bTo1518bFrames"]["observedAt"] = observed_at
                        if child_node == "out-1519b-or-longer-frames":
                            interface_ethernet_statistics_dict_buffer["out1519bOrLongerFrames"] = {}
                            interface_ethernet_statistics_dict_buffer["out1519bOrLongerFrames"]["type"] = "Property"
                            interface_ethernet_statistics_dict_buffer["out1519bOrLongerFrames"]["value"] = int(element_text)
                            interface_ethernet_statistics_dict_buffer["out1519bOrLongerFrames"]["observedAt"] = observed_at
                        if child_node == "last-clear":
                            interface_ethernet_statistics_dict_buffer["lastClear"] = {}
                            interface_ethernet_statistics_dict_buffer["lastClear"]["type"] = "Property"
                            interface_ethernet_statistics_dict_buffer["lastClear"]["value"] = element_text
                            interface_ethernet_statistics_dict_buffer["lastClear"]["observedAt"] = observed_at
                        if len(parent_path) - 1 == 2:
                            dict_buffers.append(interface_ethernet_statistics_dict_buffer)
                if len(parent_path) - 1 == 1:
                    dict_buffers.append(interface_ethernet_dict_buffer)
        if parent_path[1] == "subinterface":
            interface_subinterface_dict_buffer = {}
            if "interface_subinterface_index" in iteration_keys:
                interface_subinterface_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterface:" + source + ":" + iteration_keys.get("interface_subinterface_index")
            interface_subinterface_dict_buffer["type"] = "InterfaceSubinterface"
            if len(parent_path) - 1 == 1 or len(parent_path) - 1 == 2:
                interface_subinterface_dict_buffer["isPartOf"] = {}
                interface_subinterface_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_subinterface_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                interface_subinterface_dict_buffer["isPartOf"]["observedAt"] = observed_at
                if child_node == "index":
                    if "." + str(element_text) not in interface_subinterface_dict_buffer["id"].split(":")[-1]:
                        interface_subinterface_dict_buffer["id"] = interface_subinterface_dict_buffer["id"] + "." + str(element_text)
                    interface_subinterface_dict_buffer["index"] = {}
                    interface_subinterface_dict_buffer["index"]["type"] = "Property"
                    interface_subinterface_dict_buffer["index"]["value"] = int(element_text)
                    interface_subinterface_dict_buffer["index"]["observedAt"] = observed_at
                if child_node == "description":
                    interface_subinterface_dict_buffer["description"] = {}
                    interface_subinterface_dict_buffer["description"]["type"] = "Property"
                    interface_subinterface_dict_buffer["description"]["value"] = element_text
                    interface_subinterface_dict_buffer["description"]["observedAt"] = observed_at
                if child_node == "admin-state":
                    interface_subinterface_dict_buffer["adminState"] = {}
                    interface_subinterface_dict_buffer["adminState"]["type"] = "Property"
                    interface_subinterface_dict_buffer["adminState"]["value"] = element_text
                    interface_subinterface_dict_buffer["adminState"]["observedAt"] = observed_at
                if child_node == "ip-mtu":
                    interface_subinterface_dict_buffer["ipMtu"] = {}
                    interface_subinterface_dict_buffer["ipMtu"]["type"] = "Property"
                    interface_subinterface_dict_buffer["ipMtu"]["value"] = int(element_text)
                    interface_subinterface_dict_buffer["ipMtu"]["observedAt"] = observed_at
                if child_node == "l2-mtu":
                    interface_subinterface_dict_buffer["l2Mtu"] = {}
                    interface_subinterface_dict_buffer["l2Mtu"]["type"] = "Property"
                    interface_subinterface_dict_buffer["l2Mtu"]["value"] = int(element_text)
                    interface_subinterface_dict_buffer["l2Mtu"]["observedAt"] = observed_at
                if child_node == "mpls-mtu":
                    interface_subinterface_dict_buffer["mplsMtu"] = {}
                    interface_subinterface_dict_buffer["mplsMtu"]["type"] = "Property"
                    interface_subinterface_dict_buffer["mplsMtu"]["value"] = int(element_text)
                    interface_subinterface_dict_buffer["mplsMtu"]["observedAt"] = observed_at
                if parent_path[2] == "unidirectional-link-delay":
                    interface_subinterface_unidirectional_link_delay_dict_buffer = {}
                    interface_subinterface_unidirectional_link_delay_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceUnidirectionalLinkDelay:" + ":".join(interface_subinterface_dict_buffer["id"].split(":")[3:])
                    interface_subinterface_unidirectional_link_delay_dict_buffer["type"] = "InterfaceSubinterfaceUnidirectionalLinkDelay"
                    if len(parent_path) - 1 == 2 or len(parent_path) - 1 == 3:
                        interface_subinterface_unidirectional_link_delay_dict_buffer["isPartOf"] = {}
                        interface_subinterface_unidirectional_link_delay_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_subinterface_unidirectional_link_delay_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                        interface_subinterface_unidirectional_link_delay_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "static-delay":
                            interface_subinterface_unidirectional_link_delay_dict_buffer["staticDelay"] = {}
                            interface_subinterface_unidirectional_link_delay_dict_buffer["staticDelay"]["type"] = "Property"
                            interface_subinterface_unidirectional_link_delay_dict_buffer["staticDelay"]["value"] = element_text
                            interface_subinterface_unidirectional_link_delay_dict_buffer["staticDelay"]["observedAt"] = observed_at
                        if child_node == "last-reported-dynamic-delay":
                            interface_subinterface_unidirectional_link_delay_dict_buffer["lastReportedDynamicDelay"] = {}
                            interface_subinterface_unidirectional_link_delay_dict_buffer["lastReportedDynamicDelay"]["type"] = "Property"
                            interface_subinterface_unidirectional_link_delay_dict_buffer["lastReportedDynamicDelay"]["value"] = element_text
                            interface_subinterface_unidirectional_link_delay_dict_buffer["lastReportedDynamicDelay"]["observedAt"] = observed_at
                        if len(parent_path) - 1 == 2:
                            dict_buffers.append(interface_subinterface_unidirectional_link_delay_dict_buffer)
                if child_node == "name":
                    if interface_subinterface_dict_buffer["id"].split(":")[-1] != element_text:
                        interface_subinterface_dict_buffer["id"] = interface_subinterface_dict_buffer["id"] + ":" + element_text
                    interface_subinterface_dict_buffer["name"] = {}
                    interface_subinterface_dict_buffer["name"]["type"] = "Property"
                    interface_subinterface_dict_buffer["name"]["value"] = element_text
                    interface_subinterface_dict_buffer["name"]["observedAt"] = observed_at
                if child_node == "ifindex":
                    interface_subinterface_dict_buffer["ifindex"] = {}
                    interface_subinterface_dict_buffer["ifindex"]["type"] = "Property"
                    interface_subinterface_dict_buffer["ifindex"]["value"] = int(element_text)
                    interface_subinterface_dict_buffer["ifindex"]["observedAt"] = observed_at
                if child_node == "oper-state":
                    interface_subinterface_dict_buffer["operState"] = {}
                    interface_subinterface_dict_buffer["operState"]["type"] = "Property"
                    interface_subinterface_dict_buffer["operState"]["value"] = element_text
                    interface_subinterface_dict_buffer["operState"]["observedAt"] = observed_at
                if child_node == "oper-down-reason":
                    interface_subinterface_dict_buffer["operDownReason"] = {}
                    interface_subinterface_dict_buffer["operDownReason"]["type"] = "Property"
                    interface_subinterface_dict_buffer["operDownReason"]["value"] = element_text
                    interface_subinterface_dict_buffer["operDownReason"]["observedAt"] = observed_at
                if child_node == "last-change":
                    interface_subinterface_dict_buffer["lastChange"] = {}
                    interface_subinterface_dict_buffer["lastChange"]["type"] = "Property"
                    interface_subinterface_dict_buffer["lastChange"]["value"] = element_text
                    interface_subinterface_dict_buffer["lastChange"]["observedAt"] = observed_at
                if parent_path[2] == "ipv4":
                    interface_subinterface_ipv4_dict_buffer = {}
                    interface_subinterface_ipv4_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceIpv4:" + ":".join(interface_subinterface_dict_buffer["id"].split(":")[3:])
                    interface_subinterface_ipv4_dict_buffer["type"] = "InterfaceSubinterfaceIpv4"
                    if len(parent_path) - 1 == 2 or len(parent_path) - 1 == 3:
                        interface_subinterface_ipv4_dict_buffer["isPartOf"] = {}
                        interface_subinterface_ipv4_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_subinterface_ipv4_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                        interface_subinterface_ipv4_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "admin-state":
                            interface_subinterface_ipv4_dict_buffer["adminState"] = {}
                            interface_subinterface_ipv4_dict_buffer["adminState"]["type"] = "Property"
                            interface_subinterface_ipv4_dict_buffer["adminState"]["value"] = element_text
                            interface_subinterface_ipv4_dict_buffer["adminState"]["observedAt"] = observed_at
                        if parent_path[3] == "address":
                            interface_subinterface_ipv4_address_dict_buffer = {}
                            if "interface_subinterface_ipv4_address_ip_prefix" in iteration_keys:
                                interface_subinterface_ipv4_address_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceIpv4Address:" + source + ":" + iteration_keys.get("interface_subinterface_ipv4_address_ip-prefix")
                            interface_subinterface_ipv4_address_dict_buffer["type"] = "InterfaceSubinterfaceIpv4Address"
                            if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                                interface_subinterface_ipv4_address_dict_buffer["isPartOf"] = {}
                                interface_subinterface_ipv4_address_dict_buffer["isPartOf"]["type"] = "Relationship"
                                interface_subinterface_ipv4_address_dict_buffer["isPartOf"]["object"] = interface_subinterface_ipv4_dict_buffer["id"]
                                interface_subinterface_ipv4_address_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                if child_node == "ip-prefix":
                                    interface_subinterface_ipv4_address_dict_buffer["ipPrefix"] = {}
                                    interface_subinterface_ipv4_address_dict_buffer["ipPrefix"]["type"] = "Property"
                                    interface_subinterface_ipv4_address_dict_buffer["ipPrefix"]["value"] = element_text
                                    interface_subinterface_ipv4_address_dict_buffer["ipPrefix"]["observedAt"] = observed_at
                                if child_node == "anycast-gw":
                                    interface_subinterface_ipv4_address_dict_buffer["anycastGw"] = {}
                                    interface_subinterface_ipv4_address_dict_buffer["anycastGw"]["type"] = "Property"
                                    interface_subinterface_ipv4_address_dict_buffer["anycastGw"]["value"] = eval(str(element_text).capitalize())
                                    interface_subinterface_ipv4_address_dict_buffer["anycastGw"]["observedAt"] = observed_at
                                if child_node == "origin":
                                    interface_subinterface_ipv4_address_dict_buffer["origin"] = {}
                                    interface_subinterface_ipv4_address_dict_buffer["origin"]["type"] = "Property"
                                    interface_subinterface_ipv4_address_dict_buffer["origin"]["value"] = element_text
                                    interface_subinterface_ipv4_address_dict_buffer["origin"]["observedAt"] = observed_at
                                if child_node == "primary":
                                    interface_subinterface_ipv4_address_dict_buffer["primary"] = {}
                                    interface_subinterface_ipv4_address_dict_buffer["primary"]["type"] = "Property"
                                    interface_subinterface_ipv4_address_dict_buffer["primary"]["value"] = element_text
                                    interface_subinterface_ipv4_address_dict_buffer["primary"]["observedAt"] = observed_at
                                if child_node == "status":
                                    interface_subinterface_ipv4_address_dict_buffer["status"] = {}
                                    interface_subinterface_ipv4_address_dict_buffer["status"]["type"] = "Property"
                                    interface_subinterface_ipv4_address_dict_buffer["status"]["value"] = element_text
                                    interface_subinterface_ipv4_address_dict_buffer["status"]["observedAt"] = observed_at
                                if len(parent_path) - 1 == 3:
                                    dict_buffers.append(interface_subinterface_ipv4_address_dict_buffer)
                        if child_node == "allow-directed-broadcast":
                            interface_subinterface_ipv4_dict_buffer["allowDirectedBroadcast"] = {}
                            interface_subinterface_ipv4_dict_buffer["allowDirectedBroadcast"]["type"] = "Property"
                            interface_subinterface_ipv4_dict_buffer["allowDirectedBroadcast"]["value"] = eval(str(element_text).capitalize())
                            interface_subinterface_ipv4_dict_buffer["allowDirectedBroadcast"]["observedAt"] = observed_at
                        if parent_path[3] == "unnumbered":
                            interface_subinterface_ipv4_unnumbered_dict_buffer = {}
                            interface_subinterface_ipv4_unnumbered_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceIpv4Unnumbered:" + ":".join(interface_subinterface_ipv4_dict_buffer["id"].split(":")[3:])
                            interface_subinterface_ipv4_unnumbered_dict_buffer["type"] = "InterfaceSubinterfaceIpv4Unnumbered"
                            if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                                interface_subinterface_ipv4_unnumbered_dict_buffer["isPartOf"] = {}
                                interface_subinterface_ipv4_unnumbered_dict_buffer["isPartOf"]["type"] = "Relationship"
                                interface_subinterface_ipv4_unnumbered_dict_buffer["isPartOf"]["object"] = interface_subinterface_ipv4_dict_buffer["id"]
                                interface_subinterface_ipv4_unnumbered_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                if child_node == "admin-state":
                                    interface_subinterface_ipv4_unnumbered_dict_buffer["adminState"] = {}
                                    interface_subinterface_ipv4_unnumbered_dict_buffer["adminState"]["type"] = "Property"
                                    interface_subinterface_ipv4_unnumbered_dict_buffer["adminState"]["value"] = element_text
                                    interface_subinterface_ipv4_unnumbered_dict_buffer["adminState"]["observedAt"] = observed_at
                                if child_node == "interface":
                                    interface_subinterface_ipv4_unnumbered_dict_buffer["interface"] = {}
                                    interface_subinterface_ipv4_unnumbered_dict_buffer["interface"]["type"] = "Property"
                                    interface_subinterface_ipv4_unnumbered_dict_buffer["interface"]["value"] = element_text
                                    interface_subinterface_ipv4_unnumbered_dict_buffer["interface"]["observedAt"] = observed_at
                                if child_node == "address":
                                    interface_subinterface_ipv4_unnumbered_dict_buffer["address"] = {}
                                    interface_subinterface_ipv4_unnumbered_dict_buffer["address"]["type"] = "Property"
                                    interface_subinterface_ipv4_unnumbered_dict_buffer["address"]["value"] = element_text
                                    interface_subinterface_ipv4_unnumbered_dict_buffer["address"]["observedAt"] = observed_at
                                if child_node == "unavailable-address-reason":
                                    interface_subinterface_ipv4_unnumbered_dict_buffer["unavailableAddressReason"] = {}
                                    interface_subinterface_ipv4_unnumbered_dict_buffer["unavailableAddressReason"]["type"] = "Property"
                                    interface_subinterface_ipv4_unnumbered_dict_buffer["unavailableAddressReason"]["value"] = element_text
                                    interface_subinterface_ipv4_unnumbered_dict_buffer["unavailableAddressReason"]["observedAt"] = observed_at
                                if len(parent_path) - 1 == 3:
                                    dict_buffers.append(interface_subinterface_ipv4_unnumbered_dict_buffer)
                        if parent_path[3] == "statistics":
                            interface_subinterface_ipv4_statistics_dict_buffer = {}
                            interface_subinterface_ipv4_statistics_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceIpv4Statistics:" + ":".join(interface_subinterface_ipv4_dict_buffer["id"].split(":")[3:])
                            interface_subinterface_ipv4_statistics_dict_buffer["type"] = "InterfaceSubinterfaceIpv4Statistics"
                            if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                                interface_subinterface_ipv4_statistics_dict_buffer["isPartOf"] = {}
                                interface_subinterface_ipv4_statistics_dict_buffer["isPartOf"]["type"] = "Relationship"
                                interface_subinterface_ipv4_statistics_dict_buffer["isPartOf"]["object"] = interface_subinterface_ipv4_dict_buffer["id"]
                                interface_subinterface_ipv4_statistics_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                if child_node == "in-packets":
                                    interface_subinterface_ipv4_statistics_dict_buffer["inPackets"] = {}
                                    interface_subinterface_ipv4_statistics_dict_buffer["inPackets"]["type"] = "Property"
                                    interface_subinterface_ipv4_statistics_dict_buffer["inPackets"]["value"] = int(element_text)
                                    interface_subinterface_ipv4_statistics_dict_buffer["inPackets"]["observedAt"] = observed_at
                                if child_node == "in-octets":
                                    interface_subinterface_ipv4_statistics_dict_buffer["inOctets"] = {}
                                    interface_subinterface_ipv4_statistics_dict_buffer["inOctets"]["type"] = "Property"
                                    interface_subinterface_ipv4_statistics_dict_buffer["inOctets"]["value"] = int(element_text)
                                    interface_subinterface_ipv4_statistics_dict_buffer["inOctets"]["observedAt"] = observed_at
                                if child_node == "in-error-packets":
                                    interface_subinterface_ipv4_statistics_dict_buffer["inErrorPackets"] = {}
                                    interface_subinterface_ipv4_statistics_dict_buffer["inErrorPackets"]["type"] = "Property"
                                    interface_subinterface_ipv4_statistics_dict_buffer["inErrorPackets"]["value"] = int(element_text)
                                    interface_subinterface_ipv4_statistics_dict_buffer["inErrorPackets"]["observedAt"] = observed_at
                                if child_node == "in-discarded-packets":
                                    interface_subinterface_ipv4_statistics_dict_buffer["inDiscardedPackets"] = {}
                                    interface_subinterface_ipv4_statistics_dict_buffer["inDiscardedPackets"]["type"] = "Property"
                                    interface_subinterface_ipv4_statistics_dict_buffer["inDiscardedPackets"]["value"] = int(element_text)
                                    interface_subinterface_ipv4_statistics_dict_buffer["inDiscardedPackets"]["observedAt"] = observed_at
                                if child_node == "in-terminated-packets":
                                    interface_subinterface_ipv4_statistics_dict_buffer["inTerminatedPackets"] = {}
                                    interface_subinterface_ipv4_statistics_dict_buffer["inTerminatedPackets"]["type"] = "Property"
                                    interface_subinterface_ipv4_statistics_dict_buffer["inTerminatedPackets"]["value"] = int(element_text)
                                    interface_subinterface_ipv4_statistics_dict_buffer["inTerminatedPackets"]["observedAt"] = observed_at
                                if child_node == "in-terminated-octets":
                                    interface_subinterface_ipv4_statistics_dict_buffer["inTerminatedOctets"] = {}
                                    interface_subinterface_ipv4_statistics_dict_buffer["inTerminatedOctets"]["type"] = "Property"
                                    interface_subinterface_ipv4_statistics_dict_buffer["inTerminatedOctets"]["value"] = int(element_text)
                                    interface_subinterface_ipv4_statistics_dict_buffer["inTerminatedOctets"]["observedAt"] = observed_at
                                if child_node == "in-forwarded-packets":
                                    interface_subinterface_ipv4_statistics_dict_buffer["inForwardedPackets"] = {}
                                    interface_subinterface_ipv4_statistics_dict_buffer["inForwardedPackets"]["type"] = "Property"
                                    interface_subinterface_ipv4_statistics_dict_buffer["inForwardedPackets"]["value"] = int(element_text)
                                    interface_subinterface_ipv4_statistics_dict_buffer["inForwardedPackets"]["observedAt"] = observed_at
                                if child_node == "in-forwarded-octets":
                                    interface_subinterface_ipv4_statistics_dict_buffer["inForwardedOctets"] = {}
                                    interface_subinterface_ipv4_statistics_dict_buffer["inForwardedOctets"]["type"] = "Property"
                                    interface_subinterface_ipv4_statistics_dict_buffer["inForwardedOctets"]["value"] = int(element_text)
                                    interface_subinterface_ipv4_statistics_dict_buffer["inForwardedOctets"]["observedAt"] = observed_at
                                if child_node == "in-matched-ra-packets":
                                    interface_subinterface_ipv4_statistics_dict_buffer["inMatchedRaPackets"] = {}
                                    interface_subinterface_ipv4_statistics_dict_buffer["inMatchedRaPackets"]["type"] = "Property"
                                    interface_subinterface_ipv4_statistics_dict_buffer["inMatchedRaPackets"]["value"] = int(element_text)
                                    interface_subinterface_ipv4_statistics_dict_buffer["inMatchedRaPackets"]["observedAt"] = observed_at
                                if child_node == "out-forwarded-packets":
                                    interface_subinterface_ipv4_statistics_dict_buffer["outForwardedPackets"] = {}
                                    interface_subinterface_ipv4_statistics_dict_buffer["outForwardedPackets"]["type"] = "Property"
                                    interface_subinterface_ipv4_statistics_dict_buffer["outForwardedPackets"]["value"] = int(element_text)
                                    interface_subinterface_ipv4_statistics_dict_buffer["outForwardedPackets"]["observedAt"] = observed_at
                                if child_node == "out-forwarded-octets":
                                    interface_subinterface_ipv4_statistics_dict_buffer["outForwardedOctets"] = {}
                                    interface_subinterface_ipv4_statistics_dict_buffer["outForwardedOctets"]["type"] = "Property"
                                    interface_subinterface_ipv4_statistics_dict_buffer["outForwardedOctets"]["value"] = int(element_text)
                                    interface_subinterface_ipv4_statistics_dict_buffer["outForwardedOctets"]["observedAt"] = observed_at
                                if child_node == "out-originated-packets":
                                    interface_subinterface_ipv4_statistics_dict_buffer["outOriginatedPackets"] = {}
                                    interface_subinterface_ipv4_statistics_dict_buffer["outOriginatedPackets"]["type"] = "Property"
                                    interface_subinterface_ipv4_statistics_dict_buffer["outOriginatedPackets"]["value"] = int(element_text)
                                    interface_subinterface_ipv4_statistics_dict_buffer["outOriginatedPackets"]["observedAt"] = observed_at
                                if child_node == "out-originated-octets":
                                    interface_subinterface_ipv4_statistics_dict_buffer["outOriginatedOctets"] = {}
                                    interface_subinterface_ipv4_statistics_dict_buffer["outOriginatedOctets"]["type"] = "Property"
                                    interface_subinterface_ipv4_statistics_dict_buffer["outOriginatedOctets"]["value"] = int(element_text)
                                    interface_subinterface_ipv4_statistics_dict_buffer["outOriginatedOctets"]["observedAt"] = observed_at
                                if child_node == "out-error-packets":
                                    interface_subinterface_ipv4_statistics_dict_buffer["outErrorPackets"] = {}
                                    interface_subinterface_ipv4_statistics_dict_buffer["outErrorPackets"]["type"] = "Property"
                                    interface_subinterface_ipv4_statistics_dict_buffer["outErrorPackets"]["value"] = int(element_text)
                                    interface_subinterface_ipv4_statistics_dict_buffer["outErrorPackets"]["observedAt"] = observed_at
                                if child_node == "out-discarded-packets":
                                    interface_subinterface_ipv4_statistics_dict_buffer["outDiscardedPackets"] = {}
                                    interface_subinterface_ipv4_statistics_dict_buffer["outDiscardedPackets"]["type"] = "Property"
                                    interface_subinterface_ipv4_statistics_dict_buffer["outDiscardedPackets"]["value"] = int(element_text)
                                    interface_subinterface_ipv4_statistics_dict_buffer["outDiscardedPackets"]["observedAt"] = observed_at
                                if child_node == "out-packets":
                                    interface_subinterface_ipv4_statistics_dict_buffer["outPackets"] = {}
                                    interface_subinterface_ipv4_statistics_dict_buffer["outPackets"]["type"] = "Property"
                                    interface_subinterface_ipv4_statistics_dict_buffer["outPackets"]["value"] = int(element_text)
                                    interface_subinterface_ipv4_statistics_dict_buffer["outPackets"]["observedAt"] = observed_at
                                if child_node == "out-octets":
                                    interface_subinterface_ipv4_statistics_dict_buffer["outOctets"] = {}
                                    interface_subinterface_ipv4_statistics_dict_buffer["outOctets"]["type"] = "Property"
                                    interface_subinterface_ipv4_statistics_dict_buffer["outOctets"]["value"] = int(element_text)
                                    interface_subinterface_ipv4_statistics_dict_buffer["outOctets"]["observedAt"] = observed_at
                                if child_node == "last-clear":
                                    interface_subinterface_ipv4_statistics_dict_buffer["lastClear"] = {}
                                    interface_subinterface_ipv4_statistics_dict_buffer["lastClear"]["type"] = "Property"
                                    interface_subinterface_ipv4_statistics_dict_buffer["lastClear"]["value"] = element_text
                                    interface_subinterface_ipv4_statistics_dict_buffer["lastClear"]["observedAt"] = observed_at
                                if len(parent_path) - 1 == 3:
                                    dict_buffers.append(interface_subinterface_ipv4_statistics_dict_buffer)
                        if len(parent_path) - 1 == 2:
                            dict_buffers.append(interface_subinterface_ipv4_dict_buffer)
                if parent_path[2] == "ipv6":
                    interface_subinterface_ipv6_dict_buffer = {}
                    interface_subinterface_ipv6_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceIpv6:" + ":".join(interface_subinterface_dict_buffer["id"].split(":")[3:])
                    interface_subinterface_ipv6_dict_buffer["type"] = "InterfaceSubinterfaceIpv6"
                    if len(parent_path) - 1 == 2 or len(parent_path) - 1 == 3:
                        interface_subinterface_ipv6_dict_buffer["isPartOf"] = {}
                        interface_subinterface_ipv6_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_subinterface_ipv6_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                        interface_subinterface_ipv6_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "admin-state":
                            interface_subinterface_ipv6_dict_buffer["adminState"] = {}
                            interface_subinterface_ipv6_dict_buffer["adminState"]["type"] = "Property"
                            interface_subinterface_ipv6_dict_buffer["adminState"]["value"] = element_text
                            interface_subinterface_ipv6_dict_buffer["adminState"]["observedAt"] = observed_at
                        if parent_path[3] == "address":
                            interface_subinterface_ipv6_address_dict_buffer = {}
                            if "interface_subinterface_ipv6_address_ip_prefix" in iteration_keys:
                                interface_subinterface_ipv6_address_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceIpv6Address:" + source + ":" + iteration_keys.get("interface_subinterface_ipv6_address_ip-prefix")
                            interface_subinterface_ipv6_address_dict_buffer["type"] = "InterfaceSubinterfaceIpv6Address"
                            if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                                interface_subinterface_ipv6_address_dict_buffer["isPartOf"] = {}
                                interface_subinterface_ipv6_address_dict_buffer["isPartOf"]["type"] = "Relationship"
                                interface_subinterface_ipv6_address_dict_buffer["isPartOf"]["object"] = interface_subinterface_ipv6_dict_buffer["id"]
                                interface_subinterface_ipv6_address_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                if child_node == "ip-prefix":
                                    interface_subinterface_ipv6_address_dict_buffer["ipPrefix"] = {}
                                    interface_subinterface_ipv6_address_dict_buffer["ipPrefix"]["type"] = "Property"
                                    interface_subinterface_ipv6_address_dict_buffer["ipPrefix"]["value"] = element_text
                                    interface_subinterface_ipv6_address_dict_buffer["ipPrefix"]["observedAt"] = observed_at
                                if child_node == "type":
                                    interface_subinterface_ipv6_address_dict_buffer["type"] = {}
                                    interface_subinterface_ipv6_address_dict_buffer["type"]["type"] = "Property"
                                    interface_subinterface_ipv6_address_dict_buffer["type"]["value"] = element_text
                                    interface_subinterface_ipv6_address_dict_buffer["type"]["observedAt"] = observed_at
                                if child_node == "anycast-gw":
                                    interface_subinterface_ipv6_address_dict_buffer["anycastGw"] = {}
                                    interface_subinterface_ipv6_address_dict_buffer["anycastGw"]["type"] = "Property"
                                    interface_subinterface_ipv6_address_dict_buffer["anycastGw"]["value"] = eval(str(element_text).capitalize())
                                    interface_subinterface_ipv6_address_dict_buffer["anycastGw"]["observedAt"] = observed_at
                                if child_node == "origin":
                                    interface_subinterface_ipv6_address_dict_buffer["origin"] = {}
                                    interface_subinterface_ipv6_address_dict_buffer["origin"]["type"] = "Property"
                                    interface_subinterface_ipv6_address_dict_buffer["origin"]["value"] = element_text
                                    interface_subinterface_ipv6_address_dict_buffer["origin"]["observedAt"] = observed_at
                                if child_node == "primary":
                                    interface_subinterface_ipv6_address_dict_buffer["primary"] = {}
                                    interface_subinterface_ipv6_address_dict_buffer["primary"]["type"] = "Property"
                                    interface_subinterface_ipv6_address_dict_buffer["primary"]["value"] = element_text
                                    interface_subinterface_ipv6_address_dict_buffer["primary"]["observedAt"] = observed_at
                                if child_node == "status":
                                    interface_subinterface_ipv6_address_dict_buffer["status"] = {}
                                    interface_subinterface_ipv6_address_dict_buffer["status"]["type"] = "Property"
                                    interface_subinterface_ipv6_address_dict_buffer["status"]["value"] = element_text
                                    interface_subinterface_ipv6_address_dict_buffer["status"]["observedAt"] = observed_at
                                if len(parent_path) - 1 == 3:
                                    dict_buffers.append(interface_subinterface_ipv6_address_dict_buffer)
                        if parent_path[3] == "statistics":
                            interface_subinterface_ipv6_statistics_dict_buffer = {}
                            interface_subinterface_ipv6_statistics_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceIpv6Statistics:" + ":".join(interface_subinterface_ipv6_dict_buffer["id"].split(":")[3:])
                            interface_subinterface_ipv6_statistics_dict_buffer["type"] = "InterfaceSubinterfaceIpv6Statistics"
                            if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                                interface_subinterface_ipv6_statistics_dict_buffer["isPartOf"] = {}
                                interface_subinterface_ipv6_statistics_dict_buffer["isPartOf"]["type"] = "Relationship"
                                interface_subinterface_ipv6_statistics_dict_buffer["isPartOf"]["object"] = interface_subinterface_ipv6_dict_buffer["id"]
                                interface_subinterface_ipv6_statistics_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                if child_node == "in-packets":
                                    interface_subinterface_ipv6_statistics_dict_buffer["inPackets"] = {}
                                    interface_subinterface_ipv6_statistics_dict_buffer["inPackets"]["type"] = "Property"
                                    interface_subinterface_ipv6_statistics_dict_buffer["inPackets"]["value"] = int(element_text)
                                    interface_subinterface_ipv6_statistics_dict_buffer["inPackets"]["observedAt"] = observed_at
                                if child_node == "in-octets":
                                    interface_subinterface_ipv6_statistics_dict_buffer["inOctets"] = {}
                                    interface_subinterface_ipv6_statistics_dict_buffer["inOctets"]["type"] = "Property"
                                    interface_subinterface_ipv6_statistics_dict_buffer["inOctets"]["value"] = int(element_text)
                                    interface_subinterface_ipv6_statistics_dict_buffer["inOctets"]["observedAt"] = observed_at
                                if child_node == "in-error-packets":
                                    interface_subinterface_ipv6_statistics_dict_buffer["inErrorPackets"] = {}
                                    interface_subinterface_ipv6_statistics_dict_buffer["inErrorPackets"]["type"] = "Property"
                                    interface_subinterface_ipv6_statistics_dict_buffer["inErrorPackets"]["value"] = int(element_text)
                                    interface_subinterface_ipv6_statistics_dict_buffer["inErrorPackets"]["observedAt"] = observed_at
                                if child_node == "in-discarded-packets":
                                    interface_subinterface_ipv6_statistics_dict_buffer["inDiscardedPackets"] = {}
                                    interface_subinterface_ipv6_statistics_dict_buffer["inDiscardedPackets"]["type"] = "Property"
                                    interface_subinterface_ipv6_statistics_dict_buffer["inDiscardedPackets"]["value"] = int(element_text)
                                    interface_subinterface_ipv6_statistics_dict_buffer["inDiscardedPackets"]["observedAt"] = observed_at
                                if child_node == "in-terminated-packets":
                                    interface_subinterface_ipv6_statistics_dict_buffer["inTerminatedPackets"] = {}
                                    interface_subinterface_ipv6_statistics_dict_buffer["inTerminatedPackets"]["type"] = "Property"
                                    interface_subinterface_ipv6_statistics_dict_buffer["inTerminatedPackets"]["value"] = int(element_text)
                                    interface_subinterface_ipv6_statistics_dict_buffer["inTerminatedPackets"]["observedAt"] = observed_at
                                if child_node == "in-terminated-octets":
                                    interface_subinterface_ipv6_statistics_dict_buffer["inTerminatedOctets"] = {}
                                    interface_subinterface_ipv6_statistics_dict_buffer["inTerminatedOctets"]["type"] = "Property"
                                    interface_subinterface_ipv6_statistics_dict_buffer["inTerminatedOctets"]["value"] = int(element_text)
                                    interface_subinterface_ipv6_statistics_dict_buffer["inTerminatedOctets"]["observedAt"] = observed_at
                                if child_node == "in-forwarded-packets":
                                    interface_subinterface_ipv6_statistics_dict_buffer["inForwardedPackets"] = {}
                                    interface_subinterface_ipv6_statistics_dict_buffer["inForwardedPackets"]["type"] = "Property"
                                    interface_subinterface_ipv6_statistics_dict_buffer["inForwardedPackets"]["value"] = int(element_text)
                                    interface_subinterface_ipv6_statistics_dict_buffer["inForwardedPackets"]["observedAt"] = observed_at
                                if child_node == "in-forwarded-octets":
                                    interface_subinterface_ipv6_statistics_dict_buffer["inForwardedOctets"] = {}
                                    interface_subinterface_ipv6_statistics_dict_buffer["inForwardedOctets"]["type"] = "Property"
                                    interface_subinterface_ipv6_statistics_dict_buffer["inForwardedOctets"]["value"] = int(element_text)
                                    interface_subinterface_ipv6_statistics_dict_buffer["inForwardedOctets"]["observedAt"] = observed_at
                                if child_node == "in-matched-ra-packets":
                                    interface_subinterface_ipv6_statistics_dict_buffer["inMatchedRaPackets"] = {}
                                    interface_subinterface_ipv6_statistics_dict_buffer["inMatchedRaPackets"]["type"] = "Property"
                                    interface_subinterface_ipv6_statistics_dict_buffer["inMatchedRaPackets"]["value"] = int(element_text)
                                    interface_subinterface_ipv6_statistics_dict_buffer["inMatchedRaPackets"]["observedAt"] = observed_at
                                if child_node == "out-forwarded-packets":
                                    interface_subinterface_ipv6_statistics_dict_buffer["outForwardedPackets"] = {}
                                    interface_subinterface_ipv6_statistics_dict_buffer["outForwardedPackets"]["type"] = "Property"
                                    interface_subinterface_ipv6_statistics_dict_buffer["outForwardedPackets"]["value"] = int(element_text)
                                    interface_subinterface_ipv6_statistics_dict_buffer["outForwardedPackets"]["observedAt"] = observed_at
                                if child_node == "out-forwarded-octets":
                                    interface_subinterface_ipv6_statistics_dict_buffer["outForwardedOctets"] = {}
                                    interface_subinterface_ipv6_statistics_dict_buffer["outForwardedOctets"]["type"] = "Property"
                                    interface_subinterface_ipv6_statistics_dict_buffer["outForwardedOctets"]["value"] = int(element_text)
                                    interface_subinterface_ipv6_statistics_dict_buffer["outForwardedOctets"]["observedAt"] = observed_at
                                if child_node == "out-originated-packets":
                                    interface_subinterface_ipv6_statistics_dict_buffer["outOriginatedPackets"] = {}
                                    interface_subinterface_ipv6_statistics_dict_buffer["outOriginatedPackets"]["type"] = "Property"
                                    interface_subinterface_ipv6_statistics_dict_buffer["outOriginatedPackets"]["value"] = int(element_text)
                                    interface_subinterface_ipv6_statistics_dict_buffer["outOriginatedPackets"]["observedAt"] = observed_at
                                if child_node == "out-originated-octets":
                                    interface_subinterface_ipv6_statistics_dict_buffer["outOriginatedOctets"] = {}
                                    interface_subinterface_ipv6_statistics_dict_buffer["outOriginatedOctets"]["type"] = "Property"
                                    interface_subinterface_ipv6_statistics_dict_buffer["outOriginatedOctets"]["value"] = int(element_text)
                                    interface_subinterface_ipv6_statistics_dict_buffer["outOriginatedOctets"]["observedAt"] = observed_at
                                if child_node == "out-error-packets":
                                    interface_subinterface_ipv6_statistics_dict_buffer["outErrorPackets"] = {}
                                    interface_subinterface_ipv6_statistics_dict_buffer["outErrorPackets"]["type"] = "Property"
                                    interface_subinterface_ipv6_statistics_dict_buffer["outErrorPackets"]["value"] = int(element_text)
                                    interface_subinterface_ipv6_statistics_dict_buffer["outErrorPackets"]["observedAt"] = observed_at
                                if child_node == "out-discarded-packets":
                                    interface_subinterface_ipv6_statistics_dict_buffer["outDiscardedPackets"] = {}
                                    interface_subinterface_ipv6_statistics_dict_buffer["outDiscardedPackets"]["type"] = "Property"
                                    interface_subinterface_ipv6_statistics_dict_buffer["outDiscardedPackets"]["value"] = int(element_text)
                                    interface_subinterface_ipv6_statistics_dict_buffer["outDiscardedPackets"]["observedAt"] = observed_at
                                if child_node == "out-packets":
                                    interface_subinterface_ipv6_statistics_dict_buffer["outPackets"] = {}
                                    interface_subinterface_ipv6_statistics_dict_buffer["outPackets"]["type"] = "Property"
                                    interface_subinterface_ipv6_statistics_dict_buffer["outPackets"]["value"] = int(element_text)
                                    interface_subinterface_ipv6_statistics_dict_buffer["outPackets"]["observedAt"] = observed_at
                                if child_node == "out-octets":
                                    interface_subinterface_ipv6_statistics_dict_buffer["outOctets"] = {}
                                    interface_subinterface_ipv6_statistics_dict_buffer["outOctets"]["type"] = "Property"
                                    interface_subinterface_ipv6_statistics_dict_buffer["outOctets"]["value"] = int(element_text)
                                    interface_subinterface_ipv6_statistics_dict_buffer["outOctets"]["observedAt"] = observed_at
                                if child_node == "last-clear":
                                    interface_subinterface_ipv6_statistics_dict_buffer["lastClear"] = {}
                                    interface_subinterface_ipv6_statistics_dict_buffer["lastClear"]["type"] = "Property"
                                    interface_subinterface_ipv6_statistics_dict_buffer["lastClear"]["value"] = element_text
                                    interface_subinterface_ipv6_statistics_dict_buffer["lastClear"]["observedAt"] = observed_at
                                if len(parent_path) - 1 == 3:
                                    dict_buffers.append(interface_subinterface_ipv6_statistics_dict_buffer)
                        if len(parent_path) - 1 == 2:
                            dict_buffers.append(interface_subinterface_ipv6_dict_buffer)
                if parent_path[2] == "anycast-gw":
                    interface_subinterface_anycast_gw_dict_buffer = {}
                    interface_subinterface_anycast_gw_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceAnycastGw:" + ":".join(interface_subinterface_dict_buffer["id"].split(":")[3:])
                    interface_subinterface_anycast_gw_dict_buffer["type"] = "InterfaceSubinterfaceAnycastGw"
                    if len(parent_path) - 1 == 2 or len(parent_path) - 1 == 3:
                        interface_subinterface_anycast_gw_dict_buffer["isPartOf"] = {}
                        interface_subinterface_anycast_gw_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_subinterface_anycast_gw_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                        interface_subinterface_anycast_gw_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "virtual-router-id":
                            if interface_subinterface_anycast_gw_dict_buffer["id"].split(":")[-1] != int(element_text):
                                interface_subinterface_anycast_gw_dict_buffer["id"] = interface_subinterface_anycast_gw_dict_buffer["id"] + ":" + int(element_text)
                            interface_subinterface_anycast_gw_dict_buffer["virtualRouterId"] = {}
                            interface_subinterface_anycast_gw_dict_buffer["virtualRouterId"]["type"] = "Property"
                            interface_subinterface_anycast_gw_dict_buffer["virtualRouterId"]["value"] = int(element_text)
                            interface_subinterface_anycast_gw_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                        if child_node == "anycast-gw-mac":
                            interface_subinterface_anycast_gw_dict_buffer["anycastGwMac"] = {}
                            interface_subinterface_anycast_gw_dict_buffer["anycastGwMac"]["type"] = "Property"
                            interface_subinterface_anycast_gw_dict_buffer["anycastGwMac"]["value"] = element_text
                            interface_subinterface_anycast_gw_dict_buffer["anycastGwMac"]["observedAt"] = observed_at
                        if child_node == "anycast-gw-mac-origin":
                            interface_subinterface_anycast_gw_dict_buffer["anycastGwMacOrigin"] = {}
                            interface_subinterface_anycast_gw_dict_buffer["anycastGwMacOrigin"]["type"] = "Property"
                            interface_subinterface_anycast_gw_dict_buffer["anycastGwMacOrigin"]["value"] = element_text
                            interface_subinterface_anycast_gw_dict_buffer["anycastGwMacOrigin"]["observedAt"] = observed_at
                        if len(parent_path) - 1 == 2:
                            dict_buffers.append(interface_subinterface_anycast_gw_dict_buffer)
                if parent_path[2] == "statistics":
                    interface_subinterface_statistics_dict_buffer = {}
                    interface_subinterface_statistics_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceStatistics:" + ":".join(interface_subinterface_dict_buffer["id"].split(":")[3:])
                    interface_subinterface_statistics_dict_buffer["type"] = "InterfaceSubinterfaceStatistics"
                    if len(parent_path) - 1 == 2 or len(parent_path) - 1 == 3:
                        interface_subinterface_statistics_dict_buffer["isPartOf"] = {}
                        interface_subinterface_statistics_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_subinterface_statistics_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                        interface_subinterface_statistics_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "in-packets":
                            interface_subinterface_statistics_dict_buffer["inPackets"] = {}
                            interface_subinterface_statistics_dict_buffer["inPackets"]["type"] = "Property"
                            interface_subinterface_statistics_dict_buffer["inPackets"]["value"] = int(element_text)
                            interface_subinterface_statistics_dict_buffer["inPackets"]["observedAt"] = observed_at
                        if child_node == "in-octets":
                            interface_subinterface_statistics_dict_buffer["inOctets"] = {}
                            interface_subinterface_statistics_dict_buffer["inOctets"]["type"] = "Property"
                            interface_subinterface_statistics_dict_buffer["inOctets"]["value"] = int(element_text)
                            interface_subinterface_statistics_dict_buffer["inOctets"]["observedAt"] = observed_at
                        if child_node == "in-error-packets":
                            interface_subinterface_statistics_dict_buffer["inErrorPackets"] = {}
                            interface_subinterface_statistics_dict_buffer["inErrorPackets"]["type"] = "Property"
                            interface_subinterface_statistics_dict_buffer["inErrorPackets"]["value"] = int(element_text)
                            interface_subinterface_statistics_dict_buffer["inErrorPackets"]["observedAt"] = observed_at
                        if child_node == "in-discarded-packets":
                            interface_subinterface_statistics_dict_buffer["inDiscardedPackets"] = {}
                            interface_subinterface_statistics_dict_buffer["inDiscardedPackets"]["type"] = "Property"
                            interface_subinterface_statistics_dict_buffer["inDiscardedPackets"]["value"] = int(element_text)
                            interface_subinterface_statistics_dict_buffer["inDiscardedPackets"]["observedAt"] = observed_at
                        if child_node == "in-terminated-packets":
                            interface_subinterface_statistics_dict_buffer["inTerminatedPackets"] = {}
                            interface_subinterface_statistics_dict_buffer["inTerminatedPackets"]["type"] = "Property"
                            interface_subinterface_statistics_dict_buffer["inTerminatedPackets"]["value"] = int(element_text)
                            interface_subinterface_statistics_dict_buffer["inTerminatedPackets"]["observedAt"] = observed_at
                        if child_node == "in-terminated-octets":
                            interface_subinterface_statistics_dict_buffer["inTerminatedOctets"] = {}
                            interface_subinterface_statistics_dict_buffer["inTerminatedOctets"]["type"] = "Property"
                            interface_subinterface_statistics_dict_buffer["inTerminatedOctets"]["value"] = int(element_text)
                            interface_subinterface_statistics_dict_buffer["inTerminatedOctets"]["observedAt"] = observed_at
                        if child_node == "in-forwarded-packets":
                            interface_subinterface_statistics_dict_buffer["inForwardedPackets"] = {}
                            interface_subinterface_statistics_dict_buffer["inForwardedPackets"]["type"] = "Property"
                            interface_subinterface_statistics_dict_buffer["inForwardedPackets"]["value"] = int(element_text)
                            interface_subinterface_statistics_dict_buffer["inForwardedPackets"]["observedAt"] = observed_at
                        if child_node == "in-forwarded-octets":
                            interface_subinterface_statistics_dict_buffer["inForwardedOctets"] = {}
                            interface_subinterface_statistics_dict_buffer["inForwardedOctets"]["type"] = "Property"
                            interface_subinterface_statistics_dict_buffer["inForwardedOctets"]["value"] = int(element_text)
                            interface_subinterface_statistics_dict_buffer["inForwardedOctets"]["observedAt"] = observed_at
                        if child_node == "in-matched-ra-packets":
                            interface_subinterface_statistics_dict_buffer["inMatchedRaPackets"] = {}
                            interface_subinterface_statistics_dict_buffer["inMatchedRaPackets"]["type"] = "Property"
                            interface_subinterface_statistics_dict_buffer["inMatchedRaPackets"]["value"] = int(element_text)
                            interface_subinterface_statistics_dict_buffer["inMatchedRaPackets"]["observedAt"] = observed_at
                        if child_node == "out-forwarded-packets":
                            interface_subinterface_statistics_dict_buffer["outForwardedPackets"] = {}
                            interface_subinterface_statistics_dict_buffer["outForwardedPackets"]["type"] = "Property"
                            interface_subinterface_statistics_dict_buffer["outForwardedPackets"]["value"] = int(element_text)
                            interface_subinterface_statistics_dict_buffer["outForwardedPackets"]["observedAt"] = observed_at
                        if child_node == "out-forwarded-octets":
                            interface_subinterface_statistics_dict_buffer["outForwardedOctets"] = {}
                            interface_subinterface_statistics_dict_buffer["outForwardedOctets"]["type"] = "Property"
                            interface_subinterface_statistics_dict_buffer["outForwardedOctets"]["value"] = int(element_text)
                            interface_subinterface_statistics_dict_buffer["outForwardedOctets"]["observedAt"] = observed_at
                        if child_node == "out-originated-packets":
                            interface_subinterface_statistics_dict_buffer["outOriginatedPackets"] = {}
                            interface_subinterface_statistics_dict_buffer["outOriginatedPackets"]["type"] = "Property"
                            interface_subinterface_statistics_dict_buffer["outOriginatedPackets"]["value"] = int(element_text)
                            interface_subinterface_statistics_dict_buffer["outOriginatedPackets"]["observedAt"] = observed_at
                        if child_node == "out-originated-octets":
                            interface_subinterface_statistics_dict_buffer["outOriginatedOctets"] = {}
                            interface_subinterface_statistics_dict_buffer["outOriginatedOctets"]["type"] = "Property"
                            interface_subinterface_statistics_dict_buffer["outOriginatedOctets"]["value"] = int(element_text)
                            interface_subinterface_statistics_dict_buffer["outOriginatedOctets"]["observedAt"] = observed_at
                        if child_node == "out-error-packets":
                            interface_subinterface_statistics_dict_buffer["outErrorPackets"] = {}
                            interface_subinterface_statistics_dict_buffer["outErrorPackets"]["type"] = "Property"
                            interface_subinterface_statistics_dict_buffer["outErrorPackets"]["value"] = int(element_text)
                            interface_subinterface_statistics_dict_buffer["outErrorPackets"]["observedAt"] = observed_at
                        if child_node == "out-discarded-packets":
                            interface_subinterface_statistics_dict_buffer["outDiscardedPackets"] = {}
                            interface_subinterface_statistics_dict_buffer["outDiscardedPackets"]["type"] = "Property"
                            interface_subinterface_statistics_dict_buffer["outDiscardedPackets"]["value"] = int(element_text)
                            interface_subinterface_statistics_dict_buffer["outDiscardedPackets"]["observedAt"] = observed_at
                        if child_node == "out-packets":
                            interface_subinterface_statistics_dict_buffer["outPackets"] = {}
                            interface_subinterface_statistics_dict_buffer["outPackets"]["type"] = "Property"
                            interface_subinterface_statistics_dict_buffer["outPackets"]["value"] = int(element_text)
                            interface_subinterface_statistics_dict_buffer["outPackets"]["observedAt"] = observed_at
                        if child_node == "out-octets":
                            interface_subinterface_statistics_dict_buffer["outOctets"] = {}
                            interface_subinterface_statistics_dict_buffer["outOctets"]["type"] = "Property"
                            interface_subinterface_statistics_dict_buffer["outOctets"]["value"] = int(element_text)
                            interface_subinterface_statistics_dict_buffer["outOctets"]["observedAt"] = observed_at
                        if child_node == "last-clear":
                            interface_subinterface_statistics_dict_buffer["lastClear"] = {}
                            interface_subinterface_statistics_dict_buffer["lastClear"]["type"] = "Property"
                            interface_subinterface_statistics_dict_buffer["lastClear"]["value"] = element_text
                            interface_subinterface_statistics_dict_buffer["lastClear"]["observedAt"] = observed_at
                        if len(parent_path) - 1 == 2:
                            dict_buffers.append(interface_subinterface_statistics_dict_buffer)
                if parent_path[2] == "bridge-table":
                    interface_subinterface_bridge_table_dict_buffer = {}
                    interface_subinterface_bridge_table_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceBridgeTable:" + ":".join(interface_subinterface_dict_buffer["id"].split(":")[3:])
                    interface_subinterface_bridge_table_dict_buffer["type"] = "InterfaceSubinterfaceBridgeTable"
                    if len(parent_path) - 1 == 2 or len(parent_path) - 1 == 3:
                        interface_subinterface_bridge_table_dict_buffer["isPartOf"] = {}
                        interface_subinterface_bridge_table_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_subinterface_bridge_table_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                        interface_subinterface_bridge_table_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "discard-unknown-src-mac":
                            interface_subinterface_bridge_table_dict_buffer["discardUnknownSrcMac"] = {}
                            interface_subinterface_bridge_table_dict_buffer["discardUnknownSrcMac"]["type"] = "Property"
                            interface_subinterface_bridge_table_dict_buffer["discardUnknownSrcMac"]["value"] = eval(str(element_text).capitalize())
                            interface_subinterface_bridge_table_dict_buffer["discardUnknownSrcMac"]["observedAt"] = observed_at
                        if parent_path[3] == "mac-limit":
                            interface_subinterface_bridge_table_mac_limit_dict_buffer = {}
                            interface_subinterface_bridge_table_mac_limit_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceBridgeTableMacLimit:" + ":".join(interface_subinterface_bridge_table_dict_buffer["id"].split(":")[3:])
                            interface_subinterface_bridge_table_mac_limit_dict_buffer["type"] = "InterfaceSubinterfaceBridgeTableMacLimit"
                            if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                                interface_subinterface_bridge_table_mac_limit_dict_buffer["isPartOf"] = {}
                                interface_subinterface_bridge_table_mac_limit_dict_buffer["isPartOf"]["type"] = "Relationship"
                                interface_subinterface_bridge_table_mac_limit_dict_buffer["isPartOf"]["object"] = interface_subinterface_bridge_table_dict_buffer["id"]
                                interface_subinterface_bridge_table_mac_limit_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                if child_node == "maximum-entries":
                                    interface_subinterface_bridge_table_mac_limit_dict_buffer["maximumEntries"] = {}
                                    interface_subinterface_bridge_table_mac_limit_dict_buffer["maximumEntries"]["type"] = "Property"
                                    interface_subinterface_bridge_table_mac_limit_dict_buffer["maximumEntries"]["value"] = int(element_text)
                                    interface_subinterface_bridge_table_mac_limit_dict_buffer["maximumEntries"]["observedAt"] = observed_at
                                if child_node == "warning-threshold-pct":
                                    interface_subinterface_bridge_table_mac_limit_dict_buffer["warningThresholdPct"] = {}
                                    interface_subinterface_bridge_table_mac_limit_dict_buffer["warningThresholdPct"]["type"] = "Property"
                                    interface_subinterface_bridge_table_mac_limit_dict_buffer["warningThresholdPct"]["value"] = int(element_text)
                                    interface_subinterface_bridge_table_mac_limit_dict_buffer["warningThresholdPct"]["observedAt"] = observed_at
                                if len(parent_path) - 1 == 3:
                                    dict_buffers.append(interface_subinterface_bridge_table_mac_limit_dict_buffer)
                        if parent_path[3] == "mac-learning":
                            interface_subinterface_bridge_table_mac_learning_dict_buffer = {}
                            interface_subinterface_bridge_table_mac_learning_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceBridgeTableMacLearning:" + ":".join(interface_subinterface_bridge_table_dict_buffer["id"].split(":")[3:])
                            interface_subinterface_bridge_table_mac_learning_dict_buffer["type"] = "InterfaceSubinterfaceBridgeTableMacLearning"
                            if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                                interface_subinterface_bridge_table_mac_learning_dict_buffer["isPartOf"] = {}
                                interface_subinterface_bridge_table_mac_learning_dict_buffer["isPartOf"]["type"] = "Relationship"
                                interface_subinterface_bridge_table_mac_learning_dict_buffer["isPartOf"]["object"] = interface_subinterface_bridge_table_dict_buffer["id"]
                                interface_subinterface_bridge_table_mac_learning_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                if child_node == "admin-state":
                                    interface_subinterface_bridge_table_mac_learning_dict_buffer["adminState"] = {}
                                    interface_subinterface_bridge_table_mac_learning_dict_buffer["adminState"]["type"] = "Property"
                                    interface_subinterface_bridge_table_mac_learning_dict_buffer["adminState"]["value"] = element_text
                                    interface_subinterface_bridge_table_mac_learning_dict_buffer["adminState"]["observedAt"] = observed_at
                                if parent_path[4] == "aging":
                                    interface_subinterface_bridge_table_mac_learning_aging_dict_buffer = {}
                                    interface_subinterface_bridge_table_mac_learning_aging_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceBridgeTableMacLearningAging:" + ":".join(interface_subinterface_bridge_table_mac_learning_dict_buffer["id"].split(":")[3:])
                                    interface_subinterface_bridge_table_mac_learning_aging_dict_buffer["type"] = "InterfaceSubinterfaceBridgeTableMacLearningAging"
                                    if len(parent_path) - 1 == 4 or len(parent_path) - 1 == 5:
                                        interface_subinterface_bridge_table_mac_learning_aging_dict_buffer["isPartOf"] = {}
                                        interface_subinterface_bridge_table_mac_learning_aging_dict_buffer["isPartOf"]["type"] = "Relationship"
                                        interface_subinterface_bridge_table_mac_learning_aging_dict_buffer["isPartOf"]["object"] = interface_subinterface_bridge_table_mac_learning_dict_buffer["id"]
                                        interface_subinterface_bridge_table_mac_learning_aging_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                        if child_node == "admin-state":
                                            interface_subinterface_bridge_table_mac_learning_aging_dict_buffer["adminState"] = {}
                                            interface_subinterface_bridge_table_mac_learning_aging_dict_buffer["adminState"]["type"] = "Property"
                                            interface_subinterface_bridge_table_mac_learning_aging_dict_buffer["adminState"]["value"] = element_text
                                            interface_subinterface_bridge_table_mac_learning_aging_dict_buffer["adminState"]["observedAt"] = observed_at
                                        if len(parent_path) - 1 == 4:
                                            dict_buffers.append(interface_subinterface_bridge_table_mac_learning_aging_dict_buffer)
                                if len(parent_path) - 1 == 3:
                                    dict_buffers.append(interface_subinterface_bridge_table_mac_learning_dict_buffer)
                        if parent_path[3] == "mac-duplication":
                            interface_subinterface_bridge_table_mac_duplication_dict_buffer = {}
                            interface_subinterface_bridge_table_mac_duplication_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceBridgeTableMacDuplication:" + ":".join(interface_subinterface_bridge_table_dict_buffer["id"].split(":")[3:])
                            interface_subinterface_bridge_table_mac_duplication_dict_buffer["type"] = "InterfaceSubinterfaceBridgeTableMacDuplication"
                            if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                                interface_subinterface_bridge_table_mac_duplication_dict_buffer["isPartOf"] = {}
                                interface_subinterface_bridge_table_mac_duplication_dict_buffer["isPartOf"]["type"] = "Relationship"
                                interface_subinterface_bridge_table_mac_duplication_dict_buffer["isPartOf"]["object"] = interface_subinterface_bridge_table_dict_buffer["id"]
                                interface_subinterface_bridge_table_mac_duplication_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                if child_node == "action":
                                    interface_subinterface_bridge_table_mac_duplication_dict_buffer["action"] = {}
                                    interface_subinterface_bridge_table_mac_duplication_dict_buffer["action"]["type"] = "Property"
                                    interface_subinterface_bridge_table_mac_duplication_dict_buffer["action"]["value"] = element_text
                                    interface_subinterface_bridge_table_mac_duplication_dict_buffer["action"]["observedAt"] = observed_at
                                if len(parent_path) - 1 == 3:
                                    dict_buffers.append(interface_subinterface_bridge_table_mac_duplication_dict_buffer)
                        if parent_path[3] == "srl_nokia-interfaces-bridge-table-statistics:statistics":
                            interface_subinterface_bridge_table_statistics_dict_buffer = {}
                            interface_subinterface_bridge_table_statistics_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceBridgeTableStatistics:" + ":".join(interface_subinterface_bridge_table_dict_buffer["id"].split(":")[3:])
                            interface_subinterface_bridge_table_statistics_dict_buffer["type"] = "InterfaceSubinterfaceBridgeTableStatistics"
                            if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                                interface_subinterface_bridge_table_statistics_dict_buffer["isPartOf"] = {}
                                interface_subinterface_bridge_table_statistics_dict_buffer["isPartOf"]["type"] = "Relationship"
                                interface_subinterface_bridge_table_statistics_dict_buffer["isPartOf"]["object"] = interface_subinterface_bridge_table_dict_buffer["id"]
                                interface_subinterface_bridge_table_statistics_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                if child_node == "active-entries":
                                    interface_subinterface_bridge_table_statistics_dict_buffer["activeEntries"] = {}
                                    interface_subinterface_bridge_table_statistics_dict_buffer["activeEntries"]["type"] = "Property"
                                    interface_subinterface_bridge_table_statistics_dict_buffer["activeEntries"]["value"] = int(element_text)
                                    interface_subinterface_bridge_table_statistics_dict_buffer["activeEntries"]["observedAt"] = observed_at
                                if child_node == "total-entries":
                                    interface_subinterface_bridge_table_statistics_dict_buffer["totalEntries"] = {}
                                    interface_subinterface_bridge_table_statistics_dict_buffer["totalEntries"]["type"] = "Property"
                                    interface_subinterface_bridge_table_statistics_dict_buffer["totalEntries"]["value"] = int(element_text)
                                    interface_subinterface_bridge_table_statistics_dict_buffer["totalEntries"]["observedAt"] = observed_at
                                if child_node == "failed-entries":
                                    interface_subinterface_bridge_table_statistics_dict_buffer["failedEntries"] = {}
                                    interface_subinterface_bridge_table_statistics_dict_buffer["failedEntries"]["type"] = "Property"
                                    interface_subinterface_bridge_table_statistics_dict_buffer["failedEntries"]["value"] = int(element_text)
                                    interface_subinterface_bridge_table_statistics_dict_buffer["failedEntries"]["observedAt"] = observed_at
                                if parent_path[4] == "mac-type":
                                    interface_subinterface_bridge_table_statistics_mac_type_dict_buffer = {}
                                    if "interface_subinterface_bridge_table_statistics_mac_type_type" in iteration_keys:
                                        interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceBridgeTableStatisticsMacType:" + source + ":" + iteration_keys.get("interface_subinterface_bridge-table_statistics_mac-type_type")
                                    interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["type"] = "InterfaceSubinterfaceBridgeTableStatisticsMacType"
                                    if len(parent_path) - 1 == 4 or len(parent_path) - 1 == 5:
                                        interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["isPartOf"] = {}
                                        interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["isPartOf"]["type"] = "Relationship"
                                        interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["isPartOf"]["object"] = interface_subinterface_bridge_table_statistics_dict_buffer["id"]
                                        interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                        if child_node == "type":
                                            interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["type"] = {}
                                            interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["type"]["type"] = "Property"
                                            interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["type"]["value"] = element_text
                                            interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["type"]["observedAt"] = observed_at
                                        if child_node == "active-entries":
                                            interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["activeEntries"] = {}
                                            interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["activeEntries"]["type"] = "Property"
                                            interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["activeEntries"]["value"] = int(element_text)
                                            interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["activeEntries"]["observedAt"] = observed_at
                                        if child_node == "total-entries":
                                            interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["totalEntries"] = {}
                                            interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["totalEntries"]["type"] = "Property"
                                            interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["totalEntries"]["value"] = int(element_text)
                                            interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["totalEntries"]["observedAt"] = observed_at
                                        if child_node == "failed-entries":
                                            interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["failedEntries"] = {}
                                            interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["failedEntries"]["type"] = "Property"
                                            interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["failedEntries"]["value"] = int(element_text)
                                            interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["failedEntries"]["observedAt"] = observed_at
                                        if len(parent_path) - 1 == 4:
                                            dict_buffers.append(interface_subinterface_bridge_table_statistics_mac_type_dict_buffer)
                                if len(parent_path) - 1 == 3:
                                    dict_buffers.append(interface_subinterface_bridge_table_statistics_dict_buffer)
                        if len(parent_path) - 1 == 2:
                            dict_buffers.append(interface_subinterface_bridge_table_dict_buffer)
                if len(parent_path) - 1 == 1:
                    dict_buffers.append(interface_subinterface_dict_buffer)
        if parent_path[1] == "sflow":
            interface_sflow_dict_buffer = {}
            interface_sflow_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSflow:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
            interface_sflow_dict_buffer["type"] = "InterfaceSflow"
            if len(parent_path) - 1 == 1 or len(parent_path) - 1 == 2:
                interface_sflow_dict_buffer["isPartOf"] = {}
                interface_sflow_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_sflow_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                interface_sflow_dict_buffer["isPartOf"]["observedAt"] = observed_at
                if child_node == "admin-state":
                    interface_sflow_dict_buffer["adminState"] = {}
                    interface_sflow_dict_buffer["adminState"]["type"] = "Property"
                    interface_sflow_dict_buffer["adminState"]["value"] = element_text
                    interface_sflow_dict_buffer["adminState"]["observedAt"] = observed_at
                if len(parent_path) - 1 == 1:
                    dict_buffers.append(interface_sflow_dict_buffer)
        if len(parent_path) - 1 == 0:
            dict_buffers.append(interface_dict_buffer)
        if parent_path[0] == "srl_nokia-platform:platform" or parent_path[0] == "platform":
            if parent_path[1] == "srl_nokia-platform:platform" or parent_path[1] == "platform":
                if parent_path[2] == "linecard" or parent_path[2] == "srl_nokia-platform-lc:linecard":
                    linecard_dict_buffer = {}
                    if "linecard_slot" in iteration_keys:
                        linecard_dict_buffer["id"] = "urn:ngsi-ld:Linecard:" + source + ":" +  iteration_keys.get("linecard_slot")
                    linecard_dict_buffer["type"] = "Linecard"
                if child_node == "slot":
                    linecard_dict_buffer["slot"] = {}
                    linecard_dict_buffer["slot"]["type"] = "Property"
                    linecard_dict_buffer["slot"]["value"] = int(element_text)
                    linecard_dict_buffer["slot"]["observedAt"] = observed_at
                if child_node == "admin-state":
                    linecard_dict_buffer["adminState"] = {}
                    linecard_dict_buffer["adminState"]["type"] = "Property"
                    linecard_dict_buffer["adminState"]["value"] = element_text
                    linecard_dict_buffer["adminState"]["observedAt"] = observed_at
                if child_node == "oper-state":
                    linecard_dict_buffer["operState"] = {}
                    linecard_dict_buffer["operState"]["type"] = "Property"
                    linecard_dict_buffer["operState"]["value"] = element_text
                    linecard_dict_buffer["operState"]["observedAt"] = observed_at
                if child_node == "last-booted":
                    linecard_dict_buffer["lastBooted"] = {}
                    linecard_dict_buffer["lastBooted"]["type"] = "Property"
                    linecard_dict_buffer["lastBooted"]["value"] = element_text
                    linecard_dict_buffer["lastBooted"]["observedAt"] = observed_at
                if child_node == "last-change":
                    linecard_dict_buffer["lastChange"] = {}
                    linecard_dict_buffer["lastChange"]["type"] = "Property"
                    linecard_dict_buffer["lastChange"]["value"] = element_text
                    linecard_dict_buffer["lastChange"]["observedAt"] = observed_at
                if child_node == "part-number":
                    linecard_dict_buffer["partNumber"] = {}
                    linecard_dict_buffer["partNumber"]["type"] = "Property"
                    linecard_dict_buffer["partNumber"]["value"] = element_text
                    linecard_dict_buffer["partNumber"]["observedAt"] = observed_at
                if child_node == "removable":
                    linecard_dict_buffer["removable"] = {}
                    linecard_dict_buffer["removable"]["type"] = "Property"
                    linecard_dict_buffer["removable"]["value"] = eval(str(element_text).capitalize())
                    linecard_dict_buffer["removable"]["observedAt"] = observed_at
                if child_node == "failure-reason":
                    linecard_dict_buffer["failureReason"] = {}
                    linecard_dict_buffer["failureReason"]["type"] = "Property"
                    linecard_dict_buffer["failureReason"]["value"] = element_text
                    linecard_dict_buffer["failureReason"]["observedAt"] = observed_at
                if child_node == "clei-code":
                    linecard_dict_buffer["cleiCode"] = {}
                    linecard_dict_buffer["cleiCode"]["type"] = "Property"
                    linecard_dict_buffer["cleiCode"]["value"] = element_text
                    linecard_dict_buffer["cleiCode"]["observedAt"] = observed_at
                if child_node == "serial-number":
                    linecard_dict_buffer["serialNumber"] = {}
                    linecard_dict_buffer["serialNumber"]["type"] = "Property"
                    linecard_dict_buffer["serialNumber"]["value"] = element_text
                    linecard_dict_buffer["serialNumber"]["observedAt"] = observed_at
                if child_node == "manufactured-date":
                    linecard_dict_buffer["manufacturedDate"] = {}
                    linecard_dict_buffer["manufacturedDate"]["type"] = "Property"
                    linecard_dict_buffer["manufacturedDate"]["value"] = element_text
                    linecard_dict_buffer["manufacturedDate"]["observedAt"] = observed_at
                if parent_path[3] == "srl_nokia-platform-lc:bios":
                    linecard_bios_dict_buffer = {}
                    linecard_bios_dict_buffer["id"] = "urn:ngsi-ld:LinecardBios:" + ":".join(linecard_dict_buffer["id"].split(":")[3:])
                    linecard_bios_dict_buffer["type"] = "LinecardBios"
                    if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                        linecard_bios_dict_buffer["isPartOf"] = {}
                        linecard_bios_dict_buffer["isPartOf"]["type"] = "Relationship"
                        linecard_bios_dict_buffer["isPartOf"]["object"] = linecard_dict_buffer["id"]
                        linecard_bios_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "manufacturer":
                            linecard_bios_dict_buffer["manufacturer"] = {}
                            linecard_bios_dict_buffer["manufacturer"]["type"] = "Property"
                            linecard_bios_dict_buffer["manufacturer"]["value"] = element_text
                            linecard_bios_dict_buffer["manufacturer"]["observedAt"] = observed_at
                        if child_node == "software-version":
                            linecard_bios_dict_buffer["softwareVersion"] = {}
                            linecard_bios_dict_buffer["softwareVersion"]["type"] = "Property"
                            linecard_bios_dict_buffer["softwareVersion"]["value"] = element_text
                            linecard_bios_dict_buffer["softwareVersion"]["observedAt"] = observed_at
                        if len(parent_path) - 1 == 3:
                            dict_buffers.append(linecard_bios_dict_buffer)
                if child_node == "rebooting-at":
                    linecard_dict_buffer["rebootingAt"] = {}
                    linecard_dict_buffer["rebootingAt"]["type"] = "Property"
                    linecard_dict_buffer["rebootingAt"]["value"] = element_text
                    linecard_dict_buffer["rebootingAt"]["observedAt"] = observed_at
                if child_node == "type":
                    linecard_dict_buffer["type"] = {}
                    linecard_dict_buffer["type"]["type"] = "Property"
                    linecard_dict_buffer["type"]["value"] = element_text
                    linecard_dict_buffer["type"]["observedAt"] = observed_at
                if parent_path[3] == "srl_nokia-platform-lc:forwarding-complex":
                    linecard_forwarding_complex_dict_buffer = {}
                    if "linecard_forwarding_complex_name" in iteration_keys:
                        linecard_forwarding_complex_dict_buffer["id"] = "urn:ngsi-ld:LinecardForwardingComplex:" + source + ":" + iteration_keys.get("linecard_forwarding-complex_name")
                    linecard_forwarding_complex_dict_buffer["type"] = "LinecardForwardingComplex"
                    if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                        linecard_forwarding_complex_dict_buffer["isPartOf"] = {}
                        linecard_forwarding_complex_dict_buffer["isPartOf"]["type"] = "Relationship"
                        linecard_forwarding_complex_dict_buffer["isPartOf"]["object"] = linecard_dict_buffer["id"]
                        linecard_forwarding_complex_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "name":
                            if linecard_forwarding_complex_dict_buffer["id"].split(":")[-1] != element_text:
                                linecard_forwarding_complex_dict_buffer["id"] = linecard_forwarding_complex_dict_buffer["id"] + ":" + element_text
                            linecard_forwarding_complex_dict_buffer["name"] = {}
                            linecard_forwarding_complex_dict_buffer["name"]["type"] = "Property"
                            linecard_forwarding_complex_dict_buffer["name"]["value"] = element_text
                            linecard_forwarding_complex_dict_buffer["name"]["observedAt"] = observed_at
                        if child_node == "interfaces":
                            linecard_forwarding_complex_dict_buffer["interfaces"] = {}
                            linecard_forwarding_complex_dict_buffer["interfaces"]["type"] = "Property"
                            linecard_forwarding_complex_dict_buffer["interfaces"]["value"] = element_text
                            linecard_forwarding_complex_dict_buffer["interfaces"]["observedAt"] = observed_at
                        if child_node == "oper-state":
                            linecard_forwarding_complex_dict_buffer["operState"] = {}
                            linecard_forwarding_complex_dict_buffer["operState"]["type"] = "Property"
                            linecard_forwarding_complex_dict_buffer["operState"]["value"] = element_text
                            linecard_forwarding_complex_dict_buffer["operState"]["observedAt"] = observed_at
                        if child_node == "last-booted":
                            linecard_forwarding_complex_dict_buffer["lastBooted"] = {}
                            linecard_forwarding_complex_dict_buffer["lastBooted"]["type"] = "Property"
                            linecard_forwarding_complex_dict_buffer["lastBooted"]["value"] = element_text
                            linecard_forwarding_complex_dict_buffer["lastBooted"]["observedAt"] = observed_at
                        if child_node == "last-change":
                            linecard_forwarding_complex_dict_buffer["lastChange"] = {}
                            linecard_forwarding_complex_dict_buffer["lastChange"]["type"] = "Property"
                            linecard_forwarding_complex_dict_buffer["lastChange"]["value"] = element_text
                            linecard_forwarding_complex_dict_buffer["lastChange"]["observedAt"] = observed_at
                        if child_node == "part-number":
                            linecard_forwarding_complex_dict_buffer["partNumber"] = {}
                            linecard_forwarding_complex_dict_buffer["partNumber"]["type"] = "Property"
                            linecard_forwarding_complex_dict_buffer["partNumber"]["value"] = element_text
                            linecard_forwarding_complex_dict_buffer["partNumber"]["observedAt"] = observed_at
                        if child_node == "removable":
                            linecard_forwarding_complex_dict_buffer["removable"] = {}
                            linecard_forwarding_complex_dict_buffer["removable"]["type"] = "Property"
                            linecard_forwarding_complex_dict_buffer["removable"]["value"] = eval(str(element_text).capitalize())
                            linecard_forwarding_complex_dict_buffer["removable"]["observedAt"] = observed_at
                        if parent_path[4] == "fabric":
                            linecard_forwarding_complex_fabric_dict_buffer = {}
                            linecard_forwarding_complex_fabric_dict_buffer["id"] = "urn:ngsi-ld:LinecardForwardingComplexFabric:" + ":".join(linecard_forwarding_complex_dict_buffer["id"].split(":")[3:])
                            linecard_forwarding_complex_fabric_dict_buffer["type"] = "LinecardForwardingComplexFabric"
                            if len(parent_path) - 1 == 4 or len(parent_path) - 1 == 5:
                                linecard_forwarding_complex_fabric_dict_buffer["isPartOf"] = {}
                                linecard_forwarding_complex_fabric_dict_buffer["isPartOf"]["type"] = "Relationship"
                                linecard_forwarding_complex_fabric_dict_buffer["isPartOf"]["object"] = linecard_forwarding_complex_dict_buffer["id"]
                                linecard_forwarding_complex_fabric_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                if child_node == "availability":
                                    linecard_forwarding_complex_fabric_dict_buffer["availability"] = {}
                                    linecard_forwarding_complex_fabric_dict_buffer["availability"]["type"] = "Property"
                                    linecard_forwarding_complex_fabric_dict_buffer["availability"]["value"] = int(element_text)
                                    linecard_forwarding_complex_fabric_dict_buffer["availability"]["observedAt"] = observed_at
                                if child_node == "utilization-ingress":
                                    linecard_forwarding_complex_fabric_dict_buffer["utilizationIngress"] = {}
                                    linecard_forwarding_complex_fabric_dict_buffer["utilizationIngress"]["type"] = "Property"
                                    linecard_forwarding_complex_fabric_dict_buffer["utilizationIngress"]["value"] = int(element_text)
                                    linecard_forwarding_complex_fabric_dict_buffer["utilizationIngress"]["observedAt"] = observed_at
                                if child_node == "utilization-egress":
                                    linecard_forwarding_complex_fabric_dict_buffer["utilizationEgress"] = {}
                                    linecard_forwarding_complex_fabric_dict_buffer["utilizationEgress"]["type"] = "Property"
                                    linecard_forwarding_complex_fabric_dict_buffer["utilizationEgress"]["value"] = int(element_text)
                                    linecard_forwarding_complex_fabric_dict_buffer["utilizationEgress"]["observedAt"] = observed_at
                                if len(parent_path) - 1 == 4:
                                    dict_buffers.append(linecard_forwarding_complex_fabric_dict_buffer)
                        if parent_path[4] == "pipeline":
                            linecard_forwarding_complex_pipeline_dict_buffer = {}
                            if "linecard_forwarding_complex_pipeline_index" in iteration_keys:
                                linecard_forwarding_complex_pipeline_dict_buffer["id"] = "urn:ngsi-ld:LinecardForwardingComplexPipeline:" + source + ":" + iteration_keys.get("linecard_forwarding-complex_pipeline_index")
                            linecard_forwarding_complex_pipeline_dict_buffer["type"] = "LinecardForwardingComplexPipeline"
                            if len(parent_path) - 1 == 4 or len(parent_path) - 1 == 5:
                                linecard_forwarding_complex_pipeline_dict_buffer["isPartOf"] = {}
                                linecard_forwarding_complex_pipeline_dict_buffer["isPartOf"]["type"] = "Relationship"
                                linecard_forwarding_complex_pipeline_dict_buffer["isPartOf"]["object"] = linecard_forwarding_complex_dict_buffer["id"]
                                linecard_forwarding_complex_pipeline_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                if child_node == "index":
                                    if "." + str(element_text) not in linecard_forwarding_complex_pipeline_dict_buffer["id"].split(":")[-1]:
                                        linecard_forwarding_complex_pipeline_dict_buffer["id"] = linecard_forwarding_complex_pipeline_dict_buffer["id"] + "." + str(element_text)
                                    linecard_forwarding_complex_pipeline_dict_buffer["index"] = {}
                                    linecard_forwarding_complex_pipeline_dict_buffer["index"]["type"] = "Property"
                                    linecard_forwarding_complex_pipeline_dict_buffer["index"]["value"] = element_text
                                    linecard_forwarding_complex_pipeline_dict_buffer["index"]["observedAt"] = observed_at
                                if parent_path[5] == "pipeline-counters":
                                    if parent_path[6] == "host-interface-block":
                                        if parent_path[7] == "packet-extraction":
                                            linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer = {}
                                            linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["id"] = "urn:ngsi-ld:LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtraction:" + ":".join(linecard_forwarding_complex_pipeline_dict_buffer["id"].split(":")[3:])
                                            linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["type"] = "LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtraction"
                                            if len(parent_path) - 1 == 7 or len(parent_path) - 1 == 8:
                                                linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["isPartOf"] = {}
                                                linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["isPartOf"]["object"] = linecard_forwarding_complex_pipeline_dict_buffer["id"]
                                                linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                if child_node == "extracted-packets":
                                                    linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["extractedPackets"] = {}
                                                    linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["extractedPackets"]["type"] = "Property"
                                                    linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["extractedPackets"]["value"] = int(element_text)
                                                    linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["extractedPackets"]["observedAt"] = observed_at
                                                if child_node == "extracted-octets":
                                                    linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["extractedOctets"] = {}
                                                    linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["extractedOctets"]["type"] = "Property"
                                                    linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["extractedOctets"]["value"] = int(element_text)
                                                    linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["extractedOctets"]["observedAt"] = observed_at
                                                if parent_path[8] == "extraction-reason":
                                                    linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer = {}
                                                    if "linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_reason" in iteration_keys:
                                                        linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["id"] = "urn:ngsi-ld:LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtractionExtractionReason:" + source + ":" + iteration_keys.get("linecard_forwarding-complex_pipeline_packet-extraction_extraction-reason_reason")
                                                    linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["type"] = "LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtractionExtractionReason"
                                                    if len(parent_path) - 1 == 8 or len(parent_path) - 1 == 9:
                                                        linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["isPartOf"] = {}
                                                        linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["isPartOf"]["object"] = linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["id"]
                                                        linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                        if child_node == "extracted-packets":
                                                            linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["extractedPackets"] = {}
                                                            linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["extractedPackets"]["type"] = "Property"
                                                            linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["extractedPackets"]["value"] = int(element_text)
                                                            linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["extractedPackets"]["observedAt"] = observed_at
                                                        if child_node == "extracted-octets":
                                                            linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["extractedOctets"] = {}
                                                            linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["extractedOctets"]["type"] = "Property"
                                                            linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["extractedOctets"]["value"] = int(element_text)
                                                            linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["extractedOctets"]["observedAt"] = observed_at
                                                        if len(parent_path) - 1 == 8:
                                                            dict_buffers.append(linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer)
                                                if len(parent_path) - 1 == 7:
                                                    dict_buffers.append(linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer)
                                if len(parent_path) - 1 == 4:
                                    dict_buffers.append(linecard_forwarding_complex_pipeline_dict_buffer)
                        if len(parent_path) - 1 == 3:
                            dict_buffers.append(linecard_forwarding_complex_dict_buffer)
                if child_node == "software-version":
                    linecard_dict_buffer["softwareVersion"] = {}
                    linecard_dict_buffer["softwareVersion"]["type"] = "Property"
                    linecard_dict_buffer["softwareVersion"]["value"] = element_text
                    linecard_dict_buffer["softwareVersion"]["observedAt"] = observed_at
                if child_node == "locator-state":
                    linecard_dict_buffer["locatorState"] = {}
                    linecard_dict_buffer["locatorState"]["type"] = "Property"
                    linecard_dict_buffer["locatorState"]["value"] = element_text
                    linecard_dict_buffer["locatorState"]["observedAt"] = observed_at
                if parent_path[3] == "srl_nokia-platform-lc:power":
                    linecard_power_dict_buffer = {}
                    linecard_power_dict_buffer["id"] = "urn:ngsi-ld:LinecardPower:" + ":".join(linecard_dict_buffer["id"].split(":")[3:])
                    linecard_power_dict_buffer["type"] = "LinecardPower"
                    if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                        linecard_power_dict_buffer["isPartOf"] = {}
                        linecard_power_dict_buffer["isPartOf"]["type"] = "Relationship"
                        linecard_power_dict_buffer["isPartOf"]["object"] = linecard_dict_buffer["id"]
                        linecard_power_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "allocated":
                            linecard_power_dict_buffer["allocated"] = {}
                            linecard_power_dict_buffer["allocated"]["type"] = "Property"
                            linecard_power_dict_buffer["allocated"]["value"] = int(element_text)
                            linecard_power_dict_buffer["allocated"]["observedAt"] = observed_at
                        if child_node == "used":
                            linecard_power_dict_buffer["used"] = {}
                            linecard_power_dict_buffer["used"]["type"] = "Property"
                            linecard_power_dict_buffer["used"]["value"] = int(element_text)
                            linecard_power_dict_buffer["used"]["observedAt"] = observed_at
                        if child_node == "required":
                            linecard_power_dict_buffer["required"] = {}
                            linecard_power_dict_buffer["required"]["type"] = "Property"
                            linecard_power_dict_buffer["required"]["value"] = int(element_text)
                            linecard_power_dict_buffer["required"]["observedAt"] = observed_at
                        if len(parent_path) - 1 == 3:
                            dict_buffers.append(linecard_power_dict_buffer)
                if parent_path[3] == "srl_nokia-platform-lc:temperature":
                    linecard_temperature_dict_buffer = {}
                    linecard_temperature_dict_buffer["id"] = "urn:ngsi-ld:LinecardTemperature:" + ":".join(linecard_dict_buffer["id"].split(":")[3:])
                    linecard_temperature_dict_buffer["type"] = "LinecardTemperature"
                    if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                        linecard_temperature_dict_buffer["isPartOf"] = {}
                        linecard_temperature_dict_buffer["isPartOf"]["type"] = "Relationship"
                        linecard_temperature_dict_buffer["isPartOf"]["object"] = linecard_dict_buffer["id"]
                        linecard_temperature_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "instant":
                            linecard_temperature_dict_buffer["instant"] = {}
                            linecard_temperature_dict_buffer["instant"]["type"] = "Property"
                            linecard_temperature_dict_buffer["instant"]["value"] = int(element_text)
                            linecard_temperature_dict_buffer["instant"]["observedAt"] = observed_at
                        if child_node == "maximum":
                            linecard_temperature_dict_buffer["maximum"] = {}
                            linecard_temperature_dict_buffer["maximum"]["type"] = "Property"
                            linecard_temperature_dict_buffer["maximum"]["value"] = int(element_text)
                            linecard_temperature_dict_buffer["maximum"]["observedAt"] = observed_at
                        if child_node == "maximum-time":
                            linecard_temperature_dict_buffer["maximumTime"] = {}
                            linecard_temperature_dict_buffer["maximumTime"]["type"] = "Property"
                            linecard_temperature_dict_buffer["maximumTime"]["value"] = element_text
                            linecard_temperature_dict_buffer["maximumTime"]["observedAt"] = observed_at
                        if child_node == "alarm-status":
                            linecard_temperature_dict_buffer["alarmStatus"] = {}
                            linecard_temperature_dict_buffer["alarmStatus"]["type"] = "Property"
                            linecard_temperature_dict_buffer["alarmStatus"]["value"] = eval(str(element_text).capitalize())
                            linecard_temperature_dict_buffer["alarmStatus"]["observedAt"] = observed_at
                        if child_node == "margin":
                            linecard_temperature_dict_buffer["margin"] = {}
                            linecard_temperature_dict_buffer["margin"]["type"] = "Property"
                            linecard_temperature_dict_buffer["margin"]["value"] = int(element_text)
                            linecard_temperature_dict_buffer["margin"]["observedAt"] = observed_at
                        if len(parent_path) - 1 == 3:
                            dict_buffers.append(linecard_temperature_dict_buffer)
                if len(parent_path) - 1 == 2:
                    dict_buffers.append(linecard_dict_buffer)

dict_buffer_combinated = defaultdict(dict)
for dict_buffer in dict_buffers:
    key = (dict_buffer["id"], dict_buffer["type"])
    if key not in dict_buffer_combinated:
        dict_buffer_combinated[key] = dict_buffer
    else:
        dict_buffer_combinated[key].update(dict_buffer)
dict_buffers = list(dict_buffer_combinated.values())

print(json.dumps(dict_buffers[::-1], indent=4))
dict_buffers.clear()
