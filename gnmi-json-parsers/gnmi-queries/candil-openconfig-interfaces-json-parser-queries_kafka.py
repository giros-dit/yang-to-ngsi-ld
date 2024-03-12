import json
import numpy as np
from kafka import KafkaConsumer
from kafka import KafkaProducer

dict_buffers = []
consumer = KafkaConsumer('input', bootstrap_servers=['localhost:9092'], value_deserializer=lambda x: json.loads(x.decode('utf-8')))
while True:
    for message in consumer:
        data = json.loads(message.value)
        json_data = data[0]["updates"][0]["values"]
        timestamp_data = int(data[0]["timestamp"])
        datetime_ns = np.datetime64(timestamp_data, 'ns')
        observed_at = str(datetime_ns.astype('datetime64[ms]')) + 'Z'

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
                            interface_dict_buffer["name"]["observedAt"] = observed_at
                        config = interface.get("config")
                        if isinstance(config, dict):
                            if config is not None and len(config) != 0:
                                interface_config_dict_buffer = {}
                                interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceConfig:" + interface_dict_buffer["id"].split(":")[-1]
                                interface_config_dict_buffer["type"] = "InterfaceConfig"
                                interface_config_dict_buffer["isPartOf"] = {}
                                interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                name = config.get("name")
                                if name is not None:
                                    element_text = name
                                    if interface_config_dict_buffer["id"].split(":")[-1] != element_text:
                                        interface_config_dict_buffer["id"] = interface_config_dict_buffer["id"] + element_text
                                    interface_config_dict_buffer["name"] = {}
                                    interface_config_dict_buffer["name"]["type"] = "Property"
                                    interface_config_dict_buffer["name"]["value"] = element_text
                                    interface_config_dict_buffer["name"]["observedAt"] = observed_at
                                type = config.get("type")
                                if type is not None and len(type) != 0:
                                    element_text = type
                                    if element_text is not None:
                                        interface_config_dict_buffer["configType"] = {}
                                        interface_config_dict_buffer["configType"]["type"] = "Relationship"
                                        interface_config_dict_buffer["configType"]["object"] = "urn:ngsi-ld:YANGIdentity:" + element_text
                                        interface_config_dict_buffer["configType"]["observedAt"] = observed_at
                                mtu = config.get("mtu")
                                if mtu is not None:
                                    element_text = mtu
                                    interface_config_dict_buffer["mtu"] = {}
                                    interface_config_dict_buffer["mtu"]["type"] = "Property"
                                    interface_config_dict_buffer["mtu"]["value"] = int(element_text)
                                    interface_config_dict_buffer["mtu"]["observedAt"] = observed_at
                                loopbackMode = config.get("loopback-mode")
                                if loopbackMode is not None:
                                    element_text = loopbackMode
                                    interface_config_dict_buffer["loopbackMode"] = {}
                                    interface_config_dict_buffer["loopbackMode"]["type"] = "Property"
                                    interface_config_dict_buffer["loopbackMode"]["value"] = eval(str(element_text).capitalize())
                                    interface_config_dict_buffer["loopbackMode"]["observedAt"] = observed_at
                                description = config.get("description")
                                if description is not None:
                                    element_text = description
                                    interface_config_dict_buffer["description"] = {}
                                    interface_config_dict_buffer["description"]["type"] = "Property"
                                    interface_config_dict_buffer["description"]["value"] = element_text
                                    interface_config_dict_buffer["description"]["observedAt"] = observed_at
                                enabled = config.get("enabled")
                                if enabled is not None:
                                    element_text = enabled
                                    interface_config_dict_buffer["enabled"] = {}
                                    interface_config_dict_buffer["enabled"]["type"] = "Property"
                                    interface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                    interface_config_dict_buffer["enabled"]["observedAt"] = observed_at
                                tpid = config.get("tpid")
                                if tpid is not None and len(tpid) != 0:
                                    element_text = tpid
                                    if element_text is not None:
                                        interface_config_dict_buffer["tpid"] = {}
                                        interface_config_dict_buffer["tpid"]["type"] = "Relationship"
                                        interface_config_dict_buffer["tpid"]["object"] = "urn:ngsi-ld:YANGIdentity:" + element_text
                                        interface_config_dict_buffer["tpid"]["observedAt"] = observed_at
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
                                interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                name = state.get("name")
                                if name is not None:
                                    element_text = name
                                    if interface_state_dict_buffer["id"].split(":")[-1] != element_text:
                                        interface_state_dict_buffer["id"] = interface_state_dict_buffer["id"] + element_text
                                    interface_state_dict_buffer["name"] = {}
                                    interface_state_dict_buffer["name"]["type"] = "Property"
                                    interface_state_dict_buffer["name"]["value"] = element_text
                                    interface_state_dict_buffer["name"]["observedAt"] = observed_at
                                type = state.get("type")
                                if type is not None and len(type) != 0:
                                    element_text = type
                                    if element_text is not None:
                                        interface_state_dict_buffer["stateType"] = {}
                                        interface_state_dict_buffer["stateType"]["type"] = "Relationship"
                                        interface_state_dict_buffer["stateType"]["object"] = "urn:ngsi-ld:YANGIdentity:" + element_text
                                        interface_state_dict_buffer["stateType"]["observedAt"] = observed_at
                                mtu = state.get("mtu")
                                if mtu is not None:
                                    element_text = mtu
                                    interface_state_dict_buffer["mtu"] = {}
                                    interface_state_dict_buffer["mtu"]["type"] = "Property"
                                    interface_state_dict_buffer["mtu"]["value"] = int(element_text)
                                    interface_state_dict_buffer["mtu"]["observedAt"] = observed_at
                                loopbackMode = state.get("loopback-mode")
                                if loopbackMode is not None:
                                    element_text = loopbackMode
                                    interface_state_dict_buffer["loopbackMode"] = {}
                                    interface_state_dict_buffer["loopbackMode"]["type"] = "Property"
                                    interface_state_dict_buffer["loopbackMode"]["value"] = eval(str(element_text).capitalize())
                                    interface_state_dict_buffer["loopbackMode"]["observedAt"] = observed_at
                                description = state.get("description")
                                if description is not None:
                                    element_text = description
                                    interface_state_dict_buffer["description"] = {}
                                    interface_state_dict_buffer["description"]["type"] = "Property"
                                    interface_state_dict_buffer["description"]["value"] = element_text
                                    interface_state_dict_buffer["description"]["observedAt"] = observed_at
                                enabled = state.get("enabled")
                                if enabled is not None:
                                    element_text = enabled
                                    interface_state_dict_buffer["enabled"] = {}
                                    interface_state_dict_buffer["enabled"]["type"] = "Property"
                                    interface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                    interface_state_dict_buffer["enabled"]["observedAt"] = observed_at
                                ifindex = state.get("ifindex")
                                if ifindex is not None:
                                    element_text = ifindex
                                    interface_state_dict_buffer["ifindex"] = {}
                                    interface_state_dict_buffer["ifindex"]["type"] = "Property"
                                    interface_state_dict_buffer["ifindex"]["value"] = int(element_text)
                                    interface_state_dict_buffer["ifindex"]["observedAt"] = observed_at
                                adminStatus = state.get("admin-status")
                                if adminStatus is not None:
                                    element_text = adminStatus
                                    interface_state_dict_buffer["adminStatus"] = {}
                                    interface_state_dict_buffer["adminStatus"]["type"] = "Property"
                                    interface_state_dict_buffer["adminStatus"]["value"] = element_text
                                    interface_state_dict_buffer["adminStatus"]["observedAt"] = observed_at
                                operStatus = state.get("oper-status")
                                if operStatus is not None:
                                    element_text = operStatus
                                    interface_state_dict_buffer["operStatus"] = {}
                                    interface_state_dict_buffer["operStatus"]["type"] = "Property"
                                    interface_state_dict_buffer["operStatus"]["value"] = element_text
                                    interface_state_dict_buffer["operStatus"]["observedAt"] = observed_at
                                lastChange = state.get("last-change")
                                if lastChange is not None:
                                    element_text = lastChange
                                    interface_state_dict_buffer["lastChange"] = {}
                                    interface_state_dict_buffer["lastChange"]["type"] = "Property"
                                    interface_state_dict_buffer["lastChange"]["value"] = int(element_text)
                                    interface_state_dict_buffer["lastChange"]["observedAt"] = observed_at
                                counters = state.get("counters")
                                if isinstance(counters, dict):
                                    if counters is not None and len(counters) != 0:
                                        interface_state_counters_dict_buffer = {}
                                        interface_state_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceStateCounters:" + interface_state_dict_buffer["id"].split(":")[-1]
                                        interface_state_counters_dict_buffer["type"] = "InterfaceStateCounters"
                                        interface_state_counters_dict_buffer["isPartOf"] = {}
                                        interface_state_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                                        interface_state_counters_dict_buffer["isPartOf"]["object"] = interface_state_dict_buffer["id"]
                                        interface_state_counters_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                        inOctets = counters.get("in-octets")
                                        if inOctets is not None:
                                            element_text = inOctets
                                            interface_state_counters_dict_buffer["inOctets"] = {}
                                            interface_state_counters_dict_buffer["inOctets"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["inOctets"]["value"] = int(element_text)
                                            interface_state_counters_dict_buffer["inOctets"]["observedAt"] = observed_at
                                        inUnicastPkts = counters.get("in-unicast-pkts")
                                        if inUnicastPkts is not None:
                                            element_text = inUnicastPkts
                                            interface_state_counters_dict_buffer["inUnicastPkts"] = {}
                                            interface_state_counters_dict_buffer["inUnicastPkts"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["inUnicastPkts"]["value"] = int(element_text)
                                            interface_state_counters_dict_buffer["inUnicastPkts"]["observedAt"] = observed_at
                                        inBroadcastPkts = counters.get("in-broadcast-pkts")
                                        if inBroadcastPkts is not None:
                                            element_text = inBroadcastPkts
                                            interface_state_counters_dict_buffer["inBroadcastPkts"] = {}
                                            interface_state_counters_dict_buffer["inBroadcastPkts"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["inBroadcastPkts"]["value"] = int(element_text)
                                            interface_state_counters_dict_buffer["inBroadcastPkts"]["observedAt"] = observed_at
                                        inMulticastPkts = counters.get("in-multicast-pkts")
                                        if inMulticastPkts is not None:
                                            element_text = inMulticastPkts
                                            interface_state_counters_dict_buffer["inMulticastPkts"] = {}
                                            interface_state_counters_dict_buffer["inMulticastPkts"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["inMulticastPkts"]["value"] = int(element_text)
                                            interface_state_counters_dict_buffer["inMulticastPkts"]["observedAt"] = observed_at
                                        inDiscards = counters.get("in-discards")
                                        if inDiscards is not None:
                                            element_text = inDiscards
                                            interface_state_counters_dict_buffer["inDiscards"] = {}
                                            interface_state_counters_dict_buffer["inDiscards"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["inDiscards"]["value"] = int(element_text)
                                            interface_state_counters_dict_buffer["inDiscards"]["observedAt"] = observed_at
                                        inErrors = counters.get("in-errors")
                                        if inErrors is not None:
                                            element_text = inErrors
                                            interface_state_counters_dict_buffer["inErrors"] = {}
                                            interface_state_counters_dict_buffer["inErrors"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["inErrors"]["value"] = int(element_text)
                                            interface_state_counters_dict_buffer["inErrors"]["observedAt"] = observed_at
                                        inUnknownProtos = counters.get("in-unknown-protos")
                                        if inUnknownProtos is not None:
                                            element_text = inUnknownProtos
                                            interface_state_counters_dict_buffer["inUnknownProtos"] = {}
                                            interface_state_counters_dict_buffer["inUnknownProtos"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["inUnknownProtos"]["value"] = int(element_text)
                                            interface_state_counters_dict_buffer["inUnknownProtos"]["observedAt"] = observed_at
                                        inFcsErrors = counters.get("in-fcs-errors")
                                        if inFcsErrors is not None:
                                            element_text = inFcsErrors
                                            interface_state_counters_dict_buffer["inFcsErrors"] = {}
                                            interface_state_counters_dict_buffer["inFcsErrors"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["inFcsErrors"]["value"] = int(element_text)
                                            interface_state_counters_dict_buffer["inFcsErrors"]["observedAt"] = observed_at
                                        outOctets = counters.get("out-octets")
                                        if outOctets is not None:
                                            element_text = outOctets
                                            interface_state_counters_dict_buffer["outOctets"] = {}
                                            interface_state_counters_dict_buffer["outOctets"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["outOctets"]["value"] = int(element_text)
                                            interface_state_counters_dict_buffer["outOctets"]["observedAt"] = observed_at
                                        outUnicastPkts = counters.get("out-unicast-pkts")
                                        if outUnicastPkts is not None:
                                            element_text = outUnicastPkts
                                            interface_state_counters_dict_buffer["outUnicastPkts"] = {}
                                            interface_state_counters_dict_buffer["outUnicastPkts"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["outUnicastPkts"]["value"] = int(element_text)
                                            interface_state_counters_dict_buffer["outUnicastPkts"]["observedAt"] = observed_at
                                        outBroadcastPkts = counters.get("out-broadcast-pkts")
                                        if outBroadcastPkts is not None:
                                            element_text = outBroadcastPkts
                                            interface_state_counters_dict_buffer["outBroadcastPkts"] = {}
                                            interface_state_counters_dict_buffer["outBroadcastPkts"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["outBroadcastPkts"]["value"] = int(element_text)
                                            interface_state_counters_dict_buffer["outBroadcastPkts"]["observedAt"] = observed_at
                                        outMulticastPkts = counters.get("out-multicast-pkts")
                                        if outMulticastPkts is not None:
                                            element_text = outMulticastPkts
                                            interface_state_counters_dict_buffer["outMulticastPkts"] = {}
                                            interface_state_counters_dict_buffer["outMulticastPkts"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["outMulticastPkts"]["value"] = int(element_text)
                                            interface_state_counters_dict_buffer["outMulticastPkts"]["observedAt"] = observed_at
                                        outDiscards = counters.get("out-discards")
                                        if outDiscards is not None:
                                            element_text = outDiscards
                                            interface_state_counters_dict_buffer["outDiscards"] = {}
                                            interface_state_counters_dict_buffer["outDiscards"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["outDiscards"]["value"] = int(element_text)
                                            interface_state_counters_dict_buffer["outDiscards"]["observedAt"] = observed_at
                                        outErrors = counters.get("out-errors")
                                        if outErrors is not None:
                                            element_text = outErrors
                                            interface_state_counters_dict_buffer["outErrors"] = {}
                                            interface_state_counters_dict_buffer["outErrors"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["outErrors"]["value"] = int(element_text)
                                            interface_state_counters_dict_buffer["outErrors"]["observedAt"] = observed_at
                                        carrierTransitions = counters.get("carrier-transitions")
                                        if carrierTransitions is not None:
                                            element_text = carrierTransitions
                                            interface_state_counters_dict_buffer["carrierTransitions"] = {}
                                            interface_state_counters_dict_buffer["carrierTransitions"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["carrierTransitions"]["value"] = int(element_text)
                                            interface_state_counters_dict_buffer["carrierTransitions"]["observedAt"] = observed_at
                                        lastClear = counters.get("last-clear")
                                        if lastClear is not None:
                                            element_text = lastClear
                                            interface_state_counters_dict_buffer["lastClear"] = {}
                                            interface_state_counters_dict_buffer["lastClear"]["type"] = "Property"
                                            interface_state_counters_dict_buffer["lastClear"]["value"] = int(element_text)
                                            interface_state_counters_dict_buffer["lastClear"]["observedAt"] = observed_at
                                        dict_buffers.append(interface_state_counters_dict_buffer)
                                tpid = state.get("tpid")
                                if tpid is not None and len(tpid) != 0:
                                    element_text = tpid
                                    if element_text is not None:
                                        interface_state_dict_buffer["tpid"] = {}
                                        interface_state_dict_buffer["tpid"]["type"] = "Relationship"
                                        interface_state_dict_buffer["tpid"]["object"] = "urn:ngsi-ld:YANGIdentity:" + element_text
                                        interface_state_dict_buffer["tpid"]["observedAt"] = observed_at
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
                                        interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                        up = config.get("up")
                                        if up is not None:
                                            element_text = up
                                            interface_config_dict_buffer["up"] = {}
                                            interface_config_dict_buffer["up"]["type"] = "Property"
                                            interface_config_dict_buffer["up"]["value"] = int(element_text)
                                            interface_config_dict_buffer["up"]["observedAt"] = observed_at
                                        down = config.get("down")
                                        if down is not None:
                                            element_text = down
                                            interface_config_dict_buffer["down"] = {}
                                            interface_config_dict_buffer["down"]["type"] = "Property"
                                            interface_config_dict_buffer["down"]["value"] = int(element_text)
                                            interface_config_dict_buffer["down"]["observedAt"] = observed_at
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
                                        interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                        up = state.get("up")
                                        if up is not None:
                                            element_text = up
                                            interface_state_dict_buffer["up"] = {}
                                            interface_state_dict_buffer["up"]["type"] = "Property"
                                            interface_state_dict_buffer["up"]["value"] = int(element_text)
                                            interface_state_dict_buffer["up"]["observedAt"] = observed_at
                                        down = state.get("down")
                                        if down is not None:
                                            element_text = down
                                            interface_state_dict_buffer["down"] = {}
                                            interface_state_dict_buffer["down"]["type"] = "Property"
                                            interface_state_dict_buffer["down"]["value"] = int(element_text)
                                            interface_state_dict_buffer["down"]["observedAt"] = observed_at
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
                                    interface_subinterface_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                    index = subinterface.get("index")
                                    if index is not None:
                                        element_text = index
                                        if "." + str(element_text) not in interface_subinterface_dict_buffer["id"].split(":")[-1]:
                                            interface_subinterface_dict_buffer["id"] = interface_subinterface_dict_buffer["id"] + "." + str(element_text)
                                        interface_subinterface_dict_buffer["index"] = {}
                                        interface_subinterface_dict_buffer["index"]["type"] = "Relationship"
                                        interface_subinterface_dict_buffer["index"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceConfig:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                        interface_subinterface_dict_buffer["index"]["observedAt"] = observed_at
                                    config = subinterface.get("config")
                                    if isinstance(config, dict):
                                        if config is not None and len(config) != 0:
                                            interface_subinterface_config_dict_buffer = {}
                                            interface_subinterface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceConfig:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                            interface_subinterface_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceConfig"
                                            interface_subinterface_config_dict_buffer["isPartOf"] = {}
                                            interface_subinterface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                            interface_subinterface_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                            interface_subinterface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                            index = config.get("index")
                                            if index is not None:
                                                element_text = index
                                                if "." + str(element_text) not in interface_subinterface_config_dict_buffer["id"].split(":")[-1]:
                                                    interface_subinterface_config_dict_buffer["id"] = interface_subinterface_config_dict_buffer["id"] + "." + str(element_text)
                                                interface_subinterface_config_dict_buffer["index"] = {}
                                                interface_subinterface_config_dict_buffer["index"]["type"] = "Property"
                                                interface_subinterface_config_dict_buffer["index"]["value"] = int(element_text)
                                                interface_subinterface_config_dict_buffer["index"]["observedAt"] = observed_at
                                            description = config.get("description")
                                            if description is not None:
                                                element_text = description
                                                interface_subinterface_config_dict_buffer["description"] = {}
                                                interface_subinterface_config_dict_buffer["description"]["type"] = "Property"
                                                interface_subinterface_config_dict_buffer["description"]["value"] = element_text
                                                interface_subinterface_config_dict_buffer["description"]["observedAt"] = observed_at
                                            enabled = config.get("enabled")
                                            if enabled is not None:
                                                element_text = enabled
                                                interface_subinterface_config_dict_buffer["enabled"] = {}
                                                interface_subinterface_config_dict_buffer["enabled"]["type"] = "Property"
                                                interface_subinterface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                interface_subinterface_config_dict_buffer["enabled"]["observedAt"] = observed_at
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
                                            interface_subinterface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                            index = state.get("index")
                                            if index is not None:
                                                element_text = index
                                                if "." + str(element_text) not in interface_subinterface_state_dict_buffer["id"].split(":")[-1]:
                                                    interface_subinterface_state_dict_buffer["id"] = interface_subinterface_state_dict_buffer["id"] + "." + str(element_text)
                                                interface_subinterface_state_dict_buffer["index"] = {}
                                                interface_subinterface_state_dict_buffer["index"]["type"] = "Property"
                                                interface_subinterface_state_dict_buffer["index"]["value"] = int(element_text)
                                                interface_subinterface_state_dict_buffer["index"]["observedAt"] = observed_at
                                            description = state.get("description")
                                            if description is not None:
                                                element_text = description
                                                interface_subinterface_state_dict_buffer["description"] = {}
                                                interface_subinterface_state_dict_buffer["description"]["type"] = "Property"
                                                interface_subinterface_state_dict_buffer["description"]["value"] = element_text
                                                interface_subinterface_state_dict_buffer["description"]["observedAt"] = observed_at
                                            enabled = state.get("enabled")
                                            if enabled is not None:
                                                element_text = enabled
                                                interface_subinterface_state_dict_buffer["enabled"] = {}
                                                interface_subinterface_state_dict_buffer["enabled"]["type"] = "Property"
                                                interface_subinterface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                interface_subinterface_state_dict_buffer["enabled"]["observedAt"] = observed_at
                                            name = state.get("name")
                                            if name is not None:
                                                element_text = name
                                                if interface_subinterface_state_dict_buffer["id"].split(":")[-1] != element_text:
                                                    interface_subinterface_state_dict_buffer["id"] = interface_subinterface_state_dict_buffer["id"] + element_text
                                                interface_subinterface_state_dict_buffer["name"] = {}
                                                interface_subinterface_state_dict_buffer["name"]["type"] = "Property"
                                                interface_subinterface_state_dict_buffer["name"]["value"] = element_text
                                                interface_subinterface_state_dict_buffer["name"]["observedAt"] = observed_at
                                            ifindex = state.get("ifindex")
                                            if ifindex is not None:
                                                element_text = ifindex
                                                interface_subinterface_state_dict_buffer["ifindex"] = {}
                                                interface_subinterface_state_dict_buffer["ifindex"]["type"] = "Property"
                                                interface_subinterface_state_dict_buffer["ifindex"]["value"] = int(element_text)
                                                interface_subinterface_state_dict_buffer["ifindex"]["observedAt"] = observed_at
                                            adminStatus = state.get("admin-status")
                                            if adminStatus is not None:
                                                element_text = adminStatus
                                                interface_subinterface_state_dict_buffer["adminStatus"] = {}
                                                interface_subinterface_state_dict_buffer["adminStatus"]["type"] = "Property"
                                                interface_subinterface_state_dict_buffer["adminStatus"]["value"] = element_text
                                                interface_subinterface_state_dict_buffer["adminStatus"]["observedAt"] = observed_at
                                            operStatus = state.get("oper-status")
                                            if operStatus is not None:
                                                element_text = operStatus
                                                interface_subinterface_state_dict_buffer["operStatus"] = {}
                                                interface_subinterface_state_dict_buffer["operStatus"]["type"] = "Property"
                                                interface_subinterface_state_dict_buffer["operStatus"]["value"] = element_text
                                                interface_subinterface_state_dict_buffer["operStatus"]["observedAt"] = observed_at
                                            lastChange = state.get("last-change")
                                            if lastChange is not None:
                                                element_text = lastChange
                                                interface_subinterface_state_dict_buffer["lastChange"] = {}
                                                interface_subinterface_state_dict_buffer["lastChange"]["type"] = "Property"
                                                interface_subinterface_state_dict_buffer["lastChange"]["value"] = int(element_text)
                                                interface_subinterface_state_dict_buffer["lastChange"]["observedAt"] = observed_at
                                            counters = state.get("counters")
                                            if isinstance(counters, dict):
                                                if counters is not None and len(counters) != 0:
                                                    interface_subinterface_state_counters_dict_buffer = {}
                                                    interface_subinterface_state_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceStateCounters:" + interface_subinterface_state_dict_buffer["id"].split(":")[-1]
                                                    interface_subinterface_state_counters_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceStateCounters"
                                                    interface_subinterface_state_counters_dict_buffer["isPartOf"] = {}
                                                    interface_subinterface_state_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_subinterface_state_counters_dict_buffer["isPartOf"]["object"] = interface_subinterface_state_dict_buffer["id"]
                                                    interface_subinterface_state_counters_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    inOctets = counters.get("in-octets")
                                                    if inOctets is not None:
                                                        element_text = inOctets
                                                        interface_subinterface_state_counters_dict_buffer["inOctets"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["inOctets"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["inOctets"]["value"] = int(element_text)
                                                        interface_subinterface_state_counters_dict_buffer["inOctets"]["observedAt"] = observed_at
                                                    inUnicastPkts = counters.get("in-unicast-pkts")
                                                    if inUnicastPkts is not None:
                                                        element_text = inUnicastPkts
                                                        interface_subinterface_state_counters_dict_buffer["inUnicastPkts"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["inUnicastPkts"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["inUnicastPkts"]["value"] = int(element_text)
                                                        interface_subinterface_state_counters_dict_buffer["inUnicastPkts"]["observedAt"] = observed_at
                                                    inBroadcastPkts = counters.get("in-broadcast-pkts")
                                                    if inBroadcastPkts is not None:
                                                        element_text = inBroadcastPkts
                                                        interface_subinterface_state_counters_dict_buffer["inBroadcastPkts"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["inBroadcastPkts"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["inBroadcastPkts"]["value"] = int(element_text)
                                                        interface_subinterface_state_counters_dict_buffer["inBroadcastPkts"]["observedAt"] = observed_at
                                                    inMulticastPkts = counters.get("in-multicast-pkts")
                                                    if inMulticastPkts is not None:
                                                        element_text = inMulticastPkts
                                                        interface_subinterface_state_counters_dict_buffer["inMulticastPkts"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["inMulticastPkts"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["inMulticastPkts"]["value"] = int(element_text)
                                                        interface_subinterface_state_counters_dict_buffer["inMulticastPkts"]["observedAt"] = observed_at
                                                    inDiscards = counters.get("in-discards")
                                                    if inDiscards is not None:
                                                        element_text = inDiscards
                                                        interface_subinterface_state_counters_dict_buffer["inDiscards"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["inDiscards"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["inDiscards"]["value"] = int(element_text)
                                                        interface_subinterface_state_counters_dict_buffer["inDiscards"]["observedAt"] = observed_at
                                                    inErrors = counters.get("in-errors")
                                                    if inErrors is not None:
                                                        element_text = inErrors
                                                        interface_subinterface_state_counters_dict_buffer["inErrors"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["inErrors"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["inErrors"]["value"] = int(element_text)
                                                        interface_subinterface_state_counters_dict_buffer["inErrors"]["observedAt"] = observed_at
                                                    inUnknownProtos = counters.get("in-unknown-protos")
                                                    if inUnknownProtos is not None:
                                                        element_text = inUnknownProtos
                                                        interface_subinterface_state_counters_dict_buffer["inUnknownProtos"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["inUnknownProtos"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["inUnknownProtos"]["value"] = int(element_text)
                                                        interface_subinterface_state_counters_dict_buffer["inUnknownProtos"]["observedAt"] = observed_at
                                                    inFcsErrors = counters.get("in-fcs-errors")
                                                    if inFcsErrors is not None:
                                                        element_text = inFcsErrors
                                                        interface_subinterface_state_counters_dict_buffer["inFcsErrors"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["inFcsErrors"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["inFcsErrors"]["value"] = int(element_text)
                                                        interface_subinterface_state_counters_dict_buffer["inFcsErrors"]["observedAt"] = observed_at
                                                    outOctets = counters.get("out-octets")
                                                    if outOctets is not None:
                                                        element_text = outOctets
                                                        interface_subinterface_state_counters_dict_buffer["outOctets"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["outOctets"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["outOctets"]["value"] = int(element_text)
                                                        interface_subinterface_state_counters_dict_buffer["outOctets"]["observedAt"] = observed_at
                                                    outUnicastPkts = counters.get("out-unicast-pkts")
                                                    if outUnicastPkts is not None:
                                                        element_text = outUnicastPkts
                                                        interface_subinterface_state_counters_dict_buffer["outUnicastPkts"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["outUnicastPkts"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["outUnicastPkts"]["value"] = int(element_text)
                                                        interface_subinterface_state_counters_dict_buffer["outUnicastPkts"]["observedAt"] = observed_at
                                                    outBroadcastPkts = counters.get("out-broadcast-pkts")
                                                    if outBroadcastPkts is not None:
                                                        element_text = outBroadcastPkts
                                                        interface_subinterface_state_counters_dict_buffer["outBroadcastPkts"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["outBroadcastPkts"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["outBroadcastPkts"]["value"] = int(element_text)
                                                        interface_subinterface_state_counters_dict_buffer["outBroadcastPkts"]["observedAt"] = observed_at
                                                    outMulticastPkts = counters.get("out-multicast-pkts")
                                                    if outMulticastPkts is not None:
                                                        element_text = outMulticastPkts
                                                        interface_subinterface_state_counters_dict_buffer["outMulticastPkts"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["outMulticastPkts"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["outMulticastPkts"]["value"] = int(element_text)
                                                        interface_subinterface_state_counters_dict_buffer["outMulticastPkts"]["observedAt"] = observed_at
                                                    outDiscards = counters.get("out-discards")
                                                    if outDiscards is not None:
                                                        element_text = outDiscards
                                                        interface_subinterface_state_counters_dict_buffer["outDiscards"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["outDiscards"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["outDiscards"]["value"] = int(element_text)
                                                        interface_subinterface_state_counters_dict_buffer["outDiscards"]["observedAt"] = observed_at
                                                    outErrors = counters.get("out-errors")
                                                    if outErrors is not None:
                                                        element_text = outErrors
                                                        interface_subinterface_state_counters_dict_buffer["outErrors"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["outErrors"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["outErrors"]["value"] = int(element_text)
                                                        interface_subinterface_state_counters_dict_buffer["outErrors"]["observedAt"] = observed_at
                                                    carrierTransitions = counters.get("carrier-transitions")
                                                    if carrierTransitions is not None:
                                                        element_text = carrierTransitions
                                                        interface_subinterface_state_counters_dict_buffer["carrierTransitions"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["carrierTransitions"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["carrierTransitions"]["value"] = int(element_text)
                                                        interface_subinterface_state_counters_dict_buffer["carrierTransitions"]["observedAt"] = observed_at
                                                    lastClear = counters.get("last-clear")
                                                    if lastClear is not None:
                                                        element_text = lastClear
                                                        interface_subinterface_state_counters_dict_buffer["lastClear"] = {}
                                                        interface_subinterface_state_counters_dict_buffer["lastClear"]["type"] = "Property"
                                                        interface_subinterface_state_counters_dict_buffer["lastClear"]["value"] = int(element_text)
                                                        interface_subinterface_state_counters_dict_buffer["lastClear"]["observedAt"] = observed_at
                                                    dict_buffers.append(interface_subinterface_state_counters_dict_buffer)
                                            dict_buffers.append(interface_subinterface_state_dict_buffer)
                                    vlan = subinterface.get("openconfig-vlan:vlan")
                                    if isinstance(vlan, dict):
                                        if vlan is not None and len(vlan) != 0:
                                            config = vlan.get("config")
                                            if isinstance(config, dict):
                                                if config is not None and len(config) != 0:
                                                    interface_subinterface_config_dict_buffer = {}
                                                    interface_subinterface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceVlanConfig:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                    interface_subinterface_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceVlanConfig"
                                                    interface_subinterface_config_dict_buffer["isPartOf"] = {}
                                                    interface_subinterface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_subinterface_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                    interface_subinterface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    vlanId = config.get("vlan-id")
                                                    if vlanId is not None:
                                                        element_text = vlanId
                                                        if interface_subinterface_config_dict_buffer["id"].split(":")[-1] != element_text:
                                                            interface_subinterface_config_dict_buffer["id"] = interface_subinterface_config_dict_buffer["id"] + element_text
                                                        interface_subinterface_config_dict_buffer["vlanId"] = {}
                                                        interface_subinterface_config_dict_buffer["vlanId"]["type"] = "Property"
                                                        interface_subinterface_config_dict_buffer["vlanId"]["value"] = element_text
                                                        interface_subinterface_config_dict_buffer["vlanId"]["observedAt"] = observed_at
                                                    dict_buffers.append(interface_subinterface_config_dict_buffer)
                                            state = vlan.get("state")
                                            if isinstance(state, dict):
                                                if state is not None and len(state) != 0:
                                                    interface_subinterface_state_dict_buffer = {}
                                                    interface_subinterface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceVlanState:" + interface_subinterface_dict_buffer["id"].split(":")[-1]
                                                    interface_subinterface_state_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceVlanState"
                                                    interface_subinterface_state_dict_buffer["isPartOf"] = {}
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    vlanId = state.get("vlan-id")
                                                    if vlanId is not None:
                                                        element_text = vlanId
                                                        if interface_subinterface_state_dict_buffer["id"].split(":")[-1] != element_text:
                                                            interface_subinterface_state_dict_buffer["id"] = interface_subinterface_state_dict_buffer["id"] + element_text
                                                        interface_subinterface_state_dict_buffer["vlanId"] = {}
                                                        interface_subinterface_state_dict_buffer["vlanId"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["vlanId"]["value"] = element_text
                                                        interface_subinterface_state_dict_buffer["vlanId"]["observedAt"] = observed_at
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
                                                        interface_subinterface_address_dict_buffer["isPartOf"]["observedAt"] = observed_at
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
                                                            interface_subinterface_address_dict_buffer["ip"]["observedAt"] = observed_at
                                                        config = address.get("config")
                                                        if isinstance(config, dict):
                                                            if config is not None and len(config) != 0:
                                                                interface_subinterface_address_config_dict_buffer = {}
                                                                interface_subinterface_address_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressConfig:" + interface_subinterface_address_dict_buffer["id"].split(":")[-1]
                                                                interface_subinterface_address_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressConfig"
                                                                interface_subinterface_address_config_dict_buffer["isPartOf"] = {}
                                                                interface_subinterface_address_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                interface_subinterface_address_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_dict_buffer["id"]
                                                                interface_subinterface_address_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                ip = config.get("ip")
                                                                if ip is not None:
                                                                    element_text = ip
                                                                    interface_subinterface_address_config_dict_buffer["ip"] = {}
                                                                    interface_subinterface_address_config_dict_buffer["ip"]["type"] = "Property"
                                                                    interface_subinterface_address_config_dict_buffer["ip"]["value"] = element_text
                                                                    interface_subinterface_address_config_dict_buffer["ip"]["observedAt"] = observed_at
                                                                prefixLength = config.get("prefix-length")
                                                                if prefixLength is not None:
                                                                    element_text = prefixLength
                                                                    interface_subinterface_address_config_dict_buffer["prefixLength"] = {}
                                                                    interface_subinterface_address_config_dict_buffer["prefixLength"]["type"] = "Property"
                                                                    interface_subinterface_address_config_dict_buffer["prefixLength"]["value"] = int(element_text)
                                                                    interface_subinterface_address_config_dict_buffer["prefixLength"]["observedAt"] = observed_at
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
                                                                interface_subinterface_address_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                ip = state.get("ip")
                                                                if ip is not None:
                                                                    element_text = ip
                                                                    interface_subinterface_address_state_dict_buffer["ip"] = {}
                                                                    interface_subinterface_address_state_dict_buffer["ip"]["type"] = "Property"
                                                                    interface_subinterface_address_state_dict_buffer["ip"]["value"] = element_text
                                                                    interface_subinterface_address_state_dict_buffer["ip"]["observedAt"] = observed_at
                                                                prefixLength = state.get("prefix-length")
                                                                if prefixLength is not None:
                                                                    element_text = prefixLength
                                                                    interface_subinterface_address_state_dict_buffer["prefixLength"] = {}
                                                                    interface_subinterface_address_state_dict_buffer["prefixLength"]["type"] = "Property"
                                                                    interface_subinterface_address_state_dict_buffer["prefixLength"]["value"] = int(element_text)
                                                                    interface_subinterface_address_state_dict_buffer["prefixLength"]["observedAt"] = observed_at
                                                                origin = state.get("origin")
                                                                if origin is not None:
                                                                    element_text = origin
                                                                    interface_subinterface_address_state_dict_buffer["origin"] = {}
                                                                    interface_subinterface_address_state_dict_buffer["origin"]["type"] = "Property"
                                                                    interface_subinterface_address_state_dict_buffer["origin"]["value"] = element_text
                                                                    interface_subinterface_address_state_dict_buffer["origin"]["observedAt"] = observed_at
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
                                                                    interface_subinterface_address_vrrp_group_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                    virtualRouterId = vrrp_group.get("virtual-router-id")
                                                                    if virtualRouterId is not None:
                                                                        element_text = virtualRouterId
                                                                        if interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1] != element_text:
                                                                            interface_subinterface_address_vrrp_group_dict_buffer["id"] = interface_subinterface_address_vrrp_group_dict_buffer["id"] + element_text
                                                                        interface_subinterface_address_vrrp_group_dict_buffer["virtualRouterId"] = {}
                                                                        interface_subinterface_address_vrrp_group_dict_buffer["virtualRouterId"]["type"] = "Relationship"
                                                                        interface_subinterface_address_vrrp_group_dict_buffer["virtualRouterId"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupConfig:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                        interface_subinterface_address_vrrp_group_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                                    config = vrrp_group.get("config")
                                                                    if isinstance(config, dict):
                                                                        if config is not None and len(config) != 0:
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer = {}
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupConfig:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupConfig"
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"] = {}
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_vrrp_group_dict_buffer["id"]
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                            virtualRouterId = config.get("virtual-router-id")
                                                                            if virtualRouterId is not None:
                                                                                element_text = virtualRouterId
                                                                                if interface_subinterface_address_vrrp_group_config_dict_buffer["id"].split(":")[-1] != int(element_text):
                                                                                    interface_subinterface_address_vrrp_group_config_dict_buffer["id"] = interface_subinterface_address_vrrp_group_config_dict_buffer["id"] + int(element_text)
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["virtualRouterId"] = {}
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["value"] = int(element_text)
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                                            virtualAddress = config.get("virtual-address")
                                                                            if virtualAddress is not None:
                                                                                element_text = virtualAddress
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["virtualAddress"] = {}
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["virtualAddress"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["virtualAddress"]["value"] = element_text
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["virtualAddress"]["observedAt"] = observed_at
                                                                            priority = config.get("priority")
                                                                            if priority is not None:
                                                                                element_text = priority
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["priority"] = {}
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["priority"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["priority"]["value"] = int(element_text)
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["priority"]["observedAt"] = observed_at
                                                                            preempt = config.get("preempt")
                                                                            if preempt is not None:
                                                                                element_text = preempt
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["preempt"] = {}
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["preempt"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["preempt"]["value"] = eval(str(element_text).capitalize())
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["preempt"]["observedAt"] = observed_at
                                                                            preemptDelay = config.get("preempt-delay")
                                                                            if preemptDelay is not None:
                                                                                element_text = preemptDelay
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["preemptDelay"] = {}
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["preemptDelay"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["preemptDelay"]["value"] = int(element_text)
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["preemptDelay"]["observedAt"] = observed_at
                                                                            acceptMode = config.get("accept-mode")
                                                                            if acceptMode is not None:
                                                                                element_text = acceptMode
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["acceptMode"] = {}
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["acceptMode"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["acceptMode"]["value"] = eval(str(element_text).capitalize())
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["acceptMode"]["observedAt"] = observed_at
                                                                            advertisementInterval = config.get("advertisement-interval")
                                                                            if advertisementInterval is not None:
                                                                                element_text = advertisementInterval
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["advertisementInterval"] = {}
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["value"] = int(element_text)
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["observedAt"] = observed_at
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
                                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                            virtualRouterId = state.get("virtual-router-id")
                                                                            if virtualRouterId is not None:
                                                                                element_text = virtualRouterId
                                                                                if interface_subinterface_address_vrrp_group_state_dict_buffer["id"].split(":")[-1] != int(element_text):
                                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["id"] = interface_subinterface_address_vrrp_group_state_dict_buffer["id"] + int(element_text)
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["virtualRouterId"] = {}
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["value"] = int(element_text)
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                                            virtualAddress = state.get("virtual-address")
                                                                            if virtualAddress is not None:
                                                                                element_text = virtualAddress
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["virtualAddress"] = {}
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["virtualAddress"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["virtualAddress"]["value"] = element_text
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["virtualAddress"]["observedAt"] = observed_at
                                                                            priority = state.get("priority")
                                                                            if priority is not None:
                                                                                element_text = priority
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["priority"] = {}
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["priority"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["priority"]["value"] = int(element_text)
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["priority"]["observedAt"] = observed_at
                                                                            preempt = state.get("preempt")
                                                                            if preempt is not None:
                                                                                element_text = preempt
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["preempt"] = {}
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["preempt"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["preempt"]["value"] = eval(str(element_text).capitalize())
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["preempt"]["observedAt"] = observed_at
                                                                            preemptDelay = state.get("preempt-delay")
                                                                            if preemptDelay is not None:
                                                                                element_text = preemptDelay
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["preemptDelay"] = {}
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["preemptDelay"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["preemptDelay"]["value"] = int(element_text)
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["preemptDelay"]["observedAt"] = observed_at
                                                                            acceptMode = state.get("accept-mode")
                                                                            if acceptMode is not None:
                                                                                element_text = acceptMode
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["acceptMode"] = {}
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["acceptMode"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["acceptMode"]["value"] = eval(str(element_text).capitalize())
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["acceptMode"]["observedAt"] = observed_at
                                                                            advertisementInterval = state.get("advertisement-interval")
                                                                            if advertisementInterval is not None:
                                                                                element_text = advertisementInterval
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["advertisementInterval"] = {}
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["value"] = int(element_text)
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["observedAt"] = observed_at
                                                                            currentPriority = state.get("current-priority")
                                                                            if currentPriority is not None:
                                                                                element_text = currentPriority
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["currentPriority"] = {}
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["currentPriority"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["currentPriority"]["value"] = int(element_text)
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["currentPriority"]["observedAt"] = observed_at
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
                                                                                    interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                                    trackInterface = config.get("track-interface")
                                                                                    if trackInterface is not None:
                                                                                        element_text = trackInterface
                                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["trackInterface"] = {}
                                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["trackInterface"]["type"] = "Relationship"
                                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["trackInterface"]["object"] = "urn:ngsi-ld:Interface:" + interface_subinterface_address_vrrp_group_config_dict_buffer["id"].split(":")[-1]
                                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["trackInterface"]["observedAt"] = observed_at
                                                                                    priorityDecrement = config.get("priority-decrement")
                                                                                    if priorityDecrement is not None:
                                                                                        element_text = priorityDecrement
                                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["priorityDecrement"] = {}
                                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["type"] = "Property"
                                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["value"] = int(element_text)
                                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["observedAt"] = observed_at
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
                                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                                    trackInterface = state.get("track-interface")
                                                                                    if trackInterface is not None:
                                                                                        element_text = trackInterface
                                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["trackInterface"] = {}
                                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["trackInterface"]["type"] = "Relationship"
                                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["trackInterface"]["object"] = "urn:ngsi-ld:Interface:" + interface_subinterface_address_vrrp_group_state_dict_buffer["id"].split(":")[-1]
                                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["trackInterface"]["observedAt"] = observed_at
                                                                                    priorityDecrement = state.get("priority-decrement")
                                                                                    if priorityDecrement is not None:
                                                                                        element_text = priorityDecrement
                                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["priorityDecrement"] = {}
                                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["type"] = "Property"
                                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["value"] = int(element_text)
                                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["observedAt"] = observed_at
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
                                                            interface_subinterface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            mode = config.get("mode")
                                                            if mode is not None:
                                                                element_text = mode
                                                                interface_subinterface_config_dict_buffer["mode"] = {}
                                                                interface_subinterface_config_dict_buffer["mode"]["type"] = "Property"
                                                                interface_subinterface_config_dict_buffer["mode"]["value"] = element_text
                                                                interface_subinterface_config_dict_buffer["mode"]["observedAt"] = observed_at
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
                                                            interface_subinterface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            mode = state.get("mode")
                                                            if mode is not None:
                                                                element_text = mode
                                                                interface_subinterface_state_dict_buffer["mode"] = {}
                                                                interface_subinterface_state_dict_buffer["mode"]["type"] = "Property"
                                                                interface_subinterface_state_dict_buffer["mode"]["value"] = element_text
                                                                interface_subinterface_state_dict_buffer["mode"]["observedAt"] = observed_at
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
                                                        interface_subinterface_neighbor_dict_buffer["isPartOf"]["observedAt"] = observed_at
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
                                                            interface_subinterface_neighbor_dict_buffer["ip"]["observedAt"] = observed_at
                                                        config = neighbor.get("config")
                                                        if isinstance(config, dict):
                                                            if config is not None and len(config) != 0:
                                                                interface_subinterface_neighbor_config_dict_buffer = {}
                                                                interface_subinterface_neighbor_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4NeighborsNeighborConfig:" + interface_subinterface_neighbor_dict_buffer["id"].split(":")[-1]
                                                                interface_subinterface_neighbor_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4NeighborsNeighborConfig"
                                                                interface_subinterface_neighbor_config_dict_buffer["isPartOf"] = {}
                                                                interface_subinterface_neighbor_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                interface_subinterface_neighbor_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_neighbor_dict_buffer["id"]
                                                                interface_subinterface_neighbor_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                ip = config.get("ip")
                                                                if ip is not None:
                                                                    element_text = ip
                                                                    interface_subinterface_neighbor_config_dict_buffer["ip"] = {}
                                                                    interface_subinterface_neighbor_config_dict_buffer["ip"]["type"] = "Property"
                                                                    interface_subinterface_neighbor_config_dict_buffer["ip"]["value"] = element_text
                                                                    interface_subinterface_neighbor_config_dict_buffer["ip"]["observedAt"] = observed_at
                                                                linkLayerAddress = config.get("link-layer-address")
                                                                if linkLayerAddress is not None:
                                                                    element_text = linkLayerAddress
                                                                    interface_subinterface_neighbor_config_dict_buffer["linkLayerAddress"] = {}
                                                                    interface_subinterface_neighbor_config_dict_buffer["linkLayerAddress"]["type"] = "Property"
                                                                    interface_subinterface_neighbor_config_dict_buffer["linkLayerAddress"]["value"] = element_text
                                                                    interface_subinterface_neighbor_config_dict_buffer["linkLayerAddress"]["observedAt"] = observed_at
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
                                                                interface_subinterface_neighbor_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                ip = state.get("ip")
                                                                if ip is not None:
                                                                    element_text = ip
                                                                    interface_subinterface_neighbor_state_dict_buffer["ip"] = {}
                                                                    interface_subinterface_neighbor_state_dict_buffer["ip"]["type"] = "Property"
                                                                    interface_subinterface_neighbor_state_dict_buffer["ip"]["value"] = element_text
                                                                    interface_subinterface_neighbor_state_dict_buffer["ip"]["observedAt"] = observed_at
                                                                linkLayerAddress = state.get("link-layer-address")
                                                                if linkLayerAddress is not None:
                                                                    element_text = linkLayerAddress
                                                                    interface_subinterface_neighbor_state_dict_buffer["linkLayerAddress"] = {}
                                                                    interface_subinterface_neighbor_state_dict_buffer["linkLayerAddress"]["type"] = "Property"
                                                                    interface_subinterface_neighbor_state_dict_buffer["linkLayerAddress"]["value"] = element_text
                                                                    interface_subinterface_neighbor_state_dict_buffer["linkLayerAddress"]["observedAt"] = observed_at
                                                                origin = state.get("origin")
                                                                if origin is not None:
                                                                    element_text = origin
                                                                    interface_subinterface_neighbor_state_dict_buffer["origin"] = {}
                                                                    interface_subinterface_neighbor_state_dict_buffer["origin"]["type"] = "Property"
                                                                    interface_subinterface_neighbor_state_dict_buffer["origin"]["value"] = element_text
                                                                    interface_subinterface_neighbor_state_dict_buffer["origin"]["observedAt"] = observed_at
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
                                                            interface_subinterface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            enabled = config.get("enabled")
                                                            if enabled is not None:
                                                                element_text = enabled
                                                                interface_subinterface_config_dict_buffer["enabled"] = {}
                                                                interface_subinterface_config_dict_buffer["enabled"]["type"] = "Property"
                                                                interface_subinterface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                                interface_subinterface_config_dict_buffer["enabled"]["observedAt"] = observed_at
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
                                                            interface_subinterface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            enabled = state.get("enabled")
                                                            if enabled is not None:
                                                                element_text = enabled
                                                                interface_subinterface_state_dict_buffer["enabled"] = {}
                                                                interface_subinterface_state_dict_buffer["enabled"]["type"] = "Property"
                                                                interface_subinterface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                                interface_subinterface_state_dict_buffer["enabled"]["observedAt"] = observed_at
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
                                                                    interface_subinterface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                    interface = config.get("interface")
                                                                    if interface is not None:
                                                                        element_text = interface
                                                                        if interface_subinterface_config_dict_buffer["id"].split(":")[-1] != element_text:
                                                                            interface_subinterface_config_dict_buffer["id"] = interface_subinterface_config_dict_buffer["id"] + element_text
                                                                        interface_subinterface_config_dict_buffer["interface"] = {}
                                                                        interface_subinterface_config_dict_buffer["interface"]["type"] = "Relationship"
                                                                        interface_subinterface_config_dict_buffer["interface"]["object"] = "urn:ngsi-ld:Interface:" + interface_subinterface_config_dict_buffer["id"].split(":")[-1]
                                                                        interface_subinterface_config_dict_buffer["interface"]["observedAt"] = observed_at
                                                                    subinterface = config.get("subinterface")
                                                                    if subinterface is not None:
                                                                        element_text = subinterface
                                                                        if "." + str(element_text) not in interface_subinterface_config_dict_buffer["id"].split(":")[-1]:
                                                                            interface_subinterface_config_dict_buffer["id"] = interface_subinterface_config_dict_buffer["id"] + "." + str(element_text)
                                                                        interface_subinterface_config_dict_buffer["subinterface"] = {}
                                                                        interface_subinterface_config_dict_buffer["subinterface"]["type"] = "Relationship"
                                                                        interface_subinterface_config_dict_buffer["subinterface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterface:" + interface_subinterface_config_dict_buffer["id"].split(":")[-1]
                                                                        interface_subinterface_config_dict_buffer["subinterface"]["observedAt"] = observed_at
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
                                                                    interface_subinterface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                    interface = state.get("interface")
                                                                    if interface is not None:
                                                                        element_text = interface
                                                                        if interface_subinterface_state_dict_buffer["id"].split(":")[-1] != element_text:
                                                                            interface_subinterface_state_dict_buffer["id"] = interface_subinterface_state_dict_buffer["id"] + element_text
                                                                        interface_subinterface_state_dict_buffer["interface"] = {}
                                                                        interface_subinterface_state_dict_buffer["interface"]["type"] = "Relationship"
                                                                        interface_subinterface_state_dict_buffer["interface"]["object"] = "urn:ngsi-ld:Interface:" + interface_subinterface_state_dict_buffer["id"].split(":")[-1]
                                                                        interface_subinterface_state_dict_buffer["interface"]["observedAt"] = observed_at
                                                                    subinterface = state.get("subinterface")
                                                                    if subinterface is not None:
                                                                        element_text = subinterface
                                                                        if "." + str(element_text) not in interface_subinterface_state_dict_buffer["id"].split(":")[-1]:
                                                                            interface_subinterface_state_dict_buffer["id"] = interface_subinterface_state_dict_buffer["id"] + "." + str(element_text)
                                                                        interface_subinterface_state_dict_buffer["subinterface"] = {}
                                                                        interface_subinterface_state_dict_buffer["subinterface"]["type"] = "Relationship"
                                                                        interface_subinterface_state_dict_buffer["subinterface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterface:" + interface_subinterface_state_dict_buffer["id"].split(":")[-1]
                                                                        interface_subinterface_state_dict_buffer["subinterface"]["observedAt"] = observed_at
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
                                                    interface_subinterface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    enabled = config.get("enabled")
                                                    if enabled is not None:
                                                        element_text = enabled
                                                        interface_subinterface_config_dict_buffer["enabled"] = {}
                                                        interface_subinterface_config_dict_buffer["enabled"]["type"] = "Property"
                                                        interface_subinterface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                        interface_subinterface_config_dict_buffer["enabled"]["observedAt"] = observed_at
                                                    mtu = config.get("mtu")
                                                    if mtu is not None:
                                                        element_text = mtu
                                                        interface_subinterface_config_dict_buffer["mtu"] = {}
                                                        interface_subinterface_config_dict_buffer["mtu"]["type"] = "Property"
                                                        interface_subinterface_config_dict_buffer["mtu"]["value"] = int(element_text)
                                                        interface_subinterface_config_dict_buffer["mtu"]["observedAt"] = observed_at
                                                    dhcpClient = config.get("dhcp-client")
                                                    if dhcpClient is not None:
                                                        element_text = dhcpClient
                                                        interface_subinterface_config_dict_buffer["dhcpClient"] = {}
                                                        interface_subinterface_config_dict_buffer["dhcpClient"]["type"] = "Property"
                                                        interface_subinterface_config_dict_buffer["dhcpClient"]["value"] = eval(str(element_text).capitalize())
                                                        interface_subinterface_config_dict_buffer["dhcpClient"]["observedAt"] = observed_at
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
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    enabled = state.get("enabled")
                                                    if enabled is not None:
                                                        element_text = enabled
                                                        interface_subinterface_state_dict_buffer["enabled"] = {}
                                                        interface_subinterface_state_dict_buffer["enabled"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                        interface_subinterface_state_dict_buffer["enabled"]["observedAt"] = observed_at
                                                    mtu = state.get("mtu")
                                                    if mtu is not None:
                                                        element_text = mtu
                                                        interface_subinterface_state_dict_buffer["mtu"] = {}
                                                        interface_subinterface_state_dict_buffer["mtu"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["mtu"]["value"] = int(element_text)
                                                        interface_subinterface_state_dict_buffer["mtu"]["observedAt"] = observed_at
                                                    dhcpClient = state.get("dhcp-client")
                                                    if dhcpClient is not None:
                                                        element_text = dhcpClient
                                                        interface_subinterface_state_dict_buffer["dhcpClient"] = {}
                                                        interface_subinterface_state_dict_buffer["dhcpClient"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["dhcpClient"]["value"] = eval(str(element_text).capitalize())
                                                        interface_subinterface_state_dict_buffer["dhcpClient"]["observedAt"] = observed_at
                                                    counters = state.get("counters")
                                                    if isinstance(counters, dict):
                                                        if counters is not None and len(counters) != 0:
                                                            interface_subinterface_state_counters_dict_buffer = {}
                                                            interface_subinterface_state_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv4StateCounters:" + interface_subinterface_state_dict_buffer["id"].split(":")[-1]
                                                            interface_subinterface_state_counters_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv4StateCounters"
                                                            interface_subinterface_state_counters_dict_buffer["isPartOf"] = {}
                                                            interface_subinterface_state_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_subinterface_state_counters_dict_buffer["isPartOf"]["object"] = interface_subinterface_state_dict_buffer["id"]
                                                            interface_subinterface_state_counters_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            inPkts = counters.get("in-pkts")
                                                            if inPkts is not None:
                                                                element_text = inPkts
                                                                interface_subinterface_state_counters_dict_buffer["inPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inPkts"]["observedAt"] = observed_at
                                                            inOctets = counters.get("in-octets")
                                                            if inOctets is not None:
                                                                element_text = inOctets
                                                                interface_subinterface_state_counters_dict_buffer["inOctets"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inOctets"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inOctets"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inOctets"]["observedAt"] = observed_at
                                                            inErrorPkts = counters.get("in-error-pkts")
                                                            if inErrorPkts is not None:
                                                                element_text = inErrorPkts
                                                                interface_subinterface_state_counters_dict_buffer["inErrorPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inErrorPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inErrorPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inErrorPkts"]["observedAt"] = observed_at
                                                            inForwardedPkts = counters.get("in-forwarded-pkts")
                                                            if inForwardedPkts is not None:
                                                                element_text = inForwardedPkts
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedPkts"]["observedAt"] = observed_at
                                                            inForwardedOctets = counters.get("in-forwarded-octets")
                                                            if inForwardedOctets is not None:
                                                                element_text = inForwardedOctets
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedOctets"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedOctets"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedOctets"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedOctets"]["observedAt"] = observed_at
                                                            inDiscardedPkts = counters.get("in-discarded-pkts")
                                                            if inDiscardedPkts is not None:
                                                                element_text = inDiscardedPkts
                                                                interface_subinterface_state_counters_dict_buffer["inDiscardedPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inDiscardedPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inDiscardedPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inDiscardedPkts"]["observedAt"] = observed_at
                                                            outPkts = counters.get("out-pkts")
                                                            if outPkts is not None:
                                                                element_text = outPkts
                                                                interface_subinterface_state_counters_dict_buffer["outPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outPkts"]["observedAt"] = observed_at
                                                            outOctets = counters.get("out-octets")
                                                            if outOctets is not None:
                                                                element_text = outOctets
                                                                interface_subinterface_state_counters_dict_buffer["outOctets"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outOctets"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outOctets"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outOctets"]["observedAt"] = observed_at
                                                            outErrorPkts = counters.get("out-error-pkts")
                                                            if outErrorPkts is not None:
                                                                element_text = outErrorPkts
                                                                interface_subinterface_state_counters_dict_buffer["outErrorPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outErrorPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outErrorPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outErrorPkts"]["observedAt"] = observed_at
                                                            outForwardedPkts = counters.get("out-forwarded-pkts")
                                                            if outForwardedPkts is not None:
                                                                element_text = outForwardedPkts
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedPkts"]["observedAt"] = observed_at
                                                            outForwardedOctets = counters.get("out-forwarded-octets")
                                                            if outForwardedOctets is not None:
                                                                element_text = outForwardedOctets
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedOctets"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedOctets"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedOctets"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedOctets"]["observedAt"] = observed_at
                                                            outDiscardedPkts = counters.get("out-discarded-pkts")
                                                            if outDiscardedPkts is not None:
                                                                element_text = outDiscardedPkts
                                                                interface_subinterface_state_counters_dict_buffer["outDiscardedPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outDiscardedPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outDiscardedPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outDiscardedPkts"]["observedAt"] = observed_at
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
                                                        interface_subinterface_address_dict_buffer["isPartOf"]["observedAt"] = observed_at
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
                                                            interface_subinterface_address_dict_buffer["ip"]["observedAt"] = observed_at
                                                        config = address.get("config")
                                                        if isinstance(config, dict):
                                                            if config is not None and len(config) != 0:
                                                                interface_subinterface_address_config_dict_buffer = {}
                                                                interface_subinterface_address_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressConfig:" + interface_subinterface_address_dict_buffer["id"].split(":")[-1]
                                                                interface_subinterface_address_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressConfig"
                                                                interface_subinterface_address_config_dict_buffer["isPartOf"] = {}
                                                                interface_subinterface_address_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                interface_subinterface_address_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_dict_buffer["id"]
                                                                interface_subinterface_address_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                ip = config.get("ip")
                                                                if ip is not None:
                                                                    element_text = ip
                                                                    interface_subinterface_address_config_dict_buffer["ip"] = {}
                                                                    interface_subinterface_address_config_dict_buffer["ip"]["type"] = "Property"
                                                                    interface_subinterface_address_config_dict_buffer["ip"]["value"] = element_text
                                                                    interface_subinterface_address_config_dict_buffer["ip"]["observedAt"] = observed_at
                                                                prefixLength = config.get("prefix-length")
                                                                if prefixLength is not None:
                                                                    element_text = prefixLength
                                                                    interface_subinterface_address_config_dict_buffer["prefixLength"] = {}
                                                                    interface_subinterface_address_config_dict_buffer["prefixLength"]["type"] = "Property"
                                                                    interface_subinterface_address_config_dict_buffer["prefixLength"]["value"] = int(element_text)
                                                                    interface_subinterface_address_config_dict_buffer["prefixLength"]["observedAt"] = observed_at
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
                                                                interface_subinterface_address_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                ip = state.get("ip")
                                                                if ip is not None:
                                                                    element_text = ip
                                                                    interface_subinterface_address_state_dict_buffer["ip"] = {}
                                                                    interface_subinterface_address_state_dict_buffer["ip"]["type"] = "Property"
                                                                    interface_subinterface_address_state_dict_buffer["ip"]["value"] = element_text
                                                                    interface_subinterface_address_state_dict_buffer["ip"]["observedAt"] = observed_at
                                                                prefixLength = state.get("prefix-length")
                                                                if prefixLength is not None:
                                                                    element_text = prefixLength
                                                                    interface_subinterface_address_state_dict_buffer["prefixLength"] = {}
                                                                    interface_subinterface_address_state_dict_buffer["prefixLength"]["type"] = "Property"
                                                                    interface_subinterface_address_state_dict_buffer["prefixLength"]["value"] = int(element_text)
                                                                    interface_subinterface_address_state_dict_buffer["prefixLength"]["observedAt"] = observed_at
                                                                origin = state.get("origin")
                                                                if origin is not None:
                                                                    element_text = origin
                                                                    interface_subinterface_address_state_dict_buffer["origin"] = {}
                                                                    interface_subinterface_address_state_dict_buffer["origin"]["type"] = "Property"
                                                                    interface_subinterface_address_state_dict_buffer["origin"]["value"] = element_text
                                                                    interface_subinterface_address_state_dict_buffer["origin"]["observedAt"] = observed_at
                                                                status = state.get("status")
                                                                if status is not None:
                                                                    element_text = status
                                                                    interface_subinterface_address_state_dict_buffer["status"] = {}
                                                                    interface_subinterface_address_state_dict_buffer["status"]["type"] = "Property"
                                                                    interface_subinterface_address_state_dict_buffer["status"]["value"] = element_text
                                                                    interface_subinterface_address_state_dict_buffer["status"]["observedAt"] = observed_at
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
                                                                    interface_subinterface_address_vrrp_group_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                    virtualRouterId = vrrp_group.get("virtual-router-id")
                                                                    if virtualRouterId is not None:
                                                                        element_text = virtualRouterId
                                                                        if interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1] != element_text:
                                                                            interface_subinterface_address_vrrp_group_dict_buffer["id"] = interface_subinterface_address_vrrp_group_dict_buffer["id"] + element_text
                                                                        interface_subinterface_address_vrrp_group_dict_buffer["virtualRouterId"] = {}
                                                                        interface_subinterface_address_vrrp_group_dict_buffer["virtualRouterId"]["type"] = "Relationship"
                                                                        interface_subinterface_address_vrrp_group_dict_buffer["virtualRouterId"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfig:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                        interface_subinterface_address_vrrp_group_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                                    config = vrrp_group.get("config")
                                                                    if isinstance(config, dict):
                                                                        if config is not None and len(config) != 0:
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer = {}
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfig:" + interface_subinterface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfig"
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"] = {}
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_address_vrrp_group_dict_buffer["id"]
                                                                            interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                            virtualRouterId = config.get("virtual-router-id")
                                                                            if virtualRouterId is not None:
                                                                                element_text = virtualRouterId
                                                                                if interface_subinterface_address_vrrp_group_config_dict_buffer["id"].split(":")[-1] != int(element_text):
                                                                                    interface_subinterface_address_vrrp_group_config_dict_buffer["id"] = interface_subinterface_address_vrrp_group_config_dict_buffer["id"] + int(element_text)
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["virtualRouterId"] = {}
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["value"] = int(element_text)
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                                            virtualAddress = config.get("virtual-address")
                                                                            if virtualAddress is not None:
                                                                                element_text = virtualAddress
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["virtualAddress"] = {}
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["virtualAddress"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["virtualAddress"]["value"] = element_text
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["virtualAddress"]["observedAt"] = observed_at
                                                                            priority = config.get("priority")
                                                                            if priority is not None:
                                                                                element_text = priority
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["priority"] = {}
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["priority"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["priority"]["value"] = int(element_text)
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["priority"]["observedAt"] = observed_at
                                                                            preempt = config.get("preempt")
                                                                            if preempt is not None:
                                                                                element_text = preempt
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["preempt"] = {}
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["preempt"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["preempt"]["value"] = eval(str(element_text).capitalize())
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["preempt"]["observedAt"] = observed_at
                                                                            preemptDelay = config.get("preempt-delay")
                                                                            if preemptDelay is not None:
                                                                                element_text = preemptDelay
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["preemptDelay"] = {}
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["preemptDelay"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["preemptDelay"]["value"] = int(element_text)
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["preemptDelay"]["observedAt"] = observed_at
                                                                            acceptMode = config.get("accept-mode")
                                                                            if acceptMode is not None:
                                                                                element_text = acceptMode
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["acceptMode"] = {}
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["acceptMode"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["acceptMode"]["value"] = eval(str(element_text).capitalize())
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["acceptMode"]["observedAt"] = observed_at
                                                                            advertisementInterval = config.get("advertisement-interval")
                                                                            if advertisementInterval is not None:
                                                                                element_text = advertisementInterval
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["advertisementInterval"] = {}
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["value"] = int(element_text)
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["observedAt"] = observed_at
                                                                            virtualLinkLocal = config.get("virtual-link-local")
                                                                            if virtualLinkLocal is not None:
                                                                                element_text = virtualLinkLocal
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["virtualLinkLocal"] = {}
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["virtualLinkLocal"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["virtualLinkLocal"]["value"] = element_text
                                                                                interface_subinterface_address_vrrp_group_config_dict_buffer["virtualLinkLocal"]["observedAt"] = observed_at
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
                                                                            interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                            virtualRouterId = state.get("virtual-router-id")
                                                                            if virtualRouterId is not None:
                                                                                element_text = virtualRouterId
                                                                                if interface_subinterface_address_vrrp_group_state_dict_buffer["id"].split(":")[-1] != int(element_text):
                                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["id"] = interface_subinterface_address_vrrp_group_state_dict_buffer["id"] + int(element_text)
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["virtualRouterId"] = {}
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["value"] = int(element_text)
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                                            virtualAddress = state.get("virtual-address")
                                                                            if virtualAddress is not None:
                                                                                element_text = virtualAddress
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["virtualAddress"] = {}
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["virtualAddress"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["virtualAddress"]["value"] = element_text
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["virtualAddress"]["observedAt"] = observed_at
                                                                            priority = state.get("priority")
                                                                            if priority is not None:
                                                                                element_text = priority
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["priority"] = {}
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["priority"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["priority"]["value"] = int(element_text)
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["priority"]["observedAt"] = observed_at
                                                                            preempt = state.get("preempt")
                                                                            if preempt is not None:
                                                                                element_text = preempt
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["preempt"] = {}
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["preempt"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["preempt"]["value"] = eval(str(element_text).capitalize())
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["preempt"]["observedAt"] = observed_at
                                                                            preemptDelay = state.get("preempt-delay")
                                                                            if preemptDelay is not None:
                                                                                element_text = preemptDelay
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["preemptDelay"] = {}
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["preemptDelay"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["preemptDelay"]["value"] = int(element_text)
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["preemptDelay"]["observedAt"] = observed_at
                                                                            acceptMode = state.get("accept-mode")
                                                                            if acceptMode is not None:
                                                                                element_text = acceptMode
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["acceptMode"] = {}
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["acceptMode"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["acceptMode"]["value"] = eval(str(element_text).capitalize())
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["acceptMode"]["observedAt"] = observed_at
                                                                            advertisementInterval = state.get("advertisement-interval")
                                                                            if advertisementInterval is not None:
                                                                                element_text = advertisementInterval
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["advertisementInterval"] = {}
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["value"] = int(element_text)
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["observedAt"] = observed_at
                                                                            currentPriority = state.get("current-priority")
                                                                            if currentPriority is not None:
                                                                                element_text = currentPriority
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["currentPriority"] = {}
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["currentPriority"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["currentPriority"]["value"] = int(element_text)
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["currentPriority"]["observedAt"] = observed_at
                                                                            virtualLinkLocal = state.get("virtual-link-local")
                                                                            if virtualLinkLocal is not None:
                                                                                element_text = virtualLinkLocal
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["virtualLinkLocal"] = {}
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["virtualLinkLocal"]["type"] = "Property"
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["virtualLinkLocal"]["value"] = element_text
                                                                                interface_subinterface_address_vrrp_group_state_dict_buffer["virtualLinkLocal"]["observedAt"] = observed_at
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
                                                                                    interface_subinterface_address_vrrp_group_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                                    trackInterface = config.get("track-interface")
                                                                                    if trackInterface is not None:
                                                                                        element_text = trackInterface
                                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["trackInterface"] = {}
                                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["trackInterface"]["type"] = "Relationship"
                                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["trackInterface"]["object"] = "urn:ngsi-ld:Interface:" + interface_subinterface_address_vrrp_group_config_dict_buffer["id"].split(":")[-1]
                                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["trackInterface"]["observedAt"] = observed_at
                                                                                    priorityDecrement = config.get("priority-decrement")
                                                                                    if priorityDecrement is not None:
                                                                                        element_text = priorityDecrement
                                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["priorityDecrement"] = {}
                                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["type"] = "Property"
                                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["value"] = int(element_text)
                                                                                        interface_subinterface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["observedAt"] = observed_at
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
                                                                                    interface_subinterface_address_vrrp_group_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                                    trackInterface = state.get("track-interface")
                                                                                    if trackInterface is not None:
                                                                                        element_text = trackInterface
                                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["trackInterface"] = {}
                                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["trackInterface"]["type"] = "Relationship"
                                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["trackInterface"]["object"] = "urn:ngsi-ld:Interface:" + interface_subinterface_address_vrrp_group_state_dict_buffer["id"].split(":")[-1]
                                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["trackInterface"]["observedAt"] = observed_at
                                                                                    priorityDecrement = state.get("priority-decrement")
                                                                                    if priorityDecrement is not None:
                                                                                        element_text = priorityDecrement
                                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["priorityDecrement"] = {}
                                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["type"] = "Property"
                                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["value"] = int(element_text)
                                                                                        interface_subinterface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["observedAt"] = observed_at
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
                                                            interface_subinterface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            interval = config.get("interval")
                                                            if interval is not None:
                                                                element_text = interval
                                                                interface_subinterface_config_dict_buffer["interval"] = {}
                                                                interface_subinterface_config_dict_buffer["interval"]["type"] = "Property"
                                                                interface_subinterface_config_dict_buffer["interval"]["value"] = int(element_text)
                                                                interface_subinterface_config_dict_buffer["interval"]["observedAt"] = observed_at
                                                            lifetime = config.get("lifetime")
                                                            if lifetime is not None:
                                                                element_text = lifetime
                                                                interface_subinterface_config_dict_buffer["lifetime"] = {}
                                                                interface_subinterface_config_dict_buffer["lifetime"]["type"] = "Property"
                                                                interface_subinterface_config_dict_buffer["lifetime"]["value"] = int(element_text)
                                                                interface_subinterface_config_dict_buffer["lifetime"]["observedAt"] = observed_at
                                                            suppress = config.get("suppress")
                                                            if suppress is not None:
                                                                element_text = suppress
                                                                interface_subinterface_config_dict_buffer["suppress"] = {}
                                                                interface_subinterface_config_dict_buffer["suppress"]["type"] = "Property"
                                                                interface_subinterface_config_dict_buffer["suppress"]["value"] = eval(str(element_text).capitalize())
                                                                interface_subinterface_config_dict_buffer["suppress"]["observedAt"] = observed_at
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
                                                            interface_subinterface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            interval = state.get("interval")
                                                            if interval is not None:
                                                                element_text = interval
                                                                interface_subinterface_state_dict_buffer["interval"] = {}
                                                                interface_subinterface_state_dict_buffer["interval"]["type"] = "Property"
                                                                interface_subinterface_state_dict_buffer["interval"]["value"] = int(element_text)
                                                                interface_subinterface_state_dict_buffer["interval"]["observedAt"] = observed_at
                                                            lifetime = state.get("lifetime")
                                                            if lifetime is not None:
                                                                element_text = lifetime
                                                                interface_subinterface_state_dict_buffer["lifetime"] = {}
                                                                interface_subinterface_state_dict_buffer["lifetime"]["type"] = "Property"
                                                                interface_subinterface_state_dict_buffer["lifetime"]["value"] = int(element_text)
                                                                interface_subinterface_state_dict_buffer["lifetime"]["observedAt"] = observed_at
                                                            suppress = state.get("suppress")
                                                            if suppress is not None:
                                                                element_text = suppress
                                                                interface_subinterface_state_dict_buffer["suppress"] = {}
                                                                interface_subinterface_state_dict_buffer["suppress"]["type"] = "Property"
                                                                interface_subinterface_state_dict_buffer["suppress"]["value"] = eval(str(element_text).capitalize())
                                                                interface_subinterface_state_dict_buffer["suppress"]["observedAt"] = observed_at
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
                                                        interface_subinterface_neighbor_dict_buffer["isPartOf"]["observedAt"] = observed_at
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
                                                            interface_subinterface_neighbor_dict_buffer["ip"]["observedAt"] = observed_at
                                                        config = neighbor.get("config")
                                                        if isinstance(config, dict):
                                                            if config is not None and len(config) != 0:
                                                                interface_subinterface_neighbor_config_dict_buffer = {}
                                                                interface_subinterface_neighbor_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborConfig:" + interface_subinterface_neighbor_dict_buffer["id"].split(":")[-1]
                                                                interface_subinterface_neighbor_config_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6NeighborsNeighborConfig"
                                                                interface_subinterface_neighbor_config_dict_buffer["isPartOf"] = {}
                                                                interface_subinterface_neighbor_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                interface_subinterface_neighbor_config_dict_buffer["isPartOf"]["object"] = interface_subinterface_neighbor_dict_buffer["id"]
                                                                interface_subinterface_neighbor_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                ip = config.get("ip")
                                                                if ip is not None:
                                                                    element_text = ip
                                                                    interface_subinterface_neighbor_config_dict_buffer["ip"] = {}
                                                                    interface_subinterface_neighbor_config_dict_buffer["ip"]["type"] = "Property"
                                                                    interface_subinterface_neighbor_config_dict_buffer["ip"]["value"] = element_text
                                                                    interface_subinterface_neighbor_config_dict_buffer["ip"]["observedAt"] = observed_at
                                                                linkLayerAddress = config.get("link-layer-address")
                                                                if linkLayerAddress is not None:
                                                                    element_text = linkLayerAddress
                                                                    interface_subinterface_neighbor_config_dict_buffer["linkLayerAddress"] = {}
                                                                    interface_subinterface_neighbor_config_dict_buffer["linkLayerAddress"]["type"] = "Property"
                                                                    interface_subinterface_neighbor_config_dict_buffer["linkLayerAddress"]["value"] = element_text
                                                                    interface_subinterface_neighbor_config_dict_buffer["linkLayerAddress"]["observedAt"] = observed_at
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
                                                                interface_subinterface_neighbor_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                ip = state.get("ip")
                                                                if ip is not None:
                                                                    element_text = ip
                                                                    interface_subinterface_neighbor_state_dict_buffer["ip"] = {}
                                                                    interface_subinterface_neighbor_state_dict_buffer["ip"]["type"] = "Property"
                                                                    interface_subinterface_neighbor_state_dict_buffer["ip"]["value"] = element_text
                                                                    interface_subinterface_neighbor_state_dict_buffer["ip"]["observedAt"] = observed_at
                                                                linkLayerAddress = state.get("link-layer-address")
                                                                if linkLayerAddress is not None:
                                                                    element_text = linkLayerAddress
                                                                    interface_subinterface_neighbor_state_dict_buffer["linkLayerAddress"] = {}
                                                                    interface_subinterface_neighbor_state_dict_buffer["linkLayerAddress"]["type"] = "Property"
                                                                    interface_subinterface_neighbor_state_dict_buffer["linkLayerAddress"]["value"] = element_text
                                                                    interface_subinterface_neighbor_state_dict_buffer["linkLayerAddress"]["observedAt"] = observed_at
                                                                origin = state.get("origin")
                                                                if origin is not None:
                                                                    element_text = origin
                                                                    interface_subinterface_neighbor_state_dict_buffer["origin"] = {}
                                                                    interface_subinterface_neighbor_state_dict_buffer["origin"]["type"] = "Property"
                                                                    interface_subinterface_neighbor_state_dict_buffer["origin"]["value"] = element_text
                                                                    interface_subinterface_neighbor_state_dict_buffer["origin"]["observedAt"] = observed_at
                                                                isRouter = state.get("is-router")
                                                                if isRouter is not None:
                                                                    element_text = isRouter
                                                                    interface_subinterface_neighbor_state_dict_buffer["isRouter"] = {}
                                                                    interface_subinterface_neighbor_state_dict_buffer["isRouter"]["type"] = "Property"
                                                                    interface_subinterface_neighbor_state_dict_buffer["isRouter"]["value"] = element_text
                                                                    interface_subinterface_neighbor_state_dict_buffer["isRouter"]["observedAt"] = observed_at
                                                                neighborState = state.get("neighbor-state")
                                                                if neighborState is not None:
                                                                    element_text = neighborState
                                                                    interface_subinterface_neighbor_state_dict_buffer["neighborState"] = {}
                                                                    interface_subinterface_neighbor_state_dict_buffer["neighborState"]["type"] = "Property"
                                                                    interface_subinterface_neighbor_state_dict_buffer["neighborState"]["value"] = element_text
                                                                    interface_subinterface_neighbor_state_dict_buffer["neighborState"]["observedAt"] = observed_at
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
                                                            interface_subinterface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            enabled = config.get("enabled")
                                                            if enabled is not None:
                                                                element_text = enabled
                                                                interface_subinterface_config_dict_buffer["enabled"] = {}
                                                                interface_subinterface_config_dict_buffer["enabled"]["type"] = "Property"
                                                                interface_subinterface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                                interface_subinterface_config_dict_buffer["enabled"]["observedAt"] = observed_at
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
                                                            interface_subinterface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            enabled = state.get("enabled")
                                                            if enabled is not None:
                                                                element_text = enabled
                                                                interface_subinterface_state_dict_buffer["enabled"] = {}
                                                                interface_subinterface_state_dict_buffer["enabled"]["type"] = "Property"
                                                                interface_subinterface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                                interface_subinterface_state_dict_buffer["enabled"]["observedAt"] = observed_at
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
                                                                    interface_subinterface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                    interface = config.get("interface")
                                                                    if interface is not None:
                                                                        element_text = interface
                                                                        if interface_subinterface_config_dict_buffer["id"].split(":")[-1] != element_text:
                                                                            interface_subinterface_config_dict_buffer["id"] = interface_subinterface_config_dict_buffer["id"] + element_text
                                                                        interface_subinterface_config_dict_buffer["interface"] = {}
                                                                        interface_subinterface_config_dict_buffer["interface"]["type"] = "Relationship"
                                                                        interface_subinterface_config_dict_buffer["interface"]["object"] = "urn:ngsi-ld:Interface:" + interface_subinterface_config_dict_buffer["id"].split(":")[-1]
                                                                        interface_subinterface_config_dict_buffer["interface"]["observedAt"] = observed_at
                                                                    subinterface = config.get("subinterface")
                                                                    if subinterface is not None:
                                                                        element_text = subinterface
                                                                        if "." + str(element_text) not in interface_subinterface_config_dict_buffer["id"].split(":")[-1]:
                                                                            interface_subinterface_config_dict_buffer["id"] = interface_subinterface_config_dict_buffer["id"] + "." + str(element_text)
                                                                        interface_subinterface_config_dict_buffer["subinterface"] = {}
                                                                        interface_subinterface_config_dict_buffer["subinterface"]["type"] = "Relationship"
                                                                        interface_subinterface_config_dict_buffer["subinterface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterface:" + interface_subinterface_config_dict_buffer["id"].split(":")[-1]
                                                                        interface_subinterface_config_dict_buffer["subinterface"]["observedAt"] = observed_at
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
                                                                    interface_subinterface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                    interface = state.get("interface")
                                                                    if interface is not None:
                                                                        element_text = interface
                                                                        if interface_subinterface_state_dict_buffer["id"].split(":")[-1] != element_text:
                                                                            interface_subinterface_state_dict_buffer["id"] = interface_subinterface_state_dict_buffer["id"] + element_text
                                                                        interface_subinterface_state_dict_buffer["interface"] = {}
                                                                        interface_subinterface_state_dict_buffer["interface"]["type"] = "Relationship"
                                                                        interface_subinterface_state_dict_buffer["interface"]["object"] = "urn:ngsi-ld:Interface:" + interface_subinterface_state_dict_buffer["id"].split(":")[-1]
                                                                        interface_subinterface_state_dict_buffer["interface"]["observedAt"] = observed_at
                                                                    subinterface = state.get("subinterface")
                                                                    if subinterface is not None:
                                                                        element_text = subinterface
                                                                        if "." + str(element_text) not in interface_subinterface_state_dict_buffer["id"].split(":")[-1]:
                                                                            interface_subinterface_state_dict_buffer["id"] = interface_subinterface_state_dict_buffer["id"] + "." + str(element_text)
                                                                        interface_subinterface_state_dict_buffer["subinterface"] = {}
                                                                        interface_subinterface_state_dict_buffer["subinterface"]["type"] = "Relationship"
                                                                        interface_subinterface_state_dict_buffer["subinterface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterface:" + interface_subinterface_state_dict_buffer["id"].split(":")[-1]
                                                                        interface_subinterface_state_dict_buffer["subinterface"]["observedAt"] = observed_at
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
                                                    interface_subinterface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    enabled = config.get("enabled")
                                                    if enabled is not None:
                                                        element_text = enabled
                                                        interface_subinterface_config_dict_buffer["enabled"] = {}
                                                        interface_subinterface_config_dict_buffer["enabled"]["type"] = "Property"
                                                        interface_subinterface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                        interface_subinterface_config_dict_buffer["enabled"]["observedAt"] = observed_at
                                                    mtu = config.get("mtu")
                                                    if mtu is not None:
                                                        element_text = mtu
                                                        interface_subinterface_config_dict_buffer["mtu"] = {}
                                                        interface_subinterface_config_dict_buffer["mtu"]["type"] = "Property"
                                                        interface_subinterface_config_dict_buffer["mtu"]["value"] = int(element_text)
                                                        interface_subinterface_config_dict_buffer["mtu"]["observedAt"] = observed_at
                                                    dupAddrDetectTransmits = config.get("dup-addr-detect-transmits")
                                                    if dupAddrDetectTransmits is not None:
                                                        element_text = dupAddrDetectTransmits
                                                        interface_subinterface_config_dict_buffer["dupAddrDetectTransmits"] = {}
                                                        interface_subinterface_config_dict_buffer["dupAddrDetectTransmits"]["type"] = "Property"
                                                        interface_subinterface_config_dict_buffer["dupAddrDetectTransmits"]["value"] = int(element_text)
                                                        interface_subinterface_config_dict_buffer["dupAddrDetectTransmits"]["observedAt"] = observed_at
                                                    dhcpClient = config.get("dhcp-client")
                                                    if dhcpClient is not None:
                                                        element_text = dhcpClient
                                                        interface_subinterface_config_dict_buffer["dhcpClient"] = {}
                                                        interface_subinterface_config_dict_buffer["dhcpClient"]["type"] = "Property"
                                                        interface_subinterface_config_dict_buffer["dhcpClient"]["value"] = eval(str(element_text).capitalize())
                                                        interface_subinterface_config_dict_buffer["dhcpClient"]["observedAt"] = observed_at
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
                                                    interface_subinterface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    enabled = state.get("enabled")
                                                    if enabled is not None:
                                                        element_text = enabled
                                                        interface_subinterface_state_dict_buffer["enabled"] = {}
                                                        interface_subinterface_state_dict_buffer["enabled"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                        interface_subinterface_state_dict_buffer["enabled"]["observedAt"] = observed_at
                                                    mtu = state.get("mtu")
                                                    if mtu is not None:
                                                        element_text = mtu
                                                        interface_subinterface_state_dict_buffer["mtu"] = {}
                                                        interface_subinterface_state_dict_buffer["mtu"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["mtu"]["value"] = int(element_text)
                                                        interface_subinterface_state_dict_buffer["mtu"]["observedAt"] = observed_at
                                                    dupAddrDetectTransmits = state.get("dup-addr-detect-transmits")
                                                    if dupAddrDetectTransmits is not None:
                                                        element_text = dupAddrDetectTransmits
                                                        interface_subinterface_state_dict_buffer["dupAddrDetectTransmits"] = {}
                                                        interface_subinterface_state_dict_buffer["dupAddrDetectTransmits"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["dupAddrDetectTransmits"]["value"] = int(element_text)
                                                        interface_subinterface_state_dict_buffer["dupAddrDetectTransmits"]["observedAt"] = observed_at
                                                    dhcpClient = state.get("dhcp-client")
                                                    if dhcpClient is not None:
                                                        element_text = dhcpClient
                                                        interface_subinterface_state_dict_buffer["dhcpClient"] = {}
                                                        interface_subinterface_state_dict_buffer["dhcpClient"]["type"] = "Property"
                                                        interface_subinterface_state_dict_buffer["dhcpClient"]["value"] = eval(str(element_text).capitalize())
                                                        interface_subinterface_state_dict_buffer["dhcpClient"]["observedAt"] = observed_at
                                                    counters = state.get("counters")
                                                    if isinstance(counters, dict):
                                                        if counters is not None and len(counters) != 0:
                                                            interface_subinterface_state_counters_dict_buffer = {}
                                                            interface_subinterface_state_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterfaceIpv6StateCounters:" + interface_subinterface_state_dict_buffer["id"].split(":")[-1]
                                                            interface_subinterface_state_counters_dict_buffer["type"] = "InterfaceSubinterfacesSubinterfaceIpv6StateCounters"
                                                            interface_subinterface_state_counters_dict_buffer["isPartOf"] = {}
                                                            interface_subinterface_state_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_subinterface_state_counters_dict_buffer["isPartOf"]["object"] = interface_subinterface_state_dict_buffer["id"]
                                                            interface_subinterface_state_counters_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            inPkts = counters.get("in-pkts")
                                                            if inPkts is not None:
                                                                element_text = inPkts
                                                                interface_subinterface_state_counters_dict_buffer["inPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inPkts"]["observedAt"] = observed_at
                                                            inOctets = counters.get("in-octets")
                                                            if inOctets is not None:
                                                                element_text = inOctets
                                                                interface_subinterface_state_counters_dict_buffer["inOctets"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inOctets"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inOctets"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inOctets"]["observedAt"] = observed_at
                                                            inErrorPkts = counters.get("in-error-pkts")
                                                            if inErrorPkts is not None:
                                                                element_text = inErrorPkts
                                                                interface_subinterface_state_counters_dict_buffer["inErrorPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inErrorPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inErrorPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inErrorPkts"]["observedAt"] = observed_at
                                                            inForwardedPkts = counters.get("in-forwarded-pkts")
                                                            if inForwardedPkts is not None:
                                                                element_text = inForwardedPkts
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedPkts"]["observedAt"] = observed_at
                                                            inForwardedOctets = counters.get("in-forwarded-octets")
                                                            if inForwardedOctets is not None:
                                                                element_text = inForwardedOctets
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedOctets"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedOctets"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedOctets"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inForwardedOctets"]["observedAt"] = observed_at
                                                            inDiscardedPkts = counters.get("in-discarded-pkts")
                                                            if inDiscardedPkts is not None:
                                                                element_text = inDiscardedPkts
                                                                interface_subinterface_state_counters_dict_buffer["inDiscardedPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["inDiscardedPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["inDiscardedPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["inDiscardedPkts"]["observedAt"] = observed_at
                                                            outPkts = counters.get("out-pkts")
                                                            if outPkts is not None:
                                                                element_text = outPkts
                                                                interface_subinterface_state_counters_dict_buffer["outPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outPkts"]["observedAt"] = observed_at
                                                            outOctets = counters.get("out-octets")
                                                            if outOctets is not None:
                                                                element_text = outOctets
                                                                interface_subinterface_state_counters_dict_buffer["outOctets"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outOctets"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outOctets"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outOctets"]["observedAt"] = observed_at
                                                            outErrorPkts = counters.get("out-error-pkts")
                                                            if outErrorPkts is not None:
                                                                element_text = outErrorPkts
                                                                interface_subinterface_state_counters_dict_buffer["outErrorPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outErrorPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outErrorPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outErrorPkts"]["observedAt"] = observed_at
                                                            outForwardedPkts = counters.get("out-forwarded-pkts")
                                                            if outForwardedPkts is not None:
                                                                element_text = outForwardedPkts
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedPkts"]["observedAt"] = observed_at
                                                            outForwardedOctets = counters.get("out-forwarded-octets")
                                                            if outForwardedOctets is not None:
                                                                element_text = outForwardedOctets
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedOctets"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedOctets"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedOctets"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outForwardedOctets"]["observedAt"] = observed_at
                                                            outDiscardedPkts = counters.get("out-discarded-pkts")
                                                            if outDiscardedPkts is not None:
                                                                element_text = outDiscardedPkts
                                                                interface_subinterface_state_counters_dict_buffer["outDiscardedPkts"] = {}
                                                                interface_subinterface_state_counters_dict_buffer["outDiscardedPkts"]["type"] = "Property"
                                                                interface_subinterface_state_counters_dict_buffer["outDiscardedPkts"]["value"] = int(element_text)
                                                                interface_subinterface_state_counters_dict_buffer["outDiscardedPkts"]["observedAt"] = observed_at
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
                                        interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                        macAddress = config.get("mac-address")
                                        if macAddress is not None:
                                            element_text = macAddress
                                            interface_config_dict_buffer["macAddress"] = {}
                                            interface_config_dict_buffer["macAddress"]["type"] = "Property"
                                            interface_config_dict_buffer["macAddress"]["value"] = element_text
                                            interface_config_dict_buffer["macAddress"]["observedAt"] = observed_at
                                        autoNegotiate = config.get("auto-negotiate")
                                        if autoNegotiate is not None:
                                            element_text = autoNegotiate
                                            interface_config_dict_buffer["autoNegotiate"] = {}
                                            interface_config_dict_buffer["autoNegotiate"]["type"] = "Property"
                                            interface_config_dict_buffer["autoNegotiate"]["value"] = eval(str(element_text).capitalize())
                                            interface_config_dict_buffer["autoNegotiate"]["observedAt"] = observed_at
                                        duplexMode = config.get("duplex-mode")
                                        if duplexMode is not None:
                                            element_text = duplexMode
                                            interface_config_dict_buffer["duplexMode"] = {}
                                            interface_config_dict_buffer["duplexMode"]["type"] = "Property"
                                            interface_config_dict_buffer["duplexMode"]["value"] = element_text
                                            interface_config_dict_buffer["duplexMode"]["observedAt"] = observed_at
                                        portSpeed = config.get("port-speed")
                                        if portSpeed is not None and len(portSpeed) != 0:
                                            element_text = portSpeed
                                            if element_text is not None:
                                                interface_config_dict_buffer["portSpeed"] = {}
                                                interface_config_dict_buffer["portSpeed"]["type"] = "Relationship"
                                                interface_config_dict_buffer["portSpeed"]["object"] = "urn:ngsi-ld:YANGIdentity:" + element_text
                                                interface_config_dict_buffer["portSpeed"]["observedAt"] = observed_at
                                        enableFlowControl = config.get("enable-flow-control")
                                        if enableFlowControl is not None:
                                            element_text = enableFlowControl
                                            interface_config_dict_buffer["enableFlowControl"] = {}
                                            interface_config_dict_buffer["enableFlowControl"]["type"] = "Property"
                                            interface_config_dict_buffer["enableFlowControl"]["value"] = eval(str(element_text).capitalize())
                                            interface_config_dict_buffer["enableFlowControl"]["observedAt"] = observed_at
                                        aggregateId = config.get("aggregate-id")
                                        if aggregateId is not None:
                                            element_text = aggregateId
                                            if interface_config_dict_buffer["id"].split(":")[-1] != element_text:
                                                interface_config_dict_buffer["id"] = interface_config_dict_buffer["id"] + element_text
                                            interface_config_dict_buffer["aggregateId"] = {}
                                            interface_config_dict_buffer["aggregateId"]["type"] = "Relationship"
                                            interface_config_dict_buffer["aggregateId"]["object"] = "urn:ngsi-ld:Interface:" + interface_config_dict_buffer["id"].split(":")[-1]
                                            interface_config_dict_buffer["aggregateId"]["observedAt"] = observed_at
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
                                        interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                        macAddress = state.get("mac-address")
                                        if macAddress is not None:
                                            element_text = macAddress
                                            interface_state_dict_buffer["macAddress"] = {}
                                            interface_state_dict_buffer["macAddress"]["type"] = "Property"
                                            interface_state_dict_buffer["macAddress"]["value"] = element_text
                                            interface_state_dict_buffer["macAddress"]["observedAt"] = observed_at
                                        autoNegotiate = state.get("auto-negotiate")
                                        if autoNegotiate is not None:
                                            element_text = autoNegotiate
                                            interface_state_dict_buffer["autoNegotiate"] = {}
                                            interface_state_dict_buffer["autoNegotiate"]["type"] = "Property"
                                            interface_state_dict_buffer["autoNegotiate"]["value"] = eval(str(element_text).capitalize())
                                            interface_state_dict_buffer["autoNegotiate"]["observedAt"] = observed_at
                                        duplexMode = state.get("duplex-mode")
                                        if duplexMode is not None:
                                            element_text = duplexMode
                                            interface_state_dict_buffer["duplexMode"] = {}
                                            interface_state_dict_buffer["duplexMode"]["type"] = "Property"
                                            interface_state_dict_buffer["duplexMode"]["value"] = element_text
                                            interface_state_dict_buffer["duplexMode"]["observedAt"] = observed_at
                                        portSpeed = state.get("port-speed")
                                        if portSpeed is not None and len(portSpeed) != 0:
                                            element_text = portSpeed
                                            if element_text is not None:
                                                interface_state_dict_buffer["portSpeed"] = {}
                                                interface_state_dict_buffer["portSpeed"]["type"] = "Relationship"
                                                interface_state_dict_buffer["portSpeed"]["object"] = "urn:ngsi-ld:YANGIdentity:" + element_text
                                                interface_state_dict_buffer["portSpeed"]["observedAt"] = observed_at
                                        enableFlowControl = state.get("enable-flow-control")
                                        if enableFlowControl is not None:
                                            element_text = enableFlowControl
                                            interface_state_dict_buffer["enableFlowControl"] = {}
                                            interface_state_dict_buffer["enableFlowControl"]["type"] = "Property"
                                            interface_state_dict_buffer["enableFlowControl"]["value"] = eval(str(element_text).capitalize())
                                            interface_state_dict_buffer["enableFlowControl"]["observedAt"] = observed_at
                                        hwMacAddress = state.get("hw-mac-address")
                                        if hwMacAddress is not None:
                                            element_text = hwMacAddress
                                            interface_state_dict_buffer["hwMacAddress"] = {}
                                            interface_state_dict_buffer["hwMacAddress"]["type"] = "Property"
                                            interface_state_dict_buffer["hwMacAddress"]["value"] = element_text
                                            interface_state_dict_buffer["hwMacAddress"]["observedAt"] = observed_at
                                        negotiatedDuplexMode = state.get("negotiated-duplex-mode")
                                        if negotiatedDuplexMode is not None:
                                            element_text = negotiatedDuplexMode
                                            interface_state_dict_buffer["negotiatedDuplexMode"] = {}
                                            interface_state_dict_buffer["negotiatedDuplexMode"]["type"] = "Property"
                                            interface_state_dict_buffer["negotiatedDuplexMode"]["value"] = element_text
                                            interface_state_dict_buffer["negotiatedDuplexMode"]["observedAt"] = observed_at
                                        negotiatedPortSpeed = state.get("negotiated-port-speed")
                                        if negotiatedPortSpeed is not None and len(negotiatedPortSpeed) != 0:
                                            element_text = negotiatedPortSpeed
                                            if element_text is not None:
                                                interface_state_dict_buffer["negotiatedPortSpeed"] = {}
                                                interface_state_dict_buffer["negotiatedPortSpeed"]["type"] = "Relationship"
                                                interface_state_dict_buffer["negotiatedPortSpeed"]["object"] = "urn:ngsi-ld:YANGIdentity:" + element_text
                                                interface_state_dict_buffer["negotiatedPortSpeed"]["observedAt"] = observed_at
                                        counters = state.get("counters")
                                        if isinstance(counters, dict):
                                            if counters is not None and len(counters) != 0:
                                                interface_state_counters_dict_buffer = {}
                                                interface_state_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetStateCounters:" + interface_state_dict_buffer["id"].split(":")[-1]
                                                interface_state_counters_dict_buffer["type"] = "InterfaceEthernetStateCounters"
                                                interface_state_counters_dict_buffer["isPartOf"] = {}
                                                interface_state_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_state_counters_dict_buffer["isPartOf"]["object"] = interface_state_dict_buffer["id"]
                                                interface_state_counters_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                inMacControlFrames = counters.get("in-mac-control-frames")
                                                if inMacControlFrames is not None:
                                                    element_text = inMacControlFrames
                                                    interface_state_counters_dict_buffer["inMacControlFrames"] = {}
                                                    interface_state_counters_dict_buffer["inMacControlFrames"]["type"] = "Property"
                                                    interface_state_counters_dict_buffer["inMacControlFrames"]["value"] = int(element_text)
                                                    interface_state_counters_dict_buffer["inMacControlFrames"]["observedAt"] = observed_at
                                                inMacPauseFrames = counters.get("in-mac-pause-frames")
                                                if inMacPauseFrames is not None:
                                                    element_text = inMacPauseFrames
                                                    interface_state_counters_dict_buffer["inMacPauseFrames"] = {}
                                                    interface_state_counters_dict_buffer["inMacPauseFrames"]["type"] = "Property"
                                                    interface_state_counters_dict_buffer["inMacPauseFrames"]["value"] = int(element_text)
                                                    interface_state_counters_dict_buffer["inMacPauseFrames"]["observedAt"] = observed_at
                                                inOversizeFrames = counters.get("in-oversize-frames")
                                                if inOversizeFrames is not None:
                                                    element_text = inOversizeFrames
                                                    interface_state_counters_dict_buffer["inOversizeFrames"] = {}
                                                    interface_state_counters_dict_buffer["inOversizeFrames"]["type"] = "Property"
                                                    interface_state_counters_dict_buffer["inOversizeFrames"]["value"] = int(element_text)
                                                    interface_state_counters_dict_buffer["inOversizeFrames"]["observedAt"] = observed_at
                                                inJabberFrames = counters.get("in-jabber-frames")
                                                if inJabberFrames is not None:
                                                    element_text = inJabberFrames
                                                    interface_state_counters_dict_buffer["inJabberFrames"] = {}
                                                    interface_state_counters_dict_buffer["inJabberFrames"]["type"] = "Property"
                                                    interface_state_counters_dict_buffer["inJabberFrames"]["value"] = int(element_text)
                                                    interface_state_counters_dict_buffer["inJabberFrames"]["observedAt"] = observed_at
                                                inFragmentFrames = counters.get("in-fragment-frames")
                                                if inFragmentFrames is not None:
                                                    element_text = inFragmentFrames
                                                    interface_state_counters_dict_buffer["inFragmentFrames"] = {}
                                                    interface_state_counters_dict_buffer["inFragmentFrames"]["type"] = "Property"
                                                    interface_state_counters_dict_buffer["inFragmentFrames"]["value"] = int(element_text)
                                                    interface_state_counters_dict_buffer["inFragmentFrames"]["observedAt"] = observed_at
                                                in8021qFrames = counters.get("in-8021q-frames")
                                                if in8021qFrames is not None:
                                                    element_text = in8021qFrames
                                                    interface_state_counters_dict_buffer["in8021qFrames"] = {}
                                                    interface_state_counters_dict_buffer["in8021qFrames"]["type"] = "Property"
                                                    interface_state_counters_dict_buffer["in8021qFrames"]["value"] = int(element_text)
                                                    interface_state_counters_dict_buffer["in8021qFrames"]["observedAt"] = observed_at
                                                inCrcErrors = counters.get("in-crc-errors")
                                                if inCrcErrors is not None:
                                                    element_text = inCrcErrors
                                                    interface_state_counters_dict_buffer["inCrcErrors"] = {}
                                                    interface_state_counters_dict_buffer["inCrcErrors"]["type"] = "Property"
                                                    interface_state_counters_dict_buffer["inCrcErrors"]["value"] = int(element_text)
                                                    interface_state_counters_dict_buffer["inCrcErrors"]["observedAt"] = observed_at
                                                outMacControlFrames = counters.get("out-mac-control-frames")
                                                if outMacControlFrames is not None:
                                                    element_text = outMacControlFrames
                                                    interface_state_counters_dict_buffer["outMacControlFrames"] = {}
                                                    interface_state_counters_dict_buffer["outMacControlFrames"]["type"] = "Property"
                                                    interface_state_counters_dict_buffer["outMacControlFrames"]["value"] = int(element_text)
                                                    interface_state_counters_dict_buffer["outMacControlFrames"]["observedAt"] = observed_at
                                                outMacPauseFrames = counters.get("out-mac-pause-frames")
                                                if outMacPauseFrames is not None:
                                                    element_text = outMacPauseFrames
                                                    interface_state_counters_dict_buffer["outMacPauseFrames"] = {}
                                                    interface_state_counters_dict_buffer["outMacPauseFrames"]["type"] = "Property"
                                                    interface_state_counters_dict_buffer["outMacPauseFrames"]["value"] = int(element_text)
                                                    interface_state_counters_dict_buffer["outMacPauseFrames"]["observedAt"] = observed_at
                                                out8021qFrames = counters.get("out-8021q-frames")
                                                if out8021qFrames is not None:
                                                    element_text = out8021qFrames
                                                    interface_state_counters_dict_buffer["out8021qFrames"] = {}
                                                    interface_state_counters_dict_buffer["out8021qFrames"]["type"] = "Property"
                                                    interface_state_counters_dict_buffer["out8021qFrames"]["value"] = int(element_text)
                                                    interface_state_counters_dict_buffer["out8021qFrames"]["observedAt"] = observed_at
                                                dict_buffers.append(interface_state_counters_dict_buffer)
                                        aggregateId = state.get("aggregate-id")
                                        if aggregateId is not None:
                                            element_text = aggregateId
                                            if interface_state_dict_buffer["id"].split(":")[-1] != element_text:
                                                interface_state_dict_buffer["id"] = interface_state_dict_buffer["id"] + element_text
                                            interface_state_dict_buffer["aggregateId"] = {}
                                            interface_state_dict_buffer["aggregateId"]["type"] = "Relationship"
                                            interface_state_dict_buffer["aggregateId"]["object"] = "urn:ngsi-ld:Interface:" + interface_state_dict_buffer["id"].split(":")[-1]
                                            interface_state_dict_buffer["aggregateId"]["observedAt"] = observed_at
                                        dict_buffers.append(interface_state_dict_buffer)
                                switched_vlan = ethernet.get("switched-vlan")
                                if isinstance(switched_vlan, dict):
                                    if switched_vlan is not None and len(switched_vlan) != 0:
                                        config = switched_vlan.get("config")
                                        if isinstance(config, dict):
                                            if config is not None and len(config) != 0:
                                                interface_config_dict_buffer = {}
                                                interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetSwitchedVlanConfig:" + interface_dict_buffer["id"].split(":")[-1]
                                                interface_config_dict_buffer["type"] = "InterfaceEthernetSwitchedVlanConfig"
                                                interface_config_dict_buffer["isPartOf"] = {}
                                                interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                interfaceMode = config.get("interface-mode")
                                                if interfaceMode is not None:
                                                    element_text = interfaceMode
                                                    interface_config_dict_buffer["interfaceMode"] = {}
                                                    interface_config_dict_buffer["interfaceMode"]["type"] = "Property"
                                                    interface_config_dict_buffer["interfaceMode"]["value"] = element_text
                                                    interface_config_dict_buffer["interfaceMode"]["observedAt"] = observed_at
                                                nativeVlan = config.get("native-vlan")
                                                if nativeVlan is not None:
                                                    element_text = nativeVlan
                                                    interface_config_dict_buffer["nativeVlan"] = {}
                                                    interface_config_dict_buffer["nativeVlan"]["type"] = "Property"
                                                    interface_config_dict_buffer["nativeVlan"]["value"] = int(element_text)
                                                    interface_config_dict_buffer["nativeVlan"]["observedAt"] = observed_at
                                                accessVlan = config.get("access-vlan")
                                                if accessVlan is not None:
                                                    element_text = accessVlan
                                                    interface_config_dict_buffer["accessVlan"] = {}
                                                    interface_config_dict_buffer["accessVlan"]["type"] = "Property"
                                                    interface_config_dict_buffer["accessVlan"]["value"] = int(element_text)
                                                    interface_config_dict_buffer["accessVlan"]["observedAt"] = observed_at
                                                trunkVlans = config.get("trunk-vlans")
                                                if trunkVlans is not None:
                                                    element_text = trunkVlans
                                                    interface_config_dict_buffer["trunkVlans"] = {}
                                                    interface_config_dict_buffer["trunkVlans"]["type"] = "Property"
                                                    interface_config_dict_buffer["trunkVlans"]["value"] = element_text
                                                    interface_config_dict_buffer["trunkVlans"]["observedAt"] = observed_at
                                                dict_buffers.append(interface_config_dict_buffer)
                                        state = switched_vlan.get("state")
                                        if isinstance(state, dict):
                                            if state is not None and len(state) != 0:
                                                interface_state_dict_buffer = {}
                                                interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetSwitchedVlanState:" + interface_dict_buffer["id"].split(":")[-1]
                                                interface_state_dict_buffer["type"] = "InterfaceEthernetSwitchedVlanState"
                                                interface_state_dict_buffer["isPartOf"] = {}
                                                interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                interfaceMode = state.get("interface-mode")
                                                if interfaceMode is not None:
                                                    element_text = interfaceMode
                                                    interface_state_dict_buffer["interfaceMode"] = {}
                                                    interface_state_dict_buffer["interfaceMode"]["type"] = "Property"
                                                    interface_state_dict_buffer["interfaceMode"]["value"] = element_text
                                                    interface_state_dict_buffer["interfaceMode"]["observedAt"] = observed_at
                                                nativeVlan = state.get("native-vlan")
                                                if nativeVlan is not None:
                                                    element_text = nativeVlan
                                                    interface_state_dict_buffer["nativeVlan"] = {}
                                                    interface_state_dict_buffer["nativeVlan"]["type"] = "Property"
                                                    interface_state_dict_buffer["nativeVlan"]["value"] = int(element_text)
                                                    interface_state_dict_buffer["nativeVlan"]["observedAt"] = observed_at
                                                accessVlan = state.get("access-vlan")
                                                if accessVlan is not None:
                                                    element_text = accessVlan
                                                    interface_state_dict_buffer["accessVlan"] = {}
                                                    interface_state_dict_buffer["accessVlan"]["type"] = "Property"
                                                    interface_state_dict_buffer["accessVlan"]["value"] = int(element_text)
                                                    interface_state_dict_buffer["accessVlan"]["observedAt"] = observed_at
                                                trunkVlans = state.get("trunk-vlans")
                                                if trunkVlans is not None:
                                                    element_text = trunkVlans
                                                    interface_state_dict_buffer["trunkVlans"] = {}
                                                    interface_state_dict_buffer["trunkVlans"]["type"] = "Property"
                                                    interface_state_dict_buffer["trunkVlans"]["value"] = element_text
                                                    interface_state_dict_buffer["trunkVlans"]["observedAt"] = observed_at
                                                dict_buffers.append(interface_state_dict_buffer)
                        aggregation = interface.get("openconfig-if-aggregate:aggregation")
                        if isinstance(aggregation, dict):
                            if aggregation is not None and len(aggregation) != 0:
                                config = aggregation.get("config")
                                if isinstance(config, dict):
                                    if config is not None and len(config) != 0:
                                        interface_config_dict_buffer = {}
                                        interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceAggregationConfig:" + interface_dict_buffer["id"].split(":")[-1]
                                        interface_config_dict_buffer["type"] = "InterfaceAggregationConfig"
                                        interface_config_dict_buffer["isPartOf"] = {}
                                        interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                        interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                        interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                        lagType = config.get("lag-type")
                                        if lagType is not None:
                                            element_text = lagType
                                            interface_config_dict_buffer["lagType"] = {}
                                            interface_config_dict_buffer["lagType"]["type"] = "Property"
                                            interface_config_dict_buffer["lagType"]["value"] = element_text
                                            interface_config_dict_buffer["lagType"]["observedAt"] = observed_at
                                        minLinks = config.get("min-links")
                                        if minLinks is not None:
                                            element_text = minLinks
                                            interface_config_dict_buffer["minLinks"] = {}
                                            interface_config_dict_buffer["minLinks"]["type"] = "Property"
                                            interface_config_dict_buffer["minLinks"]["value"] = int(element_text)
                                            interface_config_dict_buffer["minLinks"]["observedAt"] = observed_at
                                        dict_buffers.append(interface_config_dict_buffer)
                                state = aggregation.get("state")
                                if isinstance(state, dict):
                                    if state is not None and len(state) != 0:
                                        interface_state_dict_buffer = {}
                                        interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceAggregationState:" + interface_dict_buffer["id"].split(":")[-1]
                                        interface_state_dict_buffer["type"] = "InterfaceAggregationState"
                                        interface_state_dict_buffer["isPartOf"] = {}
                                        interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                        interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                        interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                        lagType = state.get("lag-type")
                                        if lagType is not None:
                                            element_text = lagType
                                            interface_state_dict_buffer["lagType"] = {}
                                            interface_state_dict_buffer["lagType"]["type"] = "Property"
                                            interface_state_dict_buffer["lagType"]["value"] = element_text
                                            interface_state_dict_buffer["lagType"]["observedAt"] = observed_at
                                        minLinks = state.get("min-links")
                                        if minLinks is not None:
                                            element_text = minLinks
                                            interface_state_dict_buffer["minLinks"] = {}
                                            interface_state_dict_buffer["minLinks"]["type"] = "Property"
                                            interface_state_dict_buffer["minLinks"]["value"] = int(element_text)
                                            interface_state_dict_buffer["minLinks"]["observedAt"] = observed_at
                                        lagSpeed = state.get("lag-speed")
                                        if lagSpeed is not None:
                                            element_text = lagSpeed
                                            interface_state_dict_buffer["lagSpeed"] = {}
                                            interface_state_dict_buffer["lagSpeed"]["type"] = "Property"
                                            interface_state_dict_buffer["lagSpeed"]["value"] = int(element_text)
                                            interface_state_dict_buffer["lagSpeed"]["observedAt"] = observed_at
                                        member = state.get("member")
                                        if member is not None:
                                            element_text = member
                                            interface_state_dict_buffer["member"] = {}
                                            interface_state_dict_buffer["member"]["type"] = "Relationship"
                                            interface_state_dict_buffer["member"]["object"] = "urn:ngsi-ld:Interface:" + interface_state_dict_buffer["id"].split(":")[-1]
                                            interface_state_dict_buffer["member"]["observedAt"] = observed_at
                                        dict_buffers.append(interface_state_dict_buffer)
                                switched_vlan = aggregation.get("switched-vlan")
                                if isinstance(switched_vlan, dict):
                                    if switched_vlan is not None and len(switched_vlan) != 0:
                                        config = switched_vlan.get("config")
                                        if isinstance(config, dict):
                                            if config is not None and len(config) != 0:
                                                interface_config_dict_buffer = {}
                                                interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceAggregationSwitchedVlanConfig:" + interface_dict_buffer["id"].split(":")[-1]
                                                interface_config_dict_buffer["type"] = "InterfaceAggregationSwitchedVlanConfig"
                                                interface_config_dict_buffer["isPartOf"] = {}
                                                interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                interfaceMode = config.get("interface-mode")
                                                if interfaceMode is not None:
                                                    element_text = interfaceMode
                                                    interface_config_dict_buffer["interfaceMode"] = {}
                                                    interface_config_dict_buffer["interfaceMode"]["type"] = "Property"
                                                    interface_config_dict_buffer["interfaceMode"]["value"] = element_text
                                                    interface_config_dict_buffer["interfaceMode"]["observedAt"] = observed_at
                                                nativeVlan = config.get("native-vlan")
                                                if nativeVlan is not None:
                                                    element_text = nativeVlan
                                                    interface_config_dict_buffer["nativeVlan"] = {}
                                                    interface_config_dict_buffer["nativeVlan"]["type"] = "Property"
                                                    interface_config_dict_buffer["nativeVlan"]["value"] = int(element_text)
                                                    interface_config_dict_buffer["nativeVlan"]["observedAt"] = observed_at
                                                accessVlan = config.get("access-vlan")
                                                if accessVlan is not None:
                                                    element_text = accessVlan
                                                    interface_config_dict_buffer["accessVlan"] = {}
                                                    interface_config_dict_buffer["accessVlan"]["type"] = "Property"
                                                    interface_config_dict_buffer["accessVlan"]["value"] = int(element_text)
                                                    interface_config_dict_buffer["accessVlan"]["observedAt"] = observed_at
                                                trunkVlans = config.get("trunk-vlans")
                                                if trunkVlans is not None:
                                                    element_text = trunkVlans
                                                    interface_config_dict_buffer["trunkVlans"] = {}
                                                    interface_config_dict_buffer["trunkVlans"]["type"] = "Property"
                                                    interface_config_dict_buffer["trunkVlans"]["value"] = element_text
                                                    interface_config_dict_buffer["trunkVlans"]["observedAt"] = observed_at
                                                dict_buffers.append(interface_config_dict_buffer)
                                        state = switched_vlan.get("state")
                                        if isinstance(state, dict):
                                            if state is not None and len(state) != 0:
                                                interface_state_dict_buffer = {}
                                                interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceAggregationSwitchedVlanState:" + interface_dict_buffer["id"].split(":")[-1]
                                                interface_state_dict_buffer["type"] = "InterfaceAggregationSwitchedVlanState"
                                                interface_state_dict_buffer["isPartOf"] = {}
                                                interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                interfaceMode = state.get("interface-mode")
                                                if interfaceMode is not None:
                                                    element_text = interfaceMode
                                                    interface_state_dict_buffer["interfaceMode"] = {}
                                                    interface_state_dict_buffer["interfaceMode"]["type"] = "Property"
                                                    interface_state_dict_buffer["interfaceMode"]["value"] = element_text
                                                    interface_state_dict_buffer["interfaceMode"]["observedAt"] = observed_at
                                                nativeVlan = state.get("native-vlan")
                                                if nativeVlan is not None:
                                                    element_text = nativeVlan
                                                    interface_state_dict_buffer["nativeVlan"] = {}
                                                    interface_state_dict_buffer["nativeVlan"]["type"] = "Property"
                                                    interface_state_dict_buffer["nativeVlan"]["value"] = int(element_text)
                                                    interface_state_dict_buffer["nativeVlan"]["observedAt"] = observed_at
                                                accessVlan = state.get("access-vlan")
                                                if accessVlan is not None:
                                                    element_text = accessVlan
                                                    interface_state_dict_buffer["accessVlan"] = {}
                                                    interface_state_dict_buffer["accessVlan"]["type"] = "Property"
                                                    interface_state_dict_buffer["accessVlan"]["value"] = int(element_text)
                                                    interface_state_dict_buffer["accessVlan"]["observedAt"] = observed_at
                                                trunkVlans = state.get("trunk-vlans")
                                                if trunkVlans is not None:
                                                    element_text = trunkVlans
                                                    interface_state_dict_buffer["trunkVlans"] = {}
                                                    interface_state_dict_buffer["trunkVlans"]["type"] = "Property"
                                                    interface_state_dict_buffer["trunkVlans"]["value"] = element_text
                                                    interface_state_dict_buffer["trunkVlans"]["observedAt"] = observed_at
                                                dict_buffers.append(interface_state_dict_buffer)
                        routed_vlan = interface.get("openconfig-vlan:routed-vlan")
                        if isinstance(routed_vlan, dict):
                            if routed_vlan is not None and len(routed_vlan) != 0:
                                config = routed_vlan.get("config")
                                if isinstance(config, dict):
                                    if config is not None and len(config) != 0:
                                        interface_config_dict_buffer = {}
                                        interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanConfig:" + interface_dict_buffer["id"].split(":")[-1]
                                        interface_config_dict_buffer["type"] = "InterfaceRoutedVlanConfig"
                                        interface_config_dict_buffer["isPartOf"] = {}
                                        interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                        interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                        interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                        vlan = config.get("vlan")
                                        if vlan is not None:
                                            element_text = vlan
                                            interface_config_dict_buffer["vlan"] = {}
                                            interface_config_dict_buffer["vlan"]["type"] = "Property"
                                            interface_config_dict_buffer["vlan"]["value"] = element_text
                                            interface_config_dict_buffer["vlan"]["observedAt"] = observed_at
                                        dict_buffers.append(interface_config_dict_buffer)
                                state = routed_vlan.get("state")
                                if isinstance(state, dict):
                                    if state is not None and len(state) != 0:
                                        interface_state_dict_buffer = {}
                                        interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanState:" + interface_dict_buffer["id"].split(":")[-1]
                                        interface_state_dict_buffer["type"] = "InterfaceRoutedVlanState"
                                        interface_state_dict_buffer["isPartOf"] = {}
                                        interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                        interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                        interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                        vlan = state.get("vlan")
                                        if vlan is not None:
                                            element_text = vlan
                                            interface_state_dict_buffer["vlan"] = {}
                                            interface_state_dict_buffer["vlan"]["type"] = "Property"
                                            interface_state_dict_buffer["vlan"]["value"] = element_text
                                            interface_state_dict_buffer["vlan"]["observedAt"] = observed_at
                                        dict_buffers.append(interface_state_dict_buffer)
                                ipv4 = routed_vlan.get("ipv4")
                                if isinstance(ipv4, dict):
                                    if ipv4 is not None and len(ipv4) != 0:
                                        addresses = ipv4.get("addresses")
                                        if isinstance(addresses, dict):
                                            if addresses is not None and len(addresses) != 0:
                                                addresses_address = addresses.get("address")
                                                for address in addresses_address:
                                                    interface_address_dict_buffer = {}
                                                    interface_address_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4AddressesAddress:" + interface_dict_buffer["id"].split(":")[-1]
                                                    interface_address_dict_buffer["type"] = "InterfaceRoutedVlanIpv4AddressesAddress"
                                                    interface_address_dict_buffer["isPartOf"] = {}
                                                    interface_address_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_address_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                    interface_address_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    ip = address.get("ip")
                                                    if ip is not None:
                                                        element_text = ip
                                                        if ":" in element_text:
                                                            element_text = element_text.replace(":",".")
                                                        if interface_address_dict_buffer["id"].split(":")[-1] != element_text:
                                                            interface_address_dict_buffer["id"] = interface_address_dict_buffer["id"] + ":" + element_text
                                                        interface_address_dict_buffer["ip"] = {}
                                                        interface_address_dict_buffer["ip"]["type"] = "Relationship"
                                                        interface_address_dict_buffer["ip"]["object"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4AddressesAddressConfig:" + interface_address_dict_buffer["id"].split(":")[-1]
                                                        interface_address_dict_buffer["ip"]["observedAt"] = observed_at
                                                    config = address.get("config")
                                                    if isinstance(config, dict):
                                                        if config is not None and len(config) != 0:
                                                            interface_address_config_dict_buffer = {}
                                                            interface_address_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4AddressesAddressConfig:" + interface_address_dict_buffer["id"].split(":")[-1]
                                                            interface_address_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv4AddressesAddressConfig"
                                                            interface_address_config_dict_buffer["isPartOf"] = {}
                                                            interface_address_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_address_config_dict_buffer["isPartOf"]["object"] = interface_address_dict_buffer["id"]
                                                            interface_address_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            ip = config.get("ip")
                                                            if ip is not None:
                                                                element_text = ip
                                                                interface_address_config_dict_buffer["ip"] = {}
                                                                interface_address_config_dict_buffer["ip"]["type"] = "Property"
                                                                interface_address_config_dict_buffer["ip"]["value"] = element_text
                                                                interface_address_config_dict_buffer["ip"]["observedAt"] = observed_at
                                                            prefixLength = config.get("prefix-length")
                                                            if prefixLength is not None:
                                                                element_text = prefixLength
                                                                interface_address_config_dict_buffer["prefixLength"] = {}
                                                                interface_address_config_dict_buffer["prefixLength"]["type"] = "Property"
                                                                interface_address_config_dict_buffer["prefixLength"]["value"] = int(element_text)
                                                                interface_address_config_dict_buffer["prefixLength"]["observedAt"] = observed_at
                                                            dict_buffers.append(interface_address_config_dict_buffer)
                                                    state = address.get("state")
                                                    if isinstance(state, dict):
                                                        if state is not None and len(state) != 0:
                                                            interface_address_state_dict_buffer = {}
                                                            interface_address_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4AddressesAddressState:" + interface_address_dict_buffer["id"].split(":")[-1]
                                                            interface_address_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv4AddressesAddressState"
                                                            interface_address_state_dict_buffer["isPartOf"] = {}
                                                            interface_address_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_address_state_dict_buffer["isPartOf"]["object"] = interface_address_dict_buffer["id"]
                                                            interface_address_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            ip = state.get("ip")
                                                            if ip is not None:
                                                                element_text = ip
                                                                interface_address_state_dict_buffer["ip"] = {}
                                                                interface_address_state_dict_buffer["ip"]["type"] = "Property"
                                                                interface_address_state_dict_buffer["ip"]["value"] = element_text
                                                                interface_address_state_dict_buffer["ip"]["observedAt"] = observed_at
                                                            prefixLength = state.get("prefix-length")
                                                            if prefixLength is not None:
                                                                element_text = prefixLength
                                                                interface_address_state_dict_buffer["prefixLength"] = {}
                                                                interface_address_state_dict_buffer["prefixLength"]["type"] = "Property"
                                                                interface_address_state_dict_buffer["prefixLength"]["value"] = int(element_text)
                                                                interface_address_state_dict_buffer["prefixLength"]["observedAt"] = observed_at
                                                            origin = state.get("origin")
                                                            if origin is not None:
                                                                element_text = origin
                                                                interface_address_state_dict_buffer["origin"] = {}
                                                                interface_address_state_dict_buffer["origin"]["type"] = "Property"
                                                                interface_address_state_dict_buffer["origin"]["value"] = element_text
                                                                interface_address_state_dict_buffer["origin"]["observedAt"] = observed_at
                                                            dict_buffers.append(interface_address_state_dict_buffer)
                                                    vrrp = address.get("vrrp")
                                                    if isinstance(vrrp, dict):
                                                        if vrrp is not None and len(vrrp) != 0:
                                                            vrrp_vrrp_group = vrrp.get("vrrp-group")
                                                            for vrrp_group in vrrp_vrrp_group:
                                                                interface_address_vrrp_group_dict_buffer = {}
                                                                interface_address_vrrp_group_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroup:" + interface_address_dict_buffer["id"].split(":")[-1]
                                                                interface_address_vrrp_group_dict_buffer["type"] = "InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroup"
                                                                interface_address_vrrp_group_dict_buffer["isPartOf"] = {}
                                                                interface_address_vrrp_group_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                interface_address_vrrp_group_dict_buffer["isPartOf"]["object"] = interface_address_dict_buffer["id"]
                                                                interface_address_vrrp_group_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                virtualRouterId = vrrp_group.get("virtual-router-id")
                                                                if virtualRouterId is not None:
                                                                    element_text = virtualRouterId
                                                                    if interface_address_vrrp_group_dict_buffer["id"].split(":")[-1] != element_text:
                                                                        interface_address_vrrp_group_dict_buffer["id"] = interface_address_vrrp_group_dict_buffer["id"] + element_text
                                                                    interface_address_vrrp_group_dict_buffer["virtualRouterId"] = {}
                                                                    interface_address_vrrp_group_dict_buffer["virtualRouterId"]["type"] = "Relationship"
                                                                    interface_address_vrrp_group_dict_buffer["virtualRouterId"]["object"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupConfig:" + interface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                    interface_address_vrrp_group_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                                config = vrrp_group.get("config")
                                                                if isinstance(config, dict):
                                                                    if config is not None and len(config) != 0:
                                                                        interface_address_vrrp_group_config_dict_buffer = {}
                                                                        interface_address_vrrp_group_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupConfig:" + interface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                        interface_address_vrrp_group_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupConfig"
                                                                        interface_address_vrrp_group_config_dict_buffer["isPartOf"] = {}
                                                                        interface_address_vrrp_group_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                        interface_address_vrrp_group_config_dict_buffer["isPartOf"]["object"] = interface_address_vrrp_group_dict_buffer["id"]
                                                                        interface_address_vrrp_group_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                        virtualRouterId = config.get("virtual-router-id")
                                                                        if virtualRouterId is not None:
                                                                            element_text = virtualRouterId
                                                                            if interface_address_vrrp_group_config_dict_buffer["id"].split(":")[-1] != int(element_text):
                                                                                interface_address_vrrp_group_config_dict_buffer["id"] = interface_address_vrrp_group_config_dict_buffer["id"] + int(element_text)
                                                                            interface_address_vrrp_group_config_dict_buffer["virtualRouterId"] = {}
                                                                            interface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["type"] = "Property"
                                                                            interface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["value"] = int(element_text)
                                                                            interface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                                        virtualAddress = config.get("virtual-address")
                                                                        if virtualAddress is not None:
                                                                            element_text = virtualAddress
                                                                            interface_address_vrrp_group_config_dict_buffer["virtualAddress"] = {}
                                                                            interface_address_vrrp_group_config_dict_buffer["virtualAddress"]["type"] = "Property"
                                                                            interface_address_vrrp_group_config_dict_buffer["virtualAddress"]["value"] = element_text
                                                                            interface_address_vrrp_group_config_dict_buffer["virtualAddress"]["observedAt"] = observed_at
                                                                        priority = config.get("priority")
                                                                        if priority is not None:
                                                                            element_text = priority
                                                                            interface_address_vrrp_group_config_dict_buffer["priority"] = {}
                                                                            interface_address_vrrp_group_config_dict_buffer["priority"]["type"] = "Property"
                                                                            interface_address_vrrp_group_config_dict_buffer["priority"]["value"] = int(element_text)
                                                                            interface_address_vrrp_group_config_dict_buffer["priority"]["observedAt"] = observed_at
                                                                        preempt = config.get("preempt")
                                                                        if preempt is not None:
                                                                            element_text = preempt
                                                                            interface_address_vrrp_group_config_dict_buffer["preempt"] = {}
                                                                            interface_address_vrrp_group_config_dict_buffer["preempt"]["type"] = "Property"
                                                                            interface_address_vrrp_group_config_dict_buffer["preempt"]["value"] = eval(str(element_text).capitalize())
                                                                            interface_address_vrrp_group_config_dict_buffer["preempt"]["observedAt"] = observed_at
                                                                        preemptDelay = config.get("preempt-delay")
                                                                        if preemptDelay is not None:
                                                                            element_text = preemptDelay
                                                                            interface_address_vrrp_group_config_dict_buffer["preemptDelay"] = {}
                                                                            interface_address_vrrp_group_config_dict_buffer["preemptDelay"]["type"] = "Property"
                                                                            interface_address_vrrp_group_config_dict_buffer["preemptDelay"]["value"] = int(element_text)
                                                                            interface_address_vrrp_group_config_dict_buffer["preemptDelay"]["observedAt"] = observed_at
                                                                        acceptMode = config.get("accept-mode")
                                                                        if acceptMode is not None:
                                                                            element_text = acceptMode
                                                                            interface_address_vrrp_group_config_dict_buffer["acceptMode"] = {}
                                                                            interface_address_vrrp_group_config_dict_buffer["acceptMode"]["type"] = "Property"
                                                                            interface_address_vrrp_group_config_dict_buffer["acceptMode"]["value"] = eval(str(element_text).capitalize())
                                                                            interface_address_vrrp_group_config_dict_buffer["acceptMode"]["observedAt"] = observed_at
                                                                        advertisementInterval = config.get("advertisement-interval")
                                                                        if advertisementInterval is not None:
                                                                            element_text = advertisementInterval
                                                                            interface_address_vrrp_group_config_dict_buffer["advertisementInterval"] = {}
                                                                            interface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["type"] = "Property"
                                                                            interface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["value"] = int(element_text)
                                                                            interface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["observedAt"] = observed_at
                                                                        dict_buffers.append(interface_address_vrrp_group_config_dict_buffer)
                                                                state = vrrp_group.get("state")
                                                                if isinstance(state, dict):
                                                                    if state is not None and len(state) != 0:
                                                                        interface_address_vrrp_group_state_dict_buffer = {}
                                                                        interface_address_vrrp_group_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupState:" + interface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                        interface_address_vrrp_group_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupState"
                                                                        interface_address_vrrp_group_state_dict_buffer["isPartOf"] = {}
                                                                        interface_address_vrrp_group_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                        interface_address_vrrp_group_state_dict_buffer["isPartOf"]["object"] = interface_address_vrrp_group_dict_buffer["id"]
                                                                        interface_address_vrrp_group_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                        virtualRouterId = state.get("virtual-router-id")
                                                                        if virtualRouterId is not None:
                                                                            element_text = virtualRouterId
                                                                            if interface_address_vrrp_group_state_dict_buffer["id"].split(":")[-1] != int(element_text):
                                                                                interface_address_vrrp_group_state_dict_buffer["id"] = interface_address_vrrp_group_state_dict_buffer["id"] + int(element_text)
                                                                            interface_address_vrrp_group_state_dict_buffer["virtualRouterId"] = {}
                                                                            interface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["type"] = "Property"
                                                                            interface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["value"] = int(element_text)
                                                                            interface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                                        virtualAddress = state.get("virtual-address")
                                                                        if virtualAddress is not None:
                                                                            element_text = virtualAddress
                                                                            interface_address_vrrp_group_state_dict_buffer["virtualAddress"] = {}
                                                                            interface_address_vrrp_group_state_dict_buffer["virtualAddress"]["type"] = "Property"
                                                                            interface_address_vrrp_group_state_dict_buffer["virtualAddress"]["value"] = element_text
                                                                            interface_address_vrrp_group_state_dict_buffer["virtualAddress"]["observedAt"] = observed_at
                                                                        priority = state.get("priority")
                                                                        if priority is not None:
                                                                            element_text = priority
                                                                            interface_address_vrrp_group_state_dict_buffer["priority"] = {}
                                                                            interface_address_vrrp_group_state_dict_buffer["priority"]["type"] = "Property"
                                                                            interface_address_vrrp_group_state_dict_buffer["priority"]["value"] = int(element_text)
                                                                            interface_address_vrrp_group_state_dict_buffer["priority"]["observedAt"] = observed_at
                                                                        preempt = state.get("preempt")
                                                                        if preempt is not None:
                                                                            element_text = preempt
                                                                            interface_address_vrrp_group_state_dict_buffer["preempt"] = {}
                                                                            interface_address_vrrp_group_state_dict_buffer["preempt"]["type"] = "Property"
                                                                            interface_address_vrrp_group_state_dict_buffer["preempt"]["value"] = eval(str(element_text).capitalize())
                                                                            interface_address_vrrp_group_state_dict_buffer["preempt"]["observedAt"] = observed_at
                                                                        preemptDelay = state.get("preempt-delay")
                                                                        if preemptDelay is not None:
                                                                            element_text = preemptDelay
                                                                            interface_address_vrrp_group_state_dict_buffer["preemptDelay"] = {}
                                                                            interface_address_vrrp_group_state_dict_buffer["preemptDelay"]["type"] = "Property"
                                                                            interface_address_vrrp_group_state_dict_buffer["preemptDelay"]["value"] = int(element_text)
                                                                            interface_address_vrrp_group_state_dict_buffer["preemptDelay"]["observedAt"] = observed_at
                                                                        acceptMode = state.get("accept-mode")
                                                                        if acceptMode is not None:
                                                                            element_text = acceptMode
                                                                            interface_address_vrrp_group_state_dict_buffer["acceptMode"] = {}
                                                                            interface_address_vrrp_group_state_dict_buffer["acceptMode"]["type"] = "Property"
                                                                            interface_address_vrrp_group_state_dict_buffer["acceptMode"]["value"] = eval(str(element_text).capitalize())
                                                                            interface_address_vrrp_group_state_dict_buffer["acceptMode"]["observedAt"] = observed_at
                                                                        advertisementInterval = state.get("advertisement-interval")
                                                                        if advertisementInterval is not None:
                                                                            element_text = advertisementInterval
                                                                            interface_address_vrrp_group_state_dict_buffer["advertisementInterval"] = {}
                                                                            interface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["type"] = "Property"
                                                                            interface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["value"] = int(element_text)
                                                                            interface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["observedAt"] = observed_at
                                                                        currentPriority = state.get("current-priority")
                                                                        if currentPriority is not None:
                                                                            element_text = currentPriority
                                                                            interface_address_vrrp_group_state_dict_buffer["currentPriority"] = {}
                                                                            interface_address_vrrp_group_state_dict_buffer["currentPriority"]["type"] = "Property"
                                                                            interface_address_vrrp_group_state_dict_buffer["currentPriority"]["value"] = int(element_text)
                                                                            interface_address_vrrp_group_state_dict_buffer["currentPriority"]["observedAt"] = observed_at
                                                                        dict_buffers.append(interface_address_vrrp_group_state_dict_buffer)
                                                                interface_tracking = vrrp_group.get("interface-tracking")
                                                                if isinstance(interface_tracking, dict):
                                                                    if interface_tracking is not None and len(interface_tracking) != 0:
                                                                        config = interface_tracking.get("config")
                                                                        if isinstance(config, dict):
                                                                            if config is not None and len(config) != 0:
                                                                                interface_address_vrrp_group_config_dict_buffer = {}
                                                                                interface_address_vrrp_group_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig:" + interface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                                interface_address_vrrp_group_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig"
                                                                                interface_address_vrrp_group_config_dict_buffer["isPartOf"] = {}
                                                                                interface_address_vrrp_group_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                                interface_address_vrrp_group_config_dict_buffer["isPartOf"]["object"] = interface_address_vrrp_group_dict_buffer["id"]
                                                                                interface_address_vrrp_group_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                                trackInterface = config.get("track-interface")
                                                                                if trackInterface is not None:
                                                                                    element_text = trackInterface
                                                                                    interface_address_vrrp_group_config_dict_buffer["trackInterface"] = {}
                                                                                    interface_address_vrrp_group_config_dict_buffer["trackInterface"]["type"] = "Relationship"
                                                                                    interface_address_vrrp_group_config_dict_buffer["trackInterface"]["object"] = "urn:ngsi-ld:Interface:" + interface_address_vrrp_group_config_dict_buffer["id"].split(":")[-1]
                                                                                    interface_address_vrrp_group_config_dict_buffer["trackInterface"]["observedAt"] = observed_at
                                                                                priorityDecrement = config.get("priority-decrement")
                                                                                if priorityDecrement is not None:
                                                                                    element_text = priorityDecrement
                                                                                    interface_address_vrrp_group_config_dict_buffer["priorityDecrement"] = {}
                                                                                    interface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["type"] = "Property"
                                                                                    interface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["value"] = int(element_text)
                                                                                    interface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["observedAt"] = observed_at
                                                                                dict_buffers.append(interface_address_vrrp_group_config_dict_buffer)
                                                                        state = interface_tracking.get("state")
                                                                        if isinstance(state, dict):
                                                                            if state is not None and len(state) != 0:
                                                                                interface_address_vrrp_group_state_dict_buffer = {}
                                                                                interface_address_vrrp_group_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingState:" + interface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                                interface_address_vrrp_group_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingState"
                                                                                interface_address_vrrp_group_state_dict_buffer["isPartOf"] = {}
                                                                                interface_address_vrrp_group_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                                interface_address_vrrp_group_state_dict_buffer["isPartOf"]["object"] = interface_address_vrrp_group_dict_buffer["id"]
                                                                                interface_address_vrrp_group_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                                trackInterface = state.get("track-interface")
                                                                                if trackInterface is not None:
                                                                                    element_text = trackInterface
                                                                                    interface_address_vrrp_group_state_dict_buffer["trackInterface"] = {}
                                                                                    interface_address_vrrp_group_state_dict_buffer["trackInterface"]["type"] = "Relationship"
                                                                                    interface_address_vrrp_group_state_dict_buffer["trackInterface"]["object"] = "urn:ngsi-ld:Interface:" + interface_address_vrrp_group_state_dict_buffer["id"].split(":")[-1]
                                                                                    interface_address_vrrp_group_state_dict_buffer["trackInterface"]["observedAt"] = observed_at
                                                                                priorityDecrement = state.get("priority-decrement")
                                                                                if priorityDecrement is not None:
                                                                                    element_text = priorityDecrement
                                                                                    interface_address_vrrp_group_state_dict_buffer["priorityDecrement"] = {}
                                                                                    interface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["type"] = "Property"
                                                                                    interface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["value"] = int(element_text)
                                                                                    interface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["observedAt"] = observed_at
                                                                                dict_buffers.append(interface_address_vrrp_group_state_dict_buffer)
                                                                dict_buffers.append(interface_address_vrrp_group_dict_buffer)
                                                    dict_buffers.append(interface_address_dict_buffer)
                                        proxy_arp = ipv4.get("proxy-arp")
                                        if isinstance(proxy_arp, dict):
                                            if proxy_arp is not None and len(proxy_arp) != 0:
                                                config = proxy_arp.get("config")
                                                if isinstance(config, dict):
                                                    if config is not None and len(config) != 0:
                                                        interface_config_dict_buffer = {}
                                                        interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4ProxyArpConfig:" + interface_dict_buffer["id"].split(":")[-1]
                                                        interface_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv4ProxyArpConfig"
                                                        interface_config_dict_buffer["isPartOf"] = {}
                                                        interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                        interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                        mode = config.get("mode")
                                                        if mode is not None:
                                                            element_text = mode
                                                            interface_config_dict_buffer["mode"] = {}
                                                            interface_config_dict_buffer["mode"]["type"] = "Property"
                                                            interface_config_dict_buffer["mode"]["value"] = element_text
                                                            interface_config_dict_buffer["mode"]["observedAt"] = observed_at
                                                        dict_buffers.append(interface_config_dict_buffer)
                                                state = proxy_arp.get("state")
                                                if isinstance(state, dict):
                                                    if state is not None and len(state) != 0:
                                                        interface_state_dict_buffer = {}
                                                        interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4ProxyArpState:" + interface_dict_buffer["id"].split(":")[-1]
                                                        interface_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv4ProxyArpState"
                                                        interface_state_dict_buffer["isPartOf"] = {}
                                                        interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                        interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                        mode = state.get("mode")
                                                        if mode is not None:
                                                            element_text = mode
                                                            interface_state_dict_buffer["mode"] = {}
                                                            interface_state_dict_buffer["mode"]["type"] = "Property"
                                                            interface_state_dict_buffer["mode"]["value"] = element_text
                                                            interface_state_dict_buffer["mode"]["observedAt"] = observed_at
                                                        dict_buffers.append(interface_state_dict_buffer)
                                        neighbors = ipv4.get("neighbors")
                                        if isinstance(neighbors, dict):
                                            if neighbors is not None and len(neighbors) != 0:
                                                neighbors_neighbor = neighbors.get("neighbor")
                                                for neighbor in neighbors_neighbor:
                                                    interface_neighbor_dict_buffer = {}
                                                    interface_neighbor_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4NeighborsNeighbor:" + interface_dict_buffer["id"].split(":")[-1]
                                                    interface_neighbor_dict_buffer["type"] = "InterfaceRoutedVlanIpv4NeighborsNeighbor"
                                                    interface_neighbor_dict_buffer["isPartOf"] = {}
                                                    interface_neighbor_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_neighbor_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                    interface_neighbor_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    ip = neighbor.get("ip")
                                                    if ip is not None:
                                                        element_text = ip
                                                        if ":" in element_text:
                                                            element_text = element_text.replace(":",".")
                                                        if interface_neighbor_dict_buffer["id"].split(":")[-1] != element_text:
                                                            interface_neighbor_dict_buffer["id"] = interface_neighbor_dict_buffer["id"] + ":" + element_text
                                                        interface_neighbor_dict_buffer["ip"] = {}
                                                        interface_neighbor_dict_buffer["ip"]["type"] = "Relationship"
                                                        interface_neighbor_dict_buffer["ip"]["object"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4NeighborsNeighborConfig:" + interface_neighbor_dict_buffer["id"].split(":")[-1]
                                                        interface_neighbor_dict_buffer["ip"]["observedAt"] = observed_at
                                                    config = neighbor.get("config")
                                                    if isinstance(config, dict):
                                                        if config is not None and len(config) != 0:
                                                            interface_neighbor_config_dict_buffer = {}
                                                            interface_neighbor_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4NeighborsNeighborConfig:" + interface_neighbor_dict_buffer["id"].split(":")[-1]
                                                            interface_neighbor_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv4NeighborsNeighborConfig"
                                                            interface_neighbor_config_dict_buffer["isPartOf"] = {}
                                                            interface_neighbor_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_neighbor_config_dict_buffer["isPartOf"]["object"] = interface_neighbor_dict_buffer["id"]
                                                            interface_neighbor_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            ip = config.get("ip")
                                                            if ip is not None:
                                                                element_text = ip
                                                                interface_neighbor_config_dict_buffer["ip"] = {}
                                                                interface_neighbor_config_dict_buffer["ip"]["type"] = "Property"
                                                                interface_neighbor_config_dict_buffer["ip"]["value"] = element_text
                                                                interface_neighbor_config_dict_buffer["ip"]["observedAt"] = observed_at
                                                            linkLayerAddress = config.get("link-layer-address")
                                                            if linkLayerAddress is not None:
                                                                element_text = linkLayerAddress
                                                                interface_neighbor_config_dict_buffer["linkLayerAddress"] = {}
                                                                interface_neighbor_config_dict_buffer["linkLayerAddress"]["type"] = "Property"
                                                                interface_neighbor_config_dict_buffer["linkLayerAddress"]["value"] = element_text
                                                                interface_neighbor_config_dict_buffer["linkLayerAddress"]["observedAt"] = observed_at
                                                            dict_buffers.append(interface_neighbor_config_dict_buffer)
                                                    state = neighbor.get("state")
                                                    if isinstance(state, dict):
                                                        if state is not None and len(state) != 0:
                                                            interface_neighbor_state_dict_buffer = {}
                                                            interface_neighbor_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4NeighborsNeighborState:" + interface_neighbor_dict_buffer["id"].split(":")[-1]
                                                            interface_neighbor_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv4NeighborsNeighborState"
                                                            interface_neighbor_state_dict_buffer["isPartOf"] = {}
                                                            interface_neighbor_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_neighbor_state_dict_buffer["isPartOf"]["object"] = interface_neighbor_dict_buffer["id"]
                                                            interface_neighbor_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            ip = state.get("ip")
                                                            if ip is not None:
                                                                element_text = ip
                                                                interface_neighbor_state_dict_buffer["ip"] = {}
                                                                interface_neighbor_state_dict_buffer["ip"]["type"] = "Property"
                                                                interface_neighbor_state_dict_buffer["ip"]["value"] = element_text
                                                                interface_neighbor_state_dict_buffer["ip"]["observedAt"] = observed_at
                                                            linkLayerAddress = state.get("link-layer-address")
                                                            if linkLayerAddress is not None:
                                                                element_text = linkLayerAddress
                                                                interface_neighbor_state_dict_buffer["linkLayerAddress"] = {}
                                                                interface_neighbor_state_dict_buffer["linkLayerAddress"]["type"] = "Property"
                                                                interface_neighbor_state_dict_buffer["linkLayerAddress"]["value"] = element_text
                                                                interface_neighbor_state_dict_buffer["linkLayerAddress"]["observedAt"] = observed_at
                                                            origin = state.get("origin")
                                                            if origin is not None:
                                                                element_text = origin
                                                                interface_neighbor_state_dict_buffer["origin"] = {}
                                                                interface_neighbor_state_dict_buffer["origin"]["type"] = "Property"
                                                                interface_neighbor_state_dict_buffer["origin"]["value"] = element_text
                                                                interface_neighbor_state_dict_buffer["origin"]["observedAt"] = observed_at
                                                            dict_buffers.append(interface_neighbor_state_dict_buffer)
                                                    dict_buffers.append(interface_neighbor_dict_buffer)
                                        unnumbered = ipv4.get("unnumbered")
                                        if isinstance(unnumbered, dict):
                                            if unnumbered is not None and len(unnumbered) != 0:
                                                config = unnumbered.get("config")
                                                if isinstance(config, dict):
                                                    if config is not None and len(config) != 0:
                                                        interface_config_dict_buffer = {}
                                                        interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4UnnumberedConfig:" + interface_dict_buffer["id"].split(":")[-1]
                                                        interface_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv4UnnumberedConfig"
                                                        interface_config_dict_buffer["isPartOf"] = {}
                                                        interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                        interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                        enabled = config.get("enabled")
                                                        if enabled is not None:
                                                            element_text = enabled
                                                            interface_config_dict_buffer["enabled"] = {}
                                                            interface_config_dict_buffer["enabled"]["type"] = "Property"
                                                            interface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                            interface_config_dict_buffer["enabled"]["observedAt"] = observed_at
                                                        dict_buffers.append(interface_config_dict_buffer)
                                                state = unnumbered.get("state")
                                                if isinstance(state, dict):
                                                    if state is not None and len(state) != 0:
                                                        interface_state_dict_buffer = {}
                                                        interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4UnnumberedState:" + interface_dict_buffer["id"].split(":")[-1]
                                                        interface_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv4UnnumberedState"
                                                        interface_state_dict_buffer["isPartOf"] = {}
                                                        interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                        interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                        enabled = state.get("enabled")
                                                        if enabled is not None:
                                                            element_text = enabled
                                                            interface_state_dict_buffer["enabled"] = {}
                                                            interface_state_dict_buffer["enabled"]["type"] = "Property"
                                                            interface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                            interface_state_dict_buffer["enabled"]["observedAt"] = observed_at
                                                        dict_buffers.append(interface_state_dict_buffer)
                                                interface_ref = unnumbered.get("interface-ref")
                                                if isinstance(interface_ref, dict):
                                                    if interface_ref is not None and len(interface_ref) != 0:
                                                        config = interface_ref.get("config")
                                                        if isinstance(config, dict):
                                                            if config is not None and len(config) != 0:
                                                                interface_config_dict_buffer = {}
                                                                interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4UnnumberedInterfaceRefConfig:" + interface_dict_buffer["id"].split(":")[-1]
                                                                interface_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv4UnnumberedInterfaceRefConfig"
                                                                interface_config_dict_buffer["isPartOf"] = {}
                                                                interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                                interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                interface = config.get("interface")
                                                                if interface is not None:
                                                                    element_text = interface
                                                                    if interface_config_dict_buffer["id"].split(":")[-1] != element_text:
                                                                        interface_config_dict_buffer["id"] = interface_config_dict_buffer["id"] + element_text
                                                                    interface_config_dict_buffer["interface"] = {}
                                                                    interface_config_dict_buffer["interface"]["type"] = "Relationship"
                                                                    interface_config_dict_buffer["interface"]["object"] = "urn:ngsi-ld:Interface:" + interface_config_dict_buffer["id"].split(":")[-1]
                                                                    interface_config_dict_buffer["interface"]["observedAt"] = observed_at
                                                                subinterface = config.get("subinterface")
                                                                if subinterface is not None:
                                                                    element_text = subinterface
                                                                    if "." + str(element_text) not in interface_config_dict_buffer["id"].split(":")[-1]:
                                                                        interface_config_dict_buffer["id"] = interface_config_dict_buffer["id"] + "." + str(element_text)
                                                                    interface_config_dict_buffer["subinterface"] = {}
                                                                    interface_config_dict_buffer["subinterface"]["type"] = "Relationship"
                                                                    interface_config_dict_buffer["subinterface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterface:" + interface_config_dict_buffer["id"].split(":")[-1]
                                                                    interface_config_dict_buffer["subinterface"]["observedAt"] = observed_at
                                                                dict_buffers.append(interface_config_dict_buffer)
                                                        state = interface_ref.get("state")
                                                        if isinstance(state, dict):
                                                            if state is not None and len(state) != 0:
                                                                interface_state_dict_buffer = {}
                                                                interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4UnnumberedInterfaceRefState:" + interface_dict_buffer["id"].split(":")[-1]
                                                                interface_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv4UnnumberedInterfaceRefState"
                                                                interface_state_dict_buffer["isPartOf"] = {}
                                                                interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                                interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                interface = state.get("interface")
                                                                if interface is not None:
                                                                    element_text = interface
                                                                    if interface_state_dict_buffer["id"].split(":")[-1] != element_text:
                                                                        interface_state_dict_buffer["id"] = interface_state_dict_buffer["id"] + element_text
                                                                    interface_state_dict_buffer["interface"] = {}
                                                                    interface_state_dict_buffer["interface"]["type"] = "Relationship"
                                                                    interface_state_dict_buffer["interface"]["object"] = "urn:ngsi-ld:Interface:" + interface_state_dict_buffer["id"].split(":")[-1]
                                                                    interface_state_dict_buffer["interface"]["observedAt"] = observed_at
                                                                subinterface = state.get("subinterface")
                                                                if subinterface is not None:
                                                                    element_text = subinterface
                                                                    if "." + str(element_text) not in interface_state_dict_buffer["id"].split(":")[-1]:
                                                                        interface_state_dict_buffer["id"] = interface_state_dict_buffer["id"] + "." + str(element_text)
                                                                    interface_state_dict_buffer["subinterface"] = {}
                                                                    interface_state_dict_buffer["subinterface"]["type"] = "Relationship"
                                                                    interface_state_dict_buffer["subinterface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterface:" + interface_state_dict_buffer["id"].split(":")[-1]
                                                                    interface_state_dict_buffer["subinterface"]["observedAt"] = observed_at
                                                                dict_buffers.append(interface_state_dict_buffer)
                                        config = ipv4.get("config")
                                        if isinstance(config, dict):
                                            if config is not None and len(config) != 0:
                                                interface_config_dict_buffer = {}
                                                interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4Config:" + interface_dict_buffer["id"].split(":")[-1]
                                                interface_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv4Config"
                                                interface_config_dict_buffer["isPartOf"] = {}
                                                interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                enabled = config.get("enabled")
                                                if enabled is not None:
                                                    element_text = enabled
                                                    interface_config_dict_buffer["enabled"] = {}
                                                    interface_config_dict_buffer["enabled"]["type"] = "Property"
                                                    interface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                    interface_config_dict_buffer["enabled"]["observedAt"] = observed_at
                                                mtu = config.get("mtu")
                                                if mtu is not None:
                                                    element_text = mtu
                                                    interface_config_dict_buffer["mtu"] = {}
                                                    interface_config_dict_buffer["mtu"]["type"] = "Property"
                                                    interface_config_dict_buffer["mtu"]["value"] = int(element_text)
                                                    interface_config_dict_buffer["mtu"]["observedAt"] = observed_at
                                                dhcpClient = config.get("dhcp-client")
                                                if dhcpClient is not None:
                                                    element_text = dhcpClient
                                                    interface_config_dict_buffer["dhcpClient"] = {}
                                                    interface_config_dict_buffer["dhcpClient"]["type"] = "Property"
                                                    interface_config_dict_buffer["dhcpClient"]["value"] = eval(str(element_text).capitalize())
                                                    interface_config_dict_buffer["dhcpClient"]["observedAt"] = observed_at
                                                dict_buffers.append(interface_config_dict_buffer)
                                        state = ipv4.get("state")
                                        if isinstance(state, dict):
                                            if state is not None and len(state) != 0:
                                                interface_state_dict_buffer = {}
                                                interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4State:" + interface_dict_buffer["id"].split(":")[-1]
                                                interface_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv4State"
                                                interface_state_dict_buffer["isPartOf"] = {}
                                                interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                enabled = state.get("enabled")
                                                if enabled is not None:
                                                    element_text = enabled
                                                    interface_state_dict_buffer["enabled"] = {}
                                                    interface_state_dict_buffer["enabled"]["type"] = "Property"
                                                    interface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                    interface_state_dict_buffer["enabled"]["observedAt"] = observed_at
                                                mtu = state.get("mtu")
                                                if mtu is not None:
                                                    element_text = mtu
                                                    interface_state_dict_buffer["mtu"] = {}
                                                    interface_state_dict_buffer["mtu"]["type"] = "Property"
                                                    interface_state_dict_buffer["mtu"]["value"] = int(element_text)
                                                    interface_state_dict_buffer["mtu"]["observedAt"] = observed_at
                                                dhcpClient = state.get("dhcp-client")
                                                if dhcpClient is not None:
                                                    element_text = dhcpClient
                                                    interface_state_dict_buffer["dhcpClient"] = {}
                                                    interface_state_dict_buffer["dhcpClient"]["type"] = "Property"
                                                    interface_state_dict_buffer["dhcpClient"]["value"] = eval(str(element_text).capitalize())
                                                    interface_state_dict_buffer["dhcpClient"]["observedAt"] = observed_at
                                                counters = state.get("counters")
                                                if isinstance(counters, dict):
                                                    if counters is not None and len(counters) != 0:
                                                        interface_state_counters_dict_buffer = {}
                                                        interface_state_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv4StateCounters:" + interface_state_dict_buffer["id"].split(":")[-1]
                                                        interface_state_counters_dict_buffer["type"] = "InterfaceRoutedVlanIpv4StateCounters"
                                                        interface_state_counters_dict_buffer["isPartOf"] = {}
                                                        interface_state_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_state_counters_dict_buffer["isPartOf"]["object"] = interface_state_dict_buffer["id"]
                                                        interface_state_counters_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                        inPkts = counters.get("in-pkts")
                                                        if inPkts is not None:
                                                            element_text = inPkts
                                                            interface_state_counters_dict_buffer["inPkts"] = {}
                                                            interface_state_counters_dict_buffer["inPkts"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["inPkts"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["inPkts"]["observedAt"] = observed_at
                                                        inOctets = counters.get("in-octets")
                                                        if inOctets is not None:
                                                            element_text = inOctets
                                                            interface_state_counters_dict_buffer["inOctets"] = {}
                                                            interface_state_counters_dict_buffer["inOctets"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["inOctets"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["inOctets"]["observedAt"] = observed_at
                                                        inErrorPkts = counters.get("in-error-pkts")
                                                        if inErrorPkts is not None:
                                                            element_text = inErrorPkts
                                                            interface_state_counters_dict_buffer["inErrorPkts"] = {}
                                                            interface_state_counters_dict_buffer["inErrorPkts"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["inErrorPkts"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["inErrorPkts"]["observedAt"] = observed_at
                                                        inForwardedPkts = counters.get("in-forwarded-pkts")
                                                        if inForwardedPkts is not None:
                                                            element_text = inForwardedPkts
                                                            interface_state_counters_dict_buffer["inForwardedPkts"] = {}
                                                            interface_state_counters_dict_buffer["inForwardedPkts"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["inForwardedPkts"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["inForwardedPkts"]["observedAt"] = observed_at
                                                        inForwardedOctets = counters.get("in-forwarded-octets")
                                                        if inForwardedOctets is not None:
                                                            element_text = inForwardedOctets
                                                            interface_state_counters_dict_buffer["inForwardedOctets"] = {}
                                                            interface_state_counters_dict_buffer["inForwardedOctets"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["inForwardedOctets"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["inForwardedOctets"]["observedAt"] = observed_at
                                                        inDiscardedPkts = counters.get("in-discarded-pkts")
                                                        if inDiscardedPkts is not None:
                                                            element_text = inDiscardedPkts
                                                            interface_state_counters_dict_buffer["inDiscardedPkts"] = {}
                                                            interface_state_counters_dict_buffer["inDiscardedPkts"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["inDiscardedPkts"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["inDiscardedPkts"]["observedAt"] = observed_at
                                                        outPkts = counters.get("out-pkts")
                                                        if outPkts is not None:
                                                            element_text = outPkts
                                                            interface_state_counters_dict_buffer["outPkts"] = {}
                                                            interface_state_counters_dict_buffer["outPkts"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["outPkts"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["outPkts"]["observedAt"] = observed_at
                                                        outOctets = counters.get("out-octets")
                                                        if outOctets is not None:
                                                            element_text = outOctets
                                                            interface_state_counters_dict_buffer["outOctets"] = {}
                                                            interface_state_counters_dict_buffer["outOctets"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["outOctets"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["outOctets"]["observedAt"] = observed_at
                                                        outErrorPkts = counters.get("out-error-pkts")
                                                        if outErrorPkts is not None:
                                                            element_text = outErrorPkts
                                                            interface_state_counters_dict_buffer["outErrorPkts"] = {}
                                                            interface_state_counters_dict_buffer["outErrorPkts"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["outErrorPkts"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["outErrorPkts"]["observedAt"] = observed_at
                                                        outForwardedPkts = counters.get("out-forwarded-pkts")
                                                        if outForwardedPkts is not None:
                                                            element_text = outForwardedPkts
                                                            interface_state_counters_dict_buffer["outForwardedPkts"] = {}
                                                            interface_state_counters_dict_buffer["outForwardedPkts"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["outForwardedPkts"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["outForwardedPkts"]["observedAt"] = observed_at
                                                        outForwardedOctets = counters.get("out-forwarded-octets")
                                                        if outForwardedOctets is not None:
                                                            element_text = outForwardedOctets
                                                            interface_state_counters_dict_buffer["outForwardedOctets"] = {}
                                                            interface_state_counters_dict_buffer["outForwardedOctets"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["outForwardedOctets"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["outForwardedOctets"]["observedAt"] = observed_at
                                                        outDiscardedPkts = counters.get("out-discarded-pkts")
                                                        if outDiscardedPkts is not None:
                                                            element_text = outDiscardedPkts
                                                            interface_state_counters_dict_buffer["outDiscardedPkts"] = {}
                                                            interface_state_counters_dict_buffer["outDiscardedPkts"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["outDiscardedPkts"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["outDiscardedPkts"]["observedAt"] = observed_at
                                                        dict_buffers.append(interface_state_counters_dict_buffer)
                                                dict_buffers.append(interface_state_dict_buffer)
                                ipv6 = routed_vlan.get("ipv6")
                                if isinstance(ipv6, dict):
                                    if ipv6 is not None and len(ipv6) != 0:
                                        addresses = ipv6.get("addresses")
                                        if isinstance(addresses, dict):
                                            if addresses is not None and len(addresses) != 0:
                                                addresses_address = addresses.get("address")
                                                for address in addresses_address:
                                                    interface_address_dict_buffer = {}
                                                    interface_address_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6AddressesAddress:" + interface_dict_buffer["id"].split(":")[-1]
                                                    interface_address_dict_buffer["type"] = "InterfaceRoutedVlanIpv6AddressesAddress"
                                                    interface_address_dict_buffer["isPartOf"] = {}
                                                    interface_address_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_address_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                    interface_address_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    ip = address.get("ip")
                                                    if ip is not None:
                                                        element_text = ip
                                                        if ":" in element_text:
                                                            element_text = element_text.replace(":",".")
                                                        if interface_address_dict_buffer["id"].split(":")[-1] != element_text:
                                                            interface_address_dict_buffer["id"] = interface_address_dict_buffer["id"] + ":" + element_text
                                                        interface_address_dict_buffer["ip"] = {}
                                                        interface_address_dict_buffer["ip"]["type"] = "Relationship"
                                                        interface_address_dict_buffer["ip"]["object"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6AddressesAddressConfig:" + interface_address_dict_buffer["id"].split(":")[-1]
                                                        interface_address_dict_buffer["ip"]["observedAt"] = observed_at
                                                    config = address.get("config")
                                                    if isinstance(config, dict):
                                                        if config is not None and len(config) != 0:
                                                            interface_address_config_dict_buffer = {}
                                                            interface_address_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6AddressesAddressConfig:" + interface_address_dict_buffer["id"].split(":")[-1]
                                                            interface_address_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv6AddressesAddressConfig"
                                                            interface_address_config_dict_buffer["isPartOf"] = {}
                                                            interface_address_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_address_config_dict_buffer["isPartOf"]["object"] = interface_address_dict_buffer["id"]
                                                            interface_address_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            ip = config.get("ip")
                                                            if ip is not None:
                                                                element_text = ip
                                                                interface_address_config_dict_buffer["ip"] = {}
                                                                interface_address_config_dict_buffer["ip"]["type"] = "Property"
                                                                interface_address_config_dict_buffer["ip"]["value"] = element_text
                                                                interface_address_config_dict_buffer["ip"]["observedAt"] = observed_at
                                                            prefixLength = config.get("prefix-length")
                                                            if prefixLength is not None:
                                                                element_text = prefixLength
                                                                interface_address_config_dict_buffer["prefixLength"] = {}
                                                                interface_address_config_dict_buffer["prefixLength"]["type"] = "Property"
                                                                interface_address_config_dict_buffer["prefixLength"]["value"] = int(element_text)
                                                                interface_address_config_dict_buffer["prefixLength"]["observedAt"] = observed_at
                                                            dict_buffers.append(interface_address_config_dict_buffer)
                                                    state = address.get("state")
                                                    if isinstance(state, dict):
                                                        if state is not None and len(state) != 0:
                                                            interface_address_state_dict_buffer = {}
                                                            interface_address_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6AddressesAddressState:" + interface_address_dict_buffer["id"].split(":")[-1]
                                                            interface_address_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv6AddressesAddressState"
                                                            interface_address_state_dict_buffer["isPartOf"] = {}
                                                            interface_address_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_address_state_dict_buffer["isPartOf"]["object"] = interface_address_dict_buffer["id"]
                                                            interface_address_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            ip = state.get("ip")
                                                            if ip is not None:
                                                                element_text = ip
                                                                interface_address_state_dict_buffer["ip"] = {}
                                                                interface_address_state_dict_buffer["ip"]["type"] = "Property"
                                                                interface_address_state_dict_buffer["ip"]["value"] = element_text
                                                                interface_address_state_dict_buffer["ip"]["observedAt"] = observed_at
                                                            prefixLength = state.get("prefix-length")
                                                            if prefixLength is not None:
                                                                element_text = prefixLength
                                                                interface_address_state_dict_buffer["prefixLength"] = {}
                                                                interface_address_state_dict_buffer["prefixLength"]["type"] = "Property"
                                                                interface_address_state_dict_buffer["prefixLength"]["value"] = int(element_text)
                                                                interface_address_state_dict_buffer["prefixLength"]["observedAt"] = observed_at
                                                            origin = state.get("origin")
                                                            if origin is not None:
                                                                element_text = origin
                                                                interface_address_state_dict_buffer["origin"] = {}
                                                                interface_address_state_dict_buffer["origin"]["type"] = "Property"
                                                                interface_address_state_dict_buffer["origin"]["value"] = element_text
                                                                interface_address_state_dict_buffer["origin"]["observedAt"] = observed_at
                                                            status = state.get("status")
                                                            if status is not None:
                                                                element_text = status
                                                                interface_address_state_dict_buffer["status"] = {}
                                                                interface_address_state_dict_buffer["status"]["type"] = "Property"
                                                                interface_address_state_dict_buffer["status"]["value"] = element_text
                                                                interface_address_state_dict_buffer["status"]["observedAt"] = observed_at
                                                            dict_buffers.append(interface_address_state_dict_buffer)
                                                    vrrp = address.get("vrrp")
                                                    if isinstance(vrrp, dict):
                                                        if vrrp is not None and len(vrrp) != 0:
                                                            vrrp_vrrp_group = vrrp.get("vrrp-group")
                                                            for vrrp_group in vrrp_vrrp_group:
                                                                interface_address_vrrp_group_dict_buffer = {}
                                                                interface_address_vrrp_group_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroup:" + interface_address_dict_buffer["id"].split(":")[-1]
                                                                interface_address_vrrp_group_dict_buffer["type"] = "InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroup"
                                                                interface_address_vrrp_group_dict_buffer["isPartOf"] = {}
                                                                interface_address_vrrp_group_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                interface_address_vrrp_group_dict_buffer["isPartOf"]["object"] = interface_address_dict_buffer["id"]
                                                                interface_address_vrrp_group_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                virtualRouterId = vrrp_group.get("virtual-router-id")
                                                                if virtualRouterId is not None:
                                                                    element_text = virtualRouterId
                                                                    if interface_address_vrrp_group_dict_buffer["id"].split(":")[-1] != element_text:
                                                                        interface_address_vrrp_group_dict_buffer["id"] = interface_address_vrrp_group_dict_buffer["id"] + element_text
                                                                    interface_address_vrrp_group_dict_buffer["virtualRouterId"] = {}
                                                                    interface_address_vrrp_group_dict_buffer["virtualRouterId"]["type"] = "Relationship"
                                                                    interface_address_vrrp_group_dict_buffer["virtualRouterId"]["object"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupConfig:" + interface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                    interface_address_vrrp_group_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                                config = vrrp_group.get("config")
                                                                if isinstance(config, dict):
                                                                    if config is not None and len(config) != 0:
                                                                        interface_address_vrrp_group_config_dict_buffer = {}
                                                                        interface_address_vrrp_group_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupConfig:" + interface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                        interface_address_vrrp_group_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupConfig"
                                                                        interface_address_vrrp_group_config_dict_buffer["isPartOf"] = {}
                                                                        interface_address_vrrp_group_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                        interface_address_vrrp_group_config_dict_buffer["isPartOf"]["object"] = interface_address_vrrp_group_dict_buffer["id"]
                                                                        interface_address_vrrp_group_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                        virtualRouterId = config.get("virtual-router-id")
                                                                        if virtualRouterId is not None:
                                                                            element_text = virtualRouterId
                                                                            if interface_address_vrrp_group_config_dict_buffer["id"].split(":")[-1] != int(element_text):
                                                                                interface_address_vrrp_group_config_dict_buffer["id"] = interface_address_vrrp_group_config_dict_buffer["id"] + int(element_text)
                                                                            interface_address_vrrp_group_config_dict_buffer["virtualRouterId"] = {}
                                                                            interface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["type"] = "Property"
                                                                            interface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["value"] = int(element_text)
                                                                            interface_address_vrrp_group_config_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                                        virtualAddress = config.get("virtual-address")
                                                                        if virtualAddress is not None:
                                                                            element_text = virtualAddress
                                                                            interface_address_vrrp_group_config_dict_buffer["virtualAddress"] = {}
                                                                            interface_address_vrrp_group_config_dict_buffer["virtualAddress"]["type"] = "Property"
                                                                            interface_address_vrrp_group_config_dict_buffer["virtualAddress"]["value"] = element_text
                                                                            interface_address_vrrp_group_config_dict_buffer["virtualAddress"]["observedAt"] = observed_at
                                                                        priority = config.get("priority")
                                                                        if priority is not None:
                                                                            element_text = priority
                                                                            interface_address_vrrp_group_config_dict_buffer["priority"] = {}
                                                                            interface_address_vrrp_group_config_dict_buffer["priority"]["type"] = "Property"
                                                                            interface_address_vrrp_group_config_dict_buffer["priority"]["value"] = int(element_text)
                                                                            interface_address_vrrp_group_config_dict_buffer["priority"]["observedAt"] = observed_at
                                                                        preempt = config.get("preempt")
                                                                        if preempt is not None:
                                                                            element_text = preempt
                                                                            interface_address_vrrp_group_config_dict_buffer["preempt"] = {}
                                                                            interface_address_vrrp_group_config_dict_buffer["preempt"]["type"] = "Property"
                                                                            interface_address_vrrp_group_config_dict_buffer["preempt"]["value"] = eval(str(element_text).capitalize())
                                                                            interface_address_vrrp_group_config_dict_buffer["preempt"]["observedAt"] = observed_at
                                                                        preemptDelay = config.get("preempt-delay")
                                                                        if preemptDelay is not None:
                                                                            element_text = preemptDelay
                                                                            interface_address_vrrp_group_config_dict_buffer["preemptDelay"] = {}
                                                                            interface_address_vrrp_group_config_dict_buffer["preemptDelay"]["type"] = "Property"
                                                                            interface_address_vrrp_group_config_dict_buffer["preemptDelay"]["value"] = int(element_text)
                                                                            interface_address_vrrp_group_config_dict_buffer["preemptDelay"]["observedAt"] = observed_at
                                                                        acceptMode = config.get("accept-mode")
                                                                        if acceptMode is not None:
                                                                            element_text = acceptMode
                                                                            interface_address_vrrp_group_config_dict_buffer["acceptMode"] = {}
                                                                            interface_address_vrrp_group_config_dict_buffer["acceptMode"]["type"] = "Property"
                                                                            interface_address_vrrp_group_config_dict_buffer["acceptMode"]["value"] = eval(str(element_text).capitalize())
                                                                            interface_address_vrrp_group_config_dict_buffer["acceptMode"]["observedAt"] = observed_at
                                                                        advertisementInterval = config.get("advertisement-interval")
                                                                        if advertisementInterval is not None:
                                                                            element_text = advertisementInterval
                                                                            interface_address_vrrp_group_config_dict_buffer["advertisementInterval"] = {}
                                                                            interface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["type"] = "Property"
                                                                            interface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["value"] = int(element_text)
                                                                            interface_address_vrrp_group_config_dict_buffer["advertisementInterval"]["observedAt"] = observed_at
                                                                        virtualLinkLocal = config.get("virtual-link-local")
                                                                        if virtualLinkLocal is not None:
                                                                            element_text = virtualLinkLocal
                                                                            interface_address_vrrp_group_config_dict_buffer["virtualLinkLocal"] = {}
                                                                            interface_address_vrrp_group_config_dict_buffer["virtualLinkLocal"]["type"] = "Property"
                                                                            interface_address_vrrp_group_config_dict_buffer["virtualLinkLocal"]["value"] = element_text
                                                                            interface_address_vrrp_group_config_dict_buffer["virtualLinkLocal"]["observedAt"] = observed_at
                                                                        dict_buffers.append(interface_address_vrrp_group_config_dict_buffer)
                                                                state = vrrp_group.get("state")
                                                                if isinstance(state, dict):
                                                                    if state is not None and len(state) != 0:
                                                                        interface_address_vrrp_group_state_dict_buffer = {}
                                                                        interface_address_vrrp_group_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupState:" + interface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                        interface_address_vrrp_group_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupState"
                                                                        interface_address_vrrp_group_state_dict_buffer["isPartOf"] = {}
                                                                        interface_address_vrrp_group_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                        interface_address_vrrp_group_state_dict_buffer["isPartOf"]["object"] = interface_address_vrrp_group_dict_buffer["id"]
                                                                        interface_address_vrrp_group_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                        virtualRouterId = state.get("virtual-router-id")
                                                                        if virtualRouterId is not None:
                                                                            element_text = virtualRouterId
                                                                            if interface_address_vrrp_group_state_dict_buffer["id"].split(":")[-1] != int(element_text):
                                                                                interface_address_vrrp_group_state_dict_buffer["id"] = interface_address_vrrp_group_state_dict_buffer["id"] + int(element_text)
                                                                            interface_address_vrrp_group_state_dict_buffer["virtualRouterId"] = {}
                                                                            interface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["type"] = "Property"
                                                                            interface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["value"] = int(element_text)
                                                                            interface_address_vrrp_group_state_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                                                                        virtualAddress = state.get("virtual-address")
                                                                        if virtualAddress is not None:
                                                                            element_text = virtualAddress
                                                                            interface_address_vrrp_group_state_dict_buffer["virtualAddress"] = {}
                                                                            interface_address_vrrp_group_state_dict_buffer["virtualAddress"]["type"] = "Property"
                                                                            interface_address_vrrp_group_state_dict_buffer["virtualAddress"]["value"] = element_text
                                                                            interface_address_vrrp_group_state_dict_buffer["virtualAddress"]["observedAt"] = observed_at
                                                                        priority = state.get("priority")
                                                                        if priority is not None:
                                                                            element_text = priority
                                                                            interface_address_vrrp_group_state_dict_buffer["priority"] = {}
                                                                            interface_address_vrrp_group_state_dict_buffer["priority"]["type"] = "Property"
                                                                            interface_address_vrrp_group_state_dict_buffer["priority"]["value"] = int(element_text)
                                                                            interface_address_vrrp_group_state_dict_buffer["priority"]["observedAt"] = observed_at
                                                                        preempt = state.get("preempt")
                                                                        if preempt is not None:
                                                                            element_text = preempt
                                                                            interface_address_vrrp_group_state_dict_buffer["preempt"] = {}
                                                                            interface_address_vrrp_group_state_dict_buffer["preempt"]["type"] = "Property"
                                                                            interface_address_vrrp_group_state_dict_buffer["preempt"]["value"] = eval(str(element_text).capitalize())
                                                                            interface_address_vrrp_group_state_dict_buffer["preempt"]["observedAt"] = observed_at
                                                                        preemptDelay = state.get("preempt-delay")
                                                                        if preemptDelay is not None:
                                                                            element_text = preemptDelay
                                                                            interface_address_vrrp_group_state_dict_buffer["preemptDelay"] = {}
                                                                            interface_address_vrrp_group_state_dict_buffer["preemptDelay"]["type"] = "Property"
                                                                            interface_address_vrrp_group_state_dict_buffer["preemptDelay"]["value"] = int(element_text)
                                                                            interface_address_vrrp_group_state_dict_buffer["preemptDelay"]["observedAt"] = observed_at
                                                                        acceptMode = state.get("accept-mode")
                                                                        if acceptMode is not None:
                                                                            element_text = acceptMode
                                                                            interface_address_vrrp_group_state_dict_buffer["acceptMode"] = {}
                                                                            interface_address_vrrp_group_state_dict_buffer["acceptMode"]["type"] = "Property"
                                                                            interface_address_vrrp_group_state_dict_buffer["acceptMode"]["value"] = eval(str(element_text).capitalize())
                                                                            interface_address_vrrp_group_state_dict_buffer["acceptMode"]["observedAt"] = observed_at
                                                                        advertisementInterval = state.get("advertisement-interval")
                                                                        if advertisementInterval is not None:
                                                                            element_text = advertisementInterval
                                                                            interface_address_vrrp_group_state_dict_buffer["advertisementInterval"] = {}
                                                                            interface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["type"] = "Property"
                                                                            interface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["value"] = int(element_text)
                                                                            interface_address_vrrp_group_state_dict_buffer["advertisementInterval"]["observedAt"] = observed_at
                                                                        currentPriority = state.get("current-priority")
                                                                        if currentPriority is not None:
                                                                            element_text = currentPriority
                                                                            interface_address_vrrp_group_state_dict_buffer["currentPriority"] = {}
                                                                            interface_address_vrrp_group_state_dict_buffer["currentPriority"]["type"] = "Property"
                                                                            interface_address_vrrp_group_state_dict_buffer["currentPriority"]["value"] = int(element_text)
                                                                            interface_address_vrrp_group_state_dict_buffer["currentPriority"]["observedAt"] = observed_at
                                                                        virtualLinkLocal = state.get("virtual-link-local")
                                                                        if virtualLinkLocal is not None:
                                                                            element_text = virtualLinkLocal
                                                                            interface_address_vrrp_group_state_dict_buffer["virtualLinkLocal"] = {}
                                                                            interface_address_vrrp_group_state_dict_buffer["virtualLinkLocal"]["type"] = "Property"
                                                                            interface_address_vrrp_group_state_dict_buffer["virtualLinkLocal"]["value"] = element_text
                                                                            interface_address_vrrp_group_state_dict_buffer["virtualLinkLocal"]["observedAt"] = observed_at
                                                                        dict_buffers.append(interface_address_vrrp_group_state_dict_buffer)
                                                                interface_tracking = vrrp_group.get("interface-tracking")
                                                                if isinstance(interface_tracking, dict):
                                                                    if interface_tracking is not None and len(interface_tracking) != 0:
                                                                        config = interface_tracking.get("config")
                                                                        if isinstance(config, dict):
                                                                            if config is not None and len(config) != 0:
                                                                                interface_address_vrrp_group_config_dict_buffer = {}
                                                                                interface_address_vrrp_group_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig:" + interface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                                interface_address_vrrp_group_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupInterfaceTrackingConfig"
                                                                                interface_address_vrrp_group_config_dict_buffer["isPartOf"] = {}
                                                                                interface_address_vrrp_group_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                                interface_address_vrrp_group_config_dict_buffer["isPartOf"]["object"] = interface_address_vrrp_group_dict_buffer["id"]
                                                                                interface_address_vrrp_group_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                                trackInterface = config.get("track-interface")
                                                                                if trackInterface is not None:
                                                                                    element_text = trackInterface
                                                                                    interface_address_vrrp_group_config_dict_buffer["trackInterface"] = {}
                                                                                    interface_address_vrrp_group_config_dict_buffer["trackInterface"]["type"] = "Relationship"
                                                                                    interface_address_vrrp_group_config_dict_buffer["trackInterface"]["object"] = "urn:ngsi-ld:Interface:" + interface_address_vrrp_group_config_dict_buffer["id"].split(":")[-1]
                                                                                    interface_address_vrrp_group_config_dict_buffer["trackInterface"]["observedAt"] = observed_at
                                                                                priorityDecrement = config.get("priority-decrement")
                                                                                if priorityDecrement is not None:
                                                                                    element_text = priorityDecrement
                                                                                    interface_address_vrrp_group_config_dict_buffer["priorityDecrement"] = {}
                                                                                    interface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["type"] = "Property"
                                                                                    interface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["value"] = int(element_text)
                                                                                    interface_address_vrrp_group_config_dict_buffer["priorityDecrement"]["observedAt"] = observed_at
                                                                                dict_buffers.append(interface_address_vrrp_group_config_dict_buffer)
                                                                        state = interface_tracking.get("state")
                                                                        if isinstance(state, dict):
                                                                            if state is not None and len(state) != 0:
                                                                                interface_address_vrrp_group_state_dict_buffer = {}
                                                                                interface_address_vrrp_group_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupInterfaceTrackingState:" + interface_address_vrrp_group_dict_buffer["id"].split(":")[-1]
                                                                                interface_address_vrrp_group_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv6AddressesAddressVrrpVrrpGroupInterfaceTrackingState"
                                                                                interface_address_vrrp_group_state_dict_buffer["isPartOf"] = {}
                                                                                interface_address_vrrp_group_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                                interface_address_vrrp_group_state_dict_buffer["isPartOf"]["object"] = interface_address_vrrp_group_dict_buffer["id"]
                                                                                interface_address_vrrp_group_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                                trackInterface = state.get("track-interface")
                                                                                if trackInterface is not None:
                                                                                    element_text = trackInterface
                                                                                    interface_address_vrrp_group_state_dict_buffer["trackInterface"] = {}
                                                                                    interface_address_vrrp_group_state_dict_buffer["trackInterface"]["type"] = "Relationship"
                                                                                    interface_address_vrrp_group_state_dict_buffer["trackInterface"]["object"] = "urn:ngsi-ld:Interface:" + interface_address_vrrp_group_state_dict_buffer["id"].split(":")[-1]
                                                                                    interface_address_vrrp_group_state_dict_buffer["trackInterface"]["observedAt"] = observed_at
                                                                                priorityDecrement = state.get("priority-decrement")
                                                                                if priorityDecrement is not None:
                                                                                    element_text = priorityDecrement
                                                                                    interface_address_vrrp_group_state_dict_buffer["priorityDecrement"] = {}
                                                                                    interface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["type"] = "Property"
                                                                                    interface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["value"] = int(element_text)
                                                                                    interface_address_vrrp_group_state_dict_buffer["priorityDecrement"]["observedAt"] = observed_at
                                                                                dict_buffers.append(interface_address_vrrp_group_state_dict_buffer)
                                                                dict_buffers.append(interface_address_vrrp_group_dict_buffer)
                                                    dict_buffers.append(interface_address_dict_buffer)
                                        router_advertisement = ipv6.get("router-advertisement")
                                        if isinstance(router_advertisement, dict):
                                            if router_advertisement is not None and len(router_advertisement) != 0:
                                                config = router_advertisement.get("config")
                                                if isinstance(config, dict):
                                                    if config is not None and len(config) != 0:
                                                        interface_config_dict_buffer = {}
                                                        interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6RouterAdvertisementConfig:" + interface_dict_buffer["id"].split(":")[-1]
                                                        interface_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv6RouterAdvertisementConfig"
                                                        interface_config_dict_buffer["isPartOf"] = {}
                                                        interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                        interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                        interval = config.get("interval")
                                                        if interval is not None:
                                                            element_text = interval
                                                            interface_config_dict_buffer["interval"] = {}
                                                            interface_config_dict_buffer["interval"]["type"] = "Property"
                                                            interface_config_dict_buffer["interval"]["value"] = int(element_text)
                                                            interface_config_dict_buffer["interval"]["observedAt"] = observed_at
                                                        lifetime = config.get("lifetime")
                                                        if lifetime is not None:
                                                            element_text = lifetime
                                                            interface_config_dict_buffer["lifetime"] = {}
                                                            interface_config_dict_buffer["lifetime"]["type"] = "Property"
                                                            interface_config_dict_buffer["lifetime"]["value"] = int(element_text)
                                                            interface_config_dict_buffer["lifetime"]["observedAt"] = observed_at
                                                        suppress = config.get("suppress")
                                                        if suppress is not None:
                                                            element_text = suppress
                                                            interface_config_dict_buffer["suppress"] = {}
                                                            interface_config_dict_buffer["suppress"]["type"] = "Property"
                                                            interface_config_dict_buffer["suppress"]["value"] = eval(str(element_text).capitalize())
                                                            interface_config_dict_buffer["suppress"]["observedAt"] = observed_at
                                                        dict_buffers.append(interface_config_dict_buffer)
                                                state = router_advertisement.get("state")
                                                if isinstance(state, dict):
                                                    if state is not None and len(state) != 0:
                                                        interface_state_dict_buffer = {}
                                                        interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6RouterAdvertisementState:" + interface_dict_buffer["id"].split(":")[-1]
                                                        interface_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv6RouterAdvertisementState"
                                                        interface_state_dict_buffer["isPartOf"] = {}
                                                        interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                        interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                        interval = state.get("interval")
                                                        if interval is not None:
                                                            element_text = interval
                                                            interface_state_dict_buffer["interval"] = {}
                                                            interface_state_dict_buffer["interval"]["type"] = "Property"
                                                            interface_state_dict_buffer["interval"]["value"] = int(element_text)
                                                            interface_state_dict_buffer["interval"]["observedAt"] = observed_at
                                                        lifetime = state.get("lifetime")
                                                        if lifetime is not None:
                                                            element_text = lifetime
                                                            interface_state_dict_buffer["lifetime"] = {}
                                                            interface_state_dict_buffer["lifetime"]["type"] = "Property"
                                                            interface_state_dict_buffer["lifetime"]["value"] = int(element_text)
                                                            interface_state_dict_buffer["lifetime"]["observedAt"] = observed_at
                                                        suppress = state.get("suppress")
                                                        if suppress is not None:
                                                            element_text = suppress
                                                            interface_state_dict_buffer["suppress"] = {}
                                                            interface_state_dict_buffer["suppress"]["type"] = "Property"
                                                            interface_state_dict_buffer["suppress"]["value"] = eval(str(element_text).capitalize())
                                                            interface_state_dict_buffer["suppress"]["observedAt"] = observed_at
                                                        dict_buffers.append(interface_state_dict_buffer)
                                        neighbors = ipv6.get("neighbors")
                                        if isinstance(neighbors, dict):
                                            if neighbors is not None and len(neighbors) != 0:
                                                neighbors_neighbor = neighbors.get("neighbor")
                                                for neighbor in neighbors_neighbor:
                                                    interface_neighbor_dict_buffer = {}
                                                    interface_neighbor_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6NeighborsNeighbor:" + interface_dict_buffer["id"].split(":")[-1]
                                                    interface_neighbor_dict_buffer["type"] = "InterfaceRoutedVlanIpv6NeighborsNeighbor"
                                                    interface_neighbor_dict_buffer["isPartOf"] = {}
                                                    interface_neighbor_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                    interface_neighbor_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                    interface_neighbor_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                    ip = neighbor.get("ip")
                                                    if ip is not None:
                                                        element_text = ip
                                                        if ":" in element_text:
                                                            element_text = element_text.replace(":",".")
                                                        if interface_neighbor_dict_buffer["id"].split(":")[-1] != element_text:
                                                            interface_neighbor_dict_buffer["id"] = interface_neighbor_dict_buffer["id"] + ":" + element_text
                                                        interface_neighbor_dict_buffer["ip"] = {}
                                                        interface_neighbor_dict_buffer["ip"]["type"] = "Relationship"
                                                        interface_neighbor_dict_buffer["ip"]["object"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6NeighborsNeighborConfig:" + interface_neighbor_dict_buffer["id"].split(":")[-1]
                                                        interface_neighbor_dict_buffer["ip"]["observedAt"] = observed_at
                                                    config = neighbor.get("config")
                                                    if isinstance(config, dict):
                                                        if config is not None and len(config) != 0:
                                                            interface_neighbor_config_dict_buffer = {}
                                                            interface_neighbor_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6NeighborsNeighborConfig:" + interface_neighbor_dict_buffer["id"].split(":")[-1]
                                                            interface_neighbor_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv6NeighborsNeighborConfig"
                                                            interface_neighbor_config_dict_buffer["isPartOf"] = {}
                                                            interface_neighbor_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_neighbor_config_dict_buffer["isPartOf"]["object"] = interface_neighbor_dict_buffer["id"]
                                                            interface_neighbor_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            ip = config.get("ip")
                                                            if ip is not None:
                                                                element_text = ip
                                                                interface_neighbor_config_dict_buffer["ip"] = {}
                                                                interface_neighbor_config_dict_buffer["ip"]["type"] = "Property"
                                                                interface_neighbor_config_dict_buffer["ip"]["value"] = element_text
                                                                interface_neighbor_config_dict_buffer["ip"]["observedAt"] = observed_at
                                                            linkLayerAddress = config.get("link-layer-address")
                                                            if linkLayerAddress is not None:
                                                                element_text = linkLayerAddress
                                                                interface_neighbor_config_dict_buffer["linkLayerAddress"] = {}
                                                                interface_neighbor_config_dict_buffer["linkLayerAddress"]["type"] = "Property"
                                                                interface_neighbor_config_dict_buffer["linkLayerAddress"]["value"] = element_text
                                                                interface_neighbor_config_dict_buffer["linkLayerAddress"]["observedAt"] = observed_at
                                                            dict_buffers.append(interface_neighbor_config_dict_buffer)
                                                    state = neighbor.get("state")
                                                    if isinstance(state, dict):
                                                        if state is not None and len(state) != 0:
                                                            interface_neighbor_state_dict_buffer = {}
                                                            interface_neighbor_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6NeighborsNeighborState:" + interface_neighbor_dict_buffer["id"].split(":")[-1]
                                                            interface_neighbor_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv6NeighborsNeighborState"
                                                            interface_neighbor_state_dict_buffer["isPartOf"] = {}
                                                            interface_neighbor_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                            interface_neighbor_state_dict_buffer["isPartOf"]["object"] = interface_neighbor_dict_buffer["id"]
                                                            interface_neighbor_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                            ip = state.get("ip")
                                                            if ip is not None:
                                                                element_text = ip
                                                                interface_neighbor_state_dict_buffer["ip"] = {}
                                                                interface_neighbor_state_dict_buffer["ip"]["type"] = "Property"
                                                                interface_neighbor_state_dict_buffer["ip"]["value"] = element_text
                                                                interface_neighbor_state_dict_buffer["ip"]["observedAt"] = observed_at
                                                            linkLayerAddress = state.get("link-layer-address")
                                                            if linkLayerAddress is not None:
                                                                element_text = linkLayerAddress
                                                                interface_neighbor_state_dict_buffer["linkLayerAddress"] = {}
                                                                interface_neighbor_state_dict_buffer["linkLayerAddress"]["type"] = "Property"
                                                                interface_neighbor_state_dict_buffer["linkLayerAddress"]["value"] = element_text
                                                                interface_neighbor_state_dict_buffer["linkLayerAddress"]["observedAt"] = observed_at
                                                            origin = state.get("origin")
                                                            if origin is not None:
                                                                element_text = origin
                                                                interface_neighbor_state_dict_buffer["origin"] = {}
                                                                interface_neighbor_state_dict_buffer["origin"]["type"] = "Property"
                                                                interface_neighbor_state_dict_buffer["origin"]["value"] = element_text
                                                                interface_neighbor_state_dict_buffer["origin"]["observedAt"] = observed_at
                                                            isRouter = state.get("is-router")
                                                            if isRouter is not None:
                                                                element_text = isRouter
                                                                interface_neighbor_state_dict_buffer["isRouter"] = {}
                                                                interface_neighbor_state_dict_buffer["isRouter"]["type"] = "Property"
                                                                interface_neighbor_state_dict_buffer["isRouter"]["value"] = element_text
                                                                interface_neighbor_state_dict_buffer["isRouter"]["observedAt"] = observed_at
                                                            neighborState = state.get("neighbor-state")
                                                            if neighborState is not None:
                                                                element_text = neighborState
                                                                interface_neighbor_state_dict_buffer["neighborState"] = {}
                                                                interface_neighbor_state_dict_buffer["neighborState"]["type"] = "Property"
                                                                interface_neighbor_state_dict_buffer["neighborState"]["value"] = element_text
                                                                interface_neighbor_state_dict_buffer["neighborState"]["observedAt"] = observed_at
                                                            dict_buffers.append(interface_neighbor_state_dict_buffer)
                                                    dict_buffers.append(interface_neighbor_dict_buffer)
                                        unnumbered = ipv6.get("unnumbered")
                                        if isinstance(unnumbered, dict):
                                            if unnumbered is not None and len(unnumbered) != 0:
                                                config = unnumbered.get("config")
                                                if isinstance(config, dict):
                                                    if config is not None and len(config) != 0:
                                                        interface_config_dict_buffer = {}
                                                        interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6UnnumberedConfig:" + interface_dict_buffer["id"].split(":")[-1]
                                                        interface_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv6UnnumberedConfig"
                                                        interface_config_dict_buffer["isPartOf"] = {}
                                                        interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                        interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                        enabled = config.get("enabled")
                                                        if enabled is not None:
                                                            element_text = enabled
                                                            interface_config_dict_buffer["enabled"] = {}
                                                            interface_config_dict_buffer["enabled"]["type"] = "Property"
                                                            interface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                            interface_config_dict_buffer["enabled"]["observedAt"] = observed_at
                                                        dict_buffers.append(interface_config_dict_buffer)
                                                state = unnumbered.get("state")
                                                if isinstance(state, dict):
                                                    if state is not None and len(state) != 0:
                                                        interface_state_dict_buffer = {}
                                                        interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6UnnumberedState:" + interface_dict_buffer["id"].split(":")[-1]
                                                        interface_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv6UnnumberedState"
                                                        interface_state_dict_buffer["isPartOf"] = {}
                                                        interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                        interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                        enabled = state.get("enabled")
                                                        if enabled is not None:
                                                            element_text = enabled
                                                            interface_state_dict_buffer["enabled"] = {}
                                                            interface_state_dict_buffer["enabled"]["type"] = "Property"
                                                            interface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                            interface_state_dict_buffer["enabled"]["observedAt"] = observed_at
                                                        dict_buffers.append(interface_state_dict_buffer)
                                                interface_ref = unnumbered.get("interface-ref")
                                                if isinstance(interface_ref, dict):
                                                    if interface_ref is not None and len(interface_ref) != 0:
                                                        config = interface_ref.get("config")
                                                        if isinstance(config, dict):
                                                            if config is not None and len(config) != 0:
                                                                interface_config_dict_buffer = {}
                                                                interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6UnnumberedInterfaceRefConfig:" + interface_dict_buffer["id"].split(":")[-1]
                                                                interface_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv6UnnumberedInterfaceRefConfig"
                                                                interface_config_dict_buffer["isPartOf"] = {}
                                                                interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                                interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                interface = config.get("interface")
                                                                if interface is not None:
                                                                    element_text = interface
                                                                    if interface_config_dict_buffer["id"].split(":")[-1] != element_text:
                                                                        interface_config_dict_buffer["id"] = interface_config_dict_buffer["id"] + element_text
                                                                    interface_config_dict_buffer["interface"] = {}
                                                                    interface_config_dict_buffer["interface"]["type"] = "Relationship"
                                                                    interface_config_dict_buffer["interface"]["object"] = "urn:ngsi-ld:Interface:" + interface_config_dict_buffer["id"].split(":")[-1]
                                                                    interface_config_dict_buffer["interface"]["observedAt"] = observed_at
                                                                subinterface = config.get("subinterface")
                                                                if subinterface is not None:
                                                                    element_text = subinterface
                                                                    if "." + str(element_text) not in interface_config_dict_buffer["id"].split(":")[-1]:
                                                                        interface_config_dict_buffer["id"] = interface_config_dict_buffer["id"] + "." + str(element_text)
                                                                    interface_config_dict_buffer["subinterface"] = {}
                                                                    interface_config_dict_buffer["subinterface"]["type"] = "Relationship"
                                                                    interface_config_dict_buffer["subinterface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterface:" + interface_config_dict_buffer["id"].split(":")[-1]
                                                                    interface_config_dict_buffer["subinterface"]["observedAt"] = observed_at
                                                                dict_buffers.append(interface_config_dict_buffer)
                                                        state = interface_ref.get("state")
                                                        if isinstance(state, dict):
                                                            if state is not None and len(state) != 0:
                                                                interface_state_dict_buffer = {}
                                                                interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6UnnumberedInterfaceRefState:" + interface_dict_buffer["id"].split(":")[-1]
                                                                interface_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv6UnnumberedInterfaceRefState"
                                                                interface_state_dict_buffer["isPartOf"] = {}
                                                                interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                                interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                                interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                                interface = state.get("interface")
                                                                if interface is not None:
                                                                    element_text = interface
                                                                    if interface_state_dict_buffer["id"].split(":")[-1] != element_text:
                                                                        interface_state_dict_buffer["id"] = interface_state_dict_buffer["id"] + element_text
                                                                    interface_state_dict_buffer["interface"] = {}
                                                                    interface_state_dict_buffer["interface"]["type"] = "Relationship"
                                                                    interface_state_dict_buffer["interface"]["object"] = "urn:ngsi-ld:Interface:" + interface_state_dict_buffer["id"].split(":")[-1]
                                                                    interface_state_dict_buffer["interface"]["observedAt"] = observed_at
                                                                subinterface = state.get("subinterface")
                                                                if subinterface is not None:
                                                                    element_text = subinterface
                                                                    if "." + str(element_text) not in interface_state_dict_buffer["id"].split(":")[-1]:
                                                                        interface_state_dict_buffer["id"] = interface_state_dict_buffer["id"] + "." + str(element_text)
                                                                    interface_state_dict_buffer["subinterface"] = {}
                                                                    interface_state_dict_buffer["subinterface"]["type"] = "Relationship"
                                                                    interface_state_dict_buffer["subinterface"]["object"] = "urn:ngsi-ld:InterfaceSubinterfacesSubinterface:" + interface_state_dict_buffer["id"].split(":")[-1]
                                                                    interface_state_dict_buffer["subinterface"]["observedAt"] = observed_at
                                                                dict_buffers.append(interface_state_dict_buffer)
                                        config = ipv6.get("config")
                                        if isinstance(config, dict):
                                            if config is not None and len(config) != 0:
                                                interface_config_dict_buffer = {}
                                                interface_config_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6Config:" + interface_dict_buffer["id"].split(":")[-1]
                                                interface_config_dict_buffer["type"] = "InterfaceRoutedVlanIpv6Config"
                                                interface_config_dict_buffer["isPartOf"] = {}
                                                interface_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_config_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                interface_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                enabled = config.get("enabled")
                                                if enabled is not None:
                                                    element_text = enabled
                                                    interface_config_dict_buffer["enabled"] = {}
                                                    interface_config_dict_buffer["enabled"]["type"] = "Property"
                                                    interface_config_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                    interface_config_dict_buffer["enabled"]["observedAt"] = observed_at
                                                mtu = config.get("mtu")
                                                if mtu is not None:
                                                    element_text = mtu
                                                    interface_config_dict_buffer["mtu"] = {}
                                                    interface_config_dict_buffer["mtu"]["type"] = "Property"
                                                    interface_config_dict_buffer["mtu"]["value"] = int(element_text)
                                                    interface_config_dict_buffer["mtu"]["observedAt"] = observed_at
                                                dupAddrDetectTransmits = config.get("dup-addr-detect-transmits")
                                                if dupAddrDetectTransmits is not None:
                                                    element_text = dupAddrDetectTransmits
                                                    interface_config_dict_buffer["dupAddrDetectTransmits"] = {}
                                                    interface_config_dict_buffer["dupAddrDetectTransmits"]["type"] = "Property"
                                                    interface_config_dict_buffer["dupAddrDetectTransmits"]["value"] = int(element_text)
                                                    interface_config_dict_buffer["dupAddrDetectTransmits"]["observedAt"] = observed_at
                                                dhcpClient = config.get("dhcp-client")
                                                if dhcpClient is not None:
                                                    element_text = dhcpClient
                                                    interface_config_dict_buffer["dhcpClient"] = {}
                                                    interface_config_dict_buffer["dhcpClient"]["type"] = "Property"
                                                    interface_config_dict_buffer["dhcpClient"]["value"] = eval(str(element_text).capitalize())
                                                    interface_config_dict_buffer["dhcpClient"]["observedAt"] = observed_at
                                                dict_buffers.append(interface_config_dict_buffer)
                                        state = ipv6.get("state")
                                        if isinstance(state, dict):
                                            if state is not None and len(state) != 0:
                                                interface_state_dict_buffer = {}
                                                interface_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6State:" + interface_dict_buffer["id"].split(":")[-1]
                                                interface_state_dict_buffer["type"] = "InterfaceRoutedVlanIpv6State"
                                                interface_state_dict_buffer["isPartOf"] = {}
                                                interface_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                interface_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                                                interface_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                enabled = state.get("enabled")
                                                if enabled is not None:
                                                    element_text = enabled
                                                    interface_state_dict_buffer["enabled"] = {}
                                                    interface_state_dict_buffer["enabled"]["type"] = "Property"
                                                    interface_state_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                                                    interface_state_dict_buffer["enabled"]["observedAt"] = observed_at
                                                mtu = state.get("mtu")
                                                if mtu is not None:
                                                    element_text = mtu
                                                    interface_state_dict_buffer["mtu"] = {}
                                                    interface_state_dict_buffer["mtu"]["type"] = "Property"
                                                    interface_state_dict_buffer["mtu"]["value"] = int(element_text)
                                                    interface_state_dict_buffer["mtu"]["observedAt"] = observed_at
                                                dupAddrDetectTransmits = state.get("dup-addr-detect-transmits")
                                                if dupAddrDetectTransmits is not None:
                                                    element_text = dupAddrDetectTransmits
                                                    interface_state_dict_buffer["dupAddrDetectTransmits"] = {}
                                                    interface_state_dict_buffer["dupAddrDetectTransmits"]["type"] = "Property"
                                                    interface_state_dict_buffer["dupAddrDetectTransmits"]["value"] = int(element_text)
                                                    interface_state_dict_buffer["dupAddrDetectTransmits"]["observedAt"] = observed_at
                                                dhcpClient = state.get("dhcp-client")
                                                if dhcpClient is not None:
                                                    element_text = dhcpClient
                                                    interface_state_dict_buffer["dhcpClient"] = {}
                                                    interface_state_dict_buffer["dhcpClient"]["type"] = "Property"
                                                    interface_state_dict_buffer["dhcpClient"]["value"] = eval(str(element_text).capitalize())
                                                    interface_state_dict_buffer["dhcpClient"]["observedAt"] = observed_at
                                                counters = state.get("counters")
                                                if isinstance(counters, dict):
                                                    if counters is not None and len(counters) != 0:
                                                        interface_state_counters_dict_buffer = {}
                                                        interface_state_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceRoutedVlanIpv6StateCounters:" + interface_state_dict_buffer["id"].split(":")[-1]
                                                        interface_state_counters_dict_buffer["type"] = "InterfaceRoutedVlanIpv6StateCounters"
                                                        interface_state_counters_dict_buffer["isPartOf"] = {}
                                                        interface_state_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                        interface_state_counters_dict_buffer["isPartOf"]["object"] = interface_state_dict_buffer["id"]
                                                        interface_state_counters_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                        inPkts = counters.get("in-pkts")
                                                        if inPkts is not None:
                                                            element_text = inPkts
                                                            interface_state_counters_dict_buffer["inPkts"] = {}
                                                            interface_state_counters_dict_buffer["inPkts"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["inPkts"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["inPkts"]["observedAt"] = observed_at
                                                        inOctets = counters.get("in-octets")
                                                        if inOctets is not None:
                                                            element_text = inOctets
                                                            interface_state_counters_dict_buffer["inOctets"] = {}
                                                            interface_state_counters_dict_buffer["inOctets"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["inOctets"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["inOctets"]["observedAt"] = observed_at
                                                        inErrorPkts = counters.get("in-error-pkts")
                                                        if inErrorPkts is not None:
                                                            element_text = inErrorPkts
                                                            interface_state_counters_dict_buffer["inErrorPkts"] = {}
                                                            interface_state_counters_dict_buffer["inErrorPkts"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["inErrorPkts"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["inErrorPkts"]["observedAt"] = observed_at
                                                        inForwardedPkts = counters.get("in-forwarded-pkts")
                                                        if inForwardedPkts is not None:
                                                            element_text = inForwardedPkts
                                                            interface_state_counters_dict_buffer["inForwardedPkts"] = {}
                                                            interface_state_counters_dict_buffer["inForwardedPkts"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["inForwardedPkts"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["inForwardedPkts"]["observedAt"] = observed_at
                                                        inForwardedOctets = counters.get("in-forwarded-octets")
                                                        if inForwardedOctets is not None:
                                                            element_text = inForwardedOctets
                                                            interface_state_counters_dict_buffer["inForwardedOctets"] = {}
                                                            interface_state_counters_dict_buffer["inForwardedOctets"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["inForwardedOctets"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["inForwardedOctets"]["observedAt"] = observed_at
                                                        inDiscardedPkts = counters.get("in-discarded-pkts")
                                                        if inDiscardedPkts is not None:
                                                            element_text = inDiscardedPkts
                                                            interface_state_counters_dict_buffer["inDiscardedPkts"] = {}
                                                            interface_state_counters_dict_buffer["inDiscardedPkts"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["inDiscardedPkts"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["inDiscardedPkts"]["observedAt"] = observed_at
                                                        outPkts = counters.get("out-pkts")
                                                        if outPkts is not None:
                                                            element_text = outPkts
                                                            interface_state_counters_dict_buffer["outPkts"] = {}
                                                            interface_state_counters_dict_buffer["outPkts"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["outPkts"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["outPkts"]["observedAt"] = observed_at
                                                        outOctets = counters.get("out-octets")
                                                        if outOctets is not None:
                                                            element_text = outOctets
                                                            interface_state_counters_dict_buffer["outOctets"] = {}
                                                            interface_state_counters_dict_buffer["outOctets"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["outOctets"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["outOctets"]["observedAt"] = observed_at
                                                        outErrorPkts = counters.get("out-error-pkts")
                                                        if outErrorPkts is not None:
                                                            element_text = outErrorPkts
                                                            interface_state_counters_dict_buffer["outErrorPkts"] = {}
                                                            interface_state_counters_dict_buffer["outErrorPkts"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["outErrorPkts"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["outErrorPkts"]["observedAt"] = observed_at
                                                        outForwardedPkts = counters.get("out-forwarded-pkts")
                                                        if outForwardedPkts is not None:
                                                            element_text = outForwardedPkts
                                                            interface_state_counters_dict_buffer["outForwardedPkts"] = {}
                                                            interface_state_counters_dict_buffer["outForwardedPkts"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["outForwardedPkts"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["outForwardedPkts"]["observedAt"] = observed_at
                                                        outForwardedOctets = counters.get("out-forwarded-octets")
                                                        if outForwardedOctets is not None:
                                                            element_text = outForwardedOctets
                                                            interface_state_counters_dict_buffer["outForwardedOctets"] = {}
                                                            interface_state_counters_dict_buffer["outForwardedOctets"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["outForwardedOctets"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["outForwardedOctets"]["observedAt"] = observed_at
                                                        outDiscardedPkts = counters.get("out-discarded-pkts")
                                                        if outDiscardedPkts is not None:
                                                            element_text = outDiscardedPkts
                                                            interface_state_counters_dict_buffer["outDiscardedPkts"] = {}
                                                            interface_state_counters_dict_buffer["outDiscardedPkts"]["type"] = "Property"
                                                            interface_state_counters_dict_buffer["outDiscardedPkts"]["value"] = int(element_text)
                                                            interface_state_counters_dict_buffer["outDiscardedPkts"]["observedAt"] = observed_at
                                                        dict_buffers.append(interface_state_counters_dict_buffer)
                                                dict_buffers.append(interface_state_dict_buffer)
                        dict_buffers.append(interface_dict_buffer)
        if isinstance(json_data.get("vlans"), dict):
            vlans = json_data.get("vlans")
            if vlans is not None and len(vlans) != 0:
                if "vlan" in list(vlans.keys()):
                    vlans = vlans.get("vlan")
                elif "openconfig-vlan:vlan" in list(vlans.keys()):
                    vlans = vlans.get("openconfig-vlan:vlan")
                for vlan in vlans:
                    if vlan is not None and len(vlan) != 0:
                        vlan_dict_buffer = {}
                        vlan_dict_buffer["id"] = "urn:ngsi-ld:Vlan:"
                        vlan_dict_buffer["type"] = "Vlan"
                        vlanId = vlan.get("vlan-id")
                        if vlanId is not None:
                            element_text = vlanId
                            if vlan_dict_buffer["id"].split(":")[-1] != element_text:
                                vlan_dict_buffer["id"] = vlan_dict_buffer["id"] + element_text
                            vlan_dict_buffer["vlanId"] = {}
                            vlan_dict_buffer["vlanId"]["type"] = "Relationship"
                            vlan_dict_buffer["vlanId"]["object"] = "urn:ngsi-ld:VlanConfig:" + vlan_dict_buffer["id"].split(":")[-1]
                            vlan_dict_buffer["vlanId"]["observedAt"] = observed_at
                        config = vlan.get("config")
                        if isinstance(config, dict):
                            if config is not None and len(config) != 0:
                                vlan_config_dict_buffer = {}
                                vlan_config_dict_buffer["id"] = "urn:ngsi-ld:VlanConfig:" + vlan_dict_buffer["id"].split(":")[-1]
                                vlan_config_dict_buffer["type"] = "VlanConfig"
                                vlan_config_dict_buffer["isPartOf"] = {}
                                vlan_config_dict_buffer["isPartOf"]["type"] = "Relationship"
                                vlan_config_dict_buffer["isPartOf"]["object"] = vlan_dict_buffer["id"]
                                vlan_config_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                vlanId = config.get("vlan-id")
                                if vlanId is not None:
                                    element_text = vlanId
                                    if vlan_config_dict_buffer["id"].split(":")[-1] != int(element_text):
                                        vlan_config_dict_buffer["id"] = vlan_config_dict_buffer["id"] + int(element_text)
                                    vlan_config_dict_buffer["vlanId"] = {}
                                    vlan_config_dict_buffer["vlanId"]["type"] = "Property"
                                    vlan_config_dict_buffer["vlanId"]["value"] = int(element_text)
                                    vlan_config_dict_buffer["vlanId"]["observedAt"] = observed_at
                                name = config.get("name")
                                if name is not None:
                                    element_text = name
                                    if vlan_config_dict_buffer["id"].split(":")[-1] != element_text:
                                        vlan_config_dict_buffer["id"] = vlan_config_dict_buffer["id"] + element_text
                                    vlan_config_dict_buffer["name"] = {}
                                    vlan_config_dict_buffer["name"]["type"] = "Property"
                                    vlan_config_dict_buffer["name"]["value"] = element_text
                                    vlan_config_dict_buffer["name"]["observedAt"] = observed_at
                                status = config.get("status")
                                if status is not None:
                                    element_text = status
                                    vlan_config_dict_buffer["status"] = {}
                                    vlan_config_dict_buffer["status"]["type"] = "Property"
                                    vlan_config_dict_buffer["status"]["value"] = element_text
                                    vlan_config_dict_buffer["status"]["observedAt"] = observed_at
                                dict_buffers.append(vlan_config_dict_buffer)
                        state = vlan.get("state")
                        if isinstance(state, dict):
                            if state is not None and len(state) != 0:
                                vlan_state_dict_buffer = {}
                                vlan_state_dict_buffer["id"] = "urn:ngsi-ld:VlanState:" + vlan_dict_buffer["id"].split(":")[-1]
                                vlan_state_dict_buffer["type"] = "VlanState"
                                vlan_state_dict_buffer["isPartOf"] = {}
                                vlan_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                vlan_state_dict_buffer["isPartOf"]["object"] = vlan_dict_buffer["id"]
                                vlan_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                vlanId = state.get("vlan-id")
                                if vlanId is not None:
                                    element_text = vlanId
                                    if vlan_state_dict_buffer["id"].split(":")[-1] != int(element_text):
                                        vlan_state_dict_buffer["id"] = vlan_state_dict_buffer["id"] + int(element_text)
                                    vlan_state_dict_buffer["vlanId"] = {}
                                    vlan_state_dict_buffer["vlanId"]["type"] = "Property"
                                    vlan_state_dict_buffer["vlanId"]["value"] = int(element_text)
                                    vlan_state_dict_buffer["vlanId"]["observedAt"] = observed_at
                                name = state.get("name")
                                if name is not None:
                                    element_text = name
                                    if vlan_state_dict_buffer["id"].split(":")[-1] != element_text:
                                        vlan_state_dict_buffer["id"] = vlan_state_dict_buffer["id"] + element_text
                                    vlan_state_dict_buffer["name"] = {}
                                    vlan_state_dict_buffer["name"]["type"] = "Property"
                                    vlan_state_dict_buffer["name"]["value"] = element_text
                                    vlan_state_dict_buffer["name"]["observedAt"] = observed_at
                                status = state.get("status")
                                if status is not None:
                                    element_text = status
                                    vlan_state_dict_buffer["status"] = {}
                                    vlan_state_dict_buffer["status"]["type"] = "Property"
                                    vlan_state_dict_buffer["status"]["value"] = element_text
                                    vlan_state_dict_buffer["status"]["observedAt"] = observed_at
                                dict_buffers.append(vlan_state_dict_buffer)
                        members = vlan.get("members")
                        if isinstance(members, dict):
                            if members is not None and len(members) != 0:
                                members_member = members.get("member")
                                for member in members_member:
                                    vlan_member_dict_buffer = {}
                                    vlan_member_dict_buffer["id"] = "urn:ngsi-ld:VlanMembersMember:" + vlan_dict_buffer["id"].split(":")[-1]
                                    vlan_member_dict_buffer["type"] = "VlanMembersMember"
                                    vlan_member_dict_buffer["isPartOf"] = {}
                                    vlan_member_dict_buffer["isPartOf"]["type"] = "Relationship"
                                    vlan_member_dict_buffer["isPartOf"]["object"] = vlan_dict_buffer["id"]
                                    vlan_member_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                    state = member.get("state")
                                    if isinstance(state, dict):
                                        if state is not None and len(state) != 0:
                                            vlan_member_state_dict_buffer = {}
                                            vlan_member_state_dict_buffer["id"] = "urn:ngsi-ld:VlanMembersMemberState:" + vlan_member_dict_buffer["id"].split(":")[-1]
                                            vlan_member_state_dict_buffer["type"] = "VlanMembersMemberState"
                                            vlan_member_state_dict_buffer["isPartOf"] = {}
                                            vlan_member_state_dict_buffer["isPartOf"]["type"] = "Relationship"
                                            vlan_member_state_dict_buffer["isPartOf"]["object"] = vlan_member_dict_buffer["id"]
                                            vlan_member_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                            interface = state.get("interface")
                                            if interface is not None:
                                                element_text = interface
                                                if vlan_member_state_dict_buffer["id"].split(":")[-1] != element_text:
                                                    vlan_member_state_dict_buffer["id"] = vlan_member_state_dict_buffer["id"] + element_text
                                                vlan_member_state_dict_buffer["interface"] = {}
                                                vlan_member_state_dict_buffer["interface"]["type"] = "Relationship"
                                                vlan_member_state_dict_buffer["interface"]["object"] = "urn:ngsi-ld:Interface:" + vlan_member_state_dict_buffer["id"].split(":")[-1]
                                                vlan_member_state_dict_buffer["interface"]["observedAt"] = observed_at
                                            dict_buffers.append(vlan_member_state_dict_buffer)
                                    dict_buffers.append(vlan_member_dict_buffer)
                        dict_buffers.append(vlan_dict_buffer)

        producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
        producer.send('output', value=json.dumps(dict_buffers[::-1], indent=4).encode('utf-8'))
        producer.flush()
        dict_buffers.clear()
