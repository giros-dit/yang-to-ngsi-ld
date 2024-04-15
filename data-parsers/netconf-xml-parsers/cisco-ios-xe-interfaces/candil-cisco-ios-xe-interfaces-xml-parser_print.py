import json
import xml.etree.ElementTree as et
import sys

xml = sys.argv[1]
tree = et.parse(xml)
root = tree.getroot()
observed_at = root[0].text
dict_buffers = []

for interface in root.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}interface"):
    interface_dict_buffer = {}
    interface_dict_buffer["id"] = "urn:ngsi-ld:Interface"
    interface_dict_buffer["type"] = "Interface"
    name = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}name")
    if name is not None:
        element_text = name.text
        if element_text is not None:
            interface_dict_buffer["id"] = interface_dict_buffer["id"] + ":" + element_text
            interface_dict_buffer["name"] = {}
            interface_dict_buffer["name"]["type"] = "Property"
            interface_dict_buffer["name"]["value"] = element_text
            interface_dict_buffer["name"]["observedAt"] = observed_at
    interfaceType = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}interface-type")
    if interfaceType is not None:
        element_text = interfaceType.text
        if element_text is not None:
            interface_dict_buffer["interfaceType"] = {}
            interface_dict_buffer["interfaceType"]["type"] = "Property"
            interface_dict_buffer["interfaceType"]["value"] = element_text
            interface_dict_buffer["interfaceType"]["observedAt"] = observed_at
    adminStatus = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}admin-status")
    if adminStatus is not None:
        element_text = adminStatus.text
        if element_text is not None:
            interface_dict_buffer["adminStatus"] = {}
            interface_dict_buffer["adminStatus"]["type"] = "Property"
            interface_dict_buffer["adminStatus"]["value"] = element_text
            interface_dict_buffer["adminStatus"]["observedAt"] = observed_at
    operStatus = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}oper-status")
    if operStatus is not None:
        element_text = operStatus.text
        if element_text is not None:
            interface_dict_buffer["operStatus"] = {}
            interface_dict_buffer["operStatus"]["type"] = "Property"
            interface_dict_buffer["operStatus"]["value"] = element_text
            interface_dict_buffer["operStatus"]["observedAt"] = observed_at
    lastChange = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}last-change")
    if lastChange is not None:
        element_text = lastChange.text
        if element_text is not None:
            interface_dict_buffer["lastChange"] = {}
            interface_dict_buffer["lastChange"]["type"] = "Property"
            interface_dict_buffer["lastChange"]["value"] = element_text
            interface_dict_buffer["lastChange"]["observedAt"] = observed_at
    ifIndex = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}if-index")
    if ifIndex is not None:
        element_text = ifIndex.text
        if element_text is not None:
            interface_dict_buffer["ifIndex"] = {}
            interface_dict_buffer["ifIndex"]["type"] = "Property"
            interface_dict_buffer["ifIndex"]["value"] = int(element_text)
            interface_dict_buffer["ifIndex"]["observedAt"] = observed_at
    physAddress = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}phys-address")
    if physAddress is not None:
        element_text = physAddress.text
        if element_text is not None:
            interface_dict_buffer["physAddress"] = {}
            interface_dict_buffer["physAddress"]["type"] = "Property"
            interface_dict_buffer["physAddress"]["value"] = element_text
            interface_dict_buffer["physAddress"]["observedAt"] = observed_at
    higherLayerIf = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}higher-layer-if")
    if higherLayerIf is not None:
        element_text = higherLayerIf.text
        if element_text is not None:
            interface_dict_buffer["higherLayerIf"] = {}
            interface_dict_buffer["higherLayerIf"]["type"] = "Property"
            interface_dict_buffer["higherLayerIf"]["value"] = element_text
            interface_dict_buffer["higherLayerIf"]["observedAt"] = observed_at
    lowerLayerIf = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}lower-layer-if")
    if lowerLayerIf is not None:
        element_text = lowerLayerIf.text
        if element_text is not None:
            interface_dict_buffer["lowerLayerIf"] = {}
            interface_dict_buffer["lowerLayerIf"]["type"] = "Property"
            interface_dict_buffer["lowerLayerIf"]["value"] = element_text
            interface_dict_buffer["lowerLayerIf"]["observedAt"] = observed_at
    speed = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}speed")
    if speed is not None:
        element_text = speed.text
        if element_text is not None:
            interface_dict_buffer["speed"] = {}
            interface_dict_buffer["speed"]["type"] = "Property"
            interface_dict_buffer["speed"]["value"] = int(element_text)
            interface_dict_buffer["speed"]["observedAt"] = observed_at
    for statistics in interface.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}statistics"):
        interface_statistics_dict_buffer = {}
        interface_statistics_dict_buffer["id"] = "urn:ngsi-ld:InterfaceStatistics:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
        interface_statistics_dict_buffer["type"] = "InterfaceStatistics"
        interface_statistics_dict_buffer["isPartOf"] = {}
        interface_statistics_dict_buffer["isPartOf"]["type"] = "Relationship"
        interface_statistics_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
        interface_statistics_dict_buffer["isPartOf"]["observedAt"] = observed_at
        discontinuityTime = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}discontinuity-time")
        if discontinuityTime is not None:
            element_text = discontinuityTime.text
            if element_text is not None:
                interface_statistics_dict_buffer["discontinuityTime"] = {}
                interface_statistics_dict_buffer["discontinuityTime"]["type"] = "Property"
                interface_statistics_dict_buffer["discontinuityTime"]["value"] = element_text
                interface_statistics_dict_buffer["discontinuityTime"]["observedAt"] = observed_at
        inOctets = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-octets")
        if inOctets is not None:
            element_text = inOctets.text
            if element_text is not None:
                interface_statistics_dict_buffer["inOctets"] = {}
                interface_statistics_dict_buffer["inOctets"]["type"] = "Property"
                interface_statistics_dict_buffer["inOctets"]["value"] = int(element_text)
                interface_statistics_dict_buffer["inOctets"]["observedAt"] = observed_at
        inUnicastPkts = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-unicast-pkts")
        if inUnicastPkts is not None:
            element_text = inUnicastPkts.text
            if element_text is not None:
                interface_statistics_dict_buffer["inUnicastPkts"] = {}
                interface_statistics_dict_buffer["inUnicastPkts"]["type"] = "Property"
                interface_statistics_dict_buffer["inUnicastPkts"]["value"] = int(element_text)
                interface_statistics_dict_buffer["inUnicastPkts"]["observedAt"] = observed_at
        inBroadcastPkts = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-broadcast-pkts")
        if inBroadcastPkts is not None:
            element_text = inBroadcastPkts.text
            if element_text is not None:
                interface_statistics_dict_buffer["inBroadcastPkts"] = {}
                interface_statistics_dict_buffer["inBroadcastPkts"]["type"] = "Property"
                interface_statistics_dict_buffer["inBroadcastPkts"]["value"] = int(element_text)
                interface_statistics_dict_buffer["inBroadcastPkts"]["observedAt"] = observed_at
        inMulticastPkts = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-multicast-pkts")
        if inMulticastPkts is not None:
            element_text = inMulticastPkts.text
            if element_text is not None:
                interface_statistics_dict_buffer["inMulticastPkts"] = {}
                interface_statistics_dict_buffer["inMulticastPkts"]["type"] = "Property"
                interface_statistics_dict_buffer["inMulticastPkts"]["value"] = int(element_text)
                interface_statistics_dict_buffer["inMulticastPkts"]["observedAt"] = observed_at
        inDiscards = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-discards")
        if inDiscards is not None:
            element_text = inDiscards.text
            if element_text is not None:
                interface_statistics_dict_buffer["inDiscards"] = {}
                interface_statistics_dict_buffer["inDiscards"]["type"] = "Property"
                interface_statistics_dict_buffer["inDiscards"]["value"] = int(element_text)
                interface_statistics_dict_buffer["inDiscards"]["observedAt"] = observed_at
        inErrors = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-errors")
        if inErrors is not None:
            element_text = inErrors.text
            if element_text is not None:
                interface_statistics_dict_buffer["inErrors"] = {}
                interface_statistics_dict_buffer["inErrors"]["type"] = "Property"
                interface_statistics_dict_buffer["inErrors"]["value"] = int(element_text)
                interface_statistics_dict_buffer["inErrors"]["observedAt"] = observed_at
        inUnknownProtos = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-unknown-protos")
        if inUnknownProtos is not None:
            element_text = inUnknownProtos.text
            if element_text is not None:
                interface_statistics_dict_buffer["inUnknownProtos"] = {}
                interface_statistics_dict_buffer["inUnknownProtos"]["type"] = "Property"
                interface_statistics_dict_buffer["inUnknownProtos"]["value"] = int(element_text)
                interface_statistics_dict_buffer["inUnknownProtos"]["observedAt"] = observed_at
        outOctets = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}out-octets")
        if outOctets is not None:
            element_text = outOctets.text
            if element_text is not None:
                interface_statistics_dict_buffer["outOctets"] = {}
                interface_statistics_dict_buffer["outOctets"]["type"] = "Property"
                interface_statistics_dict_buffer["outOctets"]["value"] = int(element_text)
                interface_statistics_dict_buffer["outOctets"]["observedAt"] = observed_at
        outUnicastPkts = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}out-unicast-pkts")
        if outUnicastPkts is not None:
            element_text = outUnicastPkts.text
            if element_text is not None:
                interface_statistics_dict_buffer["outUnicastPkts"] = {}
                interface_statistics_dict_buffer["outUnicastPkts"]["type"] = "Property"
                interface_statistics_dict_buffer["outUnicastPkts"]["value"] = int(element_text)
                interface_statistics_dict_buffer["outUnicastPkts"]["observedAt"] = observed_at
        outBroadcastPkts = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}out-broadcast-pkts")
        if outBroadcastPkts is not None:
            element_text = outBroadcastPkts.text
            if element_text is not None:
                interface_statistics_dict_buffer["outBroadcastPkts"] = {}
                interface_statistics_dict_buffer["outBroadcastPkts"]["type"] = "Property"
                interface_statistics_dict_buffer["outBroadcastPkts"]["value"] = int(element_text)
                interface_statistics_dict_buffer["outBroadcastPkts"]["observedAt"] = observed_at
        outMulticastPkts = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}out-multicast-pkts")
        if outMulticastPkts is not None:
            element_text = outMulticastPkts.text
            if element_text is not None:
                interface_statistics_dict_buffer["outMulticastPkts"] = {}
                interface_statistics_dict_buffer["outMulticastPkts"]["type"] = "Property"
                interface_statistics_dict_buffer["outMulticastPkts"]["value"] = int(element_text)
                interface_statistics_dict_buffer["outMulticastPkts"]["observedAt"] = observed_at
        outDiscards = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}out-discards")
        if outDiscards is not None:
            element_text = outDiscards.text
            if element_text is not None:
                interface_statistics_dict_buffer["outDiscards"] = {}
                interface_statistics_dict_buffer["outDiscards"]["type"] = "Property"
                interface_statistics_dict_buffer["outDiscards"]["value"] = int(element_text)
                interface_statistics_dict_buffer["outDiscards"]["observedAt"] = observed_at
        outErrors = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}out-errors")
        if outErrors is not None:
            element_text = outErrors.text
            if element_text is not None:
                interface_statistics_dict_buffer["outErrors"] = {}
                interface_statistics_dict_buffer["outErrors"]["type"] = "Property"
                interface_statistics_dict_buffer["outErrors"]["value"] = int(element_text)
                interface_statistics_dict_buffer["outErrors"]["observedAt"] = observed_at
        rxPps = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}rx-pps")
        if rxPps is not None:
            element_text = rxPps.text
            if element_text is not None:
                interface_statistics_dict_buffer["rxPps"] = {}
                interface_statistics_dict_buffer["rxPps"]["type"] = "Property"
                interface_statistics_dict_buffer["rxPps"]["value"] = int(element_text)
                interface_statistics_dict_buffer["rxPps"]["observedAt"] = observed_at
        rxKbps = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}rx-kbps")
        if rxKbps is not None:
            element_text = rxKbps.text
            if element_text is not None:
                interface_statistics_dict_buffer["rxKbps"] = {}
                interface_statistics_dict_buffer["rxKbps"]["type"] = "Property"
                interface_statistics_dict_buffer["rxKbps"]["value"] = int(element_text)
                interface_statistics_dict_buffer["rxKbps"]["observedAt"] = observed_at
        txPps = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}tx-pps")
        if txPps is not None:
            element_text = txPps.text
            if element_text is not None:
                interface_statistics_dict_buffer["txPps"] = {}
                interface_statistics_dict_buffer["txPps"]["type"] = "Property"
                interface_statistics_dict_buffer["txPps"]["value"] = int(element_text)
                interface_statistics_dict_buffer["txPps"]["observedAt"] = observed_at
        txKbps = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}tx-kbps")
        if txKbps is not None:
            element_text = txKbps.text
            if element_text is not None:
                interface_statistics_dict_buffer["txKbps"] = {}
                interface_statistics_dict_buffer["txKbps"]["type"] = "Property"
                interface_statistics_dict_buffer["txKbps"]["value"] = int(element_text)
                interface_statistics_dict_buffer["txKbps"]["observedAt"] = observed_at
        numFlaps = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}num-flaps")
        if numFlaps is not None:
            element_text = numFlaps.text
            if element_text is not None:
                interface_statistics_dict_buffer["numFlaps"] = {}
                interface_statistics_dict_buffer["numFlaps"]["type"] = "Property"
                interface_statistics_dict_buffer["numFlaps"]["value"] = int(element_text)
                interface_statistics_dict_buffer["numFlaps"]["observedAt"] = observed_at
        inCrcErrors = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-crc-errors")
        if inCrcErrors is not None:
            element_text = inCrcErrors.text
            if element_text is not None:
                interface_statistics_dict_buffer["inCrcErrors"] = {}
                interface_statistics_dict_buffer["inCrcErrors"]["type"] = "Property"
                interface_statistics_dict_buffer["inCrcErrors"]["value"] = int(element_text)
                interface_statistics_dict_buffer["inCrcErrors"]["observedAt"] = observed_at
        inDiscards64 = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-discards-64")
        if inDiscards64 is not None:
            element_text = inDiscards64.text
            if element_text is not None:
                interface_statistics_dict_buffer["inDiscards64"] = {}
                interface_statistics_dict_buffer["inDiscards64"]["type"] = "Property"
                interface_statistics_dict_buffer["inDiscards64"]["value"] = int(element_text)
                interface_statistics_dict_buffer["inDiscards64"]["observedAt"] = observed_at
        inErrors64 = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-errors-64")
        if inErrors64 is not None:
            element_text = inErrors64.text
            if element_text is not None:
                interface_statistics_dict_buffer["inErrors64"] = {}
                interface_statistics_dict_buffer["inErrors64"]["type"] = "Property"
                interface_statistics_dict_buffer["inErrors64"]["value"] = int(element_text)
                interface_statistics_dict_buffer["inErrors64"]["observedAt"] = observed_at
        inUnknownProtos64 = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-unknown-protos-64")
        if inUnknownProtos64 is not None:
            element_text = inUnknownProtos64.text
            if element_text is not None:
                interface_statistics_dict_buffer["inUnknownProtos64"] = {}
                interface_statistics_dict_buffer["inUnknownProtos64"]["type"] = "Property"
                interface_statistics_dict_buffer["inUnknownProtos64"]["value"] = int(element_text)
                interface_statistics_dict_buffer["inUnknownProtos64"]["observedAt"] = observed_at
        outOctets64 = statistics.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}out-octets-64")
        if outOctets64 is not None:
            element_text = outOctets64.text
            if element_text is not None:
                interface_statistics_dict_buffer["outOctets64"] = {}
                interface_statistics_dict_buffer["outOctets64"]["type"] = "Property"
                interface_statistics_dict_buffer["outOctets64"]["value"] = int(element_text)
                interface_statistics_dict_buffer["outOctets64"]["observedAt"] = observed_at
        dict_buffers.append(interface_statistics_dict_buffer)
    for diffserv_info in interface.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}diffserv-info"):
        interface_diffserv_info_dict_buffer = {}
        interface_diffserv_info_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfo:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
        interface_diffserv_info_dict_buffer["type"] = "InterfaceDiffservInfo"
        interface_diffserv_info_dict_buffer["isPartOf"] = {}
        interface_diffserv_info_dict_buffer["isPartOf"]["type"] = "Relationship"
        interface_diffserv_info_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
        interface_diffserv_info_dict_buffer["isPartOf"]["observedAt"] = observed_at
        direction = diffserv_info.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}direction")
        if direction is not None:
            element_text = direction.text
            if element_text is not None:
                interface_diffserv_info_dict_buffer["direction"] = {}
                interface_diffserv_info_dict_buffer["direction"]["type"] = "Property"
                interface_diffserv_info_dict_buffer["direction"]["value"] = element_text
                interface_diffserv_info_dict_buffer["direction"]["observedAt"] = observed_at
        policyName = diffserv_info.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}policy-name")
        if policyName is not None:
            element_text = policyName.text
            if element_text is not None:
                interface_diffserv_info_dict_buffer["id"] = interface_diffserv_info_dict_buffer["id"] + ":" + element_text
                interface_diffserv_info_dict_buffer["policyName"] = {}
                interface_diffserv_info_dict_buffer["policyName"]["type"] = "Property"
                interface_diffserv_info_dict_buffer["policyName"]["value"] = element_text
                interface_diffserv_info_dict_buffer["policyName"]["observedAt"] = observed_at
        for diffserv_target_classifier_stats in diffserv_info.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}diffserv-target-classifier-stats"):
            interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer = {}
            interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoDiffservTargetClassifierStats:" + ":".join(interface_diffserv_info_dict_buffer["id"].split(":")[3:])
            interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["type"] = "InterfaceDiffservInfoDiffservTargetClassifierStats"
            interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["isPartOf"] = {}
            interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_dict_buffer["id"]
            interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["isPartOf"]["observedAt"] = observed_at
            classifierEntryName = diffserv_target_classifier_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}classifier-entry-name")
            if classifierEntryName is not None:
                element_text = classifierEntryName.text
                if element_text is not None:
                    interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["id"] = interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["id"] + ":" + element_text
                    interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["classifierEntryName"] = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["classifierEntryName"]["type"] = "Property"
                    interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["classifierEntryName"]["value"] = element_text
                    interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["classifierEntryName"]["observedAt"] = observed_at
            parentPath = diffserv_target_classifier_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}parent-path")
            if parentPath is not None:
                element_text = parentPath.text
                if element_text is not None:
                    interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["parentPath"] = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["parentPath"]["type"] = "Property"
                    interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["parentPath"]["value"] = element_text
                    interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["parentPath"]["observedAt"] = observed_at
            for classifier_entry_stats in diffserv_target_classifier_stats.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}classifier-entry-stats"):
                interface_diffserv_info_diffserv_target_classifier_stats_classifier_entry_stats_dict_buffer = {}
                interface_diffserv_info_diffserv_target_classifier_stats_classifier_entry_stats_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoDiffservTargetClassifierStatsClassifierEntryStats:" + ":".join(interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["id"].split(":")[3:])
                interface_diffserv_info_diffserv_target_classifier_stats_classifier_entry_stats_dict_buffer["type"] = "InterfaceDiffservInfoDiffservTargetClassifierStatsClassifierEntryStats"
                interface_diffserv_info_diffserv_target_classifier_stats_classifier_entry_stats_dict_buffer["isPartOf"] = {}
                interface_diffserv_info_diffserv_target_classifier_stats_classifier_entry_stats_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_diffserv_info_diffserv_target_classifier_stats_classifier_entry_stats_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["id"]
                interface_diffserv_info_diffserv_target_classifier_stats_classifier_entry_stats_dict_buffer["isPartOf"]["observedAt"] = observed_at
                classifiedPkts = classifier_entry_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}classified-pkts")
                if classifiedPkts is not None:
                    element_text = classifiedPkts.text
                    if element_text is not None:
                        interface_diffserv_info_diffserv_target_classifier_stats_classifier_entry_stats_dict_buffer["classifiedPkts"] = {}
                        interface_diffserv_info_diffserv_target_classifier_stats_classifier_entry_stats_dict_buffer["classifiedPkts"]["type"] = "Property"
                        interface_diffserv_info_diffserv_target_classifier_stats_classifier_entry_stats_dict_buffer["classifiedPkts"]["value"] = int(element_text)
                        interface_diffserv_info_diffserv_target_classifier_stats_classifier_entry_stats_dict_buffer["classifiedPkts"]["observedAt"] = observed_at
                classifiedBytes = classifier_entry_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}classified-bytes")
                if classifiedBytes is not None:
                    element_text = classifiedBytes.text
                    if element_text is not None:
                        interface_diffserv_info_diffserv_target_classifier_stats_classifier_entry_stats_dict_buffer["classifiedBytes"] = {}
                        interface_diffserv_info_diffserv_target_classifier_stats_classifier_entry_stats_dict_buffer["classifiedBytes"]["type"] = "Property"
                        interface_diffserv_info_diffserv_target_classifier_stats_classifier_entry_stats_dict_buffer["classifiedBytes"]["value"] = int(element_text)
                        interface_diffserv_info_diffserv_target_classifier_stats_classifier_entry_stats_dict_buffer["classifiedBytes"]["observedAt"] = observed_at
                classifiedRate = classifier_entry_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}classified-rate")
                if classifiedRate is not None:
                    element_text = classifiedRate.text
                    if element_text is not None:
                        interface_diffserv_info_diffserv_target_classifier_stats_classifier_entry_stats_dict_buffer["classifiedRate"] = {}
                        interface_diffserv_info_diffserv_target_classifier_stats_classifier_entry_stats_dict_buffer["classifiedRate"]["type"] = "Property"
                        interface_diffserv_info_diffserv_target_classifier_stats_classifier_entry_stats_dict_buffer["classifiedRate"]["value"] = int(element_text)
                        interface_diffserv_info_diffserv_target_classifier_stats_classifier_entry_stats_dict_buffer["classifiedRate"]["observedAt"] = observed_at
                dict_buffers.append(interface_diffserv_info_diffserv_target_classifier_stats_classifier_entry_stats_dict_buffer)
            for meter_stats in diffserv_target_classifier_stats.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}meter-stats"):
                interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer = {}
                interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoDiffservTargetClassifierStatsMeterStats:" + ":".join(interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["id"].split(":")[3:])
                interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["type"] = "InterfaceDiffservInfoDiffservTargetClassifierStatsMeterStats"
                interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["isPartOf"] = {}
                interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["id"]
                interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["isPartOf"]["observedAt"] = observed_at
                meterId = meter_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}meter-id")
                if meterId is not None:
                    element_text = meterId.text
                    if element_text is not None:
                        interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["id"] = interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["id"] + ":" + int(element_text)
                        interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["meterId"] = {}
                        interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["meterId"]["type"] = "Property"
                        interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["meterId"]["value"] = int(element_text)
                        interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["meterId"]["observedAt"] = observed_at
                meterSucceedPkts = meter_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}meter-succeed-pkts")
                if meterSucceedPkts is not None:
                    element_text = meterSucceedPkts.text
                    if element_text is not None:
                        interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["meterSucceedPkts"] = {}
                        interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["meterSucceedPkts"]["type"] = "Property"
                        interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["meterSucceedPkts"]["value"] = int(element_text)
                        interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["meterSucceedPkts"]["observedAt"] = observed_at
                meterSucceedBytes = meter_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}meter-succeed-bytes")
                if meterSucceedBytes is not None:
                    element_text = meterSucceedBytes.text
                    if element_text is not None:
                        interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["meterSucceedBytes"] = {}
                        interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["meterSucceedBytes"]["type"] = "Property"
                        interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["meterSucceedBytes"]["value"] = int(element_text)
                        interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["meterSucceedBytes"]["observedAt"] = observed_at
                meterFailedPkts = meter_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}meter-failed-pkts")
                if meterFailedPkts is not None:
                    element_text = meterFailedPkts.text
                    if element_text is not None:
                        interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["meterFailedPkts"] = {}
                        interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["meterFailedPkts"]["type"] = "Property"
                        interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["meterFailedPkts"]["value"] = int(element_text)
                        interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["meterFailedPkts"]["observedAt"] = observed_at
                meterFailedBytes = meter_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}meter-failed-bytes")
                if meterFailedBytes is not None:
                    element_text = meterFailedBytes.text
                    if element_text is not None:
                        interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["meterFailedBytes"] = {}
                        interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["meterFailedBytes"]["type"] = "Property"
                        interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["meterFailedBytes"]["value"] = int(element_text)
                        interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer["meterFailedBytes"]["observedAt"] = observed_at
                dict_buffers.append(interface_diffserv_info_diffserv_target_classifier_stats_meter_stats_dict_buffer)
            for queuing_stats in diffserv_target_classifier_stats.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}queuing-stats"):
                interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer = {}
                interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoDiffservTargetClassifierStatsQueuingStats:" + ":".join(interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["id"].split(":")[3:])
                interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["type"] = "InterfaceDiffservInfoDiffservTargetClassifierStatsQueuingStats"
                interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["isPartOf"] = {}
                interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["id"]
                interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["isPartOf"]["observedAt"] = observed_at
                outputPkts = queuing_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}output-pkts")
                if outputPkts is not None:
                    element_text = outputPkts.text
                    if element_text is not None:
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["outputPkts"] = {}
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["outputPkts"]["type"] = "Property"
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["outputPkts"]["value"] = int(element_text)
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["outputPkts"]["observedAt"] = observed_at
                outputBytes = queuing_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}output-bytes")
                if outputBytes is not None:
                    element_text = outputBytes.text
                    if element_text is not None:
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["outputBytes"] = {}
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["outputBytes"]["type"] = "Property"
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["outputBytes"]["value"] = int(element_text)
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["outputBytes"]["observedAt"] = observed_at
                queueSizePkts = queuing_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}queue-size-pkts")
                if queueSizePkts is not None:
                    element_text = queueSizePkts.text
                    if element_text is not None:
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["queueSizePkts"] = {}
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["queueSizePkts"]["type"] = "Property"
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["queueSizePkts"]["value"] = int(element_text)
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["queueSizePkts"]["observedAt"] = observed_at
                queueSizeBytes = queuing_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}queue-size-bytes")
                if queueSizeBytes is not None:
                    element_text = queueSizeBytes.text
                    if element_text is not None:
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["queueSizeBytes"] = {}
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["queueSizeBytes"]["type"] = "Property"
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["queueSizeBytes"]["value"] = int(element_text)
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["queueSizeBytes"]["observedAt"] = observed_at
                dropPkts = queuing_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}drop-pkts")
                if dropPkts is not None:
                    element_text = dropPkts.text
                    if element_text is not None:
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["dropPkts"] = {}
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["dropPkts"]["type"] = "Property"
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["dropPkts"]["value"] = int(element_text)
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["dropPkts"]["observedAt"] = observed_at
                dropBytes = queuing_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}drop-bytes")
                if dropBytes is not None:
                    element_text = dropBytes.text
                    if element_text is not None:
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["dropBytes"] = {}
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["dropBytes"]["type"] = "Property"
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["dropBytes"]["value"] = int(element_text)
                        interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["dropBytes"]["observedAt"] = observed_at
                for wred_stats in queuing_stats.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-stats"):
                    interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoDiffservTargetClassifierStatsQueuingStatsWredStats:" + ":".join(interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["id"].split(":")[3:])
                    interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["type"] = "InterfaceDiffservInfoDiffservTargetClassifierStatsQueuingStatsWredStats"
                    interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["isPartOf"] = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["id"]
                    interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    earlyDropPkts = wred_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}early-drop-pkts")
                    if earlyDropPkts is not None:
                        element_text = earlyDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["earlyDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["earlyDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["earlyDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["earlyDropPkts"]["observedAt"] = observed_at
                    earlyDropBytes = wred_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}early-drop-bytes")
                    if earlyDropBytes is not None:
                        element_text = earlyDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["earlyDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["earlyDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["earlyDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["earlyDropBytes"]["observedAt"] = observed_at
                    meanQueueDepth = wred_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}mean-queue-depth")
                    if meanQueueDepth is not None:
                        element_text = meanQueueDepth.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["meanQueueDepth"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["meanQueueDepth"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["meanQueueDepth"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["meanQueueDepth"]["observedAt"] = observed_at
                    transmittedPkts = wred_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}transmitted-pkts")
                    if transmittedPkts is not None:
                        element_text = transmittedPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["transmittedPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["transmittedPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["transmittedPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["transmittedPkts"]["observedAt"] = observed_at
                    transmittedBytes = wred_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}transmitted-bytes")
                    if transmittedBytes is not None:
                        element_text = transmittedBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["transmittedBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["transmittedBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["transmittedBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["transmittedBytes"]["observedAt"] = observed_at
                    tailDropPkts = wred_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}tail-drop-pkts")
                    if tailDropPkts is not None:
                        element_text = tailDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["tailDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["tailDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["tailDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["tailDropPkts"]["observedAt"] = observed_at
                    tailDropBytes = wred_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}tail-drop-bytes")
                    if tailDropBytes is not None:
                        element_text = tailDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["tailDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["tailDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["tailDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["tailDropBytes"]["observedAt"] = observed_at
                    dropPktsFlow = wred_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}drop-pkts-flow")
                    if dropPktsFlow is not None:
                        element_text = dropPktsFlow.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["dropPktsFlow"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["dropPktsFlow"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["dropPktsFlow"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["dropPktsFlow"]["observedAt"] = observed_at
                    dropPktsNoBuffer = wred_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}drop-pkts-no-buffer")
                    if dropPktsNoBuffer is not None:
                        element_text = dropPktsNoBuffer.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["dropPktsNoBuffer"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["dropPktsNoBuffer"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["dropPktsNoBuffer"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["dropPktsNoBuffer"]["observedAt"] = observed_at
                    queuePeakSizePkts = wred_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}queue-peak-size-pkts")
                    if queuePeakSizePkts is not None:
                        element_text = queuePeakSizePkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["queuePeakSizePkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["queuePeakSizePkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["queuePeakSizePkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["queuePeakSizePkts"]["observedAt"] = observed_at
                    queuePeakSizeBytes = wred_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}queue-peak-size-bytes")
                    if queuePeakSizeBytes is not None:
                        element_text = queuePeakSizeBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["queuePeakSizeBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["queuePeakSizeBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["queuePeakSizeBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["queuePeakSizeBytes"]["observedAt"] = observed_at
                    bandwidthExceedDrops = wred_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}bandwidth-exceed-drops")
                    if bandwidthExceedDrops is not None:
                        element_text = bandwidthExceedDrops.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["bandwidthExceedDrops"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["bandwidthExceedDrops"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["bandwidthExceedDrops"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer["bandwidthExceedDrops"]["observedAt"] = observed_at
                    dict_buffers.append(interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_wred_stats_dict_buffer)
                for cac_stats in queuing_stats.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}cac-stats"):
                    interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_cac_stats_dict_buffer = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_cac_stats_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoDiffservTargetClassifierStatsQueuingStatsCacStats:" + ":".join(interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["id"].split(":")[3:])
                    interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_cac_stats_dict_buffer["type"] = "InterfaceDiffservInfoDiffservTargetClassifierStatsQueuingStatsCacStats"
                    interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_cac_stats_dict_buffer["isPartOf"] = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_cac_stats_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_cac_stats_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer["id"]
                    interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_cac_stats_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    numAdmittedFlows = cac_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}num-admitted-flows")
                    if numAdmittedFlows is not None:
                        element_text = numAdmittedFlows.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_cac_stats_dict_buffer["numAdmittedFlows"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_cac_stats_dict_buffer["numAdmittedFlows"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_cac_stats_dict_buffer["numAdmittedFlows"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_cac_stats_dict_buffer["numAdmittedFlows"]["observedAt"] = observed_at
                    numNonAdmittedFlows = cac_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}num-non-admitted-flows")
                    if numNonAdmittedFlows is not None:
                        element_text = numNonAdmittedFlows.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_cac_stats_dict_buffer["numNonAdmittedFlows"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_cac_stats_dict_buffer["numNonAdmittedFlows"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_cac_stats_dict_buffer["numNonAdmittedFlows"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_cac_stats_dict_buffer["numNonAdmittedFlows"]["observedAt"] = observed_at
                    dict_buffers.append(interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_cac_stats_dict_buffer)
                dict_buffers.append(interface_diffserv_info_diffserv_target_classifier_stats_queuing_stats_dict_buffer)
            for subclass_list in diffserv_target_classifier_stats.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}subclass-list"):
                interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer = {}
                interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassList:" + ":".join(interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["id"].split(":")[3:])
                interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["type"] = "InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassList"
                interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["isPartOf"] = {}
                interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["id"]
                interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["isPartOf"]["observedAt"] = observed_at
                matchType = subclass_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}match-type")
                if matchType is not None:
                    element_text = matchType.text
                    if element_text is not None:
                        interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["matchType"] = {}
                        interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["matchType"]["type"] = "Property"
                        interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["matchType"]["value"] = element_text
                        interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["matchType"]["observedAt"] = observed_at
                for cos_counters in subclass_list.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}cos-counters"):
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListCosCounters:" + ":".join(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"].split(":")[3:])
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["type"] = "InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListCosCounters"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["isPartOf"] = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"]
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    cosMin = cos_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}cos-min")
                    if cosMin is not None:
                        element_text = cosMin.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["cosMin"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["cosMin"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["cosMin"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["cosMin"]["observedAt"] = observed_at
                    cosMax = cos_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}cos-max")
                    if cosMax is not None:
                        element_text = cosMax.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["cosMax"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["cosMax"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["cosMax"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["cosMax"]["observedAt"] = observed_at
                    wredTxPkts = cos_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-pkts")
                    if wredTxPkts is not None:
                        element_text = wredTxPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredTxPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredTxPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredTxPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredTxPkts"]["observedAt"] = observed_at
                    wredTxBytes = cos_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-bytes")
                    if wredTxBytes is not None:
                        element_text = wredTxBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredTxBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredTxBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredTxBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredTxBytes"]["observedAt"] = observed_at
                    wredTailDropPkts = cos_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-pkts")
                    if wredTailDropPkts is not None:
                        element_text = wredTailDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredTailDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredTailDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredTailDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredTailDropPkts"]["observedAt"] = observed_at
                    wredTailDropBytes = cos_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-bytes")
                    if wredTailDropBytes is not None:
                        element_text = wredTailDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredTailDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredTailDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredTailDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredTailDropBytes"]["observedAt"] = observed_at
                    wredEarlyDropPkts = cos_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-pkts")
                    if wredEarlyDropPkts is not None:
                        element_text = wredEarlyDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredEarlyDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredEarlyDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredEarlyDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredEarlyDropPkts"]["observedAt"] = observed_at
                    wredEarlyDropBytes = cos_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-bytes")
                    if wredEarlyDropBytes is not None:
                        element_text = wredEarlyDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredEarlyDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredEarlyDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredEarlyDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer["wredEarlyDropBytes"]["observedAt"] = observed_at
                    dict_buffers.append(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_counters_dict_buffer)
                for cos_default in subclass_list.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}cos-default"):
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListCosDefault:" + ":".join(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"].split(":")[3:])
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["type"] = "InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListCosDefault"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["isPartOf"] = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"]
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    wredTxPkts = cos_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-pkts")
                    if wredTxPkts is not None:
                        element_text = wredTxPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredTxPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredTxPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredTxPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredTxPkts"]["observedAt"] = observed_at
                    wredTxBytes = cos_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-bytes")
                    if wredTxBytes is not None:
                        element_text = wredTxBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredTxBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredTxBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredTxBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredTxBytes"]["observedAt"] = observed_at
                    wredTailDropPkts = cos_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-pkts")
                    if wredTailDropPkts is not None:
                        element_text = wredTailDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredTailDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredTailDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredTailDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredTailDropPkts"]["observedAt"] = observed_at
                    wredTailDropBytes = cos_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-bytes")
                    if wredTailDropBytes is not None:
                        element_text = wredTailDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredTailDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredTailDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredTailDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredTailDropBytes"]["observedAt"] = observed_at
                    wredEarlyDropPkts = cos_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-pkts")
                    if wredEarlyDropPkts is not None:
                        element_text = wredEarlyDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredEarlyDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredEarlyDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredEarlyDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredEarlyDropPkts"]["observedAt"] = observed_at
                    wredEarlyDropBytes = cos_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-bytes")
                    if wredEarlyDropBytes is not None:
                        element_text = wredEarlyDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredEarlyDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredEarlyDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredEarlyDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer["wredEarlyDropBytes"]["observedAt"] = observed_at
                    dict_buffers.append(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_cos_default_dict_buffer)
                for dscp_counters in subclass_list.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dscp-counters"):
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListDscpCounters:" + ":".join(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"].split(":")[3:])
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["type"] = "InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListDscpCounters"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["isPartOf"] = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"]
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    dscpMin = dscp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dscp-min")
                    if dscpMin is not None:
                        element_text = dscpMin.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["dscpMin"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["dscpMin"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["dscpMin"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["dscpMin"]["observedAt"] = observed_at
                    dscpMax = dscp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dscp-max")
                    if dscpMax is not None:
                        element_text = dscpMax.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["dscpMax"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["dscpMax"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["dscpMax"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["dscpMax"]["observedAt"] = observed_at
                    wredTxPkts = dscp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-pkts")
                    if wredTxPkts is not None:
                        element_text = wredTxPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredTxPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredTxPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredTxPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredTxPkts"]["observedAt"] = observed_at
                    wredTxBytes = dscp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-bytes")
                    if wredTxBytes is not None:
                        element_text = wredTxBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredTxBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredTxBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredTxBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredTxBytes"]["observedAt"] = observed_at
                    wredTailDropPkts = dscp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-pkts")
                    if wredTailDropPkts is not None:
                        element_text = wredTailDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredTailDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredTailDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredTailDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredTailDropPkts"]["observedAt"] = observed_at
                    wredTailDropBytes = dscp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-bytes")
                    if wredTailDropBytes is not None:
                        element_text = wredTailDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredTailDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredTailDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredTailDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredTailDropBytes"]["observedAt"] = observed_at
                    wredEarlyDropPkts = dscp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-pkts")
                    if wredEarlyDropPkts is not None:
                        element_text = wredEarlyDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredEarlyDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredEarlyDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredEarlyDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredEarlyDropPkts"]["observedAt"] = observed_at
                    wredEarlyDropBytes = dscp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-bytes")
                    if wredEarlyDropBytes is not None:
                        element_text = wredEarlyDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredEarlyDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredEarlyDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredEarlyDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer["wredEarlyDropBytes"]["observedAt"] = observed_at
                    dict_buffers.append(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_counters_dict_buffer)
                for dscp_default in subclass_list.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dscp-default"):
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListDscpDefault:" + ":".join(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"].split(":")[3:])
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["type"] = "InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListDscpDefault"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["isPartOf"] = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"]
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    wredTxPkts = dscp_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-pkts")
                    if wredTxPkts is not None:
                        element_text = wredTxPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredTxPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredTxPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredTxPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredTxPkts"]["observedAt"] = observed_at
                    wredTxBytes = dscp_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-bytes")
                    if wredTxBytes is not None:
                        element_text = wredTxBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredTxBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredTxBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredTxBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredTxBytes"]["observedAt"] = observed_at
                    wredTailDropPkts = dscp_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-pkts")
                    if wredTailDropPkts is not None:
                        element_text = wredTailDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredTailDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredTailDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredTailDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredTailDropPkts"]["observedAt"] = observed_at
                    wredTailDropBytes = dscp_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-bytes")
                    if wredTailDropBytes is not None:
                        element_text = wredTailDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredTailDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredTailDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredTailDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredTailDropBytes"]["observedAt"] = observed_at
                    wredEarlyDropPkts = dscp_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-pkts")
                    if wredEarlyDropPkts is not None:
                        element_text = wredEarlyDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredEarlyDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredEarlyDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredEarlyDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredEarlyDropPkts"]["observedAt"] = observed_at
                    wredEarlyDropBytes = dscp_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-bytes")
                    if wredEarlyDropBytes is not None:
                        element_text = wredEarlyDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredEarlyDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredEarlyDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredEarlyDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer["wredEarlyDropBytes"]["observedAt"] = observed_at
                    dict_buffers.append(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dscp_default_dict_buffer)
                for discard_class_counters in subclass_list.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}discard-class-counters"):
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListDiscardClassCounters:" + ":".join(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"].split(":")[3:])
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["type"] = "InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListDiscardClassCounters"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["isPartOf"] = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"]
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    discClassMin = discard_class_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}disc-class-min")
                    if discClassMin is not None:
                        element_text = discClassMin.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["discClassMin"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["discClassMin"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["discClassMin"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["discClassMin"]["observedAt"] = observed_at
                    discClassMax = discard_class_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}disc-class-max")
                    if discClassMax is not None:
                        element_text = discClassMax.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["discClassMax"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["discClassMax"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["discClassMax"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["discClassMax"]["observedAt"] = observed_at
                    wredTxPkts = discard_class_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-pkts")
                    if wredTxPkts is not None:
                        element_text = wredTxPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredTxPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredTxPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredTxPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredTxPkts"]["observedAt"] = observed_at
                    wredTxBytes = discard_class_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-bytes")
                    if wredTxBytes is not None:
                        element_text = wredTxBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredTxBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredTxBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredTxBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredTxBytes"]["observedAt"] = observed_at
                    wredTailDropPkts = discard_class_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-pkts")
                    if wredTailDropPkts is not None:
                        element_text = wredTailDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredTailDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredTailDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredTailDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredTailDropPkts"]["observedAt"] = observed_at
                    wredTailDropBytes = discard_class_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-bytes")
                    if wredTailDropBytes is not None:
                        element_text = wredTailDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredTailDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredTailDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredTailDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredTailDropBytes"]["observedAt"] = observed_at
                    wredEarlyDropPkts = discard_class_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-pkts")
                    if wredEarlyDropPkts is not None:
                        element_text = wredEarlyDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredEarlyDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredEarlyDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredEarlyDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredEarlyDropPkts"]["observedAt"] = observed_at
                    wredEarlyDropBytes = discard_class_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-bytes")
                    if wredEarlyDropBytes is not None:
                        element_text = wredEarlyDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredEarlyDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredEarlyDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredEarlyDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer["wredEarlyDropBytes"]["observedAt"] = observed_at
                    dict_buffers.append(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_discard_class_counters_dict_buffer)
                for disc_class_default in subclass_list.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}disc-class-default"):
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListDiscClassDefault:" + ":".join(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"].split(":")[3:])
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["type"] = "InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListDiscClassDefault"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["isPartOf"] = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"]
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    wredTxPkts = disc_class_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-pkts")
                    if wredTxPkts is not None:
                        element_text = wredTxPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredTxPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredTxPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredTxPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredTxPkts"]["observedAt"] = observed_at
                    wredTxBytes = disc_class_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-bytes")
                    if wredTxBytes is not None:
                        element_text = wredTxBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredTxBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredTxBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredTxBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredTxBytes"]["observedAt"] = observed_at
                    wredTailDropPkts = disc_class_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-pkts")
                    if wredTailDropPkts is not None:
                        element_text = wredTailDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredTailDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredTailDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredTailDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredTailDropPkts"]["observedAt"] = observed_at
                    wredTailDropBytes = disc_class_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-bytes")
                    if wredTailDropBytes is not None:
                        element_text = wredTailDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredTailDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredTailDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredTailDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredTailDropBytes"]["observedAt"] = observed_at
                    wredEarlyDropPkts = disc_class_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-pkts")
                    if wredEarlyDropPkts is not None:
                        element_text = wredEarlyDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredEarlyDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredEarlyDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredEarlyDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredEarlyDropPkts"]["observedAt"] = observed_at
                    wredEarlyDropBytes = disc_class_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-bytes")
                    if wredEarlyDropBytes is not None:
                        element_text = wredEarlyDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredEarlyDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredEarlyDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredEarlyDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer["wredEarlyDropBytes"]["observedAt"] = observed_at
                    dict_buffers.append(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_disc_class_default_dict_buffer)
                for precedence_counters in subclass_list.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}precedence-counters"):
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListPrecedenceCounters:" + ":".join(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"].split(":")[3:])
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["type"] = "InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListPrecedenceCounters"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["isPartOf"] = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"]
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    precMin = precedence_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}prec-min")
                    if precMin is not None:
                        element_text = precMin.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["precMin"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["precMin"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["precMin"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["precMin"]["observedAt"] = observed_at
                    precMax = precedence_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}prec-max")
                    if precMax is not None:
                        element_text = precMax.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["precMax"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["precMax"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["precMax"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["precMax"]["observedAt"] = observed_at
                    wredTxPkts = precedence_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-pkts")
                    if wredTxPkts is not None:
                        element_text = wredTxPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredTxPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredTxPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredTxPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredTxPkts"]["observedAt"] = observed_at
                    wredTxBytes = precedence_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-bytes")
                    if wredTxBytes is not None:
                        element_text = wredTxBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredTxBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredTxBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredTxBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredTxBytes"]["observedAt"] = observed_at
                    wredTailDropPkts = precedence_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-pkts")
                    if wredTailDropPkts is not None:
                        element_text = wredTailDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredTailDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredTailDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredTailDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredTailDropPkts"]["observedAt"] = observed_at
                    wredTailDropBytes = precedence_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-bytes")
                    if wredTailDropBytes is not None:
                        element_text = wredTailDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredTailDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredTailDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredTailDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredTailDropBytes"]["observedAt"] = observed_at
                    wredEarlyDropPkts = precedence_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-pkts")
                    if wredEarlyDropPkts is not None:
                        element_text = wredEarlyDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredEarlyDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredEarlyDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredEarlyDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredEarlyDropPkts"]["observedAt"] = observed_at
                    wredEarlyDropBytes = precedence_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-bytes")
                    if wredEarlyDropBytes is not None:
                        element_text = wredEarlyDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredEarlyDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredEarlyDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredEarlyDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer["wredEarlyDropBytes"]["observedAt"] = observed_at
                    dict_buffers.append(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_precedence_counters_dict_buffer)
                for prec_default in subclass_list.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}prec-default"):
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListPrecDefault:" + ":".join(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"].split(":")[3:])
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["type"] = "InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListPrecDefault"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["isPartOf"] = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"]
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    wredTxPkts = prec_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-pkts")
                    if wredTxPkts is not None:
                        element_text = wredTxPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredTxPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredTxPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredTxPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredTxPkts"]["observedAt"] = observed_at
                    wredTxBytes = prec_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-bytes")
                    if wredTxBytes is not None:
                        element_text = wredTxBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredTxBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredTxBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredTxBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredTxBytes"]["observedAt"] = observed_at
                    wredTailDropPkts = prec_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-pkts")
                    if wredTailDropPkts is not None:
                        element_text = wredTailDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredTailDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredTailDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredTailDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredTailDropPkts"]["observedAt"] = observed_at
                    wredTailDropBytes = prec_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-bytes")
                    if wredTailDropBytes is not None:
                        element_text = wredTailDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredTailDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredTailDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredTailDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredTailDropBytes"]["observedAt"] = observed_at
                    wredEarlyDropPkts = prec_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-pkts")
                    if wredEarlyDropPkts is not None:
                        element_text = wredEarlyDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredEarlyDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredEarlyDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredEarlyDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredEarlyDropPkts"]["observedAt"] = observed_at
                    wredEarlyDropBytes = prec_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-bytes")
                    if wredEarlyDropBytes is not None:
                        element_text = wredEarlyDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredEarlyDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredEarlyDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredEarlyDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer["wredEarlyDropBytes"]["observedAt"] = observed_at
                    dict_buffers.append(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_prec_default_dict_buffer)
                for mpls_exp_counters in subclass_list.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}mpls-exp-counters"):
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListMplsExpCounters:" + ":".join(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"].split(":")[3:])
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["type"] = "InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListMplsExpCounters"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["isPartOf"] = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"]
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    expMin = mpls_exp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}exp-min")
                    if expMin is not None:
                        element_text = expMin.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["expMin"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["expMin"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["expMin"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["expMin"]["observedAt"] = observed_at
                    expMax = mpls_exp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}exp-max")
                    if expMax is not None:
                        element_text = expMax.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["expMax"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["expMax"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["expMax"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["expMax"]["observedAt"] = observed_at
                    wredTxPkts = mpls_exp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-pkts")
                    if wredTxPkts is not None:
                        element_text = wredTxPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredTxPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredTxPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredTxPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredTxPkts"]["observedAt"] = observed_at
                    wredTxBytes = mpls_exp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-bytes")
                    if wredTxBytes is not None:
                        element_text = wredTxBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredTxBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredTxBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredTxBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredTxBytes"]["observedAt"] = observed_at
                    wredTailDropPkts = mpls_exp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-pkts")
                    if wredTailDropPkts is not None:
                        element_text = wredTailDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredTailDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredTailDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredTailDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredTailDropPkts"]["observedAt"] = observed_at
                    wredTailDropBytes = mpls_exp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-bytes")
                    if wredTailDropBytes is not None:
                        element_text = wredTailDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredTailDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredTailDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredTailDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredTailDropBytes"]["observedAt"] = observed_at
                    wredEarlyDropPkts = mpls_exp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-pkts")
                    if wredEarlyDropPkts is not None:
                        element_text = wredEarlyDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredEarlyDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredEarlyDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredEarlyDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredEarlyDropPkts"]["observedAt"] = observed_at
                    wredEarlyDropBytes = mpls_exp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-bytes")
                    if wredEarlyDropBytes is not None:
                        element_text = wredEarlyDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredEarlyDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredEarlyDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredEarlyDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer["wredEarlyDropBytes"]["observedAt"] = observed_at
                    dict_buffers.append(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_counters_dict_buffer)
                for mpls_exp_default in subclass_list.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}mpls-exp-default"):
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListMplsExpDefault:" + ":".join(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"].split(":")[3:])
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["type"] = "InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListMplsExpDefault"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["isPartOf"] = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"]
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    wredTxPkts = mpls_exp_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-pkts")
                    if wredTxPkts is not None:
                        element_text = wredTxPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredTxPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredTxPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredTxPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredTxPkts"]["observedAt"] = observed_at
                    wredTxBytes = mpls_exp_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-bytes")
                    if wredTxBytes is not None:
                        element_text = wredTxBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredTxBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredTxBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredTxBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredTxBytes"]["observedAt"] = observed_at
                    wredTailDropPkts = mpls_exp_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-pkts")
                    if wredTailDropPkts is not None:
                        element_text = wredTailDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredTailDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredTailDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredTailDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredTailDropPkts"]["observedAt"] = observed_at
                    wredTailDropBytes = mpls_exp_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-bytes")
                    if wredTailDropBytes is not None:
                        element_text = wredTailDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredTailDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredTailDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredTailDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredTailDropBytes"]["observedAt"] = observed_at
                    wredEarlyDropPkts = mpls_exp_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-pkts")
                    if wredEarlyDropPkts is not None:
                        element_text = wredEarlyDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredEarlyDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredEarlyDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredEarlyDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredEarlyDropPkts"]["observedAt"] = observed_at
                    wredEarlyDropBytes = mpls_exp_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-bytes")
                    if wredEarlyDropBytes is not None:
                        element_text = wredEarlyDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredEarlyDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredEarlyDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredEarlyDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer["wredEarlyDropBytes"]["observedAt"] = observed_at
                    dict_buffers.append(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_mpls_exp_default_dict_buffer)
                for dei_counters in subclass_list.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dei-counters"):
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListDeiCounters:" + ":".join(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"].split(":")[3:])
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["type"] = "InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListDeiCounters"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["isPartOf"] = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"]
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    deiMin = dei_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dei-min")
                    if deiMin is not None:
                        element_text = deiMin.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["deiMin"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["deiMin"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["deiMin"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["deiMin"]["observedAt"] = observed_at
                    deiMax = dei_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dei-max")
                    if deiMax is not None:
                        element_text = deiMax.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["deiMax"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["deiMax"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["deiMax"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["deiMax"]["observedAt"] = observed_at
                    wredTxPkts = dei_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-pkts")
                    if wredTxPkts is not None:
                        element_text = wredTxPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredTxPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredTxPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredTxPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredTxPkts"]["observedAt"] = observed_at
                    wredTxBytes = dei_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-bytes")
                    if wredTxBytes is not None:
                        element_text = wredTxBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredTxBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredTxBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredTxBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredTxBytes"]["observedAt"] = observed_at
                    wredTailDropPkts = dei_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-pkts")
                    if wredTailDropPkts is not None:
                        element_text = wredTailDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredTailDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredTailDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredTailDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredTailDropPkts"]["observedAt"] = observed_at
                    wredTailDropBytes = dei_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-bytes")
                    if wredTailDropBytes is not None:
                        element_text = wredTailDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredTailDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredTailDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredTailDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredTailDropBytes"]["observedAt"] = observed_at
                    wredEarlyDropPkts = dei_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-pkts")
                    if wredEarlyDropPkts is not None:
                        element_text = wredEarlyDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredEarlyDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredEarlyDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredEarlyDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredEarlyDropPkts"]["observedAt"] = observed_at
                    wredEarlyDropBytes = dei_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-bytes")
                    if wredEarlyDropBytes is not None:
                        element_text = wredEarlyDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredEarlyDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredEarlyDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredEarlyDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer["wredEarlyDropBytes"]["observedAt"] = observed_at
                    dict_buffers.append(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counters_dict_buffer)
                for dei_counts_default in subclass_list.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dei-counts-default"):
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListDeiCountsDefault:" + ":".join(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"].split(":")[3:])
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["type"] = "InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListDeiCountsDefault"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["isPartOf"] = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"]
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    wredTxPkts = dei_counts_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-pkts")
                    if wredTxPkts is not None:
                        element_text = wredTxPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredTxPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredTxPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredTxPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredTxPkts"]["observedAt"] = observed_at
                    wredTxBytes = dei_counts_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-bytes")
                    if wredTxBytes is not None:
                        element_text = wredTxBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredTxBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredTxBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredTxBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredTxBytes"]["observedAt"] = observed_at
                    wredTailDropPkts = dei_counts_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-pkts")
                    if wredTailDropPkts is not None:
                        element_text = wredTailDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredTailDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredTailDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredTailDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredTailDropPkts"]["observedAt"] = observed_at
                    wredTailDropBytes = dei_counts_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-bytes")
                    if wredTailDropBytes is not None:
                        element_text = wredTailDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredTailDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredTailDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredTailDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredTailDropBytes"]["observedAt"] = observed_at
                    wredEarlyDropPkts = dei_counts_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-pkts")
                    if wredEarlyDropPkts is not None:
                        element_text = wredEarlyDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredEarlyDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredEarlyDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredEarlyDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredEarlyDropPkts"]["observedAt"] = observed_at
                    wredEarlyDropBytes = dei_counts_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-bytes")
                    if wredEarlyDropBytes is not None:
                        element_text = wredEarlyDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredEarlyDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredEarlyDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredEarlyDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer["wredEarlyDropBytes"]["observedAt"] = observed_at
                    dict_buffers.append(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dei_counts_default_dict_buffer)
                for clp_counters in subclass_list.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}clp-counters"):
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListClpCounters:" + ":".join(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"].split(":")[3:])
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["type"] = "InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListClpCounters"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["isPartOf"] = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"]
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    clpVal = clp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}clp-val")
                    if clpVal is not None:
                        element_text = clpVal.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["clpVal"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["clpVal"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["clpVal"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["clpVal"]["observedAt"] = observed_at
                    wredTxPkts = clp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-pkts")
                    if wredTxPkts is not None:
                        element_text = wredTxPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredTxPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredTxPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredTxPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredTxPkts"]["observedAt"] = observed_at
                    wredTxBytes = clp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-bytes")
                    if wredTxBytes is not None:
                        element_text = wredTxBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredTxBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredTxBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredTxBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredTxBytes"]["observedAt"] = observed_at
                    wredTailDropPkts = clp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-pkts")
                    if wredTailDropPkts is not None:
                        element_text = wredTailDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredTailDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredTailDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredTailDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredTailDropPkts"]["observedAt"] = observed_at
                    wredTailDropBytes = clp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-bytes")
                    if wredTailDropBytes is not None:
                        element_text = wredTailDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredTailDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredTailDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredTailDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredTailDropBytes"]["observedAt"] = observed_at
                    wredEarlyDropPkts = clp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-pkts")
                    if wredEarlyDropPkts is not None:
                        element_text = wredEarlyDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredEarlyDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredEarlyDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredEarlyDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredEarlyDropPkts"]["observedAt"] = observed_at
                    wredEarlyDropBytes = clp_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-bytes")
                    if wredEarlyDropBytes is not None:
                        element_text = wredEarlyDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredEarlyDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredEarlyDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredEarlyDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer["wredEarlyDropBytes"]["observedAt"] = observed_at
                    dict_buffers.append(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_counters_dict_buffer)
                for clp_default in subclass_list.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}clp-default"):
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListClpDefault:" + ":".join(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"].split(":")[3:])
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["type"] = "InterfaceDiffservInfoDiffservTargetClassifierStatsSubclassListClpDefault"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["isPartOf"] = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer["id"]
                    interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    wredTxPkts = clp_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-pkts")
                    if wredTxPkts is not None:
                        element_text = wredTxPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredTxPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredTxPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredTxPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredTxPkts"]["observedAt"] = observed_at
                    wredTxBytes = clp_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tx-bytes")
                    if wredTxBytes is not None:
                        element_text = wredTxBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredTxBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredTxBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredTxBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredTxBytes"]["observedAt"] = observed_at
                    wredTailDropPkts = clp_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-pkts")
                    if wredTailDropPkts is not None:
                        element_text = wredTailDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredTailDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredTailDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredTailDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredTailDropPkts"]["observedAt"] = observed_at
                    wredTailDropBytes = clp_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-tail-drop-bytes")
                    if wredTailDropBytes is not None:
                        element_text = wredTailDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredTailDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredTailDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredTailDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredTailDropBytes"]["observedAt"] = observed_at
                    wredEarlyDropPkts = clp_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-pkts")
                    if wredEarlyDropPkts is not None:
                        element_text = wredEarlyDropPkts.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredEarlyDropPkts"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredEarlyDropPkts"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredEarlyDropPkts"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredEarlyDropPkts"]["observedAt"] = observed_at
                    wredEarlyDropBytes = clp_default.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wred-early-drop-bytes")
                    if wredEarlyDropBytes is not None:
                        element_text = wredEarlyDropBytes.text
                        if element_text is not None:
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredEarlyDropBytes"] = {}
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredEarlyDropBytes"]["type"] = "Property"
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredEarlyDropBytes"]["value"] = int(element_text)
                            interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer["wredEarlyDropBytes"]["observedAt"] = observed_at
                    dict_buffers.append(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_clp_default_dict_buffer)
                dict_buffers.append(interface_diffserv_info_diffserv_target_classifier_stats_subclass_list_dict_buffer)
            for marking_dscp_stats_val in root.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marking-dscp-stats-val"):
                marking_dscp_stats_val_dict_buffer = {}
                marking_dscp_stats_val_dict_buffer["id"] = "urn:ngsi-ld:MarkingDscpStatsVal"
                marking_dscp_stats_val_dict_buffer["type"] = "MarkingDscpStatsVal"
                dscp = marking_dscp_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dscp")
                if dscp is not None:
                    element_text = dscp.text
                    if element_text is not None:
                        marking_dscp_stats_val_dict_buffer["dscp"] = {}
                        marking_dscp_stats_val_dict_buffer["dscp"]["type"] = "Property"
                        marking_dscp_stats_val_dict_buffer["dscp"]["value"] = int(element_text)
                        marking_dscp_stats_val_dict_buffer["dscp"]["observedAt"] = observed_at
                markedPkts = marking_dscp_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marked-pkts")
                if markedPkts is not None:
                    element_text = markedPkts.text
                    if element_text is not None:
                        marking_dscp_stats_val_dict_buffer["markedPkts"] = {}
                        marking_dscp_stats_val_dict_buffer["markedPkts"]["type"] = "Property"
                        marking_dscp_stats_val_dict_buffer["markedPkts"]["value"] = int(element_text)
                        marking_dscp_stats_val_dict_buffer["markedPkts"]["observedAt"] = observed_at
                dict_buffers.append(marking_dscp_stats_val_dict_buffer)
            for marking_dscp_tunnel_stats_val in root.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marking-dscp-tunnel-stats-val"):
                marking_dscp_tunnel_stats_val_dict_buffer = {}
                marking_dscp_tunnel_stats_val_dict_buffer["id"] = "urn:ngsi-ld:MarkingDscpTunnelStatsVal"
                marking_dscp_tunnel_stats_val_dict_buffer["type"] = "MarkingDscpTunnelStatsVal"
                dscpVal = marking_dscp_tunnel_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dscp-val")
                if dscpVal is not None:
                    element_text = dscpVal.text
                    if element_text is not None:
                        marking_dscp_tunnel_stats_val_dict_buffer["dscpVal"] = {}
                        marking_dscp_tunnel_stats_val_dict_buffer["dscpVal"]["type"] = "Property"
                        marking_dscp_tunnel_stats_val_dict_buffer["dscpVal"]["value"] = int(element_text)
                        marking_dscp_tunnel_stats_val_dict_buffer["dscpVal"]["observedAt"] = observed_at
                markedPkts = marking_dscp_tunnel_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marked-pkts")
                if markedPkts is not None:
                    element_text = markedPkts.text
                    if element_text is not None:
                        marking_dscp_tunnel_stats_val_dict_buffer["markedPkts"] = {}
                        marking_dscp_tunnel_stats_val_dict_buffer["markedPkts"]["type"] = "Property"
                        marking_dscp_tunnel_stats_val_dict_buffer["markedPkts"]["value"] = int(element_text)
                        marking_dscp_tunnel_stats_val_dict_buffer["markedPkts"]["observedAt"] = observed_at
                dict_buffers.append(marking_dscp_tunnel_stats_val_dict_buffer)
            for marking_cos_stats_val in root.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marking-cos-stats-val"):
                marking_cos_stats_val_dict_buffer = {}
                marking_cos_stats_val_dict_buffer["id"] = "urn:ngsi-ld:MarkingCosStatsVal"
                marking_cos_stats_val_dict_buffer["type"] = "MarkingCosStatsVal"
                cosVal = marking_cos_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}cos-val")
                if cosVal is not None:
                    element_text = cosVal.text
                    if element_text is not None:
                        marking_cos_stats_val_dict_buffer["cosVal"] = {}
                        marking_cos_stats_val_dict_buffer["cosVal"]["type"] = "Property"
                        marking_cos_stats_val_dict_buffer["cosVal"]["value"] = int(element_text)
                        marking_cos_stats_val_dict_buffer["cosVal"]["observedAt"] = observed_at
                markedPkts = marking_cos_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marked-pkts")
                if markedPkts is not None:
                    element_text = markedPkts.text
                    if element_text is not None:
                        marking_cos_stats_val_dict_buffer["markedPkts"] = {}
                        marking_cos_stats_val_dict_buffer["markedPkts"]["type"] = "Property"
                        marking_cos_stats_val_dict_buffer["markedPkts"]["value"] = int(element_text)
                        marking_cos_stats_val_dict_buffer["markedPkts"]["observedAt"] = observed_at
                dict_buffers.append(marking_cos_stats_val_dict_buffer)
            for marking_cos_inner_stats_val in root.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marking-cos-inner-stats-val"):
                marking_cos_inner_stats_val_dict_buffer = {}
                marking_cos_inner_stats_val_dict_buffer["id"] = "urn:ngsi-ld:MarkingCosInnerStatsVal"
                marking_cos_inner_stats_val_dict_buffer["type"] = "MarkingCosInnerStatsVal"
                cosInnerVal = marking_cos_inner_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}cos-inner-val")
                if cosInnerVal is not None:
                    element_text = cosInnerVal.text
                    if element_text is not None:
                        marking_cos_inner_stats_val_dict_buffer["cosInnerVal"] = {}
                        marking_cos_inner_stats_val_dict_buffer["cosInnerVal"]["type"] = "Property"
                        marking_cos_inner_stats_val_dict_buffer["cosInnerVal"]["value"] = int(element_text)
                        marking_cos_inner_stats_val_dict_buffer["cosInnerVal"]["observedAt"] = observed_at
                markedPkts = marking_cos_inner_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marked-pkts")
                if markedPkts is not None:
                    element_text = markedPkts.text
                    if element_text is not None:
                        marking_cos_inner_stats_val_dict_buffer["markedPkts"] = {}
                        marking_cos_inner_stats_val_dict_buffer["markedPkts"]["type"] = "Property"
                        marking_cos_inner_stats_val_dict_buffer["markedPkts"]["value"] = int(element_text)
                        marking_cos_inner_stats_val_dict_buffer["markedPkts"]["observedAt"] = observed_at
                dict_buffers.append(marking_cos_inner_stats_val_dict_buffer)
            for marking_discard_class_stats_val in root.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marking-discard-class-stats-val"):
                marking_discard_class_stats_val_dict_buffer = {}
                marking_discard_class_stats_val_dict_buffer["id"] = "urn:ngsi-ld:MarkingDiscardClassStatsVal"
                marking_discard_class_stats_val_dict_buffer["type"] = "MarkingDiscardClassStatsVal"
                discClassVal = marking_discard_class_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}disc-class-val")
                if discClassVal is not None:
                    element_text = discClassVal.text
                    if element_text is not None:
                        marking_discard_class_stats_val_dict_buffer["discClassVal"] = {}
                        marking_discard_class_stats_val_dict_buffer["discClassVal"]["type"] = "Property"
                        marking_discard_class_stats_val_dict_buffer["discClassVal"]["value"] = int(element_text)
                        marking_discard_class_stats_val_dict_buffer["discClassVal"]["observedAt"] = observed_at
                markedPkts = marking_discard_class_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marked-pkts")
                if markedPkts is not None:
                    element_text = markedPkts.text
                    if element_text is not None:
                        marking_discard_class_stats_val_dict_buffer["markedPkts"] = {}
                        marking_discard_class_stats_val_dict_buffer["markedPkts"]["type"] = "Property"
                        marking_discard_class_stats_val_dict_buffer["markedPkts"]["value"] = int(element_text)
                        marking_discard_class_stats_val_dict_buffer["markedPkts"]["observedAt"] = observed_at
                dict_buffers.append(marking_discard_class_stats_val_dict_buffer)
            for marking_qos_grp_stats_val in root.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marking-qos-grp-stats-val"):
                marking_qos_grp_stats_val_dict_buffer = {}
                marking_qos_grp_stats_val_dict_buffer["id"] = "urn:ngsi-ld:MarkingQosGrpStatsVal"
                marking_qos_grp_stats_val_dict_buffer["type"] = "MarkingQosGrpStatsVal"
                qosGrpVal = marking_qos_grp_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}qos-grp-val")
                if qosGrpVal is not None:
                    element_text = qosGrpVal.text
                    if element_text is not None:
                        marking_qos_grp_stats_val_dict_buffer["qosGrpVal"] = {}
                        marking_qos_grp_stats_val_dict_buffer["qosGrpVal"]["type"] = "Property"
                        marking_qos_grp_stats_val_dict_buffer["qosGrpVal"]["value"] = int(element_text)
                        marking_qos_grp_stats_val_dict_buffer["qosGrpVal"]["observedAt"] = observed_at
                markedPkts = marking_qos_grp_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marked-pkts")
                if markedPkts is not None:
                    element_text = markedPkts.text
                    if element_text is not None:
                        marking_qos_grp_stats_val_dict_buffer["markedPkts"] = {}
                        marking_qos_grp_stats_val_dict_buffer["markedPkts"]["type"] = "Property"
                        marking_qos_grp_stats_val_dict_buffer["markedPkts"]["value"] = int(element_text)
                        marking_qos_grp_stats_val_dict_buffer["markedPkts"]["observedAt"] = observed_at
                dict_buffers.append(marking_qos_grp_stats_val_dict_buffer)
            for marking_prec_stats_val in root.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marking-prec-stats-val"):
                marking_prec_stats_val_dict_buffer = {}
                marking_prec_stats_val_dict_buffer["id"] = "urn:ngsi-ld:MarkingPrecStatsVal"
                marking_prec_stats_val_dict_buffer["type"] = "MarkingPrecStatsVal"
                precVal = marking_prec_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}prec-val")
                if precVal is not None:
                    element_text = precVal.text
                    if element_text is not None:
                        marking_prec_stats_val_dict_buffer["precVal"] = {}
                        marking_prec_stats_val_dict_buffer["precVal"]["type"] = "Property"
                        marking_prec_stats_val_dict_buffer["precVal"]["value"] = int(element_text)
                        marking_prec_stats_val_dict_buffer["precVal"]["observedAt"] = observed_at
                markedPkts = marking_prec_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marked-pkts")
                if markedPkts is not None:
                    element_text = markedPkts.text
                    if element_text is not None:
                        marking_prec_stats_val_dict_buffer["markedPkts"] = {}
                        marking_prec_stats_val_dict_buffer["markedPkts"]["type"] = "Property"
                        marking_prec_stats_val_dict_buffer["markedPkts"]["value"] = int(element_text)
                        marking_prec_stats_val_dict_buffer["markedPkts"]["observedAt"] = observed_at
                dict_buffers.append(marking_prec_stats_val_dict_buffer)
            for marking_prec_tunnel_stats_val in root.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marking-prec-tunnel-stats-val"):
                marking_prec_tunnel_stats_val_dict_buffer = {}
                marking_prec_tunnel_stats_val_dict_buffer["id"] = "urn:ngsi-ld:MarkingPrecTunnelStatsVal"
                marking_prec_tunnel_stats_val_dict_buffer["type"] = "MarkingPrecTunnelStatsVal"
                precVal = marking_prec_tunnel_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}prec-val")
                if precVal is not None:
                    element_text = precVal.text
                    if element_text is not None:
                        marking_prec_tunnel_stats_val_dict_buffer["precVal"] = {}
                        marking_prec_tunnel_stats_val_dict_buffer["precVal"]["type"] = "Property"
                        marking_prec_tunnel_stats_val_dict_buffer["precVal"]["value"] = int(element_text)
                        marking_prec_tunnel_stats_val_dict_buffer["precVal"]["observedAt"] = observed_at
                markedPkts = marking_prec_tunnel_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marked-pkts")
                if markedPkts is not None:
                    element_text = markedPkts.text
                    if element_text is not None:
                        marking_prec_tunnel_stats_val_dict_buffer["markedPkts"] = {}
                        marking_prec_tunnel_stats_val_dict_buffer["markedPkts"]["type"] = "Property"
                        marking_prec_tunnel_stats_val_dict_buffer["markedPkts"]["value"] = int(element_text)
                        marking_prec_tunnel_stats_val_dict_buffer["markedPkts"]["observedAt"] = observed_at
                dict_buffers.append(marking_prec_tunnel_stats_val_dict_buffer)
            for marking_mpls_exp_imp_stats_val in root.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marking-mpls-exp-imp-stats-val"):
                marking_mpls_exp_imp_stats_val_dict_buffer = {}
                marking_mpls_exp_imp_stats_val_dict_buffer["id"] = "urn:ngsi-ld:MarkingMplsExpImpStatsVal"
                marking_mpls_exp_imp_stats_val_dict_buffer["type"] = "MarkingMplsExpImpStatsVal"
                mplsExpImpVal = marking_mpls_exp_imp_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}mpls-exp-imp-val")
                if mplsExpImpVal is not None:
                    element_text = mplsExpImpVal.text
                    if element_text is not None:
                        marking_mpls_exp_imp_stats_val_dict_buffer["mplsExpImpVal"] = {}
                        marking_mpls_exp_imp_stats_val_dict_buffer["mplsExpImpVal"]["type"] = "Property"
                        marking_mpls_exp_imp_stats_val_dict_buffer["mplsExpImpVal"]["value"] = int(element_text)
                        marking_mpls_exp_imp_stats_val_dict_buffer["mplsExpImpVal"]["observedAt"] = observed_at
                markedPkts = marking_mpls_exp_imp_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marked-pkts")
                if markedPkts is not None:
                    element_text = markedPkts.text
                    if element_text is not None:
                        marking_mpls_exp_imp_stats_val_dict_buffer["markedPkts"] = {}
                        marking_mpls_exp_imp_stats_val_dict_buffer["markedPkts"]["type"] = "Property"
                        marking_mpls_exp_imp_stats_val_dict_buffer["markedPkts"]["value"] = int(element_text)
                        marking_mpls_exp_imp_stats_val_dict_buffer["markedPkts"]["observedAt"] = observed_at
                dict_buffers.append(marking_mpls_exp_imp_stats_val_dict_buffer)
            for marking_mpls_exp_top_stats_val in root.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marking-mpls-exp-top-stats-val"):
                marking_mpls_exp_top_stats_val_dict_buffer = {}
                marking_mpls_exp_top_stats_val_dict_buffer["id"] = "urn:ngsi-ld:MarkingMplsExpTopStatsVal"
                marking_mpls_exp_top_stats_val_dict_buffer["type"] = "MarkingMplsExpTopStatsVal"
                mplsExpTopVal = marking_mpls_exp_top_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}mpls-exp-top-val")
                if mplsExpTopVal is not None:
                    element_text = mplsExpTopVal.text
                    if element_text is not None:
                        marking_mpls_exp_top_stats_val_dict_buffer["mplsExpTopVal"] = {}
                        marking_mpls_exp_top_stats_val_dict_buffer["mplsExpTopVal"]["type"] = "Property"
                        marking_mpls_exp_top_stats_val_dict_buffer["mplsExpTopVal"]["value"] = int(element_text)
                        marking_mpls_exp_top_stats_val_dict_buffer["mplsExpTopVal"]["observedAt"] = observed_at
                markedPkts = marking_mpls_exp_top_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marked-pkts")
                if markedPkts is not None:
                    element_text = markedPkts.text
                    if element_text is not None:
                        marking_mpls_exp_top_stats_val_dict_buffer["markedPkts"] = {}
                        marking_mpls_exp_top_stats_val_dict_buffer["markedPkts"]["type"] = "Property"
                        marking_mpls_exp_top_stats_val_dict_buffer["markedPkts"]["value"] = int(element_text)
                        marking_mpls_exp_top_stats_val_dict_buffer["markedPkts"]["observedAt"] = observed_at
                dict_buffers.append(marking_mpls_exp_top_stats_val_dict_buffer)
            for marking_fr_de_stats_val in root.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marking-fr-de-stats-val"):
                marking_fr_de_stats_val_dict_buffer = {}
                marking_fr_de_stats_val_dict_buffer["id"] = "urn:ngsi-ld:MarkingFrDeStatsVal"
                marking_fr_de_stats_val_dict_buffer["type"] = "MarkingFrDeStatsVal"
                frDe = marking_fr_de_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}fr-de")
                if frDe is not None:
                    element_text = frDe.text
                    if element_text is not None:
                        marking_fr_de_stats_val_dict_buffer["frDe"] = {}
                        marking_fr_de_stats_val_dict_buffer["frDe"]["type"] = "Property"
                        marking_fr_de_stats_val_dict_buffer["frDe"]["value"] = eval(element_text.capitalize())
                        marking_fr_de_stats_val_dict_buffer["frDe"]["observedAt"] = observed_at
                markedPkts = marking_fr_de_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marked-pkts")
                if markedPkts is not None:
                    element_text = markedPkts.text
                    if element_text is not None:
                        marking_fr_de_stats_val_dict_buffer["markedPkts"] = {}
                        marking_fr_de_stats_val_dict_buffer["markedPkts"]["type"] = "Property"
                        marking_fr_de_stats_val_dict_buffer["markedPkts"]["value"] = int(element_text)
                        marking_fr_de_stats_val_dict_buffer["markedPkts"]["observedAt"] = observed_at
                dict_buffers.append(marking_fr_de_stats_val_dict_buffer)
            for marking_fr_fecn_becn_stats_val in root.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marking-fr-fecn-becn-stats-val"):
                marking_fr_fecn_becn_stats_val_dict_buffer = {}
                marking_fr_fecn_becn_stats_val_dict_buffer["id"] = "urn:ngsi-ld:MarkingFrFecnBecnStatsVal"
                marking_fr_fecn_becn_stats_val_dict_buffer["type"] = "MarkingFrFecnBecnStatsVal"
                fecnBecnVal = marking_fr_fecn_becn_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}fecn-becn-val")
                if fecnBecnVal is not None:
                    element_text = fecnBecnVal.text
                    if element_text is not None:
                        marking_fr_fecn_becn_stats_val_dict_buffer["fecnBecnVal"] = {}
                        marking_fr_fecn_becn_stats_val_dict_buffer["fecnBecnVal"]["type"] = "Property"
                        marking_fr_fecn_becn_stats_val_dict_buffer["fecnBecnVal"]["value"] = int(element_text)
                        marking_fr_fecn_becn_stats_val_dict_buffer["fecnBecnVal"]["observedAt"] = observed_at
                markedPkts = marking_fr_fecn_becn_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marked-pkts")
                if markedPkts is not None:
                    element_text = markedPkts.text
                    if element_text is not None:
                        marking_fr_fecn_becn_stats_val_dict_buffer["markedPkts"] = {}
                        marking_fr_fecn_becn_stats_val_dict_buffer["markedPkts"]["type"] = "Property"
                        marking_fr_fecn_becn_stats_val_dict_buffer["markedPkts"]["value"] = int(element_text)
                        marking_fr_fecn_becn_stats_val_dict_buffer["markedPkts"]["observedAt"] = observed_at
                dict_buffers.append(marking_fr_fecn_becn_stats_val_dict_buffer)
            for marking_atm_clp_stats_val in root.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marking-atm-clp-stats-val"):
                marking_atm_clp_stats_val_dict_buffer = {}
                marking_atm_clp_stats_val_dict_buffer["id"] = "urn:ngsi-ld:MarkingAtmClpStatsVal"
                marking_atm_clp_stats_val_dict_buffer["type"] = "MarkingAtmClpStatsVal"
                atmClpVal = marking_atm_clp_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}atm-clp-val")
                if atmClpVal is not None:
                    element_text = atmClpVal.text
                    if element_text is not None:
                        marking_atm_clp_stats_val_dict_buffer["atmClpVal"] = {}
                        marking_atm_clp_stats_val_dict_buffer["atmClpVal"]["type"] = "Property"
                        marking_atm_clp_stats_val_dict_buffer["atmClpVal"]["value"] = int(element_text)
                        marking_atm_clp_stats_val_dict_buffer["atmClpVal"]["observedAt"] = observed_at
                markedPkts = marking_atm_clp_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marked-pkts")
                if markedPkts is not None:
                    element_text = markedPkts.text
                    if element_text is not None:
                        marking_atm_clp_stats_val_dict_buffer["markedPkts"] = {}
                        marking_atm_clp_stats_val_dict_buffer["markedPkts"]["type"] = "Property"
                        marking_atm_clp_stats_val_dict_buffer["markedPkts"]["value"] = int(element_text)
                        marking_atm_clp_stats_val_dict_buffer["markedPkts"]["observedAt"] = observed_at
                dict_buffers.append(marking_atm_clp_stats_val_dict_buffer)
            for marking_vlan_inner_stats_val in root.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marking-vlan-inner-stats-val"):
                marking_vlan_inner_stats_val_dict_buffer = {}
                marking_vlan_inner_stats_val_dict_buffer["id"] = "urn:ngsi-ld:MarkingVlanInnerStatsVal"
                marking_vlan_inner_stats_val_dict_buffer["type"] = "MarkingVlanInnerStatsVal"
                vlanInnerVal = marking_vlan_inner_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}vlan-inner-val")
                if vlanInnerVal is not None:
                    element_text = vlanInnerVal.text
                    if element_text is not None:
                        marking_vlan_inner_stats_val_dict_buffer["vlanInnerVal"] = {}
                        marking_vlan_inner_stats_val_dict_buffer["vlanInnerVal"]["type"] = "Property"
                        marking_vlan_inner_stats_val_dict_buffer["vlanInnerVal"]["value"] = int(element_text)
                        marking_vlan_inner_stats_val_dict_buffer["vlanInnerVal"]["observedAt"] = observed_at
                markedPkts = marking_vlan_inner_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marked-pkts")
                if markedPkts is not None:
                    element_text = markedPkts.text
                    if element_text is not None:
                        marking_vlan_inner_stats_val_dict_buffer["markedPkts"] = {}
                        marking_vlan_inner_stats_val_dict_buffer["markedPkts"]["type"] = "Property"
                        marking_vlan_inner_stats_val_dict_buffer["markedPkts"]["value"] = int(element_text)
                        marking_vlan_inner_stats_val_dict_buffer["markedPkts"]["observedAt"] = observed_at
                dict_buffers.append(marking_vlan_inner_stats_val_dict_buffer)
            for marking_dei_stats_val in root.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marking-dei-stats-val"):
                marking_dei_stats_val_dict_buffer = {}
                marking_dei_stats_val_dict_buffer["id"] = "urn:ngsi-ld:MarkingDeiStatsVal"
                marking_dei_stats_val_dict_buffer["type"] = "MarkingDeiStatsVal"
                deiImpValue = marking_dei_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dei-imp-value")
                if deiImpValue is not None:
                    element_text = deiImpValue.text
                    if element_text is not None:
                        marking_dei_stats_val_dict_buffer["deiImpValue"] = {}
                        marking_dei_stats_val_dict_buffer["deiImpValue"]["type"] = "Property"
                        marking_dei_stats_val_dict_buffer["deiImpValue"]["value"] = int(element_text)
                        marking_dei_stats_val_dict_buffer["deiImpValue"]["observedAt"] = observed_at
                markedPkts = marking_dei_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marked-pkts")
                if markedPkts is not None:
                    element_text = markedPkts.text
                    if element_text is not None:
                        marking_dei_stats_val_dict_buffer["markedPkts"] = {}
                        marking_dei_stats_val_dict_buffer["markedPkts"]["type"] = "Property"
                        marking_dei_stats_val_dict_buffer["markedPkts"]["value"] = int(element_text)
                        marking_dei_stats_val_dict_buffer["markedPkts"]["observedAt"] = observed_at
                dict_buffers.append(marking_dei_stats_val_dict_buffer)
            for marking_dei_imp_stats_val in root.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marking-dei-imp-stats-val"):
                marking_dei_imp_stats_val_dict_buffer = {}
                marking_dei_imp_stats_val_dict_buffer["id"] = "urn:ngsi-ld:MarkingDeiImpStatsVal"
                marking_dei_imp_stats_val_dict_buffer["type"] = "MarkingDeiImpStatsVal"
                deiImpValue = marking_dei_imp_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dei-imp-value")
                if deiImpValue is not None:
                    element_text = deiImpValue.text
                    if element_text is not None:
                        marking_dei_imp_stats_val_dict_buffer["deiImpValue"] = {}
                        marking_dei_imp_stats_val_dict_buffer["deiImpValue"]["type"] = "Property"
                        marking_dei_imp_stats_val_dict_buffer["deiImpValue"]["value"] = int(element_text)
                        marking_dei_imp_stats_val_dict_buffer["deiImpValue"]["observedAt"] = observed_at
                markedPkts = marking_dei_imp_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marked-pkts")
                if markedPkts is not None:
                    element_text = markedPkts.text
                    if element_text is not None:
                        marking_dei_imp_stats_val_dict_buffer["markedPkts"] = {}
                        marking_dei_imp_stats_val_dict_buffer["markedPkts"]["type"] = "Property"
                        marking_dei_imp_stats_val_dict_buffer["markedPkts"]["value"] = int(element_text)
                        marking_dei_imp_stats_val_dict_buffer["markedPkts"]["observedAt"] = observed_at
                dict_buffers.append(marking_dei_imp_stats_val_dict_buffer)
            for marking_srp_priority_stats_val in root.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marking-srp-priority-stats-val"):
                marking_srp_priority_stats_val_dict_buffer = {}
                marking_srp_priority_stats_val_dict_buffer["id"] = "urn:ngsi-ld:MarkingSrpPriorityStatsVal"
                marking_srp_priority_stats_val_dict_buffer["type"] = "MarkingSrpPriorityStatsVal"
                srpPriorityValue = marking_srp_priority_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}srp-priority-value")
                if srpPriorityValue is not None:
                    element_text = srpPriorityValue.text
                    if element_text is not None:
                        marking_srp_priority_stats_val_dict_buffer["srpPriorityValue"] = {}
                        marking_srp_priority_stats_val_dict_buffer["srpPriorityValue"]["type"] = "Property"
                        marking_srp_priority_stats_val_dict_buffer["srpPriorityValue"]["value"] = int(element_text)
                        marking_srp_priority_stats_val_dict_buffer["srpPriorityValue"]["observedAt"] = observed_at
                markedPkts = marking_srp_priority_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marked-pkts")
                if markedPkts is not None:
                    element_text = markedPkts.text
                    if element_text is not None:
                        marking_srp_priority_stats_val_dict_buffer["markedPkts"] = {}
                        marking_srp_priority_stats_val_dict_buffer["markedPkts"]["type"] = "Property"
                        marking_srp_priority_stats_val_dict_buffer["markedPkts"]["value"] = int(element_text)
                        marking_srp_priority_stats_val_dict_buffer["markedPkts"]["observedAt"] = observed_at
                dict_buffers.append(marking_srp_priority_stats_val_dict_buffer)
            for marking_wlan_user_priority_stats_val in root.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marking-wlan-user-priority-stats-val"):
                marking_wlan_user_priority_stats_val_dict_buffer = {}
                marking_wlan_user_priority_stats_val_dict_buffer["id"] = "urn:ngsi-ld:MarkingWlanUserPriorityStatsVal"
                marking_wlan_user_priority_stats_val_dict_buffer["type"] = "MarkingWlanUserPriorityStatsVal"
                wlanUserPriorityValue = marking_wlan_user_priority_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}wlan-user-priority-value")
                if wlanUserPriorityValue is not None:
                    element_text = wlanUserPriorityValue.text
                    if element_text is not None:
                        marking_wlan_user_priority_stats_val_dict_buffer["wlanUserPriorityValue"] = {}
                        marking_wlan_user_priority_stats_val_dict_buffer["wlanUserPriorityValue"]["type"] = "Property"
                        marking_wlan_user_priority_stats_val_dict_buffer["wlanUserPriorityValue"]["value"] = int(element_text)
                        marking_wlan_user_priority_stats_val_dict_buffer["wlanUserPriorityValue"]["observedAt"] = observed_at
                markedPkts = marking_wlan_user_priority_stats_val.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}marked-pkts")
                if markedPkts is not None:
                    element_text = markedPkts.text
                    if element_text is not None:
                        marking_wlan_user_priority_stats_val_dict_buffer["markedPkts"] = {}
                        marking_wlan_user_priority_stats_val_dict_buffer["markedPkts"]["type"] = "Property"
                        marking_wlan_user_priority_stats_val_dict_buffer["markedPkts"]["value"] = int(element_text)
                        marking_wlan_user_priority_stats_val_dict_buffer["markedPkts"]["observedAt"] = observed_at
                dict_buffers.append(marking_wlan_user_priority_stats_val_dict_buffer)
            hasChild = diffserv_target_classifier_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}has-child")
            if hasChild is not None:
                element_text = hasChild.text
                if element_text is not None:
                    interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["hasChild"] = {}
                    interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["hasChild"]["type"] = "Property"
                    interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["hasChild"]["value"] = eval(element_text.capitalize())
                    interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer["hasChild"]["observedAt"] = observed_at
            dict_buffers.append(interface_diffserv_info_diffserv_target_classifier_stats_dict_buffer)
        for priority_oper_list in diffserv_info.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}priority-oper-list"):
            interface_diffserv_info_priority_oper_list_dict_buffer = {}
            interface_diffserv_info_priority_oper_list_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoPriorityOperList:" + ":".join(interface_diffserv_info_dict_buffer["id"].split(":")[3:])
            interface_diffserv_info_priority_oper_list_dict_buffer["type"] = "InterfaceDiffservInfoPriorityOperList"
            interface_diffserv_info_priority_oper_list_dict_buffer["isPartOf"] = {}
            interface_diffserv_info_priority_oper_list_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_diffserv_info_priority_oper_list_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_dict_buffer["id"]
            interface_diffserv_info_priority_oper_list_dict_buffer["isPartOf"]["observedAt"] = observed_at
            priorityLevel = priority_oper_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}priority-level")
            if priorityLevel is not None:
                element_text = priorityLevel.text
                if element_text is not None:
                    interface_diffserv_info_priority_oper_list_dict_buffer["priorityLevel"] = {}
                    interface_diffserv_info_priority_oper_list_dict_buffer["priorityLevel"]["type"] = "Property"
                    interface_diffserv_info_priority_oper_list_dict_buffer["priorityLevel"]["value"] = int(element_text)
                    interface_diffserv_info_priority_oper_list_dict_buffer["priorityLevel"]["observedAt"] = observed_at
            for agg_priority_stats in priority_oper_list.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}agg-priority-stats"):
                interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer = {}
                interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoPriorityOperListAggPriorityStats:" + ":".join(interface_diffserv_info_priority_oper_list_dict_buffer["id"].split(":")[3:])
                interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["type"] = "InterfaceDiffservInfoPriorityOperListAggPriorityStats"
                interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["isPartOf"] = {}
                interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_priority_oper_list_dict_buffer["id"]
                interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["isPartOf"]["observedAt"] = observed_at
                outputPkts = agg_priority_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}output-pkts")
                if outputPkts is not None:
                    element_text = outputPkts.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["outputPkts"] = {}
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["outputPkts"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["outputPkts"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["outputPkts"]["observedAt"] = observed_at
                outputBytes = agg_priority_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}output-bytes")
                if outputBytes is not None:
                    element_text = outputBytes.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["outputBytes"] = {}
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["outputBytes"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["outputBytes"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["outputBytes"]["observedAt"] = observed_at
                queueSizePkts = agg_priority_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}queue-size-pkts")
                if queueSizePkts is not None:
                    element_text = queueSizePkts.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["queueSizePkts"] = {}
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["queueSizePkts"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["queueSizePkts"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["queueSizePkts"]["observedAt"] = observed_at
                queueSizeBytes = agg_priority_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}queue-size-bytes")
                if queueSizeBytes is not None:
                    element_text = queueSizeBytes.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["queueSizeBytes"] = {}
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["queueSizeBytes"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["queueSizeBytes"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["queueSizeBytes"]["observedAt"] = observed_at
                dropPkts = agg_priority_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}drop-pkts")
                if dropPkts is not None:
                    element_text = dropPkts.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["dropPkts"] = {}
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["dropPkts"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["dropPkts"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["dropPkts"]["observedAt"] = observed_at
                dropBytes = agg_priority_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}drop-bytes")
                if dropBytes is not None:
                    element_text = dropBytes.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["dropBytes"] = {}
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["dropBytes"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["dropBytes"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["dropBytes"]["observedAt"] = observed_at
                dropPktsFlow = agg_priority_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}drop-pkts-flow")
                if dropPktsFlow is not None:
                    element_text = dropPktsFlow.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["dropPktsFlow"] = {}
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["dropPktsFlow"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["dropPktsFlow"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["dropPktsFlow"]["observedAt"] = observed_at
                dropPktsNoBuffer = agg_priority_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}drop-pkts-no-buffer")
                if dropPktsNoBuffer is not None:
                    element_text = dropPktsNoBuffer.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["dropPktsNoBuffer"] = {}
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["dropPktsNoBuffer"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["dropPktsNoBuffer"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer["dropPktsNoBuffer"]["observedAt"] = observed_at
                dict_buffers.append(interface_diffserv_info_priority_oper_list_agg_priority_stats_dict_buffer)
            for qlimit_default_thresh in priority_oper_list.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}qlimit-default-thresh"):
                interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer = {}
                interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoPriorityOperListQlimitDefaultThresh:" + ":".join(interface_diffserv_info_priority_oper_list_dict_buffer["id"].split(":")[3:])
                interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["type"] = "InterfaceDiffservInfoPriorityOperListQlimitDefaultThresh"
                interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["isPartOf"] = {}
                interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_priority_oper_list_dict_buffer["id"]
                interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["isPartOf"]["observedAt"] = observed_at
                bytes = qlimit_default_thresh.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}bytes")
                if bytes is not None:
                    element_text = bytes.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["bytes"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["bytes"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["bytes"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["bytes"]["observedAt"] = observed_at
                threshSizeMetric = qlimit_default_thresh.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}thresh-size-metric")
                if threshSizeMetric is not None:
                    element_text = threshSizeMetric.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["threshSizeMetric"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["threshSizeMetric"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["threshSizeMetric"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["threshSizeMetric"]["observedAt"] = observed_at
                unitVal = qlimit_default_thresh.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}unit-val")
                if unitVal is not None:
                    element_text = unitVal.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["unitVal"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["unitVal"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["unitVal"]["value"] = element_text
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["unitVal"]["observedAt"] = observed_at
                thresholdInterval = qlimit_default_thresh.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}threshold-interval")
                if thresholdInterval is not None:
                    element_text = thresholdInterval.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["thresholdInterval"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["thresholdInterval"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["thresholdInterval"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["thresholdInterval"]["observedAt"] = observed_at
                threshIntervalMetric = qlimit_default_thresh.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}thresh-interval-metric")
                if threshIntervalMetric is not None:
                    element_text = threshIntervalMetric.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["threshIntervalMetric"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["threshIntervalMetric"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["threshIntervalMetric"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["threshIntervalMetric"]["observedAt"] = observed_at
                intervalUnitVal = qlimit_default_thresh.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}interval-unit-val")
                if intervalUnitVal is not None:
                    element_text = intervalUnitVal.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["intervalUnitVal"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["intervalUnitVal"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["intervalUnitVal"]["value"] = element_text
                        interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer["intervalUnitVal"]["observedAt"] = observed_at
                dict_buffers.append(interface_diffserv_info_priority_oper_list_qlimit_default_thresh_dict_buffer)
            for qlimit_cos_thresh_list in priority_oper_list.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}qlimit-cos-thresh-list"):
                interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer = {}
                interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoPriorityOperListQlimitCosThreshList:" + ":".join(interface_diffserv_info_priority_oper_list_dict_buffer["id"].split(":")[3:])
                interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["type"] = "InterfaceDiffservInfoPriorityOperListQlimitCosThreshList"
                interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["isPartOf"] = {}
                interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_priority_oper_list_dict_buffer["id"]
                interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["isPartOf"]["observedAt"] = observed_at
                cosMin = qlimit_cos_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}cos-min")
                if cosMin is not None:
                    element_text = cosMin.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["cosMin"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["cosMin"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["cosMin"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["cosMin"]["observedAt"] = observed_at
                cosMax = qlimit_cos_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}cos-max")
                if cosMax is not None:
                    element_text = cosMax.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["cosMax"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["cosMax"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["cosMax"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["cosMax"]["observedAt"] = observed_at
                bytes = qlimit_cos_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}bytes")
                if bytes is not None:
                    element_text = bytes.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["bytes"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["bytes"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["bytes"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["bytes"]["observedAt"] = observed_at
                threshSizeMetric = qlimit_cos_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}thresh-size-metric")
                if threshSizeMetric is not None:
                    element_text = threshSizeMetric.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["threshSizeMetric"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["threshSizeMetric"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["threshSizeMetric"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["threshSizeMetric"]["observedAt"] = observed_at
                unitVal = qlimit_cos_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}unit-val")
                if unitVal is not None:
                    element_text = unitVal.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["unitVal"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["unitVal"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["unitVal"]["value"] = element_text
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["unitVal"]["observedAt"] = observed_at
                thresholdInterval = qlimit_cos_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}threshold-interval")
                if thresholdInterval is not None:
                    element_text = thresholdInterval.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["thresholdInterval"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["thresholdInterval"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["thresholdInterval"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["thresholdInterval"]["observedAt"] = observed_at
                threshIntervalMetric = qlimit_cos_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}thresh-interval-metric")
                if threshIntervalMetric is not None:
                    element_text = threshIntervalMetric.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["threshIntervalMetric"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["threshIntervalMetric"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["threshIntervalMetric"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["threshIntervalMetric"]["observedAt"] = observed_at
                intervalUnitVal = qlimit_cos_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}interval-unit-val")
                if intervalUnitVal is not None:
                    element_text = intervalUnitVal.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["intervalUnitVal"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["intervalUnitVal"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["intervalUnitVal"]["value"] = element_text
                        interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer["intervalUnitVal"]["observedAt"] = observed_at
                dict_buffers.append(interface_diffserv_info_priority_oper_list_qlimit_cos_thresh_list_dict_buffer)
            for qlimit_disc_class_thresh_list in priority_oper_list.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}qlimit-disc-class-thresh-list"):
                interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer = {}
                interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoPriorityOperListQlimitDiscClassThreshList:" + ":".join(interface_diffserv_info_priority_oper_list_dict_buffer["id"].split(":")[3:])
                interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["type"] = "InterfaceDiffservInfoPriorityOperListQlimitDiscClassThreshList"
                interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["isPartOf"] = {}
                interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_priority_oper_list_dict_buffer["id"]
                interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["isPartOf"]["observedAt"] = observed_at
                discClassMin = qlimit_disc_class_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}disc-class-min")
                if discClassMin is not None:
                    element_text = discClassMin.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["discClassMin"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["discClassMin"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["discClassMin"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["discClassMin"]["observedAt"] = observed_at
                discClassMax = qlimit_disc_class_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}disc-class-max")
                if discClassMax is not None:
                    element_text = discClassMax.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["discClassMax"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["discClassMax"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["discClassMax"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["discClassMax"]["observedAt"] = observed_at
                bytes = qlimit_disc_class_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}bytes")
                if bytes is not None:
                    element_text = bytes.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["bytes"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["bytes"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["bytes"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["bytes"]["observedAt"] = observed_at
                threshSizeMetric = qlimit_disc_class_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}thresh-size-metric")
                if threshSizeMetric is not None:
                    element_text = threshSizeMetric.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["threshSizeMetric"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["threshSizeMetric"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["threshSizeMetric"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["threshSizeMetric"]["observedAt"] = observed_at
                unitVal = qlimit_disc_class_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}unit-val")
                if unitVal is not None:
                    element_text = unitVal.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["unitVal"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["unitVal"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["unitVal"]["value"] = element_text
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["unitVal"]["observedAt"] = observed_at
                thresholdInterval = qlimit_disc_class_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}threshold-interval")
                if thresholdInterval is not None:
                    element_text = thresholdInterval.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["thresholdInterval"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["thresholdInterval"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["thresholdInterval"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["thresholdInterval"]["observedAt"] = observed_at
                threshIntervalMetric = qlimit_disc_class_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}thresh-interval-metric")
                if threshIntervalMetric is not None:
                    element_text = threshIntervalMetric.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["threshIntervalMetric"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["threshIntervalMetric"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["threshIntervalMetric"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["threshIntervalMetric"]["observedAt"] = observed_at
                intervalUnitVal = qlimit_disc_class_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}interval-unit-val")
                if intervalUnitVal is not None:
                    element_text = intervalUnitVal.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["intervalUnitVal"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["intervalUnitVal"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["intervalUnitVal"]["value"] = element_text
                        interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer["intervalUnitVal"]["observedAt"] = observed_at
                dict_buffers.append(interface_diffserv_info_priority_oper_list_qlimit_disc_class_thresh_list_dict_buffer)
            for qlimit_qos_grp_thresh_list in priority_oper_list.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}qlimit-qos-grp-thresh-list"):
                interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer = {}
                interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoPriorityOperListQlimitQosGrpThreshList:" + ":".join(interface_diffserv_info_priority_oper_list_dict_buffer["id"].split(":")[3:])
                interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["type"] = "InterfaceDiffservInfoPriorityOperListQlimitQosGrpThreshList"
                interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["isPartOf"] = {}
                interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_priority_oper_list_dict_buffer["id"]
                interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["isPartOf"]["observedAt"] = observed_at
                qosGroupMin = qlimit_qos_grp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}qos-group-min")
                if qosGroupMin is not None:
                    element_text = qosGroupMin.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["qosGroupMin"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["qosGroupMin"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["qosGroupMin"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["qosGroupMin"]["observedAt"] = observed_at
                qosGroupMax = qlimit_qos_grp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}qos-group-max")
                if qosGroupMax is not None:
                    element_text = qosGroupMax.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["qosGroupMax"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["qosGroupMax"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["qosGroupMax"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["qosGroupMax"]["observedAt"] = observed_at
                bytes = qlimit_qos_grp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}bytes")
                if bytes is not None:
                    element_text = bytes.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["bytes"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["bytes"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["bytes"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["bytes"]["observedAt"] = observed_at
                threshSizeMetric = qlimit_qos_grp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}thresh-size-metric")
                if threshSizeMetric is not None:
                    element_text = threshSizeMetric.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["threshSizeMetric"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["threshSizeMetric"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["threshSizeMetric"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["threshSizeMetric"]["observedAt"] = observed_at
                unitVal = qlimit_qos_grp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}unit-val")
                if unitVal is not None:
                    element_text = unitVal.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["unitVal"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["unitVal"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["unitVal"]["value"] = element_text
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["unitVal"]["observedAt"] = observed_at
                thresholdInterval = qlimit_qos_grp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}threshold-interval")
                if thresholdInterval is not None:
                    element_text = thresholdInterval.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["thresholdInterval"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["thresholdInterval"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["thresholdInterval"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["thresholdInterval"]["observedAt"] = observed_at
                threshIntervalMetric = qlimit_qos_grp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}thresh-interval-metric")
                if threshIntervalMetric is not None:
                    element_text = threshIntervalMetric.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["threshIntervalMetric"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["threshIntervalMetric"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["threshIntervalMetric"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["threshIntervalMetric"]["observedAt"] = observed_at
                intervalUnitVal = qlimit_qos_grp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}interval-unit-val")
                if intervalUnitVal is not None:
                    element_text = intervalUnitVal.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["intervalUnitVal"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["intervalUnitVal"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["intervalUnitVal"]["value"] = element_text
                        interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer["intervalUnitVal"]["observedAt"] = observed_at
                dict_buffers.append(interface_diffserv_info_priority_oper_list_qlimit_qos_grp_thresh_list_dict_buffer)
            for qlimit_mpls_exp_thresh_list in priority_oper_list.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}qlimit-mpls-exp-thresh-list"):
                interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer = {}
                interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoPriorityOperListQlimitMplsExpThreshList:" + ":".join(interface_diffserv_info_priority_oper_list_dict_buffer["id"].split(":")[3:])
                interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["type"] = "InterfaceDiffservInfoPriorityOperListQlimitMplsExpThreshList"
                interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["isPartOf"] = {}
                interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_priority_oper_list_dict_buffer["id"]
                interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["isPartOf"]["observedAt"] = observed_at
                expMin = qlimit_mpls_exp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}exp-min")
                if expMin is not None:
                    element_text = expMin.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["expMin"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["expMin"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["expMin"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["expMin"]["observedAt"] = observed_at
                expMax = qlimit_mpls_exp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}exp-max")
                if expMax is not None:
                    element_text = expMax.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["expMax"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["expMax"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["expMax"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["expMax"]["observedAt"] = observed_at
                bytes = qlimit_mpls_exp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}bytes")
                if bytes is not None:
                    element_text = bytes.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["bytes"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["bytes"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["bytes"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["bytes"]["observedAt"] = observed_at
                threshSizeMetric = qlimit_mpls_exp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}thresh-size-metric")
                if threshSizeMetric is not None:
                    element_text = threshSizeMetric.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["threshSizeMetric"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["threshSizeMetric"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["threshSizeMetric"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["threshSizeMetric"]["observedAt"] = observed_at
                unitVal = qlimit_mpls_exp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}unit-val")
                if unitVal is not None:
                    element_text = unitVal.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["unitVal"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["unitVal"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["unitVal"]["value"] = element_text
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["unitVal"]["observedAt"] = observed_at
                thresholdInterval = qlimit_mpls_exp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}threshold-interval")
                if thresholdInterval is not None:
                    element_text = thresholdInterval.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["thresholdInterval"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["thresholdInterval"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["thresholdInterval"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["thresholdInterval"]["observedAt"] = observed_at
                threshIntervalMetric = qlimit_mpls_exp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}thresh-interval-metric")
                if threshIntervalMetric is not None:
                    element_text = threshIntervalMetric.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["threshIntervalMetric"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["threshIntervalMetric"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["threshIntervalMetric"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["threshIntervalMetric"]["observedAt"] = observed_at
                intervalUnitVal = qlimit_mpls_exp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}interval-unit-val")
                if intervalUnitVal is not None:
                    element_text = intervalUnitVal.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["intervalUnitVal"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["intervalUnitVal"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["intervalUnitVal"]["value"] = element_text
                        interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer["intervalUnitVal"]["observedAt"] = observed_at
                dict_buffers.append(interface_diffserv_info_priority_oper_list_qlimit_mpls_exp_thresh_list_dict_buffer)
            for qlimit_dscp_thresh_list in priority_oper_list.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}qlimit-dscp-thresh-list"):
                interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer = {}
                interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["id"] = "urn:ngsi-ld:InterfaceDiffservInfoPriorityOperListQlimitDscpThreshList:" + ":".join(interface_diffserv_info_priority_oper_list_dict_buffer["id"].split(":")[3:])
                interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["type"] = "InterfaceDiffservInfoPriorityOperListQlimitDscpThreshList"
                interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["isPartOf"] = {}
                interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["isPartOf"]["object"] = interface_diffserv_info_priority_oper_list_dict_buffer["id"]
                interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["isPartOf"]["observedAt"] = observed_at
                dscpMin = qlimit_dscp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dscp-min")
                if dscpMin is not None:
                    element_text = dscpMin.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["dscpMin"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["dscpMin"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["dscpMin"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["dscpMin"]["observedAt"] = observed_at
                dscpMax = qlimit_dscp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dscp-max")
                if dscpMax is not None:
                    element_text = dscpMax.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["dscpMax"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["dscpMax"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["dscpMax"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["dscpMax"]["observedAt"] = observed_at
                bytes = qlimit_dscp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}bytes")
                if bytes is not None:
                    element_text = bytes.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["bytes"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["bytes"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["bytes"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["bytes"]["observedAt"] = observed_at
                threshSizeMetric = qlimit_dscp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}thresh-size-metric")
                if threshSizeMetric is not None:
                    element_text = threshSizeMetric.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["threshSizeMetric"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["threshSizeMetric"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["threshSizeMetric"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["threshSizeMetric"]["observedAt"] = observed_at
                unitVal = qlimit_dscp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}unit-val")
                if unitVal is not None:
                    element_text = unitVal.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["unitVal"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["unitVal"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["unitVal"]["value"] = element_text
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["unitVal"]["observedAt"] = observed_at
                thresholdInterval = qlimit_dscp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}threshold-interval")
                if thresholdInterval is not None:
                    element_text = thresholdInterval.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["thresholdInterval"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["thresholdInterval"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["thresholdInterval"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["thresholdInterval"]["observedAt"] = observed_at
                threshIntervalMetric = qlimit_dscp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}thresh-interval-metric")
                if threshIntervalMetric is not None:
                    element_text = threshIntervalMetric.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["threshIntervalMetric"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["threshIntervalMetric"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["threshIntervalMetric"]["value"] = int(element_text)
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["threshIntervalMetric"]["observedAt"] = observed_at
                intervalUnitVal = qlimit_dscp_thresh_list.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}interval-unit-val")
                if intervalUnitVal is not None:
                    element_text = intervalUnitVal.text
                    if element_text is not None:
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["intervalUnitVal"] = {}
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["intervalUnitVal"]["type"] = "Property"
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["intervalUnitVal"]["value"] = element_text
                        interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer["intervalUnitVal"]["observedAt"] = observed_at
                dict_buffers.append(interface_diffserv_info_priority_oper_list_qlimit_dscp_thresh_list_dict_buffer)
            dict_buffers.append(interface_diffserv_info_priority_oper_list_dict_buffer)
        dict_buffers.append(interface_diffserv_info_dict_buffer)
    vrf = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}vrf")
    if vrf is not None:
        element_text = vrf.text
        if element_text is not None:
            interface_dict_buffer["vrf"] = {}
            interface_dict_buffer["vrf"]["type"] = "Property"
            interface_dict_buffer["vrf"]["value"] = element_text
            interface_dict_buffer["vrf"]["observedAt"] = observed_at
    ipv4 = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}ipv4")
    if ipv4 is not None:
        element_text = ipv4.text
        if element_text is not None:
            interface_dict_buffer["ipv4"] = {}
            interface_dict_buffer["ipv4"]["type"] = "Property"
            interface_dict_buffer["ipv4"]["value"] = element_text
            interface_dict_buffer["ipv4"]["observedAt"] = observed_at
    ipv4SubnetMask = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}ipv4-subnet-mask")
    if ipv4SubnetMask is not None:
        element_text = ipv4SubnetMask.text
        if element_text is not None:
            interface_dict_buffer["ipv4SubnetMask"] = {}
            interface_dict_buffer["ipv4SubnetMask"]["type"] = "Property"
            interface_dict_buffer["ipv4SubnetMask"]["value"] = element_text
            interface_dict_buffer["ipv4SubnetMask"]["observedAt"] = observed_at
    description = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}description")
    if description is not None:
        element_text = description.text
        if element_text is not None:
            interface_dict_buffer["description"] = {}
            interface_dict_buffer["description"]["type"] = "Property"
            interface_dict_buffer["description"]["value"] = element_text
            interface_dict_buffer["description"]["observedAt"] = observed_at
    mtu = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}mtu")
    if mtu is not None:
        element_text = mtu.text
        if element_text is not None:
            interface_dict_buffer["mtu"] = {}
            interface_dict_buffer["mtu"]["type"] = "Property"
            interface_dict_buffer["mtu"]["value"] = int(element_text)
            interface_dict_buffer["mtu"]["observedAt"] = observed_at
    inputSecurityAcl = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}input-security-acl")
    if inputSecurityAcl is not None:
        element_text = inputSecurityAcl.text
        if element_text is not None:
            interface_dict_buffer["inputSecurityAcl"] = {}
            interface_dict_buffer["inputSecurityAcl"]["type"] = "Property"
            interface_dict_buffer["inputSecurityAcl"]["value"] = element_text
            interface_dict_buffer["inputSecurityAcl"]["observedAt"] = observed_at
    outputSecurityAcl = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}output-security-acl")
    if outputSecurityAcl is not None:
        element_text = outputSecurityAcl.text
        if element_text is not None:
            interface_dict_buffer["outputSecurityAcl"] = {}
            interface_dict_buffer["outputSecurityAcl"]["type"] = "Property"
            interface_dict_buffer["outputSecurityAcl"]["value"] = element_text
            interface_dict_buffer["outputSecurityAcl"]["observedAt"] = observed_at
    for v4_protocol_stats in interface.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}v4-protocol-stats"):
        interface_v4_protocol_stats_dict_buffer = {}
        interface_v4_protocol_stats_dict_buffer["id"] = "urn:ngsi-ld:InterfaceV4ProtocolStats:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
        interface_v4_protocol_stats_dict_buffer["type"] = "InterfaceV4ProtocolStats"
        interface_v4_protocol_stats_dict_buffer["isPartOf"] = {}
        interface_v4_protocol_stats_dict_buffer["isPartOf"]["type"] = "Relationship"
        interface_v4_protocol_stats_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
        interface_v4_protocol_stats_dict_buffer["isPartOf"]["observedAt"] = observed_at
        inPkts = v4_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-pkts")
        if inPkts is not None:
            element_text = inPkts.text
            if element_text is not None:
                interface_v4_protocol_stats_dict_buffer["inPkts"] = {}
                interface_v4_protocol_stats_dict_buffer["inPkts"]["type"] = "Property"
                interface_v4_protocol_stats_dict_buffer["inPkts"]["value"] = int(element_text)
                interface_v4_protocol_stats_dict_buffer["inPkts"]["observedAt"] = observed_at
        inOctets = v4_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-octets")
        if inOctets is not None:
            element_text = inOctets.text
            if element_text is not None:
                interface_v4_protocol_stats_dict_buffer["inOctets"] = {}
                interface_v4_protocol_stats_dict_buffer["inOctets"]["type"] = "Property"
                interface_v4_protocol_stats_dict_buffer["inOctets"]["value"] = int(element_text)
                interface_v4_protocol_stats_dict_buffer["inOctets"]["observedAt"] = observed_at
        inErrorPkts = v4_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-error-pkts")
        if inErrorPkts is not None:
            element_text = inErrorPkts.text
            if element_text is not None:
                interface_v4_protocol_stats_dict_buffer["inErrorPkts"] = {}
                interface_v4_protocol_stats_dict_buffer["inErrorPkts"]["type"] = "Property"
                interface_v4_protocol_stats_dict_buffer["inErrorPkts"]["value"] = int(element_text)
                interface_v4_protocol_stats_dict_buffer["inErrorPkts"]["observedAt"] = observed_at
        inForwardedPkts = v4_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-forwarded-pkts")
        if inForwardedPkts is not None:
            element_text = inForwardedPkts.text
            if element_text is not None:
                interface_v4_protocol_stats_dict_buffer["inForwardedPkts"] = {}
                interface_v4_protocol_stats_dict_buffer["inForwardedPkts"]["type"] = "Property"
                interface_v4_protocol_stats_dict_buffer["inForwardedPkts"]["value"] = int(element_text)
                interface_v4_protocol_stats_dict_buffer["inForwardedPkts"]["observedAt"] = observed_at
        inForwardedOctets = v4_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-forwarded-octets")
        if inForwardedOctets is not None:
            element_text = inForwardedOctets.text
            if element_text is not None:
                interface_v4_protocol_stats_dict_buffer["inForwardedOctets"] = {}
                interface_v4_protocol_stats_dict_buffer["inForwardedOctets"]["type"] = "Property"
                interface_v4_protocol_stats_dict_buffer["inForwardedOctets"]["value"] = int(element_text)
                interface_v4_protocol_stats_dict_buffer["inForwardedOctets"]["observedAt"] = observed_at
        inDiscardedPkts = v4_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-discarded-pkts")
        if inDiscardedPkts is not None:
            element_text = inDiscardedPkts.text
            if element_text is not None:
                interface_v4_protocol_stats_dict_buffer["inDiscardedPkts"] = {}
                interface_v4_protocol_stats_dict_buffer["inDiscardedPkts"]["type"] = "Property"
                interface_v4_protocol_stats_dict_buffer["inDiscardedPkts"]["value"] = int(element_text)
                interface_v4_protocol_stats_dict_buffer["inDiscardedPkts"]["observedAt"] = observed_at
        outPkts = v4_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}out-pkts")
        if outPkts is not None:
            element_text = outPkts.text
            if element_text is not None:
                interface_v4_protocol_stats_dict_buffer["outPkts"] = {}
                interface_v4_protocol_stats_dict_buffer["outPkts"]["type"] = "Property"
                interface_v4_protocol_stats_dict_buffer["outPkts"]["value"] = int(element_text)
                interface_v4_protocol_stats_dict_buffer["outPkts"]["observedAt"] = observed_at
        outOctets = v4_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}out-octets")
        if outOctets is not None:
            element_text = outOctets.text
            if element_text is not None:
                interface_v4_protocol_stats_dict_buffer["outOctets"] = {}
                interface_v4_protocol_stats_dict_buffer["outOctets"]["type"] = "Property"
                interface_v4_protocol_stats_dict_buffer["outOctets"]["value"] = int(element_text)
                interface_v4_protocol_stats_dict_buffer["outOctets"]["observedAt"] = observed_at
        outErrorPkts = v4_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}out-error-pkts")
        if outErrorPkts is not None:
            element_text = outErrorPkts.text
            if element_text is not None:
                interface_v4_protocol_stats_dict_buffer["outErrorPkts"] = {}
                interface_v4_protocol_stats_dict_buffer["outErrorPkts"]["type"] = "Property"
                interface_v4_protocol_stats_dict_buffer["outErrorPkts"]["value"] = int(element_text)
                interface_v4_protocol_stats_dict_buffer["outErrorPkts"]["observedAt"] = observed_at
        outForwardedPkts = v4_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}out-forwarded-pkts")
        if outForwardedPkts is not None:
            element_text = outForwardedPkts.text
            if element_text is not None:
                interface_v4_protocol_stats_dict_buffer["outForwardedPkts"] = {}
                interface_v4_protocol_stats_dict_buffer["outForwardedPkts"]["type"] = "Property"
                interface_v4_protocol_stats_dict_buffer["outForwardedPkts"]["value"] = int(element_text)
                interface_v4_protocol_stats_dict_buffer["outForwardedPkts"]["observedAt"] = observed_at
        outForwardedOctets = v4_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}out-forwarded-octets")
        if outForwardedOctets is not None:
            element_text = outForwardedOctets.text
            if element_text is not None:
                interface_v4_protocol_stats_dict_buffer["outForwardedOctets"] = {}
                interface_v4_protocol_stats_dict_buffer["outForwardedOctets"]["type"] = "Property"
                interface_v4_protocol_stats_dict_buffer["outForwardedOctets"]["value"] = int(element_text)
                interface_v4_protocol_stats_dict_buffer["outForwardedOctets"]["observedAt"] = observed_at
        outDiscardedPkts = v4_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}out-discarded-pkts")
        if outDiscardedPkts is not None:
            element_text = outDiscardedPkts.text
            if element_text is not None:
                interface_v4_protocol_stats_dict_buffer["outDiscardedPkts"] = {}
                interface_v4_protocol_stats_dict_buffer["outDiscardedPkts"]["type"] = "Property"
                interface_v4_protocol_stats_dict_buffer["outDiscardedPkts"]["value"] = int(element_text)
                interface_v4_protocol_stats_dict_buffer["outDiscardedPkts"]["observedAt"] = observed_at
        dict_buffers.append(interface_v4_protocol_stats_dict_buffer)
    for v6_protocol_stats in interface.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}v6-protocol-stats"):
        interface_v6_protocol_stats_dict_buffer = {}
        interface_v6_protocol_stats_dict_buffer["id"] = "urn:ngsi-ld:InterfaceV6ProtocolStats:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
        interface_v6_protocol_stats_dict_buffer["type"] = "InterfaceV6ProtocolStats"
        interface_v6_protocol_stats_dict_buffer["isPartOf"] = {}
        interface_v6_protocol_stats_dict_buffer["isPartOf"]["type"] = "Relationship"
        interface_v6_protocol_stats_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
        interface_v6_protocol_stats_dict_buffer["isPartOf"]["observedAt"] = observed_at
        inPkts = v6_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-pkts")
        if inPkts is not None:
            element_text = inPkts.text
            if element_text is not None:
                interface_v6_protocol_stats_dict_buffer["inPkts"] = {}
                interface_v6_protocol_stats_dict_buffer["inPkts"]["type"] = "Property"
                interface_v6_protocol_stats_dict_buffer["inPkts"]["value"] = int(element_text)
                interface_v6_protocol_stats_dict_buffer["inPkts"]["observedAt"] = observed_at
        inOctets = v6_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-octets")
        if inOctets is not None:
            element_text = inOctets.text
            if element_text is not None:
                interface_v6_protocol_stats_dict_buffer["inOctets"] = {}
                interface_v6_protocol_stats_dict_buffer["inOctets"]["type"] = "Property"
                interface_v6_protocol_stats_dict_buffer["inOctets"]["value"] = int(element_text)
                interface_v6_protocol_stats_dict_buffer["inOctets"]["observedAt"] = observed_at
        inErrorPkts = v6_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-error-pkts")
        if inErrorPkts is not None:
            element_text = inErrorPkts.text
            if element_text is not None:
                interface_v6_protocol_stats_dict_buffer["inErrorPkts"] = {}
                interface_v6_protocol_stats_dict_buffer["inErrorPkts"]["type"] = "Property"
                interface_v6_protocol_stats_dict_buffer["inErrorPkts"]["value"] = int(element_text)
                interface_v6_protocol_stats_dict_buffer["inErrorPkts"]["observedAt"] = observed_at
        inForwardedPkts = v6_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-forwarded-pkts")
        if inForwardedPkts is not None:
            element_text = inForwardedPkts.text
            if element_text is not None:
                interface_v6_protocol_stats_dict_buffer["inForwardedPkts"] = {}
                interface_v6_protocol_stats_dict_buffer["inForwardedPkts"]["type"] = "Property"
                interface_v6_protocol_stats_dict_buffer["inForwardedPkts"]["value"] = int(element_text)
                interface_v6_protocol_stats_dict_buffer["inForwardedPkts"]["observedAt"] = observed_at
        inForwardedOctets = v6_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-forwarded-octets")
        if inForwardedOctets is not None:
            element_text = inForwardedOctets.text
            if element_text is not None:
                interface_v6_protocol_stats_dict_buffer["inForwardedOctets"] = {}
                interface_v6_protocol_stats_dict_buffer["inForwardedOctets"]["type"] = "Property"
                interface_v6_protocol_stats_dict_buffer["inForwardedOctets"]["value"] = int(element_text)
                interface_v6_protocol_stats_dict_buffer["inForwardedOctets"]["observedAt"] = observed_at
        inDiscardedPkts = v6_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-discarded-pkts")
        if inDiscardedPkts is not None:
            element_text = inDiscardedPkts.text
            if element_text is not None:
                interface_v6_protocol_stats_dict_buffer["inDiscardedPkts"] = {}
                interface_v6_protocol_stats_dict_buffer["inDiscardedPkts"]["type"] = "Property"
                interface_v6_protocol_stats_dict_buffer["inDiscardedPkts"]["value"] = int(element_text)
                interface_v6_protocol_stats_dict_buffer["inDiscardedPkts"]["observedAt"] = observed_at
        outPkts = v6_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}out-pkts")
        if outPkts is not None:
            element_text = outPkts.text
            if element_text is not None:
                interface_v6_protocol_stats_dict_buffer["outPkts"] = {}
                interface_v6_protocol_stats_dict_buffer["outPkts"]["type"] = "Property"
                interface_v6_protocol_stats_dict_buffer["outPkts"]["value"] = int(element_text)
                interface_v6_protocol_stats_dict_buffer["outPkts"]["observedAt"] = observed_at
        outOctets = v6_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}out-octets")
        if outOctets is not None:
            element_text = outOctets.text
            if element_text is not None:
                interface_v6_protocol_stats_dict_buffer["outOctets"] = {}
                interface_v6_protocol_stats_dict_buffer["outOctets"]["type"] = "Property"
                interface_v6_protocol_stats_dict_buffer["outOctets"]["value"] = int(element_text)
                interface_v6_protocol_stats_dict_buffer["outOctets"]["observedAt"] = observed_at
        outErrorPkts = v6_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}out-error-pkts")
        if outErrorPkts is not None:
            element_text = outErrorPkts.text
            if element_text is not None:
                interface_v6_protocol_stats_dict_buffer["outErrorPkts"] = {}
                interface_v6_protocol_stats_dict_buffer["outErrorPkts"]["type"] = "Property"
                interface_v6_protocol_stats_dict_buffer["outErrorPkts"]["value"] = int(element_text)
                interface_v6_protocol_stats_dict_buffer["outErrorPkts"]["observedAt"] = observed_at
        outForwardedPkts = v6_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}out-forwarded-pkts")
        if outForwardedPkts is not None:
            element_text = outForwardedPkts.text
            if element_text is not None:
                interface_v6_protocol_stats_dict_buffer["outForwardedPkts"] = {}
                interface_v6_protocol_stats_dict_buffer["outForwardedPkts"]["type"] = "Property"
                interface_v6_protocol_stats_dict_buffer["outForwardedPkts"]["value"] = int(element_text)
                interface_v6_protocol_stats_dict_buffer["outForwardedPkts"]["observedAt"] = observed_at
        outForwardedOctets = v6_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}out-forwarded-octets")
        if outForwardedOctets is not None:
            element_text = outForwardedOctets.text
            if element_text is not None:
                interface_v6_protocol_stats_dict_buffer["outForwardedOctets"] = {}
                interface_v6_protocol_stats_dict_buffer["outForwardedOctets"]["type"] = "Property"
                interface_v6_protocol_stats_dict_buffer["outForwardedOctets"]["value"] = int(element_text)
                interface_v6_protocol_stats_dict_buffer["outForwardedOctets"]["observedAt"] = observed_at
        outDiscardedPkts = v6_protocol_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}out-discarded-pkts")
        if outDiscardedPkts is not None:
            element_text = outDiscardedPkts.text
            if element_text is not None:
                interface_v6_protocol_stats_dict_buffer["outDiscardedPkts"] = {}
                interface_v6_protocol_stats_dict_buffer["outDiscardedPkts"]["type"] = "Property"
                interface_v6_protocol_stats_dict_buffer["outDiscardedPkts"]["value"] = int(element_text)
                interface_v6_protocol_stats_dict_buffer["outDiscardedPkts"]["observedAt"] = observed_at
        dict_buffers.append(interface_v6_protocol_stats_dict_buffer)
    biaAddress = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}bia-address")
    if biaAddress is not None:
        element_text = biaAddress.text
        if element_text is not None:
            interface_dict_buffer["biaAddress"] = {}
            interface_dict_buffer["biaAddress"]["type"] = "Property"
            interface_dict_buffer["biaAddress"]["value"] = element_text
            interface_dict_buffer["biaAddress"]["observedAt"] = observed_at
    ipv6Addrs = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}ipv6-addrs")
    if ipv6Addrs is not None:
        element_text = ipv6Addrs.text
        if element_text is not None:
            interface_dict_buffer["ipv6Addrs"] = {}
            interface_dict_buffer["ipv6Addrs"]["type"] = "Property"
            interface_dict_buffer["ipv6Addrs"]["value"] = element_text
            interface_dict_buffer["ipv6Addrs"]["observedAt"] = observed_at
    for lag_aggregate_state in interface.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}lag-aggregate-state"):
        interface_lag_aggregate_state_dict_buffer = {}
        interface_lag_aggregate_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceLagAggregateState:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
        interface_lag_aggregate_state_dict_buffer["type"] = "InterfaceLagAggregateState"
        interface_lag_aggregate_state_dict_buffer["isPartOf"] = {}
        interface_lag_aggregate_state_dict_buffer["isPartOf"]["type"] = "Relationship"
        interface_lag_aggregate_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
        interface_lag_aggregate_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
        aggregateId = lag_aggregate_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}aggregate-id")
        if aggregateId is not None:
            element_text = aggregateId.text
            if element_text is not None:
                interface_lag_aggregate_state_dict_buffer["id"] = interface_lag_aggregate_state_dict_buffer["id"] + ":" + element_text
                interface_lag_aggregate_state_dict_buffer["aggregateId"] = {}
                interface_lag_aggregate_state_dict_buffer["aggregateId"]["type"] = "Property"
                interface_lag_aggregate_state_dict_buffer["aggregateId"]["value"] = element_text
                interface_lag_aggregate_state_dict_buffer["aggregateId"]["observedAt"] = observed_at
        lagType = lag_aggregate_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}lag-type")
        if lagType is not None:
            element_text = lagType.text
            if element_text is not None:
                interface_lag_aggregate_state_dict_buffer["lagType"] = {}
                interface_lag_aggregate_state_dict_buffer["lagType"]["type"] = "Property"
                interface_lag_aggregate_state_dict_buffer["lagType"]["value"] = element_text
                interface_lag_aggregate_state_dict_buffer["lagType"]["observedAt"] = observed_at
        minLinks = lag_aggregate_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}min-links")
        if minLinks is not None:
            element_text = minLinks.text
            if element_text is not None:
                interface_lag_aggregate_state_dict_buffer["minLinks"] = {}
                interface_lag_aggregate_state_dict_buffer["minLinks"]["type"] = "Property"
                interface_lag_aggregate_state_dict_buffer["minLinks"]["value"] = int(element_text)
                interface_lag_aggregate_state_dict_buffer["minLinks"]["observedAt"] = observed_at
        lagSpeed = lag_aggregate_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}lag-speed")
        if lagSpeed is not None:
            element_text = lagSpeed.text
            if element_text is not None:
                interface_lag_aggregate_state_dict_buffer["lagSpeed"] = {}
                interface_lag_aggregate_state_dict_buffer["lagSpeed"]["type"] = "Property"
                interface_lag_aggregate_state_dict_buffer["lagSpeed"]["value"] = int(element_text)
                interface_lag_aggregate_state_dict_buffer["lagSpeed"]["observedAt"] = observed_at
        members = lag_aggregate_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}members")
        if members is not None:
            element_text = members.text
            if element_text is not None:
                interface_lag_aggregate_state_dict_buffer["members"] = {}
                interface_lag_aggregate_state_dict_buffer["members"]["type"] = "Property"
                interface_lag_aggregate_state_dict_buffer["members"]["value"] = element_text
                interface_lag_aggregate_state_dict_buffer["members"]["observedAt"] = observed_at
        dict_buffers.append(interface_lag_aggregate_state_dict_buffer)
    ipv4TcpAdjustMss = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}ipv4-tcp-adjust-mss")
    if ipv4TcpAdjustMss is not None:
        element_text = ipv4TcpAdjustMss.text
        if element_text is not None:
            interface_dict_buffer["ipv4TcpAdjustMss"] = {}
            interface_dict_buffer["ipv4TcpAdjustMss"]["type"] = "Property"
            interface_dict_buffer["ipv4TcpAdjustMss"]["value"] = int(element_text)
            interface_dict_buffer["ipv4TcpAdjustMss"]["observedAt"] = observed_at
    ipv6TcpAdjustMss = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}ipv6-tcp-adjust-mss")
    if ipv6TcpAdjustMss is not None:
        element_text = ipv6TcpAdjustMss.text
        if element_text is not None:
            interface_dict_buffer["ipv6TcpAdjustMss"] = {}
            interface_dict_buffer["ipv6TcpAdjustMss"]["type"] = "Property"
            interface_dict_buffer["ipv6TcpAdjustMss"]["value"] = int(element_text)
            interface_dict_buffer["ipv6TcpAdjustMss"]["observedAt"] = observed_at
    intfExtStateSupport = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}intf-ext-state-support")
    if intfExtStateSupport is not None:
        element_text = intfExtStateSupport.text
        if element_text is not None:
            interface_dict_buffer["intfExtStateSupport"] = {}
            interface_dict_buffer["intfExtStateSupport"]["type"] = "Property"
            interface_dict_buffer["intfExtStateSupport"]["value"] = element_text
            interface_dict_buffer["intfExtStateSupport"]["observedAt"] = observed_at
    for intf_ext_state in interface.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}intf-ext-state"):
        interface_intf_ext_state_dict_buffer = {}
        interface_intf_ext_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceIntfExtState:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
        interface_intf_ext_state_dict_buffer["type"] = "InterfaceIntfExtState"
        interface_intf_ext_state_dict_buffer["isPartOf"] = {}
        interface_intf_ext_state_dict_buffer["isPartOf"]["type"] = "Relationship"
        interface_intf_ext_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
        interface_intf_ext_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
        errorType = intf_ext_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}error-type")
        if errorType is not None:
            element_text = errorType.text
            if element_text is not None:
                interface_intf_ext_state_dict_buffer["errorType"] = {}
                interface_intf_ext_state_dict_buffer["errorType"]["type"] = "Property"
                interface_intf_ext_state_dict_buffer["errorType"]["value"] = element_text
                interface_intf_ext_state_dict_buffer["errorType"]["observedAt"] = observed_at
        portErrorReason = intf_ext_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}port-error-reason")
        if portErrorReason is not None:
            element_text = portErrorReason.text
            if element_text is not None:
                interface_intf_ext_state_dict_buffer["portErrorReason"] = {}
                interface_intf_ext_state_dict_buffer["portErrorReason"]["type"] = "Property"
                interface_intf_ext_state_dict_buffer["portErrorReason"]["value"] = element_text
                interface_intf_ext_state_dict_buffer["portErrorReason"]["observedAt"] = observed_at
        autoMdixEnabled = intf_ext_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}auto-mdix-enabled")
        if autoMdixEnabled is not None:
            element_text = autoMdixEnabled.text
            if element_text is not None:
                interface_intf_ext_state_dict_buffer["autoMdixEnabled"] = {}
                interface_intf_ext_state_dict_buffer["autoMdixEnabled"]["type"] = "Property"
                interface_intf_ext_state_dict_buffer["autoMdixEnabled"]["value"] = eval(element_text.capitalize())
                interface_intf_ext_state_dict_buffer["autoMdixEnabled"]["observedAt"] = observed_at
        mdixOperStatusEnabled = intf_ext_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}mdix-oper-status-enabled")
        if mdixOperStatusEnabled is not None:
            element_text = mdixOperStatusEnabled.text
            if element_text is not None:
                interface_intf_ext_state_dict_buffer["mdixOperStatusEnabled"] = {}
                interface_intf_ext_state_dict_buffer["mdixOperStatusEnabled"]["type"] = "Property"
                interface_intf_ext_state_dict_buffer["mdixOperStatusEnabled"]["value"] = eval(element_text.capitalize())
                interface_intf_ext_state_dict_buffer["mdixOperStatusEnabled"]["observedAt"] = observed_at
        fecEnabled = intf_ext_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}fec-enabled")
        if fecEnabled is not None:
            element_text = fecEnabled.text
            if element_text is not None:
                interface_intf_ext_state_dict_buffer["fecEnabled"] = {}
                interface_intf_ext_state_dict_buffer["fecEnabled"]["type"] = "Property"
                interface_intf_ext_state_dict_buffer["fecEnabled"]["value"] = eval(element_text.capitalize())
                interface_intf_ext_state_dict_buffer["fecEnabled"]["observedAt"] = observed_at
        mgigDownshiftEnabled = intf_ext_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}mgig-downshift-enabled")
        if mgigDownshiftEnabled is not None:
            element_text = mgigDownshiftEnabled.text
            if element_text is not None:
                interface_intf_ext_state_dict_buffer["mgigDownshiftEnabled"] = {}
                interface_intf_ext_state_dict_buffer["mgigDownshiftEnabled"]["type"] = "Property"
                interface_intf_ext_state_dict_buffer["mgigDownshiftEnabled"]["value"] = eval(element_text.capitalize())
                interface_intf_ext_state_dict_buffer["mgigDownshiftEnabled"]["observedAt"] = observed_at
        dict_buffers.append(interface_intf_ext_state_dict_buffer)
    for storm_control in interface.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}storm-control"):
        interface_storm_control_dict_buffer = {}
        interface_storm_control_dict_buffer["id"] = "urn:ngsi-ld:InterfaceStormControl:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
        interface_storm_control_dict_buffer["type"] = "InterfaceStormControl"
        interface_storm_control_dict_buffer["isPartOf"] = {}
        interface_storm_control_dict_buffer["isPartOf"]["type"] = "Relationship"
        interface_storm_control_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
        interface_storm_control_dict_buffer["isPartOf"]["observedAt"] = observed_at
        for broadcast in storm_control.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}broadcast"):
            interface_storm_control_broadcast_dict_buffer = {}
            interface_storm_control_broadcast_dict_buffer["id"] = "urn:ngsi-ld:InterfaceStormControlBroadcast:" + ":".join(interface_storm_control_dict_buffer["id"].split(":")[3:])
            interface_storm_control_broadcast_dict_buffer["type"] = "InterfaceStormControlBroadcast"
            interface_storm_control_broadcast_dict_buffer["isPartOf"] = {}
            interface_storm_control_broadcast_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_storm_control_broadcast_dict_buffer["isPartOf"]["object"] = interface_storm_control_dict_buffer["id"]
            interface_storm_control_broadcast_dict_buffer["isPartOf"]["observedAt"] = observed_at
            filterState = broadcast.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}filter-state")
            if filterState is not None:
                element_text = filterState.text
                if element_text is not None:
                    interface_storm_control_broadcast_dict_buffer["filterState"] = {}
                    interface_storm_control_broadcast_dict_buffer["filterState"]["type"] = "Property"
                    interface_storm_control_broadcast_dict_buffer["filterState"]["value"] = element_text
                    interface_storm_control_broadcast_dict_buffer["filterState"]["observedAt"] = observed_at
            for current_rate in broadcast.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}current-rate"):
                interface_storm_control_broadcast_current_rate_dict_buffer = {}
                interface_storm_control_broadcast_current_rate_dict_buffer["id"] = "urn:ngsi-ld:InterfaceStormControlBroadcastCurrentRate:" + ":".join(interface_storm_control_broadcast_dict_buffer["id"].split(":")[3:])
                interface_storm_control_broadcast_current_rate_dict_buffer["type"] = "InterfaceStormControlBroadcastCurrentRate"
                interface_storm_control_broadcast_current_rate_dict_buffer["isPartOf"] = {}
                interface_storm_control_broadcast_current_rate_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_storm_control_broadcast_current_rate_dict_buffer["isPartOf"]["object"] = interface_storm_control_broadcast_dict_buffer["id"]
                interface_storm_control_broadcast_current_rate_dict_buffer["isPartOf"]["observedAt"] = observed_at
                bandwidth = current_rate.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}bandwidth")
                if bandwidth is not None:
                    element_text = bandwidth.text
                    if element_text is not None:
                        interface_storm_control_broadcast_current_rate_dict_buffer["bandwidth"] = {}
                        interface_storm_control_broadcast_current_rate_dict_buffer["bandwidth"]["type"] = "Property"
                        interface_storm_control_broadcast_current_rate_dict_buffer["bandwidth"]["value"] = float(element_text)
                        interface_storm_control_broadcast_current_rate_dict_buffer["bandwidth"]["observedAt"] = observed_at
                bps = current_rate.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}bps")
                if bps is not None:
                    element_text = bps.text
                    if element_text is not None:
                        interface_storm_control_broadcast_current_rate_dict_buffer["bps"] = {}
                        interface_storm_control_broadcast_current_rate_dict_buffer["bps"]["type"] = "Property"
                        interface_storm_control_broadcast_current_rate_dict_buffer["bps"]["value"] = int(element_text)
                        interface_storm_control_broadcast_current_rate_dict_buffer["bps"]["observedAt"] = observed_at
                pps = current_rate.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}pps")
                if pps is not None:
                    element_text = pps.text
                    if element_text is not None:
                        interface_storm_control_broadcast_current_rate_dict_buffer["pps"] = {}
                        interface_storm_control_broadcast_current_rate_dict_buffer["pps"]["type"] = "Property"
                        interface_storm_control_broadcast_current_rate_dict_buffer["pps"]["value"] = int(element_text)
                        interface_storm_control_broadcast_current_rate_dict_buffer["pps"]["observedAt"] = observed_at
                dict_buffers.append(interface_storm_control_broadcast_current_rate_dict_buffer)
            dict_buffers.append(interface_storm_control_broadcast_dict_buffer)
        for multicast in storm_control.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}multicast"):
            interface_storm_control_multicast_dict_buffer = {}
            interface_storm_control_multicast_dict_buffer["id"] = "urn:ngsi-ld:InterfaceStormControlMulticast:" + ":".join(interface_storm_control_dict_buffer["id"].split(":")[3:])
            interface_storm_control_multicast_dict_buffer["type"] = "InterfaceStormControlMulticast"
            interface_storm_control_multicast_dict_buffer["isPartOf"] = {}
            interface_storm_control_multicast_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_storm_control_multicast_dict_buffer["isPartOf"]["object"] = interface_storm_control_dict_buffer["id"]
            interface_storm_control_multicast_dict_buffer["isPartOf"]["observedAt"] = observed_at
            filterState = multicast.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}filter-state")
            if filterState is not None:
                element_text = filterState.text
                if element_text is not None:
                    interface_storm_control_multicast_dict_buffer["filterState"] = {}
                    interface_storm_control_multicast_dict_buffer["filterState"]["type"] = "Property"
                    interface_storm_control_multicast_dict_buffer["filterState"]["value"] = element_text
                    interface_storm_control_multicast_dict_buffer["filterState"]["observedAt"] = observed_at
            for current_rate in multicast.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}current-rate"):
                interface_storm_control_multicast_current_rate_dict_buffer = {}
                interface_storm_control_multicast_current_rate_dict_buffer["id"] = "urn:ngsi-ld:InterfaceStormControlMulticastCurrentRate:" + ":".join(interface_storm_control_multicast_dict_buffer["id"].split(":")[3:])
                interface_storm_control_multicast_current_rate_dict_buffer["type"] = "InterfaceStormControlMulticastCurrentRate"
                interface_storm_control_multicast_current_rate_dict_buffer["isPartOf"] = {}
                interface_storm_control_multicast_current_rate_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_storm_control_multicast_current_rate_dict_buffer["isPartOf"]["object"] = interface_storm_control_multicast_dict_buffer["id"]
                interface_storm_control_multicast_current_rate_dict_buffer["isPartOf"]["observedAt"] = observed_at
                bandwidth = current_rate.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}bandwidth")
                if bandwidth is not None:
                    element_text = bandwidth.text
                    if element_text is not None:
                        interface_storm_control_multicast_current_rate_dict_buffer["bandwidth"] = {}
                        interface_storm_control_multicast_current_rate_dict_buffer["bandwidth"]["type"] = "Property"
                        interface_storm_control_multicast_current_rate_dict_buffer["bandwidth"]["value"] = float(element_text)
                        interface_storm_control_multicast_current_rate_dict_buffer["bandwidth"]["observedAt"] = observed_at
                bps = current_rate.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}bps")
                if bps is not None:
                    element_text = bps.text
                    if element_text is not None:
                        interface_storm_control_multicast_current_rate_dict_buffer["bps"] = {}
                        interface_storm_control_multicast_current_rate_dict_buffer["bps"]["type"] = "Property"
                        interface_storm_control_multicast_current_rate_dict_buffer["bps"]["value"] = int(element_text)
                        interface_storm_control_multicast_current_rate_dict_buffer["bps"]["observedAt"] = observed_at
                pps = current_rate.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}pps")
                if pps is not None:
                    element_text = pps.text
                    if element_text is not None:
                        interface_storm_control_multicast_current_rate_dict_buffer["pps"] = {}
                        interface_storm_control_multicast_current_rate_dict_buffer["pps"]["type"] = "Property"
                        interface_storm_control_multicast_current_rate_dict_buffer["pps"]["value"] = int(element_text)
                        interface_storm_control_multicast_current_rate_dict_buffer["pps"]["observedAt"] = observed_at
                dict_buffers.append(interface_storm_control_multicast_current_rate_dict_buffer)
            dict_buffers.append(interface_storm_control_multicast_dict_buffer)
        for unicast in storm_control.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}unicast"):
            interface_storm_control_unicast_dict_buffer = {}
            interface_storm_control_unicast_dict_buffer["id"] = "urn:ngsi-ld:InterfaceStormControlUnicast:" + ":".join(interface_storm_control_dict_buffer["id"].split(":")[3:])
            interface_storm_control_unicast_dict_buffer["type"] = "InterfaceStormControlUnicast"
            interface_storm_control_unicast_dict_buffer["isPartOf"] = {}
            interface_storm_control_unicast_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_storm_control_unicast_dict_buffer["isPartOf"]["object"] = interface_storm_control_dict_buffer["id"]
            interface_storm_control_unicast_dict_buffer["isPartOf"]["observedAt"] = observed_at
            filterState = unicast.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}filter-state")
            if filterState is not None:
                element_text = filterState.text
                if element_text is not None:
                    interface_storm_control_unicast_dict_buffer["filterState"] = {}
                    interface_storm_control_unicast_dict_buffer["filterState"]["type"] = "Property"
                    interface_storm_control_unicast_dict_buffer["filterState"]["value"] = element_text
                    interface_storm_control_unicast_dict_buffer["filterState"]["observedAt"] = observed_at
            for current_rate in unicast.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}current-rate"):
                interface_storm_control_unicast_current_rate_dict_buffer = {}
                interface_storm_control_unicast_current_rate_dict_buffer["id"] = "urn:ngsi-ld:InterfaceStormControlUnicastCurrentRate:" + ":".join(interface_storm_control_unicast_dict_buffer["id"].split(":")[3:])
                interface_storm_control_unicast_current_rate_dict_buffer["type"] = "InterfaceStormControlUnicastCurrentRate"
                interface_storm_control_unicast_current_rate_dict_buffer["isPartOf"] = {}
                interface_storm_control_unicast_current_rate_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_storm_control_unicast_current_rate_dict_buffer["isPartOf"]["object"] = interface_storm_control_unicast_dict_buffer["id"]
                interface_storm_control_unicast_current_rate_dict_buffer["isPartOf"]["observedAt"] = observed_at
                bandwidth = current_rate.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}bandwidth")
                if bandwidth is not None:
                    element_text = bandwidth.text
                    if element_text is not None:
                        interface_storm_control_unicast_current_rate_dict_buffer["bandwidth"] = {}
                        interface_storm_control_unicast_current_rate_dict_buffer["bandwidth"]["type"] = "Property"
                        interface_storm_control_unicast_current_rate_dict_buffer["bandwidth"]["value"] = float(element_text)
                        interface_storm_control_unicast_current_rate_dict_buffer["bandwidth"]["observedAt"] = observed_at
                bps = current_rate.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}bps")
                if bps is not None:
                    element_text = bps.text
                    if element_text is not None:
                        interface_storm_control_unicast_current_rate_dict_buffer["bps"] = {}
                        interface_storm_control_unicast_current_rate_dict_buffer["bps"]["type"] = "Property"
                        interface_storm_control_unicast_current_rate_dict_buffer["bps"]["value"] = int(element_text)
                        interface_storm_control_unicast_current_rate_dict_buffer["bps"]["observedAt"] = observed_at
                pps = current_rate.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}pps")
                if pps is not None:
                    element_text = pps.text
                    if element_text is not None:
                        interface_storm_control_unicast_current_rate_dict_buffer["pps"] = {}
                        interface_storm_control_unicast_current_rate_dict_buffer["pps"]["type"] = "Property"
                        interface_storm_control_unicast_current_rate_dict_buffer["pps"]["value"] = int(element_text)
                        interface_storm_control_unicast_current_rate_dict_buffer["pps"]["observedAt"] = observed_at
                dict_buffers.append(interface_storm_control_unicast_current_rate_dict_buffer)
            dict_buffers.append(interface_storm_control_unicast_dict_buffer)
        for unknown_unicast in storm_control.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}unknown-unicast"):
            interface_storm_control_unknown_unicast_dict_buffer = {}
            interface_storm_control_unknown_unicast_dict_buffer["id"] = "urn:ngsi-ld:InterfaceStormControlUnknownUnicast:" + ":".join(interface_storm_control_dict_buffer["id"].split(":")[3:])
            interface_storm_control_unknown_unicast_dict_buffer["type"] = "InterfaceStormControlUnknownUnicast"
            interface_storm_control_unknown_unicast_dict_buffer["isPartOf"] = {}
            interface_storm_control_unknown_unicast_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_storm_control_unknown_unicast_dict_buffer["isPartOf"]["object"] = interface_storm_control_dict_buffer["id"]
            interface_storm_control_unknown_unicast_dict_buffer["isPartOf"]["observedAt"] = observed_at
            filterState = unknown_unicast.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}filter-state")
            if filterState is not None:
                element_text = filterState.text
                if element_text is not None:
                    interface_storm_control_unknown_unicast_dict_buffer["filterState"] = {}
                    interface_storm_control_unknown_unicast_dict_buffer["filterState"]["type"] = "Property"
                    interface_storm_control_unknown_unicast_dict_buffer["filterState"]["value"] = element_text
                    interface_storm_control_unknown_unicast_dict_buffer["filterState"]["observedAt"] = observed_at
            for current_rate in unknown_unicast.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}current-rate"):
                interface_storm_control_unknown_unicast_current_rate_dict_buffer = {}
                interface_storm_control_unknown_unicast_current_rate_dict_buffer["id"] = "urn:ngsi-ld:InterfaceStormControlUnknownUnicastCurrentRate:" + ":".join(interface_storm_control_unknown_unicast_dict_buffer["id"].split(":")[3:])
                interface_storm_control_unknown_unicast_current_rate_dict_buffer["type"] = "InterfaceStormControlUnknownUnicastCurrentRate"
                interface_storm_control_unknown_unicast_current_rate_dict_buffer["isPartOf"] = {}
                interface_storm_control_unknown_unicast_current_rate_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_storm_control_unknown_unicast_current_rate_dict_buffer["isPartOf"]["object"] = interface_storm_control_unknown_unicast_dict_buffer["id"]
                interface_storm_control_unknown_unicast_current_rate_dict_buffer["isPartOf"]["observedAt"] = observed_at
                bandwidth = current_rate.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}bandwidth")
                if bandwidth is not None:
                    element_text = bandwidth.text
                    if element_text is not None:
                        interface_storm_control_unknown_unicast_current_rate_dict_buffer["bandwidth"] = {}
                        interface_storm_control_unknown_unicast_current_rate_dict_buffer["bandwidth"]["type"] = "Property"
                        interface_storm_control_unknown_unicast_current_rate_dict_buffer["bandwidth"]["value"] = float(element_text)
                        interface_storm_control_unknown_unicast_current_rate_dict_buffer["bandwidth"]["observedAt"] = observed_at
                bps = current_rate.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}bps")
                if bps is not None:
                    element_text = bps.text
                    if element_text is not None:
                        interface_storm_control_unknown_unicast_current_rate_dict_buffer["bps"] = {}
                        interface_storm_control_unknown_unicast_current_rate_dict_buffer["bps"]["type"] = "Property"
                        interface_storm_control_unknown_unicast_current_rate_dict_buffer["bps"]["value"] = int(element_text)
                        interface_storm_control_unknown_unicast_current_rate_dict_buffer["bps"]["observedAt"] = observed_at
                pps = current_rate.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}pps")
                if pps is not None:
                    element_text = pps.text
                    if element_text is not None:
                        interface_storm_control_unknown_unicast_current_rate_dict_buffer["pps"] = {}
                        interface_storm_control_unknown_unicast_current_rate_dict_buffer["pps"]["type"] = "Property"
                        interface_storm_control_unknown_unicast_current_rate_dict_buffer["pps"]["value"] = int(element_text)
                        interface_storm_control_unknown_unicast_current_rate_dict_buffer["pps"]["observedAt"] = observed_at
                dict_buffers.append(interface_storm_control_unknown_unicast_current_rate_dict_buffer)
            dict_buffers.append(interface_storm_control_unknown_unicast_dict_buffer)
        levelSharedSupport = storm_control.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}level-shared-support")
        if levelSharedSupport is not None:
            element_text = levelSharedSupport.text
            if element_text is not None:
                interface_storm_control_dict_buffer["levelSharedSupport"] = {}
                interface_storm_control_dict_buffer["levelSharedSupport"]["type"] = "Property"
                interface_storm_control_dict_buffer["levelSharedSupport"]["value"] = element_text
                interface_storm_control_dict_buffer["levelSharedSupport"]["observedAt"] = observed_at
        for level_shared in storm_control.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}level-shared"):
            interface_storm_control_level_shared_dict_buffer = {}
            interface_storm_control_level_shared_dict_buffer["id"] = "urn:ngsi-ld:InterfaceStormControlLevelShared:" + ":".join(interface_storm_control_dict_buffer["id"].split(":")[3:])
            interface_storm_control_level_shared_dict_buffer["type"] = "InterfaceStormControlLevelShared"
            interface_storm_control_level_shared_dict_buffer["isPartOf"] = {}
            interface_storm_control_level_shared_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_storm_control_level_shared_dict_buffer["isPartOf"]["object"] = interface_storm_control_dict_buffer["id"]
            interface_storm_control_level_shared_dict_buffer["isPartOf"]["observedAt"] = observed_at
            filterState = level_shared.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}filter-state")
            if filterState is not None:
                element_text = filterState.text
                if element_text is not None:
                    interface_storm_control_level_shared_dict_buffer["filterState"] = {}
                    interface_storm_control_level_shared_dict_buffer["filterState"]["type"] = "Property"
                    interface_storm_control_level_shared_dict_buffer["filterState"]["value"] = element_text
                    interface_storm_control_level_shared_dict_buffer["filterState"]["observedAt"] = observed_at
            for current_rate in level_shared.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}current-rate"):
                interface_storm_control_level_shared_current_rate_dict_buffer = {}
                interface_storm_control_level_shared_current_rate_dict_buffer["id"] = "urn:ngsi-ld:InterfaceStormControlLevelSharedCurrentRate:" + ":".join(interface_storm_control_level_shared_dict_buffer["id"].split(":")[3:])
                interface_storm_control_level_shared_current_rate_dict_buffer["type"] = "InterfaceStormControlLevelSharedCurrentRate"
                interface_storm_control_level_shared_current_rate_dict_buffer["isPartOf"] = {}
                interface_storm_control_level_shared_current_rate_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_storm_control_level_shared_current_rate_dict_buffer["isPartOf"]["object"] = interface_storm_control_level_shared_dict_buffer["id"]
                interface_storm_control_level_shared_current_rate_dict_buffer["isPartOf"]["observedAt"] = observed_at
                bandwidth = current_rate.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}bandwidth")
                if bandwidth is not None:
                    element_text = bandwidth.text
                    if element_text is not None:
                        interface_storm_control_level_shared_current_rate_dict_buffer["bandwidth"] = {}
                        interface_storm_control_level_shared_current_rate_dict_buffer["bandwidth"]["type"] = "Property"
                        interface_storm_control_level_shared_current_rate_dict_buffer["bandwidth"]["value"] = float(element_text)
                        interface_storm_control_level_shared_current_rate_dict_buffer["bandwidth"]["observedAt"] = observed_at
                bps = current_rate.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}bps")
                if bps is not None:
                    element_text = bps.text
                    if element_text is not None:
                        interface_storm_control_level_shared_current_rate_dict_buffer["bps"] = {}
                        interface_storm_control_level_shared_current_rate_dict_buffer["bps"]["type"] = "Property"
                        interface_storm_control_level_shared_current_rate_dict_buffer["bps"]["value"] = int(element_text)
                        interface_storm_control_level_shared_current_rate_dict_buffer["bps"]["observedAt"] = observed_at
                pps = current_rate.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}pps")
                if pps is not None:
                    element_text = pps.text
                    if element_text is not None:
                        interface_storm_control_level_shared_current_rate_dict_buffer["pps"] = {}
                        interface_storm_control_level_shared_current_rate_dict_buffer["pps"]["type"] = "Property"
                        interface_storm_control_level_shared_current_rate_dict_buffer["pps"]["value"] = int(element_text)
                        interface_storm_control_level_shared_current_rate_dict_buffer["pps"]["observedAt"] = observed_at
                dict_buffers.append(interface_storm_control_level_shared_current_rate_dict_buffer)
            dict_buffers.append(interface_storm_control_level_shared_dict_buffer)
        dict_buffers.append(interface_storm_control_dict_buffer)
    for ether_state in interface.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}ether-state"):
        interface_ether_state_dict_buffer = {}
        interface_ether_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEtherState:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
        interface_ether_state_dict_buffer["type"] = "InterfaceEtherState"
        interface_ether_state_dict_buffer["isPartOf"] = {}
        interface_ether_state_dict_buffer["isPartOf"]["type"] = "Relationship"
        interface_ether_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
        interface_ether_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
        negotiatedDuplexMode = ether_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}negotiated-duplex-mode")
        if negotiatedDuplexMode is not None:
            element_text = negotiatedDuplexMode.text
            if element_text is not None:
                interface_ether_state_dict_buffer["negotiatedDuplexMode"] = {}
                interface_ether_state_dict_buffer["negotiatedDuplexMode"]["type"] = "Property"
                interface_ether_state_dict_buffer["negotiatedDuplexMode"]["value"] = element_text
                interface_ether_state_dict_buffer["negotiatedDuplexMode"]["observedAt"] = observed_at
        negotiatedPortSpeed = ether_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}negotiated-port-speed")
        if negotiatedPortSpeed is not None:
            element_text = negotiatedPortSpeed.text
            if element_text is not None:
                interface_ether_state_dict_buffer["negotiatedPortSpeed"] = {}
                interface_ether_state_dict_buffer["negotiatedPortSpeed"]["type"] = "Property"
                interface_ether_state_dict_buffer["negotiatedPortSpeed"]["value"] = element_text
                interface_ether_state_dict_buffer["negotiatedPortSpeed"]["observedAt"] = observed_at
        autoNegotiate = ether_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}auto-negotiate")
        if autoNegotiate is not None:
            element_text = autoNegotiate.text
            if element_text is not None:
                interface_ether_state_dict_buffer["autoNegotiate"] = {}
                interface_ether_state_dict_buffer["autoNegotiate"]["type"] = "Property"
                interface_ether_state_dict_buffer["autoNegotiate"]["value"] = eval(element_text.capitalize())
                interface_ether_state_dict_buffer["autoNegotiate"]["observedAt"] = observed_at
        enableFlowControl = ether_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}enable-flow-control")
        if enableFlowControl is not None:
            element_text = enableFlowControl.text
            if element_text is not None:
                interface_ether_state_dict_buffer["enableFlowControl"] = {}
                interface_ether_state_dict_buffer["enableFlowControl"]["type"] = "Property"
                interface_ether_state_dict_buffer["enableFlowControl"]["value"] = eval(element_text.capitalize())
                interface_ether_state_dict_buffer["enableFlowControl"]["observedAt"] = observed_at
        mediaType = ether_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}media-type")
        if mediaType is not None:
            element_text = mediaType.text
            if element_text is not None:
                interface_ether_state_dict_buffer["mediaType"] = {}
                interface_ether_state_dict_buffer["mediaType"]["type"] = "Property"
                interface_ether_state_dict_buffer["mediaType"]["value"] = element_text
                interface_ether_state_dict_buffer["mediaType"]["observedAt"] = observed_at
        dict_buffers.append(interface_ether_state_dict_buffer)
    for ether_stats in interface.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}ether-stats"):
        interface_ether_stats_dict_buffer = {}
        interface_ether_stats_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEtherStats:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
        interface_ether_stats_dict_buffer["type"] = "InterfaceEtherStats"
        interface_ether_stats_dict_buffer["isPartOf"] = {}
        interface_ether_stats_dict_buffer["isPartOf"]["type"] = "Relationship"
        interface_ether_stats_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
        interface_ether_stats_dict_buffer["isPartOf"]["observedAt"] = observed_at
        inMacControlFrames = ether_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-mac-control-frames")
        if inMacControlFrames is not None:
            element_text = inMacControlFrames.text
            if element_text is not None:
                interface_ether_stats_dict_buffer["inMacControlFrames"] = {}
                interface_ether_stats_dict_buffer["inMacControlFrames"]["type"] = "Property"
                interface_ether_stats_dict_buffer["inMacControlFrames"]["value"] = int(element_text)
                interface_ether_stats_dict_buffer["inMacControlFrames"]["observedAt"] = observed_at
        inMacPauseFrames = ether_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-mac-pause-frames")
        if inMacPauseFrames is not None:
            element_text = inMacPauseFrames.text
            if element_text is not None:
                interface_ether_stats_dict_buffer["inMacPauseFrames"] = {}
                interface_ether_stats_dict_buffer["inMacPauseFrames"]["type"] = "Property"
                interface_ether_stats_dict_buffer["inMacPauseFrames"]["value"] = int(element_text)
                interface_ether_stats_dict_buffer["inMacPauseFrames"]["observedAt"] = observed_at
        inOversizeFrames = ether_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-oversize-frames")
        if inOversizeFrames is not None:
            element_text = inOversizeFrames.text
            if element_text is not None:
                interface_ether_stats_dict_buffer["inOversizeFrames"] = {}
                interface_ether_stats_dict_buffer["inOversizeFrames"]["type"] = "Property"
                interface_ether_stats_dict_buffer["inOversizeFrames"]["value"] = int(element_text)
                interface_ether_stats_dict_buffer["inOversizeFrames"]["observedAt"] = observed_at
        inJabberFrames = ether_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-jabber-frames")
        if inJabberFrames is not None:
            element_text = inJabberFrames.text
            if element_text is not None:
                interface_ether_stats_dict_buffer["inJabberFrames"] = {}
                interface_ether_stats_dict_buffer["inJabberFrames"]["type"] = "Property"
                interface_ether_stats_dict_buffer["inJabberFrames"]["value"] = int(element_text)
                interface_ether_stats_dict_buffer["inJabberFrames"]["observedAt"] = observed_at
        inFragmentFrames = ether_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-fragment-frames")
        if inFragmentFrames is not None:
            element_text = inFragmentFrames.text
            if element_text is not None:
                interface_ether_stats_dict_buffer["inFragmentFrames"] = {}
                interface_ether_stats_dict_buffer["inFragmentFrames"]["type"] = "Property"
                interface_ether_stats_dict_buffer["inFragmentFrames"]["value"] = int(element_text)
                interface_ether_stats_dict_buffer["inFragmentFrames"]["observedAt"] = observed_at
        in8021qFrames = ether_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-8021q-frames")
        if in8021qFrames is not None:
            element_text = in8021qFrames.text
            if element_text is not None:
                interface_ether_stats_dict_buffer["in8021qFrames"] = {}
                interface_ether_stats_dict_buffer["in8021qFrames"]["type"] = "Property"
                interface_ether_stats_dict_buffer["in8021qFrames"]["value"] = int(element_text)
                interface_ether_stats_dict_buffer["in8021qFrames"]["observedAt"] = observed_at
        outMacControlFrames = ether_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}out-mac-control-frames")
        if outMacControlFrames is not None:
            element_text = outMacControlFrames.text
            if element_text is not None:
                interface_ether_stats_dict_buffer["outMacControlFrames"] = {}
                interface_ether_stats_dict_buffer["outMacControlFrames"]["type"] = "Property"
                interface_ether_stats_dict_buffer["outMacControlFrames"]["value"] = int(element_text)
                interface_ether_stats_dict_buffer["outMacControlFrames"]["observedAt"] = observed_at
        outMacPauseFrames = ether_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}out-mac-pause-frames")
        if outMacPauseFrames is not None:
            element_text = outMacPauseFrames.text
            if element_text is not None:
                interface_ether_stats_dict_buffer["outMacPauseFrames"] = {}
                interface_ether_stats_dict_buffer["outMacPauseFrames"]["type"] = "Property"
                interface_ether_stats_dict_buffer["outMacPauseFrames"]["value"] = int(element_text)
                interface_ether_stats_dict_buffer["outMacPauseFrames"]["observedAt"] = observed_at
        out8021qFrames = ether_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}out-8021q-frames")
        if out8021qFrames is not None:
            element_text = out8021qFrames.text
            if element_text is not None:
                interface_ether_stats_dict_buffer["out8021qFrames"] = {}
                interface_ether_stats_dict_buffer["out8021qFrames"]["type"] = "Property"
                interface_ether_stats_dict_buffer["out8021qFrames"]["value"] = int(element_text)
                interface_ether_stats_dict_buffer["out8021qFrames"]["observedAt"] = observed_at
        dot3CountersSupported = ether_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-counters-supported")
        if dot3CountersSupported is not None:
            element_text = dot3CountersSupported.text
            if element_text is not None:
                interface_ether_stats_dict_buffer["dot3CountersSupported"] = {}
                interface_ether_stats_dict_buffer["dot3CountersSupported"]["type"] = "Property"
                interface_ether_stats_dict_buffer["dot3CountersSupported"]["value"] = element_text
                interface_ether_stats_dict_buffer["dot3CountersSupported"]["observedAt"] = observed_at
        for dot3_counters in ether_stats.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-counters"):
            interface_ether_stats_dot3_counters_dict_buffer = {}
            interface_ether_stats_dot3_counters_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEtherStatsDot3Counters:" + ":".join(interface_ether_stats_dict_buffer["id"].split(":")[3:])
            interface_ether_stats_dot3_counters_dict_buffer["type"] = "InterfaceEtherStatsDot3Counters"
            interface_ether_stats_dot3_counters_dict_buffer["isPartOf"] = {}
            interface_ether_stats_dot3_counters_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_ether_stats_dot3_counters_dict_buffer["isPartOf"]["object"] = interface_ether_stats_dict_buffer["id"]
            interface_ether_stats_dot3_counters_dict_buffer["isPartOf"]["observedAt"] = observed_at
            dot3StatsVersion = dot3_counters.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-stats-version")
            if dot3StatsVersion is not None:
                element_text = dot3StatsVersion.text
                if element_text is not None:
                    interface_ether_stats_dot3_counters_dict_buffer["dot3StatsVersion"] = {}
                    interface_ether_stats_dot3_counters_dict_buffer["dot3StatsVersion"]["type"] = "Property"
                    interface_ether_stats_dot3_counters_dict_buffer["dot3StatsVersion"]["value"] = element_text
                    interface_ether_stats_dot3_counters_dict_buffer["dot3StatsVersion"]["observedAt"] = observed_at
            for dot3_error_counters_v2 in dot3_counters.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-error-counters-v2"):
                interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer = {}
                interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEtherStatsDot3CountersDot3ErrorCountersV2:" + ":".join(interface_ether_stats_dot3_counters_dict_buffer["id"].split(":")[3:])
                interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["type"] = "InterfaceEtherStatsDot3CountersDot3ErrorCountersV2"
                interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["isPartOf"] = {}
                interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["isPartOf"]["object"] = interface_ether_stats_dot3_counters_dict_buffer["id"]
                interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["isPartOf"]["observedAt"] = observed_at
                dot3AlignmentErrors = dot3_error_counters_v2.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-alignment-errors")
                if dot3AlignmentErrors is not None:
                    element_text = dot3AlignmentErrors.text
                    if element_text is not None:
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3AlignmentErrors"] = {}
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3AlignmentErrors"]["type"] = "Property"
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3AlignmentErrors"]["value"] = int(element_text)
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3AlignmentErrors"]["observedAt"] = observed_at
                dot3FcsErrors = dot3_error_counters_v2.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-fcs-errors")
                if dot3FcsErrors is not None:
                    element_text = dot3FcsErrors.text
                    if element_text is not None:
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3FcsErrors"] = {}
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3FcsErrors"]["type"] = "Property"
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3FcsErrors"]["value"] = int(element_text)
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3FcsErrors"]["observedAt"] = observed_at
                dot3SingleCollisionFrames = dot3_error_counters_v2.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-single-collision-frames")
                if dot3SingleCollisionFrames is not None:
                    element_text = dot3SingleCollisionFrames.text
                    if element_text is not None:
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3SingleCollisionFrames"] = {}
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3SingleCollisionFrames"]["type"] = "Property"
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3SingleCollisionFrames"]["value"] = int(element_text)
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3SingleCollisionFrames"]["observedAt"] = observed_at
                dot3MultipleCollisionFrames = dot3_error_counters_v2.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-multiple-collision-frames")
                if dot3MultipleCollisionFrames is not None:
                    element_text = dot3MultipleCollisionFrames.text
                    if element_text is not None:
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3MultipleCollisionFrames"] = {}
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3MultipleCollisionFrames"]["type"] = "Property"
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3MultipleCollisionFrames"]["value"] = int(element_text)
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3MultipleCollisionFrames"]["observedAt"] = observed_at
                dot3SqeTestErrors = dot3_error_counters_v2.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-sqe-test-errors")
                if dot3SqeTestErrors is not None:
                    element_text = dot3SqeTestErrors.text
                    if element_text is not None:
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3SqeTestErrors"] = {}
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3SqeTestErrors"]["type"] = "Property"
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3SqeTestErrors"]["value"] = int(element_text)
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3SqeTestErrors"]["observedAt"] = observed_at
                dot3DeferredTransmissions = dot3_error_counters_v2.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-deferred-transmissions")
                if dot3DeferredTransmissions is not None:
                    element_text = dot3DeferredTransmissions.text
                    if element_text is not None:
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3DeferredTransmissions"] = {}
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3DeferredTransmissions"]["type"] = "Property"
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3DeferredTransmissions"]["value"] = int(element_text)
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3DeferredTransmissions"]["observedAt"] = observed_at
                dot3LateCollisions = dot3_error_counters_v2.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-late-collisions")
                if dot3LateCollisions is not None:
                    element_text = dot3LateCollisions.text
                    if element_text is not None:
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3LateCollisions"] = {}
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3LateCollisions"]["type"] = "Property"
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3LateCollisions"]["value"] = int(element_text)
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3LateCollisions"]["observedAt"] = observed_at
                dot3ExcessiveCollisions = dot3_error_counters_v2.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-excessive-collisions")
                if dot3ExcessiveCollisions is not None:
                    element_text = dot3ExcessiveCollisions.text
                    if element_text is not None:
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3ExcessiveCollisions"] = {}
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3ExcessiveCollisions"]["type"] = "Property"
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3ExcessiveCollisions"]["value"] = int(element_text)
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3ExcessiveCollisions"]["observedAt"] = observed_at
                dot3InternalMacTransmitErrors = dot3_error_counters_v2.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-internal-mac-transmit-errors")
                if dot3InternalMacTransmitErrors is not None:
                    element_text = dot3InternalMacTransmitErrors.text
                    if element_text is not None:
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3InternalMacTransmitErrors"] = {}
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3InternalMacTransmitErrors"]["type"] = "Property"
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3InternalMacTransmitErrors"]["value"] = int(element_text)
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3InternalMacTransmitErrors"]["observedAt"] = observed_at
                dot3CarrierSenseErrors = dot3_error_counters_v2.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-carrier-sense-errors")
                if dot3CarrierSenseErrors is not None:
                    element_text = dot3CarrierSenseErrors.text
                    if element_text is not None:
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3CarrierSenseErrors"] = {}
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3CarrierSenseErrors"]["type"] = "Property"
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3CarrierSenseErrors"]["value"] = int(element_text)
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3CarrierSenseErrors"]["observedAt"] = observed_at
                dot3FrameTooLongs = dot3_error_counters_v2.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-frame-too-longs")
                if dot3FrameTooLongs is not None:
                    element_text = dot3FrameTooLongs.text
                    if element_text is not None:
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3FrameTooLongs"] = {}
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3FrameTooLongs"]["type"] = "Property"
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3FrameTooLongs"]["value"] = int(element_text)
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3FrameTooLongs"]["observedAt"] = observed_at
                dot3InternalMacReceiveErrors = dot3_error_counters_v2.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-internal-mac-receive-errors")
                if dot3InternalMacReceiveErrors is not None:
                    element_text = dot3InternalMacReceiveErrors.text
                    if element_text is not None:
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3InternalMacReceiveErrors"] = {}
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3InternalMacReceiveErrors"]["type"] = "Property"
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3InternalMacReceiveErrors"]["value"] = int(element_text)
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3InternalMacReceiveErrors"]["observedAt"] = observed_at
                dot3SymbolErrors = dot3_error_counters_v2.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-symbol-errors")
                if dot3SymbolErrors is not None:
                    element_text = dot3SymbolErrors.text
                    if element_text is not None:
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3SymbolErrors"] = {}
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3SymbolErrors"]["type"] = "Property"
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3SymbolErrors"]["value"] = int(element_text)
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3SymbolErrors"]["observedAt"] = observed_at
                dot3DuplexStatus = dot3_error_counters_v2.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-duplex-status")
                if dot3DuplexStatus is not None:
                    element_text = dot3DuplexStatus.text
                    if element_text is not None:
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3DuplexStatus"] = {}
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3DuplexStatus"]["type"] = "Property"
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3DuplexStatus"]["value"] = int(element_text)
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3DuplexStatus"]["observedAt"] = observed_at
                dot3HcAlignmentErrors = dot3_error_counters_v2.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-hc-alignment-errors")
                if dot3HcAlignmentErrors is not None:
                    element_text = dot3HcAlignmentErrors.text
                    if element_text is not None:
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcAlignmentErrors"] = {}
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcAlignmentErrors"]["type"] = "Property"
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcAlignmentErrors"]["value"] = int(element_text)
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcAlignmentErrors"]["observedAt"] = observed_at
                dot3HcInpauseFrames = dot3_error_counters_v2.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-hc-inpause-frames")
                if dot3HcInpauseFrames is not None:
                    element_text = dot3HcInpauseFrames.text
                    if element_text is not None:
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcInpauseFrames"] = {}
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcInpauseFrames"]["type"] = "Property"
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcInpauseFrames"]["value"] = int(element_text)
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcInpauseFrames"]["observedAt"] = observed_at
                dot3HcOutpauseFrames = dot3_error_counters_v2.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-hc-outpause-frames")
                if dot3HcOutpauseFrames is not None:
                    element_text = dot3HcOutpauseFrames.text
                    if element_text is not None:
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcOutpauseFrames"] = {}
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcOutpauseFrames"]["type"] = "Property"
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcOutpauseFrames"]["value"] = int(element_text)
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcOutpauseFrames"]["observedAt"] = observed_at
                dot3HcFcsErrors = dot3_error_counters_v2.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-hc-fcs-errors")
                if dot3HcFcsErrors is not None:
                    element_text = dot3HcFcsErrors.text
                    if element_text is not None:
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcFcsErrors"] = {}
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcFcsErrors"]["type"] = "Property"
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcFcsErrors"]["value"] = int(element_text)
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcFcsErrors"]["observedAt"] = observed_at
                dot3HcFrameTooLongs = dot3_error_counters_v2.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-hc-frame-too-longs")
                if dot3HcFrameTooLongs is not None:
                    element_text = dot3HcFrameTooLongs.text
                    if element_text is not None:
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcFrameTooLongs"] = {}
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcFrameTooLongs"]["type"] = "Property"
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcFrameTooLongs"]["value"] = int(element_text)
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcFrameTooLongs"]["observedAt"] = observed_at
                dot3HcInternalMacTransmitErrors = dot3_error_counters_v2.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-hc-internal-mac-transmit-errors")
                if dot3HcInternalMacTransmitErrors is not None:
                    element_text = dot3HcInternalMacTransmitErrors.text
                    if element_text is not None:
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcInternalMacTransmitErrors"] = {}
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcInternalMacTransmitErrors"]["type"] = "Property"
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcInternalMacTransmitErrors"]["value"] = int(element_text)
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcInternalMacTransmitErrors"]["observedAt"] = observed_at
                dot3HcInternalMacReceiveErrors = dot3_error_counters_v2.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-hc-internal-mac-receive-errors")
                if dot3HcInternalMacReceiveErrors is not None:
                    element_text = dot3HcInternalMacReceiveErrors.text
                    if element_text is not None:
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcInternalMacReceiveErrors"] = {}
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcInternalMacReceiveErrors"]["type"] = "Property"
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcInternalMacReceiveErrors"]["value"] = int(element_text)
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcInternalMacReceiveErrors"]["observedAt"] = observed_at
                dot3HcSymbolErrors = dot3_error_counters_v2.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dot3-hc-symbol-errors")
                if dot3HcSymbolErrors is not None:
                    element_text = dot3HcSymbolErrors.text
                    if element_text is not None:
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcSymbolErrors"] = {}
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcSymbolErrors"]["type"] = "Property"
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcSymbolErrors"]["value"] = int(element_text)
                        interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer["dot3HcSymbolErrors"]["observedAt"] = observed_at
                dict_buffers.append(interface_ether_stats_dot3_counters_dot3_error_counters_v2_dict_buffer)
            dict_buffers.append(interface_ether_stats_dot3_counters_dict_buffer)
        dict_buffers.append(interface_ether_stats_dict_buffer)
    for serial_state in interface.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}serial-state"):
        interface_serial_state_dict_buffer = {}
        interface_serial_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSerialState:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
        interface_serial_state_dict_buffer["type"] = "InterfaceSerialState"
        interface_serial_state_dict_buffer["isPartOf"] = {}
        interface_serial_state_dict_buffer["isPartOf"]["type"] = "Relationship"
        interface_serial_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
        interface_serial_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
        crcType = serial_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}crc-type")
        if crcType is not None:
            element_text = crcType.text
            if element_text is not None:
                interface_serial_state_dict_buffer["crcType"] = {}
                interface_serial_state_dict_buffer["crcType"]["type"] = "Property"
                interface_serial_state_dict_buffer["crcType"]["value"] = element_text
                interface_serial_state_dict_buffer["crcType"]["observedAt"] = observed_at
        loopback = serial_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}loopback")
        if loopback is not None:
            element_text = loopback.text
            if element_text is not None:
                interface_serial_state_dict_buffer["loopback"] = {}
                interface_serial_state_dict_buffer["loopback"]["type"] = "Property"
                interface_serial_state_dict_buffer["loopback"]["value"] = element_text
                interface_serial_state_dict_buffer["loopback"]["observedAt"] = observed_at
        keeplive = serial_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}keeplive")
        if keeplive is not None:
            element_text = keeplive.text
            if element_text is not None:
                interface_serial_state_dict_buffer["keeplive"] = {}
                interface_serial_state_dict_buffer["keeplive"]["type"] = "Property"
                interface_serial_state_dict_buffer["keeplive"]["value"] = int(element_text)
                interface_serial_state_dict_buffer["keeplive"]["observedAt"] = observed_at
        timeslot = serial_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}timeslot")
        if timeslot is not None:
            element_text = timeslot.text
            if element_text is not None:
                interface_serial_state_dict_buffer["timeslot"] = {}
                interface_serial_state_dict_buffer["timeslot"]["type"] = "Property"
                interface_serial_state_dict_buffer["timeslot"]["value"] = int(element_text)
                interface_serial_state_dict_buffer["timeslot"]["observedAt"] = observed_at
        subrate = serial_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}subrate")
        if subrate is not None:
            element_text = subrate.text
            if element_text is not None:
                interface_serial_state_dict_buffer["subrate"] = {}
                interface_serial_state_dict_buffer["subrate"]["type"] = "Property"
                interface_serial_state_dict_buffer["subrate"]["value"] = element_text
                interface_serial_state_dict_buffer["subrate"]["observedAt"] = observed_at
        dict_buffers.append(interface_serial_state_dict_buffer)
    for serial_stats in interface.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}serial-stats"):
        interface_serial_stats_dict_buffer = {}
        interface_serial_stats_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSerialStats:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
        interface_serial_stats_dict_buffer["type"] = "InterfaceSerialStats"
        interface_serial_stats_dict_buffer["isPartOf"] = {}
        interface_serial_stats_dict_buffer["isPartOf"]["type"] = "Relationship"
        interface_serial_stats_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
        interface_serial_stats_dict_buffer["isPartOf"]["observedAt"] = observed_at
        inAbortClockError = serial_stats.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}in-abort-clock-error")
        if inAbortClockError is not None:
            element_text = inAbortClockError.text
            if element_text is not None:
                interface_serial_stats_dict_buffer["inAbortClockError"] = {}
                interface_serial_stats_dict_buffer["inAbortClockError"]["type"] = "Property"
                interface_serial_stats_dict_buffer["inAbortClockError"]["value"] = int(element_text)
                interface_serial_stats_dict_buffer["inAbortClockError"]["observedAt"] = observed_at
        dict_buffers.append(interface_serial_stats_dict_buffer)
    intfClassUnspecified = interface.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}intf-class-unspecified")
    if intfClassUnspecified is not None:
        element_text = intfClassUnspecified.text
        if element_text is not None:
            interface_dict_buffer["intfClassUnspecified"] = {}
            interface_dict_buffer["intfClassUnspecified"]["type"] = "Property"
            interface_dict_buffer["intfClassUnspecified"]["value"] = eval(element_text.capitalize())
            interface_dict_buffer["intfClassUnspecified"]["observedAt"] = observed_at
    for syncserial_state in interface.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}syncserial-state"):
        interface_syncserial_state_dict_buffer = {}
        interface_syncserial_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSyncserialState:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
        interface_syncserial_state_dict_buffer["type"] = "InterfaceSyncserialState"
        interface_syncserial_state_dict_buffer["isPartOf"] = {}
        interface_syncserial_state_dict_buffer["isPartOf"]["type"] = "Relationship"
        interface_syncserial_state_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
        interface_syncserial_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
        carrierDelay = syncserial_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}carrier-delay")
        if carrierDelay is not None:
            element_text = carrierDelay.text
            if element_text is not None:
                interface_syncserial_state_dict_buffer["carrierDelay"] = {}
                interface_syncserial_state_dict_buffer["carrierDelay"]["type"] = "Property"
                interface_syncserial_state_dict_buffer["carrierDelay"]["value"] = int(element_text)
                interface_syncserial_state_dict_buffer["carrierDelay"]["observedAt"] = observed_at
        dtrPulseTime = syncserial_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dtr-pulse-time")
        if dtrPulseTime is not None:
            element_text = dtrPulseTime.text
            if element_text is not None:
                interface_syncserial_state_dict_buffer["dtrPulseTime"] = {}
                interface_syncserial_state_dict_buffer["dtrPulseTime"]["type"] = "Property"
                interface_syncserial_state_dict_buffer["dtrPulseTime"]["value"] = int(element_text)
                interface_syncserial_state_dict_buffer["dtrPulseTime"]["observedAt"] = observed_at
        restartDelay = syncserial_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}restart-delay")
        if restartDelay is not None:
            element_text = restartDelay.text
            if element_text is not None:
                interface_syncserial_state_dict_buffer["restartDelay"] = {}
                interface_syncserial_state_dict_buffer["restartDelay"]["type"] = "Property"
                interface_syncserial_state_dict_buffer["restartDelay"]["value"] = int(element_text)
                interface_syncserial_state_dict_buffer["restartDelay"]["observedAt"] = observed_at
        cableType = syncserial_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}cable-type")
        if cableType is not None:
            element_text = cableType.text
            if element_text is not None:
                interface_syncserial_state_dict_buffer["cableType"] = {}
                interface_syncserial_state_dict_buffer["cableType"]["type"] = "Property"
                interface_syncserial_state_dict_buffer["cableType"]["value"] = element_text
                interface_syncserial_state_dict_buffer["cableType"]["observedAt"] = observed_at
        loopback = syncserial_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}loopback")
        if loopback is not None:
            element_text = loopback.text
            if element_text is not None:
                interface_syncserial_state_dict_buffer["loopback"] = {}
                interface_syncserial_state_dict_buffer["loopback"]["type"] = "Property"
                interface_syncserial_state_dict_buffer["loopback"]["value"] = eval(element_text.capitalize())
                interface_syncserial_state_dict_buffer["loopback"]["observedAt"] = observed_at
        nrziEncoding = syncserial_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}nrzi-encoding")
        if nrziEncoding is not None:
            element_text = nrziEncoding.text
            if element_text is not None:
                interface_syncserial_state_dict_buffer["nrziEncoding"] = {}
                interface_syncserial_state_dict_buffer["nrziEncoding"]["type"] = "Property"
                interface_syncserial_state_dict_buffer["nrziEncoding"]["value"] = eval(element_text.capitalize())
                interface_syncserial_state_dict_buffer["nrziEncoding"]["observedAt"] = observed_at
        idleCharacter = syncserial_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}idle-character")
        if idleCharacter is not None:
            element_text = idleCharacter.text
            if element_text is not None:
                interface_syncserial_state_dict_buffer["id"] = interface_syncserial_state_dict_buffer["id"] + ":" + element_text
                interface_syncserial_state_dict_buffer["idleCharacter"] = {}
                interface_syncserial_state_dict_buffer["idleCharacter"]["type"] = "Property"
                interface_syncserial_state_dict_buffer["idleCharacter"]["value"] = element_text
                interface_syncserial_state_dict_buffer["idleCharacter"]["observedAt"] = observed_at
        rtsSignal = syncserial_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}rts-signal")
        if rtsSignal is not None:
            element_text = rtsSignal.text
            if element_text is not None:
                interface_syncserial_state_dict_buffer["rtsSignal"] = {}
                interface_syncserial_state_dict_buffer["rtsSignal"]["type"] = "Property"
                interface_syncserial_state_dict_buffer["rtsSignal"]["value"] = element_text
                interface_syncserial_state_dict_buffer["rtsSignal"]["observedAt"] = observed_at
        ctsSignal = syncserial_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}cts-signal")
        if ctsSignal is not None:
            element_text = ctsSignal.text
            if element_text is not None:
                interface_syncserial_state_dict_buffer["ctsSignal"] = {}
                interface_syncserial_state_dict_buffer["ctsSignal"]["type"] = "Property"
                interface_syncserial_state_dict_buffer["ctsSignal"]["value"] = element_text
                interface_syncserial_state_dict_buffer["ctsSignal"]["observedAt"] = observed_at
        dtrSignal = syncserial_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dtr-signal")
        if dtrSignal is not None:
            element_text = dtrSignal.text
            if element_text is not None:
                interface_syncserial_state_dict_buffer["dtrSignal"] = {}
                interface_syncserial_state_dict_buffer["dtrSignal"]["type"] = "Property"
                interface_syncserial_state_dict_buffer["dtrSignal"]["value"] = element_text
                interface_syncserial_state_dict_buffer["dtrSignal"]["observedAt"] = observed_at
        dcdSignal = syncserial_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dcd-signal")
        if dcdSignal is not None:
            element_text = dcdSignal.text
            if element_text is not None:
                interface_syncserial_state_dict_buffer["dcdSignal"] = {}
                interface_syncserial_state_dict_buffer["dcdSignal"]["type"] = "Property"
                interface_syncserial_state_dict_buffer["dcdSignal"]["value"] = element_text
                interface_syncserial_state_dict_buffer["dcdSignal"]["observedAt"] = observed_at
        dsrSignal = syncserial_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dsr-signal")
        if dsrSignal is not None:
            element_text = dsrSignal.text
            if element_text is not None:
                interface_syncserial_state_dict_buffer["dsrSignal"] = {}
                interface_syncserial_state_dict_buffer["dsrSignal"]["type"] = "Property"
                interface_syncserial_state_dict_buffer["dsrSignal"]["value"] = element_text
                interface_syncserial_state_dict_buffer["dsrSignal"]["observedAt"] = observed_at
        for dce_mode_state in syncserial_state.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dce-mode-state"):
            interface_syncserial_state_dce_mode_state_dict_buffer = {}
            interface_syncserial_state_dce_mode_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSyncserialStateDceModeState:" + ":".join(interface_syncserial_state_dict_buffer["id"].split(":")[3:])
            interface_syncserial_state_dce_mode_state_dict_buffer["type"] = "InterfaceSyncserialStateDceModeState"
            interface_syncserial_state_dce_mode_state_dict_buffer["isPartOf"] = {}
            interface_syncserial_state_dce_mode_state_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_syncserial_state_dce_mode_state_dict_buffer["isPartOf"]["object"] = interface_syncserial_state_dict_buffer["id"]
            interface_syncserial_state_dce_mode_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
            dceTerminalTimingEnable = dce_mode_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dce-terminal-timing-enable")
            if dceTerminalTimingEnable is not None:
                element_text = dceTerminalTimingEnable.text
                if element_text is not None:
                    interface_syncserial_state_dce_mode_state_dict_buffer["dceTerminalTimingEnable"] = {}
                    interface_syncserial_state_dce_mode_state_dict_buffer["dceTerminalTimingEnable"]["type"] = "Property"
                    interface_syncserial_state_dce_mode_state_dict_buffer["dceTerminalTimingEnable"]["value"] = eval(element_text.capitalize())
                    interface_syncserial_state_dce_mode_state_dict_buffer["dceTerminalTimingEnable"]["observedAt"] = observed_at
            ignoreDtr = dce_mode_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}ignore-dtr")
            if ignoreDtr is not None:
                element_text = ignoreDtr.text
                if element_text is not None:
                    interface_syncserial_state_dce_mode_state_dict_buffer["ignoreDtr"] = {}
                    interface_syncserial_state_dce_mode_state_dict_buffer["ignoreDtr"]["type"] = "Property"
                    interface_syncserial_state_dce_mode_state_dict_buffer["ignoreDtr"]["value"] = eval(element_text.capitalize())
                    interface_syncserial_state_dce_mode_state_dict_buffer["ignoreDtr"]["observedAt"] = observed_at
            serialClockRate = dce_mode_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}serial-clock-rate")
            if serialClockRate is not None:
                element_text = serialClockRate.text
                if element_text is not None:
                    interface_syncserial_state_dce_mode_state_dict_buffer["serialClockRate"] = {}
                    interface_syncserial_state_dce_mode_state_dict_buffer["serialClockRate"]["type"] = "Property"
                    interface_syncserial_state_dce_mode_state_dict_buffer["serialClockRate"]["value"] = int(element_text)
                    interface_syncserial_state_dce_mode_state_dict_buffer["serialClockRate"]["observedAt"] = observed_at
            dict_buffers.append(interface_syncserial_state_dce_mode_state_dict_buffer)
        for dte_mode_state in syncserial_state.findall(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}dte-mode-state"):
            interface_syncserial_state_dte_mode_state_dict_buffer = {}
            interface_syncserial_state_dte_mode_state_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSyncserialStateDteModeState:" + ":".join(interface_syncserial_state_dict_buffer["id"].split(":")[3:])
            interface_syncserial_state_dte_mode_state_dict_buffer["type"] = "InterfaceSyncserialStateDteModeState"
            interface_syncserial_state_dte_mode_state_dict_buffer["isPartOf"] = {}
            interface_syncserial_state_dte_mode_state_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_syncserial_state_dte_mode_state_dict_buffer["isPartOf"]["object"] = interface_syncserial_state_dict_buffer["id"]
            interface_syncserial_state_dte_mode_state_dict_buffer["isPartOf"]["observedAt"] = observed_at
            txInvertClk = dte_mode_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}tx-invert-clk")
            if txInvertClk is not None:
                element_text = txInvertClk.text
                if element_text is not None:
                    interface_syncserial_state_dte_mode_state_dict_buffer["txInvertClk"] = {}
                    interface_syncserial_state_dte_mode_state_dict_buffer["txInvertClk"]["type"] = "Property"
                    interface_syncserial_state_dte_mode_state_dict_buffer["txInvertClk"]["value"] = eval(element_text.capitalize())
                    interface_syncserial_state_dte_mode_state_dict_buffer["txInvertClk"]["observedAt"] = observed_at
            ignoreDcd = dte_mode_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}ignore-dcd")
            if ignoreDcd is not None:
                element_text = ignoreDcd.text
                if element_text is not None:
                    interface_syncserial_state_dte_mode_state_dict_buffer["ignoreDcd"] = {}
                    interface_syncserial_state_dte_mode_state_dict_buffer["ignoreDcd"]["type"] = "Property"
                    interface_syncserial_state_dte_mode_state_dict_buffer["ignoreDcd"]["value"] = eval(element_text.capitalize())
                    interface_syncserial_state_dte_mode_state_dict_buffer["ignoreDcd"]["observedAt"] = observed_at
            rxClockrate = dte_mode_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}rx-clockrate")
            if rxClockrate is not None:
                element_text = rxClockrate.text
                if element_text is not None:
                    interface_syncserial_state_dte_mode_state_dict_buffer["rxClockrate"] = {}
                    interface_syncserial_state_dte_mode_state_dict_buffer["rxClockrate"]["type"] = "Property"
                    interface_syncserial_state_dte_mode_state_dict_buffer["rxClockrate"]["value"] = int(element_text)
                    interface_syncserial_state_dte_mode_state_dict_buffer["rxClockrate"]["observedAt"] = observed_at
            rxClockThreshold = dte_mode_state.find(".//{http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper}rx-clock-threshold")
            if rxClockThreshold is not None:
                element_text = rxClockThreshold.text
                if element_text is not None:
                    interface_syncserial_state_dte_mode_state_dict_buffer["rxClockThreshold"] = {}
                    interface_syncserial_state_dte_mode_state_dict_buffer["rxClockThreshold"]["type"] = "Property"
                    interface_syncserial_state_dte_mode_state_dict_buffer["rxClockThreshold"]["value"] = int(element_text)
                    interface_syncserial_state_dte_mode_state_dict_buffer["rxClockThreshold"]["observedAt"] = observed_at
            dict_buffers.append(interface_syncserial_state_dte_mode_state_dict_buffer)
        dict_buffers.append(interface_syncserial_state_dict_buffer)
    dict_buffers.append(interface_dict_buffer)

print(json.dumps(dict_buffers[::-1], indent=4))
dict_buffers.clear()
