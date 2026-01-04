import json
import numpy as np
from datetime import datetime
import sys

json_payload = sys.argv[1]
dict_buffers = []
with open(json_payload) as f:
    data = json.load(f)
    observed_at = data.get("eventTime")

if data.get("interfaces") is not None:
    interfaces = data.get("interfaces")
elif data.get("ietf-interfaces:interfaces") is not None:
    interfaces = data.get("ietf-interfaces:interfaces")
else:
    interfaces = None
if interfaces is not None and len(interfaces) != 0:
    if "interface" in list(interfaces.keys()):
        interfaces = interfaces.get("interface")
    elif "ietf-interfaces:interface" in list(interfaces.keys()):
        interfaces = interfaces.get("ietf-interfaces:interface")
    for interface in interfaces:
        if interface is not None and len(interface) != 0:
            interface_dict_buffer = {}
            interface_dict_buffer["id"] = "urn:ngsi-ld:Interface"
            interface_dict_buffer["type"] = "Interface"
            name = interface.get("name")
            if name is not None:
                element_text = name
                if interface_dict_buffer["id"].split(":")[-1] != element_text:
                    interface_dict_buffer["id"] = interface_dict_buffer["id"] + ":" + str(element_text)
                interface_dict_buffer["name"] = {}
                interface_dict_buffer["name"]["type"] = "Property"
                interface_dict_buffer["name"]["value"] = element_text
                if observed_at is not None:
                    interface_dict_buffer["name"]["observedAt"] = observed_at
            description = interface.get("description")
            if description is not None:
                element_text = description
                interface_dict_buffer["description"] = {}
                interface_dict_buffer["description"]["type"] = "Property"
                interface_dict_buffer["description"]["value"] = element_text
                if observed_at is not None:
                    interface_dict_buffer["description"]["observedAt"] = observed_at
            type = interface.get("type")
            if type is not None and len(type) != 0:
                element_text = type
                if element_text is not None:
                    interface_dict_buffer["interfaceType"] = {}
                    interface_dict_buffer["interfaceType"]["type"] = "Relationship"
                    interface_dict_buffer["interfaceType"]["object"] = "urn:ngsi-ld:YANGIdentity:" + element_text
                    if observed_at is not None:
                        interface_dict_buffer["interfaceType"]["observedAt"] = observed_at
            enabled = interface.get("enabled")
            if enabled is not None:
                element_text = enabled
                interface_dict_buffer["enabled"] = {}
                interface_dict_buffer["enabled"]["type"] = "Property"
                interface_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                if observed_at is not None:
                    interface_dict_buffer["enabled"]["observedAt"] = observed_at
            linkUpDownTrapEnable = interface.get("link-up-down-trap-enable")
            if linkUpDownTrapEnable is not None:
                element_text = linkUpDownTrapEnable
                interface_dict_buffer["linkUpDownTrapEnable"] = {}
                interface_dict_buffer["linkUpDownTrapEnable"]["type"] = "Property"
                interface_dict_buffer["linkUpDownTrapEnable"]["value"] = element_text
                if observed_at is not None:
                    interface_dict_buffer["linkUpDownTrapEnable"]["observedAt"] = observed_at
            ipv4 = interface.get("ietf-ip:ipv4")
            if ipv4 is not None and len(ipv4) != 0:
                interface_ipv4_dict_buffer = {}
                interface_ipv4_dict_buffer["id"] = "urn:ngsi-ld:InterfaceIpv4:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
                interface_ipv4_dict_buffer["type"] = "InterfaceIpv4"
                interface_ipv4_dict_buffer["isPartOf"] = {}
                interface_ipv4_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_ipv4_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                if observed_at is not None:
                    interface_ipv4_dict_buffer["isPartOf"]["observedAt"] = observed_at
                enabled = ipv4.get("enabled")
                if enabled is not None:
                    element_text = enabled
                    interface_ipv4_dict_buffer["enabled"] = {}
                    interface_ipv4_dict_buffer["enabled"]["type"] = "Property"
                    interface_ipv4_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                    if observed_at is not None:
                        interface_ipv4_dict_buffer["enabled"]["observedAt"] = observed_at
                forwarding = ipv4.get("forwarding")
                if forwarding is not None:
                    element_text = forwarding
                    interface_ipv4_dict_buffer["forwarding"] = {}
                    interface_ipv4_dict_buffer["forwarding"]["type"] = "Property"
                    interface_ipv4_dict_buffer["forwarding"]["value"] = eval(str(element_text).capitalize())
                    if observed_at is not None:
                        interface_ipv4_dict_buffer["forwarding"]["observedAt"] = observed_at
                mtu = ipv4.get("mtu")
                if mtu is not None:
                    element_text = mtu
                    interface_ipv4_dict_buffer["mtu"] = {}
                    interface_ipv4_dict_buffer["mtu"]["type"] = "Property"
                    interface_ipv4_dict_buffer["mtu"]["value"] = int(element_text)
                    if observed_at is not None:
                        interface_ipv4_dict_buffer["mtu"]["observedAt"] = observed_at
                ipv4_address = ipv4.get("address")
                if ipv4_address is not None and len(ipv4_address) != 0:
                    for address in ipv4_address:
                        interface_ipv4_address_dict_buffer = {}
                        interface_ipv4_address_dict_buffer["id"] = "urn:ngsi-ld:InterfaceIpv4Address:" + ":".join(interface_ipv4_dict_buffer["id"].split(":")[3:])
                        interface_ipv4_address_dict_buffer["type"] = "InterfaceIpv4Address"
                        interface_ipv4_address_dict_buffer["isPartOf"] = {}
                        interface_ipv4_address_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_ipv4_address_dict_buffer["isPartOf"]["object"] = interface_ipv4_dict_buffer["id"]
                        if observed_at is not None:
                            interface_ipv4_address_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        ip = address.get("ip")
                        if ip is not None:
                            element_text = ip
                            interface_ipv4_address_dict_buffer["ip"] = {}
                            interface_ipv4_address_dict_buffer["ip"]["type"] = "Property"
                            interface_ipv4_address_dict_buffer["ip"]["value"] = element_text
                            if observed_at is not None:
                                interface_ipv4_address_dict_buffer["ip"]["observedAt"] = observed_at
                        prefixLength = address.get("prefix-length")
                        if prefixLength is not None:
                            element_text = prefixLength
                            interface_ipv4_address_dict_buffer["prefixLength"] = {}
                            interface_ipv4_address_dict_buffer["prefixLength"]["type"] = "Property"
                            interface_ipv4_address_dict_buffer["prefixLength"]["value"] = int(element_text)
                            if observed_at is not None:
                                interface_ipv4_address_dict_buffer["prefixLength"]["observedAt"] = observed_at
                        netmask = address.get("netmask")
                        if netmask is not None:
                            element_text = netmask
                            interface_ipv4_address_dict_buffer["netmask"] = {}
                            interface_ipv4_address_dict_buffer["netmask"]["type"] = "Property"
                            interface_ipv4_address_dict_buffer["netmask"]["value"] = element_text
                            if observed_at is not None:
                                interface_ipv4_address_dict_buffer["netmask"]["observedAt"] = observed_at
                        dict_buffers.append(interface_ipv4_address_dict_buffer)
                ipv4_neighbor = ipv4.get("neighbor")
                if ipv4_neighbor is not None and len(ipv4_neighbor) != 0:
                    for neighbor in ipv4_neighbor:
                        interface_ipv4_neighbor_dict_buffer = {}
                        interface_ipv4_neighbor_dict_buffer["id"] = "urn:ngsi-ld:InterfaceIpv4Neighbor:" + ":".join(interface_ipv4_dict_buffer["id"].split(":")[3:])
                        interface_ipv4_neighbor_dict_buffer["type"] = "InterfaceIpv4Neighbor"
                        interface_ipv4_neighbor_dict_buffer["isPartOf"] = {}
                        interface_ipv4_neighbor_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_ipv4_neighbor_dict_buffer["isPartOf"]["object"] = interface_ipv4_dict_buffer["id"]
                        if observed_at is not None:
                            interface_ipv4_neighbor_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        ip = neighbor.get("ip")
                        if ip is not None:
                            element_text = ip
                            interface_ipv4_neighbor_dict_buffer["ip"] = {}
                            interface_ipv4_neighbor_dict_buffer["ip"]["type"] = "Property"
                            interface_ipv4_neighbor_dict_buffer["ip"]["value"] = element_text
                            if observed_at is not None:
                                interface_ipv4_neighbor_dict_buffer["ip"]["observedAt"] = observed_at
                        linkLayerAddress = neighbor.get("link-layer-address")
                        if linkLayerAddress is not None:
                            element_text = linkLayerAddress
                            interface_ipv4_neighbor_dict_buffer["linkLayerAddress"] = {}
                            interface_ipv4_neighbor_dict_buffer["linkLayerAddress"]["type"] = "Property"
                            interface_ipv4_neighbor_dict_buffer["linkLayerAddress"]["value"] = element_text
                            if observed_at is not None:
                                interface_ipv4_neighbor_dict_buffer["linkLayerAddress"]["observedAt"] = observed_at
                        dict_buffers.append(interface_ipv4_neighbor_dict_buffer)
                dict_buffers.append(interface_ipv4_dict_buffer)
            ipv6 = interface.get("ietf-ip:ipv6")
            if ipv6 is not None and len(ipv6) != 0:
                interface_ipv6_dict_buffer = {}
                interface_ipv6_dict_buffer["id"] = "urn:ngsi-ld:InterfaceIpv6:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
                interface_ipv6_dict_buffer["type"] = "InterfaceIpv6"
                interface_ipv6_dict_buffer["isPartOf"] = {}
                interface_ipv6_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_ipv6_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                if observed_at is not None:
                    interface_ipv6_dict_buffer["isPartOf"]["observedAt"] = observed_at
                enabled = ipv6.get("enabled")
                if enabled is not None:
                    element_text = enabled
                    interface_ipv6_dict_buffer["enabled"] = {}
                    interface_ipv6_dict_buffer["enabled"]["type"] = "Property"
                    interface_ipv6_dict_buffer["enabled"]["value"] = eval(str(element_text).capitalize())
                    if observed_at is not None:
                        interface_ipv6_dict_buffer["enabled"]["observedAt"] = observed_at
                forwarding = ipv6.get("forwarding")
                if forwarding is not None:
                    element_text = forwarding
                    interface_ipv6_dict_buffer["forwarding"] = {}
                    interface_ipv6_dict_buffer["forwarding"]["type"] = "Property"
                    interface_ipv6_dict_buffer["forwarding"]["value"] = eval(str(element_text).capitalize())
                    if observed_at is not None:
                        interface_ipv6_dict_buffer["forwarding"]["observedAt"] = observed_at
                mtu = ipv6.get("mtu")
                if mtu is not None:
                    element_text = mtu
                    interface_ipv6_dict_buffer["mtu"] = {}
                    interface_ipv6_dict_buffer["mtu"]["type"] = "Property"
                    interface_ipv6_dict_buffer["mtu"]["value"] = int(element_text)
                    if observed_at is not None:
                        interface_ipv6_dict_buffer["mtu"]["observedAt"] = observed_at
                ipv6_address = ipv6.get("address")
                if ipv6_address is not None and len(ipv6_address) != 0:
                    for address in ipv6_address:
                        interface_ipv6_address_dict_buffer = {}
                        interface_ipv6_address_dict_buffer["id"] = "urn:ngsi-ld:InterfaceIpv6Address:" + ":".join(interface_ipv6_dict_buffer["id"].split(":")[3:])
                        interface_ipv6_address_dict_buffer["type"] = "InterfaceIpv6Address"
                        interface_ipv6_address_dict_buffer["isPartOf"] = {}
                        interface_ipv6_address_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_ipv6_address_dict_buffer["isPartOf"]["object"] = interface_ipv6_dict_buffer["id"]
                        if observed_at is not None:
                            interface_ipv6_address_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        ip = address.get("ip")
                        if ip is not None:
                            element_text = ip
                            interface_ipv6_address_dict_buffer["ip"] = {}
                            interface_ipv6_address_dict_buffer["ip"]["type"] = "Property"
                            interface_ipv6_address_dict_buffer["ip"]["value"] = element_text
                            if observed_at is not None:
                                interface_ipv6_address_dict_buffer["ip"]["observedAt"] = observed_at
                        prefixLength = address.get("prefix-length")
                        if prefixLength is not None:
                            element_text = prefixLength
                            interface_ipv6_address_dict_buffer["prefixLength"] = {}
                            interface_ipv6_address_dict_buffer["prefixLength"]["type"] = "Property"
                            interface_ipv6_address_dict_buffer["prefixLength"]["value"] = int(element_text)
                            if observed_at is not None:
                                interface_ipv6_address_dict_buffer["prefixLength"]["observedAt"] = observed_at
                        dict_buffers.append(interface_ipv6_address_dict_buffer)
                ipv6_neighbor = ipv6.get("neighbor")
                if ipv6_neighbor is not None and len(ipv6_neighbor) != 0:
                    for neighbor in ipv6_neighbor:
                        interface_ipv6_neighbor_dict_buffer = {}
                        interface_ipv6_neighbor_dict_buffer["id"] = "urn:ngsi-ld:InterfaceIpv6Neighbor:" + ":".join(interface_ipv6_dict_buffer["id"].split(":")[3:])
                        interface_ipv6_neighbor_dict_buffer["type"] = "InterfaceIpv6Neighbor"
                        interface_ipv6_neighbor_dict_buffer["isPartOf"] = {}
                        interface_ipv6_neighbor_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_ipv6_neighbor_dict_buffer["isPartOf"]["object"] = interface_ipv6_dict_buffer["id"]
                        if observed_at is not None:
                            interface_ipv6_neighbor_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        ip = neighbor.get("ip")
                        if ip is not None:
                            element_text = ip
                            interface_ipv6_neighbor_dict_buffer["ip"] = {}
                            interface_ipv6_neighbor_dict_buffer["ip"]["type"] = "Property"
                            interface_ipv6_neighbor_dict_buffer["ip"]["value"] = element_text
                            if observed_at is not None:
                                interface_ipv6_neighbor_dict_buffer["ip"]["observedAt"] = observed_at
                        linkLayerAddress = neighbor.get("link-layer-address")
                        if linkLayerAddress is not None:
                            element_text = linkLayerAddress
                            interface_ipv6_neighbor_dict_buffer["linkLayerAddress"] = {}
                            interface_ipv6_neighbor_dict_buffer["linkLayerAddress"]["type"] = "Property"
                            interface_ipv6_neighbor_dict_buffer["linkLayerAddress"]["value"] = element_text
                            if observed_at is not None:
                                interface_ipv6_neighbor_dict_buffer["linkLayerAddress"]["observedAt"] = observed_at
                        dict_buffers.append(interface_ipv6_neighbor_dict_buffer)
                dupAddrDetectTransmits = ipv6.get("dup-addr-detect-transmits")
                if dupAddrDetectTransmits is not None:
                    element_text = dupAddrDetectTransmits
                    interface_ipv6_dict_buffer["dupAddrDetectTransmits"] = {}
                    interface_ipv6_dict_buffer["dupAddrDetectTransmits"]["type"] = "Property"
                    interface_ipv6_dict_buffer["dupAddrDetectTransmits"]["value"] = int(element_text)
                    if observed_at is not None:
                        interface_ipv6_dict_buffer["dupAddrDetectTransmits"]["observedAt"] = observed_at
                autoconf = ipv6.get("autoconf")
                if autoconf is not None and len(autoconf) != 0:
                    interface_ipv6_autoconf_dict_buffer = {}
                    interface_ipv6_autoconf_dict_buffer["id"] = "urn:ngsi-ld:InterfaceIpv6Autoconf:" + ":".join(interface_ipv6_dict_buffer["id"].split(":")[3:])
                    interface_ipv6_autoconf_dict_buffer["type"] = "InterfaceIpv6Autoconf"
                    interface_ipv6_autoconf_dict_buffer["isPartOf"] = {}
                    interface_ipv6_autoconf_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_ipv6_autoconf_dict_buffer["isPartOf"]["object"] = interface_ipv6_dict_buffer["id"]
                    if observed_at is not None:
                        interface_ipv6_autoconf_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    createGlobalAddresses = autoconf.get("create-global-addresses")
                    if createGlobalAddresses is not None:
                        element_text = createGlobalAddresses
                        interface_ipv6_autoconf_dict_buffer["createGlobalAddresses"] = {}
                        interface_ipv6_autoconf_dict_buffer["createGlobalAddresses"]["type"] = "Property"
                        interface_ipv6_autoconf_dict_buffer["createGlobalAddresses"]["value"] = eval(str(element_text).capitalize())
                        if observed_at is not None:
                            interface_ipv6_autoconf_dict_buffer["createGlobalAddresses"]["observedAt"] = observed_at
                    createTemporaryAddresses = autoconf.get("create-temporary-addresses")
                    if createTemporaryAddresses is not None:
                        element_text = createTemporaryAddresses
                        interface_ipv6_autoconf_dict_buffer["createTemporaryAddresses"] = {}
                        interface_ipv6_autoconf_dict_buffer["createTemporaryAddresses"]["type"] = "Property"
                        interface_ipv6_autoconf_dict_buffer["createTemporaryAddresses"]["value"] = eval(str(element_text).capitalize())
                        if observed_at is not None:
                            interface_ipv6_autoconf_dict_buffer["createTemporaryAddresses"]["observedAt"] = observed_at
                    temporaryValidLifetime = autoconf.get("temporary-valid-lifetime")
                    if temporaryValidLifetime is not None:
                        element_text = temporaryValidLifetime
                        if interface_ipv6_autoconf_dict_buffer["id"].split(":")[-1] != int(element_text):
                            interface_ipv6_autoconf_dict_buffer["id"] = interface_ipv6_autoconf_dict_buffer["id"] + ":" + str(element_text)
                        interface_ipv6_autoconf_dict_buffer["temporaryValidLifetime"] = {}
                        interface_ipv6_autoconf_dict_buffer["temporaryValidLifetime"]["type"] = "Property"
                        interface_ipv6_autoconf_dict_buffer["temporaryValidLifetime"]["value"] = int(element_text)
                        if observed_at is not None:
                            interface_ipv6_autoconf_dict_buffer["temporaryValidLifetime"]["observedAt"] = observed_at
                    temporaryPreferredLifetime = autoconf.get("temporary-preferred-lifetime")
                    if temporaryPreferredLifetime is not None:
                        element_text = temporaryPreferredLifetime
                        interface_ipv6_autoconf_dict_buffer["temporaryPreferredLifetime"] = {}
                        interface_ipv6_autoconf_dict_buffer["temporaryPreferredLifetime"]["type"] = "Property"
                        interface_ipv6_autoconf_dict_buffer["temporaryPreferredLifetime"]["value"] = int(element_text)
                        if observed_at is not None:
                            interface_ipv6_autoconf_dict_buffer["temporaryPreferredLifetime"]["observedAt"] = observed_at
                    dict_buffers.append(interface_ipv6_autoconf_dict_buffer)
                dict_buffers.append(interface_ipv6_dict_buffer)
            dict_buffers.append(interface_dict_buffer)
if data.get("interfaces-state") is not None:
    interfaces_state = data.get("interfaces-state")
elif data.get("ietf-interfaces:interfaces-state") is not None:
    interfaces_state = data.get("ietf-interfaces:interfaces-state")
else:
    interfaces_state = None
if interfaces_state is not None and len(interfaces_state) != 0:
    if "interface" in list(interfaces_state.keys()):
        interfaces_state = interfaces_state.get("interface")
    elif "ietf-interfaces:interface" in list(interfaces_state.keys()):
        interfaces_state = interfaces_state.get("ietf-interfaces:interface")
    for interface in interfaces_state:
        if interface is not None and len(interface) != 0:
            interface_dict_buffer = {}
            interface_dict_buffer["id"] = "urn:ngsi-ld:Interface"
            interface_dict_buffer["type"] = "Interface"
            name = interface.get("name")
            if name is not None:
                element_text = name
                if interface_dict_buffer["id"].split(":")[-1] != element_text:
                    interface_dict_buffer["id"] = interface_dict_buffer["id"] + ":" + str(element_text)
                interface_dict_buffer["name"] = {}
                interface_dict_buffer["name"]["type"] = "Property"
                interface_dict_buffer["name"]["value"] = element_text
                if observed_at is not None:
                    interface_dict_buffer["name"]["observedAt"] = observed_at
            type = interface.get("type")
            if type is not None and len(type) != 0:
                element_text = type
                if element_text is not None:
                    interface_dict_buffer["interfaceType"] = {}
                    interface_dict_buffer["interfaceType"]["type"] = "Relationship"
                    interface_dict_buffer["interfaceType"]["object"] = "urn:ngsi-ld:YANGIdentity:" + element_text
                    if observed_at is not None:
                        interface_dict_buffer["interfaceType"]["observedAt"] = observed_at
            adminStatus = interface.get("admin-status")
            if adminStatus is not None:
                element_text = adminStatus
                interface_dict_buffer["adminStatus"] = {}
                interface_dict_buffer["adminStatus"]["type"] = "Property"
                interface_dict_buffer["adminStatus"]["value"] = element_text
                if observed_at is not None:
                    interface_dict_buffer["adminStatus"]["observedAt"] = observed_at
            operStatus = interface.get("oper-status")
            if operStatus is not None:
                element_text = operStatus
                interface_dict_buffer["operStatus"] = {}
                interface_dict_buffer["operStatus"]["type"] = "Property"
                interface_dict_buffer["operStatus"]["value"] = element_text
                if observed_at is not None:
                    interface_dict_buffer["operStatus"]["observedAt"] = observed_at
            lastChange = interface.get("last-change")
            if lastChange is not None:
                element_text = lastChange
                interface_dict_buffer["lastChange"] = {}
                interface_dict_buffer["lastChange"]["type"] = "Property"
                interface_dict_buffer["lastChange"]["value"] = element_text
                if observed_at is not None:
                    interface_dict_buffer["lastChange"]["observedAt"] = observed_at
            ifIndex = interface.get("if-index")
            if ifIndex is not None:
                element_text = ifIndex
                interface_dict_buffer["ifIndex"] = {}
                interface_dict_buffer["ifIndex"]["type"] = "Property"
                interface_dict_buffer["ifIndex"]["value"] = int(element_text)
                if observed_at is not None:
                    interface_dict_buffer["ifIndex"]["observedAt"] = observed_at
            physAddress = interface.get("phys-address")
            if physAddress is not None:
                element_text = physAddress
                interface_dict_buffer["physAddress"] = {}
                interface_dict_buffer["physAddress"]["type"] = "Property"
                interface_dict_buffer["physAddress"]["value"] = element_text
                if observed_at is not None:
                    interface_dict_buffer["physAddress"]["observedAt"] = observed_at
            higherLayerIf = interface.get("higher-layer-if")
            if higherLayerIf is not None:
                element_text = higherLayerIf
                interface_dict_buffer["higherLayerIf"] = {}
                interface_dict_buffer["higherLayerIf"]["type"] = "Relationship"
                interface_dict_buffer["higherLayerIf"]["object"] = "urn:ngsi-ld:Interface:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
                if observed_at is not None:
                    interface_dict_buffer["higherLayerIf"]["observedAt"] = observed_at
            lowerLayerIf = interface.get("lower-layer-if")
            if lowerLayerIf is not None:
                element_text = lowerLayerIf
                interface_dict_buffer["lowerLayerIf"] = {}
                interface_dict_buffer["lowerLayerIf"]["type"] = "Relationship"
                interface_dict_buffer["lowerLayerIf"]["object"] = "urn:ngsi-ld:Interface:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
                if observed_at is not None:
                    interface_dict_buffer["lowerLayerIf"]["observedAt"] = observed_at
            speed = interface.get("speed")
            if speed is not None:
                element_text = speed
                interface_dict_buffer["speed"] = {}
                interface_dict_buffer["speed"]["type"] = "Property"
                interface_dict_buffer["speed"]["value"] = int(element_text)
                if observed_at is not None:
                    interface_dict_buffer["speed"]["observedAt"] = observed_at
            statistics = interface.get("statistics")
            if statistics is not None and len(statistics) != 0:
                interface_statistics_dict_buffer = {}
                interface_statistics_dict_buffer["id"] = "urn:ngsi-ld:InterfaceStatistics:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
                interface_statistics_dict_buffer["type"] = "InterfaceStatistics"
                interface_statistics_dict_buffer["isPartOf"] = {}
                interface_statistics_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_statistics_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                if observed_at is not None:
                    interface_statistics_dict_buffer["isPartOf"]["observedAt"] = observed_at
                discontinuityTime = statistics.get("discontinuity-time")
                if discontinuityTime is not None:
                    element_text = discontinuityTime
                    interface_statistics_dict_buffer["discontinuityTime"] = {}
                    interface_statistics_dict_buffer["discontinuityTime"]["type"] = "Property"
                    interface_statistics_dict_buffer["discontinuityTime"]["value"] = element_text
                    if observed_at is not None:
                        interface_statistics_dict_buffer["discontinuityTime"]["observedAt"] = observed_at
                inOctets = statistics.get("in-octets")
                if inOctets is not None:
                    element_text = inOctets
                    interface_statistics_dict_buffer["inOctets"] = {}
                    interface_statistics_dict_buffer["inOctets"]["type"] = "Property"
                    interface_statistics_dict_buffer["inOctets"]["value"] = int(element_text)
                    if observed_at is not None:
                        interface_statistics_dict_buffer["inOctets"]["observedAt"] = observed_at
                inUnicastPkts = statistics.get("in-unicast-pkts")
                if inUnicastPkts is not None:
                    element_text = inUnicastPkts
                    interface_statistics_dict_buffer["inUnicastPkts"] = {}
                    interface_statistics_dict_buffer["inUnicastPkts"]["type"] = "Property"
                    interface_statistics_dict_buffer["inUnicastPkts"]["value"] = int(element_text)
                    if observed_at is not None:
                        interface_statistics_dict_buffer["inUnicastPkts"]["observedAt"] = observed_at
                inBroadcastPkts = statistics.get("in-broadcast-pkts")
                if inBroadcastPkts is not None:
                    element_text = inBroadcastPkts
                    interface_statistics_dict_buffer["inBroadcastPkts"] = {}
                    interface_statistics_dict_buffer["inBroadcastPkts"]["type"] = "Property"
                    interface_statistics_dict_buffer["inBroadcastPkts"]["value"] = int(element_text)
                    if observed_at is not None:
                        interface_statistics_dict_buffer["inBroadcastPkts"]["observedAt"] = observed_at
                inMulticastPkts = statistics.get("in-multicast-pkts")
                if inMulticastPkts is not None:
                    element_text = inMulticastPkts
                    interface_statistics_dict_buffer["inMulticastPkts"] = {}
                    interface_statistics_dict_buffer["inMulticastPkts"]["type"] = "Property"
                    interface_statistics_dict_buffer["inMulticastPkts"]["value"] = int(element_text)
                    if observed_at is not None:
                        interface_statistics_dict_buffer["inMulticastPkts"]["observedAt"] = observed_at
                inDiscards = statistics.get("in-discards")
                if inDiscards is not None:
                    element_text = inDiscards
                    interface_statistics_dict_buffer["inDiscards"] = {}
                    interface_statistics_dict_buffer["inDiscards"]["type"] = "Property"
                    interface_statistics_dict_buffer["inDiscards"]["value"] = int(element_text)
                    if observed_at is not None:
                        interface_statistics_dict_buffer["inDiscards"]["observedAt"] = observed_at
                inErrors = statistics.get("in-errors")
                if inErrors is not None:
                    element_text = inErrors
                    interface_statistics_dict_buffer["inErrors"] = {}
                    interface_statistics_dict_buffer["inErrors"]["type"] = "Property"
                    interface_statistics_dict_buffer["inErrors"]["value"] = int(element_text)
                    if observed_at is not None:
                        interface_statistics_dict_buffer["inErrors"]["observedAt"] = observed_at
                inUnknownProtos = statistics.get("in-unknown-protos")
                if inUnknownProtos is not None:
                    element_text = inUnknownProtos
                    interface_statistics_dict_buffer["inUnknownProtos"] = {}
                    interface_statistics_dict_buffer["inUnknownProtos"]["type"] = "Property"
                    interface_statistics_dict_buffer["inUnknownProtos"]["value"] = int(element_text)
                    if observed_at is not None:
                        interface_statistics_dict_buffer["inUnknownProtos"]["observedAt"] = observed_at
                outOctets = statistics.get("out-octets")
                if outOctets is not None:
                    element_text = outOctets
                    interface_statistics_dict_buffer["outOctets"] = {}
                    interface_statistics_dict_buffer["outOctets"]["type"] = "Property"
                    interface_statistics_dict_buffer["outOctets"]["value"] = int(element_text)
                    if observed_at is not None:
                        interface_statistics_dict_buffer["outOctets"]["observedAt"] = observed_at
                outUnicastPkts = statistics.get("out-unicast-pkts")
                if outUnicastPkts is not None:
                    element_text = outUnicastPkts
                    interface_statistics_dict_buffer["outUnicastPkts"] = {}
                    interface_statistics_dict_buffer["outUnicastPkts"]["type"] = "Property"
                    interface_statistics_dict_buffer["outUnicastPkts"]["value"] = int(element_text)
                    if observed_at is not None:
                        interface_statistics_dict_buffer["outUnicastPkts"]["observedAt"] = observed_at
                outBroadcastPkts = statistics.get("out-broadcast-pkts")
                if outBroadcastPkts is not None:
                    element_text = outBroadcastPkts
                    interface_statistics_dict_buffer["outBroadcastPkts"] = {}
                    interface_statistics_dict_buffer["outBroadcastPkts"]["type"] = "Property"
                    interface_statistics_dict_buffer["outBroadcastPkts"]["value"] = int(element_text)
                    if observed_at is not None:
                        interface_statistics_dict_buffer["outBroadcastPkts"]["observedAt"] = observed_at
                outMulticastPkts = statistics.get("out-multicast-pkts")
                if outMulticastPkts is not None:
                    element_text = outMulticastPkts
                    interface_statistics_dict_buffer["outMulticastPkts"] = {}
                    interface_statistics_dict_buffer["outMulticastPkts"]["type"] = "Property"
                    interface_statistics_dict_buffer["outMulticastPkts"]["value"] = int(element_text)
                    if observed_at is not None:
                        interface_statistics_dict_buffer["outMulticastPkts"]["observedAt"] = observed_at
                outDiscards = statistics.get("out-discards")
                if outDiscards is not None:
                    element_text = outDiscards
                    interface_statistics_dict_buffer["outDiscards"] = {}
                    interface_statistics_dict_buffer["outDiscards"]["type"] = "Property"
                    interface_statistics_dict_buffer["outDiscards"]["value"] = int(element_text)
                    if observed_at is not None:
                        interface_statistics_dict_buffer["outDiscards"]["observedAt"] = observed_at
                outErrors = statistics.get("out-errors")
                if outErrors is not None:
                    element_text = outErrors
                    interface_statistics_dict_buffer["outErrors"] = {}
                    interface_statistics_dict_buffer["outErrors"]["type"] = "Property"
                    interface_statistics_dict_buffer["outErrors"]["value"] = int(element_text)
                    if observed_at is not None:
                        interface_statistics_dict_buffer["outErrors"]["observedAt"] = observed_at
                dict_buffers.append(interface_statistics_dict_buffer)
            ipv4 = interface.get("ietf-ip:ipv4")
            if ipv4 is not None and len(ipv4) != 0:
                interface_ipv4_dict_buffer = {}
                interface_ipv4_dict_buffer["id"] = "urn:ngsi-ld:InterfaceIpv4:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
                interface_ipv4_dict_buffer["type"] = "InterfaceIpv4"
                interface_ipv4_dict_buffer["isPartOf"] = {}
                interface_ipv4_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_ipv4_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                if observed_at is not None:
                    interface_ipv4_dict_buffer["isPartOf"]["observedAt"] = observed_at
                forwarding = ipv4.get("forwarding")
                if forwarding is not None:
                    element_text = forwarding
                    interface_ipv4_dict_buffer["forwarding"] = {}
                    interface_ipv4_dict_buffer["forwarding"]["type"] = "Property"
                    interface_ipv4_dict_buffer["forwarding"]["value"] = eval(str(element_text).capitalize())
                    if observed_at is not None:
                        interface_ipv4_dict_buffer["forwarding"]["observedAt"] = observed_at
                mtu = ipv4.get("mtu")
                if mtu is not None:
                    element_text = mtu
                    interface_ipv4_dict_buffer["mtu"] = {}
                    interface_ipv4_dict_buffer["mtu"]["type"] = "Property"
                    interface_ipv4_dict_buffer["mtu"]["value"] = int(element_text)
                    if observed_at is not None:
                        interface_ipv4_dict_buffer["mtu"]["observedAt"] = observed_at
                ipv4_address = ipv4.get("address")
                if ipv4_address is not None and len(ipv4_address) != 0:
                    for address in ipv4_address:
                        interface_ipv4_address_dict_buffer = {}
                        interface_ipv4_address_dict_buffer["id"] = "urn:ngsi-ld:InterfaceIpv4Address:" + ":".join(interface_ipv4_dict_buffer["id"].split(":")[3:])
                        interface_ipv4_address_dict_buffer["type"] = "InterfaceIpv4Address"
                        interface_ipv4_address_dict_buffer["isPartOf"] = {}
                        interface_ipv4_address_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_ipv4_address_dict_buffer["isPartOf"]["object"] = interface_ipv4_dict_buffer["id"]
                        if observed_at is not None:
                            interface_ipv4_address_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        ip = address.get("ip")
                        if ip is not None:
                            element_text = ip
                            interface_ipv4_address_dict_buffer["ip"] = {}
                            interface_ipv4_address_dict_buffer["ip"]["type"] = "Property"
                            interface_ipv4_address_dict_buffer["ip"]["value"] = element_text
                            if observed_at is not None:
                                interface_ipv4_address_dict_buffer["ip"]["observedAt"] = observed_at
                        prefixLength = address.get("prefix-length")
                        if prefixLength is not None:
                            element_text = prefixLength
                            interface_ipv4_address_dict_buffer["prefixLength"] = {}
                            interface_ipv4_address_dict_buffer["prefixLength"]["type"] = "Property"
                            interface_ipv4_address_dict_buffer["prefixLength"]["value"] = int(element_text)
                            if observed_at is not None:
                                interface_ipv4_address_dict_buffer["prefixLength"]["observedAt"] = observed_at
                        netmask = address.get("netmask")
                        if netmask is not None:
                            element_text = netmask
                            interface_ipv4_address_dict_buffer["netmask"] = {}
                            interface_ipv4_address_dict_buffer["netmask"]["type"] = "Property"
                            interface_ipv4_address_dict_buffer["netmask"]["value"] = element_text
                            if observed_at is not None:
                                interface_ipv4_address_dict_buffer["netmask"]["observedAt"] = observed_at
                        origin = address.get("origin")
                        if origin is not None:
                            element_text = origin
                            interface_ipv4_address_dict_buffer["origin"] = {}
                            interface_ipv4_address_dict_buffer["origin"]["type"] = "Property"
                            interface_ipv4_address_dict_buffer["origin"]["value"] = element_text
                            if observed_at is not None:
                                interface_ipv4_address_dict_buffer["origin"]["observedAt"] = observed_at
                        dict_buffers.append(interface_ipv4_address_dict_buffer)
                ipv4_neighbor = ipv4.get("neighbor")
                if ipv4_neighbor is not None and len(ipv4_neighbor) != 0:
                    for neighbor in ipv4_neighbor:
                        interface_ipv4_neighbor_dict_buffer = {}
                        interface_ipv4_neighbor_dict_buffer["id"] = "urn:ngsi-ld:InterfaceIpv4Neighbor:" + ":".join(interface_ipv4_dict_buffer["id"].split(":")[3:])
                        interface_ipv4_neighbor_dict_buffer["type"] = "InterfaceIpv4Neighbor"
                        interface_ipv4_neighbor_dict_buffer["isPartOf"] = {}
                        interface_ipv4_neighbor_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_ipv4_neighbor_dict_buffer["isPartOf"]["object"] = interface_ipv4_dict_buffer["id"]
                        if observed_at is not None:
                            interface_ipv4_neighbor_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        ip = neighbor.get("ip")
                        if ip is not None:
                            element_text = ip
                            interface_ipv4_neighbor_dict_buffer["ip"] = {}
                            interface_ipv4_neighbor_dict_buffer["ip"]["type"] = "Property"
                            interface_ipv4_neighbor_dict_buffer["ip"]["value"] = element_text
                            if observed_at is not None:
                                interface_ipv4_neighbor_dict_buffer["ip"]["observedAt"] = observed_at
                        linkLayerAddress = neighbor.get("link-layer-address")
                        if linkLayerAddress is not None:
                            element_text = linkLayerAddress
                            interface_ipv4_neighbor_dict_buffer["linkLayerAddress"] = {}
                            interface_ipv4_neighbor_dict_buffer["linkLayerAddress"]["type"] = "Property"
                            interface_ipv4_neighbor_dict_buffer["linkLayerAddress"]["value"] = element_text
                            if observed_at is not None:
                                interface_ipv4_neighbor_dict_buffer["linkLayerAddress"]["observedAt"] = observed_at
                        origin = neighbor.get("origin")
                        if origin is not None:
                            element_text = origin
                            interface_ipv4_neighbor_dict_buffer["origin"] = {}
                            interface_ipv4_neighbor_dict_buffer["origin"]["type"] = "Property"
                            interface_ipv4_neighbor_dict_buffer["origin"]["value"] = element_text
                            if observed_at is not None:
                                interface_ipv4_neighbor_dict_buffer["origin"]["observedAt"] = observed_at
                        dict_buffers.append(interface_ipv4_neighbor_dict_buffer)
                dict_buffers.append(interface_ipv4_dict_buffer)
            ipv6 = interface.get("ietf-ip:ipv6")
            if ipv6 is not None and len(ipv6) != 0:
                interface_ipv6_dict_buffer = {}
                interface_ipv6_dict_buffer["id"] = "urn:ngsi-ld:InterfaceIpv6:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
                interface_ipv6_dict_buffer["type"] = "InterfaceIpv6"
                interface_ipv6_dict_buffer["isPartOf"] = {}
                interface_ipv6_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_ipv6_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
                if observed_at is not None:
                    interface_ipv6_dict_buffer["isPartOf"]["observedAt"] = observed_at
                forwarding = ipv6.get("forwarding")
                if forwarding is not None:
                    element_text = forwarding
                    interface_ipv6_dict_buffer["forwarding"] = {}
                    interface_ipv6_dict_buffer["forwarding"]["type"] = "Property"
                    interface_ipv6_dict_buffer["forwarding"]["value"] = eval(str(element_text).capitalize())
                    if observed_at is not None:
                        interface_ipv6_dict_buffer["forwarding"]["observedAt"] = observed_at
                mtu = ipv6.get("mtu")
                if mtu is not None:
                    element_text = mtu
                    interface_ipv6_dict_buffer["mtu"] = {}
                    interface_ipv6_dict_buffer["mtu"]["type"] = "Property"
                    interface_ipv6_dict_buffer["mtu"]["value"] = int(element_text)
                    if observed_at is not None:
                        interface_ipv6_dict_buffer["mtu"]["observedAt"] = observed_at
                ipv6_address = ipv6.get("address")
                if ipv6_address is not None and len(ipv6_address) != 0:
                    for address in ipv6_address:
                        interface_ipv6_address_dict_buffer = {}
                        interface_ipv6_address_dict_buffer["id"] = "urn:ngsi-ld:InterfaceIpv6Address:" + ":".join(interface_ipv6_dict_buffer["id"].split(":")[3:])
                        interface_ipv6_address_dict_buffer["type"] = "InterfaceIpv6Address"
                        interface_ipv6_address_dict_buffer["isPartOf"] = {}
                        interface_ipv6_address_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_ipv6_address_dict_buffer["isPartOf"]["object"] = interface_ipv6_dict_buffer["id"]
                        if observed_at is not None:
                            interface_ipv6_address_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        ip = address.get("ip")
                        if ip is not None:
                            element_text = ip
                            interface_ipv6_address_dict_buffer["ip"] = {}
                            interface_ipv6_address_dict_buffer["ip"]["type"] = "Property"
                            interface_ipv6_address_dict_buffer["ip"]["value"] = element_text
                            if observed_at is not None:
                                interface_ipv6_address_dict_buffer["ip"]["observedAt"] = observed_at
                        prefixLength = address.get("prefix-length")
                        if prefixLength is not None:
                            element_text = prefixLength
                            interface_ipv6_address_dict_buffer["prefixLength"] = {}
                            interface_ipv6_address_dict_buffer["prefixLength"]["type"] = "Property"
                            interface_ipv6_address_dict_buffer["prefixLength"]["value"] = int(element_text)
                            if observed_at is not None:
                                interface_ipv6_address_dict_buffer["prefixLength"]["observedAt"] = observed_at
                        origin = address.get("origin")
                        if origin is not None:
                            element_text = origin
                            interface_ipv6_address_dict_buffer["origin"] = {}
                            interface_ipv6_address_dict_buffer["origin"]["type"] = "Property"
                            interface_ipv6_address_dict_buffer["origin"]["value"] = element_text
                            if observed_at is not None:
                                interface_ipv6_address_dict_buffer["origin"]["observedAt"] = observed_at
                        status = address.get("status")
                        if status is not None:
                            element_text = status
                            interface_ipv6_address_dict_buffer["status"] = {}
                            interface_ipv6_address_dict_buffer["status"]["type"] = "Property"
                            interface_ipv6_address_dict_buffer["status"]["value"] = element_text
                            if observed_at is not None:
                                interface_ipv6_address_dict_buffer["status"]["observedAt"] = observed_at
                        dict_buffers.append(interface_ipv6_address_dict_buffer)
                ipv6_neighbor = ipv6.get("neighbor")
                if ipv6_neighbor is not None and len(ipv6_neighbor) != 0:
                    for neighbor in ipv6_neighbor:
                        interface_ipv6_neighbor_dict_buffer = {}
                        interface_ipv6_neighbor_dict_buffer["id"] = "urn:ngsi-ld:InterfaceIpv6Neighbor:" + ":".join(interface_ipv6_dict_buffer["id"].split(":")[3:])
                        interface_ipv6_neighbor_dict_buffer["type"] = "InterfaceIpv6Neighbor"
                        interface_ipv6_neighbor_dict_buffer["isPartOf"] = {}
                        interface_ipv6_neighbor_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_ipv6_neighbor_dict_buffer["isPartOf"]["object"] = interface_ipv6_dict_buffer["id"]
                        if observed_at is not None:
                            interface_ipv6_neighbor_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        ip = neighbor.get("ip")
                        if ip is not None:
                            element_text = ip
                            interface_ipv6_neighbor_dict_buffer["ip"] = {}
                            interface_ipv6_neighbor_dict_buffer["ip"]["type"] = "Property"
                            interface_ipv6_neighbor_dict_buffer["ip"]["value"] = element_text
                            if observed_at is not None:
                                interface_ipv6_neighbor_dict_buffer["ip"]["observedAt"] = observed_at
                        linkLayerAddress = neighbor.get("link-layer-address")
                        if linkLayerAddress is not None:
                            element_text = linkLayerAddress
                            interface_ipv6_neighbor_dict_buffer["linkLayerAddress"] = {}
                            interface_ipv6_neighbor_dict_buffer["linkLayerAddress"]["type"] = "Property"
                            interface_ipv6_neighbor_dict_buffer["linkLayerAddress"]["value"] = element_text
                            if observed_at is not None:
                                interface_ipv6_neighbor_dict_buffer["linkLayerAddress"]["observedAt"] = observed_at
                        origin = neighbor.get("origin")
                        if origin is not None:
                            element_text = origin
                            interface_ipv6_neighbor_dict_buffer["origin"] = {}
                            interface_ipv6_neighbor_dict_buffer["origin"]["type"] = "Property"
                            interface_ipv6_neighbor_dict_buffer["origin"]["value"] = element_text
                            if observed_at is not None:
                                interface_ipv6_neighbor_dict_buffer["origin"]["observedAt"] = observed_at
                        isRouter = neighbor.get("is-router")
                        if isRouter is not None:
                            element_text = isRouter
                            interface_ipv6_neighbor_dict_buffer["isRouter"] = {}
                            interface_ipv6_neighbor_dict_buffer["isRouter"]["type"] = "Property"
                            interface_ipv6_neighbor_dict_buffer["isRouter"]["value"] = element_text
                            if observed_at is not None:
                                interface_ipv6_neighbor_dict_buffer["isRouter"]["observedAt"] = observed_at
                        state = neighbor.get("state")
                        if state is not None:
                            element_text = state
                            interface_ipv6_neighbor_dict_buffer["state"] = {}
                            interface_ipv6_neighbor_dict_buffer["state"]["type"] = "Property"
                            interface_ipv6_neighbor_dict_buffer["state"]["value"] = element_text
                            if observed_at is not None:
                                interface_ipv6_neighbor_dict_buffer["state"]["observedAt"] = observed_at
                        dict_buffers.append(interface_ipv6_neighbor_dict_buffer)
                dict_buffers.append(interface_ipv6_dict_buffer)
            dict_buffers.append(interface_dict_buffer)

output_file = open("dict_buffers.json", 'w')
output_file.write(json.dumps(dict_buffers[::-1], indent=4))
output_file.close()
dict_buffers.clear()
