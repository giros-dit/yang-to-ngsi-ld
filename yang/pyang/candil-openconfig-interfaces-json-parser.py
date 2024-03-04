import json
import sys

json_payload = sys.argv[1]
dict_buffers = []
with open(json_payload) as f:
    data = json.load(f)
    json_data = data[0]["updates"][0]["values"]

if isinstance(json_data.get("interfaces"), dict):
    interfaces = json_data.get("interfaces")
    if interfaces is not None and len(interfaces) != 0:
        if "interface" in list(interfaces.keys()):
            interfaces = interfaces.get("interface")
        elif "openconfig-interfaces:interface" in list(interfaces.keys()):
            interfaces = interfaces.get("openconfig-interfaces:interface")
        for interface in interfaces:
            if interface is not None and len(interface) != 0:
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
                config = interface.get("config")
                if isinstance(config, dict):
                    if config is not None and len(config) != 0:
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
                        if type is not None and len(type) != 0:
                            element_text = type
                            if element_text is not None:
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
                state = interface.get("state")
                if isinstance(state, dict):
                    if state is not None and len(state) != 0:
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
                        if type is not None and len(type) != 0:
                            element_text = type
                            if element_text is not None:
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
                        counters = state.get("counters")
                        if isinstance(counters, dict):
                            if counters is not None and len(counters) != 0:
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
                hold_time = interface.get("hold-time")
                if isinstance(hold_time, dict):
                    if hold_time is not None and len(hold_time) != 0:
                        config = hold_time.get("config")
                        if isinstance(config, dict):
                            if config is not None and len(config) != 0:
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
                        state = hold_time.get("state")
                        if isinstance(state, dict):
                            if state is not None and len(state) != 0:
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
                subinterfaces = interface.get("subinterfaces")
                if isinstance(subinterfaces, dict):
                    if subinterfaces is not None and len(subinterfaces) != 0:
                        subinterfaces_subinterface = subinterfaces.get("subinterface")
                        for subinterface in subinterfaces_subinterface:
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
                            config = subinterface.get("config")
                            if isinstance(config, dict):
                                if config is not None and len(config) != 0:
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
                            state = subinterface.get("state")
                            if isinstance(state, dict):
                                if state is not None and len(state) != 0:
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
                                    counters = state.get("counters")
                                    if isinstance(counters, dict):
                                        if counters is not None and len(counters) != 0:
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
                            ipv4 = subinterface.get("openconfig-if-ip:ipv4")
                            if isinstance(ipv4, dict):
                                if ipv4 is not None and len(ipv4) != 0:
                                    addresses = ipv4.get("addresses")
                                    if isinstance(addresses, dict):
                                        if addresses is not None and len(addresses) != 0:
                                            addresses_address = addresses.get("address")
                                            for address in addresses_address:
                                                interface_subinterface_address_dict_buffer = {}
                                                interface_subinterface_address_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddress:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                interface_subinterface_address_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4AddressesAddress"
                                                interface_subinterface_address_dict_buffer["isPartOf"] = {}
                                                interface_subinterface_address_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_subinterface_address_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                ip = address.get("ip")
                                                if ip is not None:
                                                    element_text = ip
                                                    if ":" in element_text:
                                                        element_text = element_text.replace(":",".")
                                                    if interface_subinterface_address_dict_buffer["id"].split(":")[-1] != element_text:
                                                        interface_subinterface_address_dict_buffer["id"] = interface_subinterface_address_dict_buffer["id"] + ":" + element_text
                                                    interface_subinterface_address_dict_buffer["ip"] = {}
                                                    interface_subinterface_address_dict_buffer["ip"]["type"] = "Relationship"
                                                    interface_subinterface_address_dict_buffer["ip"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressConfig:" + interface_subinterface_address_dict_buffer["id"].split(":")[-1]
                                                config = address.get("config")
                                                if isinstance(config, dict):
                                                    if config is not None and len(config) != 0:
                                                        interface_subinterface_address_config_dict_buffer = {}
                                                        interface_subinterface_address_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressConfig:" + interface_subinterface_address_dict_buffer["id"].split(":")[-1]
                                                        interface_subinterface_address_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressConfig"
                                                        interface_subinterface_address_config_dict_buffer["isPartOf"] = {}
                                                        interface_subinterface_address_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_subinterface_address_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_dict_buffer["id"]
                                                        ip = config.get("ip")
                                                        if ip is not None:
                                                            element_text = ip
                                                            interface_subinterface_address_config_dict_buffer["ip"] = {}
                                                            interface_subinterface_address_config_dict_buffer["ip"]["type"] = "Property"
                                                            interface_subinterface_address_config_dict_buffer["ip"]["value"] = element_text
                                                        prefixLength = config.get("prefix-length")
                                                        if prefixLength is not None:
                                                            element_text = prefixLength
                                                            interface_subinterface_address_config_dict_buffer["prefixLength"] = {}
                                                            interface_subinterface_address_config_dict_buffer["prefixLength"]["type"] = "Property"
                                                            interface_subinterface_address_config_dict_buffer["prefixLength"]["value"] = int(element_text)
                                                        dict_buffers.append(interface_subinterface_address_config_dict_buffer)
                                                state = address.get("state")
                                                if isinstance(state, dict):
                                                    if state is not None and len(state) != 0:
                                                        interface_subinterface_address_state_dict_buffer = {}
                                                        interface_subinterface_address_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressState:" + interface_subinterface_address_dict_buffer["id"].split(":")[-1]
                                                        interface_subinterface_address_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressState"
                                                        interface_subinterface_address_state_dict_buffer["isPartOf"] = {}
                                                        interface_subinterface_address_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_subinterface_address_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_dict_buffer["id"]
                                                        ip = state.get("ip")
                                                        if ip is not None:
                                                            element_text = ip
                                                            interface_subinterface_address_state_dict_buffer["ip"] = {}
                                                            interface_subinterface_address_state_dict_buffer["ip"]["type"] = "Property"
                                                            interface_subinterface_address_state_dict_buffer["ip"]["value"] = element_text
                                                        prefixLength = state.get("prefix-length")
                                                        if prefixLength is not None:
                                                            element_text = prefixLength
                                                            interface_subinterface_address_state_dict_buffer["prefixLength"] = {}
                                                            interface_subinterface_address_state_dict_buffer["prefixLength"]["type"] = "Property"
                                                            interface_subinterface_address_state_dict_buffer["prefixLength"]["value"] = int(element_text)
                                                        origin = state.get("origin")
                                                        if origin is not None:
                                                            element_text = origin
                                                            interface_subinterface_address_state_dict_buffer["origin"] = {}
                                                            interface_subinterface_address_state_dict_buffer["origin"]["type"] = "Property"
                                                            interface_subinterface_address_state_dict_buffer["origin"]["value"] = element_text
                                                        dict_buffers.append(interface_subinterface_address_state_dict_buffer)
                                                vrrp = address.get("vrrp")
                                                if isinstance(vrrp, dict):
                                                    if vrrp is not None and len(vrrp) != 0:
                                                        vrrp_vrrp_group = vrrp.get("vrrp-group")
                                                        for vrrp_group in vrrp_vrrp_group:
                                                            interface_subinterface_address_vrrp_group_dict_buffer = {}
                                                            interface_subinterface_address_vrrp_group_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroup:" + interface_subinterface_address_dict_buffer["id"].split(":")[-1]
                                                            interface_subinterface_address_vrrp_group_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroup"
                                                            interface_subinterface_address_vrrp_group_dict_buffer["isPartOf"] = {}
                                                            interface_subinterface_address_vrrp_group_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_subinterface_address_vrrp_group_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_dict_buffer["id"]
                                                            virtualRouterId = vrrp_group.get("virtual-router-id")
                                                            if virtualRouterId is not None:
                                                                element_text = virtualRouterId
                                                                if interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1] != element_text:
                                                                    interface_subinterface_address_vrrp_group_dict_buffer["id"] = interface_subinterface_address_vrrp_group_dict_buffer["id"] + element_text
                                                                interface_subinterface_address_vrrp_group_dict_buffer["virtualRouterId"] = {}
                                                                interface_subinterface_address_vrrp_group_dict_buffer["virtualRouterId"]["type"] = "Relationship"
                                                                interface_subinterface_address_vrrp_group_dict_buffer["virtualRouterId"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupConfig:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                            config = vrrp_group.get("config")
                                                            if isinstance(config, dict):
                                                                if config is not None and len(config) != 0:
                                                                    interface_subinterface_address_vrrp_group_config_dict_buffer = {}
                                                                    interface_subinterface_address_vrrp_group_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupConfig:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                    interface_subinterface_address_vrrp_group_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupConfig"
                                                                    interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"] = {}
                                                                    interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                    interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_vrrp_group_dict_buffer["id"]
                                                                    virtualRouterId = config.get("virtual-router-id")
                                                                    if virtualRouterId is not None:
                                                                        element_text = virtualRouterId
                                                                        if interface_subinterface_address_vrrp_group_config_dict_buffer["id"].split(":")[-1] != int(element_text):
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["id"] = interface_subinterface_address_vrrp_group_config_dict_buffer["id"] + int(element_text)
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["virtualRouterId"] = {}
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["value"] = int(element_text)
                                                                    virtualAddress = config.get("virtual-address")
                                                                    if virtualAddress is not None:
                                                                        element_text = virtualAddress
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["virtualAddress"] = {}
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["virtualAddress"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["virtualAddress"]["value"] = element_text
                                                                    priority = config.get("priority")
                                                                    if priority is not None:
                                                                        element_text = priority
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["priority"] = {}
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["priority"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["priority"]["value"] = int(element_text)
                                                                    preempt = config.get("preempt")
                                                                    if preempt is not None:
                                                                        element_text = preempt
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["preempt"] = {}
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["preempt"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["preempt"]["value"] = eval(str(element_text).capitalize())
                                                                    preemptDelay = config.get("preempt-delay")
                                                                    if preemptDelay is not None:
                                                                        element_text = preemptDelay
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["preemptDelay"] = {}
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["preemptDelay"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["preemptDelay"]["value"] = int(element_text)
                                                                    acceptMode = config.get("accept-mode")
                                                                    if acceptMode is not None:
                                                                        element_text = acceptMode
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["acceptMode"] = {}
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["acceptMode"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["acceptMode"]["value"] = eval(str(element_text).capitalize())
                                                                    advertisementInterval = config.get("advertisement-interval")
                                                                    if advertisementInterval is not None:
                                                                        element_text = advertisementInterval
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["advertisementInterval"] = {}
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["value"] = int(element_text)
                                                                    dict_buffers.append(interface_subinterface_address_vrrp_group_config_dict_buffer)
                                                            state = vrrp_group.get("state")
                                                            if isinstance(state, dict):
                                                                if state is not None and len(state) != 0:
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer = {}
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupState:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupState"
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"] = {}
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_vrrp_group_dict_buffer["id"]
                                                                    virtualRouterId = state.get("virtual-router-id")
                                                                    if virtualRouterId is not None:
                                                                        element_text = virtualRouterId
                                                                        if interface_subinterface_address_vrrp_group_state_dict_buffer["id"].split(":")[-1] != int(element_text):
                                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["id"] = interface_subinterface_address_vrrp_group_state_dict_buffer["id"] + int(element_text)
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["virtualRouterId"] = {}
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["value"] = int(element_text)
                                                                    virtualAddress = state.get("virtual-address")
                                                                    if virtualAddress is not None:
                                                                        element_text = virtualAddress
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["virtualAddress"] = {}
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["virtualAddress"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["virtualAddress"]["value"] = element_text
                                                                    priority = state.get("priority")
                                                                    if priority is not None:
                                                                        element_text = priority
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["priority"] = {}
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["priority"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["priority"]["value"] = int(element_text)
                                                                    preempt = state.get("preempt")
                                                                    if preempt is not None:
                                                                        element_text = preempt
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["preempt"] = {}
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["preempt"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["preempt"]["value"] = eval(str(element_text).capitalize())
                                                                    preemptDelay = state.get("preempt-delay")
                                                                    if preemptDelay is not None:
                                                                        element_text = preemptDelay
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["preemptDelay"] = {}
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["preemptDelay"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["preemptDelay"]["value"] = int(element_text)
                                                                    acceptMode = state.get("accept-mode")
                                                                    if acceptMode is not None:
                                                                        element_text = acceptMode
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["acceptMode"] = {}
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["acceptMode"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["acceptMode"]["value"] = eval(str(element_text).capitalize())
                                                                    advertisementInterval = state.get("advertisement-interval")
                                                                    if advertisementInterval is not None:
                                                                        element_text = advertisementInterval
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["advertisementInterval"] = {}
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["value"] = int(element_text)
                                                                    currentPriority = state.get("current-priority")
                                                                    if currentPriority is not None:
                                                                        element_text = currentPriority
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["currentPriority"] = {}
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["currentPriority"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["currentPriority"]["value"] = int(element_text)
                                                                    dict_buffers.append(interface_subinterface_address_vrrp_group_state_dict_buffer)
                                                            interface_tracking = vrrp_group.get("interface-tracking")
                                                            if isinstance(interface_tracking, dict):
                                                                if interface_tracking is not None and len(interface_tracking) != 0:
                                                                    config = interface_tracking.get("config")
                                                                    if isinstance(config, dict):
                                                                        if config is not None and len(config) != 0:
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer = {}
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig"
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"] = {}
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_vrrp_group_dict_buffer["id"]
                                                                            trackInterface = config.get("track-interface")
                                                                            if trackInterface is not None:
                                                                                element_text = trackInterface
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["trackInterface"] = {}
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["trackInterface"]["type"] = "Relationship"
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["trackInterface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfigInterface:" + interface_subinterface_address_vrrp_group_config_dict_buffer["id"].split(":")[-1]
                                                                            priorityDecrement = config.get("priority-decrement")
                                                                            if priorityDecrement is not None:
                                                                                element_text = priorityDecrement
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["priorityDecrement"] = {}
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["value"] = int(element_text)
                                                                            dict_buffers.append(interface_subinterface_address_vrrp_group_config_dict_buffer)
                                                                    state = interface_tracking.get("state")
                                                                    if isinstance(state, dict):
                                                                        if state is not None and len(state) != 0:
                                                                            interface_subinterface_address_vrrp_group_state_dict_buffer = {}
                                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingState:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingState"
                                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"] = {}
                                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_vrrp_group_dict_buffer["id"]
                                                                            trackInterface = state.get("track-interface")
                                                                            if trackInterface is not None:
                                                                                element_text = trackInterface
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["trackInterface"] = {}
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["trackInterface"]["type"] = "Relationship"
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["trackInterface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingStateInterface:" + interface_subinterface_address_vrrp_group_state_dict_buffer["id"].split(":")[-1]
                                                                            priorityDecrement = state.get("priority-decrement")
                                                                            if priorityDecrement is not None:
                                                                                element_text = priorityDecrement
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["priorityDecrement"] = {}
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["value"] = int(element_text)
                                                                            dict_buffers.append(interface_subinterface_address_vrrp_group_state_dict_buffer)
                                                            dict_buffers.append(interface_subinterface_address_vrrp_group_dict_buffer)
                                                dict_buffers.append(interface_subinterface_address_dict_buffer)
                                    proxy_arp = ipv4.get("proxy-arp")
                                    if isinstance(proxy_arp, dict):
                                        if proxy_arp is not None and len(proxy_arp) != 0:
                                            config = proxy_arp.get("config")
                                            if isinstance(config, dict):
                                                if config is not None and len(config) != 0:
                                                    interface_subinterface_config_dict_buffer = {}
                                                    interface_subinterface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4ProxyArpConfig:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                    interface_subinterface_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4ProxyArpConfig"
                                                    interface_subinterface_config_dict_buffer["isPartOf"] = {}
                                                    interface_subinterface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_subinterface_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                    mode = config.get("mode")
                                                    if mode is not None:
                                                        element_text = mode
                                                        interface_subinterface_config_dict_buffer["mode"] = {}
                                                        interface_subinterface_config_dict_buffer["mode"]["type"] = "Property"
                                                        interface_subinterface_config_dict_buffer["mode"]["value"] = element_text
                                                    dict_buffers.append(interface_subinterface_config_dict_buffer)
                                            state = proxy_arp.get("state")
                                            if isinstance(state, dict):
                                                if state is not None and len(state) != 0:
                                                    interface_subinterface_state_dict_buffer = {}
                                                    interface_subinterface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4ProxyArpState:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                    interface_subinterface_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4ProxyArpState"
                                                    interface_subinterface_state_dict_buffer["isPartOf"] = {}
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                    mode = state.get("mode")
                                                    if mode is not None:
                                                        element_text = mode
                                                        interface_subinterface_state_dict_buffer["mode"] = {}
                                                        interface_subinterface_state_dict_buffer["mode"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["mode"]["value"] = element_text
                                                    dict_buffers.append(interface_subinterface_state_dict_buffer)
                                    neighbors = ipv4.get("neighbors")
                                    if isinstance(neighbors, dict):
                                        if neighbors is not None and len(neighbors) != 0:
                                            neighbors_neighbor = neighbors.get("neighbor")
                                            for neighbor in neighbors_neighbor:
                                                interface_subinterface_neighbor_dict_buffer = {}
                                                interface_subinterface_neighbor_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4NeighborsNeighbor:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                interface_subinterface_neighbor_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4NeighborsNeighbor"
                                                interface_subinterface_neighbor_dict_buffer["isPartOf"] = {}
                                                interface_subinterface_neighbor_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_subinterface_neighbor_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                ip = neighbor.get("ip")
                                                if ip is not None:
                                                    element_text = ip
                                                    if ":" in element_text:
                                                        element_text = element_text.replace(":",".")
                                                    if interface_subinterface_neighbor_dict_buffer["id"].split(":")[-1] != element_text:
                                                        interface_subinterface_neighbor_dict_buffer["id"] = interface_subinterface_neighbor_dict_buffer["id"] + ":" + element_text
                                                    interface_subinterface_neighbor_dict_buffer["ip"] = {}
                                                    interface_subinterface_neighbor_dict_buffer["ip"]["type"] = "Relationship"
                                                    interface_subinterface_neighbor_dict_buffer["ip"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4NeighborsNeighborConfig:" + interface_subinterface_neighbor_dict_buffer["id"].split(":")[-1]
                                                config = neighbor.get("config")
                                                if isinstance(config, dict):
                                                    if config is not None and len(config) != 0:
                                                        interface_subinterface_neighbor_config_dict_buffer = {}
                                                        interface_subinterface_neighbor_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4NeighborsNeighborConfig:" + interface_subinterface_neighbor_dict_buffer["id"].split(":")[-1]
                                                        interface_subinterface_neighbor_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4NeighborsNeighborConfig"
                                                        interface_subinterface_neighbor_config_dict_buffer["isPartOf"] = {}
                                                        interface_subinterface_neighbor_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_subinterface_neighbor_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_neighbor_dict_buffer["id"]
                                                        ip = config.get("ip")
                                                        if ip is not None:
                                                            element_text = ip
                                                            interface_subinterface_neighbor_config_dict_buffer["ip"] = {}
                                                            interface_subinterface_neighbor_config_dict_buffer["ip"]["type"] = "Property"
                                                            interface_subinterface_neighbor_config_dict_buffer["ip"]["value"] = element_text
                                                        linkLayerAddress = config.get("link-layer-address")
                                                        if linkLayerAddress is not None:
                                                            element_text = linkLayerAddress
                                                            interface_subinterface_neighbor_config_dict_buffer["linkLayerAddress"] = {}
                                                            interface_subinterface_neighbor_config_dict_buffer["linkLayerAddress"]["type"] = "Property"
                                                            interface_subinterface_neighbor_config_dict_buffer["linkLayerAddress"]["value"] = element_text
                                                        dict_buffers.append(interface_subinterface_neighbor_config_dict_buffer)
                                                state = neighbor.get("state")
                                                if isinstance(state, dict):
                                                    if state is not None and len(state) != 0:
                                                        interface_subinterface_neighbor_state_dict_buffer = {}
                                                        interface_subinterface_neighbor_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4NeighborsNeighborState:" + interface_subinterface_neighbor_dict_buffer["id"].split(":")[-1]
                                                        interface_subinterface_neighbor_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4NeighborsNeighborState"
                                                        interface_subinterface_neighbor_state_dict_buffer["isPartOf"] = {}
                                                        interface_subinterface_neighbor_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_subinterface_neighbor_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_neighbor_dict_buffer["id"]
                                                        ip = state.get("ip")
                                                        if ip is not None:
                                                            element_text = ip
                                                            interface_subinterface_neighbor_state_dict_buffer["ip"] = {}
                                                            interface_subinterface_neighbor_state_dict_buffer["ip"]["type"] = "Property"
                                                            interface_subinterface_neighbor_state_dict_buffer["ip"]["value"] = element_text
                                                        linkLayerAddress = state.get("link-layer-address")
                                                        if linkLayerAddress is not None:
                                                            element_text = linkLayerAddress
                                                            interface_subinterface_neighbor_state_dict_buffer["linkLayerAddress"] = {}
                                                            interface_subinterface_neighbor_state_dict_buffer["linkLayerAddress"]["type"] = "Property"
                                                            interface_subinterface_neighbor_state_dict_buffer["linkLayerAddress"]["value"] = element_text
                                                        origin = state.get("origin")
                                                        if origin is not None:
                                                            element_text = origin
                                                            interface_subinterface_neighbor_state_dict_buffer["origin"] = {}
                                                            interface_subinterface_neighbor_state_dict_buffer["origin"]["type"] = "Property"
                                                            interface_subinterface_neighbor_state_dict_buffer["origin"]["value"] = element_text
                                                        dict_buffers.append(interface_subinterface_neighbor_state_dict_buffer)
                                                dict_buffers.append(interface_subinterface_neighbor_dict_buffer)
                                    unnumbered = ipv4.get("unnumbered")
                                    if isinstance(unnumbered, dict):
                                        if unnumbered is not None and len(unnumbered) != 0:
                                            config = unnumbered.get("config")
                                            if isinstance(config, dict):
                                                if config is not None and len(config) != 0:
                                                    interface_subinterface_config_dict_buffer = {}
                                                    interface_subinterface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4UnnumberedConfig:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                    interface_subinterface_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4UnnumberedConfig"
                                                    interface_subinterface_config_dict_buffer["isPartOf"] = {}
                                                    interface_subinterface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_subinterface_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                    enabled = config.get("enabled")
                                                    if enabled is not None:
                                                        element_text = enabled
                                                        interface_subinterface_config_dict_buffer["enabled"] = {}
                                                        interface_subinterface_config_dict_buffer["enabled"]["type"] = "Property"
                                                        interface_subinterface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                    dict_buffers.append(interface_subinterface_config_dict_buffer)
                                            state = unnumbered.get("state")
                                            if isinstance(state, dict):
                                                if state is not None and len(state) != 0:
                                                    interface_subinterface_state_dict_buffer = {}
                                                    interface_subinterface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4UnnumberedState:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                    interface_subinterface_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4UnnumberedState"
                                                    interface_subinterface_state_dict_buffer["isPartOf"] = {}
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                    enabled = state.get("enabled")
                                                    if enabled is not None:
                                                        element_text = enabled
                                                        interface_subinterface_state_dict_buffer["enabled"] = {}
                                                        interface_subinterface_state_dict_buffer["enabled"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                    dict_buffers.append(interface_subinterface_state_dict_buffer)
                                            interface_ref = unnumbered.get("interface-ref")
                                            if isinstance(interface_ref, dict):
                                                if interface_ref is not None and len(interface_ref) != 0:
                                                    config = interface_ref.get("config")
                                                    if isinstance(config, dict):
                                                        if config is not None and len(config) != 0:
                                                            interface_subinterface_config_dict_buffer = {}
                                                            interface_subinterface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4UnnumberedInterfaceRefConfig:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                            interface_subinterface_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4UnnumberedInterfaceRefConfig"
                                                            interface_subinterface_config_dict_buffer["isPartOf"] = {}
                                                            interface_subinterface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_subinterface_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                            interface = config.get("interface")
                                                            if interface is not None:
                                                                element_text = interface
                                                                if interface_subinterface_config_dict_buffer["id"].split(":")[-1] != element_text:
                                                                    interface_subinterface_config_dict_buffer["id"] = interface_subinterface_config_dict_buffer["id"] + element_text
                                                                interface_subinterface_config_dict_buffer["interface"] = {}
                                                                interface_subinterface_config_dict_buffer["interface"]["type"] = "Relationship"
                                                                interface_subinterface_config_dict_buffer["interface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4UnnumberedInterfaceRefConfigInterface:" + interface_subinterface_config_dict_buffer["id"].split(":")[-1]
                                                            subinterface = config.get("subinterface")
                                                            if subinterface is not None:
                                                                element_text = subinterface
                                                                if "." + str(element_text) not in interface_subinterface_config_dict_buffer["id"].split(":")[-1]:
                                                                    interface_subinterface_config_dict_buffer["id"] = interface_subinterface_config_dict_buffer["id"] + "." + str(element_text)
                                                                interface_subinterface_config_dict_buffer["subinterface"] = {}
                                                                interface_subinterface_config_dict_buffer["subinterface"]["type"] = "Relationship"
                                                                interface_subinterface_config_dict_buffer["subinterface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4UnnumberedInterfaceRefConfigSubinterface:" + interface_subinterface_config_dict_buffer["id"].split(":")[-1]
                                                            dict_buffers.append(interface_subinterface_config_dict_buffer)
                                                    state = interface_ref.get("state")
                                                    if isinstance(state, dict):
                                                        if state is not None and len(state) != 0:
                                                            interface_subinterface_state_dict_buffer = {}
                                                            interface_subinterface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4UnnumberedInterfaceRefState:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                            interface_subinterface_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4UnnumberedInterfaceRefState"
                                                            interface_subinterface_state_dict_buffer["isPartOf"] = {}
                                                            interface_subinterface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_subinterface_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                            interface = state.get("interface")
                                                            if interface is not None:
                                                                element_text = interface
                                                                if interface_subinterface_state_dict_buffer["id"].split(":")[-1] != element_text:
                                                                    interface_subinterface_state_dict_buffer["id"] = interface_subinterface_state_dict_buffer["id"] + element_text
                                                                interface_subinterface_state_dict_buffer["interface"] = {}
                                                                interface_subinterface_state_dict_buffer["interface"]["type"] = "Relationship"
                                                                interface_subinterface_state_dict_buffer["interface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4UnnumberedInterfaceRefStateInterface:" + interface_subinterface_state_dict_buffer["id"].split(":")[-1]
                                                            subinterface = state.get("subinterface")
                                                            if subinterface is not None:
                                                                element_text = subinterface
                                                                if "." + str(element_text) not in interface_subinterface_state_dict_buffer["id"].split(":")[-1]:
                                                                    interface_subinterface_state_dict_buffer["id"] = interface_subinterface_state_dict_buffer["id"] + "." + str(element_text)
                                                                interface_subinterface_state_dict_buffer["subinterface"] = {}
                                                                interface_subinterface_state_dict_buffer["subinterface"]["type"] = "Relationship"
                                                                interface_subinterface_state_dict_buffer["subinterface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4UnnumberedInterfaceRefStateSubinterface:" + interface_subinterface_state_dict_buffer["id"].split(":")[-1]
                                                            dict_buffers.append(interface_subinterface_state_dict_buffer)
                                    config = ipv4.get("config")
                                    if isinstance(config, dict):
                                        if config is not None and len(config) != 0:
                                            interface_subinterface_config_dict_buffer = {}
                                            interface_subinterface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4Config:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                            interface_subinterface_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4Config"
                                            interface_subinterface_config_dict_buffer["isPartOf"] = {}
                                            interface_subinterface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                            interface_subinterface_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                            enabled = config.get("enabled")
                                            if enabled is not None:
                                                element_text = enabled
                                                interface_subinterface_config_dict_buffer["enabled"] = {}
                                                interface_subinterface_config_dict_buffer["enabled"]["type"] = "Property"
                                                interface_subinterface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                            mtu = config.get("mtu")
                                            if mtu is not None:
                                                element_text = mtu
                                                interface_subinterface_config_dict_buffer["mtu"] = {}
                                                interface_subinterface_config_dict_buffer["mtu"]["type"] = "Property"
                                                interface_subinterface_config_dict_buffer["mtu"]["value"] = int(element_text)
                                            dhcpClient = config.get("dhcp-client")
                                            if dhcpClient is not None:
                                                element_text = dhcpClient
                                                interface_subinterface_config_dict_buffer["dhcpClient"] = {}
                                                interface_subinterface_config_dict_buffer["dhcpClient"]["type"] = "Property"
                                                interface_subinterface_config_dict_buffer["dhcpClient"]["value"] = eval(str(element_text).capitalize())
                                            dict_buffers.append(interface_subinterface_config_dict_buffer)
                                    state = ipv4.get("state")
                                    if isinstance(state, dict):
                                        if state is not None and len(state) != 0:
                                            interface_subinterface_state_dict_buffer = {}
                                            interface_subinterface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4State:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                            interface_subinterface_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4State"
                                            interface_subinterface_state_dict_buffer["isPartOf"] = {}
                                            interface_subinterface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                            interface_subinterface_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                            enabled = state.get("enabled")
                                            if enabled is not None:
                                                element_text = enabled
                                                interface_subinterface_state_dict_buffer["enabled"] = {}
                                                interface_subinterface_state_dict_buffer["enabled"]["type"] = "Property"
                                                interface_subinterface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                            mtu = state.get("mtu")
                                            if mtu is not None:
                                                element_text = mtu
                                                interface_subinterface_state_dict_buffer["mtu"] = {}
                                                interface_subinterface_state_dict_buffer["mtu"]["type"] = "Property"
                                                interface_subinterface_state_dict_buffer["mtu"]["value"] = int(element_text)
                                            dhcpClient = state.get("dhcp-client")
                                            if dhcpClient is not None:
                                                element_text = dhcpClient
                                                interface_subinterface_state_dict_buffer["dhcpClient"] = {}
                                                interface_subinterface_state_dict_buffer["dhcpClient"]["type"] = "Property"
                                                interface_subinterface_state_dict_buffer["dhcpClient"]["value"] = eval(str(element_text).capitalize())
                                            counters = state.get("counters")
                                            if isinstance(counters, dict):
                                                if counters is not None and len(counters) != 0:
                                                    interface_subinterface_state_counters_dict_buffer = {}
                                                    interface_subinterface_state_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4StateCounters:" + interface_subinterface_state_dict_buffer["id"].split(":")[-1]
                                                    interface_subinterface_state_counters_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4StateCounters"
                                                    interface_subinterface_state_counters_dict_buffer["isPartOf"] = {}
                                                    interface_subinterface_state_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_subinterface_state_counters_dict_buffer["isPartOf"]["object"] = interface_subinterface_state_dict_buffer["id"]
                                                    inPkts = counters.get("in-pkts")
                                                    if inPkts is not None:
                                                        element_text = inPkts
                                                        interface_subinterface_state_counters_dict_buffer["inPkts"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["inPkts"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["inPkts"]["value"] = int(element_text)
                                                    inOctets = counters.get("in-octets")
                                                    if inOctets is not None:
                                                        element_text = inOctets
                                                        interface_subinterface_state_counters_dict_buffer["inOctets"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["inOctets"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["inOctets"]["value"] = int(element_text)
                                                    inErrorPkts = counters.get("in-error-pkts")
                                                    if inErrorPkts is not None:
                                                        element_text = inErrorPkts
                                                        interface_subinterface_state_counters_dict_buffer["inErrorPkts"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["inErrorPkts"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["inErrorPkts"]["value"] = int(element_text)
                                                    inForwardedPkts = counters.get("in-forwarded-pkts")
                                                    if inForwardedPkts is not None:
                                                        element_text = inForwardedPkts
                                                        interface_subinterface_state_counters_dict_buffer["inForwardedPkts"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["inForwardedPkts"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["inForwardedPkts"]["value"] = int(element_text)
                                                    inForwardedOctets = counters.get("in-forwarded-octets")
                                                    if inForwardedOctets is not None:
                                                        element_text = inForwardedOctets
                                                        interface_subinterface_state_counters_dict_buffer["inForwardedOctets"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["inForwardedOctets"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["inForwardedOctets"]["value"] = int(element_text)
                                                    inDiscardedPkts = counters.get("in-discarded-pkts")
                                                    if inDiscardedPkts is not None:
                                                        element_text = inDiscardedPkts
                                                        interface_subinterface_state_counters_dict_buffer["inDiscardedPkts"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["inDiscardedPkts"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["inDiscardedPkts"]["value"] = int(element_text)
                                                    outPkts = counters.get("out-pkts")
                                                    if outPkts is not None:
                                                        element_text = outPkts
                                                        interface_subinterface_state_counters_dict_buffer["outPkts"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["outPkts"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["outPkts"]["value"] = int(element_text)
                                                    outOctets = counters.get("out-octets")
                                                    if outOctets is not None:
                                                        element_text = outOctets
                                                        interface_subinterface_state_counters_dict_buffer["outOctets"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["outOctets"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["outOctets"]["value"] = int(element_text)
                                                    outErrorPkts = counters.get("out-error-pkts")
                                                    if outErrorPkts is not None:
                                                        element_text = outErrorPkts
                                                        interface_subinterface_state_counters_dict_buffer["outErrorPkts"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["outErrorPkts"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["outErrorPkts"]["value"] = int(element_text)
                                                    outForwardedPkts = counters.get("out-forwarded-pkts")
                                                    if outForwardedPkts is not None:
                                                        element_text = outForwardedPkts
                                                        interface_subinterface_state_counters_dict_buffer["outForwardedPkts"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["outForwardedPkts"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["outForwardedPkts"]["value"] = int(element_text)
                                                    outForwardedOctets = counters.get("out-forwarded-octets")
                                                    if outForwardedOctets is not None:
                                                        element_text = outForwardedOctets
                                                        interface_subinterface_state_counters_dict_buffer["outForwardedOctets"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["outForwardedOctets"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["outForwardedOctets"]["value"] = int(element_text)
                                                    outDiscardedPkts = counters.get("out-discarded-pkts")
                                                    if outDiscardedPkts is not None:
                                                        element_text = outDiscardedPkts
                                                        interface_subinterface_state_counters_dict_buffer["outDiscardedPkts"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["outDiscardedPkts"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["outDiscardedPkts"]["value"] = int(element_text)
                                                    dict_buffers.append(interface_subinterface_state_counters_dict_buffer)
                                            dict_buffers.append(interface_subinterface_state_dict_buffer)
                            ipv6 = subinterface.get("openconfig-if-ip:ipv6")
                            if isinstance(ipv6, dict):
                                if ipv6 is not None and len(ipv6) != 0:
                                    addresses = ipv6.get("addresses")
                                    if isinstance(addresses, dict):
                                        if addresses is not None and len(addresses) != 0:
                                            addresses_address = addresses.get("address")
                                            for address in addresses_address:
                                                interface_subinterface_address_dict_buffer = {}
                                                interface_subinterface_address_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddress:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                interface_subinterface_address_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6AddressesAddress"
                                                interface_subinterface_address_dict_buffer["isPartOf"] = {}
                                                interface_subinterface_address_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_subinterface_address_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                ip = address.get("ip")
                                                if ip is not None:
                                                    element_text = ip
                                                    if ":" in element_text:
                                                        element_text = element_text.replace(":",".")
                                                    if interface_subinterface_address_dict_buffer["id"].split(":")[-1] != element_text:
                                                        interface_subinterface_address_dict_buffer["id"] = interface_subinterface_address_dict_buffer["id"] + ":" + element_text
                                                    interface_subinterface_address_dict_buffer["ip"] = {}
                                                    interface_subinterface_address_dict_buffer["ip"]["type"] = "Relationship"
                                                    interface_subinterface_address_dict_buffer["ip"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressConfig:" + interface_subinterface_address_dict_buffer["id"].split(":")[-1]
                                                config = address.get("config")
                                                if isinstance(config, dict):
                                                    if config is not None and len(config) != 0:
                                                        interface_subinterface_address_config_dict_buffer = {}
                                                        interface_subinterface_address_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressConfig:" + interface_subinterface_address_dict_buffer["id"].split(":")[-1]
                                                        interface_subinterface_address_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressConfig"
                                                        interface_subinterface_address_config_dict_buffer["isPartOf"] = {}
                                                        interface_subinterface_address_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_subinterface_address_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_dict_buffer["id"]
                                                        ip = config.get("ip")
                                                        if ip is not None:
                                                            element_text = ip
                                                            interface_subinterface_address_config_dict_buffer["ip"] = {}
                                                            interface_subinterface_address_config_dict_buffer["ip"]["type"] = "Property"
                                                            interface_subinterface_address_config_dict_buffer["ip"]["value"] = element_text
                                                        prefixLength = config.get("prefix-length")
                                                        if prefixLength is not None:
                                                            element_text = prefixLength
                                                            interface_subinterface_address_config_dict_buffer["prefixLength"] = {}
                                                            interface_subinterface_address_config_dict_buffer["prefixLength"]["type"] = "Property"
                                                            interface_subinterface_address_config_dict_buffer["prefixLength"]["value"] = int(element_text)
                                                        dict_buffers.append(interface_subinterface_address_config_dict_buffer)
                                                state = address.get("state")
                                                if isinstance(state, dict):
                                                    if state is not None and len(state) != 0:
                                                        interface_subinterface_address_state_dict_buffer = {}
                                                        interface_subinterface_address_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressState:" + interface_subinterface_address_dict_buffer["id"].split(":")[-1]
                                                        interface_subinterface_address_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressState"
                                                        interface_subinterface_address_state_dict_buffer["isPartOf"] = {}
                                                        interface_subinterface_address_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_subinterface_address_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_dict_buffer["id"]
                                                        ip = state.get("ip")
                                                        if ip is not None:
                                                            element_text = ip
                                                            interface_subinterface_address_state_dict_buffer["ip"] = {}
                                                            interface_subinterface_address_state_dict_buffer["ip"]["type"] = "Property"
                                                            interface_subinterface_address_state_dict_buffer["ip"]["value"] = element_text
                                                        prefixLength = state.get("prefix-length")
                                                        if prefixLength is not None:
                                                            element_text = prefixLength
                                                            interface_subinterface_address_state_dict_buffer["prefixLength"] = {}
                                                            interface_subinterface_address_state_dict_buffer["prefixLength"]["type"] = "Property"
                                                            interface_subinterface_address_state_dict_buffer["prefixLength"]["value"] = int(element_text)
                                                        origin = state.get("origin")
                                                        if origin is not None:
                                                            element_text = origin
                                                            interface_subinterface_address_state_dict_buffer["origin"] = {}
                                                            interface_subinterface_address_state_dict_buffer["origin"]["type"] = "Property"
                                                            interface_subinterface_address_state_dict_buffer["origin"]["value"] = element_text
                                                        status = state.get("status")
                                                        if status is not None:
                                                            element_text = status
                                                            interface_subinterface_address_state_dict_buffer["status"] = {}
                                                            interface_subinterface_address_state_dict_buffer["status"]["type"] = "Property"
                                                            interface_subinterface_address_state_dict_buffer["status"]["value"] = element_text
                                                        dict_buffers.append(interface_subinterface_address_state_dict_buffer)
                                                vrrp = address.get("vrrp")
                                                if isinstance(vrrp, dict):
                                                    if vrrp is not None and len(vrrp) != 0:
                                                        vrrp_vrrp_group = vrrp.get("vrrp-group")
                                                        for vrrp_group in vrrp_vrrp_group:
                                                            interface_subinterface_address_vrrp_group_dict_buffer = {}
                                                            interface_subinterface_address_vrrp_group_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroup:" + interface_subinterface_address_dict_buffer["id"].split(":")[-1]
                                                            interface_subinterface_address_vrrp_group_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroup"
                                                            interface_subinterface_address_vrrp_group_dict_buffer["isPartOf"] = {}
                                                            interface_subinterface_address_vrrp_group_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_subinterface_address_vrrp_group_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_dict_buffer["id"]
                                                            virtualRouterId = vrrp_group.get("virtual-router-id")
                                                            if virtualRouterId is not None:
                                                                element_text = virtualRouterId
                                                                if interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1] != element_text:
                                                                    interface_subinterface_address_vrrp_group_dict_buffer["id"] = interface_subinterface_address_vrrp_group_dict_buffer["id"] + element_text
                                                                interface_subinterface_address_vrrp_group_dict_buffer["virtualRouterId"] = {}
                                                                interface_subinterface_address_vrrp_group_dict_buffer["virtualRouterId"]["type"] = "Relationship"
                                                                interface_subinterface_address_vrrp_group_dict_buffer["virtualRouterId"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfig:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                            config = vrrp_group.get("config")
                                                            if isinstance(config, dict):
                                                                if config is not None and len(config) != 0:
                                                                    interface_subinterface_address_vrrp_group_config_dict_buffer = {}
                                                                    interface_subinterface_address_vrrp_group_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfig:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                    interface_subinterface_address_vrrp_group_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfig"
                                                                    interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"] = {}
                                                                    interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                    interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_vrrp_group_dict_buffer["id"]
                                                                    virtualRouterId = config.get("virtual-router-id")
                                                                    if virtualRouterId is not None:
                                                                        element_text = virtualRouterId
                                                                        if interface_subinterface_address_vrrp_group_config_dict_buffer["id"].split(":")[-1] != int(element_text):
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["id"] = interface_subinterface_address_vrrp_group_config_dict_buffer["id"] + int(element_text)
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["virtualRouterId"] = {}
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["value"] = int(element_text)
                                                                    virtualAddress = config.get("virtual-address")
                                                                    if virtualAddress is not None:
                                                                        element_text = virtualAddress
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["virtualAddress"] = {}
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["virtualAddress"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["virtualAddress"]["value"] = element_text
                                                                    priority = config.get("priority")
                                                                    if priority is not None:
                                                                        element_text = priority
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["priority"] = {}
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["priority"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["priority"]["value"] = int(element_text)
                                                                    preempt = config.get("preempt")
                                                                    if preempt is not None:
                                                                        element_text = preempt
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["preempt"] = {}
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["preempt"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["preempt"]["value"] = eval(str(element_text).capitalize())
                                                                    preemptDelay = config.get("preempt-delay")
                                                                    if preemptDelay is not None:
                                                                        element_text = preemptDelay
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["preemptDelay"] = {}
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["preemptDelay"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["preemptDelay"]["value"] = int(element_text)
                                                                    acceptMode = config.get("accept-mode")
                                                                    if acceptMode is not None:
                                                                        element_text = acceptMode
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["acceptMode"] = {}
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["acceptMode"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["acceptMode"]["value"] = eval(str(element_text).capitalize())
                                                                    advertisementInterval = config.get("advertisement-interval")
                                                                    if advertisementInterval is not None:
                                                                        element_text = advertisementInterval
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["advertisementInterval"] = {}
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["value"] = int(element_text)
                                                                    virtualLinkLocal = config.get("virtual-link-local")
                                                                    if virtualLinkLocal is not None:
                                                                        element_text = virtualLinkLocal
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["virtualLinkLocal"] = {}
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["virtualLinkLocal"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["virtualLinkLocal"]["value"] = element_text
                                                                    dict_buffers.append(interface_subinterface_address_vrrp_group_config_dict_buffer)
                                                            state = vrrp_group.get("state")
                                                            if isinstance(state, dict):
                                                                if state is not None and len(state) != 0:
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer = {}
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupState:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupState"
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"] = {}
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_vrrp_group_dict_buffer["id"]
                                                                    virtualRouterId = state.get("virtual-router-id")
                                                                    if virtualRouterId is not None:
                                                                        element_text = virtualRouterId
                                                                        if interface_subinterface_address_vrrp_group_state_dict_buffer["id"].split(":")[-1] != int(element_text):
                                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["id"] = interface_subinterface_address_vrrp_group_state_dict_buffer["id"] + int(element_text)
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["virtualRouterId"] = {}
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["value"] = int(element_text)
                                                                    virtualAddress = state.get("virtual-address")
                                                                    if virtualAddress is not None:
                                                                        element_text = virtualAddress
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["virtualAddress"] = {}
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["virtualAddress"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["virtualAddress"]["value"] = element_text
                                                                    priority = state.get("priority")
                                                                    if priority is not None:
                                                                        element_text = priority
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["priority"] = {}
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["priority"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["priority"]["value"] = int(element_text)
                                                                    preempt = state.get("preempt")
                                                                    if preempt is not None:
                                                                        element_text = preempt
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["preempt"] = {}
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["preempt"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["preempt"]["value"] = eval(str(element_text).capitalize())
                                                                    preemptDelay = state.get("preempt-delay")
                                                                    if preemptDelay is not None:
                                                                        element_text = preemptDelay
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["preemptDelay"] = {}
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["preemptDelay"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["preemptDelay"]["value"] = int(element_text)
                                                                    acceptMode = state.get("accept-mode")
                                                                    if acceptMode is not None:
                                                                        element_text = acceptMode
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["acceptMode"] = {}
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["acceptMode"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["acceptMode"]["value"] = eval(str(element_text).capitalize())
                                                                    advertisementInterval = state.get("advertisement-interval")
                                                                    if advertisementInterval is not None:
                                                                        element_text = advertisementInterval
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["advertisementInterval"] = {}
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["value"] = int(element_text)
                                                                    currentPriority = state.get("current-priority")
                                                                    if currentPriority is not None:
                                                                        element_text = currentPriority
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["currentPriority"] = {}
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["currentPriority"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["currentPriority"]["value"] = int(element_text)
                                                                    virtualLinkLocal = state.get("virtual-link-local")
                                                                    if virtualLinkLocal is not None:
                                                                        element_text = virtualLinkLocal
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["virtualLinkLocal"] = {}
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["virtualLinkLocal"]["type"] = "Property"
                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["virtualLinkLocal"]["value"] = element_text
                                                                    dict_buffers.append(interface_subinterface_address_vrrp_group_state_dict_buffer)
                                                            interface_tracking = vrrp_group.get("interface-tracking")
                                                            if isinstance(interface_tracking, dict):
                                                                if interface_tracking is not None and len(interface_tracking) != 0:
                                                                    config = interface_tracking.get("config")
                                                                    if isinstance(config, dict):
                                                                        if config is not None and len(config) != 0:
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer = {}
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig"
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"] = {}
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_vrrp_group_dict_buffer["id"]
                                                                            trackInterface = config.get("track-interface")
                                                                            if trackInterface is not None:
                                                                                element_text = trackInterface
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["trackInterface"] = {}
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["trackInterface"]["type"] = "Relationship"
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["trackInterface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupInterfaceTrackingConfigInterface:" + interface_subinterface_address_vrrp_group_config_dict_buffer["id"].split(":")[-1]
                                                                            priorityDecrement = config.get("priority-decrement")
                                                                            if priorityDecrement is not None:
                                                                                element_text = priorityDecrement
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["priorityDecrement"] = {}
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["value"] = int(element_text)
                                                                            dict_buffers.append(interface_subinterface_address_vrrp_group_config_dict_buffer)
                                                                    state = interface_tracking.get("state")
                                                                    if isinstance(state, dict):
                                                                        if state is not None and len(state) != 0:
                                                                            interface_subinterface_address_vrrp_group_state_dict_buffer = {}
                                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupInterfaceTrackingState:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupInterfaceTrackingState"
                                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"] = {}
                                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_vrrp_group_dict_buffer["id"]
                                                                            trackInterface = state.get("track-interface")
                                                                            if trackInterface is not None:
                                                                                element_text = trackInterface
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["trackInterface"] = {}
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["trackInterface"]["type"] = "Relationship"
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["trackInterface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupInterfaceTrackingStateInterface:" + interface_subinterface_address_vrrp_group_state_dict_buffer["id"].split(":")[-1]
                                                                            priorityDecrement = state.get("priority-decrement")
                                                                            if priorityDecrement is not None:
                                                                                element_text = priorityDecrement
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["priorityDecrement"] = {}
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["value"] = int(element_text)
                                                                            dict_buffers.append(interface_subinterface_address_vrrp_group_state_dict_buffer)
                                                            dict_buffers.append(interface_subinterface_address_vrrp_group_dict_buffer)
                                                dict_buffers.append(interface_subinterface_address_dict_buffer)
                                    router_advertisement = ipv6.get("router-advertisement")
                                    if isinstance(router_advertisement, dict):
                                        if router_advertisement is not None and len(router_advertisement) != 0:
                                            config = router_advertisement.get("config")
                                            if isinstance(config, dict):
                                                if config is not None and len(config) != 0:
                                                    interface_subinterface_config_dict_buffer = {}
                                                    interface_subinterface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6RouterAdvertisementConfig:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                    interface_subinterface_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6RouterAdvertisementConfig"
                                                    interface_subinterface_config_dict_buffer["isPartOf"] = {}
                                                    interface_subinterface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_subinterface_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                    interval = config.get("interval")
                                                    if interval is not None:
                                                        element_text = interval
                                                        interface_subinterface_config_dict_buffer["interval"] = {}
                                                        interface_subinterface_config_dict_buffer["interval"]["type"] = "Property"
                                                        interface_subinterface_config_dict_buffer["interval"]["value"] = int(element_text)
                                                    lifetime = config.get("lifetime")
                                                    if lifetime is not None:
                                                        element_text = lifetime
                                                        interface_subinterface_config_dict_buffer["lifetime"] = {}
                                                        interface_subinterface_config_dict_buffer["lifetime"]["type"] = "Property"
                                                        interface_subinterface_config_dict_buffer["lifetime"]["value"] = int(element_text)
                                                    suppress = config.get("suppress")
                                                    if suppress is not None:
                                                        element_text = suppress
                                                        interface_subinterface_config_dict_buffer["suppress"] = {}
                                                        interface_subinterface_config_dict_buffer["suppress"]["type"] = "Property"
                                                        interface_subinterface_config_dict_buffer["suppress"]["value"] = eval(str(element_text).capitalize())
                                                    dict_buffers.append(interface_subinterface_config_dict_buffer)
                                            state = router_advertisement.get("state")
                                            if isinstance(state, dict):
                                                if state is not None and len(state) != 0:
                                                    interface_subinterface_state_dict_buffer = {}
                                                    interface_subinterface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6RouterAdvertisementState:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                    interface_subinterface_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6RouterAdvertisementState"
                                                    interface_subinterface_state_dict_buffer["isPartOf"] = {}
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                    interval = state.get("interval")
                                                    if interval is not None:
                                                        element_text = interval
                                                        interface_subinterface_state_dict_buffer["interval"] = {}
                                                        interface_subinterface_state_dict_buffer["interval"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["interval"]["value"] = int(element_text)
                                                    lifetime = state.get("lifetime")
                                                    if lifetime is not None:
                                                        element_text = lifetime
                                                        interface_subinterface_state_dict_buffer["lifetime"] = {}
                                                        interface_subinterface_state_dict_buffer["lifetime"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["lifetime"]["value"] = int(element_text)
                                                    suppress = state.get("suppress")
                                                    if suppress is not None:
                                                        element_text = suppress
                                                        interface_subinterface_state_dict_buffer["suppress"] = {}
                                                        interface_subinterface_state_dict_buffer["suppress"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["suppress"]["value"] = eval(str(element_text).capitalize())
                                                    dict_buffers.append(interface_subinterface_state_dict_buffer)
                                    neighbors = ipv6.get("neighbors")
                                    if isinstance(neighbors, dict):
                                        if neighbors is not None and len(neighbors) != 0:
                                            neighbors_neighbor = neighbors.get("neighbor")
                                            for neighbor in neighbors_neighbor:
                                                interface_subinterface_neighbor_dict_buffer = {}
                                                interface_subinterface_neighbor_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighbor:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                interface_subinterface_neighbor_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighbor"
                                                interface_subinterface_neighbor_dict_buffer["isPartOf"] = {}
                                                interface_subinterface_neighbor_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_subinterface_neighbor_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                ip = neighbor.get("ip")
                                                if ip is not None:
                                                    element_text = ip
                                                    if ":" in element_text:
                                                        element_text = element_text.replace(":",".")
                                                    if interface_subinterface_neighbor_dict_buffer["id"].split(":")[-1] != element_text:
                                                        interface_subinterface_neighbor_dict_buffer["id"] = interface_subinterface_neighbor_dict_buffer["id"] + ":" + element_text
                                                    interface_subinterface_neighbor_dict_buffer["ip"] = {}
                                                    interface_subinterface_neighbor_dict_buffer["ip"]["type"] = "Relationship"
                                                    interface_subinterface_neighbor_dict_buffer["ip"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborConfig:" + interface_subinterface_neighbor_dict_buffer["id"].split(":")[-1]
                                                config = neighbor.get("config")
                                                if isinstance(config, dict):
                                                    if config is not None and len(config) != 0:
                                                        interface_subinterface_neighbor_config_dict_buffer = {}
                                                        interface_subinterface_neighbor_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborConfig:" + interface_subinterface_neighbor_dict_buffer["id"].split(":")[-1]
                                                        interface_subinterface_neighbor_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborConfig"
                                                        interface_subinterface_neighbor_config_dict_buffer["isPartOf"] = {}
                                                        interface_subinterface_neighbor_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_subinterface_neighbor_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_neighbor_dict_buffer["id"]
                                                        ip = config.get("ip")
                                                        if ip is not None:
                                                            element_text = ip
                                                            interface_subinterface_neighbor_config_dict_buffer["ip"] = {}
                                                            interface_subinterface_neighbor_config_dict_buffer["ip"]["type"] = "Property"
                                                            interface_subinterface_neighbor_config_dict_buffer["ip"]["value"] = element_text
                                                        linkLayerAddress = config.get("link-layer-address")
                                                        if linkLayerAddress is not None:
                                                            element_text = linkLayerAddress
                                                            interface_subinterface_neighbor_config_dict_buffer["linkLayerAddress"] = {}
                                                            interface_subinterface_neighbor_config_dict_buffer["linkLayerAddress"]["type"] = "Property"
                                                            interface_subinterface_neighbor_config_dict_buffer["linkLayerAddress"]["value"] = element_text
                                                        dict_buffers.append(interface_subinterface_neighbor_config_dict_buffer)
                                                state = neighbor.get("state")
                                                if isinstance(state, dict):
                                                    if state is not None and len(state) != 0:
                                                        interface_subinterface_neighbor_state_dict_buffer = {}
                                                        interface_subinterface_neighbor_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborState:" + interface_subinterface_neighbor_dict_buffer["id"].split(":")[-1]
                                                        interface_subinterface_neighbor_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborState"
                                                        interface_subinterface_neighbor_state_dict_buffer["isPartOf"] = {}
                                                        interface_subinterface_neighbor_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_subinterface_neighbor_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_neighbor_dict_buffer["id"]
                                                        ip = state.get("ip")
                                                        if ip is not None:
                                                            element_text = ip
                                                            interface_subinterface_neighbor_state_dict_buffer["ip"] = {}
                                                            interface_subinterface_neighbor_state_dict_buffer["ip"]["type"] = "Property"
                                                            interface_subinterface_neighbor_state_dict_buffer["ip"]["value"] = element_text
                                                        linkLayerAddress = state.get("link-layer-address")
                                                        if linkLayerAddress is not None:
                                                            element_text = linkLayerAddress
                                                            interface_subinterface_neighbor_state_dict_buffer["linkLayerAddress"] = {}
                                                            interface_subinterface_neighbor_state_dict_buffer["linkLayerAddress"]["type"] = "Property"
                                                            interface_subinterface_neighbor_state_dict_buffer["linkLayerAddress"]["value"] = element_text
                                                        origin = state.get("origin")
                                                        if origin is not None:
                                                            element_text = origin
                                                            interface_subinterface_neighbor_state_dict_buffer["origin"] = {}
                                                            interface_subinterface_neighbor_state_dict_buffer["origin"]["type"] = "Property"
                                                            interface_subinterface_neighbor_state_dict_buffer["origin"]["value"] = element_text
                                                        isRouter = state.get("is-router")
                                                        if isRouter is not None:
                                                            element_text = isRouter
                                                            interface_subinterface_neighbor_state_dict_buffer["isRouter"] = {}
                                                            interface_subinterface_neighbor_state_dict_buffer["isRouter"]["type"] = "Property"
                                                            interface_subinterface_neighbor_state_dict_buffer["isRouter"]["value"] = element_text
                                                        neighborState = state.get("neighbor-state")
                                                        if neighborState is not None:
                                                            element_text = neighborState
                                                            interface_subinterface_neighbor_state_dict_buffer["neighborState"] = {}
                                                            interface_subinterface_neighbor_state_dict_buffer["neighborState"]["type"] = "Property"
                                                            interface_subinterface_neighbor_state_dict_buffer["neighborState"]["value"] = element_text
                                                        dict_buffers.append(interface_subinterface_neighbor_state_dict_buffer)
                                                dict_buffers.append(interface_subinterface_neighbor_dict_buffer)
                                    unnumbered = ipv6.get("unnumbered")
                                    if isinstance(unnumbered, dict):
                                        if unnumbered is not None and len(unnumbered) != 0:
                                            config = unnumbered.get("config")
                                            if isinstance(config, dict):
                                                if config is not None and len(config) != 0:
                                                    interface_subinterface_config_dict_buffer = {}
                                                    interface_subinterface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6UnnumberedConfig:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                    interface_subinterface_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6UnnumberedConfig"
                                                    interface_subinterface_config_dict_buffer["isPartOf"] = {}
                                                    interface_subinterface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_subinterface_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                    enabled = config.get("enabled")
                                                    if enabled is not None:
                                                        element_text = enabled
                                                        interface_subinterface_config_dict_buffer["enabled"] = {}
                                                        interface_subinterface_config_dict_buffer["enabled"]["type"] = "Property"
                                                        interface_subinterface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                    dict_buffers.append(interface_subinterface_config_dict_buffer)
                                            state = unnumbered.get("state")
                                            if isinstance(state, dict):
                                                if state is not None and len(state) != 0:
                                                    interface_subinterface_state_dict_buffer = {}
                                                    interface_subinterface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6UnnumberedState:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                    interface_subinterface_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6UnnumberedState"
                                                    interface_subinterface_state_dict_buffer["isPartOf"] = {}
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                    enabled = state.get("enabled")
                                                    if enabled is not None:
                                                        element_text = enabled
                                                        interface_subinterface_state_dict_buffer["enabled"] = {}
                                                        interface_subinterface_state_dict_buffer["enabled"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                    dict_buffers.append(interface_subinterface_state_dict_buffer)
                                            interface_ref = unnumbered.get("interface-ref")
                                            if isinstance(interface_ref, dict):
                                                if interface_ref is not None and len(interface_ref) != 0:
                                                    config = interface_ref.get("config")
                                                    if isinstance(config, dict):
                                                        if config is not None and len(config) != 0:
                                                            interface_subinterface_config_dict_buffer = {}
                                                            interface_subinterface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6UnnumberedInterfaceRefConfig:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                            interface_subinterface_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6UnnumberedInterfaceRefConfig"
                                                            interface_subinterface_config_dict_buffer["isPartOf"] = {}
                                                            interface_subinterface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_subinterface_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                            interface = config.get("interface")
                                                            if interface is not None:
                                                                element_text = interface
                                                                if interface_subinterface_config_dict_buffer["id"].split(":")[-1] != element_text:
                                                                    interface_subinterface_config_dict_buffer["id"] = interface_subinterface_config_dict_buffer["id"] + element_text
                                                                interface_subinterface_config_dict_buffer["interface"] = {}
                                                                interface_subinterface_config_dict_buffer["interface"]["type"] = "Relationship"
                                                                interface_subinterface_config_dict_buffer["interface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6UnnumberedInterfaceRefConfigInterface:" + interface_subinterface_config_dict_buffer["id"].split(":")[-1]
                                                            subinterface = config.get("subinterface")
                                                            if subinterface is not None:
                                                                element_text = subinterface
                                                                if "." + str(element_text) not in interface_subinterface_config_dict_buffer["id"].split(":")[-1]:
                                                                    interface_subinterface_config_dict_buffer["id"] = interface_subinterface_config_dict_buffer["id"] + "." + str(element_text)
                                                                interface_subinterface_config_dict_buffer["subinterface"] = {}
                                                                interface_subinterface_config_dict_buffer["subinterface"]["type"] = "Relationship"
                                                                interface_subinterface_config_dict_buffer["subinterface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6UnnumberedInterfaceRefConfigSubinterface:" + interface_subinterface_config_dict_buffer["id"].split(":")[-1]
                                                            dict_buffers.append(interface_subinterface_config_dict_buffer)
                                                    state = interface_ref.get("state")
                                                    if isinstance(state, dict):
                                                        if state is not None and len(state) != 0:
                                                            interface_subinterface_state_dict_buffer = {}
                                                            interface_subinterface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6UnnumberedInterfaceRefState:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                            interface_subinterface_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6UnnumberedInterfaceRefState"
                                                            interface_subinterface_state_dict_buffer["isPartOf"] = {}
                                                            interface_subinterface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_subinterface_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                            interface = state.get("interface")
                                                            if interface is not None:
                                                                element_text = interface
                                                                if interface_subinterface_state_dict_buffer["id"].split(":")[-1] != element_text:
                                                                    interface_subinterface_state_dict_buffer["id"] = interface_subinterface_state_dict_buffer["id"] + element_text
                                                                interface_subinterface_state_dict_buffer["interface"] = {}
                                                                interface_subinterface_state_dict_buffer["interface"]["type"] = "Relationship"
                                                                interface_subinterface_state_dict_buffer["interface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6UnnumberedInterfaceRefStateInterface:" + interface_subinterface_state_dict_buffer["id"].split(":")[-1]
                                                            subinterface = state.get("subinterface")
                                                            if subinterface is not None:
                                                                element_text = subinterface
                                                                if "." + str(element_text) not in interface_subinterface_state_dict_buffer["id"].split(":")[-1]:
                                                                    interface_subinterface_state_dict_buffer["id"] = interface_subinterface_state_dict_buffer["id"] + "." + str(element_text)
                                                                interface_subinterface_state_dict_buffer["subinterface"] = {}
                                                                interface_subinterface_state_dict_buffer["subinterface"]["type"] = "Relationship"
                                                                interface_subinterface_state_dict_buffer["subinterface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6UnnumberedInterfaceRefStateSubinterface:" + interface_subinterface_state_dict_buffer["id"].split(":")[-1]
                                                            dict_buffers.append(interface_subinterface_state_dict_buffer)
                                    config = ipv6.get("config")
                                    if isinstance(config, dict):
                                        if config is not None and len(config) != 0:
                                            interface_subinterface_config_dict_buffer = {}
                                            interface_subinterface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6Config:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                            interface_subinterface_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6Config"
                                            interface_subinterface_config_dict_buffer["isPartOf"] = {}
                                            interface_subinterface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                            interface_subinterface_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                            enabled = config.get("enabled")
                                            if enabled is not None:
                                                element_text = enabled
                                                interface_subinterface_config_dict_buffer["enabled"] = {}
                                                interface_subinterface_config_dict_buffer["enabled"]["type"] = "Property"
                                                interface_subinterface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                            mtu = config.get("mtu")
                                            if mtu is not None:
                                                element_text = mtu
                                                interface_subinterface_config_dict_buffer["mtu"] = {}
                                                interface_subinterface_config_dict_buffer["mtu"]["type"] = "Property"
                                                interface_subinterface_config_dict_buffer["mtu"]["value"] = int(element_text)
                                            dupAddrDetectTransmits = config.get("dup-addr-detect-transmits")
                                            if dupAddrDetectTransmits is not None:
                                                element_text = dupAddrDetectTransmits
                                                interface_subinterface_config_dict_buffer["dupAddrDetectTransmits"] = {}
                                                interface_subinterface_config_dict_buffer["dupAddrDetectTransmits"]["type"] = "Property"
                                                interface_subinterface_config_dict_buffer["dupAddrDetectTransmits"]["value"] = int(element_text)
                                            dhcpClient = config.get("dhcp-client")
                                            if dhcpClient is not None:
                                                element_text = dhcpClient
                                                interface_subinterface_config_dict_buffer["dhcpClient"] = {}
                                                interface_subinterface_config_dict_buffer["dhcpClient"]["type"] = "Property"
                                                interface_subinterface_config_dict_buffer["dhcpClient"]["value"] = eval(str(element_text).capitalize())
                                            dict_buffers.append(interface_subinterface_config_dict_buffer)
                                    state = ipv6.get("state")
                                    if isinstance(state, dict):
                                        if state is not None and len(state) != 0:
                                            interface_subinterface_state_dict_buffer = {}
                                            interface_subinterface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6State:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                            interface_subinterface_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6State"
                                            interface_subinterface_state_dict_buffer["isPartOf"] = {}
                                            interface_subinterface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                            interface_subinterface_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                            enabled = state.get("enabled")
                                            if enabled is not None:
                                                element_text = enabled
                                                interface_subinterface_state_dict_buffer["enabled"] = {}
                                                interface_subinterface_state_dict_buffer["enabled"]["type"] = "Property"
                                                interface_subinterface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                            mtu = state.get("mtu")
                                            if mtu is not None:
                                                element_text = mtu
                                                interface_subinterface_state_dict_buffer["mtu"] = {}
                                                interface_subinterface_state_dict_buffer["mtu"]["type"] = "Property"
                                                interface_subinterface_state_dict_buffer["mtu"]["value"] = int(element_text)
                                            dupAddrDetectTransmits = state.get("dup-addr-detect-transmits")
                                            if dupAddrDetectTransmits is not None:
                                                element_text = dupAddrDetectTransmits
                                                interface_subinterface_state_dict_buffer["dupAddrDetectTransmits"] = {}
                                                interface_subinterface_state_dict_buffer["dupAddrDetectTransmits"]["type"] = "Property"
                                                interface_subinterface_state_dict_buffer["dupAddrDetectTransmits"]["value"] = int(element_text)
                                            dhcpClient = state.get("dhcp-client")
                                            if dhcpClient is not None:
                                                element_text = dhcpClient
                                                interface_subinterface_state_dict_buffer["dhcpClient"] = {}
                                                interface_subinterface_state_dict_buffer["dhcpClient"]["type"] = "Property"
                                                interface_subinterface_state_dict_buffer["dhcpClient"]["value"] = eval(str(element_text).capitalize())
                                            counters = state.get("counters")
                                            if isinstance(counters, dict):
                                                if counters is not None and len(counters) != 0:
                                                    interface_subinterface_state_counters_dict_buffer = {}
                                                    interface_subinterface_state_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6StateCounters:" + interface_subinterface_state_dict_buffer["id"].split(":")[-1]
                                                    interface_subinterface_state_counters_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6StateCounters"
                                                    interface_subinterface_state_counters_dict_buffer["isPartOf"] = {}
                                                    interface_subinterface_state_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_subinterface_state_counters_dict_buffer["isPartOf"]["object"] = interface_subinterface_state_dict_buffer["id"]
                                                    inPkts = counters.get("in-pkts")
                                                    if inPkts is not None:
                                                        element_text = inPkts
                                                        interface_subinterface_state_counters_dict_buffer["inPkts"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["inPkts"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["inPkts"]["value"] = int(element_text)
                                                    inOctets = counters.get("in-octets")
                                                    if inOctets is not None:
                                                        element_text = inOctets
                                                        interface_subinterface_state_counters_dict_buffer["inOctets"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["inOctets"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["inOctets"]["value"] = int(element_text)
                                                    inErrorPkts = counters.get("in-error-pkts")
                                                    if inErrorPkts is not None:
                                                        element_text = inErrorPkts
                                                        interface_subinterface_state_counters_dict_buffer["inErrorPkts"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["inErrorPkts"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["inErrorPkts"]["value"] = int(element_text)
                                                    inForwardedPkts = counters.get("in-forwarded-pkts")
                                                    if inForwardedPkts is not None:
                                                        element_text = inForwardedPkts
                                                        interface_subinterface_state_counters_dict_buffer["inForwardedPkts"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["inForwardedPkts"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["inForwardedPkts"]["value"] = int(element_text)
                                                    inForwardedOctets = counters.get("in-forwarded-octets")
                                                    if inForwardedOctets is not None:
                                                        element_text = inForwardedOctets
                                                        interface_subinterface_state_counters_dict_buffer["inForwardedOctets"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["inForwardedOctets"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["inForwardedOctets"]["value"] = int(element_text)
                                                    inDiscardedPkts = counters.get("in-discarded-pkts")
                                                    if inDiscardedPkts is not None:
                                                        element_text = inDiscardedPkts
                                                        interface_subinterface_state_counters_dict_buffer["inDiscardedPkts"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["inDiscardedPkts"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["inDiscardedPkts"]["value"] = int(element_text)
                                                    outPkts = counters.get("out-pkts")
                                                    if outPkts is not None:
                                                        element_text = outPkts
                                                        interface_subinterface_state_counters_dict_buffer["outPkts"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["outPkts"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["outPkts"]["value"] = int(element_text)
                                                    outOctets = counters.get("out-octets")
                                                    if outOctets is not None:
                                                        element_text = outOctets
                                                        interface_subinterface_state_counters_dict_buffer["outOctets"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["outOctets"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["outOctets"]["value"] = int(element_text)
                                                    outErrorPkts = counters.get("out-error-pkts")
                                                    if outErrorPkts is not None:
                                                        element_text = outErrorPkts
                                                        interface_subinterface_state_counters_dict_buffer["outErrorPkts"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["outErrorPkts"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["outErrorPkts"]["value"] = int(element_text)
                                                    outForwardedPkts = counters.get("out-forwarded-pkts")
                                                    if outForwardedPkts is not None:
                                                        element_text = outForwardedPkts
                                                        interface_subinterface_state_counters_dict_buffer["outForwardedPkts"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["outForwardedPkts"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["outForwardedPkts"]["value"] = int(element_text)
                                                    outForwardedOctets = counters.get("out-forwarded-octets")
                                                    if outForwardedOctets is not None:
                                                        element_text = outForwardedOctets
                                                        interface_subinterface_state_counters_dict_buffer["outForwardedOctets"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["outForwardedOctets"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["outForwardedOctets"]["value"] = int(element_text)
                                                    outDiscardedPkts = counters.get("out-discarded-pkts")
                                                    if outDiscardedPkts is not None:
                                                        element_text = outDiscardedPkts
                                                        interface_subinterface_state_counters_dict_buffer["outDiscardedPkts"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["outDiscardedPkts"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["outDiscardedPkts"]["value"] = int(element_text)
                                                    dict_buffers.append(interface_subinterface_state_counters_dict_buffer)
                                            dict_buffers.append(interface_subinterface_state_dict_buffer)
                            dict_buffers.append(interface_subinterface_dict_buffer)
                ethernet = interface.get("openconfig-if-ethernet:ethernet")
                if isinstance(ethernet, dict):
                    if ethernet is not None and len(ethernet) != 0:
                        config = ethernet.get("config")
                        if isinstance(config, dict):
                            if config is not None and len(config) != 0:
                                interface_config_dict_buffer = {}
                                interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetConfig:" + interface_dict_buffer["id"].split(":")[-1]
                                interface_config_dict_buffer["type"] = "InterfaceEthernetConfig"
                                interface_config_dict_buffer["isPartOf"] = {}
                                interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                macAddress = config.get("mac-address")
                                if macAddress is not None:
                                    element_text = macAddress
                                    interface_config_dict_buffer["macAddress"] = {}
                                    interface_config_dict_buffer["macAddress"]["type"] = "Property"
                                    interface_config_dict_buffer["macAddress"]["value"] = element_text
                                autoNegotiate = config.get("auto-negotiate")
                                if autoNegotiate is not None:
                                    element_text = autoNegotiate
                                    interface_config_dict_buffer["autoNegotiate"] = {}
                                    interface_config_dict_buffer["autoNegotiate"]["type"] = "Property"
                                    interface_config_dict_buffer["autoNegotiate"]["value"] = eval(str(element_text).capitalize())
                                duplexMode = config.get("duplex-mode")
                                if duplexMode is not None:
                                    element_text = duplexMode
                                    interface_config_dict_buffer["duplexMode"] = {}
                                    interface_config_dict_buffer["duplexMode"]["type"] = "Property"
                                    interface_config_dict_buffer["duplexMode"]["value"] = element_text
                                portSpeed = config.get("port-speed")
                                if portSpeed is not None and len(portSpeed) != 0:
                                    element_text = portSpeed
                                    if element_text is not None:
                                        interface_config_dict_buffer["port-speed"] = {}
                                        interface_config_dict_buffer["port-speed"]["type"] = "Relationship"
                                        interface_config_dict_buffer["port-speed"]["object"] = "urn:ngsi-ld:YANGIdentity:" + element_text
                                enableFlowControl = config.get("enable-flow-control")
                                if enableFlowControl is not None:
                                    element_text = enableFlowControl
                                    interface_config_dict_buffer["enableFlowControl"] = {}
                                    interface_config_dict_buffer["enableFlowControl"]["type"] = "Property"
                                    interface_config_dict_buffer["enableFlowControl"]["value"] = eval(str(element_text).capitalize())
                                dict_buffers.append(interface_config_dict_buffer)
                        state = ethernet.get("state")
                        if isinstance(state, dict):
                            if state is not None and len(state) != 0:
                                interface_state_dict_buffer = {}
                                interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetState:" + interface_dict_buffer["id"].split(":")[-1]
                                interface_state_dict_buffer["type"] = "InterfaceEthernetState"
                                interface_state_dict_buffer["isPartOf"] = {}
                                interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                macAddress = state.get("mac-address")
                                if macAddress is not None:
                                    element_text = macAddress
                                    interface_state_dict_buffer["macAddress"] = {}
                                    interface_state_dict_buffer["macAddress"]["type"] = "Property"
                                    interface_state_dict_buffer["macAddress"]["value"] = element_text
                                autoNegotiate = state.get("auto-negotiate")
                                if autoNegotiate is not None:
                                    element_text = autoNegotiate
                                    interface_state_dict_buffer["autoNegotiate"] = {}
                                    interface_state_dict_buffer["autoNegotiate"]["type"] = "Property"
                                    interface_state_dict_buffer["autoNegotiate"]["value"] = eval(str(element_text).capitalize())
                                duplexMode = state.get("duplex-mode")
                                if duplexMode is not None:
                                    element_text = duplexMode
                                    interface_state_dict_buffer["duplexMode"] = {}
                                    interface_state_dict_buffer["duplexMode"]["type"] = "Property"
                                    interface_state_dict_buffer["duplexMode"]["value"] = element_text
                                portSpeed = state.get("port-speed")
                                if portSpeed is not None and len(portSpeed) != 0:
                                    element_text = portSpeed
                                    if element_text is not None:
                                        interface_state_dict_buffer["port-speed"] = {}
                                        interface_state_dict_buffer["port-speed"]["type"] = "Relationship"
                                        interface_state_dict_buffer["port-speed"]["object"] = "urn:ngsi-ld:YANGIdentity:" + element_text
                                enableFlowControl = state.get("enable-flow-control")
                                if enableFlowControl is not None:
                                    element_text = enableFlowControl
                                    interface_state_dict_buffer["enableFlowControl"] = {}
                                    interface_state_dict_buffer["enableFlowControl"]["type"] = "Property"
                                    interface_state_dict_buffer["enableFlowControl"]["value"] = eval(str(element_text).capitalize())
                                hwMacAddress = state.get("hw-mac-address")
                                if hwMacAddress is not None:
                                    element_text = hwMacAddress
                                    interface_state_dict_buffer["hwMacAddress"] = {}
                                    interface_state_dict_buffer["hwMacAddress"]["type"] = "Property"
                                    interface_state_dict_buffer["hwMacAddress"]["value"] = element_text
                                negotiatedDuplexMode = state.get("negotiated-duplex-mode")
                                if negotiatedDuplexMode is not None:
                                    element_text = negotiatedDuplexMode
                                    interface_state_dict_buffer["negotiatedDuplexMode"] = {}
                                    interface_state_dict_buffer["negotiatedDuplexMode"]["type"] = "Property"
                                    interface_state_dict_buffer["negotiatedDuplexMode"]["value"] = element_text
                                negotiatedPortSpeed = state.get("negotiated-port-speed")
                                if negotiatedPortSpeed is not None and len(negotiatedPortSpeed) != 0:
                                    element_text = negotiatedPortSpeed
                                    if element_text is not None:
                                        interface_state_dict_buffer["negotiated-port-speed"] = {}
                                        interface_state_dict_buffer["negotiated-port-speed"]["type"] = "Relationship"
                                        interface_state_dict_buffer["negotiated-port-speed"]["object"] = "urn:ngsi-ld:YANGIdentity:" + element_text
                                counters = state.get("counters")
                                if isinstance(counters, dict):
                                    if counters is not None and len(counters) != 0:
                                        interface_state_counters_dict_buffer = {}
                                        interface_state_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetStateCounters:" + interface_state_dict_buffer["id"].split(":")[-1]
                                        interface_state_counters_dict_buffer["type"] = "InterfaceEthernetStateCounters"
                                        interface_state_counters_dict_buffer["isPartOf"] = {}
                                        interface_state_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                                        interface_state_counters_dict_buffer["isPartOf"]["object"] = interface_state_dict_buffer["id"]
                                        inMacControlFrames = counters.get("in-mac-control-frames")
                                        if inMacControlFrames is not None:
                                            element_text = inMacControlFrames
                                            interface_state_counters_dict_buffer["inMacControlFrames"] = {}
                                            interface_state_counters_dict_buffer["inMacControlFrames"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["inMacControlFrames"]["value"] = int(element_text)
                                        inMacPauseFrames = counters.get("in-mac-pause-frames")
                                        if inMacPauseFrames is not None:
                                            element_text = inMacPauseFrames
                                            interface_state_counters_dict_buffer["inMacPauseFrames"] = {}
                                            interface_state_counters_dict_buffer["inMacPauseFrames"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["inMacPauseFrames"]["value"] = int(element_text)
                                        inOversizeFrames = counters.get("in-oversize-frames")
                                        if inOversizeFrames is not None:
                                            element_text = inOversizeFrames
                                            interface_state_counters_dict_buffer["inOversizeFrames"] = {}
                                            interface_state_counters_dict_buffer["inOversizeFrames"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["inOversizeFrames"]["value"] = int(element_text)
                                        inJabberFrames = counters.get("in-jabber-frames")
                                        if inJabberFrames is not None:
                                            element_text = inJabberFrames
                                            interface_state_counters_dict_buffer["inJabberFrames"] = {}
                                            interface_state_counters_dict_buffer["inJabberFrames"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["inJabberFrames"]["value"] = int(element_text)
                                        inFragmentFrames = counters.get("in-fragment-frames")
                                        if inFragmentFrames is not None:
                                            element_text = inFragmentFrames
                                            interface_state_counters_dict_buffer["inFragmentFrames"] = {}
                                            interface_state_counters_dict_buffer["inFragmentFrames"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["inFragmentFrames"]["value"] = int(element_text)
                                        in8021qFrames = counters.get("in-8021q-frames")
                                        if in8021qFrames is not None:
                                            element_text = in8021qFrames
                                            interface_state_counters_dict_buffer["in8021qFrames"] = {}
                                            interface_state_counters_dict_buffer["in8021qFrames"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["in8021qFrames"]["value"] = int(element_text)
                                        inCrcErrors = counters.get("in-crc-errors")
                                        if inCrcErrors is not None:
                                            element_text = inCrcErrors
                                            interface_state_counters_dict_buffer["inCrcErrors"] = {}
                                            interface_state_counters_dict_buffer["inCrcErrors"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["inCrcErrors"]["value"] = int(element_text)
                                        outMacControlFrames = counters.get("out-mac-control-frames")
                                        if outMacControlFrames is not None:
                                            element_text = outMacControlFrames
                                            interface_state_counters_dict_buffer["outMacControlFrames"] = {}
                                            interface_state_counters_dict_buffer["outMacControlFrames"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["outMacControlFrames"]["value"] = int(element_text)
                                        outMacPauseFrames = counters.get("out-mac-pause-frames")
                                        if outMacPauseFrames is not None:
                                            element_text = outMacPauseFrames
                                            interface_state_counters_dict_buffer["outMacPauseFrames"] = {}
                                            interface_state_counters_dict_buffer["outMacPauseFrames"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["outMacPauseFrames"]["value"] = int(element_text)
                                        out8021qFrames = counters.get("out-8021q-frames")
                                        if out8021qFrames is not None:
                                            element_text = out8021qFrames
                                            interface_state_counters_dict_buffer["out8021qFrames"] = {}
                                            interface_state_counters_dict_buffer["out8021qFrames"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["out8021qFrames"]["value"] = int(element_text)
                                        dict_buffers.append(interface_state_counters_dict_buffer)
                                dict_buffers.append(interface_state_dict_buffer)
                dict_buffers.append(interface_dict_buffer)

output_file = open("dict_buffers_queries.json", 'w')
output_file.write(json.dumps(dict_buffers[::-1], indent=4))
output_file.close()
dict_buffers.clear()
