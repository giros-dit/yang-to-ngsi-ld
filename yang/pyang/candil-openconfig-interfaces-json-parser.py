import json
import sys

json_payload = sys.argv[1]
dict_buffers = []
with open(json_payload) as f:
    data = json.load(f)
    json_data = data[0]["updates"][0]["values"]

if isinstance(json_data.get("interfaces"), dict):
    interfaces = json_data.get("interfaces")
    if interfaces is not None:
        interfaces = interfaces.get("interface")
        for interface in interfaces:
            interface_dict_buffer = {}
            interface_dict_buffer["id"] = "urn:ngsi-ld:Interface:"
            interface_dict_buffer["type"] = "Interface"
            name = interface.get("name")
            if name is not None:
                element_text = name
                if interface_dict_buffer["id"].split(":")[-1] != element_text:
                    interface_dict_buffer["id"] = interface_dict_buffer["id"] + element_text
                interface_dict_buffer["name"] = {}
                interface_dict_buffer["name"]["type"] = "Relationship"
                interface_dict_buffer["name"]["object"] = "urn:ngsi-ld:InterfaceConfig:" + interface_dict_buffer["id"].split(":")[-1]
            if isinstance(interface.get("config"), dict):
                config = interface.get("config")
                interface_config_dict_buffer = {}
                interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceConfig:" + interface_dict_buffer["id"].split(":")[-1]
                interface_config_dict_buffer["type"] = "InterfaceConfig"
                interface_config_dict_buffer["isPartOf"] = {}
                interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                name = config.get("name")
                if name is not None:
                    element_text = name
                    if interface_config_dict_buffer["id"].split(":")[-1] != element_text:
                        interface_config_dict_buffer["id"] = interface_config_dict_buffer["id"] + element_text
                    interface_config_dict_buffer["name"] = {}
                    interface_config_dict_buffer["name"]["type"] = "Property"
                    interface_config_dict_buffer["name"]["value"] = element_text
                type = config.get("type")
                if type is not None:
                        interface_config_dict_buffer["configType"] = {}
                        interface_config_dict_buffer["configType"]["type"] = "Relationship"
                        interface_config_dict_buffer["configType"]["object"] = "urn:ngsi-ld:YANGIdentity:" + element_text
                mtu = config.get("mtu")
                if mtu is not None:
                    element_text = mtu
                    interface_config_dict_buffer["mtu"] = {}
                    interface_config_dict_buffer["mtu"]["type"] = "Property"
                    interface_config_dict_buffer["mtu"]["value"] = int(element_text)
                loopbackMode = config.get("loopback-mode")
                if loopbackMode is not None:
                    element_text = loopbackMode
                    interface_config_dict_buffer["loopbackMode"] = {}
                    interface_config_dict_buffer["loopbackMode"]["type"] = "Property"
                    interface_config_dict_buffer["loopbackMode"]["value"] = eval(str(element_text).capitalize())
                description = config.get("description")
                if description is not None:
                    element_text = description
                    interface_config_dict_buffer["description"] = {}
                    interface_config_dict_buffer["description"]["type"] = "Property"
                    interface_config_dict_buffer["description"]["value"] = element_text
                enabled = config.get("enabled")
                if enabled is not None:
                    element_text = enabled
                    interface_config_dict_buffer["enabled"] = {}
                    interface_config_dict_buffer["enabled"]["type"] = "Property"
                    interface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                dict_buffers.append(interface_config_dict_buffer)
            if isinstance(interface.get("state"), dict):
                state = interface.get("state")
                interface_state_dict_buffer = {}
                interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceState:" + interface_dict_buffer["id"].split(":")[-1]
                interface_state_dict_buffer["type"] = "InterfaceState"
                interface_state_dict_buffer["isPartOf"] = {}
                interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                name = state.get("name")
                if name is not None:
                    element_text = name
                    if interface_state_dict_buffer["id"].split(":")[-1] != element_text:
                        interface_state_dict_buffer["id"] = interface_state_dict_buffer["id"] + element_text
                    interface_state_dict_buffer["name"] = {}
                    interface_state_dict_buffer["name"]["type"] = "Property"
                    interface_state_dict_buffer["name"]["value"] = element_text
                type = state.get("type")
                if type is not None:
                        interface_state_dict_buffer["stateType"] = {}
                        interface_state_dict_buffer["stateType"]["type"] = "Relationship"
                        interface_state_dict_buffer["stateType"]["object"] = "urn:ngsi-ld:YANGIdentity:" + element_text
                mtu = state.get("mtu")
                if mtu is not None:
                    element_text = mtu
                    interface_state_dict_buffer["mtu"] = {}
                    interface_state_dict_buffer["mtu"]["type"] = "Property"
                    interface_state_dict_buffer["mtu"]["value"] = int(element_text)
                loopbackMode = state.get("loopback-mode")
                if loopbackMode is not None:
                    element_text = loopbackMode
                    interface_state_dict_buffer["loopbackMode"] = {}
                    interface_state_dict_buffer["loopbackMode"]["type"] = "Property"
                    interface_state_dict_buffer["loopbackMode"]["value"] = eval(str(element_text).capitalize())
                description = state.get("description")
                if description is not None:
                    element_text = description
                    interface_state_dict_buffer["description"] = {}
                    interface_state_dict_buffer["description"]["type"] = "Property"
                    interface_state_dict_buffer["description"]["value"] = element_text
                enabled = state.get("enabled")
                if enabled is not None:
                    element_text = enabled
                    interface_state_dict_buffer["enabled"] = {}
                    interface_state_dict_buffer["enabled"]["type"] = "Property"
                    interface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                ifindex = state.get("ifindex")
                if ifindex is not None:
                    element_text = ifindex
                    interface_state_dict_buffer["ifindex"] = {}
                    interface_state_dict_buffer["ifindex"]["type"] = "Property"
                    interface_state_dict_buffer["ifindex"]["value"] = int(element_text)
                adminStatus = state.get("admin-status")
                if adminStatus is not None:
                    element_text = adminStatus
                    interface_state_dict_buffer["adminStatus"] = {}
                    interface_state_dict_buffer["adminStatus"]["type"] = "Property"
                    interface_state_dict_buffer["adminStatus"]["value"] = element_text
                operStatus = state.get("oper-status")
                if operStatus is not None:
                    element_text = operStatus
                    interface_state_dict_buffer["operStatus"] = {}
                    interface_state_dict_buffer["operStatus"]["type"] = "Property"
                    interface_state_dict_buffer["operStatus"]["value"] = element_text
                lastChange = state.get("last-change")
                if lastChange is not None:
                    element_text = lastChange
                    interface_state_dict_buffer["lastChange"] = {}
                    interface_state_dict_buffer["lastChange"]["type"] = "Property"
                    interface_state_dict_buffer["lastChange"]["value"] = int(element_text)
                if isinstance(state.get("counters"), dict):
                    counters = state.get("counters")
                    interface_state_counters_dict_buffer = {}
                    interface_state_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceStateCounters:" + interface_state_dict_buffer["id"].split(":")[-1]
                    interface_state_counters_dict_buffer["type"] = "InterfaceStateCounters"
                    interface_state_counters_dict_buffer["isPartOf"] = {}
                    interface_state_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_state_counters_dict_buffer["isPartOf"]["object"] = interface_state_dict_buffer["id"]
                    inOctets = counters.get("in-octets")
                    if inOctets is not None:
                        element_text = inOctets
                        interface_state_counters_dict_buffer["inOctets"] = {}
                        interface_state_counters_dict_buffer["inOctets"]["type"] = "Property"
                        interface_state_counters_dict_buffer["inOctets"]["value"] = int(element_text)
                    inUnicastPkts = counters.get("in-unicast-pkts")
                    if inUnicastPkts is not None:
                        element_text = inUnicastPkts
                        interface_state_counters_dict_buffer["inUnicastPkts"] = {}
                        interface_state_counters_dict_buffer["inUnicastPkts"]["type"] = "Property"
                        interface_state_counters_dict_buffer["inUnicastPkts"]["value"] = int(element_text)
                    inBroadcastPkts = counters.get("in-broadcast-pkts")
                    if inBroadcastPkts is not None:
                        element_text = inBroadcastPkts
                        interface_state_counters_dict_buffer["inBroadcastPkts"] = {}
                        interface_state_counters_dict_buffer["inBroadcastPkts"]["type"] = "Property"
                        interface_state_counters_dict_buffer["inBroadcastPkts"]["value"] = int(element_text)
                    inMulticastPkts = counters.get("in-multicast-pkts")
                    if inMulticastPkts is not None:
                        element_text = inMulticastPkts
                        interface_state_counters_dict_buffer["inMulticastPkts"] = {}
                        interface_state_counters_dict_buffer["inMulticastPkts"]["type"] = "Property"
                        interface_state_counters_dict_buffer["inMulticastPkts"]["value"] = int(element_text)
                    inDiscards = counters.get("in-discards")
                    if inDiscards is not None:
                        element_text = inDiscards
                        interface_state_counters_dict_buffer["inDiscards"] = {}
                        interface_state_counters_dict_buffer["inDiscards"]["type"] = "Property"
                        interface_state_counters_dict_buffer["inDiscards"]["value"] = int(element_text)
                    inErrors = counters.get("in-errors")
                    if inErrors is not None:
                        element_text = inErrors
                        interface_state_counters_dict_buffer["inErrors"] = {}
                        interface_state_counters_dict_buffer["inErrors"]["type"] = "Property"
                        interface_state_counters_dict_buffer["inErrors"]["value"] = int(element_text)
                    inUnknownProtos = counters.get("in-unknown-protos")
                    if inUnknownProtos is not None:
                        element_text = inUnknownProtos
                        interface_state_counters_dict_buffer["inUnknownProtos"] = {}
                        interface_state_counters_dict_buffer["inUnknownProtos"]["type"] = "Property"
                        interface_state_counters_dict_buffer["inUnknownProtos"]["value"] = int(element_text)
                    inFcsErrors = counters.get("in-fcs-errors")
                    if inFcsErrors is not None:
                        element_text = inFcsErrors
                        interface_state_counters_dict_buffer["inFcsErrors"] = {}
                        interface_state_counters_dict_buffer["inFcsErrors"]["type"] = "Property"
                        interface_state_counters_dict_buffer["inFcsErrors"]["value"] = int(element_text)
                    outOctets = counters.get("out-octets")
                    if outOctets is not None:
                        element_text = outOctets
                        interface_state_counters_dict_buffer["outOctets"] = {}
                        interface_state_counters_dict_buffer["outOctets"]["type"] = "Property"
                        interface_state_counters_dict_buffer["outOctets"]["value"] = int(element_text)
                    outUnicastPkts = counters.get("out-unicast-pkts")
                    if outUnicastPkts is not None:
                        element_text = outUnicastPkts
                        interface_state_counters_dict_buffer["outUnicastPkts"] = {}
                        interface_state_counters_dict_buffer["outUnicastPkts"]["type"] = "Property"
                        interface_state_counters_dict_buffer["outUnicastPkts"]["value"] = int(element_text)
                    outBroadcastPkts = counters.get("out-broadcast-pkts")
                    if outBroadcastPkts is not None:
                        element_text = outBroadcastPkts
                        interface_state_counters_dict_buffer["outBroadcastPkts"] = {}
                        interface_state_counters_dict_buffer["outBroadcastPkts"]["type"] = "Property"
                        interface_state_counters_dict_buffer["outBroadcastPkts"]["value"] = int(element_text)
                    outMulticastPkts = counters.get("out-multicast-pkts")
                    if outMulticastPkts is not None:
                        element_text = outMulticastPkts
                        interface_state_counters_dict_buffer["outMulticastPkts"] = {}
                        interface_state_counters_dict_buffer["outMulticastPkts"]["type"] = "Property"
                        interface_state_counters_dict_buffer["outMulticastPkts"]["value"] = int(element_text)
                    outDiscards = counters.get("out-discards")
                    if outDiscards is not None:
                        element_text = outDiscards
                        interface_state_counters_dict_buffer["outDiscards"] = {}
                        interface_state_counters_dict_buffer["outDiscards"]["type"] = "Property"
                        interface_state_counters_dict_buffer["outDiscards"]["value"] = int(element_text)
                    outErrors = counters.get("out-errors")
                    if outErrors is not None:
                        element_text = outErrors
                        interface_state_counters_dict_buffer["outErrors"] = {}
                        interface_state_counters_dict_buffer["outErrors"]["type"] = "Property"
                        interface_state_counters_dict_buffer["outErrors"]["value"] = int(element_text)
                    carrierTransitions = counters.get("carrier-transitions")
                    if carrierTransitions is not None:
                        element_text = carrierTransitions
                        interface_state_counters_dict_buffer["carrierTransitions"] = {}
                        interface_state_counters_dict_buffer["carrierTransitions"]["type"] = "Property"
                        interface_state_counters_dict_buffer["carrierTransitions"]["value"] = int(element_text)
                    lastClear = counters.get("last-clear")
                    if lastClear is not None:
                        element_text = lastClear
                        interface_state_counters_dict_buffer["lastClear"] = {}
                        interface_state_counters_dict_buffer["lastClear"]["type"] = "Property"
                        interface_state_counters_dict_buffer["lastClear"]["value"] = int(element_text)
                    dict_buffers.append(interface_state_counters_dict_buffer)
                dict_buffers.append(interface_state_dict_buffer)
            if isinstance(interface.get("config"), dict):
                config = interface.get("config")
                interface_config_dict_buffer = {}
                interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceHoldTimeConfig:" + interface_dict_buffer["id"].split(":")[-1]
                interface_config_dict_buffer["type"] = "InterfaceHoldTimeConfig"
                interface_config_dict_buffer["isPartOf"] = {}
                interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                up = config.get("up")
                if up is not None:
                    element_text = up
                    interface_config_dict_buffer["up"] = {}
                    interface_config_dict_buffer["up"]["type"] = "Property"
                    interface_config_dict_buffer["up"]["value"] = int(element_text)
                down = config.get("down")
                if down is not None:
                    element_text = down
                    interface_config_dict_buffer["down"] = {}
                    interface_config_dict_buffer["down"]["type"] = "Property"
                    interface_config_dict_buffer["down"]["value"] = int(element_text)
                dict_buffers.append(interface_config_dict_buffer)
            if isinstance(interface.get("state"), dict):
                state = interface.get("state")
                interface_state_dict_buffer = {}
                interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceHoldTimeState:" + interface_dict_buffer["id"].split(":")[-1]
                interface_state_dict_buffer["type"] = "InterfaceHoldTimeState"
                interface_state_dict_buffer["isPartOf"] = {}
                interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                up = state.get("up")
                if up is not None:
                    element_text = up
                    interface_state_dict_buffer["up"] = {}
                    interface_state_dict_buffer["up"]["type"] = "Property"
                    interface_state_dict_buffer["up"]["value"] = int(element_text)
                down = state.get("down")
                if down is not None:
                    element_text = down
                    interface_state_dict_buffer["down"] = {}
                    interface_state_dict_buffer["down"]["type"] = "Property"
                    interface_state_dict_buffer["down"]["value"] = int(element_text)
                dict_buffers.append(interface_state_dict_buffer)
            if isinstance(interface.get("subinterfaces"), dict):
                subinterfaces = interface.get("subinterfaces")
                if subinterfaces is not None:
                    subinterfaces = subinterfaces.get("subinterface")
                    for subinterface in subinterfaces:
                        interface_subinterface_dict_buffer = {}
                        interface_subinterface_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterface:" + interface_dict_buffer["id"].split(":")[-1]
                        interface_subinterface_dict_buffer["type"] = "InterfaceSubinterfacesSubinterface"
                        interface_subinterface_dict_buffer["isPartOf"] = {}
                        interface_subinterface_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_subinterface_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                        index = subinterface.get("index")
                        if index is not None:
                            element_text = index
                            if "." + str(element_text) not in interface_subinterface_dict_buffer["id"].split(":")[-1]:
                                interface_subinterface_dict_buffer["id"] = interface_subinterface_dict_buffer["id"] + "." + str(element_text)
                            interface_subinterface_dict_buffer["index"] = {}
                            interface_subinterface_dict_buffer["index"]["type"] = "Relationship"
                            interface_subinterface_dict_buffer["index"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceConfig:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                        if isinstance(subinterface.get("config"), dict):
                            config = subinterface.get("config")
                            interface_subinterface_config_dict_buffer = {}
                            interface_subinterface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceConfig:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                            interface_subinterface_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceConfig"
                            interface_subinterface_config_dict_buffer["isPartOf"] = {}
                            interface_subinterface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                            interface_subinterface_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                            index = config.get("index")
                            if index is not None:
                                element_text = index
                                if "." + str(element_text) not in interface_subinterface_config_dict_buffer["id"].split(":")[-1]:
                                    interface_subinterface_config_dict_buffer["id"] = interface_subinterface_config_dict_buffer["id"] + "." + str(element_text)
                                interface_subinterface_config_dict_buffer["index"] = {}
                                interface_subinterface_config_dict_buffer["index"]["type"] = "Property"
                                interface_subinterface_config_dict_buffer["index"]["value"] = int(element_text)
                            description = config.get("description")
                            if description is not None:
                                element_text = description
                                interface_subinterface_config_dict_buffer["description"] = {}
                                interface_subinterface_config_dict_buffer["description"]["type"] = "Property"
                                interface_subinterface_config_dict_buffer["description"]["value"] = element_text
                            enabled = config.get("enabled")
                            if enabled is not None:
                                element_text = enabled
                                interface_subinterface_config_dict_buffer["enabled"] = {}
                                interface_subinterface_config_dict_buffer["enabled"]["type"] = "Property"
                                interface_subinterface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                            dict_buffers.append(interface_subinterface_config_dict_buffer)
                        if isinstance(subinterface.get("state"), dict):
                            state = subinterface.get("state")
                            interface_subinterface_state_dict_buffer = {}
                            interface_subinterface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceState:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                            interface_subinterface_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceState"
                            interface_subinterface_state_dict_buffer["isPartOf"] = {}
                            interface_subinterface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                            interface_subinterface_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                            index = state.get("index")
                            if index is not None:
                                element_text = index
                                if "." + str(element_text) not in interface_subinterface_state_dict_buffer["id"].split(":")[-1]:
                                    interface_subinterface_state_dict_buffer["id"] = interface_subinterface_state_dict_buffer["id"] + "." + str(element_text)
                                interface_subinterface_state_dict_buffer["index"] = {}
                                interface_subinterface_state_dict_buffer["index"]["type"] = "Property"
                                interface_subinterface_state_dict_buffer["index"]["value"] = int(element_text)
                            description = state.get("description")
                            if description is not None:
                                element_text = description
                                interface_subinterface_state_dict_buffer["description"] = {}
                                interface_subinterface_state_dict_buffer["description"]["type"] = "Property"
                                interface_subinterface_state_dict_buffer["description"]["value"] = element_text
                            enabled = state.get("enabled")
                            if enabled is not None:
                                element_text = enabled
                                interface_subinterface_state_dict_buffer["enabled"] = {}
                                interface_subinterface_state_dict_buffer["enabled"]["type"] = "Property"
                                interface_subinterface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                            name = state.get("name")
                            if name is not None:
                                element_text = name
                                if interface_subinterface_state_dict_buffer["id"].split(":")[-1] != element_text:
                                    interface_subinterface_state_dict_buffer["id"] = interface_subinterface_state_dict_buffer["id"] + element_text
                                interface_subinterface_state_dict_buffer["name"] = {}
                                interface_subinterface_state_dict_buffer["name"]["type"] = "Property"
                                interface_subinterface_state_dict_buffer["name"]["value"] = element_text
                            ifindex = state.get("ifindex")
                            if ifindex is not None:
                                element_text = ifindex
                                interface_subinterface_state_dict_buffer["ifindex"] = {}
                                interface_subinterface_state_dict_buffer["ifindex"]["type"] = "Property"
                                interface_subinterface_state_dict_buffer["ifindex"]["value"] = int(element_text)
                            adminStatus = state.get("admin-status")
                            if adminStatus is not None:
                                element_text = adminStatus
                                interface_subinterface_state_dict_buffer["adminStatus"] = {}
                                interface_subinterface_state_dict_buffer["adminStatus"]["type"] = "Property"
                                interface_subinterface_state_dict_buffer["adminStatus"]["value"] = element_text
                            operStatus = state.get("oper-status")
                            if operStatus is not None:
                                element_text = operStatus
                                interface_subinterface_state_dict_buffer["operStatus"] = {}
                                interface_subinterface_state_dict_buffer["operStatus"]["type"] = "Property"
                                interface_subinterface_state_dict_buffer["operStatus"]["value"] = element_text
                            lastChange = state.get("last-change")
                            if lastChange is not None:
                                element_text = lastChange
                                interface_subinterface_state_dict_buffer["lastChange"] = {}
                                interface_subinterface_state_dict_buffer["lastChange"]["type"] = "Property"
                                interface_subinterface_state_dict_buffer["lastChange"]["value"] = int(element_text)
                            if isinstance(state.get("counters"), dict):
                                counters = state.get("counters")
                                interface_subinterface_state_counters_dict_buffer = {}
                                interface_subinterface_state_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceStateCounters:" + interface_subinterface_state_dict_buffer["id"].split(":")[-1]
                                interface_subinterface_state_counters_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceStateCounters"
                                interface_subinterface_state_counters_dict_buffer["isPartOf"] = {}
                                interface_subinterface_state_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                                interface_subinterface_state_counters_dict_buffer["isPartOf"]["object"] = interface_subinterface_state_dict_buffer["id"]
                                inOctets = counters.get("in-octets")
                                if inOctets is not None:
                                    element_text = inOctets
                                    interface_subinterface_state_counters_dict_buffer["inOctets"] = {}
                                    interface_subinterface_state_counters_dict_buffer["inOctets"]["type"] = "Property"
                                    interface_subinterface_state_counters_dict_buffer["inOctets"]["value"] = int(element_text)
                                inUnicastPkts = counters.get("in-unicast-pkts")
                                if inUnicastPkts is not None:
                                    element_text = inUnicastPkts
                                    interface_subinterface_state_counters_dict_buffer["inUnicastPkts"] = {}
                                    interface_subinterface_state_counters_dict_buffer["inUnicastPkts"]["type"] = "Property"
                                    interface_subinterface_state_counters_dict_buffer["inUnicastPkts"]["value"] = int(element_text)
                                inBroadcastPkts = counters.get("in-broadcast-pkts")
                                if inBroadcastPkts is not None:
                                    element_text = inBroadcastPkts
                                    interface_subinterface_state_counters_dict_buffer["inBroadcastPkts"] = {}
                                    interface_subinterface_state_counters_dict_buffer["inBroadcastPkts"]["type"] = "Property"
                                    interface_subinterface_state_counters_dict_buffer["inBroadcastPkts"]["value"] = int(element_text)
                                inMulticastPkts = counters.get("in-multicast-pkts")
                                if inMulticastPkts is not None:
                                    element_text = inMulticastPkts
                                    interface_subinterface_state_counters_dict_buffer["inMulticastPkts"] = {}
                                    interface_subinterface_state_counters_dict_buffer["inMulticastPkts"]["type"] = "Property"
                                    interface_subinterface_state_counters_dict_buffer["inMulticastPkts"]["value"] = int(element_text)
                                inDiscards = counters.get("in-discards")
                                if inDiscards is not None:
                                    element_text = inDiscards
                                    interface_subinterface_state_counters_dict_buffer["inDiscards"] = {}
                                    interface_subinterface_state_counters_dict_buffer["inDiscards"]["type"] = "Property"
                                    interface_subinterface_state_counters_dict_buffer["inDiscards"]["value"] = int(element_text)
                                inErrors = counters.get("in-errors")
                                if inErrors is not None:
                                    element_text = inErrors
                                    interface_subinterface_state_counters_dict_buffer["inErrors"] = {}
                                    interface_subinterface_state_counters_dict_buffer["inErrors"]["type"] = "Property"
                                    interface_subinterface_state_counters_dict_buffer["inErrors"]["value"] = int(element_text)
                                inUnknownProtos = counters.get("in-unknown-protos")
                                if inUnknownProtos is not None:
                                    element_text = inUnknownProtos
                                    interface_subinterface_state_counters_dict_buffer["inUnknownProtos"] = {}
                                    interface_subinterface_state_counters_dict_buffer["inUnknownProtos"]["type"] = "Property"
                                    interface_subinterface_state_counters_dict_buffer["inUnknownProtos"]["value"] = int(element_text)
                                inFcsErrors = counters.get("in-fcs-errors")
                                if inFcsErrors is not None:
                                    element_text = inFcsErrors
                                    interface_subinterface_state_counters_dict_buffer["inFcsErrors"] = {}
                                    interface_subinterface_state_counters_dict_buffer["inFcsErrors"]["type"] = "Property"
                                    interface_subinterface_state_counters_dict_buffer["inFcsErrors"]["value"] = int(element_text)
                                outOctets = counters.get("out-octets")
                                if outOctets is not None:
                                    element_text = outOctets
                                    interface_subinterface_state_counters_dict_buffer["outOctets"] = {}
                                    interface_subinterface_state_counters_dict_buffer["outOctets"]["type"] = "Property"
                                    interface_subinterface_state_counters_dict_buffer["outOctets"]["value"] = int(element_text)
                                outUnicastPkts = counters.get("out-unicast-pkts")
                                if outUnicastPkts is not None:
                                    element_text = outUnicastPkts
                                    interface_subinterface_state_counters_dict_buffer["outUnicastPkts"] = {}
                                    interface_subinterface_state_counters_dict_buffer["outUnicastPkts"]["type"] = "Property"
                                    interface_subinterface_state_counters_dict_buffer["outUnicastPkts"]["value"] = int(element_text)
                                outBroadcastPkts = counters.get("out-broadcast-pkts")
                                if outBroadcastPkts is not None:
                                    element_text = outBroadcastPkts
                                    interface_subinterface_state_counters_dict_buffer["outBroadcastPkts"] = {}
                                    interface_subinterface_state_counters_dict_buffer["outBroadcastPkts"]["type"] = "Property"
                                    interface_subinterface_state_counters_dict_buffer["outBroadcastPkts"]["value"] = int(element_text)
                                outMulticastPkts = counters.get("out-multicast-pkts")
                                if outMulticastPkts is not None:
                                    element_text = outMulticastPkts
                                    interface_subinterface_state_counters_dict_buffer["outMulticastPkts"] = {}
                                    interface_subinterface_state_counters_dict_buffer["outMulticastPkts"]["type"] = "Property"
                                    interface_subinterface_state_counters_dict_buffer["outMulticastPkts"]["value"] = int(element_text)
                                outDiscards = counters.get("out-discards")
                                if outDiscards is not None:
                                    element_text = outDiscards
                                    interface_subinterface_state_counters_dict_buffer["outDiscards"] = {}
                                    interface_subinterface_state_counters_dict_buffer["outDiscards"]["type"] = "Property"
                                    interface_subinterface_state_counters_dict_buffer["outDiscards"]["value"] = int(element_text)
                                outErrors = counters.get("out-errors")
                                if outErrors is not None:
                                    element_text = outErrors
                                    interface_subinterface_state_counters_dict_buffer["outErrors"] = {}
                                    interface_subinterface_state_counters_dict_buffer["outErrors"]["type"] = "Property"
                                    interface_subinterface_state_counters_dict_buffer["outErrors"]["value"] = int(element_text)
                                carrierTransitions = counters.get("carrier-transitions")
                                if carrierTransitions is not None:
                                    element_text = carrierTransitions
                                    interface_subinterface_state_counters_dict_buffer["carrierTransitions"] = {}
                                    interface_subinterface_state_counters_dict_buffer["carrierTransitions"]["type"] = "Property"
                                    interface_subinterface_state_counters_dict_buffer["carrierTransitions"]["value"] = int(element_text)
                                lastClear = counters.get("last-clear")
                                if lastClear is not None:
                                    element_text = lastClear
                                    interface_subinterface_state_counters_dict_buffer["lastClear"] = {}
                                    interface_subinterface_state_counters_dict_buffer["lastClear"]["type"] = "Property"
                                    interface_subinterface_state_counters_dict_buffer["lastClear"]["value"] = int(element_text)
                                dict_buffers.append(interface_subinterface_state_counters_dict_buffer)
                            dict_buffers.append(interface_subinterface_state_dict_buffer)
                        dict_buffers.append(interface_subinterface_dict_buffer)
            dict_buffers.append(interface_dict_buffer)

output_file = open("dict_buffers.json", 'w')
output_file.write(json.dumps(dict_buffers[::-1], indent=4))
output_file.close()
dict_buffers.clear()
