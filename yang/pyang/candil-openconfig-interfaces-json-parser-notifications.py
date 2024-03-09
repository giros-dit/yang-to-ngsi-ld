import json
import numpy as np
from collections import defaultdict
import sys

json_payload = sys.argv[1]
dict_buffers = []
parent_paths = []
child_nodes = []
values = []
iteration_keys = []

with open(json_payload) as f:
    data = json.load(f)
    timestamp_data = int(data[0]["timestamp"])
    observed_at = str(np.datetime64(timestamp_data, 'ns'))

for item in data:
    for key, value in item['values'].items():
        parent_paths.append(key.split("/")[1:-1])
        child_nodes.append(key.split("/")[-1])
        values.append(value)
        for i_key, i_value in item['tags'].items():
            if i_key != 'source' and i_key != 'subscription-name':
                iteration_key = {}
                iteration_key[i_key] = i_value
                iteration_keys.append(iteration_key)

for element_text, child_node, parent_path, iteration_key in zip(values, child_nodes, parent_paths, iteration_keys):
    if parent_path[0] == "openconfig-interfaces:interfaces" or parent_path[0] == "interfaces":
        if parent_path[1] == "interface":
            interface_dict_buffer = {}
            if iteration_key.get("interface_name"):
                interface_dict_buffer["id"] = "urn:ngsi-ld:Interface:" + iteration_key.get("interface_name")
            interface_dict_buffer["type"] = "Interface"
        if len(parent_path) - 1 == 1 or len(parent_path) - 1 == 2:
            if interface_dict_buffer["id"].split(":")[-1] != element_text:
                interface_dict_buffer["id"] = interface_dict_buffer["id"] + element_text
            interface_dict_buffer["name"] = {}
            interface_dict_buffer["name"]["type"] = "Relationship"
            interface_dict_buffer["name"]["object"] = "urn:ngsi-ld:InterfaceConfig:" + interface_dict_buffer["id"].split(":")[-1]
            interface_dict_buffer["name"]["observedAt"] = observed_at
        if parent_path[2] == "config":
            interface_config_dict_buffer = {}
            interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceConfig:" + interface_dict_buffer["id"].split(":")[-1]
            interface_config_dict_buffer["type"] = "InterfaceConfig"
            if len(parent_path) - 1 == 2 or len(parent_path) - 1 == 3:
                interface_config_dict_buffer["isPartOf"] = {}
                interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                if child_node == "name":
                    if interface_config_dict_buffer["id"].split(":")[-1] != element_text:
                        interface_config_dict_buffer["id"] = interface_config_dict_buffer["id"] + element_text
                    interface_config_dict_buffer["name"] = {}
                    interface_config_dict_buffer["name"]["type"] = "Property"
                    interface_config_dict_buffer["name"]["value"] = element_text
                    interface_config_dict_buffer["name"]["observedAt"] = observed_at
                if child_node == "mtu":
                    interface_config_dict_buffer["mtu"] = {}
                    interface_config_dict_buffer["mtu"]["type"] = "Property"
                    interface_config_dict_buffer["mtu"]["value"] = int(element_text)
                    interface_config_dict_buffer["mtu"]["observedAt"] = observed_at
                if child_node == "loopback-mode":
                    interface_config_dict_buffer["loopbackMode"] = {}
                    interface_config_dict_buffer["loopbackMode"]["type"] = "Property"
                    interface_config_dict_buffer["loopbackMode"]["value"] = eval(str(element_text).capitalize())
                    interface_config_dict_buffer["loopbackMode"]["observedAt"] = observed_at
                if child_node == "description":
                    interface_config_dict_buffer["description"] = {}
                    interface_config_dict_buffer["description"]["type"] = "Property"
                    interface_config_dict_buffer["description"]["value"] = element_text
                    interface_config_dict_buffer["description"]["observedAt"] = observed_at
                if child_node == "enabled":
                    interface_config_dict_buffer["enabled"] = {}
                    interface_config_dict_buffer["enabled"]["type"] = "Property"
                    interface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                    interface_config_dict_buffer["enabled"]["observedAt"] = observed_at
                if len(parent_path) - 1 == 2:
                    dict_buffers.append(interface_config_dict_buffer)
        if parent_path[2] == "state":
            interface_state_dict_buffer = {}
            interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceState:" + interface_dict_buffer["id"].split(":")[-1]
            interface_state_dict_buffer["type"] = "InterfaceState"
            if len(parent_path) - 1 == 2 or len(parent_path) - 1 == 3:
                interface_state_dict_buffer["isPartOf"] = {}
                interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                if child_node == "name":
                    if interface_state_dict_buffer["id"].split(":")[-1] != element_text:
                        interface_state_dict_buffer["id"] = interface_state_dict_buffer["id"] + element_text
                    interface_state_dict_buffer["name"] = {}
                    interface_state_dict_buffer["name"]["type"] = "Property"
                    interface_state_dict_buffer["name"]["value"] = element_text
                    interface_state_dict_buffer["name"]["observedAt"] = observed_at
                if child_node == "mtu":
                    interface_state_dict_buffer["mtu"] = {}
                    interface_state_dict_buffer["mtu"]["type"] = "Property"
                    interface_state_dict_buffer["mtu"]["value"] = int(element_text)
                    interface_state_dict_buffer["mtu"]["observedAt"] = observed_at
                if child_node == "loopback-mode":
                    interface_state_dict_buffer["loopbackMode"] = {}
                    interface_state_dict_buffer["loopbackMode"]["type"] = "Property"
                    interface_state_dict_buffer["loopbackMode"]["value"] = eval(str(element_text).capitalize())
                    interface_state_dict_buffer["loopbackMode"]["observedAt"] = observed_at
                if child_node == "description":
                    interface_state_dict_buffer["description"] = {}
                    interface_state_dict_buffer["description"]["type"] = "Property"
                    interface_state_dict_buffer["description"]["value"] = element_text
                    interface_state_dict_buffer["description"]["observedAt"] = observed_at
                if child_node == "enabled":
                    interface_state_dict_buffer["enabled"] = {}
                    interface_state_dict_buffer["enabled"]["type"] = "Property"
                    interface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                    interface_state_dict_buffer["enabled"]["observedAt"] = observed_at
                if child_node == "ifindex":
                    interface_state_dict_buffer["ifindex"] = {}
                    interface_state_dict_buffer["ifindex"]["type"] = "Property"
                    interface_state_dict_buffer["ifindex"]["value"] = int(element_text)
                    interface_state_dict_buffer["ifindex"]["observedAt"] = observed_at
                if child_node == "admin-status":
                    interface_state_dict_buffer["adminStatus"] = {}
                    interface_state_dict_buffer["adminStatus"]["type"] = "Property"
                    interface_state_dict_buffer["adminStatus"]["value"] = element_text
                    interface_state_dict_buffer["adminStatus"]["observedAt"] = observed_at
                if child_node == "oper-status":
                    interface_state_dict_buffer["operStatus"] = {}
                    interface_state_dict_buffer["operStatus"]["type"] = "Property"
                    interface_state_dict_buffer["operStatus"]["value"] = element_text
                    interface_state_dict_buffer["operStatus"]["observedAt"] = observed_at
                if child_node == "last-change":
                    interface_state_dict_buffer["lastChange"] = {}
                    interface_state_dict_buffer["lastChange"]["type"] = "Property"
                    interface_state_dict_buffer["lastChange"]["value"] = int(element_text)
                    interface_state_dict_buffer["lastChange"]["observedAt"] = observed_at
                if parent_path[3] == "counters":
                    interface_state_counters_dict_buffer = {}
                    interface_state_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceStateCounters:" + interface_state_dict_buffer["id"].split(":")[-1]
                    interface_state_counters_dict_buffer["type"] = "InterfaceStateCounters"
                    if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                        interface_state_counters_dict_buffer["isPartOf"] = {}
                        interface_state_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_state_counters_dict_buffer["isPartOf"]["object"] = interface_state_dict_buffer["id"]
                        interface_state_counters_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "in-octets":
                            interface_state_counters_dict_buffer["inOctets"] = {}
                            interface_state_counters_dict_buffer["inOctets"]["type"] = "Property"
                            interface_state_counters_dict_buffer["inOctets"]["value"] = int(element_text)
                            interface_state_counters_dict_buffer["inOctets"]["observedAt"] = observed_at
                        if child_node == "in-unicast-pkts":
                            interface_state_counters_dict_buffer["inUnicastPkts"] = {}
                            interface_state_counters_dict_buffer["inUnicastPkts"]["type"] = "Property"
                            interface_state_counters_dict_buffer["inUnicastPkts"]["value"] = int(element_text)
                            interface_state_counters_dict_buffer["inUnicastPkts"]["observedAt"] = observed_at
                        if child_node == "in-broadcast-pkts":
                            interface_state_counters_dict_buffer["inBroadcastPkts"] = {}
                            interface_state_counters_dict_buffer["inBroadcastPkts"]["type"] = "Property"
                            interface_state_counters_dict_buffer["inBroadcastPkts"]["value"] = int(element_text)
                            interface_state_counters_dict_buffer["inBroadcastPkts"]["observedAt"] = observed_at
                        if child_node == "in-multicast-pkts":
                            interface_state_counters_dict_buffer["inMulticastPkts"] = {}
                            interface_state_counters_dict_buffer["inMulticastPkts"]["type"] = "Property"
                            interface_state_counters_dict_buffer["inMulticastPkts"]["value"] = int(element_text)
                            interface_state_counters_dict_buffer["inMulticastPkts"]["observedAt"] = observed_at
                        if child_node == "in-discards":
                            interface_state_counters_dict_buffer["inDiscards"] = {}
                            interface_state_counters_dict_buffer["inDiscards"]["type"] = "Property"
                            interface_state_counters_dict_buffer["inDiscards"]["value"] = int(element_text)
                            interface_state_counters_dict_buffer["inDiscards"]["observedAt"] = observed_at
                        if child_node == "in-errors":
                            interface_state_counters_dict_buffer["inErrors"] = {}
                            interface_state_counters_dict_buffer["inErrors"]["type"] = "Property"
                            interface_state_counters_dict_buffer["inErrors"]["value"] = int(element_text)
                            interface_state_counters_dict_buffer["inErrors"]["observedAt"] = observed_at
                        if child_node == "in-unknown-protos":
                            interface_state_counters_dict_buffer["inUnknownProtos"] = {}
                            interface_state_counters_dict_buffer["inUnknownProtos"]["type"] = "Property"
                            interface_state_counters_dict_buffer["inUnknownProtos"]["value"] = int(element_text)
                            interface_state_counters_dict_buffer["inUnknownProtos"]["observedAt"] = observed_at
                        if child_node == "in-fcs-errors":
                            interface_state_counters_dict_buffer["inFcsErrors"] = {}
                            interface_state_counters_dict_buffer["inFcsErrors"]["type"] = "Property"
                            interface_state_counters_dict_buffer["inFcsErrors"]["value"] = int(element_text)
                            interface_state_counters_dict_buffer["inFcsErrors"]["observedAt"] = observed_at
                        if child_node == "out-octets":
                            interface_state_counters_dict_buffer["outOctets"] = {}
                            interface_state_counters_dict_buffer["outOctets"]["type"] = "Property"
                            interface_state_counters_dict_buffer["outOctets"]["value"] = int(element_text)
                            interface_state_counters_dict_buffer["outOctets"]["observedAt"] = observed_at
                        if child_node == "out-unicast-pkts":
                            interface_state_counters_dict_buffer["outUnicastPkts"] = {}
                            interface_state_counters_dict_buffer["outUnicastPkts"]["type"] = "Property"
                            interface_state_counters_dict_buffer["outUnicastPkts"]["value"] = int(element_text)
                            interface_state_counters_dict_buffer["outUnicastPkts"]["observedAt"] = observed_at
                        if child_node == "out-broadcast-pkts":
                            interface_state_counters_dict_buffer["outBroadcastPkts"] = {}
                            interface_state_counters_dict_buffer["outBroadcastPkts"]["type"] = "Property"
                            interface_state_counters_dict_buffer["outBroadcastPkts"]["value"] = int(element_text)
                            interface_state_counters_dict_buffer["outBroadcastPkts"]["observedAt"] = observed_at
                        if child_node == "out-multicast-pkts":
                            interface_state_counters_dict_buffer["outMulticastPkts"] = {}
                            interface_state_counters_dict_buffer["outMulticastPkts"]["type"] = "Property"
                            interface_state_counters_dict_buffer["outMulticastPkts"]["value"] = int(element_text)
                            interface_state_counters_dict_buffer["outMulticastPkts"]["observedAt"] = observed_at
                        if child_node == "out-discards":
                            interface_state_counters_dict_buffer["outDiscards"] = {}
                            interface_state_counters_dict_buffer["outDiscards"]["type"] = "Property"
                            interface_state_counters_dict_buffer["outDiscards"]["value"] = int(element_text)
                            interface_state_counters_dict_buffer["outDiscards"]["observedAt"] = observed_at
                        if child_node == "out-errors":
                            interface_state_counters_dict_buffer["outErrors"] = {}
                            interface_state_counters_dict_buffer["outErrors"]["type"] = "Property"
                            interface_state_counters_dict_buffer["outErrors"]["value"] = int(element_text)
                            interface_state_counters_dict_buffer["outErrors"]["observedAt"] = observed_at
                        if child_node == "carrier-transitions":
                            interface_state_counters_dict_buffer["carrierTransitions"] = {}
                            interface_state_counters_dict_buffer["carrierTransitions"]["type"] = "Property"
                            interface_state_counters_dict_buffer["carrierTransitions"]["value"] = int(element_text)
                            interface_state_counters_dict_buffer["carrierTransitions"]["observedAt"] = observed_at
                        if child_node == "last-clear":
                            interface_state_counters_dict_buffer["lastClear"] = {}
                            interface_state_counters_dict_buffer["lastClear"]["type"] = "Property"
                            interface_state_counters_dict_buffer["lastClear"]["value"] = int(element_text)
                            interface_state_counters_dict_buffer["lastClear"]["observedAt"] = observed_at
                        if len(parent_path) - 1 == 3:
                            dict_buffers.append(interface_state_counters_dict_buffer)
                if len(parent_path) - 1 == 2:
                    dict_buffers.append(interface_state_dict_buffer)
        if parent_path[2] == "hold-time":
            if parent_path[3] == "config":
                interface_config_dict_buffer = {}
                interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceHoldTimeConfig:" + interface_dict_buffer["id"].split(":")[-1]
                interface_config_dict_buffer["type"] = "InterfaceHoldTimeConfig"
                if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                    interface_config_dict_buffer["isPartOf"] = {}
                    interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                    interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    if child_node == "up":
                        interface_config_dict_buffer["up"] = {}
                        interface_config_dict_buffer["up"]["type"] = "Property"
                        interface_config_dict_buffer["up"]["value"] = int(element_text)
                        interface_config_dict_buffer["up"]["observedAt"] = observed_at
                    if child_node == "down":
                        interface_config_dict_buffer["down"] = {}
                        interface_config_dict_buffer["down"]["type"] = "Property"
                        interface_config_dict_buffer["down"]["value"] = int(element_text)
                        interface_config_dict_buffer["down"]["observedAt"] = observed_at
                    if len(parent_path) - 1 == 3:
                        dict_buffers.append(interface_config_dict_buffer)
                if parent_path[4] == "state":
                    interface_state_dict_buffer = {}
                    interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceHoldTimeState:" + interface_dict_buffer["id"].split(":")[-1]
                    interface_state_dict_buffer["type"] = "InterfaceHoldTimeState"
                    if len(parent_path) - 1 == 4 or len(parent_path) - 1 == 5:
                        interface_state_dict_buffer["isPartOf"] = {}
                        interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                        interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "up":
                            interface_state_dict_buffer["up"] = {}
                            interface_state_dict_buffer["up"]["type"] = "Property"
                            interface_state_dict_buffer["up"]["value"] = int(element_text)
                            interface_state_dict_buffer["up"]["observedAt"] = observed_at
                        if child_node == "down":
                            interface_state_dict_buffer["down"] = {}
                            interface_state_dict_buffer["down"]["type"] = "Property"
                            interface_state_dict_buffer["down"]["value"] = int(element_text)
                            interface_state_dict_buffer["down"]["observedAt"] = observed_at
                        if len(parent_path) - 1 == 4:
                            dict_buffers.append(interface_state_dict_buffer)
        if parent_path[2] == "subinterfaces":
            if parent_path[3] == "subinterface":
                interface_subinterface_dict_buffer = {}
                if iteration_key.get("interface_subinterface_index"):
                    interface_subinterface_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterface:" + iteration_key
                interface_subinterface_dict_buffer["type"] = "InterfaceSubinterfacesSubinterface"
                if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                    interface_subinterface_dict_buffer["isPartOf"] = {}
                    interface_subinterface_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_subinterface_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                    interface_subinterface_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                        if "." + str(element_text) not in interface_subinterface_dict_buffer["id"].split(":")[-1]:
                            interface_subinterface_dict_buffer["id"] = interface_subinterface_dict_buffer["id"] + "." + str(element_text)
                        interface_subinterface_dict_buffer["index"] = {}
                        interface_subinterface_dict_buffer["index"]["type"] = "Relationship"
                        interface_subinterface_dict_buffer["index"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceConfig:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                        interface_subinterface_dict_buffer["index"]["observedAt"] = observed_at
                    if parent_path[4] == "config":
                        interface_subinterface_config_dict_buffer = {}
                        interface_subinterface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceConfig:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                        interface_subinterface_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceConfig"
                        if len(parent_path) - 1 == 4 or len(parent_path) - 1 == 5:
                            interface_subinterface_config_dict_buffer["isPartOf"] = {}
                            interface_subinterface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                            interface_subinterface_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                            interface_subinterface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                            if child_node == "index":
                                if "." + str(element_text) not in interface_subinterface_config_dict_buffer["id"].split(":")[-1]:
                                    interface_subinterface_config_dict_buffer["id"] = interface_subinterface_config_dict_buffer["id"] + "." + str(element_text)
                                interface_subinterface_config_dict_buffer["index"] = {}
                                interface_subinterface_config_dict_buffer["index"]["type"] = "Property"
                                interface_subinterface_config_dict_buffer["index"]["value"] = int(element_text)
                                interface_subinterface_config_dict_buffer["index"]["observedAt"] = observed_at
                            if child_node == "description":
                                interface_subinterface_config_dict_buffer["description"] = {}
                                interface_subinterface_config_dict_buffer["description"]["type"] = "Property"
                                interface_subinterface_config_dict_buffer["description"]["value"] = element_text
                                interface_subinterface_config_dict_buffer["description"]["observedAt"] = observed_at
                            if child_node == "enabled":
                                interface_subinterface_config_dict_buffer["enabled"] = {}
                                interface_subinterface_config_dict_buffer["enabled"]["type"] = "Property"
                                interface_subinterface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                interface_subinterface_config_dict_buffer["enabled"]["observedAt"] = observed_at
                            if len(parent_path) - 1 == 4:
                                dict_buffers.append(interface_subinterface_config_dict_buffer)
                    if parent_path[4] == "state":
                        interface_subinterface_state_dict_buffer = {}
                        interface_subinterface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceState:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                        interface_subinterface_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceState"
                        if len(parent_path) - 1 == 4 or len(parent_path) - 1 == 5:
                            interface_subinterface_state_dict_buffer["isPartOf"] = {}
                            interface_subinterface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                            interface_subinterface_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                            interface_subinterface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                            if child_node == "index":
                                if "." + str(element_text) not in interface_subinterface_state_dict_buffer["id"].split(":")[-1]:
                                    interface_subinterface_state_dict_buffer["id"] = interface_subinterface_state_dict_buffer["id"] + "." + str(element_text)
                                interface_subinterface_state_dict_buffer["index"] = {}
                                interface_subinterface_state_dict_buffer["index"]["type"] = "Property"
                                interface_subinterface_state_dict_buffer["index"]["value"] = int(element_text)
                                interface_subinterface_state_dict_buffer["index"]["observedAt"] = observed_at
                            if child_node == "description":
                                interface_subinterface_state_dict_buffer["description"] = {}
                                interface_subinterface_state_dict_buffer["description"]["type"] = "Property"
                                interface_subinterface_state_dict_buffer["description"]["value"] = element_text
                                interface_subinterface_state_dict_buffer["description"]["observedAt"] = observed_at
                            if child_node == "enabled":
                                interface_subinterface_state_dict_buffer["enabled"] = {}
                                interface_subinterface_state_dict_buffer["enabled"]["type"] = "Property"
                                interface_subinterface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                interface_subinterface_state_dict_buffer["enabled"]["observedAt"] = observed_at
                            if child_node == "name":
                                if interface_subinterface_state_dict_buffer["id"].split(":")[-1] != element_text:
                                    interface_subinterface_state_dict_buffer["id"] = interface_subinterface_state_dict_buffer["id"] + element_text
                                interface_subinterface_state_dict_buffer["name"] = {}
                                interface_subinterface_state_dict_buffer["name"]["type"] = "Property"
                                interface_subinterface_state_dict_buffer["name"]["value"] = element_text
                                interface_subinterface_state_dict_buffer["name"]["observedAt"] = observed_at
                            if child_node == "ifindex":
                                interface_subinterface_state_dict_buffer["ifindex"] = {}
                                interface_subinterface_state_dict_buffer["ifindex"]["type"] = "Property"
                                interface_subinterface_state_dict_buffer["ifindex"]["value"] = int(element_text)
                                interface_subinterface_state_dict_buffer["ifindex"]["observedAt"] = observed_at
                            if child_node == "admin-status":
                                interface_subinterface_state_dict_buffer["adminStatus"] = {}
                                interface_subinterface_state_dict_buffer["adminStatus"]["type"] = "Property"
                                interface_subinterface_state_dict_buffer["adminStatus"]["value"] = element_text
                                interface_subinterface_state_dict_buffer["adminStatus"]["observedAt"] = observed_at
                            if child_node == "oper-status":
                                interface_subinterface_state_dict_buffer["operStatus"] = {}
                                interface_subinterface_state_dict_buffer["operStatus"]["type"] = "Property"
                                interface_subinterface_state_dict_buffer["operStatus"]["value"] = element_text
                                interface_subinterface_state_dict_buffer["operStatus"]["observedAt"] = observed_at
                            if child_node == "last-change":
                                interface_subinterface_state_dict_buffer["lastChange"] = {}
                                interface_subinterface_state_dict_buffer["lastChange"]["type"] = "Property"
                                interface_subinterface_state_dict_buffer["lastChange"]["value"] = int(element_text)
                                interface_subinterface_state_dict_buffer["lastChange"]["observedAt"] = observed_at
                            if parent_path[5] == "counters":
                                interface_subinterface_state_counters_dict_buffer = {}
                                interface_subinterface_state_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceStateCounters:" + interface_subinterface_state_dict_buffer["id"].split(":")[-1]
                                interface_subinterface_state_counters_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceStateCounters"
                                if len(parent_path) - 1 == 5 or len(parent_path) - 1 == 6:
                                    interface_subinterface_state_counters_dict_buffer["isPartOf"] = {}
                                    interface_subinterface_state_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                                    interface_subinterface_state_counters_dict_buffer["isPartOf"]["object"] = interface_subinterface_state_dict_buffer["id"]
                                    interface_subinterface_state_counters_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                    if child_node == "in-octets":
                                        interface_subinterface_state_counters_dict_buffer["inOctets"] = {}
                                        interface_subinterface_state_counters_dict_buffer["inOctets"]["type"] = "Property"
                                        interface_subinterface_state_counters_dict_buffer["inOctets"]["value"] = int(element_text)
                                        interface_subinterface_state_counters_dict_buffer["inOctets"]["observedAt"] = observed_at
                                    if child_node == "in-unicast-pkts":
                                        interface_subinterface_state_counters_dict_buffer["inUnicastPkts"] = {}
                                        interface_subinterface_state_counters_dict_buffer["inUnicastPkts"]["type"] = "Property"
                                        interface_subinterface_state_counters_dict_buffer["inUnicastPkts"]["value"] = int(element_text)
                                        interface_subinterface_state_counters_dict_buffer["inUnicastPkts"]["observedAt"] = observed_at
                                    if child_node == "in-broadcast-pkts":
                                        interface_subinterface_state_counters_dict_buffer["inBroadcastPkts"] = {}
                                        interface_subinterface_state_counters_dict_buffer["inBroadcastPkts"]["type"] = "Property"
                                        interface_subinterface_state_counters_dict_buffer["inBroadcastPkts"]["value"] = int(element_text)
                                        interface_subinterface_state_counters_dict_buffer["inBroadcastPkts"]["observedAt"] = observed_at
                                    if child_node == "in-multicast-pkts":
                                        interface_subinterface_state_counters_dict_buffer["inMulticastPkts"] = {}
                                        interface_subinterface_state_counters_dict_buffer["inMulticastPkts"]["type"] = "Property"
                                        interface_subinterface_state_counters_dict_buffer["inMulticastPkts"]["value"] = int(element_text)
                                        interface_subinterface_state_counters_dict_buffer["inMulticastPkts"]["observedAt"] = observed_at
                                    if child_node == "in-discards":
                                        interface_subinterface_state_counters_dict_buffer["inDiscards"] = {}
                                        interface_subinterface_state_counters_dict_buffer["inDiscards"]["type"] = "Property"
                                        interface_subinterface_state_counters_dict_buffer["inDiscards"]["value"] = int(element_text)
                                        interface_subinterface_state_counters_dict_buffer["inDiscards"]["observedAt"] = observed_at
                                    if child_node == "in-errors":
                                        interface_subinterface_state_counters_dict_buffer["inErrors"] = {}
                                        interface_subinterface_state_counters_dict_buffer["inErrors"]["type"] = "Property"
                                        interface_subinterface_state_counters_dict_buffer["inErrors"]["value"] = int(element_text)
                                        interface_subinterface_state_counters_dict_buffer["inErrors"]["observedAt"] = observed_at
                                    if child_node == "in-unknown-protos":
                                        interface_subinterface_state_counters_dict_buffer["inUnknownProtos"] = {}
                                        interface_subinterface_state_counters_dict_buffer["inUnknownProtos"]["type"] = "Property"
                                        interface_subinterface_state_counters_dict_buffer["inUnknownProtos"]["value"] = int(element_text)
                                        interface_subinterface_state_counters_dict_buffer["inUnknownProtos"]["observedAt"] = observed_at
                                    if child_node == "in-fcs-errors":
                                        interface_subinterface_state_counters_dict_buffer["inFcsErrors"] = {}
                                        interface_subinterface_state_counters_dict_buffer["inFcsErrors"]["type"] = "Property"
                                        interface_subinterface_state_counters_dict_buffer["inFcsErrors"]["value"] = int(element_text)
                                        interface_subinterface_state_counters_dict_buffer["inFcsErrors"]["observedAt"] = observed_at
                                    if child_node == "out-octets":
                                        interface_subinterface_state_counters_dict_buffer["outOctets"] = {}
                                        interface_subinterface_state_counters_dict_buffer["outOctets"]["type"] = "Property"
                                        interface_subinterface_state_counters_dict_buffer["outOctets"]["value"] = int(element_text)
                                        interface_subinterface_state_counters_dict_buffer["outOctets"]["observedAt"] = observed_at
                                    if child_node == "out-unicast-pkts":
                                        interface_subinterface_state_counters_dict_buffer["outUnicastPkts"] = {}
                                        interface_subinterface_state_counters_dict_buffer["outUnicastPkts"]["type"] = "Property"
                                        interface_subinterface_state_counters_dict_buffer["outUnicastPkts"]["value"] = int(element_text)
                                        interface_subinterface_state_counters_dict_buffer["outUnicastPkts"]["observedAt"] = observed_at
                                    if child_node == "out-broadcast-pkts":
                                        interface_subinterface_state_counters_dict_buffer["outBroadcastPkts"] = {}
                                        interface_subinterface_state_counters_dict_buffer["outBroadcastPkts"]["type"] = "Property"
                                        interface_subinterface_state_counters_dict_buffer["outBroadcastPkts"]["value"] = int(element_text)
                                        interface_subinterface_state_counters_dict_buffer["outBroadcastPkts"]["observedAt"] = observed_at
                                    if child_node == "out-multicast-pkts":
                                        interface_subinterface_state_counters_dict_buffer["outMulticastPkts"] = {}
                                        interface_subinterface_state_counters_dict_buffer["outMulticastPkts"]["type"] = "Property"
                                        interface_subinterface_state_counters_dict_buffer["outMulticastPkts"]["value"] = int(element_text)
                                        interface_subinterface_state_counters_dict_buffer["outMulticastPkts"]["observedAt"] = observed_at
                                    if child_node == "out-discards":
                                        interface_subinterface_state_counters_dict_buffer["outDiscards"] = {}
                                        interface_subinterface_state_counters_dict_buffer["outDiscards"]["type"] = "Property"
                                        interface_subinterface_state_counters_dict_buffer["outDiscards"]["value"] = int(element_text)
                                        interface_subinterface_state_counters_dict_buffer["outDiscards"]["observedAt"] = observed_at
                                    if child_node == "out-errors":
                                        interface_subinterface_state_counters_dict_buffer["outErrors"] = {}
                                        interface_subinterface_state_counters_dict_buffer["outErrors"]["type"] = "Property"
                                        interface_subinterface_state_counters_dict_buffer["outErrors"]["value"] = int(element_text)
                                        interface_subinterface_state_counters_dict_buffer["outErrors"]["observedAt"] = observed_at
                                    if child_node == "carrier-transitions":
                                        interface_subinterface_state_counters_dict_buffer["carrierTransitions"] = {}
                                        interface_subinterface_state_counters_dict_buffer["carrierTransitions"]["type"] = "Property"
                                        interface_subinterface_state_counters_dict_buffer["carrierTransitions"]["value"] = int(element_text)
                                        interface_subinterface_state_counters_dict_buffer["carrierTransitions"]["observedAt"] = observed_at
                                    if child_node == "last-clear":
                                        interface_subinterface_state_counters_dict_buffer["lastClear"] = {}
                                        interface_subinterface_state_counters_dict_buffer["lastClear"]["type"] = "Property"
                                        interface_subinterface_state_counters_dict_buffer["lastClear"]["value"] = int(element_text)
                                        interface_subinterface_state_counters_dict_buffer["lastClear"]["observedAt"] = observed_at
                                    if len(parent_path) - 1 == 5:
                                        dict_buffers.append(interface_subinterface_state_counters_dict_buffer)
                            if len(parent_path) - 1 == 4:
                                dict_buffers.append(interface_subinterface_state_dict_buffer)
                    if parent_path[4] == "openconfig-vlan:vlan" or parent_path[4] == "vlan":
                        if parent_path[5] == "config":
                            interface_subinterface_config_dict_buffer = {}
                            interface_subinterface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceVlanConfig:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                            interface_subinterface_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceVlanConfig"
                            if len(parent_path) - 1 == 5 or len(parent_path) - 1 == 6:
                                interface_subinterface_config_dict_buffer["isPartOf"] = {}
                                interface_subinterface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                interface_subinterface_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                interface_subinterface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                if child_node == "vlan-id":
                                    if interface_subinterface_config_dict_buffer["id"].split(":")[-1] != element_text:
                                        interface_subinterface_config_dict_buffer["id"] = interface_subinterface_config_dict_buffer["id"] + element_text
                                    interface_subinterface_config_dict_buffer["vlanId"] = {}
                                    interface_subinterface_config_dict_buffer["vlanId"]["type"] = "Property"
                                    interface_subinterface_config_dict_buffer["vlanId"]["value"] = element_text
                                    interface_subinterface_config_dict_buffer["vlanId"]["observedAt"] = observed_at
                                if len(parent_path) - 1 == 5:
                                    dict_buffers.append(interface_subinterface_config_dict_buffer)
                            if parent_path[6] == "state":
                                interface_subinterface_state_dict_buffer = {}
                                interface_subinterface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceVlanState:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                interface_subinterface_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceVlanState"
                                if len(parent_path) - 1 == 6 or len(parent_path) - 1 == 7:
                                    interface_subinterface_state_dict_buffer["isPartOf"] = {}
                                    interface_subinterface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                    interface_subinterface_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                    interface_subinterface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                    if child_node == "vlan-id":
                                        if interface_subinterface_state_dict_buffer["id"].split(":")[-1] != element_text:
                                            interface_subinterface_state_dict_buffer["id"] = interface_subinterface_state_dict_buffer["id"] + element_text
                                        interface_subinterface_state_dict_buffer["vlanId"] = {}
                                        interface_subinterface_state_dict_buffer["vlanId"]["type"] = "Property"
                                        interface_subinterface_state_dict_buffer["vlanId"]["value"] = element_text
                                        interface_subinterface_state_dict_buffer["vlanId"]["observedAt"] = observed_at
                                    if len(parent_path) - 1 == 6:
                                        dict_buffers.append(interface_subinterface_state_dict_buffer)
                    if parent_path[4] == "openconfig-if-ip:ipv4" or parent_path[4] == "ipv4":
                        if parent_path[5] == "addresses":
                            if parent_path[6] == "address":
                                interface_subinterface_address_dict_buffer = {}
                                if iteration_key.get("interface_subinterface_address_ip"):
                                    interface_subinterface_address_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddress:" + iteration_key
                                interface_subinterface_address_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4AddressesAddress"
                                if len(parent_path) - 1 == 6 or len(parent_path) - 1 == 7:
                                    interface_subinterface_address_dict_buffer["isPartOf"] = {}
                                    interface_subinterface_address_dict_buffer["isPartOf"]["type"] = "Relationship"
                                    interface_subinterface_address_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                    interface_subinterface_address_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                    if len(parent_path) - 1 == 6 or len(parent_path) - 1 == 7:
                                        if ":" in element_text:
                                            element_text = element_text.replace(":",".")
                                        if interface_subinterface_address_dict_buffer["id"].split(":")[-1] != element_text:
                                            interface_subinterface_address_dict_buffer["id"] = interface_subinterface_address_dict_buffer["id"] + ":" + element_text
                                        interface_subinterface_address_dict_buffer["ip"] = {}
                                        interface_subinterface_address_dict_buffer["ip"]["type"] = "Relationship"
                                        interface_subinterface_address_dict_buffer["ip"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressConfig:" + interface_subinterface_address_dict_buffer["id"].split(":")[-1]
                                        interface_subinterface_address_dict_buffer["ip"]["observedAt"] = observed_at
                                    if parent_path[7] == "config":
                                        interface_subinterface_address_config_dict_buffer = {}
                                        interface_subinterface_address_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressConfig:" + interface_subinterface_address_dict_buffer["id"].split(":")[-1]
                                        interface_subinterface_address_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressConfig"
                                        if len(parent_path) - 1 == 7 or len(parent_path) - 1 == 8:
                                            interface_subinterface_address_config_dict_buffer["isPartOf"] = {}
                                            interface_subinterface_address_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                            interface_subinterface_address_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_dict_buffer["id"]
                                            interface_subinterface_address_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                            if child_node == "ip":
                                                interface_subinterface_address_config_dict_buffer["ip"] = {}
                                                interface_subinterface_address_config_dict_buffer["ip"]["type"] = "Property"
                                                interface_subinterface_address_config_dict_buffer["ip"]["value"] = element_text
                                                interface_subinterface_address_config_dict_buffer["ip"]["observedAt"] = observed_at
                                            if child_node == "prefix-length":
                                                interface_subinterface_address_config_dict_buffer["prefixLength"] = {}
                                                interface_subinterface_address_config_dict_buffer["prefixLength"]["type"] = "Property"
                                                interface_subinterface_address_config_dict_buffer["prefixLength"]["value"] = int(element_text)
                                                interface_subinterface_address_config_dict_buffer["prefixLength"]["observedAt"] = observed_at
                                            if len(parent_path) - 1 == 7:
                                                dict_buffers.append(interface_subinterface_address_config_dict_buffer)
                                    if parent_path[7] == "state":
                                        interface_subinterface_address_state_dict_buffer = {}
                                        interface_subinterface_address_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressState:" + interface_subinterface_address_dict_buffer["id"].split(":")[-1]
                                        interface_subinterface_address_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressState"
                                        if len(parent_path) - 1 == 7 or len(parent_path) - 1 == 8:
                                            interface_subinterface_address_state_dict_buffer["isPartOf"] = {}
                                            interface_subinterface_address_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                            interface_subinterface_address_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_dict_buffer["id"]
                                            interface_subinterface_address_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                            if child_node == "ip":
                                                interface_subinterface_address_state_dict_buffer["ip"] = {}
                                                interface_subinterface_address_state_dict_buffer["ip"]["type"] = "Property"
                                                interface_subinterface_address_state_dict_buffer["ip"]["value"] = element_text
                                                interface_subinterface_address_state_dict_buffer["ip"]["observedAt"] = observed_at
                                            if child_node == "prefix-length":
                                                interface_subinterface_address_state_dict_buffer["prefixLength"] = {}
                                                interface_subinterface_address_state_dict_buffer["prefixLength"]["type"] = "Property"
                                                interface_subinterface_address_state_dict_buffer["prefixLength"]["value"] = int(element_text)
                                                interface_subinterface_address_state_dict_buffer["prefixLength"]["observedAt"] = observed_at
                                            if child_node == "origin":
                                                interface_subinterface_address_state_dict_buffer["origin"] = {}
                                                interface_subinterface_address_state_dict_buffer["origin"]["type"] = "Property"
                                                interface_subinterface_address_state_dict_buffer["origin"]["value"] = element_text
                                                interface_subinterface_address_state_dict_buffer["origin"]["observedAt"] = observed_at
                                            if len(parent_path) - 1 == 7:
                                                dict_buffers.append(interface_subinterface_address_state_dict_buffer)
                                    if parent_path[7] == "vrrp":
                                        if parent_path[8] == "vrrp-group":
                                            interface_subinterface_address_vrrp_group_dict_buffer = {}
                                            if iteration_key.get("interface_subinterface_address_vrrp-group_virtual-router-id"):
                                                interface_subinterface_address_vrrp_group_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroup:" + iteration_key
                                            interface_subinterface_address_vrrp_group_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroup"
                                            if len(parent_path) - 1 == 8 or len(parent_path) - 1 == 9:
                                                interface_subinterface_address_vrrp_group_dict_buffer["isPartOf"] = {}
                                                interface_subinterface_address_vrrp_group_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_subinterface_address_vrrp_group_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_dict_buffer["id"]
                                                interface_subinterface_address_vrrp_group_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                if len(parent_path) - 1 == 8 or len(parent_path) - 1 == 9:
                                                    if interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1] != element_text:
                                                        interface_subinterface_address_vrrp_group_dict_buffer["id"] = interface_subinterface_address_vrrp_group_dict_buffer["id"] + element_text
                                                    interface_subinterface_address_vrrp_group_dict_buffer["virtualRouterId"] = {}
                                                    interface_subinterface_address_vrrp_group_dict_buffer["virtualRouterId"]["type"] = "Relationship"
                                                    interface_subinterface_address_vrrp_group_dict_buffer["virtualRouterId"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupConfig:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                    interface_subinterface_address_vrrp_group_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                if parent_path[9] == "config":
                                                    interface_subinterface_address_vrrp_group_config_dict_buffer = {}
                                                    interface_subinterface_address_vrrp_group_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupConfig:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                    interface_subinterface_address_vrrp_group_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupConfig"
                                                    if len(parent_path) - 1 == 9 or len(parent_path) - 1 == 10:
                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"] = {}
                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_vrrp_group_dict_buffer["id"]
                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                        if child_node == "virtual-router-id":
                                                            if interface_subinterface_address_vrrp_group_config_dict_buffer["id"].split(":")[-1] != int(element_text):
                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["id"] = interface_subinterface_address_vrrp_group_config_dict_buffer["id"] + int(element_text)
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["virtualRouterId"] = {}
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["value"] = int(element_text)
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                        if child_node == "virtual-address":
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["virtualAddress"] = {}
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["virtualAddress"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["virtualAddress"]["value"] = element_text
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["virtualAddress"]["observedAt"] = observed_at
                                                        if child_node == "priority":
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["priority"] = {}
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["priority"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["priority"]["value"] = int(element_text)
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["priority"]["observedAt"] = observed_at
                                                        if child_node == "preempt":
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["preempt"] = {}
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["preempt"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["preempt"]["value"] = eval(str(element_text).capitalize())
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["preempt"]["observedAt"] = observed_at
                                                        if child_node == "preempt-delay":
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["preemptDelay"] = {}
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["preemptDelay"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["preemptDelay"]["value"] = int(element_text)
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["preemptDelay"]["observedAt"] = observed_at
                                                        if child_node == "accept-mode":
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["acceptMode"] = {}
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["acceptMode"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["acceptMode"]["value"] = eval(str(element_text).capitalize())
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["acceptMode"]["observedAt"] = observed_at
                                                        if child_node == "advertisement-interval":
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["advertisementInterval"] = {}
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["value"] = int(element_text)
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["observedAt"] = observed_at
                                                        if len(parent_path) - 1 == 9:
                                                            dict_buffers.append(interface_subinterface_address_vrrp_group_config_dict_buffer)
                                                if parent_path[9] == "state":
                                                    interface_subinterface_address_vrrp_group_state_dict_buffer = {}
                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupState:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupState"
                                                    if len(parent_path) - 1 == 9 or len(parent_path) - 1 == 10:
                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"] = {}
                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_vrrp_group_dict_buffer["id"]
                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                        if child_node == "virtual-router-id":
                                                            if interface_subinterface_address_vrrp_group_state_dict_buffer["id"].split(":")[-1] != int(element_text):
                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["id"] = interface_subinterface_address_vrrp_group_state_dict_buffer["id"] + int(element_text)
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["virtualRouterId"] = {}
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["value"] = int(element_text)
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                        if child_node == "virtual-address":
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["virtualAddress"] = {}
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["virtualAddress"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["virtualAddress"]["value"] = element_text
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["virtualAddress"]["observedAt"] = observed_at
                                                        if child_node == "priority":
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["priority"] = {}
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["priority"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["priority"]["value"] = int(element_text)
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["priority"]["observedAt"] = observed_at
                                                        if child_node == "preempt":
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["preempt"] = {}
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["preempt"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["preempt"]["value"] = eval(str(element_text).capitalize())
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["preempt"]["observedAt"] = observed_at
                                                        if child_node == "preempt-delay":
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["preemptDelay"] = {}
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["preemptDelay"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["preemptDelay"]["value"] = int(element_text)
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["preemptDelay"]["observedAt"] = observed_at
                                                        if child_node == "accept-mode":
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["acceptMode"] = {}
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["acceptMode"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["acceptMode"]["value"] = eval(str(element_text).capitalize())
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["acceptMode"]["observedAt"] = observed_at
                                                        if child_node == "advertisement-interval":
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["advertisementInterval"] = {}
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["value"] = int(element_text)
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["observedAt"] = observed_at
                                                        if child_node == "current-priority":
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["currentPriority"] = {}
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["currentPriority"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["currentPriority"]["value"] = int(element_text)
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["currentPriority"]["observedAt"] = observed_at
                                                        if len(parent_path) - 1 == 9:
                                                            dict_buffers.append(interface_subinterface_address_vrrp_group_state_dict_buffer)
                                                if parent_path[9] == "interface-tracking":
                                                    if parent_path[10] == "config":
                                                        interface_subinterface_address_vrrp_group_config_dict_buffer = {}
                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig"
                                                        if len(parent_path) - 1 == 10 or len(parent_path) - 1 == 11:
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"] = {}
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_vrrp_group_dict_buffer["id"]
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            if len(parent_path) - 1 == 10 or len(parent_path) - 1 == 11:
                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["trackInterface"] = {}
                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["trackInterface"]["type"] = "Relationship"
                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["trackInterface"]["object"] = "urn:ngsi-ld:Interface:" + interface_subinterface_address_vrrp_group_config_dict_buffer["id"].split(":")[-1]
                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["trackInterface"]["observedAt"] = observed_at
                                                            if child_node == "priority-decrement":
                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["priorityDecrement"] = {}
                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["type"] = "Property"
                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["value"] = int(element_text)
                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["observedAt"] = observed_at
                                                            if len(parent_path) - 1 == 10:
                                                                dict_buffers.append(interface_subinterface_address_vrrp_group_config_dict_buffer)
                                                        if parent_path[11] == "state":
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer = {}
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingState:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingState"
                                                            if len(parent_path) - 1 == 11 or len(parent_path) - 1 == 12:
                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"] = {}
                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_vrrp_group_dict_buffer["id"]
                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                if len(parent_path) - 1 == 11 or len(parent_path) - 1 == 12:
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["trackInterface"] = {}
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["trackInterface"]["type"] = "Relationship"
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["trackInterface"]["object"] = "urn:ngsi-ld:Interface:" + interface_subinterface_address_vrrp_group_state_dict_buffer["id"].split(":")[-1]
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["trackInterface"]["observedAt"] = observed_at
                                                                if child_node == "priority-decrement":
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["priorityDecrement"] = {}
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["type"] = "Property"
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["value"] = int(element_text)
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["observedAt"] = observed_at
                                                                if len(parent_path) - 1 == 11:
                                                                    dict_buffers.append(interface_subinterface_address_vrrp_group_state_dict_buffer)
                                                if len(parent_path) - 1 == 8:
                                                    dict_buffers.append(interface_subinterface_address_vrrp_group_dict_buffer)
                                    if len(parent_path) - 1 == 6:
                                        dict_buffers.append(interface_subinterface_address_dict_buffer)
                            if parent_path[6] == "proxy-arp":
                                if parent_path[7] == "config":
                                    interface_subinterface_config_dict_buffer = {}
                                    interface_subinterface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4ProxyArpConfig:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                    interface_subinterface_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4ProxyArpConfig"
                                    if len(parent_path) - 1 == 7 or len(parent_path) - 1 == 8:
                                        interface_subinterface_config_dict_buffer["isPartOf"] = {}
                                        interface_subinterface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                        interface_subinterface_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                        interface_subinterface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                        if child_node == "mode":
                                            interface_subinterface_config_dict_buffer["mode"] = {}
                                            interface_subinterface_config_dict_buffer["mode"]["type"] = "Property"
                                            interface_subinterface_config_dict_buffer["mode"]["value"] = element_text
                                            interface_subinterface_config_dict_buffer["mode"]["observedAt"] = observed_at
                                        if len(parent_path) - 1 == 7:
                                            dict_buffers.append(interface_subinterface_config_dict_buffer)
                                    if parent_path[8] == "state":
                                        interface_subinterface_state_dict_buffer = {}
                                        interface_subinterface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4ProxyArpState:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                        interface_subinterface_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4ProxyArpState"
                                        if len(parent_path) - 1 == 8 or len(parent_path) - 1 == 9:
                                            interface_subinterface_state_dict_buffer["isPartOf"] = {}
                                            interface_subinterface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                            interface_subinterface_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                            interface_subinterface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                            if child_node == "mode":
                                                interface_subinterface_state_dict_buffer["mode"] = {}
                                                interface_subinterface_state_dict_buffer["mode"]["type"] = "Property"
                                                interface_subinterface_state_dict_buffer["mode"]["value"] = element_text
                                                interface_subinterface_state_dict_buffer["mode"]["observedAt"] = observed_at
                                            if len(parent_path) - 1 == 8:
                                                dict_buffers.append(interface_subinterface_state_dict_buffer)
                                if parent_path[7] == "neighbors":
                                    if parent_path[8] == "neighbor":
                                        interface_subinterface_neighbor_dict_buffer = {}
                                        if iteration_key.get("interface_subinterface_neighbor_ip"):
                                            interface_subinterface_neighbor_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4NeighborsNeighbor:" + iteration_key
                                        interface_subinterface_neighbor_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4NeighborsNeighbor"
                                        if len(parent_path) - 1 == 8 or len(parent_path) - 1 == 9:
                                            interface_subinterface_neighbor_dict_buffer["isPartOf"] = {}
                                            interface_subinterface_neighbor_dict_buffer["isPartOf"]["type"] = "Relationship"
                                            interface_subinterface_neighbor_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                            interface_subinterface_neighbor_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                            if len(parent_path) - 1 == 8 or len(parent_path) - 1 == 9:
                                                if ":" in element_text:
                                                    element_text = element_text.replace(":",".")
                                                if interface_subinterface_neighbor_dict_buffer["id"].split(":")[-1] != element_text:
                                                    interface_subinterface_neighbor_dict_buffer["id"] = interface_subinterface_neighbor_dict_buffer["id"] + ":" + element_text
                                                interface_subinterface_neighbor_dict_buffer["ip"] = {}
                                                interface_subinterface_neighbor_dict_buffer["ip"]["type"] = "Relationship"
                                                interface_subinterface_neighbor_dict_buffer["ip"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4NeighborsNeighborConfig:" + interface_subinterface_neighbor_dict_buffer["id"].split(":")[-1]
                                                interface_subinterface_neighbor_dict_buffer["ip"]["observedAt"] = observed_at
                                            if parent_path[9] == "config":
                                                interface_subinterface_neighbor_config_dict_buffer = {}
                                                interface_subinterface_neighbor_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4NeighborsNeighborConfig:" + interface_subinterface_neighbor_dict_buffer["id"].split(":")[-1]
                                                interface_subinterface_neighbor_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4NeighborsNeighborConfig"
                                                if len(parent_path) - 1 == 9 or len(parent_path) - 1 == 10:
                                                    interface_subinterface_neighbor_config_dict_buffer["isPartOf"] = {}
                                                    interface_subinterface_neighbor_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_subinterface_neighbor_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_neighbor_dict_buffer["id"]
                                                    interface_subinterface_neighbor_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    if child_node == "ip":
                                                        interface_subinterface_neighbor_config_dict_buffer["ip"] = {}
                                                        interface_subinterface_neighbor_config_dict_buffer["ip"]["type"] = "Property"
                                                        interface_subinterface_neighbor_config_dict_buffer["ip"]["value"] = element_text
                                                        interface_subinterface_neighbor_config_dict_buffer["ip"]["observedAt"] = observed_at
                                                    if child_node == "link-layer-address":
                                                        interface_subinterface_neighbor_config_dict_buffer["linkLayerAddress"] = {}
                                                        interface_subinterface_neighbor_config_dict_buffer["linkLayerAddress"]["type"] = "Property"
                                                        interface_subinterface_neighbor_config_dict_buffer["linkLayerAddress"]["value"] = element_text
                                                        interface_subinterface_neighbor_config_dict_buffer["linkLayerAddress"]["observedAt"] = observed_at
                                                    if len(parent_path) - 1 == 9:
                                                        dict_buffers.append(interface_subinterface_neighbor_config_dict_buffer)
                                            if parent_path[9] == "state":
                                                interface_subinterface_neighbor_state_dict_buffer = {}
                                                interface_subinterface_neighbor_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4NeighborsNeighborState:" + interface_subinterface_neighbor_dict_buffer["id"].split(":")[-1]
                                                interface_subinterface_neighbor_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4NeighborsNeighborState"
                                                if len(parent_path) - 1 == 9 or len(parent_path) - 1 == 10:
                                                    interface_subinterface_neighbor_state_dict_buffer["isPartOf"] = {}
                                                    interface_subinterface_neighbor_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_subinterface_neighbor_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_neighbor_dict_buffer["id"]
                                                    interface_subinterface_neighbor_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    if child_node == "ip":
                                                        interface_subinterface_neighbor_state_dict_buffer["ip"] = {}
                                                        interface_subinterface_neighbor_state_dict_buffer["ip"]["type"] = "Property"
                                                        interface_subinterface_neighbor_state_dict_buffer["ip"]["value"] = element_text
                                                        interface_subinterface_neighbor_state_dict_buffer["ip"]["observedAt"] = observed_at
                                                    if child_node == "link-layer-address":
                                                        interface_subinterface_neighbor_state_dict_buffer["linkLayerAddress"] = {}
                                                        interface_subinterface_neighbor_state_dict_buffer["linkLayerAddress"]["type"] = "Property"
                                                        interface_subinterface_neighbor_state_dict_buffer["linkLayerAddress"]["value"] = element_text
                                                        interface_subinterface_neighbor_state_dict_buffer["linkLayerAddress"]["observedAt"] = observed_at
                                                    if child_node == "origin":
                                                        interface_subinterface_neighbor_state_dict_buffer["origin"] = {}
                                                        interface_subinterface_neighbor_state_dict_buffer["origin"]["type"] = "Property"
                                                        interface_subinterface_neighbor_state_dict_buffer["origin"]["value"] = element_text
                                                        interface_subinterface_neighbor_state_dict_buffer["origin"]["observedAt"] = observed_at
                                                    if len(parent_path) - 1 == 9:
                                                        dict_buffers.append(interface_subinterface_neighbor_state_dict_buffer)
                                            if len(parent_path) - 1 == 8:
                                                dict_buffers.append(interface_subinterface_neighbor_dict_buffer)
                                    if parent_path[8] == "unnumbered":
                                        if parent_path[9] == "config":
                                            interface_subinterface_config_dict_buffer = {}
                                            interface_subinterface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4UnnumberedConfig:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                            interface_subinterface_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4UnnumberedConfig"
                                            if len(parent_path) - 1 == 9 or len(parent_path) - 1 == 10:
                                                interface_subinterface_config_dict_buffer["isPartOf"] = {}
                                                interface_subinterface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_subinterface_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                interface_subinterface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                if child_node == "enabled":
                                                    interface_subinterface_config_dict_buffer["enabled"] = {}
                                                    interface_subinterface_config_dict_buffer["enabled"]["type"] = "Property"
                                                    interface_subinterface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                    interface_subinterface_config_dict_buffer["enabled"]["observedAt"] = observed_at
                                                if len(parent_path) - 1 == 9:
                                                    dict_buffers.append(interface_subinterface_config_dict_buffer)
                                            if parent_path[10] == "state":
                                                interface_subinterface_state_dict_buffer = {}
                                                interface_subinterface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4UnnumberedState:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                interface_subinterface_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4UnnumberedState"
                                                if len(parent_path) - 1 == 10 or len(parent_path) - 1 == 11:
                                                    interface_subinterface_state_dict_buffer["isPartOf"] = {}
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    if child_node == "enabled":
                                                        interface_subinterface_state_dict_buffer["enabled"] = {}
                                                        interface_subinterface_state_dict_buffer["enabled"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                        interface_subinterface_state_dict_buffer["enabled"]["observedAt"] = observed_at
                                                    if len(parent_path) - 1 == 10:
                                                        dict_buffers.append(interface_subinterface_state_dict_buffer)
                                                if parent_path[11] == "interface-ref":
                                                    if parent_path[12] == "config":
                                                        interface_subinterface_config_dict_buffer = {}
                                                        interface_subinterface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4UnnumberedInterfaceRefConfig:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                        interface_subinterface_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4UnnumberedInterfaceRefConfig"
                                                        if len(parent_path) - 1 == 12 or len(parent_path) - 1 == 13:
                                                            interface_subinterface_config_dict_buffer["isPartOf"] = {}
                                                            interface_subinterface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_subinterface_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                            interface_subinterface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            if len(parent_path) - 1 == 12 or len(parent_path) - 1 == 13:
                                                                if interface_subinterface_config_dict_buffer["id"].split(":")[-1] != element_text:
                                                                    interface_subinterface_config_dict_buffer["id"] = interface_subinterface_config_dict_buffer["id"] + element_text
                                                                interface_subinterface_config_dict_buffer["interface"] = {}
                                                                interface_subinterface_config_dict_buffer["interface"]["type"] = "Relationship"
                                                                interface_subinterface_config_dict_buffer["interface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4UnnumberedInterfaceRefConfigInterface:" + interface_subinterface_config_dict_buffer["id"].split(":")[-1]
                                                                interface_subinterface_config_dict_buffer["interface"]["observedAt"] = observed_at
                                                            if len(parent_path) - 1 == 12 or len(parent_path) - 1 == 13:
                                                                if "." + str(element_text) not in interface_subinterface_config_dict_buffer["id"].split(":")[-1]:
                                                                    interface_subinterface_config_dict_buffer["id"] = interface_subinterface_config_dict_buffer["id"] + "." + str(element_text)
                                                                interface_subinterface_config_dict_buffer["subinterface"] = {}
                                                                interface_subinterface_config_dict_buffer["subinterface"]["type"] = "Relationship"
                                                                interface_subinterface_config_dict_buffer["subinterface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4UnnumberedInterfaceRefConfigSubinterface:" + interface_subinterface_config_dict_buffer["id"].split(":")[-1]
                                                                interface_subinterface_config_dict_buffer["subinterface"]["observedAt"] = observed_at
                                                            if len(parent_path) - 1 == 12:
                                                                dict_buffers.append(interface_subinterface_config_dict_buffer)
                                                        if parent_path[13] == "state":
                                                            interface_subinterface_state_dict_buffer = {}
                                                            interface_subinterface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4UnnumberedInterfaceRefState:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                            interface_subinterface_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4UnnumberedInterfaceRefState"
                                                            if len(parent_path) - 1 == 13 or len(parent_path) - 1 == 14:
                                                                interface_subinterface_state_dict_buffer["isPartOf"] = {}
                                                                interface_subinterface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                interface_subinterface_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                                interface_subinterface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                if len(parent_path) - 1 == 13 or len(parent_path) - 1 == 14:
                                                                    if interface_subinterface_state_dict_buffer["id"].split(":")[-1] != element_text:
                                                                        interface_subinterface_state_dict_buffer["id"] = interface_subinterface_state_dict_buffer["id"] + element_text
                                                                    interface_subinterface_state_dict_buffer["interface"] = {}
                                                                    interface_subinterface_state_dict_buffer["interface"]["type"] = "Relationship"
                                                                    interface_subinterface_state_dict_buffer["interface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4UnnumberedInterfaceRefStateInterface:" + interface_subinterface_state_dict_buffer["id"].split(":")[-1]
                                                                    interface_subinterface_state_dict_buffer["interface"]["observedAt"] = observed_at
                                                                if len(parent_path) - 1 == 13 or len(parent_path) - 1 == 14:
                                                                    if "." + str(element_text) not in interface_subinterface_state_dict_buffer["id"].split(":")[-1]:
                                                                        interface_subinterface_state_dict_buffer["id"] = interface_subinterface_state_dict_buffer["id"] + "." + str(element_text)
                                                                    interface_subinterface_state_dict_buffer["subinterface"] = {}
                                                                    interface_subinterface_state_dict_buffer["subinterface"]["type"] = "Relationship"
                                                                    interface_subinterface_state_dict_buffer["subinterface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4UnnumberedInterfaceRefStateSubinterface:" + interface_subinterface_state_dict_buffer["id"].split(":")[-1]
                                                                    interface_subinterface_state_dict_buffer["subinterface"]["observedAt"] = observed_at
                                                                if len(parent_path) - 1 == 13:
                                                                    dict_buffers.append(interface_subinterface_state_dict_buffer)
                                        if parent_path[9] == "config":
                                            interface_subinterface_config_dict_buffer = {}
                                            interface_subinterface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4Config:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                            interface_subinterface_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4Config"
                                            if len(parent_path) - 1 == 9 or len(parent_path) - 1 == 10:
                                                interface_subinterface_config_dict_buffer["isPartOf"] = {}
                                                interface_subinterface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_subinterface_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                interface_subinterface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                if child_node == "enabled":
                                                    interface_subinterface_config_dict_buffer["enabled"] = {}
                                                    interface_subinterface_config_dict_buffer["enabled"]["type"] = "Property"
                                                    interface_subinterface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                    interface_subinterface_config_dict_buffer["enabled"]["observedAt"] = observed_at
                                                if child_node == "mtu":
                                                    interface_subinterface_config_dict_buffer["mtu"] = {}
                                                    interface_subinterface_config_dict_buffer["mtu"]["type"] = "Property"
                                                    interface_subinterface_config_dict_buffer["mtu"]["value"] = int(element_text)
                                                    interface_subinterface_config_dict_buffer["mtu"]["observedAt"] = observed_at
                                                if child_node == "dhcp-client":
                                                    interface_subinterface_config_dict_buffer["dhcpClient"] = {}
                                                    interface_subinterface_config_dict_buffer["dhcpClient"]["type"] = "Property"
                                                    interface_subinterface_config_dict_buffer["dhcpClient"]["value"] = eval(str(element_text).capitalize())
                                                    interface_subinterface_config_dict_buffer["dhcpClient"]["observedAt"] = observed_at
                                                if len(parent_path) - 1 == 9:
                                                    dict_buffers.append(interface_subinterface_config_dict_buffer)
                                            if parent_path[10] == "state":
                                                interface_subinterface_state_dict_buffer = {}
                                                interface_subinterface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4State:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                interface_subinterface_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4State"
                                                if len(parent_path) - 1 == 10 or len(parent_path) - 1 == 11:
                                                    interface_subinterface_state_dict_buffer["isPartOf"] = {}
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    if child_node == "enabled":
                                                        interface_subinterface_state_dict_buffer["enabled"] = {}
                                                        interface_subinterface_state_dict_buffer["enabled"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                        interface_subinterface_state_dict_buffer["enabled"]["observedAt"] = observed_at
                                                    if child_node == "mtu":
                                                        interface_subinterface_state_dict_buffer["mtu"] = {}
                                                        interface_subinterface_state_dict_buffer["mtu"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["mtu"]["value"] = int(element_text)
                                                        interface_subinterface_state_dict_buffer["mtu"]["observedAt"] = observed_at
                                                    if child_node == "dhcp-client":
                                                        interface_subinterface_state_dict_buffer["dhcpClient"] = {}
                                                        interface_subinterface_state_dict_buffer["dhcpClient"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["dhcpClient"]["value"] = eval(str(element_text).capitalize())
                                                        interface_subinterface_state_dict_buffer["dhcpClient"]["observedAt"] = observed_at
                                                    if parent_path[11] == "counters":
                                                        interface_subinterface_state_counters_dict_buffer = {}
                                                        interface_subinterface_state_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4StateCounters:" + interface_subinterface_state_dict_buffer["id"].split(":")[-1]
                                                        interface_subinterface_state_counters_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4StateCounters"
                                                        if len(parent_path) - 1 == 11 or len(parent_path) - 1 == 12:
                                                            interface_subinterface_state_counters_dict_buffer["isPartOf"] = {}
                                                            interface_subinterface_state_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_subinterface_state_counters_dict_buffer["isPartOf"]["object"] = interface_subinterface_state_dict_buffer["id"]
                                                            interface_subinterface_state_counters_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            if child_node == "in-pkts":
                                                                interface_subinterface_state_counters_dict_buffer["inPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inPkts"]["observedAt"] = observed_at
                                                            if child_node == "in-octets":
                                                                interface_subinterface_state_counters_dict_buffer["inOctets"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inOctets"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inOctets"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inOctets"]["observedAt"] = observed_at
                                                            if child_node == "in-error-pkts":
                                                                interface_subinterface_state_counters_dict_buffer["inErrorPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inErrorPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inErrorPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inErrorPkts"]["observedAt"] = observed_at
                                                            if child_node == "in-forwarded-pkts":
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedPkts"]["observedAt"] = observed_at
                                                            if child_node == "in-forwarded-octets":
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedOctets"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedOctets"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedOctets"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedOctets"]["observedAt"] = observed_at
                                                            if child_node == "in-discarded-pkts":
                                                                interface_subinterface_state_counters_dict_buffer["inDiscardedPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inDiscardedPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inDiscardedPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inDiscardedPkts"]["observedAt"] = observed_at
                                                            if child_node == "out-pkts":
                                                                interface_subinterface_state_counters_dict_buffer["outPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outPkts"]["observedAt"] = observed_at
                                                            if child_node == "out-octets":
                                                                interface_subinterface_state_counters_dict_buffer["outOctets"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outOctets"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outOctets"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outOctets"]["observedAt"] = observed_at
                                                            if child_node == "out-error-pkts":
                                                                interface_subinterface_state_counters_dict_buffer["outErrorPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outErrorPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outErrorPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outErrorPkts"]["observedAt"] = observed_at
                                                            if child_node == "out-forwarded-pkts":
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedPkts"]["observedAt"] = observed_at
                                                            if child_node == "out-forwarded-octets":
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedOctets"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedOctets"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedOctets"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedOctets"]["observedAt"] = observed_at
                                                            if child_node == "out-discarded-pkts":
                                                                interface_subinterface_state_counters_dict_buffer["outDiscardedPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outDiscardedPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outDiscardedPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outDiscardedPkts"]["observedAt"] = observed_at
                                                            if len(parent_path) - 1 == 11:
                                                                dict_buffers.append(interface_subinterface_state_counters_dict_buffer)
                                                    if len(parent_path) - 1 == 10:
                                                        dict_buffers.append(interface_subinterface_state_dict_buffer)
                    if parent_path[4] == "openconfig-if-ip:ipv6" or parent_path[4] == "ipv6":
                        if parent_path[5] == "addresses":
                            if parent_path[6] == "address":
                                interface_subinterface_address_dict_buffer = {}
                                if iteration_key.get("interface_subinterface_address_ip"):
                                    interface_subinterface_address_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddress:" + iteration_key
                                interface_subinterface_address_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6AddressesAddress"
                                if len(parent_path) - 1 == 6 or len(parent_path) - 1 == 7:
                                    interface_subinterface_address_dict_buffer["isPartOf"] = {}
                                    interface_subinterface_address_dict_buffer["isPartOf"]["type"] = "Relationship"
                                    interface_subinterface_address_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                    interface_subinterface_address_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                    if len(parent_path) - 1 == 6 or len(parent_path) - 1 == 7:
                                        if ":" in element_text:
                                            element_text = element_text.replace(":",".")
                                        if interface_subinterface_address_dict_buffer["id"].split(":")[-1] != element_text:
                                            interface_subinterface_address_dict_buffer["id"] = interface_subinterface_address_dict_buffer["id"] + ":" + element_text
                                        interface_subinterface_address_dict_buffer["ip"] = {}
                                        interface_subinterface_address_dict_buffer["ip"]["type"] = "Relationship"
                                        interface_subinterface_address_dict_buffer["ip"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressConfig:" + interface_subinterface_address_dict_buffer["id"].split(":")[-1]
                                        interface_subinterface_address_dict_buffer["ip"]["observedAt"] = observed_at
                                    if parent_path[7] == "config":
                                        interface_subinterface_address_config_dict_buffer = {}
                                        interface_subinterface_address_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressConfig:" + interface_subinterface_address_dict_buffer["id"].split(":")[-1]
                                        interface_subinterface_address_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressConfig"
                                        if len(parent_path) - 1 == 7 or len(parent_path) - 1 == 8:
                                            interface_subinterface_address_config_dict_buffer["isPartOf"] = {}
                                            interface_subinterface_address_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                            interface_subinterface_address_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_dict_buffer["id"]
                                            interface_subinterface_address_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                            if child_node == "ip":
                                                interface_subinterface_address_config_dict_buffer["ip"] = {}
                                                interface_subinterface_address_config_dict_buffer["ip"]["type"] = "Property"
                                                interface_subinterface_address_config_dict_buffer["ip"]["value"] = element_text
                                                interface_subinterface_address_config_dict_buffer["ip"]["observedAt"] = observed_at
                                            if child_node == "prefix-length":
                                                interface_subinterface_address_config_dict_buffer["prefixLength"] = {}
                                                interface_subinterface_address_config_dict_buffer["prefixLength"]["type"] = "Property"
                                                interface_subinterface_address_config_dict_buffer["prefixLength"]["value"] = int(element_text)
                                                interface_subinterface_address_config_dict_buffer["prefixLength"]["observedAt"] = observed_at
                                            if len(parent_path) - 1 == 7:
                                                dict_buffers.append(interface_subinterface_address_config_dict_buffer)
                                    if parent_path[7] == "state":
                                        interface_subinterface_address_state_dict_buffer = {}
                                        interface_subinterface_address_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressState:" + interface_subinterface_address_dict_buffer["id"].split(":")[-1]
                                        interface_subinterface_address_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressState"
                                        if len(parent_path) - 1 == 7 or len(parent_path) - 1 == 8:
                                            interface_subinterface_address_state_dict_buffer["isPartOf"] = {}
                                            interface_subinterface_address_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                            interface_subinterface_address_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_dict_buffer["id"]
                                            interface_subinterface_address_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                            if child_node == "ip":
                                                interface_subinterface_address_state_dict_buffer["ip"] = {}
                                                interface_subinterface_address_state_dict_buffer["ip"]["type"] = "Property"
                                                interface_subinterface_address_state_dict_buffer["ip"]["value"] = element_text
                                                interface_subinterface_address_state_dict_buffer["ip"]["observedAt"] = observed_at
                                            if child_node == "prefix-length":
                                                interface_subinterface_address_state_dict_buffer["prefixLength"] = {}
                                                interface_subinterface_address_state_dict_buffer["prefixLength"]["type"] = "Property"
                                                interface_subinterface_address_state_dict_buffer["prefixLength"]["value"] = int(element_text)
                                                interface_subinterface_address_state_dict_buffer["prefixLength"]["observedAt"] = observed_at
                                            if child_node == "origin":
                                                interface_subinterface_address_state_dict_buffer["origin"] = {}
                                                interface_subinterface_address_state_dict_buffer["origin"]["type"] = "Property"
                                                interface_subinterface_address_state_dict_buffer["origin"]["value"] = element_text
                                                interface_subinterface_address_state_dict_buffer["origin"]["observedAt"] = observed_at
                                            if child_node == "status":
                                                interface_subinterface_address_state_dict_buffer["status"] = {}
                                                interface_subinterface_address_state_dict_buffer["status"]["type"] = "Property"
                                                interface_subinterface_address_state_dict_buffer["status"]["value"] = element_text
                                                interface_subinterface_address_state_dict_buffer["status"]["observedAt"] = observed_at
                                            if len(parent_path) - 1 == 7:
                                                dict_buffers.append(interface_subinterface_address_state_dict_buffer)
                                    if parent_path[7] == "vrrp":
                                        if parent_path[8] == "vrrp-group":
                                            interface_subinterface_address_vrrp_group_dict_buffer = {}
                                            if iteration_key.get("interface_subinterface_address_vrrp-group_virtual-router-id"):
                                                interface_subinterface_address_vrrp_group_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroup:" + iteration_key
                                            interface_subinterface_address_vrrp_group_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroup"
                                            if len(parent_path) - 1 == 8 or len(parent_path) - 1 == 9:
                                                interface_subinterface_address_vrrp_group_dict_buffer["isPartOf"] = {}
                                                interface_subinterface_address_vrrp_group_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_subinterface_address_vrrp_group_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_dict_buffer["id"]
                                                interface_subinterface_address_vrrp_group_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                if len(parent_path) - 1 == 8 or len(parent_path) - 1 == 9:
                                                    if interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1] != element_text:
                                                        interface_subinterface_address_vrrp_group_dict_buffer["id"] = interface_subinterface_address_vrrp_group_dict_buffer["id"] + element_text
                                                    interface_subinterface_address_vrrp_group_dict_buffer["virtualRouterId"] = {}
                                                    interface_subinterface_address_vrrp_group_dict_buffer["virtualRouterId"]["type"] = "Relationship"
                                                    interface_subinterface_address_vrrp_group_dict_buffer["virtualRouterId"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfig:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                    interface_subinterface_address_vrrp_group_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                if parent_path[9] == "config":
                                                    interface_subinterface_address_vrrp_group_config_dict_buffer = {}
                                                    interface_subinterface_address_vrrp_group_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfig:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                    interface_subinterface_address_vrrp_group_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfig"
                                                    if len(parent_path) - 1 == 9 or len(parent_path) - 1 == 10:
                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"] = {}
                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_vrrp_group_dict_buffer["id"]
                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                        if child_node == "virtual-router-id":
                                                            if interface_subinterface_address_vrrp_group_config_dict_buffer["id"].split(":")[-1] != int(element_text):
                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["id"] = interface_subinterface_address_vrrp_group_config_dict_buffer["id"] + int(element_text)
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["virtualRouterId"] = {}
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["value"] = int(element_text)
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                        if child_node == "virtual-address":
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["virtualAddress"] = {}
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["virtualAddress"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["virtualAddress"]["value"] = element_text
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["virtualAddress"]["observedAt"] = observed_at
                                                        if child_node == "priority":
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["priority"] = {}
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["priority"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["priority"]["value"] = int(element_text)
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["priority"]["observedAt"] = observed_at
                                                        if child_node == "preempt":
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["preempt"] = {}
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["preempt"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["preempt"]["value"] = eval(str(element_text).capitalize())
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["preempt"]["observedAt"] = observed_at
                                                        if child_node == "preempt-delay":
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["preemptDelay"] = {}
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["preemptDelay"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["preemptDelay"]["value"] = int(element_text)
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["preemptDelay"]["observedAt"] = observed_at
                                                        if child_node == "accept-mode":
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["acceptMode"] = {}
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["acceptMode"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["acceptMode"]["value"] = eval(str(element_text).capitalize())
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["acceptMode"]["observedAt"] = observed_at
                                                        if child_node == "advertisement-interval":
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["advertisementInterval"] = {}
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["value"] = int(element_text)
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["observedAt"] = observed_at
                                                        if child_node == "virtual-link-local":
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["virtualLinkLocal"] = {}
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["virtualLinkLocal"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["virtualLinkLocal"]["value"] = element_text
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["virtualLinkLocal"]["observedAt"] = observed_at
                                                        if len(parent_path) - 1 == 9:
                                                            dict_buffers.append(interface_subinterface_address_vrrp_group_config_dict_buffer)
                                                if parent_path[9] == "state":
                                                    interface_subinterface_address_vrrp_group_state_dict_buffer = {}
                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupState:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupState"
                                                    if len(parent_path) - 1 == 9 or len(parent_path) - 1 == 10:
                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"] = {}
                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_vrrp_group_dict_buffer["id"]
                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                        if child_node == "virtual-router-id":
                                                            if interface_subinterface_address_vrrp_group_state_dict_buffer["id"].split(":")[-1] != int(element_text):
                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["id"] = interface_subinterface_address_vrrp_group_state_dict_buffer["id"] + int(element_text)
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["virtualRouterId"] = {}
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["value"] = int(element_text)
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                        if child_node == "virtual-address":
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["virtualAddress"] = {}
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["virtualAddress"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["virtualAddress"]["value"] = element_text
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["virtualAddress"]["observedAt"] = observed_at
                                                        if child_node == "priority":
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["priority"] = {}
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["priority"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["priority"]["value"] = int(element_text)
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["priority"]["observedAt"] = observed_at
                                                        if child_node == "preempt":
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["preempt"] = {}
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["preempt"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["preempt"]["value"] = eval(str(element_text).capitalize())
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["preempt"]["observedAt"] = observed_at
                                                        if child_node == "preempt-delay":
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["preemptDelay"] = {}
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["preemptDelay"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["preemptDelay"]["value"] = int(element_text)
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["preemptDelay"]["observedAt"] = observed_at
                                                        if child_node == "accept-mode":
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["acceptMode"] = {}
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["acceptMode"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["acceptMode"]["value"] = eval(str(element_text).capitalize())
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["acceptMode"]["observedAt"] = observed_at
                                                        if child_node == "advertisement-interval":
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["advertisementInterval"] = {}
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["value"] = int(element_text)
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["observedAt"] = observed_at
                                                        if child_node == "current-priority":
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["currentPriority"] = {}
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["currentPriority"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["currentPriority"]["value"] = int(element_text)
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["currentPriority"]["observedAt"] = observed_at
                                                        if child_node == "virtual-link-local":
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["virtualLinkLocal"] = {}
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["virtualLinkLocal"]["type"] = "Property"
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["virtualLinkLocal"]["value"] = element_text
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["virtualLinkLocal"]["observedAt"] = observed_at
                                                        if len(parent_path) - 1 == 9:
                                                            dict_buffers.append(interface_subinterface_address_vrrp_group_state_dict_buffer)
                                                if parent_path[9] == "interface-tracking":
                                                    if parent_path[10] == "config":
                                                        interface_subinterface_address_vrrp_group_config_dict_buffer = {}
                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig"
                                                        if len(parent_path) - 1 == 10 or len(parent_path) - 1 == 11:
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"] = {}
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_vrrp_group_dict_buffer["id"]
                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            if len(parent_path) - 1 == 10 or len(parent_path) - 1 == 11:
                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["trackInterface"] = {}
                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["trackInterface"]["type"] = "Relationship"
                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["trackInterface"]["object"] = "urn:ngsi-ld:Interface:" + interface_subinterface_address_vrrp_group_config_dict_buffer["id"].split(":")[-1]
                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["trackInterface"]["observedAt"] = observed_at
                                                            if child_node == "priority-decrement":
                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["priorityDecrement"] = {}
                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["type"] = "Property"
                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["value"] = int(element_text)
                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["observedAt"] = observed_at
                                                            if len(parent_path) - 1 == 10:
                                                                dict_buffers.append(interface_subinterface_address_vrrp_group_config_dict_buffer)
                                                        if parent_path[11] == "state":
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer = {}
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupInterfaceTrackingState:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupInterfaceTrackingState"
                                                            if len(parent_path) - 1 == 11 or len(parent_path) - 1 == 12:
                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"] = {}
                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_vrrp_group_dict_buffer["id"]
                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                if len(parent_path) - 1 == 11 or len(parent_path) - 1 == 12:
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["trackInterface"] = {}
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["trackInterface"]["type"] = "Relationship"
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["trackInterface"]["object"] = "urn:ngsi-ld:Interface:" + interface_subinterface_address_vrrp_group_state_dict_buffer["id"].split(":")[-1]
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["trackInterface"]["observedAt"] = observed_at
                                                                if child_node == "priority-decrement":
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["priorityDecrement"] = {}
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["type"] = "Property"
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["value"] = int(element_text)
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["observedAt"] = observed_at
                                                                if len(parent_path) - 1 == 11:
                                                                    dict_buffers.append(interface_subinterface_address_vrrp_group_state_dict_buffer)
                                                if len(parent_path) - 1 == 8:
                                                    dict_buffers.append(interface_subinterface_address_vrrp_group_dict_buffer)
                                    if len(parent_path) - 1 == 6:
                                        dict_buffers.append(interface_subinterface_address_dict_buffer)
                            if parent_path[6] == "router-advertisement":
                                if parent_path[7] == "config":
                                    interface_subinterface_config_dict_buffer = {}
                                    interface_subinterface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6RouterAdvertisementConfig:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                    interface_subinterface_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6RouterAdvertisementConfig"
                                    if len(parent_path) - 1 == 7 or len(parent_path) - 1 == 8:
                                        interface_subinterface_config_dict_buffer["isPartOf"] = {}
                                        interface_subinterface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                        interface_subinterface_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                        interface_subinterface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                        if child_node == "interval":
                                            interface_subinterface_config_dict_buffer["interval"] = {}
                                            interface_subinterface_config_dict_buffer["interval"]["type"] = "Property"
                                            interface_subinterface_config_dict_buffer["interval"]["value"] = int(element_text)
                                            interface_subinterface_config_dict_buffer["interval"]["observedAt"] = observed_at
                                        if child_node == "lifetime":
                                            interface_subinterface_config_dict_buffer["lifetime"] = {}
                                            interface_subinterface_config_dict_buffer["lifetime"]["type"] = "Property"
                                            interface_subinterface_config_dict_buffer["lifetime"]["value"] = int(element_text)
                                            interface_subinterface_config_dict_buffer["lifetime"]["observedAt"] = observed_at
                                        if child_node == "suppress":
                                            interface_subinterface_config_dict_buffer["suppress"] = {}
                                            interface_subinterface_config_dict_buffer["suppress"]["type"] = "Property"
                                            interface_subinterface_config_dict_buffer["suppress"]["value"] = eval(str(element_text).capitalize())
                                            interface_subinterface_config_dict_buffer["suppress"]["observedAt"] = observed_at
                                        if len(parent_path) - 1 == 7:
                                            dict_buffers.append(interface_subinterface_config_dict_buffer)
                                    if parent_path[8] == "state":
                                        interface_subinterface_state_dict_buffer = {}
                                        interface_subinterface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6RouterAdvertisementState:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                        interface_subinterface_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6RouterAdvertisementState"
                                        if len(parent_path) - 1 == 8 or len(parent_path) - 1 == 9:
                                            interface_subinterface_state_dict_buffer["isPartOf"] = {}
                                            interface_subinterface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                            interface_subinterface_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                            interface_subinterface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                            if child_node == "interval":
                                                interface_subinterface_state_dict_buffer["interval"] = {}
                                                interface_subinterface_state_dict_buffer["interval"]["type"] = "Property"
                                                interface_subinterface_state_dict_buffer["interval"]["value"] = int(element_text)
                                                interface_subinterface_state_dict_buffer["interval"]["observedAt"] = observed_at
                                            if child_node == "lifetime":
                                                interface_subinterface_state_dict_buffer["lifetime"] = {}
                                                interface_subinterface_state_dict_buffer["lifetime"]["type"] = "Property"
                                                interface_subinterface_state_dict_buffer["lifetime"]["value"] = int(element_text)
                                                interface_subinterface_state_dict_buffer["lifetime"]["observedAt"] = observed_at
                                            if child_node == "suppress":
                                                interface_subinterface_state_dict_buffer["suppress"] = {}
                                                interface_subinterface_state_dict_buffer["suppress"]["type"] = "Property"
                                                interface_subinterface_state_dict_buffer["suppress"]["value"] = eval(str(element_text).capitalize())
                                                interface_subinterface_state_dict_buffer["suppress"]["observedAt"] = observed_at
                                            if len(parent_path) - 1 == 8:
                                                dict_buffers.append(interface_subinterface_state_dict_buffer)
                                if parent_path[7] == "neighbors":
                                    if parent_path[8] == "neighbor":
                                        interface_subinterface_neighbor_dict_buffer = {}
                                        if iteration_key.get("interface_subinterface_neighbor_ip"):
                                            interface_subinterface_neighbor_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighbor:" + iteration_key
                                        interface_subinterface_neighbor_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighbor"
                                        if len(parent_path) - 1 == 8 or len(parent_path) - 1 == 9:
                                            interface_subinterface_neighbor_dict_buffer["isPartOf"] = {}
                                            interface_subinterface_neighbor_dict_buffer["isPartOf"]["type"] = "Relationship"
                                            interface_subinterface_neighbor_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                            interface_subinterface_neighbor_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                            if len(parent_path) - 1 == 8 or len(parent_path) - 1 == 9:
                                                if ":" in element_text:
                                                    element_text = element_text.replace(":",".")
                                                if interface_subinterface_neighbor_dict_buffer["id"].split(":")[-1] != element_text:
                                                    interface_subinterface_neighbor_dict_buffer["id"] = interface_subinterface_neighbor_dict_buffer["id"] + ":" + element_text
                                                interface_subinterface_neighbor_dict_buffer["ip"] = {}
                                                interface_subinterface_neighbor_dict_buffer["ip"]["type"] = "Relationship"
                                                interface_subinterface_neighbor_dict_buffer["ip"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborConfig:" + interface_subinterface_neighbor_dict_buffer["id"].split(":")[-1]
                                                interface_subinterface_neighbor_dict_buffer["ip"]["observedAt"] = observed_at
                                            if parent_path[9] == "config":
                                                interface_subinterface_neighbor_config_dict_buffer = {}
                                                interface_subinterface_neighbor_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborConfig:" + interface_subinterface_neighbor_dict_buffer["id"].split(":")[-1]
                                                interface_subinterface_neighbor_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborConfig"
                                                if len(parent_path) - 1 == 9 or len(parent_path) - 1 == 10:
                                                    interface_subinterface_neighbor_config_dict_buffer["isPartOf"] = {}
                                                    interface_subinterface_neighbor_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_subinterface_neighbor_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_neighbor_dict_buffer["id"]
                                                    interface_subinterface_neighbor_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    if child_node == "ip":
                                                        interface_subinterface_neighbor_config_dict_buffer["ip"] = {}
                                                        interface_subinterface_neighbor_config_dict_buffer["ip"]["type"] = "Property"
                                                        interface_subinterface_neighbor_config_dict_buffer["ip"]["value"] = element_text
                                                        interface_subinterface_neighbor_config_dict_buffer["ip"]["observedAt"] = observed_at
                                                    if child_node == "link-layer-address":
                                                        interface_subinterface_neighbor_config_dict_buffer["linkLayerAddress"] = {}
                                                        interface_subinterface_neighbor_config_dict_buffer["linkLayerAddress"]["type"] = "Property"
                                                        interface_subinterface_neighbor_config_dict_buffer["linkLayerAddress"]["value"] = element_text
                                                        interface_subinterface_neighbor_config_dict_buffer["linkLayerAddress"]["observedAt"] = observed_at
                                                    if len(parent_path) - 1 == 9:
                                                        dict_buffers.append(interface_subinterface_neighbor_config_dict_buffer)
                                            if parent_path[9] == "state":
                                                interface_subinterface_neighbor_state_dict_buffer = {}
                                                interface_subinterface_neighbor_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborState:" + interface_subinterface_neighbor_dict_buffer["id"].split(":")[-1]
                                                interface_subinterface_neighbor_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborState"
                                                if len(parent_path) - 1 == 9 or len(parent_path) - 1 == 10:
                                                    interface_subinterface_neighbor_state_dict_buffer["isPartOf"] = {}
                                                    interface_subinterface_neighbor_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_subinterface_neighbor_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_neighbor_dict_buffer["id"]
                                                    interface_subinterface_neighbor_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    if child_node == "ip":
                                                        interface_subinterface_neighbor_state_dict_buffer["ip"] = {}
                                                        interface_subinterface_neighbor_state_dict_buffer["ip"]["type"] = "Property"
                                                        interface_subinterface_neighbor_state_dict_buffer["ip"]["value"] = element_text
                                                        interface_subinterface_neighbor_state_dict_buffer["ip"]["observedAt"] = observed_at
                                                    if child_node == "link-layer-address":
                                                        interface_subinterface_neighbor_state_dict_buffer["linkLayerAddress"] = {}
                                                        interface_subinterface_neighbor_state_dict_buffer["linkLayerAddress"]["type"] = "Property"
                                                        interface_subinterface_neighbor_state_dict_buffer["linkLayerAddress"]["value"] = element_text
                                                        interface_subinterface_neighbor_state_dict_buffer["linkLayerAddress"]["observedAt"] = observed_at
                                                    if child_node == "origin":
                                                        interface_subinterface_neighbor_state_dict_buffer["origin"] = {}
                                                        interface_subinterface_neighbor_state_dict_buffer["origin"]["type"] = "Property"
                                                        interface_subinterface_neighbor_state_dict_buffer["origin"]["value"] = element_text
                                                        interface_subinterface_neighbor_state_dict_buffer["origin"]["observedAt"] = observed_at
                                                    if child_node == "is-router":
                                                        interface_subinterface_neighbor_state_dict_buffer["isRouter"] = {}
                                                        interface_subinterface_neighbor_state_dict_buffer["isRouter"]["type"] = "Property"
                                                        interface_subinterface_neighbor_state_dict_buffer["isRouter"]["value"] = element_text
                                                        interface_subinterface_neighbor_state_dict_buffer["isRouter"]["observedAt"] = observed_at
                                                    if child_node == "neighbor-state":
                                                        interface_subinterface_neighbor_state_dict_buffer["neighborState"] = {}
                                                        interface_subinterface_neighbor_state_dict_buffer["neighborState"]["type"] = "Property"
                                                        interface_subinterface_neighbor_state_dict_buffer["neighborState"]["value"] = element_text
                                                        interface_subinterface_neighbor_state_dict_buffer["neighborState"]["observedAt"] = observed_at
                                                    if len(parent_path) - 1 == 9:
                                                        dict_buffers.append(interface_subinterface_neighbor_state_dict_buffer)
                                            if len(parent_path) - 1 == 8:
                                                dict_buffers.append(interface_subinterface_neighbor_dict_buffer)
                                    if parent_path[8] == "unnumbered":
                                        if parent_path[9] == "config":
                                            interface_subinterface_config_dict_buffer = {}
                                            interface_subinterface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6UnnumberedConfig:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                            interface_subinterface_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6UnnumberedConfig"
                                            if len(parent_path) - 1 == 9 or len(parent_path) - 1 == 10:
                                                interface_subinterface_config_dict_buffer["isPartOf"] = {}
                                                interface_subinterface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_subinterface_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                interface_subinterface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                if child_node == "enabled":
                                                    interface_subinterface_config_dict_buffer["enabled"] = {}
                                                    interface_subinterface_config_dict_buffer["enabled"]["type"] = "Property"
                                                    interface_subinterface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                    interface_subinterface_config_dict_buffer["enabled"]["observedAt"] = observed_at
                                                if len(parent_path) - 1 == 9:
                                                    dict_buffers.append(interface_subinterface_config_dict_buffer)
                                            if parent_path[10] == "state":
                                                interface_subinterface_state_dict_buffer = {}
                                                interface_subinterface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6UnnumberedState:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                interface_subinterface_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6UnnumberedState"
                                                if len(parent_path) - 1 == 10 or len(parent_path) - 1 == 11:
                                                    interface_subinterface_state_dict_buffer["isPartOf"] = {}
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    if child_node == "enabled":
                                                        interface_subinterface_state_dict_buffer["enabled"] = {}
                                                        interface_subinterface_state_dict_buffer["enabled"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                        interface_subinterface_state_dict_buffer["enabled"]["observedAt"] = observed_at
                                                    if len(parent_path) - 1 == 10:
                                                        dict_buffers.append(interface_subinterface_state_dict_buffer)
                                                if parent_path[11] == "interface-ref":
                                                    if parent_path[12] == "config":
                                                        interface_subinterface_config_dict_buffer = {}
                                                        interface_subinterface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6UnnumberedInterfaceRefConfig:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                        interface_subinterface_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6UnnumberedInterfaceRefConfig"
                                                        if len(parent_path) - 1 == 12 or len(parent_path) - 1 == 13:
                                                            interface_subinterface_config_dict_buffer["isPartOf"] = {}
                                                            interface_subinterface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_subinterface_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                            interface_subinterface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            if len(parent_path) - 1 == 12 or len(parent_path) - 1 == 13:
                                                                if interface_subinterface_config_dict_buffer["id"].split(":")[-1] != element_text:
                                                                    interface_subinterface_config_dict_buffer["id"] = interface_subinterface_config_dict_buffer["id"] + element_text
                                                                interface_subinterface_config_dict_buffer["interface"] = {}
                                                                interface_subinterface_config_dict_buffer["interface"]["type"] = "Relationship"
                                                                interface_subinterface_config_dict_buffer["interface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6UnnumberedInterfaceRefConfigInterface:" + interface_subinterface_config_dict_buffer["id"].split(":")[-1]
                                                                interface_subinterface_config_dict_buffer["interface"]["observedAt"] = observed_at
                                                            if len(parent_path) - 1 == 12 or len(parent_path) - 1 == 13:
                                                                if "." + str(element_text) not in interface_subinterface_config_dict_buffer["id"].split(":")[-1]:
                                                                    interface_subinterface_config_dict_buffer["id"] = interface_subinterface_config_dict_buffer["id"] + "." + str(element_text)
                                                                interface_subinterface_config_dict_buffer["subinterface"] = {}
                                                                interface_subinterface_config_dict_buffer["subinterface"]["type"] = "Relationship"
                                                                interface_subinterface_config_dict_buffer["subinterface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6UnnumberedInterfaceRefConfigSubinterface:" + interface_subinterface_config_dict_buffer["id"].split(":")[-1]
                                                                interface_subinterface_config_dict_buffer["subinterface"]["observedAt"] = observed_at
                                                            if len(parent_path) - 1 == 12:
                                                                dict_buffers.append(interface_subinterface_config_dict_buffer)
                                                        if parent_path[13] == "state":
                                                            interface_subinterface_state_dict_buffer = {}
                                                            interface_subinterface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6UnnumberedInterfaceRefState:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                            interface_subinterface_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6UnnumberedInterfaceRefState"
                                                            if len(parent_path) - 1 == 13 or len(parent_path) - 1 == 14:
                                                                interface_subinterface_state_dict_buffer["isPartOf"] = {}
                                                                interface_subinterface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                interface_subinterface_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                                interface_subinterface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                if len(parent_path) - 1 == 13 or len(parent_path) - 1 == 14:
                                                                    if interface_subinterface_state_dict_buffer["id"].split(":")[-1] != element_text:
                                                                        interface_subinterface_state_dict_buffer["id"] = interface_subinterface_state_dict_buffer["id"] + element_text
                                                                    interface_subinterface_state_dict_buffer["interface"] = {}
                                                                    interface_subinterface_state_dict_buffer["interface"]["type"] = "Relationship"
                                                                    interface_subinterface_state_dict_buffer["interface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6UnnumberedInterfaceRefStateInterface:" + interface_subinterface_state_dict_buffer["id"].split(":")[-1]
                                                                    interface_subinterface_state_dict_buffer["interface"]["observedAt"] = observed_at
                                                                if len(parent_path) - 1 == 13 or len(parent_path) - 1 == 14:
                                                                    if "." + str(element_text) not in interface_subinterface_state_dict_buffer["id"].split(":")[-1]:
                                                                        interface_subinterface_state_dict_buffer["id"] = interface_subinterface_state_dict_buffer["id"] + "." + str(element_text)
                                                                    interface_subinterface_state_dict_buffer["subinterface"] = {}
                                                                    interface_subinterface_state_dict_buffer["subinterface"]["type"] = "Relationship"
                                                                    interface_subinterface_state_dict_buffer["subinterface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6UnnumberedInterfaceRefStateSubinterface:" + interface_subinterface_state_dict_buffer["id"].split(":")[-1]
                                                                    interface_subinterface_state_dict_buffer["subinterface"]["observedAt"] = observed_at
                                                                if len(parent_path) - 1 == 13:
                                                                    dict_buffers.append(interface_subinterface_state_dict_buffer)
                                        if parent_path[9] == "config":
                                            interface_subinterface_config_dict_buffer = {}
                                            interface_subinterface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6Config:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                            interface_subinterface_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6Config"
                                            if len(parent_path) - 1 == 9 or len(parent_path) - 1 == 10:
                                                interface_subinterface_config_dict_buffer["isPartOf"] = {}
                                                interface_subinterface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_subinterface_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                interface_subinterface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                if child_node == "enabled":
                                                    interface_subinterface_config_dict_buffer["enabled"] = {}
                                                    interface_subinterface_config_dict_buffer["enabled"]["type"] = "Property"
                                                    interface_subinterface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                    interface_subinterface_config_dict_buffer["enabled"]["observedAt"] = observed_at
                                                if child_node == "mtu":
                                                    interface_subinterface_config_dict_buffer["mtu"] = {}
                                                    interface_subinterface_config_dict_buffer["mtu"]["type"] = "Property"
                                                    interface_subinterface_config_dict_buffer["mtu"]["value"] = int(element_text)
                                                    interface_subinterface_config_dict_buffer["mtu"]["observedAt"] = observed_at
                                                if child_node == "dup-addr-detect-transmits":
                                                    interface_subinterface_config_dict_buffer["dupAddrDetectTransmits"] = {}
                                                    interface_subinterface_config_dict_buffer["dupAddrDetectTransmits"]["type"] = "Property"
                                                    interface_subinterface_config_dict_buffer["dupAddrDetectTransmits"]["value"] = int(element_text)
                                                    interface_subinterface_config_dict_buffer["dupAddrDetectTransmits"]["observedAt"] = observed_at
                                                if child_node == "dhcp-client":
                                                    interface_subinterface_config_dict_buffer["dhcpClient"] = {}
                                                    interface_subinterface_config_dict_buffer["dhcpClient"]["type"] = "Property"
                                                    interface_subinterface_config_dict_buffer["dhcpClient"]["value"] = eval(str(element_text).capitalize())
                                                    interface_subinterface_config_dict_buffer["dhcpClient"]["observedAt"] = observed_at
                                                if len(parent_path) - 1 == 9:
                                                    dict_buffers.append(interface_subinterface_config_dict_buffer)
                                            if parent_path[10] == "state":
                                                interface_subinterface_state_dict_buffer = {}
                                                interface_subinterface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6State:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                interface_subinterface_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6State"
                                                if len(parent_path) - 1 == 10 or len(parent_path) - 1 == 11:
                                                    interface_subinterface_state_dict_buffer["isPartOf"] = {}
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    if child_node == "enabled":
                                                        interface_subinterface_state_dict_buffer["enabled"] = {}
                                                        interface_subinterface_state_dict_buffer["enabled"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                        interface_subinterface_state_dict_buffer["enabled"]["observedAt"] = observed_at
                                                    if child_node == "mtu":
                                                        interface_subinterface_state_dict_buffer["mtu"] = {}
                                                        interface_subinterface_state_dict_buffer["mtu"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["mtu"]["value"] = int(element_text)
                                                        interface_subinterface_state_dict_buffer["mtu"]["observedAt"] = observed_at
                                                    if child_node == "dup-addr-detect-transmits":
                                                        interface_subinterface_state_dict_buffer["dupAddrDetectTransmits"] = {}
                                                        interface_subinterface_state_dict_buffer["dupAddrDetectTransmits"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["dupAddrDetectTransmits"]["value"] = int(element_text)
                                                        interface_subinterface_state_dict_buffer["dupAddrDetectTransmits"]["observedAt"] = observed_at
                                                    if child_node == "dhcp-client":
                                                        interface_subinterface_state_dict_buffer["dhcpClient"] = {}
                                                        interface_subinterface_state_dict_buffer["dhcpClient"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["dhcpClient"]["value"] = eval(str(element_text).capitalize())
                                                        interface_subinterface_state_dict_buffer["dhcpClient"]["observedAt"] = observed_at
                                                    if parent_path[11] == "counters":
                                                        interface_subinterface_state_counters_dict_buffer = {}
                                                        interface_subinterface_state_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6StateCounters:" + interface_subinterface_state_dict_buffer["id"].split(":")[-1]
                                                        interface_subinterface_state_counters_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6StateCounters"
                                                        if len(parent_path) - 1 == 11 or len(parent_path) - 1 == 12:
                                                            interface_subinterface_state_counters_dict_buffer["isPartOf"] = {}
                                                            interface_subinterface_state_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_subinterface_state_counters_dict_buffer["isPartOf"]["object"] = interface_subinterface_state_dict_buffer["id"]
                                                            interface_subinterface_state_counters_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            if child_node == "in-pkts":
                                                                interface_subinterface_state_counters_dict_buffer["inPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inPkts"]["observedAt"] = observed_at
                                                            if child_node == "in-octets":
                                                                interface_subinterface_state_counters_dict_buffer["inOctets"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inOctets"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inOctets"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inOctets"]["observedAt"] = observed_at
                                                            if child_node == "in-error-pkts":
                                                                interface_subinterface_state_counters_dict_buffer["inErrorPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inErrorPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inErrorPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inErrorPkts"]["observedAt"] = observed_at
                                                            if child_node == "in-forwarded-pkts":
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedPkts"]["observedAt"] = observed_at
                                                            if child_node == "in-forwarded-octets":
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedOctets"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedOctets"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedOctets"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedOctets"]["observedAt"] = observed_at
                                                            if child_node == "in-discarded-pkts":
                                                                interface_subinterface_state_counters_dict_buffer["inDiscardedPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inDiscardedPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inDiscardedPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inDiscardedPkts"]["observedAt"] = observed_at
                                                            if child_node == "out-pkts":
                                                                interface_subinterface_state_counters_dict_buffer["outPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outPkts"]["observedAt"] = observed_at
                                                            if child_node == "out-octets":
                                                                interface_subinterface_state_counters_dict_buffer["outOctets"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outOctets"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outOctets"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outOctets"]["observedAt"] = observed_at
                                                            if child_node == "out-error-pkts":
                                                                interface_subinterface_state_counters_dict_buffer["outErrorPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outErrorPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outErrorPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outErrorPkts"]["observedAt"] = observed_at
                                                            if child_node == "out-forwarded-pkts":
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedPkts"]["observedAt"] = observed_at
                                                            if child_node == "out-forwarded-octets":
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedOctets"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedOctets"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedOctets"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedOctets"]["observedAt"] = observed_at
                                                            if child_node == "out-discarded-pkts":
                                                                interface_subinterface_state_counters_dict_buffer["outDiscardedPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outDiscardedPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outDiscardedPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outDiscardedPkts"]["observedAt"] = observed_at
                                                            if len(parent_path) - 1 == 11:
                                                                dict_buffers.append(interface_subinterface_state_counters_dict_buffer)
                                                    if len(parent_path) - 1 == 10:
                                                        dict_buffers.append(interface_subinterface_state_dict_buffer)
                    if len(parent_path) - 1 == 3:
                        dict_buffers.append(interface_subinterface_dict_buffer)
        if parent_path[2] == "openconfig-if-ethernet:ethernet" or parent_path[2] == "ethernet":
            if parent_path[3] == "config":
                interface_config_dict_buffer = {}
                interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetConfig:" + interface_dict_buffer["id"].split(":")[-1]
                interface_config_dict_buffer["type"] = "InterfaceEthernetConfig"
                if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                    interface_config_dict_buffer["isPartOf"] = {}
                    interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                    interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    if child_node == "mac-address":
                        interface_config_dict_buffer["macAddress"] = {}
                        interface_config_dict_buffer["macAddress"]["type"] = "Property"
                        interface_config_dict_buffer["macAddress"]["value"] = element_text
                        interface_config_dict_buffer["macAddress"]["observedAt"] = observed_at
                    if child_node == "auto-negotiate":
                        interface_config_dict_buffer["autoNegotiate"] = {}
                        interface_config_dict_buffer["autoNegotiate"]["type"] = "Property"
                        interface_config_dict_buffer["autoNegotiate"]["value"] = eval(str(element_text).capitalize())
                        interface_config_dict_buffer["autoNegotiate"]["observedAt"] = observed_at
                    if child_node == "duplex-mode":
                        interface_config_dict_buffer["duplexMode"] = {}
                        interface_config_dict_buffer["duplexMode"]["type"] = "Property"
                        interface_config_dict_buffer["duplexMode"]["value"] = element_text
                        interface_config_dict_buffer["duplexMode"]["observedAt"] = observed_at
                    if child_node == "enable-flow-control":
                        interface_config_dict_buffer["enableFlowControl"] = {}
                        interface_config_dict_buffer["enableFlowControl"]["type"] = "Property"
                        interface_config_dict_buffer["enableFlowControl"]["value"] = eval(str(element_text).capitalize())
                        interface_config_dict_buffer["enableFlowControl"]["observedAt"] = observed_at
                    if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                        if interface_config_dict_buffer["id"].split(":")[-1] != element_text:
                            interface_config_dict_buffer["id"] = interface_config_dict_buffer["id"] + element_text
                        interface_config_dict_buffer["aggregateId"] = {}
                        interface_config_dict_buffer["aggregateId"]["type"] = "Relationship"
                        interface_config_dict_buffer["aggregateId"]["object"] = "urn:ngsi-ld:Interface:" + interface_config_dict_buffer["id"].split(":")[-1]
                        interface_config_dict_buffer["aggregateId"]["observedAt"] = observed_at
                    if len(parent_path) - 1 == 3:
                        dict_buffers.append(interface_config_dict_buffer)
                if parent_path[4] == "state":
                    interface_state_dict_buffer = {}
                    interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetState:" + interface_dict_buffer["id"].split(":")[-1]
                    interface_state_dict_buffer["type"] = "InterfaceEthernetState"
                    if len(parent_path) - 1 == 4 or len(parent_path) - 1 == 5:
                        interface_state_dict_buffer["isPartOf"] = {}
                        interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                        interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "mac-address":
                            interface_state_dict_buffer["macAddress"] = {}
                            interface_state_dict_buffer["macAddress"]["type"] = "Property"
                            interface_state_dict_buffer["macAddress"]["value"] = element_text
                            interface_state_dict_buffer["macAddress"]["observedAt"] = observed_at
                        if child_node == "auto-negotiate":
                            interface_state_dict_buffer["autoNegotiate"] = {}
                            interface_state_dict_buffer["autoNegotiate"]["type"] = "Property"
                            interface_state_dict_buffer["autoNegotiate"]["value"] = eval(str(element_text).capitalize())
                            interface_state_dict_buffer["autoNegotiate"]["observedAt"] = observed_at
                        if child_node == "duplex-mode":
                            interface_state_dict_buffer["duplexMode"] = {}
                            interface_state_dict_buffer["duplexMode"]["type"] = "Property"
                            interface_state_dict_buffer["duplexMode"]["value"] = element_text
                            interface_state_dict_buffer["duplexMode"]["observedAt"] = observed_at
                        if child_node == "enable-flow-control":
                            interface_state_dict_buffer["enableFlowControl"] = {}
                            interface_state_dict_buffer["enableFlowControl"]["type"] = "Property"
                            interface_state_dict_buffer["enableFlowControl"]["value"] = eval(str(element_text).capitalize())
                            interface_state_dict_buffer["enableFlowControl"]["observedAt"] = observed_at
                        if child_node == "hw-mac-address":
                            interface_state_dict_buffer["hwMacAddress"] = {}
                            interface_state_dict_buffer["hwMacAddress"]["type"] = "Property"
                            interface_state_dict_buffer["hwMacAddress"]["value"] = element_text
                            interface_state_dict_buffer["hwMacAddress"]["observedAt"] = observed_at
                        if child_node == "negotiated-duplex-mode":
                            interface_state_dict_buffer["negotiatedDuplexMode"] = {}
                            interface_state_dict_buffer["negotiatedDuplexMode"]["type"] = "Property"
                            interface_state_dict_buffer["negotiatedDuplexMode"]["value"] = element_text
                            interface_state_dict_buffer["negotiatedDuplexMode"]["observedAt"] = observed_at
                        if parent_path[5] == "counters":
                            interface_state_counters_dict_buffer = {}
                            interface_state_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetStateCounters:" + interface_state_dict_buffer["id"].split(":")[-1]
                            interface_state_counters_dict_buffer["type"] = "InterfaceEthernetStateCounters"
                            if len(parent_path) - 1 == 5 or len(parent_path) - 1 == 6:
                                interface_state_counters_dict_buffer["isPartOf"] = {}
                                interface_state_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                                interface_state_counters_dict_buffer["isPartOf"]["object"] = interface_state_dict_buffer["id"]
                                interface_state_counters_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                if child_node == "in-mac-control-frames":
                                    interface_state_counters_dict_buffer["inMacControlFrames"] = {}
                                    interface_state_counters_dict_buffer["inMacControlFrames"]["type"] = "Property"
                                    interface_state_counters_dict_buffer["inMacControlFrames"]["value"] = int(element_text)
                                    interface_state_counters_dict_buffer["inMacControlFrames"]["observedAt"] = observed_at
                                if child_node == "in-mac-pause-frames":
                                    interface_state_counters_dict_buffer["inMacPauseFrames"] = {}
                                    interface_state_counters_dict_buffer["inMacPauseFrames"]["type"] = "Property"
                                    interface_state_counters_dict_buffer["inMacPauseFrames"]["value"] = int(element_text)
                                    interface_state_counters_dict_buffer["inMacPauseFrames"]["observedAt"] = observed_at
                                if child_node == "in-oversize-frames":
                                    interface_state_counters_dict_buffer["inOversizeFrames"] = {}
                                    interface_state_counters_dict_buffer["inOversizeFrames"]["type"] = "Property"
                                    interface_state_counters_dict_buffer["inOversizeFrames"]["value"] = int(element_text)
                                    interface_state_counters_dict_buffer["inOversizeFrames"]["observedAt"] = observed_at
                                if child_node == "in-jabber-frames":
                                    interface_state_counters_dict_buffer["inJabberFrames"] = {}
                                    interface_state_counters_dict_buffer["inJabberFrames"]["type"] = "Property"
                                    interface_state_counters_dict_buffer["inJabberFrames"]["value"] = int(element_text)
                                    interface_state_counters_dict_buffer["inJabberFrames"]["observedAt"] = observed_at
                                if child_node == "in-fragment-frames":
                                    interface_state_counters_dict_buffer["inFragmentFrames"] = {}
                                    interface_state_counters_dict_buffer["inFragmentFrames"]["type"] = "Property"
                                    interface_state_counters_dict_buffer["inFragmentFrames"]["value"] = int(element_text)
                                    interface_state_counters_dict_buffer["inFragmentFrames"]["observedAt"] = observed_at
                                if child_node == "in-8021q-frames":
                                    interface_state_counters_dict_buffer["in8021qFrames"] = {}
                                    interface_state_counters_dict_buffer["in8021qFrames"]["type"] = "Property"
                                    interface_state_counters_dict_buffer["in8021qFrames"]["value"] = int(element_text)
                                    interface_state_counters_dict_buffer["in8021qFrames"]["observedAt"] = observed_at
                                if child_node == "in-crc-errors":
                                    interface_state_counters_dict_buffer["inCrcErrors"] = {}
                                    interface_state_counters_dict_buffer["inCrcErrors"]["type"] = "Property"
                                    interface_state_counters_dict_buffer["inCrcErrors"]["value"] = int(element_text)
                                    interface_state_counters_dict_buffer["inCrcErrors"]["observedAt"] = observed_at
                                if child_node == "out-mac-control-frames":
                                    interface_state_counters_dict_buffer["outMacControlFrames"] = {}
                                    interface_state_counters_dict_buffer["outMacControlFrames"]["type"] = "Property"
                                    interface_state_counters_dict_buffer["outMacControlFrames"]["value"] = int(element_text)
                                    interface_state_counters_dict_buffer["outMacControlFrames"]["observedAt"] = observed_at
                                if child_node == "out-mac-pause-frames":
                                    interface_state_counters_dict_buffer["outMacPauseFrames"] = {}
                                    interface_state_counters_dict_buffer["outMacPauseFrames"]["type"] = "Property"
                                    interface_state_counters_dict_buffer["outMacPauseFrames"]["value"] = int(element_text)
                                    interface_state_counters_dict_buffer["outMacPauseFrames"]["observedAt"] = observed_at
                                if child_node == "out-8021q-frames":
                                    interface_state_counters_dict_buffer["out8021qFrames"] = {}
                                    interface_state_counters_dict_buffer["out8021qFrames"]["type"] = "Property"
                                    interface_state_counters_dict_buffer["out8021qFrames"]["value"] = int(element_text)
                                    interface_state_counters_dict_buffer["out8021qFrames"]["observedAt"] = observed_at
                                if len(parent_path) - 1 == 5:
                                    dict_buffers.append(interface_state_counters_dict_buffer)
                        if len(parent_path) - 1 == 4 or len(parent_path) - 1 == 5:
                            if interface_state_dict_buffer["id"].split(":")[-1] != element_text:
                                interface_state_dict_buffer["id"] = interface_state_dict_buffer["id"] + element_text
                            interface_state_dict_buffer["aggregateId"] = {}
                            interface_state_dict_buffer["aggregateId"]["type"] = "Relationship"
                            interface_state_dict_buffer["aggregateId"]["object"] = "urn:ngsi-ld:Interface:" + interface_state_dict_buffer["id"].split(":")[-1]
                            interface_state_dict_buffer["aggregateId"]["observedAt"] = observed_at
                        if len(parent_path) - 1 == 4:
                            dict_buffers.append(interface_state_dict_buffer)
                    if parent_path[5] == "switched-vlan":
                        if parent_path[6] == "config":
                            interface_config_dict_buffer = {}
                            interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetSwitchedVlanConfig:" + interface_dict_buffer["id"].split(":")[-1]
                            interface_config_dict_buffer["type"] = "InterfaceEthernetSwitchedVlanConfig"
                            if len(parent_path) - 1 == 6 or len(parent_path) - 1 == 7:
                                interface_config_dict_buffer["isPartOf"] = {}
                                interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                if child_node == "interface-mode":
                                    interface_config_dict_buffer["interfaceMode"] = {}
                                    interface_config_dict_buffer["interfaceMode"]["type"] = "Property"
                                    interface_config_dict_buffer["interfaceMode"]["value"] = element_text
                                    interface_config_dict_buffer["interfaceMode"]["observedAt"] = observed_at
                                if child_node == "native-vlan":
                                    interface_config_dict_buffer["nativeVlan"] = {}
                                    interface_config_dict_buffer["nativeVlan"]["type"] = "Property"
                                    interface_config_dict_buffer["nativeVlan"]["value"] = int(element_text)
                                    interface_config_dict_buffer["nativeVlan"]["observedAt"] = observed_at
                                if child_node == "access-vlan":
                                    interface_config_dict_buffer["accessVlan"] = {}
                                    interface_config_dict_buffer["accessVlan"]["type"] = "Property"
                                    interface_config_dict_buffer["accessVlan"]["value"] = int(element_text)
                                    interface_config_dict_buffer["accessVlan"]["observedAt"] = observed_at
                                if child_node == "trunk-vlans":
                                    interface_config_dict_buffer["trunkVlans"] = {}
                                    interface_config_dict_buffer["trunkVlans"]["type"] = "Property"
                                    interface_config_dict_buffer["trunkVlans"]["value"] = element_text
                                    interface_config_dict_buffer["trunkVlans"]["observedAt"] = observed_at
                                if len(parent_path) - 1 == 6:
                                    dict_buffers.append(interface_config_dict_buffer)
                            if parent_path[7] == "state":
                                interface_state_dict_buffer = {}
                                interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetSwitchedVlanState:" + interface_dict_buffer["id"].split(":")[-1]
                                interface_state_dict_buffer["type"] = "InterfaceEthernetSwitchedVlanState"
                                if len(parent_path) - 1 == 7 or len(parent_path) - 1 == 8:
                                    interface_state_dict_buffer["isPartOf"] = {}
                                    interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                    interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                    interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                    if child_node == "interface-mode":
                                        interface_state_dict_buffer["interfaceMode"] = {}
                                        interface_state_dict_buffer["interfaceMode"]["type"] = "Property"
                                        interface_state_dict_buffer["interfaceMode"]["value"] = element_text
                                        interface_state_dict_buffer["interfaceMode"]["observedAt"] = observed_at
                                    if child_node == "native-vlan":
                                        interface_state_dict_buffer["nativeVlan"] = {}
                                        interface_state_dict_buffer["nativeVlan"]["type"] = "Property"
                                        interface_state_dict_buffer["nativeVlan"]["value"] = int(element_text)
                                        interface_state_dict_buffer["nativeVlan"]["observedAt"] = observed_at
                                    if child_node == "access-vlan":
                                        interface_state_dict_buffer["accessVlan"] = {}
                                        interface_state_dict_buffer["accessVlan"]["type"] = "Property"
                                        interface_state_dict_buffer["accessVlan"]["value"] = int(element_text)
                                        interface_state_dict_buffer["accessVlan"]["observedAt"] = observed_at
                                    if child_node == "trunk-vlans":
                                        interface_state_dict_buffer["trunkVlans"] = {}
                                        interface_state_dict_buffer["trunkVlans"]["type"] = "Property"
                                        interface_state_dict_buffer["trunkVlans"]["value"] = element_text
                                        interface_state_dict_buffer["trunkVlans"]["observedAt"] = observed_at
                                    if len(parent_path) - 1 == 7:
                                        dict_buffers.append(interface_state_dict_buffer)
        if parent_path[2] == "openconfig-if-aggregate:aggregation" or parent_path[2] == "aggregation":
            if parent_path[3] == "config":
                interface_config_dict_buffer = {}
                interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceAggregationConfig:" + interface_dict_buffer["id"].split(":")[-1]
                interface_config_dict_buffer["type"] = "InterfaceAggregationConfig"
                if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                    interface_config_dict_buffer["isPartOf"] = {}
                    interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                    interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    if child_node == "lag-type":
                        interface_config_dict_buffer["lagType"] = {}
                        interface_config_dict_buffer["lagType"]["type"] = "Property"
                        interface_config_dict_buffer["lagType"]["value"] = element_text
                        interface_config_dict_buffer["lagType"]["observedAt"] = observed_at
                    if child_node == "min-links":
                        interface_config_dict_buffer["minLinks"] = {}
                        interface_config_dict_buffer["minLinks"]["type"] = "Property"
                        interface_config_dict_buffer["minLinks"]["value"] = int(element_text)
                        interface_config_dict_buffer["minLinks"]["observedAt"] = observed_at
                    if len(parent_path) - 1 == 3:
                        dict_buffers.append(interface_config_dict_buffer)
                if parent_path[4] == "state":
                    interface_state_dict_buffer = {}
                    interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceAggregationState:" + interface_dict_buffer["id"].split(":")[-1]
                    interface_state_dict_buffer["type"] = "InterfaceAggregationState"
                    if len(parent_path) - 1 == 4 or len(parent_path) - 1 == 5:
                        interface_state_dict_buffer["isPartOf"] = {}
                        interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                        interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "lag-type":
                            interface_state_dict_buffer["lagType"] = {}
                            interface_state_dict_buffer["lagType"]["type"] = "Property"
                            interface_state_dict_buffer["lagType"]["value"] = element_text
                            interface_state_dict_buffer["lagType"]["observedAt"] = observed_at
                        if child_node == "min-links":
                            interface_state_dict_buffer["minLinks"] = {}
                            interface_state_dict_buffer["minLinks"]["type"] = "Property"
                            interface_state_dict_buffer["minLinks"]["value"] = int(element_text)
                            interface_state_dict_buffer["minLinks"]["observedAt"] = observed_at
                        if child_node == "lag-speed":
                            interface_state_dict_buffer["lagSpeed"] = {}
                            interface_state_dict_buffer["lagSpeed"]["type"] = "Property"
                            interface_state_dict_buffer["lagSpeed"]["value"] = int(element_text)
                            interface_state_dict_buffer["lagSpeed"]["observedAt"] = observed_at
                        if len(parent_path) - 1 == 4 or len(parent_path) - 1 == 5:
                            interface_state_dict_buffer["member"] = {}
                            interface_state_dict_buffer["member"]["type"] = "Relationship"
                            interface_state_dict_buffer["member"]["object"] = "urn:ngsi-ld:Interface:" + interface_state_dict_buffer["id"].split(":")[-1]
                            interface_state_dict_buffer["member"]["observedAt"] = observed_at
                        if len(parent_path) - 1 == 4:
                            dict_buffers.append(interface_state_dict_buffer)
                    if parent_path[5] == "switched-vlan":
                        if parent_path[6] == "config":
                            interface_config_dict_buffer = {}
                            interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceAggregationSwitchedVlanConfig:" + interface_dict_buffer["id"].split(":")[-1]
                            interface_config_dict_buffer["type"] = "InterfaceAggregationSwitchedVlanConfig"
                            if len(parent_path) - 1 == 6 or len(parent_path) - 1 == 7:
                                interface_config_dict_buffer["isPartOf"] = {}
                                interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                if child_node == "interface-mode":
                                    interface_config_dict_buffer["interfaceMode"] = {}
                                    interface_config_dict_buffer["interfaceMode"]["type"] = "Property"
                                    interface_config_dict_buffer["interfaceMode"]["value"] = element_text
                                    interface_config_dict_buffer["interfaceMode"]["observedAt"] = observed_at
                                if child_node == "native-vlan":
                                    interface_config_dict_buffer["nativeVlan"] = {}
                                    interface_config_dict_buffer["nativeVlan"]["type"] = "Property"
                                    interface_config_dict_buffer["nativeVlan"]["value"] = int(element_text)
                                    interface_config_dict_buffer["nativeVlan"]["observedAt"] = observed_at
                                if child_node == "access-vlan":
                                    interface_config_dict_buffer["accessVlan"] = {}
                                    interface_config_dict_buffer["accessVlan"]["type"] = "Property"
                                    interface_config_dict_buffer["accessVlan"]["value"] = int(element_text)
                                    interface_config_dict_buffer["accessVlan"]["observedAt"] = observed_at
                                if child_node == "trunk-vlans":
                                    interface_config_dict_buffer["trunkVlans"] = {}
                                    interface_config_dict_buffer["trunkVlans"]["type"] = "Property"
                                    interface_config_dict_buffer["trunkVlans"]["value"] = element_text
                                    interface_config_dict_buffer["trunkVlans"]["observedAt"] = observed_at
                                if len(parent_path) - 1 == 6:
                                    dict_buffers.append(interface_config_dict_buffer)
                            if parent_path[7] == "state":
                                interface_state_dict_buffer = {}
                                interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceAggregationSwitchedVlanState:" + interface_dict_buffer["id"].split(":")[-1]
                                interface_state_dict_buffer["type"] = "InterfaceAggregationSwitchedVlanState"
                                if len(parent_path) - 1 == 7 or len(parent_path) - 1 == 8:
                                    interface_state_dict_buffer["isPartOf"] = {}
                                    interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                    interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                    interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                    if child_node == "interface-mode":
                                        interface_state_dict_buffer["interfaceMode"] = {}
                                        interface_state_dict_buffer["interfaceMode"]["type"] = "Property"
                                        interface_state_dict_buffer["interfaceMode"]["value"] = element_text
                                        interface_state_dict_buffer["interfaceMode"]["observedAt"] = observed_at
                                    if child_node == "native-vlan":
                                        interface_state_dict_buffer["nativeVlan"] = {}
                                        interface_state_dict_buffer["nativeVlan"]["type"] = "Property"
                                        interface_state_dict_buffer["nativeVlan"]["value"] = int(element_text)
                                        interface_state_dict_buffer["nativeVlan"]["observedAt"] = observed_at
                                    if child_node == "access-vlan":
                                        interface_state_dict_buffer["accessVlan"] = {}
                                        interface_state_dict_buffer["accessVlan"]["type"] = "Property"
                                        interface_state_dict_buffer["accessVlan"]["value"] = int(element_text)
                                        interface_state_dict_buffer["accessVlan"]["observedAt"] = observed_at
                                    if child_node == "trunk-vlans":
                                        interface_state_dict_buffer["trunkVlans"] = {}
                                        interface_state_dict_buffer["trunkVlans"]["type"] = "Property"
                                        interface_state_dict_buffer["trunkVlans"]["value"] = element_text
                                        interface_state_dict_buffer["trunkVlans"]["observedAt"] = observed_at
                                    if len(parent_path) - 1 == 7:
                                        dict_buffers.append(interface_state_dict_buffer)
        if parent_path[2] == "openconfig-vlan:routed-vlan" or parent_path[2] == "routed-vlan":
            if parent_path[3] == "config":
                interface_config_dict_buffer = {}
                interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanConfig:" + interface_dict_buffer["id"].split(":")[-1]
                interface_config_dict_buffer["type"] = "InterfaceRoutedVlanConfig"
                if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                    interface_config_dict_buffer["isPartOf"] = {}
                    interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                    interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    if child_node == "vlan":
                        interface_config_dict_buffer["vlan"] = {}
                        interface_config_dict_buffer["vlan"]["type"] = "Property"
                        interface_config_dict_buffer["vlan"]["value"] = element_text
                        interface_config_dict_buffer["vlan"]["observedAt"] = observed_at
                    if len(parent_path) - 1 == 3:
                        dict_buffers.append(interface_config_dict_buffer)
                if parent_path[4] == "state":
                    interface_state_dict_buffer = {}
                    interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanState:" + interface_dict_buffer["id"].split(":")[-1]
                    interface_state_dict_buffer["type"] = "InterfaceRoutedVlanState"
                    if len(parent_path) - 1 == 4 or len(parent_path) - 1 == 5:
                        interface_state_dict_buffer["isPartOf"] = {}
                        interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                        interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        if child_node == "vlan":
                            interface_state_dict_buffer["vlan"] = {}
                            interface_state_dict_buffer["vlan"]["type"] = "Property"
                            interface_state_dict_buffer["vlan"]["value"] = element_text
                            interface_state_dict_buffer["vlan"]["observedAt"] = observed_at
                        if len(parent_path) - 1 == 4:
                            dict_buffers.append(interface_state_dict_buffer)
                    if parent_path[5] == "ipv4":
                        if parent_path[6] == "addresses":
                            if parent_path[7] == "address":
                                interface_address_dict_buffer = {}
                                if iteration_key.get("interface_address_ip"):
                                    interface_address_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4AddressesAddress:" + iteration_key
                                interface_address_dict_buffer["type"] = "InterfaceRoutedVlanIpv4AddressesAddress"
                                if len(parent_path) - 1 == 7 or len(parent_path) - 1 == 8:
                                    interface_address_dict_buffer["isPartOf"] = {}
                                    interface_address_dict_buffer["isPartOf"]["type"] = "Relationship"
                                    interface_address_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                    interface_address_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                    if len(parent_path) - 1 == 7 or len(parent_path) - 1 == 8:
                                        if ":" in element_text:
                                            element_text = element_text.replace(":",".")
                                        if interface_address_dict_buffer["id"].split(":")[-1] != element_text:
                                            interface_address_dict_buffer["id"] = interface_address_dict_buffer["id"] + ":" + element_text
                                        interface_address_dict_buffer["ip"] = {}
                                        interface_address_dict_buffer["ip"]["type"] = "Relationship"
                                        interface_address_dict_buffer["ip"]["object"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4AddressesAddressConfig:" + interface_address_dict_buffer["id"].split(":")[-1]
                                        interface_address_dict_buffer["ip"]["observedAt"] = observed_at
                                    if parent_path[8] == "config":
                                        interface_address_config_dict_buffer = {}
                                        interface_address_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4AddressesAddressConfig:" + interface_address_dict_buffer["id"].split(":")[-1]
                                        interface_address_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv4AddressesAddressConfig"
                                        if len(parent_path) - 1 == 8 or len(parent_path) - 1 == 9:
                                            interface_address_config_dict_buffer["isPartOf"] = {}
                                            interface_address_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                            interface_address_config_dict_buffer["isPartOf"]["object"] = interface_address_dict_buffer["id"]
                                            interface_address_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                            if child_node == "ip":
                                                interface_address_config_dict_buffer["ip"] = {}
                                                interface_address_config_dict_buffer["ip"]["type"] = "Property"
                                                interface_address_config_dict_buffer["ip"]["value"] = element_text
                                                interface_address_config_dict_buffer["ip"]["observedAt"] = observed_at
                                            if child_node == "prefix-length":
                                                interface_address_config_dict_buffer["prefixLength"] = {}
                                                interface_address_config_dict_buffer["prefixLength"]["type"] = "Property"
                                                interface_address_config_dict_buffer["prefixLength"]["value"] = int(element_text)
                                                interface_address_config_dict_buffer["prefixLength"]["observedAt"] = observed_at
                                            if len(parent_path) - 1 == 8:
                                                dict_buffers.append(interface_address_config_dict_buffer)
                                    if parent_path[8] == "state":
                                        interface_address_state_dict_buffer = {}
                                        interface_address_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4AddressesAddressState:" + interface_address_dict_buffer["id"].split(":")[-1]
                                        interface_address_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv4AddressesAddressState"
                                        if len(parent_path) - 1 == 8 or len(parent_path) - 1 == 9:
                                            interface_address_state_dict_buffer["isPartOf"] = {}
                                            interface_address_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                            interface_address_state_dict_buffer["isPartOf"]["object"] = interface_address_dict_buffer["id"]
                                            interface_address_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                            if child_node == "ip":
                                                interface_address_state_dict_buffer["ip"] = {}
                                                interface_address_state_dict_buffer["ip"]["type"] = "Property"
                                                interface_address_state_dict_buffer["ip"]["value"] = element_text
                                                interface_address_state_dict_buffer["ip"]["observedAt"] = observed_at
                                            if child_node == "prefix-length":
                                                interface_address_state_dict_buffer["prefixLength"] = {}
                                                interface_address_state_dict_buffer["prefixLength"]["type"] = "Property"
                                                interface_address_state_dict_buffer["prefixLength"]["value"] = int(element_text)
                                                interface_address_state_dict_buffer["prefixLength"]["observedAt"] = observed_at
                                            if child_node == "origin":
                                                interface_address_state_dict_buffer["origin"] = {}
                                                interface_address_state_dict_buffer["origin"]["type"] = "Property"
                                                interface_address_state_dict_buffer["origin"]["value"] = element_text
                                                interface_address_state_dict_buffer["origin"]["observedAt"] = observed_at
                                            if len(parent_path) - 1 == 8:
                                                dict_buffers.append(interface_address_state_dict_buffer)
                                    if parent_path[8] == "vrrp":
                                        if parent_path[9] == "vrrp-group":
                                            interface_address_vrrp_group_dict_buffer = {}
                                            if iteration_key.get("interface_address_vrrp-group_virtual-router-id"):
                                                interface_address_vrrp_group_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroup:" + iteration_key
                                            interface_address_vrrp_group_dict_buffer["type"] = "InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroup"
                                            if len(parent_path) - 1 == 9 or len(parent_path) - 1 == 10:
                                                interface_address_vrrp_group_dict_buffer["isPartOf"] = {}
                                                interface_address_vrrp_group_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_address_vrrp_group_dict_buffer["isPartOf"]["object"] = interface_address_dict_buffer["id"]
                                                interface_address_vrrp_group_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                if len(parent_path) - 1 == 9 or len(parent_path) - 1 == 10:
                                                    if interface_address_vrrp_group_dict_buffer["id"].split(":")[-1] != element_text:
                                                        interface_address_vrrp_group_dict_buffer["id"] = interface_address_vrrp_group_dict_buffer["id"] + element_text
                                                    interface_address_vrrp_group_dict_buffer["virtualRouterId"] = {}
                                                    interface_address_vrrp_group_dict_buffer["virtualRouterId"]["type"] = "Relationship"
                                                    interface_address_vrrp_group_dict_buffer["virtualRouterId"]["object"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupConfig:" + interface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                    interface_address_vrrp_group_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                if parent_path[10] == "config":
                                                    interface_address_vrrp_group_config_dict_buffer = {}
                                                    interface_address_vrrp_group_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupConfig:" + interface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                    interface_address_vrrp_group_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupConfig"
                                                    if len(parent_path) - 1 == 10 or len(parent_path) - 1 == 11:
                                                        interface_address_vrrp_group_config_dict_buffer["isPartOf"] = {}
                                                        interface_address_vrrp_group_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_address_vrrp_group_config_dict_buffer["isPartOf"]["object"] = interface_address_vrrp_group_dict_buffer["id"]
                                                        interface_address_vrrp_group_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                        if child_node == "virtual-router-id":
                                                            if interface_address_vrrp_group_config_dict_buffer["id"].split(":")[-1] != int(element_text):
                                                                interface_address_vrrp_group_config_dict_buffer["id"] = interface_address_vrrp_group_config_dict_buffer["id"] + int(element_text)
                                                            interface_address_vrrp_group_config_dict_buffer["virtualRouterId"] = {}
                                                            interface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["type"] = "Property"
                                                            interface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["value"] = int(element_text)
                                                            interface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                        if child_node == "virtual-address":
                                                            interface_address_vrrp_group_config_dict_buffer["virtualAddress"] = {}
                                                            interface_address_vrrp_group_config_dict_buffer["virtualAddress"]["type"] = "Property"
                                                            interface_address_vrrp_group_config_dict_buffer["virtualAddress"]["value"] = element_text
                                                            interface_address_vrrp_group_config_dict_buffer["virtualAddress"]["observedAt"] = observed_at
                                                        if child_node == "priority":
                                                            interface_address_vrrp_group_config_dict_buffer["priority"] = {}
                                                            interface_address_vrrp_group_config_dict_buffer["priority"]["type"] = "Property"
                                                            interface_address_vrrp_group_config_dict_buffer["priority"]["value"] = int(element_text)
                                                            interface_address_vrrp_group_config_dict_buffer["priority"]["observedAt"] = observed_at
                                                        if child_node == "preempt":
                                                            interface_address_vrrp_group_config_dict_buffer["preempt"] = {}
                                                            interface_address_vrrp_group_config_dict_buffer["preempt"]["type"] = "Property"
                                                            interface_address_vrrp_group_config_dict_buffer["preempt"]["value"] = eval(str(element_text).capitalize())
                                                            interface_address_vrrp_group_config_dict_buffer["preempt"]["observedAt"] = observed_at
                                                        if child_node == "preempt-delay":
                                                            interface_address_vrrp_group_config_dict_buffer["preemptDelay"] = {}
                                                            interface_address_vrrp_group_config_dict_buffer["preemptDelay"]["type"] = "Property"
                                                            interface_address_vrrp_group_config_dict_buffer["preemptDelay"]["value"] = int(element_text)
                                                            interface_address_vrrp_group_config_dict_buffer["preemptDelay"]["observedAt"] = observed_at
                                                        if child_node == "accept-mode":
                                                            interface_address_vrrp_group_config_dict_buffer["acceptMode"] = {}
                                                            interface_address_vrrp_group_config_dict_buffer["acceptMode"]["type"] = "Property"
                                                            interface_address_vrrp_group_config_dict_buffer["acceptMode"]["value"] = eval(str(element_text).capitalize())
                                                            interface_address_vrrp_group_config_dict_buffer["acceptMode"]["observedAt"] = observed_at
                                                        if child_node == "advertisement-interval":
                                                            interface_address_vrrp_group_config_dict_buffer["advertisementInterval"] = {}
                                                            interface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["type"] = "Property"
                                                            interface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["value"] = int(element_text)
                                                            interface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["observedAt"] = observed_at
                                                        if len(parent_path) - 1 == 10:
                                                            dict_buffers.append(interface_address_vrrp_group_config_dict_buffer)
                                                if parent_path[10] == "state":
                                                    interface_address_vrrp_group_state_dict_buffer = {}
                                                    interface_address_vrrp_group_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupState:" + interface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                    interface_address_vrrp_group_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupState"
                                                    if len(parent_path) - 1 == 10 or len(parent_path) - 1 == 11:
                                                        interface_address_vrrp_group_state_dict_buffer["isPartOf"] = {}
                                                        interface_address_vrrp_group_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_address_vrrp_group_state_dict_buffer["isPartOf"]["object"] = interface_address_vrrp_group_dict_buffer["id"]
                                                        interface_address_vrrp_group_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                        if child_node == "virtual-router-id":
                                                            if interface_address_vrrp_group_state_dict_buffer["id"].split(":")[-1] != int(element_text):
                                                                interface_address_vrrp_group_state_dict_buffer["id"] = interface_address_vrrp_group_state_dict_buffer["id"] + int(element_text)
                                                            interface_address_vrrp_group_state_dict_buffer["virtualRouterId"] = {}
                                                            interface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["type"] = "Property"
                                                            interface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["value"] = int(element_text)
                                                            interface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                        if child_node == "virtual-address":
                                                            interface_address_vrrp_group_state_dict_buffer["virtualAddress"] = {}
                                                            interface_address_vrrp_group_state_dict_buffer["virtualAddress"]["type"] = "Property"
                                                            interface_address_vrrp_group_state_dict_buffer["virtualAddress"]["value"] = element_text
                                                            interface_address_vrrp_group_state_dict_buffer["virtualAddress"]["observedAt"] = observed_at
                                                        if child_node == "priority":
                                                            interface_address_vrrp_group_state_dict_buffer["priority"] = {}
                                                            interface_address_vrrp_group_state_dict_buffer["priority"]["type"] = "Property"
                                                            interface_address_vrrp_group_state_dict_buffer["priority"]["value"] = int(element_text)
                                                            interface_address_vrrp_group_state_dict_buffer["priority"]["observedAt"] = observed_at
                                                        if child_node == "preempt":
                                                            interface_address_vrrp_group_state_dict_buffer["preempt"] = {}
                                                            interface_address_vrrp_group_state_dict_buffer["preempt"]["type"] = "Property"
                                                            interface_address_vrrp_group_state_dict_buffer["preempt"]["value"] = eval(str(element_text).capitalize())
                                                            interface_address_vrrp_group_state_dict_buffer["preempt"]["observedAt"] = observed_at
                                                        if child_node == "preempt-delay":
                                                            interface_address_vrrp_group_state_dict_buffer["preemptDelay"] = {}
                                                            interface_address_vrrp_group_state_dict_buffer["preemptDelay"]["type"] = "Property"
                                                            interface_address_vrrp_group_state_dict_buffer["preemptDelay"]["value"] = int(element_text)
                                                            interface_address_vrrp_group_state_dict_buffer["preemptDelay"]["observedAt"] = observed_at
                                                        if child_node == "accept-mode":
                                                            interface_address_vrrp_group_state_dict_buffer["acceptMode"] = {}
                                                            interface_address_vrrp_group_state_dict_buffer["acceptMode"]["type"] = "Property"
                                                            interface_address_vrrp_group_state_dict_buffer["acceptMode"]["value"] = eval(str(element_text).capitalize())
                                                            interface_address_vrrp_group_state_dict_buffer["acceptMode"]["observedAt"] = observed_at
                                                        if child_node == "advertisement-interval":
                                                            interface_address_vrrp_group_state_dict_buffer["advertisementInterval"] = {}
                                                            interface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["type"] = "Property"
                                                            interface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["value"] = int(element_text)
                                                            interface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["observedAt"] = observed_at
                                                        if child_node == "current-priority":
                                                            interface_address_vrrp_group_state_dict_buffer["currentPriority"] = {}
                                                            interface_address_vrrp_group_state_dict_buffer["currentPriority"]["type"] = "Property"
                                                            interface_address_vrrp_group_state_dict_buffer["currentPriority"]["value"] = int(element_text)
                                                            interface_address_vrrp_group_state_dict_buffer["currentPriority"]["observedAt"] = observed_at
                                                        if len(parent_path) - 1 == 10:
                                                            dict_buffers.append(interface_address_vrrp_group_state_dict_buffer)
                                                if parent_path[10] == "interface-tracking":
                                                    if parent_path[11] == "config":
                                                        interface_address_vrrp_group_config_dict_buffer = {}
                                                        interface_address_vrrp_group_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig:" + interface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                        interface_address_vrrp_group_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig"
                                                        if len(parent_path) - 1 == 11 or len(parent_path) - 1 == 12:
                                                            interface_address_vrrp_group_config_dict_buffer["isPartOf"] = {}
                                                            interface_address_vrrp_group_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_address_vrrp_group_config_dict_buffer["isPartOf"]["object"] = interface_address_vrrp_group_dict_buffer["id"]
                                                            interface_address_vrrp_group_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            if len(parent_path) - 1 == 11 or len(parent_path) - 1 == 12:
                                                                interface_address_vrrp_group_config_dict_buffer["trackInterface"] = {}
                                                                interface_address_vrrp_group_config_dict_buffer["trackInterface"]["type"] = "Relationship"
                                                                interface_address_vrrp_group_config_dict_buffer["trackInterface"]["object"] = "urn:ngsi-ld:Interface:" + interface_address_vrrp_group_config_dict_buffer["id"].split(":")[-1]
                                                                interface_address_vrrp_group_config_dict_buffer["trackInterface"]["observedAt"] = observed_at
                                                            if child_node == "priority-decrement":
                                                                interface_address_vrrp_group_config_dict_buffer["priorityDecrement"] = {}
                                                                interface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["type"] = "Property"
                                                                interface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["value"] = int(element_text)
                                                                interface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["observedAt"] = observed_at
                                                            if len(parent_path) - 1 == 11:
                                                                dict_buffers.append(interface_address_vrrp_group_config_dict_buffer)
                                                        if parent_path[12] == "state":
                                                            interface_address_vrrp_group_state_dict_buffer = {}
                                                            interface_address_vrrp_group_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingState:" + interface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                            interface_address_vrrp_group_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingState"
                                                            if len(parent_path) - 1 == 12 or len(parent_path) - 1 == 13:
                                                                interface_address_vrrp_group_state_dict_buffer["isPartOf"] = {}
                                                                interface_address_vrrp_group_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                interface_address_vrrp_group_state_dict_buffer["isPartOf"]["object"] = interface_address_vrrp_group_dict_buffer["id"]
                                                                interface_address_vrrp_group_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                if len(parent_path) - 1 == 12 or len(parent_path) - 1 == 13:
                                                                    interface_address_vrrp_group_state_dict_buffer["trackInterface"] = {}
                                                                    interface_address_vrrp_group_state_dict_buffer["trackInterface"]["type"] = "Relationship"
                                                                    interface_address_vrrp_group_state_dict_buffer["trackInterface"]["object"] = "urn:ngsi-ld:Interface:" + interface_address_vrrp_group_state_dict_buffer["id"].split(":")[-1]
                                                                    interface_address_vrrp_group_state_dict_buffer["trackInterface"]["observedAt"] = observed_at
                                                                if child_node == "priority-decrement":
                                                                    interface_address_vrrp_group_state_dict_buffer["priorityDecrement"] = {}
                                                                    interface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["type"] = "Property"
                                                                    interface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["value"] = int(element_text)
                                                                    interface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["observedAt"] = observed_at
                                                                if len(parent_path) - 1 == 12:
                                                                    dict_buffers.append(interface_address_vrrp_group_state_dict_buffer)
                                                if len(parent_path) - 1 == 9:
                                                    dict_buffers.append(interface_address_vrrp_group_dict_buffer)
                                    if len(parent_path) - 1 == 7:
                                        dict_buffers.append(interface_address_dict_buffer)
                            if parent_path[7] == "proxy-arp":
                                if parent_path[8] == "config":
                                    interface_config_dict_buffer = {}
                                    interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4ProxyArpConfig:" + interface_dict_buffer["id"].split(":")[-1]
                                    interface_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv4ProxyArpConfig"
                                    if len(parent_path) - 1 == 8 or len(parent_path) - 1 == 9:
                                        interface_config_dict_buffer["isPartOf"] = {}
                                        interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                        interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                        interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                        if child_node == "mode":
                                            interface_config_dict_buffer["mode"] = {}
                                            interface_config_dict_buffer["mode"]["type"] = "Property"
                                            interface_config_dict_buffer["mode"]["value"] = element_text
                                            interface_config_dict_buffer["mode"]["observedAt"] = observed_at
                                        if len(parent_path) - 1 == 8:
                                            dict_buffers.append(interface_config_dict_buffer)
                                    if parent_path[9] == "state":
                                        interface_state_dict_buffer = {}
                                        interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4ProxyArpState:" + interface_dict_buffer["id"].split(":")[-1]
                                        interface_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv4ProxyArpState"
                                        if len(parent_path) - 1 == 9 or len(parent_path) - 1 == 10:
                                            interface_state_dict_buffer["isPartOf"] = {}
                                            interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                            interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                            interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                            if child_node == "mode":
                                                interface_state_dict_buffer["mode"] = {}
                                                interface_state_dict_buffer["mode"]["type"] = "Property"
                                                interface_state_dict_buffer["mode"]["value"] = element_text
                                                interface_state_dict_buffer["mode"]["observedAt"] = observed_at
                                            if len(parent_path) - 1 == 9:
                                                dict_buffers.append(interface_state_dict_buffer)
                                if parent_path[8] == "neighbors":
                                    if parent_path[9] == "neighbor":
                                        interface_neighbor_dict_buffer = {}
                                        if iteration_key.get("interface_neighbor_ip"):
                                            interface_neighbor_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4NeighborsNeighbor:" + iteration_key
                                        interface_neighbor_dict_buffer["type"] = "InterfaceRoutedVlanIpv4NeighborsNeighbor"
                                        if len(parent_path) - 1 == 9 or len(parent_path) - 1 == 10:
                                            interface_neighbor_dict_buffer["isPartOf"] = {}
                                            interface_neighbor_dict_buffer["isPartOf"]["type"] = "Relationship"
                                            interface_neighbor_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                            interface_neighbor_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                            if len(parent_path) - 1 == 9 or len(parent_path) - 1 == 10:
                                                if ":" in element_text:
                                                    element_text = element_text.replace(":",".")
                                                if interface_neighbor_dict_buffer["id"].split(":")[-1] != element_text:
                                                    interface_neighbor_dict_buffer["id"] = interface_neighbor_dict_buffer["id"] + ":" + element_text
                                                interface_neighbor_dict_buffer["ip"] = {}
                                                interface_neighbor_dict_buffer["ip"]["type"] = "Relationship"
                                                interface_neighbor_dict_buffer["ip"]["object"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4NeighborsNeighborConfig:" + interface_neighbor_dict_buffer["id"].split(":")[-1]
                                                interface_neighbor_dict_buffer["ip"]["observedAt"] = observed_at
                                            if parent_path[10] == "config":
                                                interface_neighbor_config_dict_buffer = {}
                                                interface_neighbor_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4NeighborsNeighborConfig:" + interface_neighbor_dict_buffer["id"].split(":")[-1]
                                                interface_neighbor_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv4NeighborsNeighborConfig"
                                                if len(parent_path) - 1 == 10 or len(parent_path) - 1 == 11:
                                                    interface_neighbor_config_dict_buffer["isPartOf"] = {}
                                                    interface_neighbor_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_neighbor_config_dict_buffer["isPartOf"]["object"] = interface_neighbor_dict_buffer["id"]
                                                    interface_neighbor_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    if child_node == "ip":
                                                        interface_neighbor_config_dict_buffer["ip"] = {}
                                                        interface_neighbor_config_dict_buffer["ip"]["type"] = "Property"
                                                        interface_neighbor_config_dict_buffer["ip"]["value"] = element_text
                                                        interface_neighbor_config_dict_buffer["ip"]["observedAt"] = observed_at
                                                    if child_node == "link-layer-address":
                                                        interface_neighbor_config_dict_buffer["linkLayerAddress"] = {}
                                                        interface_neighbor_config_dict_buffer["linkLayerAddress"]["type"] = "Property"
                                                        interface_neighbor_config_dict_buffer["linkLayerAddress"]["value"] = element_text
                                                        interface_neighbor_config_dict_buffer["linkLayerAddress"]["observedAt"] = observed_at
                                                    if len(parent_path) - 1 == 10:
                                                        dict_buffers.append(interface_neighbor_config_dict_buffer)
                                            if parent_path[10] == "state":
                                                interface_neighbor_state_dict_buffer = {}
                                                interface_neighbor_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4NeighborsNeighborState:" + interface_neighbor_dict_buffer["id"].split(":")[-1]
                                                interface_neighbor_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv4NeighborsNeighborState"
                                                if len(parent_path) - 1 == 10 or len(parent_path) - 1 == 11:
                                                    interface_neighbor_state_dict_buffer["isPartOf"] = {}
                                                    interface_neighbor_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_neighbor_state_dict_buffer["isPartOf"]["object"] = interface_neighbor_dict_buffer["id"]
                                                    interface_neighbor_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    if child_node == "ip":
                                                        interface_neighbor_state_dict_buffer["ip"] = {}
                                                        interface_neighbor_state_dict_buffer["ip"]["type"] = "Property"
                                                        interface_neighbor_state_dict_buffer["ip"]["value"] = element_text
                                                        interface_neighbor_state_dict_buffer["ip"]["observedAt"] = observed_at
                                                    if child_node == "link-layer-address":
                                                        interface_neighbor_state_dict_buffer["linkLayerAddress"] = {}
                                                        interface_neighbor_state_dict_buffer["linkLayerAddress"]["type"] = "Property"
                                                        interface_neighbor_state_dict_buffer["linkLayerAddress"]["value"] = element_text
                                                        interface_neighbor_state_dict_buffer["linkLayerAddress"]["observedAt"] = observed_at
                                                    if child_node == "origin":
                                                        interface_neighbor_state_dict_buffer["origin"] = {}
                                                        interface_neighbor_state_dict_buffer["origin"]["type"] = "Property"
                                                        interface_neighbor_state_dict_buffer["origin"]["value"] = element_text
                                                        interface_neighbor_state_dict_buffer["origin"]["observedAt"] = observed_at
                                                    if len(parent_path) - 1 == 10:
                                                        dict_buffers.append(interface_neighbor_state_dict_buffer)
                                            if len(parent_path) - 1 == 9:
                                                dict_buffers.append(interface_neighbor_dict_buffer)
                                    if parent_path[9] == "unnumbered":
                                        if parent_path[10] == "config":
                                            interface_config_dict_buffer = {}
                                            interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4UnnumberedConfig:" + interface_dict_buffer["id"].split(":")[-1]
                                            interface_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv4UnnumberedConfig"
                                            if len(parent_path) - 1 == 10 or len(parent_path) - 1 == 11:
                                                interface_config_dict_buffer["isPartOf"] = {}
                                                interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                if child_node == "enabled":
                                                    interface_config_dict_buffer["enabled"] = {}
                                                    interface_config_dict_buffer["enabled"]["type"] = "Property"
                                                    interface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                    interface_config_dict_buffer["enabled"]["observedAt"] = observed_at
                                                if len(parent_path) - 1 == 10:
                                                    dict_buffers.append(interface_config_dict_buffer)
                                            if parent_path[11] == "state":
                                                interface_state_dict_buffer = {}
                                                interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4UnnumberedState:" + interface_dict_buffer["id"].split(":")[-1]
                                                interface_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv4UnnumberedState"
                                                if len(parent_path) - 1 == 11 or len(parent_path) - 1 == 12:
                                                    interface_state_dict_buffer["isPartOf"] = {}
                                                    interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                    interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    if child_node == "enabled":
                                                        interface_state_dict_buffer["enabled"] = {}
                                                        interface_state_dict_buffer["enabled"]["type"] = "Property"
                                                        interface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                        interface_state_dict_buffer["enabled"]["observedAt"] = observed_at
                                                    if len(parent_path) - 1 == 11:
                                                        dict_buffers.append(interface_state_dict_buffer)
                                                if parent_path[12] == "interface-ref":
                                                    if parent_path[13] == "config":
                                                        interface_config_dict_buffer = {}
                                                        interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4UnnumberedInterfaceRefConfig:" + interface_dict_buffer["id"].split(":")[-1]
                                                        interface_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv4UnnumberedInterfaceRefConfig"
                                                        if len(parent_path) - 1 == 13 or len(parent_path) - 1 == 14:
                                                            interface_config_dict_buffer["isPartOf"] = {}
                                                            interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                            interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            if len(parent_path) - 1 == 13 or len(parent_path) - 1 == 14:
                                                                if interface_config_dict_buffer["id"].split(":")[-1] != element_text:
                                                                    interface_config_dict_buffer["id"] = interface_config_dict_buffer["id"] + element_text
                                                                interface_config_dict_buffer["interface"] = {}
                                                                interface_config_dict_buffer["interface"]["type"] = "Relationship"
                                                                interface_config_dict_buffer["interface"]["object"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4UnnumberedInterfaceRefConfigInterface:" + interface_config_dict_buffer["id"].split(":")[-1]
                                                                interface_config_dict_buffer["interface"]["observedAt"] = observed_at
                                                            if len(parent_path) - 1 == 13 or len(parent_path) - 1 == 14:
                                                                if "." + str(element_text) not in interface_config_dict_buffer["id"].split(":")[-1]:
                                                                    interface_config_dict_buffer["id"] = interface_config_dict_buffer["id"] + "." + str(element_text)
                                                                interface_config_dict_buffer["subinterface"] = {}
                                                                interface_config_dict_buffer["subinterface"]["type"] = "Relationship"
                                                                interface_config_dict_buffer["subinterface"]["object"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4UnnumberedInterfaceRefConfigSubinterface:" + interface_config_dict_buffer["id"].split(":")[-1]
                                                                interface_config_dict_buffer["subinterface"]["observedAt"] = observed_at
                                                            if len(parent_path) - 1 == 13:
                                                                dict_buffers.append(interface_config_dict_buffer)
                                                        if parent_path[14] == "state":
                                                            interface_state_dict_buffer = {}
                                                            interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4UnnumberedInterfaceRefState:" + interface_dict_buffer["id"].split(":")[-1]
                                                            interface_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv4UnnumberedInterfaceRefState"
                                                            if len(parent_path) - 1 == 14 or len(parent_path) - 1 == 15:
                                                                interface_state_dict_buffer["isPartOf"] = {}
                                                                interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                                interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                if len(parent_path) - 1 == 14 or len(parent_path) - 1 == 15:
                                                                    if interface_state_dict_buffer["id"].split(":")[-1] != element_text:
                                                                        interface_state_dict_buffer["id"] = interface_state_dict_buffer["id"] + element_text
                                                                    interface_state_dict_buffer["interface"] = {}
                                                                    interface_state_dict_buffer["interface"]["type"] = "Relationship"
                                                                    interface_state_dict_buffer["interface"]["object"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4UnnumberedInterfaceRefStateInterface:" + interface_state_dict_buffer["id"].split(":")[-1]
                                                                    interface_state_dict_buffer["interface"]["observedAt"] = observed_at
                                                                if len(parent_path) - 1 == 14 or len(parent_path) - 1 == 15:
                                                                    if "." + str(element_text) not in interface_state_dict_buffer["id"].split(":")[-1]:
                                                                        interface_state_dict_buffer["id"] = interface_state_dict_buffer["id"] + "." + str(element_text)
                                                                    interface_state_dict_buffer["subinterface"] = {}
                                                                    interface_state_dict_buffer["subinterface"]["type"] = "Relationship"
                                                                    interface_state_dict_buffer["subinterface"]["object"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4UnnumberedInterfaceRefStateSubinterface:" + interface_state_dict_buffer["id"].split(":")[-1]
                                                                    interface_state_dict_buffer["subinterface"]["observedAt"] = observed_at
                                                                if len(parent_path) - 1 == 14:
                                                                    dict_buffers.append(interface_state_dict_buffer)
                                        if parent_path[10] == "config":
                                            interface_config_dict_buffer = {}
                                            interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4Config:" + interface_dict_buffer["id"].split(":")[-1]
                                            interface_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv4Config"
                                            if len(parent_path) - 1 == 10 or len(parent_path) - 1 == 11:
                                                interface_config_dict_buffer["isPartOf"] = {}
                                                interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                if child_node == "enabled":
                                                    interface_config_dict_buffer["enabled"] = {}
                                                    interface_config_dict_buffer["enabled"]["type"] = "Property"
                                                    interface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                    interface_config_dict_buffer["enabled"]["observedAt"] = observed_at
                                                if child_node == "mtu":
                                                    interface_config_dict_buffer["mtu"] = {}
                                                    interface_config_dict_buffer["mtu"]["type"] = "Property"
                                                    interface_config_dict_buffer["mtu"]["value"] = int(element_text)
                                                    interface_config_dict_buffer["mtu"]["observedAt"] = observed_at
                                                if child_node == "dhcp-client":
                                                    interface_config_dict_buffer["dhcpClient"] = {}
                                                    interface_config_dict_buffer["dhcpClient"]["type"] = "Property"
                                                    interface_config_dict_buffer["dhcpClient"]["value"] = eval(str(element_text).capitalize())
                                                    interface_config_dict_buffer["dhcpClient"]["observedAt"] = observed_at
                                                if len(parent_path) - 1 == 10:
                                                    dict_buffers.append(interface_config_dict_buffer)
                                            if parent_path[11] == "state":
                                                interface_state_dict_buffer = {}
                                                interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4State:" + interface_dict_buffer["id"].split(":")[-1]
                                                interface_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv4State"
                                                if len(parent_path) - 1 == 11 or len(parent_path) - 1 == 12:
                                                    interface_state_dict_buffer["isPartOf"] = {}
                                                    interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                    interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    if child_node == "enabled":
                                                        interface_state_dict_buffer["enabled"] = {}
                                                        interface_state_dict_buffer["enabled"]["type"] = "Property"
                                                        interface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                        interface_state_dict_buffer["enabled"]["observedAt"] = observed_at
                                                    if child_node == "mtu":
                                                        interface_state_dict_buffer["mtu"] = {}
                                                        interface_state_dict_buffer["mtu"]["type"] = "Property"
                                                        interface_state_dict_buffer["mtu"]["value"] = int(element_text)
                                                        interface_state_dict_buffer["mtu"]["observedAt"] = observed_at
                                                    if child_node == "dhcp-client":
                                                        interface_state_dict_buffer["dhcpClient"] = {}
                                                        interface_state_dict_buffer["dhcpClient"]["type"] = "Property"
                                                        interface_state_dict_buffer["dhcpClient"]["value"] = eval(str(element_text).capitalize())
                                                        interface_state_dict_buffer["dhcpClient"]["observedAt"] = observed_at
                                                    if parent_path[12] == "counters":
                                                        interface_state_counters_dict_buffer = {}
                                                        interface_state_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4StateCounters:" + interface_state_dict_buffer["id"].split(":")[-1]
                                                        interface_state_counters_dict_buffer["type"] = "InterfaceRoutedVlanIpv4StateCounters"
                                                        if len(parent_path) - 1 == 12 or len(parent_path) - 1 == 13:
                                                            interface_state_counters_dict_buffer["isPartOf"] = {}
                                                            interface_state_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_state_counters_dict_buffer["isPartOf"]["object"] = interface_state_dict_buffer["id"]
                                                            interface_state_counters_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            if child_node == "in-pkts":
                                                                interface_state_counters_dict_buffer["inPkts"] = {}
                                                                interface_state_counters_dict_buffer["inPkts"]["type"] = "Property"
                                                                interface_state_counters_dict_buffer["inPkts"]["value"] = int(element_text)
                                                                interface_state_counters_dict_buffer["inPkts"]["observedAt"] = observed_at
                                                            if child_node == "in-octets":
                                                                interface_state_counters_dict_buffer["inOctets"] = {}
                                                                interface_state_counters_dict_buffer["inOctets"]["type"] = "Property"
                                                                interface_state_counters_dict_buffer["inOctets"]["value"] = int(element_text)
                                                                interface_state_counters_dict_buffer["inOctets"]["observedAt"] = observed_at
                                                            if child_node == "in-error-pkts":
                                                                interface_state_counters_dict_buffer["inErrorPkts"] = {}
                                                                interface_state_counters_dict_buffer["inErrorPkts"]["type"] = "Property"
                                                                interface_state_counters_dict_buffer["inErrorPkts"]["value"] = int(element_text)
                                                                interface_state_counters_dict_buffer["inErrorPkts"]["observedAt"] = observed_at
                                                            if child_node == "in-forwarded-pkts":
                                                                interface_state_counters_dict_buffer["inForwardedPkts"] = {}
                                                                interface_state_counters_dict_buffer["inForwardedPkts"]["type"] = "Property"
                                                                interface_state_counters_dict_buffer["inForwardedPkts"]["value"] = int(element_text)
                                                                interface_state_counters_dict_buffer["inForwardedPkts"]["observedAt"] = observed_at
                                                            if child_node == "in-forwarded-octets":
                                                                interface_state_counters_dict_buffer["inForwardedOctets"] = {}
                                                                interface_state_counters_dict_buffer["inForwardedOctets"]["type"] = "Property"
                                                                interface_state_counters_dict_buffer["inForwardedOctets"]["value"] = int(element_text)
                                                                interface_state_counters_dict_buffer["inForwardedOctets"]["observedAt"] = observed_at
                                                            if child_node == "in-discarded-pkts":
                                                                interface_state_counters_dict_buffer["inDiscardedPkts"] = {}
                                                                interface_state_counters_dict_buffer["inDiscardedPkts"]["type"] = "Property"
                                                                interface_state_counters_dict_buffer["inDiscardedPkts"]["value"] = int(element_text)
                                                                interface_state_counters_dict_buffer["inDiscardedPkts"]["observedAt"] = observed_at
                                                            if child_node == "out-pkts":
                                                                interface_state_counters_dict_buffer["outPkts"] = {}
                                                                interface_state_counters_dict_buffer["outPkts"]["type"] = "Property"
                                                                interface_state_counters_dict_buffer["outPkts"]["value"] = int(element_text)
                                                                interface_state_counters_dict_buffer["outPkts"]["observedAt"] = observed_at
                                                            if child_node == "out-octets":
                                                                interface_state_counters_dict_buffer["outOctets"] = {}
                                                                interface_state_counters_dict_buffer["outOctets"]["type"] = "Property"
                                                                interface_state_counters_dict_buffer["outOctets"]["value"] = int(element_text)
                                                                interface_state_counters_dict_buffer["outOctets"]["observedAt"] = observed_at
                                                            if child_node == "out-error-pkts":
                                                                interface_state_counters_dict_buffer["outErrorPkts"] = {}
                                                                interface_state_counters_dict_buffer["outErrorPkts"]["type"] = "Property"
                                                                interface_state_counters_dict_buffer["outErrorPkts"]["value"] = int(element_text)
                                                                interface_state_counters_dict_buffer["outErrorPkts"]["observedAt"] = observed_at
                                                            if child_node == "out-forwarded-pkts":
                                                                interface_state_counters_dict_buffer["outForwardedPkts"] = {}
                                                                interface_state_counters_dict_buffer["outForwardedPkts"]["type"] = "Property"
                                                                interface_state_counters_dict_buffer["outForwardedPkts"]["value"] = int(element_text)
                                                                interface_state_counters_dict_buffer["outForwardedPkts"]["observedAt"] = observed_at
                                                            if child_node == "out-forwarded-octets":
                                                                interface_state_counters_dict_buffer["outForwardedOctets"] = {}
                                                                interface_state_counters_dict_buffer["outForwardedOctets"]["type"] = "Property"
                                                                interface_state_counters_dict_buffer["outForwardedOctets"]["value"] = int(element_text)
                                                                interface_state_counters_dict_buffer["outForwardedOctets"]["observedAt"] = observed_at
                                                            if child_node == "out-discarded-pkts":
                                                                interface_state_counters_dict_buffer["outDiscardedPkts"] = {}
                                                                interface_state_counters_dict_buffer["outDiscardedPkts"]["type"] = "Property"
                                                                interface_state_counters_dict_buffer["outDiscardedPkts"]["value"] = int(element_text)
                                                                interface_state_counters_dict_buffer["outDiscardedPkts"]["observedAt"] = observed_at
                                                            if len(parent_path) - 1 == 12:
                                                                dict_buffers.append(interface_state_counters_dict_buffer)
                                                    if len(parent_path) - 1 == 11:
                                                        dict_buffers.append(interface_state_dict_buffer)
                        if parent_path[6] == "ipv6":
                            if parent_path[7] == "addresses":
                                if parent_path[8] == "address":
                                    interface_address_dict_buffer = {}
                                    if iteration_key.get("interface_address_ip"):
                                        interface_address_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6AddressesAddress:" + iteration_key
                                    interface_address_dict_buffer["type"] = "InterfaceRoutedVlanIpv6AddressesAddress"
                                    if len(parent_path) - 1 == 8 or len(parent_path) - 1 == 9:
                                        interface_address_dict_buffer["isPartOf"] = {}
                                        interface_address_dict_buffer["isPartOf"]["type"] = "Relationship"
                                        interface_address_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                        interface_address_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                        if len(parent_path) - 1 == 8 or len(parent_path) - 1 == 9:
                                            if ":" in element_text:
                                                element_text = element_text.replace(":",".")
                                            if interface_address_dict_buffer["id"].split(":")[-1] != element_text:
                                                interface_address_dict_buffer["id"] = interface_address_dict_buffer["id"] + ":" + element_text
                                            interface_address_dict_buffer["ip"] = {}
                                            interface_address_dict_buffer["ip"]["type"] = "Relationship"
                                            interface_address_dict_buffer["ip"]["object"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6AddressesAddressConfig:" + interface_address_dict_buffer["id"].split(":")[-1]
                                            interface_address_dict_buffer["ip"]["observedAt"] = observed_at
                                        if parent_path[9] == "config":
                                            interface_address_config_dict_buffer = {}
                                            interface_address_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6AddressesAddressConfig:" + interface_address_dict_buffer["id"].split(":")[-1]
                                            interface_address_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv6AddressesAddressConfig"
                                            if len(parent_path) - 1 == 9 or len(parent_path) - 1 == 10:
                                                interface_address_config_dict_buffer["isPartOf"] = {}
                                                interface_address_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_address_config_dict_buffer["isPartOf"]["object"] = interface_address_dict_buffer["id"]
                                                interface_address_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                if child_node == "ip":
                                                    interface_address_config_dict_buffer["ip"] = {}
                                                    interface_address_config_dict_buffer["ip"]["type"] = "Property"
                                                    interface_address_config_dict_buffer["ip"]["value"] = element_text
                                                    interface_address_config_dict_buffer["ip"]["observedAt"] = observed_at
                                                if child_node == "prefix-length":
                                                    interface_address_config_dict_buffer["prefixLength"] = {}
                                                    interface_address_config_dict_buffer["prefixLength"]["type"] = "Property"
                                                    interface_address_config_dict_buffer["prefixLength"]["value"] = int(element_text)
                                                    interface_address_config_dict_buffer["prefixLength"]["observedAt"] = observed_at
                                                if len(parent_path) - 1 == 9:
                                                    dict_buffers.append(interface_address_config_dict_buffer)
                                        if parent_path[9] == "state":
                                            interface_address_state_dict_buffer = {}
                                            interface_address_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6AddressesAddressState:" + interface_address_dict_buffer["id"].split(":")[-1]
                                            interface_address_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv6AddressesAddressState"
                                            if len(parent_path) - 1 == 9 or len(parent_path) - 1 == 10:
                                                interface_address_state_dict_buffer["isPartOf"] = {}
                                                interface_address_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_address_state_dict_buffer["isPartOf"]["object"] = interface_address_dict_buffer["id"]
                                                interface_address_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                if child_node == "ip":
                                                    interface_address_state_dict_buffer["ip"] = {}
                                                    interface_address_state_dict_buffer["ip"]["type"] = "Property"
                                                    interface_address_state_dict_buffer["ip"]["value"] = element_text
                                                    interface_address_state_dict_buffer["ip"]["observedAt"] = observed_at
                                                if child_node == "prefix-length":
                                                    interface_address_state_dict_buffer["prefixLength"] = {}
                                                    interface_address_state_dict_buffer["prefixLength"]["type"] = "Property"
                                                    interface_address_state_dict_buffer["prefixLength"]["value"] = int(element_text)
                                                    interface_address_state_dict_buffer["prefixLength"]["observedAt"] = observed_at
                                                if child_node == "origin":
                                                    interface_address_state_dict_buffer["origin"] = {}
                                                    interface_address_state_dict_buffer["origin"]["type"] = "Property"
                                                    interface_address_state_dict_buffer["origin"]["value"] = element_text
                                                    interface_address_state_dict_buffer["origin"]["observedAt"] = observed_at
                                                if child_node == "status":
                                                    interface_address_state_dict_buffer["status"] = {}
                                                    interface_address_state_dict_buffer["status"]["type"] = "Property"
                                                    interface_address_state_dict_buffer["status"]["value"] = element_text
                                                    interface_address_state_dict_buffer["status"]["observedAt"] = observed_at
                                                if len(parent_path) - 1 == 9:
                                                    dict_buffers.append(interface_address_state_dict_buffer)
                                        if parent_path[9] == "vrrp":
                                            if parent_path[10] == "vrrp-group":
                                                interface_address_vrrp_group_dict_buffer = {}
                                                if iteration_key.get("interface_address_vrrp-group_virtual-router-id"):
                                                    interface_address_vrrp_group_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroup:" + iteration_key
                                                interface_address_vrrp_group_dict_buffer["type"] = "InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroup"
                                                if len(parent_path) - 1 == 10 or len(parent_path) - 1 == 11:
                                                    interface_address_vrrp_group_dict_buffer["isPartOf"] = {}
                                                    interface_address_vrrp_group_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_address_vrrp_group_dict_buffer["isPartOf"]["object"] = interface_address_dict_buffer["id"]
                                                    interface_address_vrrp_group_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    if len(parent_path) - 1 == 10 or len(parent_path) - 1 == 11:
                                                        if interface_address_vrrp_group_dict_buffer["id"].split(":")[-1] != element_text:
                                                            interface_address_vrrp_group_dict_buffer["id"] = interface_address_vrrp_group_dict_buffer["id"] + element_text
                                                        interface_address_vrrp_group_dict_buffer["virtualRouterId"] = {}
                                                        interface_address_vrrp_group_dict_buffer["virtualRouterId"]["type"] = "Relationship"
                                                        interface_address_vrrp_group_dict_buffer["virtualRouterId"]["object"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupConfig:" + interface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                        interface_address_vrrp_group_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                    if parent_path[11] == "config":
                                                        interface_address_vrrp_group_config_dict_buffer = {}
                                                        interface_address_vrrp_group_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupConfig:" + interface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                        interface_address_vrrp_group_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupConfig"
                                                        if len(parent_path) - 1 == 11 or len(parent_path) - 1 == 12:
                                                            interface_address_vrrp_group_config_dict_buffer["isPartOf"] = {}
                                                            interface_address_vrrp_group_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_address_vrrp_group_config_dict_buffer["isPartOf"]["object"] = interface_address_vrrp_group_dict_buffer["id"]
                                                            interface_address_vrrp_group_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            if child_node == "virtual-router-id":
                                                                if interface_address_vrrp_group_config_dict_buffer["id"].split(":")[-1] != int(element_text):
                                                                    interface_address_vrrp_group_config_dict_buffer["id"] = interface_address_vrrp_group_config_dict_buffer["id"] + int(element_text)
                                                                interface_address_vrrp_group_config_dict_buffer["virtualRouterId"] = {}
                                                                interface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["type"] = "Property"
                                                                interface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["value"] = int(element_text)
                                                                interface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                            if child_node == "virtual-address":
                                                                interface_address_vrrp_group_config_dict_buffer["virtualAddress"] = {}
                                                                interface_address_vrrp_group_config_dict_buffer["virtualAddress"]["type"] = "Property"
                                                                interface_address_vrrp_group_config_dict_buffer["virtualAddress"]["value"] = element_text
                                                                interface_address_vrrp_group_config_dict_buffer["virtualAddress"]["observedAt"] = observed_at
                                                            if child_node == "priority":
                                                                interface_address_vrrp_group_config_dict_buffer["priority"] = {}
                                                                interface_address_vrrp_group_config_dict_buffer["priority"]["type"] = "Property"
                                                                interface_address_vrrp_group_config_dict_buffer["priority"]["value"] = int(element_text)
                                                                interface_address_vrrp_group_config_dict_buffer["priority"]["observedAt"] = observed_at
                                                            if child_node == "preempt":
                                                                interface_address_vrrp_group_config_dict_buffer["preempt"] = {}
                                                                interface_address_vrrp_group_config_dict_buffer["preempt"]["type"] = "Property"
                                                                interface_address_vrrp_group_config_dict_buffer["preempt"]["value"] = eval(str(element_text).capitalize())
                                                                interface_address_vrrp_group_config_dict_buffer["preempt"]["observedAt"] = observed_at
                                                            if child_node == "preempt-delay":
                                                                interface_address_vrrp_group_config_dict_buffer["preemptDelay"] = {}
                                                                interface_address_vrrp_group_config_dict_buffer["preemptDelay"]["type"] = "Property"
                                                                interface_address_vrrp_group_config_dict_buffer["preemptDelay"]["value"] = int(element_text)
                                                                interface_address_vrrp_group_config_dict_buffer["preemptDelay"]["observedAt"] = observed_at
                                                            if child_node == "accept-mode":
                                                                interface_address_vrrp_group_config_dict_buffer["acceptMode"] = {}
                                                                interface_address_vrrp_group_config_dict_buffer["acceptMode"]["type"] = "Property"
                                                                interface_address_vrrp_group_config_dict_buffer["acceptMode"]["value"] = eval(str(element_text).capitalize())
                                                                interface_address_vrrp_group_config_dict_buffer["acceptMode"]["observedAt"] = observed_at
                                                            if child_node == "advertisement-interval":
                                                                interface_address_vrrp_group_config_dict_buffer["advertisementInterval"] = {}
                                                                interface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["type"] = "Property"
                                                                interface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["value"] = int(element_text)
                                                                interface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["observedAt"] = observed_at
                                                            if child_node == "virtual-link-local":
                                                                interface_address_vrrp_group_config_dict_buffer["virtualLinkLocal"] = {}
                                                                interface_address_vrrp_group_config_dict_buffer["virtualLinkLocal"]["type"] = "Property"
                                                                interface_address_vrrp_group_config_dict_buffer["virtualLinkLocal"]["value"] = element_text
                                                                interface_address_vrrp_group_config_dict_buffer["virtualLinkLocal"]["observedAt"] = observed_at
                                                            if len(parent_path) - 1 == 11:
                                                                dict_buffers.append(interface_address_vrrp_group_config_dict_buffer)
                                                    if parent_path[11] == "state":
                                                        interface_address_vrrp_group_state_dict_buffer = {}
                                                        interface_address_vrrp_group_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupState:" + interface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                        interface_address_vrrp_group_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupState"
                                                        if len(parent_path) - 1 == 11 or len(parent_path) - 1 == 12:
                                                            interface_address_vrrp_group_state_dict_buffer["isPartOf"] = {}
                                                            interface_address_vrrp_group_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_address_vrrp_group_state_dict_buffer["isPartOf"]["object"] = interface_address_vrrp_group_dict_buffer["id"]
                                                            interface_address_vrrp_group_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            if child_node == "virtual-router-id":
                                                                if interface_address_vrrp_group_state_dict_buffer["id"].split(":")[-1] != int(element_text):
                                                                    interface_address_vrrp_group_state_dict_buffer["id"] = interface_address_vrrp_group_state_dict_buffer["id"] + int(element_text)
                                                                interface_address_vrrp_group_state_dict_buffer["virtualRouterId"] = {}
                                                                interface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["type"] = "Property"
                                                                interface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["value"] = int(element_text)
                                                                interface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                            if child_node == "virtual-address":
                                                                interface_address_vrrp_group_state_dict_buffer["virtualAddress"] = {}
                                                                interface_address_vrrp_group_state_dict_buffer["virtualAddress"]["type"] = "Property"
                                                                interface_address_vrrp_group_state_dict_buffer["virtualAddress"]["value"] = element_text
                                                                interface_address_vrrp_group_state_dict_buffer["virtualAddress"]["observedAt"] = observed_at
                                                            if child_node == "priority":
                                                                interface_address_vrrp_group_state_dict_buffer["priority"] = {}
                                                                interface_address_vrrp_group_state_dict_buffer["priority"]["type"] = "Property"
                                                                interface_address_vrrp_group_state_dict_buffer["priority"]["value"] = int(element_text)
                                                                interface_address_vrrp_group_state_dict_buffer["priority"]["observedAt"] = observed_at
                                                            if child_node == "preempt":
                                                                interface_address_vrrp_group_state_dict_buffer["preempt"] = {}
                                                                interface_address_vrrp_group_state_dict_buffer["preempt"]["type"] = "Property"
                                                                interface_address_vrrp_group_state_dict_buffer["preempt"]["value"] = eval(str(element_text).capitalize())
                                                                interface_address_vrrp_group_state_dict_buffer["preempt"]["observedAt"] = observed_at
                                                            if child_node == "preempt-delay":
                                                                interface_address_vrrp_group_state_dict_buffer["preemptDelay"] = {}
                                                                interface_address_vrrp_group_state_dict_buffer["preemptDelay"]["type"] = "Property"
                                                                interface_address_vrrp_group_state_dict_buffer["preemptDelay"]["value"] = int(element_text)
                                                                interface_address_vrrp_group_state_dict_buffer["preemptDelay"]["observedAt"] = observed_at
                                                            if child_node == "accept-mode":
                                                                interface_address_vrrp_group_state_dict_buffer["acceptMode"] = {}
                                                                interface_address_vrrp_group_state_dict_buffer["acceptMode"]["type"] = "Property"
                                                                interface_address_vrrp_group_state_dict_buffer["acceptMode"]["value"] = eval(str(element_text).capitalize())
                                                                interface_address_vrrp_group_state_dict_buffer["acceptMode"]["observedAt"] = observed_at
                                                            if child_node == "advertisement-interval":
                                                                interface_address_vrrp_group_state_dict_buffer["advertisementInterval"] = {}
                                                                interface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["type"] = "Property"
                                                                interface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["value"] = int(element_text)
                                                                interface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["observedAt"] = observed_at
                                                            if child_node == "current-priority":
                                                                interface_address_vrrp_group_state_dict_buffer["currentPriority"] = {}
                                                                interface_address_vrrp_group_state_dict_buffer["currentPriority"]["type"] = "Property"
                                                                interface_address_vrrp_group_state_dict_buffer["currentPriority"]["value"] = int(element_text)
                                                                interface_address_vrrp_group_state_dict_buffer["currentPriority"]["observedAt"] = observed_at
                                                            if child_node == "virtual-link-local":
                                                                interface_address_vrrp_group_state_dict_buffer["virtualLinkLocal"] = {}
                                                                interface_address_vrrp_group_state_dict_buffer["virtualLinkLocal"]["type"] = "Property"
                                                                interface_address_vrrp_group_state_dict_buffer["virtualLinkLocal"]["value"] = element_text
                                                                interface_address_vrrp_group_state_dict_buffer["virtualLinkLocal"]["observedAt"] = observed_at
                                                            if len(parent_path) - 1 == 11:
                                                                dict_buffers.append(interface_address_vrrp_group_state_dict_buffer)
                                                    if parent_path[11] == "interface-tracking":
                                                        if parent_path[12] == "config":
                                                            interface_address_vrrp_group_config_dict_buffer = {}
                                                            interface_address_vrrp_group_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig:" + interface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                            interface_address_vrrp_group_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig"
                                                            if len(parent_path) - 1 == 12 or len(parent_path) - 1 == 13:
                                                                interface_address_vrrp_group_config_dict_buffer["isPartOf"] = {}
                                                                interface_address_vrrp_group_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                interface_address_vrrp_group_config_dict_buffer["isPartOf"]["object"] = interface_address_vrrp_group_dict_buffer["id"]
                                                                interface_address_vrrp_group_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                if len(parent_path) - 1 == 12 or len(parent_path) - 1 == 13:
                                                                    interface_address_vrrp_group_config_dict_buffer["trackInterface"] = {}
                                                                    interface_address_vrrp_group_config_dict_buffer["trackInterface"]["type"] = "Relationship"
                                                                    interface_address_vrrp_group_config_dict_buffer["trackInterface"]["object"] = "urn:ngsi-ld:Interface:" + interface_address_vrrp_group_config_dict_buffer["id"].split(":")[-1]
                                                                    interface_address_vrrp_group_config_dict_buffer["trackInterface"]["observedAt"] = observed_at
                                                                if child_node == "priority-decrement":
                                                                    interface_address_vrrp_group_config_dict_buffer["priorityDecrement"] = {}
                                                                    interface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["type"] = "Property"
                                                                    interface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["value"] = int(element_text)
                                                                    interface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["observedAt"] = observed_at
                                                                if len(parent_path) - 1 == 12:
                                                                    dict_buffers.append(interface_address_vrrp_group_config_dict_buffer)
                                                            if parent_path[13] == "state":
                                                                interface_address_vrrp_group_state_dict_buffer = {}
                                                                interface_address_vrrp_group_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupInterfaceTrackingState:" + interface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                interface_address_vrrp_group_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupInterfaceTrackingState"
                                                                if len(parent_path) - 1 == 13 or len(parent_path) - 1 == 14:
                                                                    interface_address_vrrp_group_state_dict_buffer["isPartOf"] = {}
                                                                    interface_address_vrrp_group_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                    interface_address_vrrp_group_state_dict_buffer["isPartOf"]["object"] = interface_address_vrrp_group_dict_buffer["id"]
                                                                    interface_address_vrrp_group_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                    if len(parent_path) - 1 == 13 or len(parent_path) - 1 == 14:
                                                                        interface_address_vrrp_group_state_dict_buffer["trackInterface"] = {}
                                                                        interface_address_vrrp_group_state_dict_buffer["trackInterface"]["type"] = "Relationship"
                                                                        interface_address_vrrp_group_state_dict_buffer["trackInterface"]["object"] = "urn:ngsi-ld:Interface:" + interface_address_vrrp_group_state_dict_buffer["id"].split(":")[-1]
                                                                        interface_address_vrrp_group_state_dict_buffer["trackInterface"]["observedAt"] = observed_at
                                                                    if child_node == "priority-decrement":
                                                                        interface_address_vrrp_group_state_dict_buffer["priorityDecrement"] = {}
                                                                        interface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["type"] = "Property"
                                                                        interface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["value"] = int(element_text)
                                                                        interface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["observedAt"] = observed_at
                                                                    if len(parent_path) - 1 == 13:
                                                                        dict_buffers.append(interface_address_vrrp_group_state_dict_buffer)
                                                    if len(parent_path) - 1 == 10:
                                                        dict_buffers.append(interface_address_vrrp_group_dict_buffer)
                                        if len(parent_path) - 1 == 8:
                                            dict_buffers.append(interface_address_dict_buffer)
                                if parent_path[8] == "router-advertisement":
                                    if parent_path[9] == "config":
                                        interface_config_dict_buffer = {}
                                        interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6RouterAdvertisementConfig:" + interface_dict_buffer["id"].split(":")[-1]
                                        interface_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv6RouterAdvertisementConfig"
                                        if len(parent_path) - 1 == 9 or len(parent_path) - 1 == 10:
                                            interface_config_dict_buffer["isPartOf"] = {}
                                            interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                            interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                            interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                            if child_node == "interval":
                                                interface_config_dict_buffer["interval"] = {}
                                                interface_config_dict_buffer["interval"]["type"] = "Property"
                                                interface_config_dict_buffer["interval"]["value"] = int(element_text)
                                                interface_config_dict_buffer["interval"]["observedAt"] = observed_at
                                            if child_node == "lifetime":
                                                interface_config_dict_buffer["lifetime"] = {}
                                                interface_config_dict_buffer["lifetime"]["type"] = "Property"
                                                interface_config_dict_buffer["lifetime"]["value"] = int(element_text)
                                                interface_config_dict_buffer["lifetime"]["observedAt"] = observed_at
                                            if child_node == "suppress":
                                                interface_config_dict_buffer["suppress"] = {}
                                                interface_config_dict_buffer["suppress"]["type"] = "Property"
                                                interface_config_dict_buffer["suppress"]["value"] = eval(str(element_text).capitalize())
                                                interface_config_dict_buffer["suppress"]["observedAt"] = observed_at
                                            if len(parent_path) - 1 == 9:
                                                dict_buffers.append(interface_config_dict_buffer)
                                        if parent_path[10] == "state":
                                            interface_state_dict_buffer = {}
                                            interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6RouterAdvertisementState:" + interface_dict_buffer["id"].split(":")[-1]
                                            interface_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv6RouterAdvertisementState"
                                            if len(parent_path) - 1 == 10 or len(parent_path) - 1 == 11:
                                                interface_state_dict_buffer["isPartOf"] = {}
                                                interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                if child_node == "interval":
                                                    interface_state_dict_buffer["interval"] = {}
                                                    interface_state_dict_buffer["interval"]["type"] = "Property"
                                                    interface_state_dict_buffer["interval"]["value"] = int(element_text)
                                                    interface_state_dict_buffer["interval"]["observedAt"] = observed_at
                                                if child_node == "lifetime":
                                                    interface_state_dict_buffer["lifetime"] = {}
                                                    interface_state_dict_buffer["lifetime"]["type"] = "Property"
                                                    interface_state_dict_buffer["lifetime"]["value"] = int(element_text)
                                                    interface_state_dict_buffer["lifetime"]["observedAt"] = observed_at
                                                if child_node == "suppress":
                                                    interface_state_dict_buffer["suppress"] = {}
                                                    interface_state_dict_buffer["suppress"]["type"] = "Property"
                                                    interface_state_dict_buffer["suppress"]["value"] = eval(str(element_text).capitalize())
                                                    interface_state_dict_buffer["suppress"]["observedAt"] = observed_at
                                                if len(parent_path) - 1 == 10:
                                                    dict_buffers.append(interface_state_dict_buffer)
                                    if parent_path[9] == "neighbors":
                                        if parent_path[10] == "neighbor":
                                            interface_neighbor_dict_buffer = {}
                                            if iteration_key.get("interface_neighbor_ip"):
                                                interface_neighbor_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6NeighborsNeighbor:" + iteration_key
                                            interface_neighbor_dict_buffer["type"] = "InterfaceRoutedVlanIpv6NeighborsNeighbor"
                                            if len(parent_path) - 1 == 10 or len(parent_path) - 1 == 11:
                                                interface_neighbor_dict_buffer["isPartOf"] = {}
                                                interface_neighbor_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_neighbor_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                interface_neighbor_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                if len(parent_path) - 1 == 10 or len(parent_path) - 1 == 11:
                                                    if ":" in element_text:
                                                        element_text = element_text.replace(":",".")
                                                    if interface_neighbor_dict_buffer["id"].split(":")[-1] != element_text:
                                                        interface_neighbor_dict_buffer["id"] = interface_neighbor_dict_buffer["id"] + ":" + element_text
                                                    interface_neighbor_dict_buffer["ip"] = {}
                                                    interface_neighbor_dict_buffer["ip"]["type"] = "Relationship"
                                                    interface_neighbor_dict_buffer["ip"]["object"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6NeighborsNeighborConfig:" + interface_neighbor_dict_buffer["id"].split(":")[-1]
                                                    interface_neighbor_dict_buffer["ip"]["observedAt"] = observed_at
                                                if parent_path[11] == "config":
                                                    interface_neighbor_config_dict_buffer = {}
                                                    interface_neighbor_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6NeighborsNeighborConfig:" + interface_neighbor_dict_buffer["id"].split(":")[-1]
                                                    interface_neighbor_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv6NeighborsNeighborConfig"
                                                    if len(parent_path) - 1 == 11 or len(parent_path) - 1 == 12:
                                                        interface_neighbor_config_dict_buffer["isPartOf"] = {}
                                                        interface_neighbor_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_neighbor_config_dict_buffer["isPartOf"]["object"] = interface_neighbor_dict_buffer["id"]
                                                        interface_neighbor_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                        if child_node == "ip":
                                                            interface_neighbor_config_dict_buffer["ip"] = {}
                                                            interface_neighbor_config_dict_buffer["ip"]["type"] = "Property"
                                                            interface_neighbor_config_dict_buffer["ip"]["value"] = element_text
                                                            interface_neighbor_config_dict_buffer["ip"]["observedAt"] = observed_at
                                                        if child_node == "link-layer-address":
                                                            interface_neighbor_config_dict_buffer["linkLayerAddress"] = {}
                                                            interface_neighbor_config_dict_buffer["linkLayerAddress"]["type"] = "Property"
                                                            interface_neighbor_config_dict_buffer["linkLayerAddress"]["value"] = element_text
                                                            interface_neighbor_config_dict_buffer["linkLayerAddress"]["observedAt"] = observed_at
                                                        if len(parent_path) - 1 == 11:
                                                            dict_buffers.append(interface_neighbor_config_dict_buffer)
                                                if parent_path[11] == "state":
                                                    interface_neighbor_state_dict_buffer = {}
                                                    interface_neighbor_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6NeighborsNeighborState:" + interface_neighbor_dict_buffer["id"].split(":")[-1]
                                                    interface_neighbor_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv6NeighborsNeighborState"
                                                    if len(parent_path) - 1 == 11 or len(parent_path) - 1 == 12:
                                                        interface_neighbor_state_dict_buffer["isPartOf"] = {}
                                                        interface_neighbor_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_neighbor_state_dict_buffer["isPartOf"]["object"] = interface_neighbor_dict_buffer["id"]
                                                        interface_neighbor_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                        if child_node == "ip":
                                                            interface_neighbor_state_dict_buffer["ip"] = {}
                                                            interface_neighbor_state_dict_buffer["ip"]["type"] = "Property"
                                                            interface_neighbor_state_dict_buffer["ip"]["value"] = element_text
                                                            interface_neighbor_state_dict_buffer["ip"]["observedAt"] = observed_at
                                                        if child_node == "link-layer-address":
                                                            interface_neighbor_state_dict_buffer["linkLayerAddress"] = {}
                                                            interface_neighbor_state_dict_buffer["linkLayerAddress"]["type"] = "Property"
                                                            interface_neighbor_state_dict_buffer["linkLayerAddress"]["value"] = element_text
                                                            interface_neighbor_state_dict_buffer["linkLayerAddress"]["observedAt"] = observed_at
                                                        if child_node == "origin":
                                                            interface_neighbor_state_dict_buffer["origin"] = {}
                                                            interface_neighbor_state_dict_buffer["origin"]["type"] = "Property"
                                                            interface_neighbor_state_dict_buffer["origin"]["value"] = element_text
                                                            interface_neighbor_state_dict_buffer["origin"]["observedAt"] = observed_at
                                                        if child_node == "is-router":
                                                            interface_neighbor_state_dict_buffer["isRouter"] = {}
                                                            interface_neighbor_state_dict_buffer["isRouter"]["type"] = "Property"
                                                            interface_neighbor_state_dict_buffer["isRouter"]["value"] = element_text
                                                            interface_neighbor_state_dict_buffer["isRouter"]["observedAt"] = observed_at
                                                        if child_node == "neighbor-state":
                                                            interface_neighbor_state_dict_buffer["neighborState"] = {}
                                                            interface_neighbor_state_dict_buffer["neighborState"]["type"] = "Property"
                                                            interface_neighbor_state_dict_buffer["neighborState"]["value"] = element_text
                                                            interface_neighbor_state_dict_buffer["neighborState"]["observedAt"] = observed_at
                                                        if len(parent_path) - 1 == 11:
                                                            dict_buffers.append(interface_neighbor_state_dict_buffer)
                                                if len(parent_path) - 1 == 10:
                                                    dict_buffers.append(interface_neighbor_dict_buffer)
                                        if parent_path[10] == "unnumbered":
                                            if parent_path[11] == "config":
                                                interface_config_dict_buffer = {}
                                                interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6UnnumberedConfig:" + interface_dict_buffer["id"].split(":")[-1]
                                                interface_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv6UnnumberedConfig"
                                                if len(parent_path) - 1 == 11 or len(parent_path) - 1 == 12:
                                                    interface_config_dict_buffer["isPartOf"] = {}
                                                    interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                    interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    if child_node == "enabled":
                                                        interface_config_dict_buffer["enabled"] = {}
                                                        interface_config_dict_buffer["enabled"]["type"] = "Property"
                                                        interface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                        interface_config_dict_buffer["enabled"]["observedAt"] = observed_at
                                                    if len(parent_path) - 1 == 11:
                                                        dict_buffers.append(interface_config_dict_buffer)
                                                if parent_path[12] == "state":
                                                    interface_state_dict_buffer = {}
                                                    interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6UnnumberedState:" + interface_dict_buffer["id"].split(":")[-1]
                                                    interface_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv6UnnumberedState"
                                                    if len(parent_path) - 1 == 12 or len(parent_path) - 1 == 13:
                                                        interface_state_dict_buffer["isPartOf"] = {}
                                                        interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                        interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                        if child_node == "enabled":
                                                            interface_state_dict_buffer["enabled"] = {}
                                                            interface_state_dict_buffer["enabled"]["type"] = "Property"
                                                            interface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                            interface_state_dict_buffer["enabled"]["observedAt"] = observed_at
                                                        if len(parent_path) - 1 == 12:
                                                            dict_buffers.append(interface_state_dict_buffer)
                                                    if parent_path[13] == "interface-ref":
                                                        if parent_path[14] == "config":
                                                            interface_config_dict_buffer = {}
                                                            interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6UnnumberedInterfaceRefConfig:" + interface_dict_buffer["id"].split(":")[-1]
                                                            interface_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv6UnnumberedInterfaceRefConfig"
                                                            if len(parent_path) - 1 == 14 or len(parent_path) - 1 == 15:
                                                                interface_config_dict_buffer["isPartOf"] = {}
                                                                interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                                interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                if len(parent_path) - 1 == 14 or len(parent_path) - 1 == 15:
                                                                    if interface_config_dict_buffer["id"].split(":")[-1] != element_text:
                                                                        interface_config_dict_buffer["id"] = interface_config_dict_buffer["id"] + element_text
                                                                    interface_config_dict_buffer["interface"] = {}
                                                                    interface_config_dict_buffer["interface"]["type"] = "Relationship"
                                                                    interface_config_dict_buffer["interface"]["object"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6UnnumberedInterfaceRefConfigInterface:" + interface_config_dict_buffer["id"].split(":")[-1]
                                                                    interface_config_dict_buffer["interface"]["observedAt"] = observed_at
                                                                if len(parent_path) - 1 == 14 or len(parent_path) - 1 == 15:
                                                                    if "." + str(element_text) not in interface_config_dict_buffer["id"].split(":")[-1]:
                                                                        interface_config_dict_buffer["id"] = interface_config_dict_buffer["id"] + "." + str(element_text)
                                                                    interface_config_dict_buffer["subinterface"] = {}
                                                                    interface_config_dict_buffer["subinterface"]["type"] = "Relationship"
                                                                    interface_config_dict_buffer["subinterface"]["object"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6UnnumberedInterfaceRefConfigSubinterface:" + interface_config_dict_buffer["id"].split(":")[-1]
                                                                    interface_config_dict_buffer["subinterface"]["observedAt"] = observed_at
                                                                if len(parent_path) - 1 == 14:
                                                                    dict_buffers.append(interface_config_dict_buffer)
                                                            if parent_path[15] == "state":
                                                                interface_state_dict_buffer = {}
                                                                interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6UnnumberedInterfaceRefState:" + interface_dict_buffer["id"].split(":")[-1]
                                                                interface_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv6UnnumberedInterfaceRefState"
                                                                if len(parent_path) - 1 == 15 or len(parent_path) - 1 == 16:
                                                                    interface_state_dict_buffer["isPartOf"] = {}
                                                                    interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                    interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                                    interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                    if len(parent_path) - 1 == 15 or len(parent_path) - 1 == 16:
                                                                        if interface_state_dict_buffer["id"].split(":")[-1] != element_text:
                                                                            interface_state_dict_buffer["id"] = interface_state_dict_buffer["id"] + element_text
                                                                        interface_state_dict_buffer["interface"] = {}
                                                                        interface_state_dict_buffer["interface"]["type"] = "Relationship"
                                                                        interface_state_dict_buffer["interface"]["object"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6UnnumberedInterfaceRefStateInterface:" + interface_state_dict_buffer["id"].split(":")[-1]
                                                                        interface_state_dict_buffer["interface"]["observedAt"] = observed_at
                                                                    if len(parent_path) - 1 == 15 or len(parent_path) - 1 == 16:
                                                                        if "." + str(element_text) not in interface_state_dict_buffer["id"].split(":")[-1]:
                                                                            interface_state_dict_buffer["id"] = interface_state_dict_buffer["id"] + "." + str(element_text)
                                                                        interface_state_dict_buffer["subinterface"] = {}
                                                                        interface_state_dict_buffer["subinterface"]["type"] = "Relationship"
                                                                        interface_state_dict_buffer["subinterface"]["object"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6UnnumberedInterfaceRefStateSubinterface:" + interface_state_dict_buffer["id"].split(":")[-1]
                                                                        interface_state_dict_buffer["subinterface"]["observedAt"] = observed_at
                                                                    if len(parent_path) - 1 == 15:
                                                                        dict_buffers.append(interface_state_dict_buffer)
                                            if parent_path[11] == "config":
                                                interface_config_dict_buffer = {}
                                                interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6Config:" + interface_dict_buffer["id"].split(":")[-1]
                                                interface_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv6Config"
                                                if len(parent_path) - 1 == 11 or len(parent_path) - 1 == 12:
                                                    interface_config_dict_buffer["isPartOf"] = {}
                                                    interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                    interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    if child_node == "enabled":
                                                        interface_config_dict_buffer["enabled"] = {}
                                                        interface_config_dict_buffer["enabled"]["type"] = "Property"
                                                        interface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                        interface_config_dict_buffer["enabled"]["observedAt"] = observed_at
                                                    if child_node == "mtu":
                                                        interface_config_dict_buffer["mtu"] = {}
                                                        interface_config_dict_buffer["mtu"]["type"] = "Property"
                                                        interface_config_dict_buffer["mtu"]["value"] = int(element_text)
                                                        interface_config_dict_buffer["mtu"]["observedAt"] = observed_at
                                                    if child_node == "dup-addr-detect-transmits":
                                                        interface_config_dict_buffer["dupAddrDetectTransmits"] = {}
                                                        interface_config_dict_buffer["dupAddrDetectTransmits"]["type"] = "Property"
                                                        interface_config_dict_buffer["dupAddrDetectTransmits"]["value"] = int(element_text)
                                                        interface_config_dict_buffer["dupAddrDetectTransmits"]["observedAt"] = observed_at
                                                    if child_node == "dhcp-client":
                                                        interface_config_dict_buffer["dhcpClient"] = {}
                                                        interface_config_dict_buffer["dhcpClient"]["type"] = "Property"
                                                        interface_config_dict_buffer["dhcpClient"]["value"] = eval(str(element_text).capitalize())
                                                        interface_config_dict_buffer["dhcpClient"]["observedAt"] = observed_at
                                                    if len(parent_path) - 1 == 11:
                                                        dict_buffers.append(interface_config_dict_buffer)
                                                if parent_path[12] == "state":
                                                    interface_state_dict_buffer = {}
                                                    interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6State:" + interface_dict_buffer["id"].split(":")[-1]
                                                    interface_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv6State"
                                                    if len(parent_path) - 1 == 12 or len(parent_path) - 1 == 13:
                                                        interface_state_dict_buffer["isPartOf"] = {}
                                                        interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                        interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                        if child_node == "enabled":
                                                            interface_state_dict_buffer["enabled"] = {}
                                                            interface_state_dict_buffer["enabled"]["type"] = "Property"
                                                            interface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                            interface_state_dict_buffer["enabled"]["observedAt"] = observed_at
                                                        if child_node == "mtu":
                                                            interface_state_dict_buffer["mtu"] = {}
                                                            interface_state_dict_buffer["mtu"]["type"] = "Property"
                                                            interface_state_dict_buffer["mtu"]["value"] = int(element_text)
                                                            interface_state_dict_buffer["mtu"]["observedAt"] = observed_at
                                                        if child_node == "dup-addr-detect-transmits":
                                                            interface_state_dict_buffer["dupAddrDetectTransmits"] = {}
                                                            interface_state_dict_buffer["dupAddrDetectTransmits"]["type"] = "Property"
                                                            interface_state_dict_buffer["dupAddrDetectTransmits"]["value"] = int(element_text)
                                                            interface_state_dict_buffer["dupAddrDetectTransmits"]["observedAt"] = observed_at
                                                        if child_node == "dhcp-client":
                                                            interface_state_dict_buffer["dhcpClient"] = {}
                                                            interface_state_dict_buffer["dhcpClient"]["type"] = "Property"
                                                            interface_state_dict_buffer["dhcpClient"]["value"] = eval(str(element_text).capitalize())
                                                            interface_state_dict_buffer["dhcpClient"]["observedAt"] = observed_at
                                                        if parent_path[13] == "counters":
                                                            interface_state_counters_dict_buffer = {}
                                                            interface_state_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6StateCounters:" + interface_state_dict_buffer["id"].split(":")[-1]
                                                            interface_state_counters_dict_buffer["type"] = "InterfaceRoutedVlanIpv6StateCounters"
                                                            if len(parent_path) - 1 == 13 or len(parent_path) - 1 == 14:
                                                                interface_state_counters_dict_buffer["isPartOf"] = {}
                                                                interface_state_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                interface_state_counters_dict_buffer["isPartOf"]["object"] = interface_state_dict_buffer["id"]
                                                                interface_state_counters_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                if child_node == "in-pkts":
                                                                    interface_state_counters_dict_buffer["inPkts"] = {}
                                                                    interface_state_counters_dict_buffer["inPkts"]["type"] = "Property"
                                                                    interface_state_counters_dict_buffer["inPkts"]["value"] = int(element_text)
                                                                    interface_state_counters_dict_buffer["inPkts"]["observedAt"] = observed_at
                                                                if child_node == "in-octets":
                                                                    interface_state_counters_dict_buffer["inOctets"] = {}
                                                                    interface_state_counters_dict_buffer["inOctets"]["type"] = "Property"
                                                                    interface_state_counters_dict_buffer["inOctets"]["value"] = int(element_text)
                                                                    interface_state_counters_dict_buffer["inOctets"]["observedAt"] = observed_at
                                                                if child_node == "in-error-pkts":
                                                                    interface_state_counters_dict_buffer["inErrorPkts"] = {}
                                                                    interface_state_counters_dict_buffer["inErrorPkts"]["type"] = "Property"
                                                                    interface_state_counters_dict_buffer["inErrorPkts"]["value"] = int(element_text)
                                                                    interface_state_counters_dict_buffer["inErrorPkts"]["observedAt"] = observed_at
                                                                if child_node == "in-forwarded-pkts":
                                                                    interface_state_counters_dict_buffer["inForwardedPkts"] = {}
                                                                    interface_state_counters_dict_buffer["inForwardedPkts"]["type"] = "Property"
                                                                    interface_state_counters_dict_buffer["inForwardedPkts"]["value"] = int(element_text)
                                                                    interface_state_counters_dict_buffer["inForwardedPkts"]["observedAt"] = observed_at
                                                                if child_node == "in-forwarded-octets":
                                                                    interface_state_counters_dict_buffer["inForwardedOctets"] = {}
                                                                    interface_state_counters_dict_buffer["inForwardedOctets"]["type"] = "Property"
                                                                    interface_state_counters_dict_buffer["inForwardedOctets"]["value"] = int(element_text)
                                                                    interface_state_counters_dict_buffer["inForwardedOctets"]["observedAt"] = observed_at
                                                                if child_node == "in-discarded-pkts":
                                                                    interface_state_counters_dict_buffer["inDiscardedPkts"] = {}
                                                                    interface_state_counters_dict_buffer["inDiscardedPkts"]["type"] = "Property"
                                                                    interface_state_counters_dict_buffer["inDiscardedPkts"]["value"] = int(element_text)
                                                                    interface_state_counters_dict_buffer["inDiscardedPkts"]["observedAt"] = observed_at
                                                                if child_node == "out-pkts":
                                                                    interface_state_counters_dict_buffer["outPkts"] = {}
                                                                    interface_state_counters_dict_buffer["outPkts"]["type"] = "Property"
                                                                    interface_state_counters_dict_buffer["outPkts"]["value"] = int(element_text)
                                                                    interface_state_counters_dict_buffer["outPkts"]["observedAt"] = observed_at
                                                                if child_node == "out-octets":
                                                                    interface_state_counters_dict_buffer["outOctets"] = {}
                                                                    interface_state_counters_dict_buffer["outOctets"]["type"] = "Property"
                                                                    interface_state_counters_dict_buffer["outOctets"]["value"] = int(element_text)
                                                                    interface_state_counters_dict_buffer["outOctets"]["observedAt"] = observed_at
                                                                if child_node == "out-error-pkts":
                                                                    interface_state_counters_dict_buffer["outErrorPkts"] = {}
                                                                    interface_state_counters_dict_buffer["outErrorPkts"]["type"] = "Property"
                                                                    interface_state_counters_dict_buffer["outErrorPkts"]["value"] = int(element_text)
                                                                    interface_state_counters_dict_buffer["outErrorPkts"]["observedAt"] = observed_at
                                                                if child_node == "out-forwarded-pkts":
                                                                    interface_state_counters_dict_buffer["outForwardedPkts"] = {}
                                                                    interface_state_counters_dict_buffer["outForwardedPkts"]["type"] = "Property"
                                                                    interface_state_counters_dict_buffer["outForwardedPkts"]["value"] = int(element_text)
                                                                    interface_state_counters_dict_buffer["outForwardedPkts"]["observedAt"] = observed_at
                                                                if child_node == "out-forwarded-octets":
                                                                    interface_state_counters_dict_buffer["outForwardedOctets"] = {}
                                                                    interface_state_counters_dict_buffer["outForwardedOctets"]["type"] = "Property"
                                                                    interface_state_counters_dict_buffer["outForwardedOctets"]["value"] = int(element_text)
                                                                    interface_state_counters_dict_buffer["outForwardedOctets"]["observedAt"] = observed_at
                                                                if child_node == "out-discarded-pkts":
                                                                    interface_state_counters_dict_buffer["outDiscardedPkts"] = {}
                                                                    interface_state_counters_dict_buffer["outDiscardedPkts"]["type"] = "Property"
                                                                    interface_state_counters_dict_buffer["outDiscardedPkts"]["value"] = int(element_text)
                                                                    interface_state_counters_dict_buffer["outDiscardedPkts"]["observedAt"] = observed_at
                                                                if len(parent_path) - 1 == 13:
                                                                    dict_buffers.append(interface_state_counters_dict_buffer)
                                                        if len(parent_path) - 1 == 12:
                                                            dict_buffers.append(interface_state_dict_buffer)
        if len(parent_path) - 1 == 1:
            dict_buffers.append(interface_dict_buffer)
    if parent_path[0] == "openconfig-vlan:vlans" or parent_path[0] == "vlans":
        if parent_path[1] == "vlan":
            vlan_dict_buffer = {}
            if iteration_key.get("vlan_vlan-id"):
                vlan_dict_buffer["id"] = "urn:ngsi-ld:Vlan:" + iteration_key.get("vlan_vlan-id")
            vlan_dict_buffer["type"] = "Vlan"
        if len(parent_path) - 1 == 1 or len(parent_path) - 1 == 2:
            if vlan_dict_buffer["id"].split(":")[-1] != element_text:
                vlan_dict_buffer["id"] = vlan_dict_buffer["id"] + element_text
            vlan_dict_buffer["vlanId"] = {}
            vlan_dict_buffer["vlanId"]["type"] = "Relationship"
            vlan_dict_buffer["vlanId"]["object"] = "urn:ngsi-ld:VlanConfig:" + vlan_dict_buffer["id"].split(":")[-1]
            vlan_dict_buffer["vlanId"]["observedAt"] = observed_at
        if parent_path[2] == "config":
            vlan_config_dict_buffer = {}
            vlan_config_dict_buffer["id"] = "urn:ngsi-ld:VlanConfig:" + vlan_dict_buffer["id"].split(":")[-1]
            vlan_config_dict_buffer["type"] = "VlanConfig"
            if len(parent_path) - 1 == 2 or len(parent_path) - 1 == 3:
                vlan_config_dict_buffer["isPartOf"] = {}
                vlan_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                vlan_config_dict_buffer["isPartOf"]["object"] = vlan_dict_buffer["id"]
                vlan_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                if child_node == "vlan-id":
                    if vlan_config_dict_buffer["id"].split(":")[-1] != int(element_text):
                        vlan_config_dict_buffer["id"] = vlan_config_dict_buffer["id"] + int(element_text)
                    vlan_config_dict_buffer["vlanId"] = {}
                    vlan_config_dict_buffer["vlanId"]["type"] = "Property"
                    vlan_config_dict_buffer["vlanId"]["value"] = int(element_text)
                    vlan_config_dict_buffer["vlanId"]["observedAt"] = observed_at
                if child_node == "name":
                    if vlan_config_dict_buffer["id"].split(":")[-1] != element_text:
                        vlan_config_dict_buffer["id"] = vlan_config_dict_buffer["id"] + element_text
                    vlan_config_dict_buffer["name"] = {}
                    vlan_config_dict_buffer["name"]["type"] = "Property"
                    vlan_config_dict_buffer["name"]["value"] = element_text
                    vlan_config_dict_buffer["name"]["observedAt"] = observed_at
                if child_node == "status":
                    vlan_config_dict_buffer["status"] = {}
                    vlan_config_dict_buffer["status"]["type"] = "Property"
                    vlan_config_dict_buffer["status"]["value"] = element_text
                    vlan_config_dict_buffer["status"]["observedAt"] = observed_at
                if len(parent_path) - 1 == 2:
                    dict_buffers.append(vlan_config_dict_buffer)
        if parent_path[2] == "state":
            vlan_state_dict_buffer = {}
            vlan_state_dict_buffer["id"] = "urn:ngsi-ld:VlanState:" + vlan_dict_buffer["id"].split(":")[-1]
            vlan_state_dict_buffer["type"] = "VlanState"
            if len(parent_path) - 1 == 2 or len(parent_path) - 1 == 3:
                vlan_state_dict_buffer["isPartOf"] = {}
                vlan_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                vlan_state_dict_buffer["isPartOf"]["object"] = vlan_dict_buffer["id"]
                vlan_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                if child_node == "vlan-id":
                    if vlan_state_dict_buffer["id"].split(":")[-1] != int(element_text):
                        vlan_state_dict_buffer["id"] = vlan_state_dict_buffer["id"] + int(element_text)
                    vlan_state_dict_buffer["vlanId"] = {}
                    vlan_state_dict_buffer["vlanId"]["type"] = "Property"
                    vlan_state_dict_buffer["vlanId"]["value"] = int(element_text)
                    vlan_state_dict_buffer["vlanId"]["observedAt"] = observed_at
                if child_node == "name":
                    if vlan_state_dict_buffer["id"].split(":")[-1] != element_text:
                        vlan_state_dict_buffer["id"] = vlan_state_dict_buffer["id"] + element_text
                    vlan_state_dict_buffer["name"] = {}
                    vlan_state_dict_buffer["name"]["type"] = "Property"
                    vlan_state_dict_buffer["name"]["value"] = element_text
                    vlan_state_dict_buffer["name"]["observedAt"] = observed_at
                if child_node == "status":
                    vlan_state_dict_buffer["status"] = {}
                    vlan_state_dict_buffer["status"]["type"] = "Property"
                    vlan_state_dict_buffer["status"]["value"] = element_text
                    vlan_state_dict_buffer["status"]["observedAt"] = observed_at
                if len(parent_path) - 1 == 2:
                    dict_buffers.append(vlan_state_dict_buffer)
        if parent_path[2] == "members":
            if parent_path[3] == "member":
                vlan_member_dict_buffer = {}
                vlan_member_dict_buffer["id"] = "urn:ngsi-ld:VlanMembersMember:" + vlan_dict_buffer["id"].split(":")[-1]
                vlan_member_dict_buffer["type"] = "VlanMembersMember"
                if len(parent_path) - 1 == 3 or len(parent_path) - 1 == 4:
                    vlan_member_dict_buffer["isPartOf"] = {}
                    vlan_member_dict_buffer["isPartOf"]["type"] = "Relationship"
                    vlan_member_dict_buffer["isPartOf"]["object"] = vlan_dict_buffer["id"]
                    vlan_member_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    if parent_path[4] == "state":
                        vlan_member_state_dict_buffer = {}
                        vlan_member_state_dict_buffer["id"] = "urn:ngsi-ld:VlanMembersMemberState:" + vlan_member_dict_buffer["id"].split(":")[-1]
                        vlan_member_state_dict_buffer["type"] = "VlanMembersMemberState"
                        if len(parent_path) - 1 == 4 or len(parent_path) - 1 == 5:
                            vlan_member_state_dict_buffer["isPartOf"] = {}
                            vlan_member_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                            vlan_member_state_dict_buffer["isPartOf"]["object"] = vlan_member_dict_buffer["id"]
                            vlan_member_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                            if len(parent_path) - 1 == 4 or len(parent_path) - 1 == 5:
                                if vlan_member_state_dict_buffer["id"].split(":")[-1] != element_text:
                                    vlan_member_state_dict_buffer["id"] = vlan_member_state_dict_buffer["id"] + element_text
                                vlan_member_state_dict_buffer["interface"] = {}
                                vlan_member_state_dict_buffer["interface"]["type"] = "Relationship"
                                vlan_member_state_dict_buffer["interface"]["object"] = "urn:ngsi-ld:VlanMembersMemberStateInterface:" + vlan_member_state_dict_buffer["id"].split(":")[-1]
                                vlan_member_state_dict_buffer["interface"]["observedAt"] = observed_at
                            if len(parent_path) - 1 == 4:
                                dict_buffers.append(vlan_member_state_dict_buffer)
                    if len(parent_path) - 1 == 3:
                        dict_buffers.append(vlan_member_dict_buffer)
        if len(parent_path) - 1 == 1:
            dict_buffers.append(vlan_dict_buffer)

dict_buffer_combinated = defaultdict(dict)
for dict_buffer in dict_buffers:
    key = (dict_buffer["id"], dict_buffer["type"])
    if key not in dict_buffer_combinated:
        dict_buffer_combinated[key] = dict_buffer
    else:
        dict_buffer_combinated[key].update(dict_buffer)
dict_buffers = list(dict_buffer_combinated.values())

output_file = open("dict_buffers_notifications.json", 'w')
output_file.write(json.dumps(dict_buffers[::-1], indent=4))
output_file.close()
dict_buffers.clear()
