import sys
import xml.etree.ElementTree as et
import logging
import logging.config
import yaml
import os
import time
import re
import subprocess
import pdb

xml_file = sys.argv[1]
dict_buffers_file = sys.argv[2]
tree = et.parse(xml_file)
root = tree.getroot()

# Store NGSI-LD-compliant data structures (Python dictionaries) in an array.
dict_buffers = []

# Generated parser code includes ietf-interfaces + ietf-ip.

for interface in root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}interface"):
    interface_dict_buffer = {}
    interface_dict_buffer["id"] = "urn:ngsi-ld:Interface:"
    interface_dict_buffer["type"] = "Interface"
    name = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}name")
    if name is not None:
        element_text = name.text
        if element_text is not None:
            interface_dict_buffer["id"] = interface_dict_buffer["id"] + element_text
            interface_dict_buffer["name"] = {}
            interface_dict_buffer["name"]["type"] = "Property"
            interface_dict_buffer["name"]["value"] = element_text
    description = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}description")
    if description is not None:
        element_text = description.text
        if element_text is not None:
            interface_dict_buffer["description"] = {}
            interface_dict_buffer["description"]["type"] = "Property"
            interface_dict_buffer["description"]["value"] = element_text
    enabled = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}enabled")
    if enabled is not None:
        element_text = enabled.text
        if element_text is not None:
            interface_dict_buffer["enabled"] = {}
            interface_dict_buffer["enabled"]["type"] = "Property"
            interface_dict_buffer["enabled"]["value"] = eval(element_text.capitalize())
    linkUpDownTrapEnable = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}link-up-down-trap-enable")
    if linkUpDownTrapEnable is not None:
        element_text = linkUpDownTrapEnable.text
        if element_text is not None:
            interface_dict_buffer["linkUpDownTrapEnable"] = {}
            interface_dict_buffer["linkUpDownTrapEnable"]["type"] = "Property"
            interface_dict_buffer["linkUpDownTrapEnable"]["value"] = element_text
    adminStatus = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}admin-status")
    if adminStatus is not None:
        element_text = adminStatus.text
        if element_text is not None:
            interface_dict_buffer["adminStatus"] = {}
            interface_dict_buffer["adminStatus"]["type"] = "Property"
            interface_dict_buffer["adminStatus"]["value"] = element_text
    operStatus = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}oper-status")
    if operStatus is not None:
        element_text = operStatus.text
        if element_text is not None:
            interface_dict_buffer["operStatus"] = {}
            interface_dict_buffer["operStatus"]["type"] = "Property"
            interface_dict_buffer["operStatus"]["value"] = element_text
    lastChange = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}last-change")
    if lastChange is not None:
        element_text = lastChange.text
        if element_text is not None:
            interface_dict_buffer["lastChange"] = {}
            interface_dict_buffer["lastChange"]["type"] = "Property"
            interface_dict_buffer["lastChange"]["value"] = element_text
    ifIndex = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}if-index")
    if ifIndex is not None:
        element_text = ifIndex.text
        if element_text is not None:
            interface_dict_buffer["ifIndex"] = {}
            interface_dict_buffer["ifIndex"]["type"] = "Property"
            interface_dict_buffer["ifIndex"]["value"] = int(element_text)
    physAddress = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}phys-address")
    if physAddress is not None:
        element_text = physAddress.text
        if element_text is not None:
            interface_dict_buffer["physAddress"] = {}
            interface_dict_buffer["physAddress"]["type"] = "Property"
            interface_dict_buffer["physAddress"]["value"] = element_text
    higherLayerIf = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}higher-layer-if")
    if higherLayerIf is not None:
        element_text = higherLayerIf.text
        if element_text is not None:
            interface_dict_buffer["higherLayerIf"] = {}
            interface_dict_buffer["higherLayerIf"]["type"] = "Relationship"
            interface_dict_buffer["higherLayerIf"]["object"] = "urn:ngsi-ld:Interface:" + element_text
    lowerLayerIf = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}lower-layer-if")
    if lowerLayerIf is not None:
        element_text = lowerLayerIf.text
        if element_text is not None:
            interface_dict_buffer["lowerLayerIf"] = {}
            interface_dict_buffer["lowerLayerIf"]["type"] = "Relationship"
            interface_dict_buffer["lowerLayerIf"]["object"] = "urn:ngsi-ld:Interface:" + element_text
    speed = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}speed")
    if speed is not None:
        element_text = speed.text
        if element_text is not None:
            interface_dict_buffer["speed"] = {}
            interface_dict_buffer["speed"]["type"] = "Property"
            interface_dict_buffer["speed"]["value"] = int(element_text)
    for statistics in interface.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}statistics"):
        interface_statistics_dict_buffer = {}
        interface_statistics_dict_buffer["id"] = "urn:ngsi-ld:Statistics:" + interface_dict_buffer["id"].split(":")[-1]
        interface_statistics_dict_buffer["type"] = "Statistics"
        interface_statistics_dict_buffer["isPartOf"] = {}
        interface_statistics_dict_buffer["isPartOf"]["type"] = "Relationship"
        interface_statistics_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
        discontinuityTime = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}discontinuity-time")
        if discontinuityTime is not None:
            element_text = discontinuityTime.text
            if element_text is not None:
                interface_statistics_dict_buffer["discontinuityTime"] = {}
                interface_statistics_dict_buffer["discontinuityTime"]["type"] = "Property"
                interface_statistics_dict_buffer["discontinuityTime"]["value"] = element_text
        inOctets = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-octets")
        if inOctets is not None:
            element_text = inOctets.text
            if element_text is not None:
                interface_statistics_dict_buffer["inOctets"] = {}
                interface_statistics_dict_buffer["inOctets"]["type"] = "Property"
                interface_statistics_dict_buffer["inOctets"]["value"] = int(element_text)
        inUnicastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-unicast-pkts")
        if inUnicastPkts is not None:
            element_text = inUnicastPkts.text
            if element_text is not None:
                interface_statistics_dict_buffer["inUnicastPkts"] = {}
                interface_statistics_dict_buffer["inUnicastPkts"]["type"] = "Property"
                interface_statistics_dict_buffer["inUnicastPkts"]["value"] = int(element_text)
        inBroadcastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-broadcast-pkts")
        if inBroadcastPkts is not None:
            element_text = inBroadcastPkts.text
            if element_text is not None:
                interface_statistics_dict_buffer["inBroadcastPkts"] = {}
                interface_statistics_dict_buffer["inBroadcastPkts"]["type"] = "Property"
                interface_statistics_dict_buffer["inBroadcastPkts"]["value"] = int(element_text)
        inMulticastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-multicast-pkts")
        if inMulticastPkts is not None:
            element_text = inMulticastPkts.text
            if element_text is not None:
                interface_statistics_dict_buffer["inMulticastPkts"] = {}
                interface_statistics_dict_buffer["inMulticastPkts"]["type"] = "Property"
                interface_statistics_dict_buffer["inMulticastPkts"]["value"] = int(element_text)
        inDiscards = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-discards")
        if inDiscards is not None:
            element_text = inDiscards.text
            if element_text is not None:
                interface_statistics_dict_buffer["inDiscards"] = {}
                interface_statistics_dict_buffer["inDiscards"]["type"] = "Property"
                interface_statistics_dict_buffer["inDiscards"]["value"] = int(element_text)
        inErrors = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-errors")
        if inErrors is not None:
            element_text = inErrors.text
            if element_text is not None:
                interface_statistics_dict_buffer["inErrors"] = {}
                interface_statistics_dict_buffer["inErrors"]["type"] = "Property"
                interface_statistics_dict_buffer["inErrors"]["value"] = int(element_text)
        inUnknownProtos = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-unknown-protos")
        if inUnknownProtos is not None:
            element_text = inUnknownProtos.text
            if element_text is not None:
                interface_statistics_dict_buffer["inUnknownProtos"] = {}
                interface_statistics_dict_buffer["inUnknownProtos"]["type"] = "Property"
                interface_statistics_dict_buffer["inUnknownProtos"]["value"] = int(element_text)
        outOctets = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-octets")
        if outOctets is not None:
            element_text = outOctets.text
            if element_text is not None:
                interface_statistics_dict_buffer["outOctets"] = {}
                interface_statistics_dict_buffer["outOctets"]["type"] = "Property"
                interface_statistics_dict_buffer["outOctets"]["value"] = int(element_text)
        outUnicastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-unicast-pkts")
        if outUnicastPkts is not None:
            element_text = outUnicastPkts.text
            if element_text is not None:
                interface_statistics_dict_buffer["outUnicastPkts"] = {}
                interface_statistics_dict_buffer["outUnicastPkts"]["type"] = "Property"
                interface_statistics_dict_buffer["outUnicastPkts"]["value"] = int(element_text)
        outBroadcastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-broadcast-pkts")
        if outBroadcastPkts is not None:
            element_text = outBroadcastPkts.text
            if element_text is not None:
                interface_statistics_dict_buffer["outBroadcastPkts"] = {}
                interface_statistics_dict_buffer["outBroadcastPkts"]["type"] = "Property"
                interface_statistics_dict_buffer["outBroadcastPkts"]["value"] = int(element_text)
        outMulticastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-multicast-pkts")
        if outMulticastPkts is not None:
            element_text = outMulticastPkts.text
            if element_text is not None:
                interface_statistics_dict_buffer["outMulticastPkts"] = {}
                interface_statistics_dict_buffer["outMulticastPkts"]["type"] = "Property"
                interface_statistics_dict_buffer["outMulticastPkts"]["value"] = int(element_text)
        outDiscards = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-discards")
        if outDiscards is not None:
            element_text = outDiscards.text
            if element_text is not None:
                interface_statistics_dict_buffer["outDiscards"] = {}
                interface_statistics_dict_buffer["outDiscards"]["type"] = "Property"
                interface_statistics_dict_buffer["outDiscards"]["value"] = int(element_text)
        outErrors = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-errors")
        if outErrors is not None:
            element_text = outErrors.text
            if element_text is not None:
                interface_statistics_dict_buffer["outErrors"] = {}
                interface_statistics_dict_buffer["outErrors"]["type"] = "Property"
                interface_statistics_dict_buffer["outErrors"]["value"] = int(element_text)
        dict_buffers.append(interface_statistics_dict_buffer)
    for ipv4 in interface.findall(".//{urn:ietf:params:xml:ns:yang:ietf-ip}ipv4"):
        interface_ipv4_dict_buffer = {}
        interface_ipv4_dict_buffer["id"] = "urn:ngsi-ld:Ipv4:" + interface_dict_buffer["id"].split(":")[-1]
        interface_ipv4_dict_buffer["type"] = "Ipv4"
        interface_ipv4_dict_buffer["isPartOf"] = {}
        interface_ipv4_dict_buffer["isPartOf"]["type"] = "Relationship"
        interface_ipv4_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
        enabled = ipv4.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}enabled")
        if enabled is not None:
            element_text = enabled.text
            if element_text is not None:
                interface_ipv4_dict_buffer["enabled"] = {}
                interface_ipv4_dict_buffer["enabled"]["type"] = "Property"
                interface_ipv4_dict_buffer["enabled"]["value"] = eval(element_text.capitalize())
        forwarding = ipv4.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}forwarding")
        if forwarding is not None:
            element_text = forwarding.text
            if element_text is not None:
                interface_ipv4_dict_buffer["forwarding"] = {}
                interface_ipv4_dict_buffer["forwarding"]["type"] = "Property"
                interface_ipv4_dict_buffer["forwarding"]["value"] = eval(element_text.capitalize())
        mtu = ipv4.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}mtu")
        if mtu is not None:
            element_text = mtu.text
            if element_text is not None:
                interface_ipv4_dict_buffer["mtu"] = {}
                interface_ipv4_dict_buffer["mtu"]["type"] = "Property"
                interface_ipv4_dict_buffer["mtu"]["value"] = int(element_text)
        for address in ipv4.findall(".//{urn:ietf:params:xml:ns:yang:ietf-ip}address"):
            interface_ipv4_address_dict_buffer = {}
            interface_ipv4_address_dict_buffer["id"] = "urn:ngsi-ld:Ipv4Address:" + interface_ipv4_dict_buffer["id"].split(":")[-1]
            interface_ipv4_address_dict_buffer["type"] = "Ipv4Address"
            interface_ipv4_address_dict_buffer["isPartOf"] = {}
            interface_ipv4_address_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_ipv4_address_dict_buffer["isPartOf"]["object"] = interface_ipv4_dict_buffer["id"]
            ip = address.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}ip")
            if ip is not None:
                element_text = ip.text
                if element_text is not None:
                    interface_ipv4_address_dict_buffer["ip"] = {}
                    interface_ipv4_address_dict_buffer["ip"]["type"] = "Property"
                    interface_ipv4_address_dict_buffer["ip"]["value"] = element_text
            origin = address.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}origin")
            if origin is not None:
                element_text = origin.text
                if element_text is not None:
                    interface_ipv4_address_dict_buffer["origin"] = {}
                    interface_ipv4_address_dict_buffer["origin"]["type"] = "Property"
                    interface_ipv4_address_dict_buffer["origin"]["value"] = element_text
            dict_buffers.append(interface_ipv4_address_dict_buffer)
        for neighbor in ipv4.findall(".//{urn:ietf:params:xml:ns:yang:ietf-ip}neighbor"):
            interface_ipv4_neighbor_dict_buffer = {}
            interface_ipv4_neighbor_dict_buffer["id"] = "urn:ngsi-ld:Ipv4Neighbor:" + interface_ipv4_dict_buffer["id"].split(":")[-1]
            interface_ipv4_neighbor_dict_buffer["type"] = "Ipv4Neighbor"
            interface_ipv4_neighbor_dict_buffer["isPartOf"] = {}
            interface_ipv4_neighbor_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_ipv4_neighbor_dict_buffer["isPartOf"]["object"] = interface_ipv4_dict_buffer["id"]
            ip = neighbor.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}ip")
            if ip is not None:
                element_text = ip.text
                if element_text is not None:
                    interface_ipv4_neighbor_dict_buffer["ip"] = {}
                    interface_ipv4_neighbor_dict_buffer["ip"]["type"] = "Property"
                    interface_ipv4_neighbor_dict_buffer["ip"]["value"] = element_text
            linkLayerAddress = neighbor.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}link-layer-address")
            if linkLayerAddress is not None:
                element_text = linkLayerAddress.text
                if element_text is not None:
                    interface_ipv4_neighbor_dict_buffer["linkLayerAddress"] = {}
                    interface_ipv4_neighbor_dict_buffer["linkLayerAddress"]["type"] = "Property"
                    interface_ipv4_neighbor_dict_buffer["linkLayerAddress"]["value"] = element_text
            origin = neighbor.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}origin")
            if origin is not None:
                element_text = origin.text
                if element_text is not None:
                    interface_ipv4_neighbor_dict_buffer["origin"] = {}
                    interface_ipv4_neighbor_dict_buffer["origin"]["type"] = "Property"
                    interface_ipv4_neighbor_dict_buffer["origin"]["value"] = element_text
            dict_buffers.append(interface_ipv4_neighbor_dict_buffer)
        dict_buffers.append(interface_ipv4_dict_buffer)
    for ipv6 in interface.findall(".//{urn:ietf:params:xml:ns:yang:ietf-ip}ipv6"):
        interface_ipv6_dict_buffer = {}
        interface_ipv6_dict_buffer["id"] = "urn:ngsi-ld:Ipv6:" + interface_dict_buffer["id"].split(":")[-1]
        interface_ipv6_dict_buffer["type"] = "Ipv6"
        interface_ipv6_dict_buffer["isPartOf"] = {}
        interface_ipv6_dict_buffer["isPartOf"]["type"] = "Relationship"
        interface_ipv6_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
        enabled = ipv6.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}enabled")
        if enabled is not None:
            element_text = enabled.text
            if element_text is not None:
                interface_ipv6_dict_buffer["enabled"] = {}
                interface_ipv6_dict_buffer["enabled"]["type"] = "Property"
                interface_ipv6_dict_buffer["enabled"]["value"] = eval(element_text.capitalize())
        forwarding = ipv6.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}forwarding")
        if forwarding is not None:
            element_text = forwarding.text
            if element_text is not None:
                interface_ipv6_dict_buffer["forwarding"] = {}
                interface_ipv6_dict_buffer["forwarding"]["type"] = "Property"
                interface_ipv6_dict_buffer["forwarding"]["value"] = eval(element_text.capitalize())
        mtu = ipv6.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}mtu")
        if mtu is not None:
            element_text = mtu.text
            if element_text is not None:
                interface_ipv6_dict_buffer["mtu"] = {}
                interface_ipv6_dict_buffer["mtu"]["type"] = "Property"
                interface_ipv6_dict_buffer["mtu"]["value"] = int(element_text)
        for address in ipv6.findall(".//{urn:ietf:params:xml:ns:yang:ietf-ip}address"):
            interface_ipv6_address_dict_buffer = {}
            interface_ipv6_address_dict_buffer["id"] = "urn:ngsi-ld:Ipv6Address:" + interface_ipv6_dict_buffer["id"].split(":")[-1]
            interface_ipv6_address_dict_buffer["type"] = "Ipv6Address"
            interface_ipv6_address_dict_buffer["isPartOf"] = {}
            interface_ipv6_address_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_ipv6_address_dict_buffer["isPartOf"]["object"] = interface_ipv6_dict_buffer["id"]
            ip = address.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}ip")
            if ip is not None:
                element_text = ip.text
                if element_text is not None:
                    interface_ipv6_address_dict_buffer["ip"] = {}
                    interface_ipv6_address_dict_buffer["ip"]["type"] = "Property"
                    interface_ipv6_address_dict_buffer["ip"]["value"] = element_text
            prefixLength = address.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}prefix-length")
            if prefixLength is not None:
                element_text = prefixLength.text
                if element_text is not None:
                    interface_ipv6_address_dict_buffer["prefixLength"] = {}
                    interface_ipv6_address_dict_buffer["prefixLength"]["type"] = "Property"
                    interface_ipv6_address_dict_buffer["prefixLength"]["value"] = int(element_text)
            origin = address.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}origin")
            if origin is not None:
                element_text = origin.text
                if element_text is not None:
                    interface_ipv6_address_dict_buffer["origin"] = {}
                    interface_ipv6_address_dict_buffer["origin"]["type"] = "Property"
                    interface_ipv6_address_dict_buffer["origin"]["value"] = element_text
            status = address.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}status")
            if status is not None:
                element_text = status.text
                if element_text is not None:
                    interface_ipv6_address_dict_buffer["status"] = {}
                    interface_ipv6_address_dict_buffer["status"]["type"] = "Property"
                    interface_ipv6_address_dict_buffer["status"]["value"] = element_text
            dict_buffers.append(interface_ipv6_address_dict_buffer)
        for neighbor in ipv6.findall(".//{urn:ietf:params:xml:ns:yang:ietf-ip}neighbor"):
            interface_ipv6_neighbor_dict_buffer = {}
            interface_ipv6_neighbor_dict_buffer["id"] = "urn:ngsi-ld:Ipv6Neighbor:" + interface_ipv6_dict_buffer["id"].split(":")[-1]
            interface_ipv6_neighbor_dict_buffer["type"] = "Ipv6Neighbor"
            interface_ipv6_neighbor_dict_buffer["isPartOf"] = {}
            interface_ipv6_neighbor_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_ipv6_neighbor_dict_buffer["isPartOf"]["object"] = interface_ipv6_dict_buffer["id"]
            ip = neighbor.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}ip")
            if ip is not None:
                element_text = ip.text
                if element_text is not None:
                    interface_ipv6_neighbor_dict_buffer["ip"] = {}
                    interface_ipv6_neighbor_dict_buffer["ip"]["type"] = "Property"
                    interface_ipv6_neighbor_dict_buffer["ip"]["value"] = element_text
            linkLayerAddress = neighbor.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}link-layer-address")
            if linkLayerAddress is not None:
                element_text = linkLayerAddress.text
                if element_text is not None:
                    interface_ipv6_neighbor_dict_buffer["linkLayerAddress"] = {}
                    interface_ipv6_neighbor_dict_buffer["linkLayerAddress"]["type"] = "Property"
                    interface_ipv6_neighbor_dict_buffer["linkLayerAddress"]["value"] = element_text
            origin = neighbor.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}origin")
            if origin is not None:
                element_text = origin.text
                if element_text is not None:
                    interface_ipv6_neighbor_dict_buffer["origin"] = {}
                    interface_ipv6_neighbor_dict_buffer["origin"]["type"] = "Property"
                    interface_ipv6_neighbor_dict_buffer["origin"]["value"] = element_text
            isRouter = neighbor.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}is-router")
            if isRouter is not None:
                element_text = isRouter.text
                if element_text is not None:
                    interface_ipv6_neighbor_dict_buffer["isRouter"] = {}
                    interface_ipv6_neighbor_dict_buffer["isRouter"]["type"] = "Property"
                    interface_ipv6_neighbor_dict_buffer["isRouter"]["value"] = element_text
            state = neighbor.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}state")
            if state is not None:
                element_text = state.text
                if element_text is not None:
                    interface_ipv6_neighbor_dict_buffer["state"] = {}
                    interface_ipv6_neighbor_dict_buffer["state"]["type"] = "Property"
                    interface_ipv6_neighbor_dict_buffer["state"]["value"] = element_text
            dict_buffers.append(interface_ipv6_neighbor_dict_buffer)
        dupAddrDetectTransmits = ipv6.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}dup-addr-detect-transmits")
        if dupAddrDetectTransmits is not None:
            element_text = dupAddrDetectTransmits.text
            if element_text is not None:
                interface_ipv6_dict_buffer["dupAddrDetectTransmits"] = {}
                interface_ipv6_dict_buffer["dupAddrDetectTransmits"]["type"] = "Property"
                interface_ipv6_dict_buffer["dupAddrDetectTransmits"]["value"] = int(element_text)
        for autoconf in ipv6.findall(".//{urn:ietf:params:xml:ns:yang:ietf-ip}autoconf"):
            interface_ipv6_autoconf_dict_buffer = {}
            interface_ipv6_autoconf_dict_buffer["id"] = "urn:ngsi-ld:Ipv6Autoconf:" + interface_ipv6_dict_buffer["id"].split(":")[-1]
            interface_ipv6_autoconf_dict_buffer["type"] = "Ipv6Autoconf"
            interface_ipv6_autoconf_dict_buffer["isPartOf"] = {}
            interface_ipv6_autoconf_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_ipv6_autoconf_dict_buffer["isPartOf"]["object"] = interface_ipv6_dict_buffer["id"]
            createGlobalAddresses = autoconf.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}create-global-addresses")
            if createGlobalAddresses is not None:
                element_text = createGlobalAddresses.text
                if element_text is not None:
                    interface_ipv6_autoconf_dict_buffer["createGlobalAddresses"] = {}
                    interface_ipv6_autoconf_dict_buffer["createGlobalAddresses"]["type"] = "Property"
                    interface_ipv6_autoconf_dict_buffer["createGlobalAddresses"]["value"] = eval(element_text.capitalize())
            createTemporaryAddresses = autoconf.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}create-temporary-addresses")
            if createTemporaryAddresses is not None:
                element_text = createTemporaryAddresses.text
                if element_text is not None:
                    interface_ipv6_autoconf_dict_buffer["createTemporaryAddresses"] = {}
                    interface_ipv6_autoconf_dict_buffer["createTemporaryAddresses"]["type"] = "Property"
                    interface_ipv6_autoconf_dict_buffer["createTemporaryAddresses"]["value"] = eval(element_text.capitalize())
            temporaryValidLifetime = autoconf.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}temporary-valid-lifetime")
            if temporaryValidLifetime is not None:
                element_text = temporaryValidLifetime.text
                if element_text is not None:
                    interface_ipv6_autoconf_dict_buffer["temporaryValidLifetime"] = {}
                    interface_ipv6_autoconf_dict_buffer["temporaryValidLifetime"]["type"] = "Property"
                    interface_ipv6_autoconf_dict_buffer["temporaryValidLifetime"]["value"] = int(element_text)
            temporaryPreferredLifetime = autoconf.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}temporary-preferred-lifetime")
            if temporaryPreferredLifetime is not None:
                element_text = temporaryPreferredLifetime.text
                if element_text is not None:
                    interface_ipv6_autoconf_dict_buffer["temporaryPreferredLifetime"] = {}
                    interface_ipv6_autoconf_dict_buffer["temporaryPreferredLifetime"]["type"] = "Property"
                    interface_ipv6_autoconf_dict_buffer["temporaryPreferredLifetime"]["value"] = int(element_text)
            dict_buffers.append(interface_ipv6_autoconf_dict_buffer)
        dict_buffers.append(interface_ipv6_dict_buffer)
    dict_buffers.append(interface_dict_buffer)

# Write dictionary buffers to an output file which name has been passed as an invocation parameter.
output_file = open(dict_buffers_file, 'w')
output_file.write(str(dict_buffers[::-1]))
output_file.close()
dict_buffers.clear()
