import json
import numpy as np
import sys

json_payload = sys.argv[1]
dict_buffers = []
with open(json_payload) as f:
    data = json.load(f)
    json_data = data[0]["updates"][0]["values"]
    timestamp_data = int(data[0]["timestamp"])
    datetime_ns = np.datetime64(timestamp_data, 'ns')
    observed_at = str(datetime_ns.astype('datetime64[ms]')) + 'Z'
    source = "-".join(data[0]["source"].split(":")[0].split("-")[1:-1]) + ":" + str(data[0]["source"].split(":")[0].split("-")[-1])

if "" in json_data:
    json_data = json_data[""]

interface = None
if json_data.get("interface")is not None:
    interface = json_data.get("interface")
elif json_data.get("srl_nokia-interfaces:interface")is not None:
    interface = json_data.get("srl_nokia-interfaces:interface")
for interface in interface:
    if interface is not None and len(interface) != 0:
        interface_dict_buffer = {}
        interface_dict_buffer["id"] = "urn:ngsi-ld:Interface:" + source
        interface_dict_buffer["type"] = "Interface"
        name = interface.get("name")
        if name is not None:
            element_text = name
            if interface_dict_buffer["id"].split(":")[-1] != element_text:
                interface_dict_buffer["id"] = interface_dict_buffer["id"] + ":" + element_text
            interface_dict_buffer["name"] = {}
            interface_dict_buffer["name"]["type"] = "Property"
            interface_dict_buffer["name"]["value"] = element_text
            interface_dict_buffer["name"]["observedAt"] = observed_at
        description = interface.get("description")
        if description is not None:
            element_text = description
            interface_dict_buffer["description"] = {}
            interface_dict_buffer["description"]["type"] = "Property"
            interface_dict_buffer["description"]["value"] = element_text
            interface_dict_buffer["description"]["observedAt"] = observed_at
        adminState = interface.get("admin-state")
        if adminState is not None:
            element_text = adminState
            interface_dict_buffer["adminState"] = {}
            interface_dict_buffer["adminState"]["type"] = "Property"
            interface_dict_buffer["adminState"]["value"] = element_text
            interface_dict_buffer["adminState"]["observedAt"] = observed_at
        breakout_mode = interface.get("breakout-mode")
        if breakout_mode is not None and len(breakout_mode) != 0:
            interface_breakout_mode_dict_buffer = {}
            interface_breakout_mode_dict_buffer["id"] = "urn:ngsi-ld:InterfaceBreakoutMode:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
            interface_breakout_mode_dict_buffer["type"] = "InterfaceBreakoutMode"
            interface_breakout_mode_dict_buffer["isPartOf"] = {}
            interface_breakout_mode_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_breakout_mode_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
            interface_breakout_mode_dict_buffer["isPartOf"]["observedAt"] = observed_at
            numBreakoutPorts = breakout_mode.get("num-breakout-ports")
            if numBreakoutPorts is not None:
                element_text = numBreakoutPorts
                interface_breakout_mode_dict_buffer["numBreakoutPorts"] = {}
                interface_breakout_mode_dict_buffer["numBreakoutPorts"]["type"] = "Property"
                interface_breakout_mode_dict_buffer["numBreakoutPorts"]["value"] = element_text
                interface_breakout_mode_dict_buffer["numBreakoutPorts"]["observedAt"] = observed_at
            breakoutPortSpeed = breakout_mode.get("breakout-port-speed")
            if breakoutPortSpeed is not None:
                element_text = breakoutPortSpeed
                interface_breakout_mode_dict_buffer["breakoutPortSpeed"] = {}
                interface_breakout_mode_dict_buffer["breakoutPortSpeed"]["type"] = "Property"
                interface_breakout_mode_dict_buffer["breakoutPortSpeed"]["value"] = element_text
                interface_breakout_mode_dict_buffer["breakoutPortSpeed"]["observedAt"] = observed_at
            dict_buffers.append(interface_breakout_mode_dict_buffer)
        mtu = interface.get("mtu")
        if mtu is not None:
            element_text = mtu
            interface_dict_buffer["mtu"] = {}
            interface_dict_buffer["mtu"]["type"] = "Property"
            interface_dict_buffer["mtu"]["value"] = int(element_text)
            interface_dict_buffer["mtu"]["observedAt"] = observed_at
        ifindex = interface.get("ifindex")
        if ifindex is not None:
            element_text = ifindex
            interface_dict_buffer["ifindex"] = {}
            interface_dict_buffer["ifindex"]["type"] = "Property"
            interface_dict_buffer["ifindex"]["value"] = int(element_text)
            interface_dict_buffer["ifindex"]["observedAt"] = observed_at
        operState = interface.get("oper-state")
        if operState is not None:
            element_text = operState
            interface_dict_buffer["operState"] = {}
            interface_dict_buffer["operState"]["type"] = "Property"
            interface_dict_buffer["operState"]["value"] = element_text
            interface_dict_buffer["operState"]["observedAt"] = observed_at
        operDownReason = interface.get("oper-down-reason")
        if operDownReason is not None:
            element_text = operDownReason
            interface_dict_buffer["operDownReason"] = {}
            interface_dict_buffer["operDownReason"]["type"] = "Property"
            interface_dict_buffer["operDownReason"]["value"] = element_text
            interface_dict_buffer["operDownReason"]["observedAt"] = observed_at
        lastChange = interface.get("last-change")
        if lastChange is not None:
            element_text = lastChange
            interface_dict_buffer["lastChange"] = {}
            interface_dict_buffer["lastChange"]["type"] = "Property"
            interface_dict_buffer["lastChange"]["value"] = element_text
            interface_dict_buffer["lastChange"]["observedAt"] = observed_at
        linecard = interface.get("linecard")
        if linecard is not None:
            element_text = linecard
            interface_dict_buffer["linecard"] = {}
            interface_dict_buffer["linecard"]["type"] = "Relationship"
            interface_dict_buffer["linecard"]["object"] = "urn:ngsi-ld:Linecard:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
            interface_dict_buffer["linecard"]["observedAt"] = observed_at
        forwardingComplex = interface.get("forwarding-complex")
        if forwardingComplex is not None:
            element_text = forwardingComplex
            interface_dict_buffer["forwardingComplex"] = {}
            interface_dict_buffer["forwardingComplex"]["type"] = "Relationship"
            interface_dict_buffer["forwardingComplex"]["object"] = "urn:ngsi-ld:ForwardingComplex:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
            interface_dict_buffer["forwardingComplex"]["observedAt"] = observed_at
        phyGroupMembers = interface.get("phy-group-members")
        if phyGroupMembers is not None:
            element_text = phyGroupMembers
            interface_dict_buffer["phyGroupMembers"] = {}
            interface_dict_buffer["phyGroupMembers"]["type"] = "Property"
            interface_dict_buffer["phyGroupMembers"]["value"] = element_text
            interface_dict_buffer["phyGroupMembers"]["observedAt"] = observed_at
        statistics = interface.get("statistics")
        if statistics is not None and len(statistics) != 0:
            interface_statistics_dict_buffer = {}
            interface_statistics_dict_buffer["id"] = "urn:ngsi-ld:InterfaceStatistics:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
            interface_statistics_dict_buffer["type"] = "InterfaceStatistics"
            interface_statistics_dict_buffer["isPartOf"] = {}
            interface_statistics_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_statistics_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
            interface_statistics_dict_buffer["isPartOf"]["observedAt"] = observed_at
            inPackets = statistics.get("in-packets")
            if inPackets is not None:
                element_text = inPackets
                interface_statistics_dict_buffer["inPackets"] = {}
                interface_statistics_dict_buffer["inPackets"]["type"] = "Property"
                interface_statistics_dict_buffer["inPackets"]["value"] = int(element_text)
                interface_statistics_dict_buffer["inPackets"]["observedAt"] = observed_at
            inOctets = statistics.get("in-octets")
            if inOctets is not None:
                element_text = inOctets
                interface_statistics_dict_buffer["inOctets"] = {}
                interface_statistics_dict_buffer["inOctets"]["type"] = "Property"
                interface_statistics_dict_buffer["inOctets"]["value"] = int(element_text)
                interface_statistics_dict_buffer["inOctets"]["observedAt"] = observed_at
            inUnicastPackets = statistics.get("in-unicast-packets")
            if inUnicastPackets is not None:
                element_text = inUnicastPackets
                interface_statistics_dict_buffer["inUnicastPackets"] = {}
                interface_statistics_dict_buffer["inUnicastPackets"]["type"] = "Property"
                interface_statistics_dict_buffer["inUnicastPackets"]["value"] = int(element_text)
                interface_statistics_dict_buffer["inUnicastPackets"]["observedAt"] = observed_at
            inBroadcastPackets = statistics.get("in-broadcast-packets")
            if inBroadcastPackets is not None:
                element_text = inBroadcastPackets
                interface_statistics_dict_buffer["inBroadcastPackets"] = {}
                interface_statistics_dict_buffer["inBroadcastPackets"]["type"] = "Property"
                interface_statistics_dict_buffer["inBroadcastPackets"]["value"] = int(element_text)
                interface_statistics_dict_buffer["inBroadcastPackets"]["observedAt"] = observed_at
            inMulticastPackets = statistics.get("in-multicast-packets")
            if inMulticastPackets is not None:
                element_text = inMulticastPackets
                interface_statistics_dict_buffer["inMulticastPackets"] = {}
                interface_statistics_dict_buffer["inMulticastPackets"]["type"] = "Property"
                interface_statistics_dict_buffer["inMulticastPackets"]["value"] = int(element_text)
                interface_statistics_dict_buffer["inMulticastPackets"]["observedAt"] = observed_at
            inDiscardedPackets = statistics.get("in-discarded-packets")
            if inDiscardedPackets is not None:
                element_text = inDiscardedPackets
                interface_statistics_dict_buffer["inDiscardedPackets"] = {}
                interface_statistics_dict_buffer["inDiscardedPackets"]["type"] = "Property"
                interface_statistics_dict_buffer["inDiscardedPackets"]["value"] = int(element_text)
                interface_statistics_dict_buffer["inDiscardedPackets"]["observedAt"] = observed_at
            inErrorPackets = statistics.get("in-error-packets")
            if inErrorPackets is not None:
                element_text = inErrorPackets
                interface_statistics_dict_buffer["inErrorPackets"] = {}
                interface_statistics_dict_buffer["inErrorPackets"]["type"] = "Property"
                interface_statistics_dict_buffer["inErrorPackets"]["value"] = int(element_text)
                interface_statistics_dict_buffer["inErrorPackets"]["observedAt"] = observed_at
            inFcsErrorPackets = statistics.get("in-fcs-error-packets")
            if inFcsErrorPackets is not None:
                element_text = inFcsErrorPackets
                interface_statistics_dict_buffer["inFcsErrorPackets"] = {}
                interface_statistics_dict_buffer["inFcsErrorPackets"]["type"] = "Property"
                interface_statistics_dict_buffer["inFcsErrorPackets"]["value"] = int(element_text)
                interface_statistics_dict_buffer["inFcsErrorPackets"]["observedAt"] = observed_at
            outPackets = statistics.get("out-packets")
            if outPackets is not None:
                element_text = outPackets
                interface_statistics_dict_buffer["outPackets"] = {}
                interface_statistics_dict_buffer["outPackets"]["type"] = "Property"
                interface_statistics_dict_buffer["outPackets"]["value"] = int(element_text)
                interface_statistics_dict_buffer["outPackets"]["observedAt"] = observed_at
            outOctets = statistics.get("out-octets")
            if outOctets is not None:
                element_text = outOctets
                interface_statistics_dict_buffer["outOctets"] = {}
                interface_statistics_dict_buffer["outOctets"]["type"] = "Property"
                interface_statistics_dict_buffer["outOctets"]["value"] = int(element_text)
                interface_statistics_dict_buffer["outOctets"]["observedAt"] = observed_at
            outMirrorOctets = statistics.get("out-mirror-octets")
            if outMirrorOctets is not None:
                element_text = outMirrorOctets
                interface_statistics_dict_buffer["outMirrorOctets"] = {}
                interface_statistics_dict_buffer["outMirrorOctets"]["type"] = "Property"
                interface_statistics_dict_buffer["outMirrorOctets"]["value"] = int(element_text)
                interface_statistics_dict_buffer["outMirrorOctets"]["observedAt"] = observed_at
            outUnicastPackets = statistics.get("out-unicast-packets")
            if outUnicastPackets is not None:
                element_text = outUnicastPackets
                interface_statistics_dict_buffer["outUnicastPackets"] = {}
                interface_statistics_dict_buffer["outUnicastPackets"]["type"] = "Property"
                interface_statistics_dict_buffer["outUnicastPackets"]["value"] = int(element_text)
                interface_statistics_dict_buffer["outUnicastPackets"]["observedAt"] = observed_at
            outBroadcastPackets = statistics.get("out-broadcast-packets")
            if outBroadcastPackets is not None:
                element_text = outBroadcastPackets
                interface_statistics_dict_buffer["outBroadcastPackets"] = {}
                interface_statistics_dict_buffer["outBroadcastPackets"]["type"] = "Property"
                interface_statistics_dict_buffer["outBroadcastPackets"]["value"] = int(element_text)
                interface_statistics_dict_buffer["outBroadcastPackets"]["observedAt"] = observed_at
            outMulticastPackets = statistics.get("out-multicast-packets")
            if outMulticastPackets is not None:
                element_text = outMulticastPackets
                interface_statistics_dict_buffer["outMulticastPackets"] = {}
                interface_statistics_dict_buffer["outMulticastPackets"]["type"] = "Property"
                interface_statistics_dict_buffer["outMulticastPackets"]["value"] = int(element_text)
                interface_statistics_dict_buffer["outMulticastPackets"]["observedAt"] = observed_at
            outDiscardedPackets = statistics.get("out-discarded-packets")
            if outDiscardedPackets is not None:
                element_text = outDiscardedPackets
                interface_statistics_dict_buffer["outDiscardedPackets"] = {}
                interface_statistics_dict_buffer["outDiscardedPackets"]["type"] = "Property"
                interface_statistics_dict_buffer["outDiscardedPackets"]["value"] = int(element_text)
                interface_statistics_dict_buffer["outDiscardedPackets"]["observedAt"] = observed_at
            outErrorPackets = statistics.get("out-error-packets")
            if outErrorPackets is not None:
                element_text = outErrorPackets
                interface_statistics_dict_buffer["outErrorPackets"] = {}
                interface_statistics_dict_buffer["outErrorPackets"]["type"] = "Property"
                interface_statistics_dict_buffer["outErrorPackets"]["value"] = int(element_text)
                interface_statistics_dict_buffer["outErrorPackets"]["observedAt"] = observed_at
            outMirrorPackets = statistics.get("out-mirror-packets")
            if outMirrorPackets is not None:
                element_text = outMirrorPackets
                interface_statistics_dict_buffer["outMirrorPackets"] = {}
                interface_statistics_dict_buffer["outMirrorPackets"]["type"] = "Property"
                interface_statistics_dict_buffer["outMirrorPackets"]["value"] = int(element_text)
                interface_statistics_dict_buffer["outMirrorPackets"]["observedAt"] = observed_at
            carrierTransitions = statistics.get("carrier-transitions")
            if carrierTransitions is not None:
                element_text = carrierTransitions
                interface_statistics_dict_buffer["carrierTransitions"] = {}
                interface_statistics_dict_buffer["carrierTransitions"]["type"] = "Property"
                interface_statistics_dict_buffer["carrierTransitions"]["value"] = int(element_text)
                interface_statistics_dict_buffer["carrierTransitions"]["observedAt"] = observed_at
            lastClear = statistics.get("last-clear")
            if lastClear is not None:
                element_text = lastClear
                interface_statistics_dict_buffer["lastClear"] = {}
                interface_statistics_dict_buffer["lastClear"]["type"] = "Property"
                interface_statistics_dict_buffer["lastClear"]["value"] = element_text
                interface_statistics_dict_buffer["lastClear"]["observedAt"] = observed_at
            dict_buffers.append(interface_statistics_dict_buffer)
        traffic_rate = interface.get("traffic-rate")
        if traffic_rate is not None and len(traffic_rate) != 0:
            interface_traffic_rate_dict_buffer = {}
            interface_traffic_rate_dict_buffer["id"] = "urn:ngsi-ld:InterfaceTrafficRate:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
            interface_traffic_rate_dict_buffer["type"] = "InterfaceTrafficRate"
            interface_traffic_rate_dict_buffer["isPartOf"] = {}
            interface_traffic_rate_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_traffic_rate_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
            interface_traffic_rate_dict_buffer["isPartOf"]["observedAt"] = observed_at
            inBps = traffic_rate.get("in-bps")
            if inBps is not None:
                element_text = inBps
                interface_traffic_rate_dict_buffer["inBps"] = {}
                interface_traffic_rate_dict_buffer["inBps"]["type"] = "Property"
                interface_traffic_rate_dict_buffer["inBps"]["value"] = int(element_text)
                interface_traffic_rate_dict_buffer["inBps"]["observedAt"] = observed_at
            outBps = traffic_rate.get("out-bps")
            if outBps is not None:
                element_text = outBps
                interface_traffic_rate_dict_buffer["outBps"] = {}
                interface_traffic_rate_dict_buffer["outBps"]["type"] = "Property"
                interface_traffic_rate_dict_buffer["outBps"]["value"] = int(element_text)
                interface_traffic_rate_dict_buffer["outBps"]["observedAt"] = observed_at
            dict_buffers.append(interface_traffic_rate_dict_buffer)
        adapter = interface.get("adapter")
        if adapter is not None and len(adapter) != 0:
            interface_adapter_dict_buffer = {}
            interface_adapter_dict_buffer["id"] = "urn:ngsi-ld:InterfaceAdapter:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
            interface_adapter_dict_buffer["type"] = "InterfaceAdapter"
            interface_adapter_dict_buffer["isPartOf"] = {}
            interface_adapter_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_adapter_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
            interface_adapter_dict_buffer["isPartOf"]["observedAt"] = observed_at
            modelNumber = adapter.get("model-number")
            if modelNumber is not None:
                element_text = modelNumber
                interface_adapter_dict_buffer["modelNumber"] = {}
                interface_adapter_dict_buffer["modelNumber"]["type"] = "Property"
                interface_adapter_dict_buffer["modelNumber"]["value"] = element_text
                interface_adapter_dict_buffer["modelNumber"]["observedAt"] = observed_at
            type = adapter.get("type")
            if type is not None:
                element_text = type
                interface_adapter_dict_buffer["type"] = {}
                interface_adapter_dict_buffer["type"]["type"] = "Property"
                interface_adapter_dict_buffer["type"]["value"] = element_text
                interface_adapter_dict_buffer["type"]["observedAt"] = observed_at
            vendorManufactureDate = adapter.get("vendor-manufacture-date")
            if vendorManufactureDate is not None:
                element_text = vendorManufactureDate
                interface_adapter_dict_buffer["vendorManufactureDate"] = {}
                interface_adapter_dict_buffer["vendorManufactureDate"]["type"] = "Property"
                interface_adapter_dict_buffer["vendorManufactureDate"]["value"] = element_text
                interface_adapter_dict_buffer["vendorManufactureDate"]["observedAt"] = observed_at
            vendorOui = adapter.get("vendor-oui")
            if vendorOui is not None:
                element_text = vendorOui
                interface_adapter_dict_buffer["vendorOui"] = {}
                interface_adapter_dict_buffer["vendorOui"]["type"] = "Property"
                interface_adapter_dict_buffer["vendorOui"]["value"] = element_text
                interface_adapter_dict_buffer["vendorOui"]["observedAt"] = observed_at
            vendorPartNumber = adapter.get("vendor-part-number")
            if vendorPartNumber is not None:
                element_text = vendorPartNumber
                interface_adapter_dict_buffer["vendorPartNumber"] = {}
                interface_adapter_dict_buffer["vendorPartNumber"]["type"] = "Property"
                interface_adapter_dict_buffer["vendorPartNumber"]["value"] = element_text
                interface_adapter_dict_buffer["vendorPartNumber"]["observedAt"] = observed_at
            vendorSerialNumber = adapter.get("vendor-serial-number")
            if vendorSerialNumber is not None:
                element_text = vendorSerialNumber
                interface_adapter_dict_buffer["vendorSerialNumber"] = {}
                interface_adapter_dict_buffer["vendorSerialNumber"]["type"] = "Property"
                interface_adapter_dict_buffer["vendorSerialNumber"]["value"] = element_text
                interface_adapter_dict_buffer["vendorSerialNumber"]["observedAt"] = observed_at
            dict_buffers.append(interface_adapter_dict_buffer)
        transceiver = interface.get("transceiver")
        if transceiver is not None and len(transceiver) != 0:
            interface_transceiver_dict_buffer = {}
            interface_transceiver_dict_buffer["id"] = "urn:ngsi-ld:InterfaceTransceiver:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
            interface_transceiver_dict_buffer["type"] = "InterfaceTransceiver"
            interface_transceiver_dict_buffer["isPartOf"] = {}
            interface_transceiver_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_transceiver_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
            interface_transceiver_dict_buffer["isPartOf"]["observedAt"] = observed_at
            txLaser = transceiver.get("tx-laser")
            if txLaser is not None:
                element_text = txLaser
                interface_transceiver_dict_buffer["txLaser"] = {}
                interface_transceiver_dict_buffer["txLaser"]["type"] = "Property"
                interface_transceiver_dict_buffer["txLaser"]["value"] = eval(str(element_text).capitalize())
                interface_transceiver_dict_buffer["txLaser"]["observedAt"] = observed_at
            operState = transceiver.get("oper-state")
            if operState is not None:
                element_text = operState
                interface_transceiver_dict_buffer["operState"] = {}
                interface_transceiver_dict_buffer["operState"]["type"] = "Property"
                interface_transceiver_dict_buffer["operState"]["value"] = element_text
                interface_transceiver_dict_buffer["operState"]["observedAt"] = observed_at
            operDownReason = transceiver.get("oper-down-reason")
            if operDownReason is not None:
                element_text = operDownReason
                interface_transceiver_dict_buffer["operDownReason"] = {}
                interface_transceiver_dict_buffer["operDownReason"]["type"] = "Property"
                interface_transceiver_dict_buffer["operDownReason"]["value"] = element_text
                interface_transceiver_dict_buffer["operDownReason"]["observedAt"] = observed_at
            ddmEvents = transceiver.get("ddm-events")
            if ddmEvents is not None:
                element_text = ddmEvents
                interface_transceiver_dict_buffer["ddmEvents"] = {}
                interface_transceiver_dict_buffer["ddmEvents"]["type"] = "Property"
                interface_transceiver_dict_buffer["ddmEvents"]["value"] = eval(str(element_text).capitalize())
                interface_transceiver_dict_buffer["ddmEvents"]["observedAt"] = observed_at
            forwardErrorCorrection = transceiver.get("forward-error-correction")
            if forwardErrorCorrection is not None:
                element_text = forwardErrorCorrection
                interface_transceiver_dict_buffer["forwardErrorCorrection"] = {}
                interface_transceiver_dict_buffer["forwardErrorCorrection"]["type"] = "Property"
                interface_transceiver_dict_buffer["forwardErrorCorrection"]["value"] = element_text
                interface_transceiver_dict_buffer["forwardErrorCorrection"]["observedAt"] = observed_at
            formFactor = transceiver.get("form-factor")
            if formFactor is not None:
                element_text = formFactor
                interface_transceiver_dict_buffer["formFactor"] = {}
                interface_transceiver_dict_buffer["formFactor"]["type"] = "Property"
                interface_transceiver_dict_buffer["formFactor"]["value"] = element_text
                interface_transceiver_dict_buffer["formFactor"]["observedAt"] = observed_at
            functionalType = transceiver.get("functional-type")
            if functionalType is not None and len(functionalType) != 0:
                element_text = functionalType
                if element_text is not None:
                    interface_transceiver_dict_buffer["functionalType"] = {}
                    interface_transceiver_dict_buffer["functionalType"]["type"] = "Relationship"
                    interface_transceiver_dict_buffer["functionalType"]["object"] = "urn:ngsi-ld:YANGIdentity:" + element_text
                    interface_transceiver_dict_buffer["functionalType"]["observedAt"] = observed_at
            ethernetPmd = transceiver.get("ethernet-pmd")
            if ethernetPmd is not None:
                element_text = ethernetPmd
                interface_transceiver_dict_buffer["ethernetPmd"] = {}
                interface_transceiver_dict_buffer["ethernetPmd"]["type"] = "Property"
                interface_transceiver_dict_buffer["ethernetPmd"]["value"] = element_text
                interface_transceiver_dict_buffer["ethernetPmd"]["observedAt"] = observed_at
            connectorType = transceiver.get("connector-type")
            if connectorType is not None:
                element_text = connectorType
                interface_transceiver_dict_buffer["connectorType"] = {}
                interface_transceiver_dict_buffer["connectorType"]["type"] = "Property"
                interface_transceiver_dict_buffer["connectorType"]["value"] = element_text
                interface_transceiver_dict_buffer["connectorType"]["observedAt"] = observed_at
            vendor = transceiver.get("vendor")
            if vendor is not None:
                element_text = vendor
                interface_transceiver_dict_buffer["vendor"] = {}
                interface_transceiver_dict_buffer["vendor"]["type"] = "Property"
                interface_transceiver_dict_buffer["vendor"]["value"] = element_text
                interface_transceiver_dict_buffer["vendor"]["observedAt"] = observed_at
            vendorPartNumber = transceiver.get("vendor-part-number")
            if vendorPartNumber is not None:
                element_text = vendorPartNumber
                interface_transceiver_dict_buffer["vendorPartNumber"] = {}
                interface_transceiver_dict_buffer["vendorPartNumber"]["type"] = "Property"
                interface_transceiver_dict_buffer["vendorPartNumber"]["value"] = element_text
                interface_transceiver_dict_buffer["vendorPartNumber"]["observedAt"] = observed_at
            vendorRevision = transceiver.get("vendor-revision")
            if vendorRevision is not None:
                element_text = vendorRevision
                interface_transceiver_dict_buffer["vendorRevision"] = {}
                interface_transceiver_dict_buffer["vendorRevision"]["type"] = "Property"
                interface_transceiver_dict_buffer["vendorRevision"]["value"] = element_text
                interface_transceiver_dict_buffer["vendorRevision"]["observedAt"] = observed_at
            vendorLotNumber = transceiver.get("vendor-lot-number")
            if vendorLotNumber is not None:
                element_text = vendorLotNumber
                interface_transceiver_dict_buffer["vendorLotNumber"] = {}
                interface_transceiver_dict_buffer["vendorLotNumber"]["type"] = "Property"
                interface_transceiver_dict_buffer["vendorLotNumber"]["value"] = element_text
                interface_transceiver_dict_buffer["vendorLotNumber"]["observedAt"] = observed_at
            serialNumber = transceiver.get("serial-number")
            if serialNumber is not None:
                element_text = serialNumber
                interface_transceiver_dict_buffer["serialNumber"] = {}
                interface_transceiver_dict_buffer["serialNumber"]["type"] = "Property"
                interface_transceiver_dict_buffer["serialNumber"]["value"] = element_text
                interface_transceiver_dict_buffer["serialNumber"]["observedAt"] = observed_at
            dateCode = transceiver.get("date-code")
            if dateCode is not None:
                element_text = dateCode
                interface_transceiver_dict_buffer["dateCode"] = {}
                interface_transceiver_dict_buffer["dateCode"]["type"] = "Property"
                interface_transceiver_dict_buffer["dateCode"]["value"] = element_text
                interface_transceiver_dict_buffer["dateCode"]["observedAt"] = observed_at
            faultCondition = transceiver.get("fault-condition")
            if faultCondition is not None:
                element_text = faultCondition
                interface_transceiver_dict_buffer["faultCondition"] = {}
                interface_transceiver_dict_buffer["faultCondition"]["type"] = "Property"
                interface_transceiver_dict_buffer["faultCondition"]["value"] = eval(str(element_text).capitalize())
                interface_transceiver_dict_buffer["faultCondition"]["observedAt"] = observed_at
            wavelength = transceiver.get("wavelength")
            if wavelength is not None:
                element_text = wavelength
                interface_transceiver_dict_buffer["wavelength"] = {}
                interface_transceiver_dict_buffer["wavelength"]["type"] = "Property"
                interface_transceiver_dict_buffer["wavelength"]["value"] = float(element_text)
                interface_transceiver_dict_buffer["wavelength"]["observedAt"] = observed_at
            temperature = transceiver.get("temperature")
            if temperature is not None and len(temperature) != 0:
                interface_transceiver_temperature_dict_buffer = {}
                interface_transceiver_temperature_dict_buffer["id"] = "urn:ngsi-ld:InterfaceTransceiverTemperature:" + ":".join(interface_transceiver_dict_buffer["id"].split(":")[3:])
                interface_transceiver_temperature_dict_buffer["type"] = "InterfaceTransceiverTemperature"
                interface_transceiver_temperature_dict_buffer["isPartOf"] = {}
                interface_transceiver_temperature_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_transceiver_temperature_dict_buffer["isPartOf"]["object"] = interface_transceiver_dict_buffer["id"]
                interface_transceiver_temperature_dict_buffer["isPartOf"]["observedAt"] = observed_at
                latestValue = temperature.get("latest-value")
                if latestValue is not None:
                    element_text = latestValue
                    interface_transceiver_temperature_dict_buffer["latestValue"] = {}
                    interface_transceiver_temperature_dict_buffer["latestValue"]["type"] = "Property"
                    interface_transceiver_temperature_dict_buffer["latestValue"]["value"] = int(element_text)
                    interface_transceiver_temperature_dict_buffer["latestValue"]["observedAt"] = observed_at
                maximum = temperature.get("maximum")
                if maximum is not None:
                    element_text = maximum
                    interface_transceiver_temperature_dict_buffer["maximum"] = {}
                    interface_transceiver_temperature_dict_buffer["maximum"]["type"] = "Property"
                    interface_transceiver_temperature_dict_buffer["maximum"]["value"] = int(element_text)
                    interface_transceiver_temperature_dict_buffer["maximum"]["observedAt"] = observed_at
                maximumTime = temperature.get("maximum-time")
                if maximumTime is not None:
                    element_text = maximumTime
                    interface_transceiver_temperature_dict_buffer["maximumTime"] = {}
                    interface_transceiver_temperature_dict_buffer["maximumTime"]["type"] = "Property"
                    interface_transceiver_temperature_dict_buffer["maximumTime"]["value"] = element_text
                    interface_transceiver_temperature_dict_buffer["maximumTime"]["observedAt"] = observed_at
                highAlarmCondition = temperature.get("high-alarm-condition")
                if highAlarmCondition is not None:
                    element_text = highAlarmCondition
                    interface_transceiver_temperature_dict_buffer["highAlarmCondition"] = {}
                    interface_transceiver_temperature_dict_buffer["highAlarmCondition"]["type"] = "Property"
                    interface_transceiver_temperature_dict_buffer["highAlarmCondition"]["value"] = eval(str(element_text).capitalize())
                    interface_transceiver_temperature_dict_buffer["highAlarmCondition"]["observedAt"] = observed_at
                highAlarmThreshold = temperature.get("high-alarm-threshold")
                if highAlarmThreshold is not None:
                    element_text = highAlarmThreshold
                    interface_transceiver_temperature_dict_buffer["highAlarmThreshold"] = {}
                    interface_transceiver_temperature_dict_buffer["highAlarmThreshold"]["type"] = "Property"
                    interface_transceiver_temperature_dict_buffer["highAlarmThreshold"]["value"] = int(element_text)
                    interface_transceiver_temperature_dict_buffer["highAlarmThreshold"]["observedAt"] = observed_at
                lowAlarmCondition = temperature.get("low-alarm-condition")
                if lowAlarmCondition is not None:
                    element_text = lowAlarmCondition
                    interface_transceiver_temperature_dict_buffer["lowAlarmCondition"] = {}
                    interface_transceiver_temperature_dict_buffer["lowAlarmCondition"]["type"] = "Property"
                    interface_transceiver_temperature_dict_buffer["lowAlarmCondition"]["value"] = eval(str(element_text).capitalize())
                    interface_transceiver_temperature_dict_buffer["lowAlarmCondition"]["observedAt"] = observed_at
                lowAlarmThreshold = temperature.get("low-alarm-threshold")
                if lowAlarmThreshold is not None:
                    element_text = lowAlarmThreshold
                    interface_transceiver_temperature_dict_buffer["lowAlarmThreshold"] = {}
                    interface_transceiver_temperature_dict_buffer["lowAlarmThreshold"]["type"] = "Property"
                    interface_transceiver_temperature_dict_buffer["lowAlarmThreshold"]["value"] = int(element_text)
                    interface_transceiver_temperature_dict_buffer["lowAlarmThreshold"]["observedAt"] = observed_at
                highWarningCondition = temperature.get("high-warning-condition")
                if highWarningCondition is not None:
                    element_text = highWarningCondition
                    interface_transceiver_temperature_dict_buffer["highWarningCondition"] = {}
                    interface_transceiver_temperature_dict_buffer["highWarningCondition"]["type"] = "Property"
                    interface_transceiver_temperature_dict_buffer["highWarningCondition"]["value"] = eval(str(element_text).capitalize())
                    interface_transceiver_temperature_dict_buffer["highWarningCondition"]["observedAt"] = observed_at
                highWarningThreshold = temperature.get("high-warning-threshold")
                if highWarningThreshold is not None:
                    element_text = highWarningThreshold
                    interface_transceiver_temperature_dict_buffer["highWarningThreshold"] = {}
                    interface_transceiver_temperature_dict_buffer["highWarningThreshold"]["type"] = "Property"
                    interface_transceiver_temperature_dict_buffer["highWarningThreshold"]["value"] = int(element_text)
                    interface_transceiver_temperature_dict_buffer["highWarningThreshold"]["observedAt"] = observed_at
                lowWarningCondition = temperature.get("low-warning-condition")
                if lowWarningCondition is not None:
                    element_text = lowWarningCondition
                    interface_transceiver_temperature_dict_buffer["lowWarningCondition"] = {}
                    interface_transceiver_temperature_dict_buffer["lowWarningCondition"]["type"] = "Property"
                    interface_transceiver_temperature_dict_buffer["lowWarningCondition"]["value"] = eval(str(element_text).capitalize())
                    interface_transceiver_temperature_dict_buffer["lowWarningCondition"]["observedAt"] = observed_at
                lowWarningThreshold = temperature.get("low-warning-threshold")
                if lowWarningThreshold is not None:
                    element_text = lowWarningThreshold
                    interface_transceiver_temperature_dict_buffer["lowWarningThreshold"] = {}
                    interface_transceiver_temperature_dict_buffer["lowWarningThreshold"]["type"] = "Property"
                    interface_transceiver_temperature_dict_buffer["lowWarningThreshold"]["value"] = int(element_text)
                    interface_transceiver_temperature_dict_buffer["lowWarningThreshold"]["observedAt"] = observed_at
                dict_buffers.append(interface_transceiver_temperature_dict_buffer)
            voltage = transceiver.get("voltage")
            if voltage is not None and len(voltage) != 0:
                interface_transceiver_voltage_dict_buffer = {}
                interface_transceiver_voltage_dict_buffer["id"] = "urn:ngsi-ld:InterfaceTransceiverVoltage:" + ":".join(interface_transceiver_dict_buffer["id"].split(":")[3:])
                interface_transceiver_voltage_dict_buffer["type"] = "InterfaceTransceiverVoltage"
                interface_transceiver_voltage_dict_buffer["isPartOf"] = {}
                interface_transceiver_voltage_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_transceiver_voltage_dict_buffer["isPartOf"]["object"] = interface_transceiver_dict_buffer["id"]
                interface_transceiver_voltage_dict_buffer["isPartOf"]["observedAt"] = observed_at
                latestValue = voltage.get("latest-value")
                if latestValue is not None:
                    element_text = latestValue
                    interface_transceiver_voltage_dict_buffer["latestValue"] = {}
                    interface_transceiver_voltage_dict_buffer["latestValue"]["type"] = "Property"
                    interface_transceiver_voltage_dict_buffer["latestValue"]["value"] = float(element_text)
                    interface_transceiver_voltage_dict_buffer["latestValue"]["observedAt"] = observed_at
                highAlarmCondition = voltage.get("high-alarm-condition")
                if highAlarmCondition is not None:
                    element_text = highAlarmCondition
                    interface_transceiver_voltage_dict_buffer["highAlarmCondition"] = {}
                    interface_transceiver_voltage_dict_buffer["highAlarmCondition"]["type"] = "Property"
                    interface_transceiver_voltage_dict_buffer["highAlarmCondition"]["value"] = eval(str(element_text).capitalize())
                    interface_transceiver_voltage_dict_buffer["highAlarmCondition"]["observedAt"] = observed_at
                highAlarmThreshold = voltage.get("high-alarm-threshold")
                if highAlarmThreshold is not None:
                    element_text = highAlarmThreshold
                    interface_transceiver_voltage_dict_buffer["highAlarmThreshold"] = {}
                    interface_transceiver_voltage_dict_buffer["highAlarmThreshold"]["type"] = "Property"
                    interface_transceiver_voltage_dict_buffer["highAlarmThreshold"]["value"] = float(element_text)
                    interface_transceiver_voltage_dict_buffer["highAlarmThreshold"]["observedAt"] = observed_at
                lowAlarmCondition = voltage.get("low-alarm-condition")
                if lowAlarmCondition is not None:
                    element_text = lowAlarmCondition
                    interface_transceiver_voltage_dict_buffer["lowAlarmCondition"] = {}
                    interface_transceiver_voltage_dict_buffer["lowAlarmCondition"]["type"] = "Property"
                    interface_transceiver_voltage_dict_buffer["lowAlarmCondition"]["value"] = eval(str(element_text).capitalize())
                    interface_transceiver_voltage_dict_buffer["lowAlarmCondition"]["observedAt"] = observed_at
                lowAlarmThreshold = voltage.get("low-alarm-threshold")
                if lowAlarmThreshold is not None:
                    element_text = lowAlarmThreshold
                    interface_transceiver_voltage_dict_buffer["lowAlarmThreshold"] = {}
                    interface_transceiver_voltage_dict_buffer["lowAlarmThreshold"]["type"] = "Property"
                    interface_transceiver_voltage_dict_buffer["lowAlarmThreshold"]["value"] = float(element_text)
                    interface_transceiver_voltage_dict_buffer["lowAlarmThreshold"]["observedAt"] = observed_at
                highWarningCondition = voltage.get("high-warning-condition")
                if highWarningCondition is not None:
                    element_text = highWarningCondition
                    interface_transceiver_voltage_dict_buffer["highWarningCondition"] = {}
                    interface_transceiver_voltage_dict_buffer["highWarningCondition"]["type"] = "Property"
                    interface_transceiver_voltage_dict_buffer["highWarningCondition"]["value"] = eval(str(element_text).capitalize())
                    interface_transceiver_voltage_dict_buffer["highWarningCondition"]["observedAt"] = observed_at
                highWarningThreshold = voltage.get("high-warning-threshold")
                if highWarningThreshold is not None:
                    element_text = highWarningThreshold
                    interface_transceiver_voltage_dict_buffer["highWarningThreshold"] = {}
                    interface_transceiver_voltage_dict_buffer["highWarningThreshold"]["type"] = "Property"
                    interface_transceiver_voltage_dict_buffer["highWarningThreshold"]["value"] = float(element_text)
                    interface_transceiver_voltage_dict_buffer["highWarningThreshold"]["observedAt"] = observed_at
                lowWarningCondition = voltage.get("low-warning-condition")
                if lowWarningCondition is not None:
                    element_text = lowWarningCondition
                    interface_transceiver_voltage_dict_buffer["lowWarningCondition"] = {}
                    interface_transceiver_voltage_dict_buffer["lowWarningCondition"]["type"] = "Property"
                    interface_transceiver_voltage_dict_buffer["lowWarningCondition"]["value"] = eval(str(element_text).capitalize())
                    interface_transceiver_voltage_dict_buffer["lowWarningCondition"]["observedAt"] = observed_at
                lowWarningThreshold = voltage.get("low-warning-threshold")
                if lowWarningThreshold is not None:
                    element_text = lowWarningThreshold
                    interface_transceiver_voltage_dict_buffer["lowWarningThreshold"] = {}
                    interface_transceiver_voltage_dict_buffer["lowWarningThreshold"]["type"] = "Property"
                    interface_transceiver_voltage_dict_buffer["lowWarningThreshold"]["value"] = float(element_text)
                    interface_transceiver_voltage_dict_buffer["lowWarningThreshold"]["observedAt"] = observed_at
                dict_buffers.append(interface_transceiver_voltage_dict_buffer)
            transceiver_channel = transceiver.get("channel")
            if transceiver_channel is not None and len(transceiver_channel) != 0:
                for channel in transceiver_channel:
                    interface_transceiver_channel_dict_buffer = {}
                    interface_transceiver_channel_dict_buffer["id"] = "urn:ngsi-ld:InterfaceTransceiverChannel:" + ":".join(interface_transceiver_dict_buffer["id"].split(":")[3:])
                    interface_transceiver_channel_dict_buffer["type"] = "InterfaceTransceiverChannel"
                    interface_transceiver_channel_dict_buffer["isPartOf"] = {}
                    interface_transceiver_channel_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_transceiver_channel_dict_buffer["isPartOf"]["object"] = interface_transceiver_dict_buffer["id"]
                    interface_transceiver_channel_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    index = channel.get("index")
                    if index is not None:
                        element_text = index
                        if "." + str(element_text) not in interface_transceiver_channel_dict_buffer["id"].split(":")[-1]:
                            interface_transceiver_channel_dict_buffer["id"] = interface_transceiver_channel_dict_buffer["id"] + "." + str(element_text)
                        interface_transceiver_channel_dict_buffer["index"] = {}
                        interface_transceiver_channel_dict_buffer["index"]["type"] = "Property"
                        interface_transceiver_channel_dict_buffer["index"]["value"] = int(element_text)
                        interface_transceiver_channel_dict_buffer["index"]["observedAt"] = observed_at
                    wavelength = channel.get("wavelength")
                    if wavelength is not None:
                        element_text = wavelength
                        interface_transceiver_channel_dict_buffer["wavelength"] = {}
                        interface_transceiver_channel_dict_buffer["wavelength"]["type"] = "Property"
                        interface_transceiver_channel_dict_buffer["wavelength"]["value"] = float(element_text)
                        interface_transceiver_channel_dict_buffer["wavelength"]["observedAt"] = observed_at
                    dict_buffers.append(interface_transceiver_channel_dict_buffer)
            dict_buffers.append(interface_transceiver_dict_buffer)
        ethernet = interface.get("ethernet")
        if ethernet is not None and len(ethernet) != 0:
            interface_ethernet_dict_buffer = {}
            interface_ethernet_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernet:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
            interface_ethernet_dict_buffer["type"] = "InterfaceEthernet"
            interface_ethernet_dict_buffer["isPartOf"] = {}
            interface_ethernet_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_ethernet_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
            interface_ethernet_dict_buffer["isPartOf"]["observedAt"] = observed_at
            aggregateId = ethernet.get("aggregate-id")
            if aggregateId is not None:
                element_text = aggregateId
                if interface_ethernet_dict_buffer["id"].split(":")[-1] != element_text:
                    interface_ethernet_dict_buffer["id"] = interface_ethernet_dict_buffer["id"] + ":" + element_text
                interface_ethernet_dict_buffer["aggregateId"] = {}
                interface_ethernet_dict_buffer["aggregateId"]["type"] = "Relationship"
                interface_ethernet_dict_buffer["aggregateId"]["object"] = "urn:ngsi-ld:Interface:" + ":".join(interface_ethernet_dict_buffer["id"].split(":")[3:])
                interface_ethernet_dict_buffer["aggregateId"]["observedAt"] = observed_at
            forwardingViable = ethernet.get("forwarding-viable")
            if forwardingViable is not None:
                element_text = forwardingViable
                interface_ethernet_dict_buffer["forwardingViable"] = {}
                interface_ethernet_dict_buffer["forwardingViable"]["type"] = "Property"
                interface_ethernet_dict_buffer["forwardingViable"]["value"] = eval(str(element_text).capitalize())
                interface_ethernet_dict_buffer["forwardingViable"]["observedAt"] = observed_at
            autoNegotiate = ethernet.get("auto-negotiate")
            if autoNegotiate is not None:
                element_text = autoNegotiate
                interface_ethernet_dict_buffer["autoNegotiate"] = {}
                interface_ethernet_dict_buffer["autoNegotiate"]["type"] = "Property"
                interface_ethernet_dict_buffer["autoNegotiate"]["value"] = eval(str(element_text).capitalize())
                interface_ethernet_dict_buffer["autoNegotiate"]["observedAt"] = observed_at
            duplexMode = ethernet.get("duplex-mode")
            if duplexMode is not None:
                element_text = duplexMode
                interface_ethernet_dict_buffer["duplexMode"] = {}
                interface_ethernet_dict_buffer["duplexMode"]["type"] = "Property"
                interface_ethernet_dict_buffer["duplexMode"]["value"] = element_text
                interface_ethernet_dict_buffer["duplexMode"]["observedAt"] = observed_at
            dacLinkTraining = ethernet.get("dac-link-training")
            if dacLinkTraining is not None:
                element_text = dacLinkTraining
                interface_ethernet_dict_buffer["dacLinkTraining"] = {}
                interface_ethernet_dict_buffer["dacLinkTraining"]["type"] = "Property"
                interface_ethernet_dict_buffer["dacLinkTraining"]["value"] = eval(str(element_text).capitalize())
                interface_ethernet_dict_buffer["dacLinkTraining"]["observedAt"] = observed_at
            flow_control = ethernet.get("flow-control")
            if flow_control is not None and len(flow_control) != 0:
                interface_ethernet_flow_control_dict_buffer = {}
                interface_ethernet_flow_control_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetFlowControl:" + ":".join(interface_ethernet_dict_buffer["id"].split(":")[3:])
                interface_ethernet_flow_control_dict_buffer["type"] = "InterfaceEthernetFlowControl"
                interface_ethernet_flow_control_dict_buffer["isPartOf"] = {}
                interface_ethernet_flow_control_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_ethernet_flow_control_dict_buffer["isPartOf"]["object"] = interface_ethernet_dict_buffer["id"]
                interface_ethernet_flow_control_dict_buffer["isPartOf"]["observedAt"] = observed_at
                receive = flow_control.get("receive")
                if receive is not None:
                    element_text = receive
                    interface_ethernet_flow_control_dict_buffer["receive"] = {}
                    interface_ethernet_flow_control_dict_buffer["receive"]["type"] = "Property"
                    interface_ethernet_flow_control_dict_buffer["receive"]["value"] = eval(str(element_text).capitalize())
                    interface_ethernet_flow_control_dict_buffer["receive"]["observedAt"] = observed_at
                transmit = flow_control.get("transmit")
                if transmit is not None:
                    element_text = transmit
                    interface_ethernet_flow_control_dict_buffer["transmit"] = {}
                    interface_ethernet_flow_control_dict_buffer["transmit"]["type"] = "Property"
                    interface_ethernet_flow_control_dict_buffer["transmit"]["value"] = eval(str(element_text).capitalize())
                    interface_ethernet_flow_control_dict_buffer["transmit"]["observedAt"] = observed_at
                dict_buffers.append(interface_ethernet_flow_control_dict_buffer)
            lacpPortPriority = ethernet.get("lacp-port-priority")
            if lacpPortPriority is not None:
                element_text = lacpPortPriority
                interface_ethernet_dict_buffer["lacpPortPriority"] = {}
                interface_ethernet_dict_buffer["lacpPortPriority"]["type"] = "Property"
                interface_ethernet_dict_buffer["lacpPortPriority"]["value"] = int(element_text)
                interface_ethernet_dict_buffer["lacpPortPriority"]["observedAt"] = observed_at
            portSpeed = ethernet.get("port-speed")
            if portSpeed is not None:
                element_text = portSpeed
                interface_ethernet_dict_buffer["portSpeed"] = {}
                interface_ethernet_dict_buffer["portSpeed"]["type"] = "Property"
                interface_ethernet_dict_buffer["portSpeed"]["value"] = element_text
                interface_ethernet_dict_buffer["portSpeed"]["observedAt"] = observed_at
            hwMacAddress = ethernet.get("hw-mac-address")
            if hwMacAddress is not None:
                element_text = hwMacAddress
                interface_ethernet_dict_buffer["hwMacAddress"] = {}
                interface_ethernet_dict_buffer["hwMacAddress"]["type"] = "Property"
                interface_ethernet_dict_buffer["hwMacAddress"]["value"] = element_text
                interface_ethernet_dict_buffer["hwMacAddress"]["observedAt"] = observed_at
            macAddress = ethernet.get("mac-address")
            if macAddress is not None:
                element_text = macAddress
                interface_ethernet_dict_buffer["macAddress"] = {}
                interface_ethernet_dict_buffer["macAddress"]["type"] = "Property"
                interface_ethernet_dict_buffer["macAddress"]["value"] = element_text
                interface_ethernet_dict_buffer["macAddress"]["observedAt"] = observed_at
            physicalMedium = ethernet.get("physical-medium")
            if physicalMedium is not None:
                element_text = physicalMedium
                interface_ethernet_dict_buffer["physicalMedium"] = {}
                interface_ethernet_dict_buffer["physicalMedium"]["type"] = "Property"
                interface_ethernet_dict_buffer["physicalMedium"]["value"] = element_text
                interface_ethernet_dict_buffer["physicalMedium"]["observedAt"] = observed_at
            ptpAsymmetry = ethernet.get("ptp-asymmetry")
            if ptpAsymmetry is not None:
                element_text = ptpAsymmetry
                interface_ethernet_dict_buffer["ptpAsymmetry"] = {}
                interface_ethernet_dict_buffer["ptpAsymmetry"]["type"] = "Property"
                interface_ethernet_dict_buffer["ptpAsymmetry"]["value"] = int(element_text)
                interface_ethernet_dict_buffer["ptpAsymmetry"]["observedAt"] = observed_at
            standbySignaling = ethernet.get("standby-signaling")
            if standbySignaling is not None:
                element_text = standbySignaling
                interface_ethernet_dict_buffer["standbySignaling"] = {}
                interface_ethernet_dict_buffer["standbySignaling"]["type"] = "Property"
                interface_ethernet_dict_buffer["standbySignaling"]["value"] = element_text
                interface_ethernet_dict_buffer["standbySignaling"]["observedAt"] = observed_at
            reloadDelay = ethernet.get("reload-delay")
            if reloadDelay is not None:
                element_text = reloadDelay
                interface_ethernet_dict_buffer["reloadDelay"] = {}
                interface_ethernet_dict_buffer["reloadDelay"]["type"] = "Property"
                interface_ethernet_dict_buffer["reloadDelay"]["value"] = int(element_text)
                interface_ethernet_dict_buffer["reloadDelay"]["observedAt"] = observed_at
            reloadDelayExpires = ethernet.get("reload-delay-expires")
            if reloadDelayExpires is not None:
                element_text = reloadDelayExpires
                interface_ethernet_dict_buffer["reloadDelayExpires"] = {}
                interface_ethernet_dict_buffer["reloadDelayExpires"]["type"] = "Property"
                interface_ethernet_dict_buffer["reloadDelayExpires"]["value"] = element_text
                interface_ethernet_dict_buffer["reloadDelayExpires"]["observedAt"] = observed_at
            hold_time = ethernet.get("hold-time")
            if hold_time is not None and len(hold_time) != 0:
                interface_ethernet_hold_time_dict_buffer = {}
                interface_ethernet_hold_time_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetHoldTime:" + ":".join(interface_ethernet_dict_buffer["id"].split(":")[3:])
                interface_ethernet_hold_time_dict_buffer["type"] = "InterfaceEthernetHoldTime"
                interface_ethernet_hold_time_dict_buffer["isPartOf"] = {}
                interface_ethernet_hold_time_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_ethernet_hold_time_dict_buffer["isPartOf"]["object"] = interface_ethernet_dict_buffer["id"]
                interface_ethernet_hold_time_dict_buffer["isPartOf"]["observedAt"] = observed_at
                up = hold_time.get("up")
                if up is not None:
                    element_text = up
                    interface_ethernet_hold_time_dict_buffer["up"] = {}
                    interface_ethernet_hold_time_dict_buffer["up"]["type"] = "Property"
                    interface_ethernet_hold_time_dict_buffer["up"]["value"] = int(element_text)
                    interface_ethernet_hold_time_dict_buffer["up"]["observedAt"] = observed_at
                upExpires = hold_time.get("up-expires")
                if upExpires is not None:
                    element_text = upExpires
                    interface_ethernet_hold_time_dict_buffer["upExpires"] = {}
                    interface_ethernet_hold_time_dict_buffer["upExpires"]["type"] = "Property"
                    interface_ethernet_hold_time_dict_buffer["upExpires"]["value"] = element_text
                    interface_ethernet_hold_time_dict_buffer["upExpires"]["observedAt"] = observed_at
                down = hold_time.get("down")
                if down is not None:
                    element_text = down
                    interface_ethernet_hold_time_dict_buffer["down"] = {}
                    interface_ethernet_hold_time_dict_buffer["down"]["type"] = "Property"
                    interface_ethernet_hold_time_dict_buffer["down"]["value"] = int(element_text)
                    interface_ethernet_hold_time_dict_buffer["down"]["observedAt"] = observed_at
                downExpires = hold_time.get("down-expires")
                if downExpires is not None:
                    element_text = downExpires
                    interface_ethernet_hold_time_dict_buffer["downExpires"] = {}
                    interface_ethernet_hold_time_dict_buffer["downExpires"]["type"] = "Property"
                    interface_ethernet_hold_time_dict_buffer["downExpires"]["value"] = element_text
                    interface_ethernet_hold_time_dict_buffer["downExpires"]["observedAt"] = observed_at
                dict_buffers.append(interface_ethernet_hold_time_dict_buffer)
            crc_monitor = ethernet.get("crc-monitor")
            if crc_monitor is not None and len(crc_monitor) != 0:
                interface_ethernet_crc_monitor_dict_buffer = {}
                interface_ethernet_crc_monitor_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetCrcMonitor:" + ":".join(interface_ethernet_dict_buffer["id"].split(":")[3:])
                interface_ethernet_crc_monitor_dict_buffer["type"] = "InterfaceEthernetCrcMonitor"
                interface_ethernet_crc_monitor_dict_buffer["isPartOf"] = {}
                interface_ethernet_crc_monitor_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_ethernet_crc_monitor_dict_buffer["isPartOf"]["object"] = interface_ethernet_dict_buffer["id"]
                interface_ethernet_crc_monitor_dict_buffer["isPartOf"]["observedAt"] = observed_at
                adminState = crc_monitor.get("admin-state")
                if adminState is not None:
                    element_text = adminState
                    interface_ethernet_crc_monitor_dict_buffer["adminState"] = {}
                    interface_ethernet_crc_monitor_dict_buffer["adminState"]["type"] = "Property"
                    interface_ethernet_crc_monitor_dict_buffer["adminState"]["value"] = element_text
                    interface_ethernet_crc_monitor_dict_buffer["adminState"]["observedAt"] = observed_at
                windowSize = crc_monitor.get("window-size")
                if windowSize is not None:
                    element_text = windowSize
                    interface_ethernet_crc_monitor_dict_buffer["windowSize"] = {}
                    interface_ethernet_crc_monitor_dict_buffer["windowSize"]["type"] = "Property"
                    interface_ethernet_crc_monitor_dict_buffer["windowSize"]["value"] = int(element_text)
                    interface_ethernet_crc_monitor_dict_buffer["windowSize"]["observedAt"] = observed_at
                signal_degrade = crc_monitor.get("signal-degrade")
                if signal_degrade is not None and len(signal_degrade) != 0:
                    interface_ethernet_crc_monitor_signal_degrade_dict_buffer = {}
                    interface_ethernet_crc_monitor_signal_degrade_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetCrcMonitorSignalDegrade:" + ":".join(interface_ethernet_crc_monitor_dict_buffer["id"].split(":")[3:])
                    interface_ethernet_crc_monitor_signal_degrade_dict_buffer["type"] = "InterfaceEthernetCrcMonitorSignalDegrade"
                    interface_ethernet_crc_monitor_signal_degrade_dict_buffer["isPartOf"] = {}
                    interface_ethernet_crc_monitor_signal_degrade_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_ethernet_crc_monitor_signal_degrade_dict_buffer["isPartOf"]["object"] = interface_ethernet_crc_monitor_dict_buffer["id"]
                    interface_ethernet_crc_monitor_signal_degrade_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    exponent = signal_degrade.get("exponent")
                    if exponent is not None:
                        element_text = exponent
                        interface_ethernet_crc_monitor_signal_degrade_dict_buffer["exponent"] = {}
                        interface_ethernet_crc_monitor_signal_degrade_dict_buffer["exponent"]["type"] = "Property"
                        interface_ethernet_crc_monitor_signal_degrade_dict_buffer["exponent"]["value"] = int(element_text)
                        interface_ethernet_crc_monitor_signal_degrade_dict_buffer["exponent"]["observedAt"] = observed_at
                    multiplier = signal_degrade.get("multiplier")
                    if multiplier is not None:
                        element_text = multiplier
                        interface_ethernet_crc_monitor_signal_degrade_dict_buffer["multiplier"] = {}
                        interface_ethernet_crc_monitor_signal_degrade_dict_buffer["multiplier"]["type"] = "Property"
                        interface_ethernet_crc_monitor_signal_degrade_dict_buffer["multiplier"]["value"] = int(element_text)
                        interface_ethernet_crc_monitor_signal_degrade_dict_buffer["multiplier"]["observedAt"] = observed_at
                    dict_buffers.append(interface_ethernet_crc_monitor_signal_degrade_dict_buffer)
                signal_failure = crc_monitor.get("signal-failure")
                if signal_failure is not None and len(signal_failure) != 0:
                    interface_ethernet_crc_monitor_signal_failure_dict_buffer = {}
                    interface_ethernet_crc_monitor_signal_failure_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetCrcMonitorSignalFailure:" + ":".join(interface_ethernet_crc_monitor_dict_buffer["id"].split(":")[3:])
                    interface_ethernet_crc_monitor_signal_failure_dict_buffer["type"] = "InterfaceEthernetCrcMonitorSignalFailure"
                    interface_ethernet_crc_monitor_signal_failure_dict_buffer["isPartOf"] = {}
                    interface_ethernet_crc_monitor_signal_failure_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_ethernet_crc_monitor_signal_failure_dict_buffer["isPartOf"]["object"] = interface_ethernet_crc_monitor_dict_buffer["id"]
                    interface_ethernet_crc_monitor_signal_failure_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    exponent = signal_failure.get("exponent")
                    if exponent is not None:
                        element_text = exponent
                        interface_ethernet_crc_monitor_signal_failure_dict_buffer["exponent"] = {}
                        interface_ethernet_crc_monitor_signal_failure_dict_buffer["exponent"]["type"] = "Property"
                        interface_ethernet_crc_monitor_signal_failure_dict_buffer["exponent"]["value"] = int(element_text)
                        interface_ethernet_crc_monitor_signal_failure_dict_buffer["exponent"]["observedAt"] = observed_at
                    multiplier = signal_failure.get("multiplier")
                    if multiplier is not None:
                        element_text = multiplier
                        interface_ethernet_crc_monitor_signal_failure_dict_buffer["multiplier"] = {}
                        interface_ethernet_crc_monitor_signal_failure_dict_buffer["multiplier"]["type"] = "Property"
                        interface_ethernet_crc_monitor_signal_failure_dict_buffer["multiplier"]["value"] = int(element_text)
                        interface_ethernet_crc_monitor_signal_failure_dict_buffer["multiplier"]["observedAt"] = observed_at
                    dict_buffers.append(interface_ethernet_crc_monitor_signal_failure_dict_buffer)
                currentAlarms = crc_monitor.get("current-alarms")
                if currentAlarms is not None:
                    element_text = currentAlarms
                    interface_ethernet_crc_monitor_dict_buffer["currentAlarms"] = {}
                    interface_ethernet_crc_monitor_dict_buffer["currentAlarms"]["type"] = "Property"
                    interface_ethernet_crc_monitor_dict_buffer["currentAlarms"]["value"] = element_text
                    interface_ethernet_crc_monitor_dict_buffer["currentAlarms"]["observedAt"] = observed_at
                dict_buffers.append(interface_ethernet_crc_monitor_dict_buffer)
            symbol_monitor = ethernet.get("symbol-monitor")
            if symbol_monitor is not None and len(symbol_monitor) != 0:
                interface_ethernet_symbol_monitor_dict_buffer = {}
                interface_ethernet_symbol_monitor_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetSymbolMonitor:" + ":".join(interface_ethernet_dict_buffer["id"].split(":")[3:])
                interface_ethernet_symbol_monitor_dict_buffer["type"] = "InterfaceEthernetSymbolMonitor"
                interface_ethernet_symbol_monitor_dict_buffer["isPartOf"] = {}
                interface_ethernet_symbol_monitor_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_ethernet_symbol_monitor_dict_buffer["isPartOf"]["object"] = interface_ethernet_dict_buffer["id"]
                interface_ethernet_symbol_monitor_dict_buffer["isPartOf"]["observedAt"] = observed_at
                adminState = symbol_monitor.get("admin-state")
                if adminState is not None:
                    element_text = adminState
                    interface_ethernet_symbol_monitor_dict_buffer["adminState"] = {}
                    interface_ethernet_symbol_monitor_dict_buffer["adminState"]["type"] = "Property"
                    interface_ethernet_symbol_monitor_dict_buffer["adminState"]["value"] = element_text
                    interface_ethernet_symbol_monitor_dict_buffer["adminState"]["observedAt"] = observed_at
                windowSize = symbol_monitor.get("window-size")
                if windowSize is not None:
                    element_text = windowSize
                    interface_ethernet_symbol_monitor_dict_buffer["windowSize"] = {}
                    interface_ethernet_symbol_monitor_dict_buffer["windowSize"]["type"] = "Property"
                    interface_ethernet_symbol_monitor_dict_buffer["windowSize"]["value"] = int(element_text)
                    interface_ethernet_symbol_monitor_dict_buffer["windowSize"]["observedAt"] = observed_at
                signal_degrade = symbol_monitor.get("signal-degrade")
                if signal_degrade is not None and len(signal_degrade) != 0:
                    interface_ethernet_symbol_monitor_signal_degrade_dict_buffer = {}
                    interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetSymbolMonitorSignalDegrade:" + ":".join(interface_ethernet_symbol_monitor_dict_buffer["id"].split(":")[3:])
                    interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["type"] = "InterfaceEthernetSymbolMonitorSignalDegrade"
                    interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["isPartOf"] = {}
                    interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["isPartOf"]["object"] = interface_ethernet_symbol_monitor_dict_buffer["id"]
                    interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    exponent = signal_degrade.get("exponent")
                    if exponent is not None:
                        element_text = exponent
                        interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["exponent"] = {}
                        interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["exponent"]["type"] = "Property"
                        interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["exponent"]["value"] = int(element_text)
                        interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["exponent"]["observedAt"] = observed_at
                    multiplier = signal_degrade.get("multiplier")
                    if multiplier is not None:
                        element_text = multiplier
                        interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["multiplier"] = {}
                        interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["multiplier"]["type"] = "Property"
                        interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["multiplier"]["value"] = int(element_text)
                        interface_ethernet_symbol_monitor_signal_degrade_dict_buffer["multiplier"]["observedAt"] = observed_at
                    dict_buffers.append(interface_ethernet_symbol_monitor_signal_degrade_dict_buffer)
                signal_failure = symbol_monitor.get("signal-failure")
                if signal_failure is not None and len(signal_failure) != 0:
                    interface_ethernet_symbol_monitor_signal_failure_dict_buffer = {}
                    interface_ethernet_symbol_monitor_signal_failure_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetSymbolMonitorSignalFailure:" + ":".join(interface_ethernet_symbol_monitor_dict_buffer["id"].split(":")[3:])
                    interface_ethernet_symbol_monitor_signal_failure_dict_buffer["type"] = "InterfaceEthernetSymbolMonitorSignalFailure"
                    interface_ethernet_symbol_monitor_signal_failure_dict_buffer["isPartOf"] = {}
                    interface_ethernet_symbol_monitor_signal_failure_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_ethernet_symbol_monitor_signal_failure_dict_buffer["isPartOf"]["object"] = interface_ethernet_symbol_monitor_dict_buffer["id"]
                    interface_ethernet_symbol_monitor_signal_failure_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    exponent = signal_failure.get("exponent")
                    if exponent is not None:
                        element_text = exponent
                        interface_ethernet_symbol_monitor_signal_failure_dict_buffer["exponent"] = {}
                        interface_ethernet_symbol_monitor_signal_failure_dict_buffer["exponent"]["type"] = "Property"
                        interface_ethernet_symbol_monitor_signal_failure_dict_buffer["exponent"]["value"] = int(element_text)
                        interface_ethernet_symbol_monitor_signal_failure_dict_buffer["exponent"]["observedAt"] = observed_at
                    multiplier = signal_failure.get("multiplier")
                    if multiplier is not None:
                        element_text = multiplier
                        interface_ethernet_symbol_monitor_signal_failure_dict_buffer["multiplier"] = {}
                        interface_ethernet_symbol_monitor_signal_failure_dict_buffer["multiplier"]["type"] = "Property"
                        interface_ethernet_symbol_monitor_signal_failure_dict_buffer["multiplier"]["value"] = int(element_text)
                        interface_ethernet_symbol_monitor_signal_failure_dict_buffer["multiplier"]["observedAt"] = observed_at
                    dict_buffers.append(interface_ethernet_symbol_monitor_signal_failure_dict_buffer)
                currentAlarms = symbol_monitor.get("current-alarms")
                if currentAlarms is not None:
                    element_text = currentAlarms
                    interface_ethernet_symbol_monitor_dict_buffer["currentAlarms"] = {}
                    interface_ethernet_symbol_monitor_dict_buffer["currentAlarms"]["type"] = "Property"
                    interface_ethernet_symbol_monitor_dict_buffer["currentAlarms"]["value"] = element_text
                    interface_ethernet_symbol_monitor_dict_buffer["currentAlarms"]["observedAt"] = observed_at
                dict_buffers.append(interface_ethernet_symbol_monitor_dict_buffer)
            storm_control = ethernet.get("storm-control")
            if storm_control is not None and len(storm_control) != 0:
                interface_ethernet_storm_control_dict_buffer = {}
                interface_ethernet_storm_control_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetStormControl:" + ":".join(interface_ethernet_dict_buffer["id"].split(":")[3:])
                interface_ethernet_storm_control_dict_buffer["type"] = "InterfaceEthernetStormControl"
                interface_ethernet_storm_control_dict_buffer["isPartOf"] = {}
                interface_ethernet_storm_control_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_ethernet_storm_control_dict_buffer["isPartOf"]["object"] = interface_ethernet_dict_buffer["id"]
                interface_ethernet_storm_control_dict_buffer["isPartOf"]["observedAt"] = observed_at
                units = storm_control.get("units")
                if units is not None:
                    element_text = units
                    interface_ethernet_storm_control_dict_buffer["units"] = {}
                    interface_ethernet_storm_control_dict_buffer["units"]["type"] = "Property"
                    interface_ethernet_storm_control_dict_buffer["units"]["value"] = element_text
                    interface_ethernet_storm_control_dict_buffer["units"]["observedAt"] = observed_at
                broadcastRate = storm_control.get("broadcast-rate")
                if broadcastRate is not None:
                    element_text = broadcastRate
                    interface_ethernet_storm_control_dict_buffer["broadcastRate"] = {}
                    interface_ethernet_storm_control_dict_buffer["broadcastRate"]["type"] = "Property"
                    interface_ethernet_storm_control_dict_buffer["broadcastRate"]["value"] = int(element_text)
                    interface_ethernet_storm_control_dict_buffer["broadcastRate"]["observedAt"] = observed_at
                multicastRate = storm_control.get("multicast-rate")
                if multicastRate is not None:
                    element_text = multicastRate
                    interface_ethernet_storm_control_dict_buffer["multicastRate"] = {}
                    interface_ethernet_storm_control_dict_buffer["multicastRate"]["type"] = "Property"
                    interface_ethernet_storm_control_dict_buffer["multicastRate"]["value"] = int(element_text)
                    interface_ethernet_storm_control_dict_buffer["multicastRate"]["observedAt"] = observed_at
                unknownUnicastRate = storm_control.get("unknown-unicast-rate")
                if unknownUnicastRate is not None:
                    element_text = unknownUnicastRate
                    interface_ethernet_storm_control_dict_buffer["unknownUnicastRate"] = {}
                    interface_ethernet_storm_control_dict_buffer["unknownUnicastRate"]["type"] = "Property"
                    interface_ethernet_storm_control_dict_buffer["unknownUnicastRate"]["value"] = int(element_text)
                    interface_ethernet_storm_control_dict_buffer["unknownUnicastRate"]["observedAt"] = observed_at
                operationalBroadcastRate = storm_control.get("operational-broadcast-rate")
                if operationalBroadcastRate is not None:
                    element_text = operationalBroadcastRate
                    interface_ethernet_storm_control_dict_buffer["operationalBroadcastRate"] = {}
                    interface_ethernet_storm_control_dict_buffer["operationalBroadcastRate"]["type"] = "Property"
                    interface_ethernet_storm_control_dict_buffer["operationalBroadcastRate"]["value"] = int(element_text)
                    interface_ethernet_storm_control_dict_buffer["operationalBroadcastRate"]["observedAt"] = observed_at
                operationalMulticastRate = storm_control.get("operational-multicast-rate")
                if operationalMulticastRate is not None:
                    element_text = operationalMulticastRate
                    interface_ethernet_storm_control_dict_buffer["operationalMulticastRate"] = {}
                    interface_ethernet_storm_control_dict_buffer["operationalMulticastRate"]["type"] = "Property"
                    interface_ethernet_storm_control_dict_buffer["operationalMulticastRate"]["value"] = int(element_text)
                    interface_ethernet_storm_control_dict_buffer["operationalMulticastRate"]["observedAt"] = observed_at
                operationalUnknownUnicastRate = storm_control.get("operational-unknown-unicast-rate")
                if operationalUnknownUnicastRate is not None:
                    element_text = operationalUnknownUnicastRate
                    interface_ethernet_storm_control_dict_buffer["operationalUnknownUnicastRate"] = {}
                    interface_ethernet_storm_control_dict_buffer["operationalUnknownUnicastRate"]["type"] = "Property"
                    interface_ethernet_storm_control_dict_buffer["operationalUnknownUnicastRate"]["value"] = int(element_text)
                    interface_ethernet_storm_control_dict_buffer["operationalUnknownUnicastRate"]["observedAt"] = observed_at
                dict_buffers.append(interface_ethernet_storm_control_dict_buffer)
            synce = ethernet.get("synce")
            if synce is not None and len(synce) != 0:
                ssm = synce.get("ssm")
                if ssm is not None and len(ssm) != 0:
                    interface_ethernet_ssm_dict_buffer = {}
                    interface_ethernet_ssm_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetSynceSsm:" + ":".join(interface_ethernet_dict_buffer["id"].split(":")[3:])
                    interface_ethernet_ssm_dict_buffer["type"] = "InterfaceEthernetSynceSsm"
                    interface_ethernet_ssm_dict_buffer["isPartOf"] = {}
                    interface_ethernet_ssm_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_ethernet_ssm_dict_buffer["isPartOf"]["object"] = interface_ethernet_dict_buffer["id"]
                    interface_ethernet_ssm_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    adminState = ssm.get("admin-state")
                    if adminState is not None:
                        element_text = adminState
                        interface_ethernet_ssm_dict_buffer["adminState"] = {}
                        interface_ethernet_ssm_dict_buffer["adminState"]["type"] = "Property"
                        interface_ethernet_ssm_dict_buffer["adminState"]["value"] = element_text
                        interface_ethernet_ssm_dict_buffer["adminState"]["observedAt"] = observed_at
                    dict_buffers.append(interface_ethernet_ssm_dict_buffer)
            statistics = ethernet.get("statistics")
            if statistics is not None and len(statistics) != 0:
                interface_ethernet_statistics_dict_buffer = {}
                interface_ethernet_statistics_dict_buffer["id"] = "urn:ngsi-ld:InterfaceEthernetStatistics:" + ":".join(interface_ethernet_dict_buffer["id"].split(":")[3:])
                interface_ethernet_statistics_dict_buffer["type"] = "InterfaceEthernetStatistics"
                interface_ethernet_statistics_dict_buffer["isPartOf"] = {}
                interface_ethernet_statistics_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_ethernet_statistics_dict_buffer["isPartOf"]["object"] = interface_ethernet_dict_buffer["id"]
                interface_ethernet_statistics_dict_buffer["isPartOf"]["observedAt"] = observed_at
                inMacPauseFrames = statistics.get("in-mac-pause-frames")
                if inMacPauseFrames is not None:
                    element_text = inMacPauseFrames
                    interface_ethernet_statistics_dict_buffer["inMacPauseFrames"] = {}
                    interface_ethernet_statistics_dict_buffer["inMacPauseFrames"]["type"] = "Property"
                    interface_ethernet_statistics_dict_buffer["inMacPauseFrames"]["value"] = int(element_text)
                    interface_ethernet_statistics_dict_buffer["inMacPauseFrames"]["observedAt"] = observed_at
                inOversizeFrames = statistics.get("in-oversize-frames")
                if inOversizeFrames is not None:
                    element_text = inOversizeFrames
                    interface_ethernet_statistics_dict_buffer["inOversizeFrames"] = {}
                    interface_ethernet_statistics_dict_buffer["inOversizeFrames"]["type"] = "Property"
                    interface_ethernet_statistics_dict_buffer["inOversizeFrames"]["value"] = int(element_text)
                    interface_ethernet_statistics_dict_buffer["inOversizeFrames"]["observedAt"] = observed_at
                inJabberFrames = statistics.get("in-jabber-frames")
                if inJabberFrames is not None:
                    element_text = inJabberFrames
                    interface_ethernet_statistics_dict_buffer["inJabberFrames"] = {}
                    interface_ethernet_statistics_dict_buffer["inJabberFrames"]["type"] = "Property"
                    interface_ethernet_statistics_dict_buffer["inJabberFrames"]["value"] = int(element_text)
                    interface_ethernet_statistics_dict_buffer["inJabberFrames"]["observedAt"] = observed_at
                inFragmentFrames = statistics.get("in-fragment-frames")
                if inFragmentFrames is not None:
                    element_text = inFragmentFrames
                    interface_ethernet_statistics_dict_buffer["inFragmentFrames"] = {}
                    interface_ethernet_statistics_dict_buffer["inFragmentFrames"]["type"] = "Property"
                    interface_ethernet_statistics_dict_buffer["inFragmentFrames"]["value"] = int(element_text)
                    interface_ethernet_statistics_dict_buffer["inFragmentFrames"]["observedAt"] = observed_at
                inCrcErrorFrames = statistics.get("in-crc-error-frames")
                if inCrcErrorFrames is not None:
                    element_text = inCrcErrorFrames
                    interface_ethernet_statistics_dict_buffer["inCrcErrorFrames"] = {}
                    interface_ethernet_statistics_dict_buffer["inCrcErrorFrames"]["type"] = "Property"
                    interface_ethernet_statistics_dict_buffer["inCrcErrorFrames"]["value"] = int(element_text)
                    interface_ethernet_statistics_dict_buffer["inCrcErrorFrames"]["observedAt"] = observed_at
                outMacPauseFrames = statistics.get("out-mac-pause-frames")
                if outMacPauseFrames is not None:
                    element_text = outMacPauseFrames
                    interface_ethernet_statistics_dict_buffer["outMacPauseFrames"] = {}
                    interface_ethernet_statistics_dict_buffer["outMacPauseFrames"]["type"] = "Property"
                    interface_ethernet_statistics_dict_buffer["outMacPauseFrames"]["value"] = int(element_text)
                    interface_ethernet_statistics_dict_buffer["outMacPauseFrames"]["observedAt"] = observed_at
                in64bFrames = statistics.get("in-64b-frames")
                if in64bFrames is not None:
                    element_text = in64bFrames
                    interface_ethernet_statistics_dict_buffer["in64bFrames"] = {}
                    interface_ethernet_statistics_dict_buffer["in64bFrames"]["type"] = "Property"
                    interface_ethernet_statistics_dict_buffer["in64bFrames"]["value"] = int(element_text)
                    interface_ethernet_statistics_dict_buffer["in64bFrames"]["observedAt"] = observed_at
                in65bTo127bFrames = statistics.get("in-65b-to-127b-frames")
                if in65bTo127bFrames is not None:
                    element_text = in65bTo127bFrames
                    interface_ethernet_statistics_dict_buffer["in65bTo127bFrames"] = {}
                    interface_ethernet_statistics_dict_buffer["in65bTo127bFrames"]["type"] = "Property"
                    interface_ethernet_statistics_dict_buffer["in65bTo127bFrames"]["value"] = int(element_text)
                    interface_ethernet_statistics_dict_buffer["in65bTo127bFrames"]["observedAt"] = observed_at
                in128bTo255bFrames = statistics.get("in-128b-to-255b-frames")
                if in128bTo255bFrames is not None:
                    element_text = in128bTo255bFrames
                    interface_ethernet_statistics_dict_buffer["in128bTo255bFrames"] = {}
                    interface_ethernet_statistics_dict_buffer["in128bTo255bFrames"]["type"] = "Property"
                    interface_ethernet_statistics_dict_buffer["in128bTo255bFrames"]["value"] = int(element_text)
                    interface_ethernet_statistics_dict_buffer["in128bTo255bFrames"]["observedAt"] = observed_at
                in256bTo511bFrames = statistics.get("in-256b-to-511b-frames")
                if in256bTo511bFrames is not None:
                    element_text = in256bTo511bFrames
                    interface_ethernet_statistics_dict_buffer["in256bTo511bFrames"] = {}
                    interface_ethernet_statistics_dict_buffer["in256bTo511bFrames"]["type"] = "Property"
                    interface_ethernet_statistics_dict_buffer["in256bTo511bFrames"]["value"] = int(element_text)
                    interface_ethernet_statistics_dict_buffer["in256bTo511bFrames"]["observedAt"] = observed_at
                in512bTo1023bFrames = statistics.get("in-512b-to-1023b-frames")
                if in512bTo1023bFrames is not None:
                    element_text = in512bTo1023bFrames
                    interface_ethernet_statistics_dict_buffer["in512bTo1023bFrames"] = {}
                    interface_ethernet_statistics_dict_buffer["in512bTo1023bFrames"]["type"] = "Property"
                    interface_ethernet_statistics_dict_buffer["in512bTo1023bFrames"]["value"] = int(element_text)
                    interface_ethernet_statistics_dict_buffer["in512bTo1023bFrames"]["observedAt"] = observed_at
                in1024bTo1518bFrames = statistics.get("in-1024b-to-1518b-frames")
                if in1024bTo1518bFrames is not None:
                    element_text = in1024bTo1518bFrames
                    interface_ethernet_statistics_dict_buffer["in1024bTo1518bFrames"] = {}
                    interface_ethernet_statistics_dict_buffer["in1024bTo1518bFrames"]["type"] = "Property"
                    interface_ethernet_statistics_dict_buffer["in1024bTo1518bFrames"]["value"] = int(element_text)
                    interface_ethernet_statistics_dict_buffer["in1024bTo1518bFrames"]["observedAt"] = observed_at
                in1519bOrLongerFrames = statistics.get("in-1519b-or-longer-frames")
                if in1519bOrLongerFrames is not None:
                    element_text = in1519bOrLongerFrames
                    interface_ethernet_statistics_dict_buffer["in1519bOrLongerFrames"] = {}
                    interface_ethernet_statistics_dict_buffer["in1519bOrLongerFrames"]["type"] = "Property"
                    interface_ethernet_statistics_dict_buffer["in1519bOrLongerFrames"]["value"] = int(element_text)
                    interface_ethernet_statistics_dict_buffer["in1519bOrLongerFrames"]["observedAt"] = observed_at
                out64bFrames = statistics.get("out-64b-frames")
                if out64bFrames is not None:
                    element_text = out64bFrames
                    interface_ethernet_statistics_dict_buffer["out64bFrames"] = {}
                    interface_ethernet_statistics_dict_buffer["out64bFrames"]["type"] = "Property"
                    interface_ethernet_statistics_dict_buffer["out64bFrames"]["value"] = int(element_text)
                    interface_ethernet_statistics_dict_buffer["out64bFrames"]["observedAt"] = observed_at
                out65bTo127bFrames = statistics.get("out-65b-to-127b-frames")
                if out65bTo127bFrames is not None:
                    element_text = out65bTo127bFrames
                    interface_ethernet_statistics_dict_buffer["out65bTo127bFrames"] = {}
                    interface_ethernet_statistics_dict_buffer["out65bTo127bFrames"]["type"] = "Property"
                    interface_ethernet_statistics_dict_buffer["out65bTo127bFrames"]["value"] = int(element_text)
                    interface_ethernet_statistics_dict_buffer["out65bTo127bFrames"]["observedAt"] = observed_at
                out128bTo255bFrames = statistics.get("out-128b-to-255b-frames")
                if out128bTo255bFrames is not None:
                    element_text = out128bTo255bFrames
                    interface_ethernet_statistics_dict_buffer["out128bTo255bFrames"] = {}
                    interface_ethernet_statistics_dict_buffer["out128bTo255bFrames"]["type"] = "Property"
                    interface_ethernet_statistics_dict_buffer["out128bTo255bFrames"]["value"] = int(element_text)
                    interface_ethernet_statistics_dict_buffer["out128bTo255bFrames"]["observedAt"] = observed_at
                out256bTo511bFrames = statistics.get("out-256b-to-511b-frames")
                if out256bTo511bFrames is not None:
                    element_text = out256bTo511bFrames
                    interface_ethernet_statistics_dict_buffer["out256bTo511bFrames"] = {}
                    interface_ethernet_statistics_dict_buffer["out256bTo511bFrames"]["type"] = "Property"
                    interface_ethernet_statistics_dict_buffer["out256bTo511bFrames"]["value"] = int(element_text)
                    interface_ethernet_statistics_dict_buffer["out256bTo511bFrames"]["observedAt"] = observed_at
                out512bTo1023bFrames = statistics.get("out-512b-to-1023b-frames")
                if out512bTo1023bFrames is not None:
                    element_text = out512bTo1023bFrames
                    interface_ethernet_statistics_dict_buffer["out512bTo1023bFrames"] = {}
                    interface_ethernet_statistics_dict_buffer["out512bTo1023bFrames"]["type"] = "Property"
                    interface_ethernet_statistics_dict_buffer["out512bTo1023bFrames"]["value"] = int(element_text)
                    interface_ethernet_statistics_dict_buffer["out512bTo1023bFrames"]["observedAt"] = observed_at
                out1024bTo1518bFrames = statistics.get("out-1024b-to-1518b-frames")
                if out1024bTo1518bFrames is not None:
                    element_text = out1024bTo1518bFrames
                    interface_ethernet_statistics_dict_buffer["out1024bTo1518bFrames"] = {}
                    interface_ethernet_statistics_dict_buffer["out1024bTo1518bFrames"]["type"] = "Property"
                    interface_ethernet_statistics_dict_buffer["out1024bTo1518bFrames"]["value"] = int(element_text)
                    interface_ethernet_statistics_dict_buffer["out1024bTo1518bFrames"]["observedAt"] = observed_at
                out1519bOrLongerFrames = statistics.get("out-1519b-or-longer-frames")
                if out1519bOrLongerFrames is not None:
                    element_text = out1519bOrLongerFrames
                    interface_ethernet_statistics_dict_buffer["out1519bOrLongerFrames"] = {}
                    interface_ethernet_statistics_dict_buffer["out1519bOrLongerFrames"]["type"] = "Property"
                    interface_ethernet_statistics_dict_buffer["out1519bOrLongerFrames"]["value"] = int(element_text)
                    interface_ethernet_statistics_dict_buffer["out1519bOrLongerFrames"]["observedAt"] = observed_at
                lastClear = statistics.get("last-clear")
                if lastClear is not None:
                    element_text = lastClear
                    interface_ethernet_statistics_dict_buffer["lastClear"] = {}
                    interface_ethernet_statistics_dict_buffer["lastClear"]["type"] = "Property"
                    interface_ethernet_statistics_dict_buffer["lastClear"]["value"] = element_text
                    interface_ethernet_statistics_dict_buffer["lastClear"]["observedAt"] = observed_at
                dict_buffers.append(interface_ethernet_statistics_dict_buffer)
            dict_buffers.append(interface_ethernet_dict_buffer)
        interface_subinterface = interface.get("subinterface")
        if interface_subinterface is not None and len(interface_subinterface) != 0:
            for subinterface in interface_subinterface:
                interface_subinterface_dict_buffer = {}
                interface_subinterface_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterface:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
                interface_subinterface_dict_buffer["type"] = "InterfaceSubinterface"
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
                    interface_subinterface_dict_buffer["index"]["type"] = "Property"
                    interface_subinterface_dict_buffer["index"]["value"] = int(element_text)
                    interface_subinterface_dict_buffer["index"]["observedAt"] = observed_at
                type = subinterface.get("type")
                if type is not None and len(type) != 0:
                    element_text = type
                    if element_text is not None:
                        interface_subinterface_dict_buffer["subinterfaceType"] = {}
                        interface_subinterface_dict_buffer["subinterfaceType"]["type"] = "Relationship"
                        interface_subinterface_dict_buffer["subinterfaceType"]["object"] = "urn:ngsi-ld:YANGIdentity:" + element_text
                        interface_subinterface_dict_buffer["subinterfaceType"]["observedAt"] = observed_at
                description = subinterface.get("description")
                if description is not None:
                    element_text = description
                    interface_subinterface_dict_buffer["description"] = {}
                    interface_subinterface_dict_buffer["description"]["type"] = "Property"
                    interface_subinterface_dict_buffer["description"]["value"] = element_text
                    interface_subinterface_dict_buffer["description"]["observedAt"] = observed_at
                adminState = subinterface.get("admin-state")
                if adminState is not None:
                    element_text = adminState
                    interface_subinterface_dict_buffer["adminState"] = {}
                    interface_subinterface_dict_buffer["adminState"]["type"] = "Property"
                    interface_subinterface_dict_buffer["adminState"]["value"] = element_text
                    interface_subinterface_dict_buffer["adminState"]["observedAt"] = observed_at
                ipMtu = subinterface.get("ip-mtu")
                if ipMtu is not None:
                    element_text = ipMtu
                    interface_subinterface_dict_buffer["ipMtu"] = {}
                    interface_subinterface_dict_buffer["ipMtu"]["type"] = "Property"
                    interface_subinterface_dict_buffer["ipMtu"]["value"] = int(element_text)
                    interface_subinterface_dict_buffer["ipMtu"]["observedAt"] = observed_at
                l2Mtu = subinterface.get("l2-mtu")
                if l2Mtu is not None:
                    element_text = l2Mtu
                    interface_subinterface_dict_buffer["l2Mtu"] = {}
                    interface_subinterface_dict_buffer["l2Mtu"]["type"] = "Property"
                    interface_subinterface_dict_buffer["l2Mtu"]["value"] = int(element_text)
                    interface_subinterface_dict_buffer["l2Mtu"]["observedAt"] = observed_at
                mplsMtu = subinterface.get("mpls-mtu")
                if mplsMtu is not None:
                    element_text = mplsMtu
                    interface_subinterface_dict_buffer["mplsMtu"] = {}
                    interface_subinterface_dict_buffer["mplsMtu"]["type"] = "Property"
                    interface_subinterface_dict_buffer["mplsMtu"]["value"] = int(element_text)
                    interface_subinterface_dict_buffer["mplsMtu"]["observedAt"] = observed_at
                unidirectional_link_delay = subinterface.get("unidirectional-link-delay")
                if unidirectional_link_delay is not None and len(unidirectional_link_delay) != 0:
                    interface_subinterface_unidirectional_link_delay_dict_buffer = {}
                    interface_subinterface_unidirectional_link_delay_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceUnidirectionalLinkDelay:" + ":".join(interface_subinterface_dict_buffer["id"].split(":")[3:])
                    interface_subinterface_unidirectional_link_delay_dict_buffer["type"] = "InterfaceSubinterfaceUnidirectionalLinkDelay"
                    interface_subinterface_unidirectional_link_delay_dict_buffer["isPartOf"] = {}
                    interface_subinterface_unidirectional_link_delay_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_subinterface_unidirectional_link_delay_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                    interface_subinterface_unidirectional_link_delay_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    staticDelay = unidirectional_link_delay.get("static-delay")
                    if staticDelay is not None:
                        element_text = staticDelay
                        interface_subinterface_unidirectional_link_delay_dict_buffer["staticDelay"] = {}
                        interface_subinterface_unidirectional_link_delay_dict_buffer["staticDelay"]["type"] = "Property"
                        interface_subinterface_unidirectional_link_delay_dict_buffer["staticDelay"]["value"] = element_text
                        interface_subinterface_unidirectional_link_delay_dict_buffer["staticDelay"]["observedAt"] = observed_at
                    lastReportedDynamicDelay = unidirectional_link_delay.get("last-reported-dynamic-delay")
                    if lastReportedDynamicDelay is not None:
                        element_text = lastReportedDynamicDelay
                        interface_subinterface_unidirectional_link_delay_dict_buffer["lastReportedDynamicDelay"] = {}
                        interface_subinterface_unidirectional_link_delay_dict_buffer["lastReportedDynamicDelay"]["type"] = "Property"
                        interface_subinterface_unidirectional_link_delay_dict_buffer["lastReportedDynamicDelay"]["value"] = element_text
                        interface_subinterface_unidirectional_link_delay_dict_buffer["lastReportedDynamicDelay"]["observedAt"] = observed_at
                    dict_buffers.append(interface_subinterface_unidirectional_link_delay_dict_buffer)
                name = subinterface.get("name")
                if name is not None:
                    element_text = name
                    if interface_subinterface_dict_buffer["id"].split(":")[-1] != element_text:
                        interface_subinterface_dict_buffer["id"] = interface_subinterface_dict_buffer["id"] + ":" + element_text
                    interface_subinterface_dict_buffer["name"] = {}
                    interface_subinterface_dict_buffer["name"]["type"] = "Property"
                    interface_subinterface_dict_buffer["name"]["value"] = element_text
                    interface_subinterface_dict_buffer["name"]["observedAt"] = observed_at
                ifindex = subinterface.get("ifindex")
                if ifindex is not None:
                    element_text = ifindex
                    interface_subinterface_dict_buffer["ifindex"] = {}
                    interface_subinterface_dict_buffer["ifindex"]["type"] = "Property"
                    interface_subinterface_dict_buffer["ifindex"]["value"] = int(element_text)
                    interface_subinterface_dict_buffer["ifindex"]["observedAt"] = observed_at
                operState = subinterface.get("oper-state")
                if operState is not None:
                    element_text = operState
                    interface_subinterface_dict_buffer["operState"] = {}
                    interface_subinterface_dict_buffer["operState"]["type"] = "Property"
                    interface_subinterface_dict_buffer["operState"]["value"] = element_text
                    interface_subinterface_dict_buffer["operState"]["observedAt"] = observed_at
                operDownReason = subinterface.get("oper-down-reason")
                if operDownReason is not None:
                    element_text = operDownReason
                    interface_subinterface_dict_buffer["operDownReason"] = {}
                    interface_subinterface_dict_buffer["operDownReason"]["type"] = "Property"
                    interface_subinterface_dict_buffer["operDownReason"]["value"] = element_text
                    interface_subinterface_dict_buffer["operDownReason"]["observedAt"] = observed_at
                lastChange = subinterface.get("last-change")
                if lastChange is not None:
                    element_text = lastChange
                    interface_subinterface_dict_buffer["lastChange"] = {}
                    interface_subinterface_dict_buffer["lastChange"]["type"] = "Property"
                    interface_subinterface_dict_buffer["lastChange"]["value"] = element_text
                    interface_subinterface_dict_buffer["lastChange"]["observedAt"] = observed_at
                ipv4 = subinterface.get("ipv4")
                if ipv4 is not None and len(ipv4) != 0:
                    interface_subinterface_ipv4_dict_buffer = {}
                    interface_subinterface_ipv4_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceIpv4:" + ":".join(interface_subinterface_dict_buffer["id"].split(":")[3:])
                    interface_subinterface_ipv4_dict_buffer["type"] = "InterfaceSubinterfaceIpv4"
                    interface_subinterface_ipv4_dict_buffer["isPartOf"] = {}
                    interface_subinterface_ipv4_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_subinterface_ipv4_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                    interface_subinterface_ipv4_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    adminState = ipv4.get("admin-state")
                    if adminState is not None:
                        element_text = adminState
                        interface_subinterface_ipv4_dict_buffer["adminState"] = {}
                        interface_subinterface_ipv4_dict_buffer["adminState"]["type"] = "Property"
                        interface_subinterface_ipv4_dict_buffer["adminState"]["value"] = element_text
                        interface_subinterface_ipv4_dict_buffer["adminState"]["observedAt"] = observed_at
                    ipv4_address = ipv4.get("address")
                    if ipv4_address is not None and len(ipv4_address) != 0:
                        for address in ipv4_address:
                            interface_subinterface_ipv4_address_dict_buffer = {}
                            interface_subinterface_ipv4_address_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceIpv4Address:" + ":".join(interface_subinterface_ipv4_dict_buffer["id"].split(":")[3:])
                            interface_subinterface_ipv4_address_dict_buffer["type"] = "InterfaceSubinterfaceIpv4Address"
                            interface_subinterface_ipv4_address_dict_buffer["isPartOf"] = {}
                            interface_subinterface_ipv4_address_dict_buffer["isPartOf"]["type"] = "Relationship"
                            interface_subinterface_ipv4_address_dict_buffer["isPartOf"]["object"] = interface_subinterface_ipv4_dict_buffer["id"]
                            interface_subinterface_ipv4_address_dict_buffer["isPartOf"]["observedAt"] = observed_at
                            ipPrefix = address.get("ip-prefix")
                            if ipPrefix is not None:
                                element_text = ipPrefix
                                interface_subinterface_ipv4_address_dict_buffer["ipPrefix"] = {}
                                interface_subinterface_ipv4_address_dict_buffer["ipPrefix"]["type"] = "Property"
                                interface_subinterface_ipv4_address_dict_buffer["ipPrefix"]["value"] = element_text
                                interface_subinterface_ipv4_address_dict_buffer["ipPrefix"]["observedAt"] = observed_at
                            anycastGw = address.get("anycast-gw")
                            if anycastGw is not None:
                                element_text = anycastGw
                                interface_subinterface_ipv4_address_dict_buffer["anycastGw"] = {}
                                interface_subinterface_ipv4_address_dict_buffer["anycastGw"]["type"] = "Property"
                                interface_subinterface_ipv4_address_dict_buffer["anycastGw"]["value"] = eval(str(element_text).capitalize())
                                interface_subinterface_ipv4_address_dict_buffer["anycastGw"]["observedAt"] = observed_at
                            origin = address.get("origin")
                            if origin is not None:
                                element_text = origin
                                interface_subinterface_ipv4_address_dict_buffer["origin"] = {}
                                interface_subinterface_ipv4_address_dict_buffer["origin"]["type"] = "Property"
                                interface_subinterface_ipv4_address_dict_buffer["origin"]["value"] = element_text
                                interface_subinterface_ipv4_address_dict_buffer["origin"]["observedAt"] = observed_at
                            primary = address.get("primary")
                            if primary is not None:
                                element_text = primary
                                interface_subinterface_ipv4_address_dict_buffer["primary"] = {}
                                interface_subinterface_ipv4_address_dict_buffer["primary"]["type"] = "Property"
                                interface_subinterface_ipv4_address_dict_buffer["primary"]["value"] = element_text
                                interface_subinterface_ipv4_address_dict_buffer["primary"]["observedAt"] = observed_at
                            status = address.get("status")
                            if status is not None:
                                element_text = status
                                interface_subinterface_ipv4_address_dict_buffer["status"] = {}
                                interface_subinterface_ipv4_address_dict_buffer["status"]["type"] = "Property"
                                interface_subinterface_ipv4_address_dict_buffer["status"]["value"] = element_text
                                interface_subinterface_ipv4_address_dict_buffer["status"]["observedAt"] = observed_at
                            dict_buffers.append(interface_subinterface_ipv4_address_dict_buffer)
                    allowDirectedBroadcast = ipv4.get("allow-directed-broadcast")
                    if allowDirectedBroadcast is not None:
                        element_text = allowDirectedBroadcast
                        interface_subinterface_ipv4_dict_buffer["allowDirectedBroadcast"] = {}
                        interface_subinterface_ipv4_dict_buffer["allowDirectedBroadcast"]["type"] = "Property"
                        interface_subinterface_ipv4_dict_buffer["allowDirectedBroadcast"]["value"] = eval(str(element_text).capitalize())
                        interface_subinterface_ipv4_dict_buffer["allowDirectedBroadcast"]["observedAt"] = observed_at
                    unnumbered = ipv4.get("unnumbered")
                    if unnumbered is not None and len(unnumbered) != 0:
                        interface_subinterface_ipv4_unnumbered_dict_buffer = {}
                        interface_subinterface_ipv4_unnumbered_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceIpv4Unnumbered:" + ":".join(interface_subinterface_ipv4_dict_buffer["id"].split(":")[3:])
                        interface_subinterface_ipv4_unnumbered_dict_buffer["type"] = "InterfaceSubinterfaceIpv4Unnumbered"
                        interface_subinterface_ipv4_unnumbered_dict_buffer["isPartOf"] = {}
                        interface_subinterface_ipv4_unnumbered_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_subinterface_ipv4_unnumbered_dict_buffer["isPartOf"]["object"] = interface_subinterface_ipv4_dict_buffer["id"]
                        interface_subinterface_ipv4_unnumbered_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        adminState = unnumbered.get("admin-state")
                        if adminState is not None:
                            element_text = adminState
                            interface_subinterface_ipv4_unnumbered_dict_buffer["adminState"] = {}
                            interface_subinterface_ipv4_unnumbered_dict_buffer["adminState"]["type"] = "Property"
                            interface_subinterface_ipv4_unnumbered_dict_buffer["adminState"]["value"] = element_text
                            interface_subinterface_ipv4_unnumbered_dict_buffer["adminState"]["observedAt"] = observed_at
                        unnumbered_interface = unnumbered.get("interface")
                        if unnumbered_interface is not None:
                            element_text = unnumbered_interface
                            interface_subinterface_ipv4_unnumbered_dict_buffer["interface"] = {}
                            interface_subinterface_ipv4_unnumbered_dict_buffer["interface"]["type"] = "Property"
                            interface_subinterface_ipv4_unnumbered_dict_buffer["interface"]["value"] = element_text
                            interface_subinterface_ipv4_unnumbered_dict_buffer["interface"]["observedAt"] = observed_at
                        address = unnumbered.get("address")
                        if address is not None:
                            element_text = address
                            interface_subinterface_ipv4_unnumbered_dict_buffer["address"] = {}
                            interface_subinterface_ipv4_unnumbered_dict_buffer["address"]["type"] = "Property"
                            interface_subinterface_ipv4_unnumbered_dict_buffer["address"]["value"] = element_text
                            interface_subinterface_ipv4_unnumbered_dict_buffer["address"]["observedAt"] = observed_at
                        unavailableAddressReason = unnumbered.get("unavailable-address-reason")
                        if unavailableAddressReason is not None:
                            element_text = unavailableAddressReason
                            interface_subinterface_ipv4_unnumbered_dict_buffer["unavailableAddressReason"] = {}
                            interface_subinterface_ipv4_unnumbered_dict_buffer["unavailableAddressReason"]["type"] = "Property"
                            interface_subinterface_ipv4_unnumbered_dict_buffer["unavailableAddressReason"]["value"] = element_text
                            interface_subinterface_ipv4_unnumbered_dict_buffer["unavailableAddressReason"]["observedAt"] = observed_at
                        dict_buffers.append(interface_subinterface_ipv4_unnumbered_dict_buffer)
                    statistics = ipv4.get("statistics")
                    if statistics is not None and len(statistics) != 0:
                        interface_subinterface_ipv4_statistics_dict_buffer = {}
                        interface_subinterface_ipv4_statistics_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceIpv4Statistics:" + ":".join(interface_subinterface_ipv4_dict_buffer["id"].split(":")[3:])
                        interface_subinterface_ipv4_statistics_dict_buffer["type"] = "InterfaceSubinterfaceIpv4Statistics"
                        interface_subinterface_ipv4_statistics_dict_buffer["isPartOf"] = {}
                        interface_subinterface_ipv4_statistics_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_subinterface_ipv4_statistics_dict_buffer["isPartOf"]["object"] = interface_subinterface_ipv4_dict_buffer["id"]
                        interface_subinterface_ipv4_statistics_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        inPackets = statistics.get("in-packets")
                        if inPackets is not None:
                            element_text = inPackets
                            interface_subinterface_ipv4_statistics_dict_buffer["inPackets"] = {}
                            interface_subinterface_ipv4_statistics_dict_buffer["inPackets"]["type"] = "Property"
                            interface_subinterface_ipv4_statistics_dict_buffer["inPackets"]["value"] = int(element_text)
                            interface_subinterface_ipv4_statistics_dict_buffer["inPackets"]["observedAt"] = observed_at
                        inOctets = statistics.get("in-octets")
                        if inOctets is not None:
                            element_text = inOctets
                            interface_subinterface_ipv4_statistics_dict_buffer["inOctets"] = {}
                            interface_subinterface_ipv4_statistics_dict_buffer["inOctets"]["type"] = "Property"
                            interface_subinterface_ipv4_statistics_dict_buffer["inOctets"]["value"] = int(element_text)
                            interface_subinterface_ipv4_statistics_dict_buffer["inOctets"]["observedAt"] = observed_at
                        inErrorPackets = statistics.get("in-error-packets")
                        if inErrorPackets is not None:
                            element_text = inErrorPackets
                            interface_subinterface_ipv4_statistics_dict_buffer["inErrorPackets"] = {}
                            interface_subinterface_ipv4_statistics_dict_buffer["inErrorPackets"]["type"] = "Property"
                            interface_subinterface_ipv4_statistics_dict_buffer["inErrorPackets"]["value"] = int(element_text)
                            interface_subinterface_ipv4_statistics_dict_buffer["inErrorPackets"]["observedAt"] = observed_at
                        inDiscardedPackets = statistics.get("in-discarded-packets")
                        if inDiscardedPackets is not None:
                            element_text = inDiscardedPackets
                            interface_subinterface_ipv4_statistics_dict_buffer["inDiscardedPackets"] = {}
                            interface_subinterface_ipv4_statistics_dict_buffer["inDiscardedPackets"]["type"] = "Property"
                            interface_subinterface_ipv4_statistics_dict_buffer["inDiscardedPackets"]["value"] = int(element_text)
                            interface_subinterface_ipv4_statistics_dict_buffer["inDiscardedPackets"]["observedAt"] = observed_at
                        inTerminatedPackets = statistics.get("in-terminated-packets")
                        if inTerminatedPackets is not None:
                            element_text = inTerminatedPackets
                            interface_subinterface_ipv4_statistics_dict_buffer["inTerminatedPackets"] = {}
                            interface_subinterface_ipv4_statistics_dict_buffer["inTerminatedPackets"]["type"] = "Property"
                            interface_subinterface_ipv4_statistics_dict_buffer["inTerminatedPackets"]["value"] = int(element_text)
                            interface_subinterface_ipv4_statistics_dict_buffer["inTerminatedPackets"]["observedAt"] = observed_at
                        inTerminatedOctets = statistics.get("in-terminated-octets")
                        if inTerminatedOctets is not None:
                            element_text = inTerminatedOctets
                            interface_subinterface_ipv4_statistics_dict_buffer["inTerminatedOctets"] = {}
                            interface_subinterface_ipv4_statistics_dict_buffer["inTerminatedOctets"]["type"] = "Property"
                            interface_subinterface_ipv4_statistics_dict_buffer["inTerminatedOctets"]["value"] = int(element_text)
                            interface_subinterface_ipv4_statistics_dict_buffer["inTerminatedOctets"]["observedAt"] = observed_at
                        inForwardedPackets = statistics.get("in-forwarded-packets")
                        if inForwardedPackets is not None:
                            element_text = inForwardedPackets
                            interface_subinterface_ipv4_statistics_dict_buffer["inForwardedPackets"] = {}
                            interface_subinterface_ipv4_statistics_dict_buffer["inForwardedPackets"]["type"] = "Property"
                            interface_subinterface_ipv4_statistics_dict_buffer["inForwardedPackets"]["value"] = int(element_text)
                            interface_subinterface_ipv4_statistics_dict_buffer["inForwardedPackets"]["observedAt"] = observed_at
                        inForwardedOctets = statistics.get("in-forwarded-octets")
                        if inForwardedOctets is not None:
                            element_text = inForwardedOctets
                            interface_subinterface_ipv4_statistics_dict_buffer["inForwardedOctets"] = {}
                            interface_subinterface_ipv4_statistics_dict_buffer["inForwardedOctets"]["type"] = "Property"
                            interface_subinterface_ipv4_statistics_dict_buffer["inForwardedOctets"]["value"] = int(element_text)
                            interface_subinterface_ipv4_statistics_dict_buffer["inForwardedOctets"]["observedAt"] = observed_at
                        inMatchedRaPackets = statistics.get("in-matched-ra-packets")
                        if inMatchedRaPackets is not None:
                            element_text = inMatchedRaPackets
                            interface_subinterface_ipv4_statistics_dict_buffer["inMatchedRaPackets"] = {}
                            interface_subinterface_ipv4_statistics_dict_buffer["inMatchedRaPackets"]["type"] = "Property"
                            interface_subinterface_ipv4_statistics_dict_buffer["inMatchedRaPackets"]["value"] = int(element_text)
                            interface_subinterface_ipv4_statistics_dict_buffer["inMatchedRaPackets"]["observedAt"] = observed_at
                        outForwardedPackets = statistics.get("out-forwarded-packets")
                        if outForwardedPackets is not None:
                            element_text = outForwardedPackets
                            interface_subinterface_ipv4_statistics_dict_buffer["outForwardedPackets"] = {}
                            interface_subinterface_ipv4_statistics_dict_buffer["outForwardedPackets"]["type"] = "Property"
                            interface_subinterface_ipv4_statistics_dict_buffer["outForwardedPackets"]["value"] = int(element_text)
                            interface_subinterface_ipv4_statistics_dict_buffer["outForwardedPackets"]["observedAt"] = observed_at
                        outForwardedOctets = statistics.get("out-forwarded-octets")
                        if outForwardedOctets is not None:
                            element_text = outForwardedOctets
                            interface_subinterface_ipv4_statistics_dict_buffer["outForwardedOctets"] = {}
                            interface_subinterface_ipv4_statistics_dict_buffer["outForwardedOctets"]["type"] = "Property"
                            interface_subinterface_ipv4_statistics_dict_buffer["outForwardedOctets"]["value"] = int(element_text)
                            interface_subinterface_ipv4_statistics_dict_buffer["outForwardedOctets"]["observedAt"] = observed_at
                        outOriginatedPackets = statistics.get("out-originated-packets")
                        if outOriginatedPackets is not None:
                            element_text = outOriginatedPackets
                            interface_subinterface_ipv4_statistics_dict_buffer["outOriginatedPackets"] = {}
                            interface_subinterface_ipv4_statistics_dict_buffer["outOriginatedPackets"]["type"] = "Property"
                            interface_subinterface_ipv4_statistics_dict_buffer["outOriginatedPackets"]["value"] = int(element_text)
                            interface_subinterface_ipv4_statistics_dict_buffer["outOriginatedPackets"]["observedAt"] = observed_at
                        outOriginatedOctets = statistics.get("out-originated-octets")
                        if outOriginatedOctets is not None:
                            element_text = outOriginatedOctets
                            interface_subinterface_ipv4_statistics_dict_buffer["outOriginatedOctets"] = {}
                            interface_subinterface_ipv4_statistics_dict_buffer["outOriginatedOctets"]["type"] = "Property"
                            interface_subinterface_ipv4_statistics_dict_buffer["outOriginatedOctets"]["value"] = int(element_text)
                            interface_subinterface_ipv4_statistics_dict_buffer["outOriginatedOctets"]["observedAt"] = observed_at
                        outErrorPackets = statistics.get("out-error-packets")
                        if outErrorPackets is not None:
                            element_text = outErrorPackets
                            interface_subinterface_ipv4_statistics_dict_buffer["outErrorPackets"] = {}
                            interface_subinterface_ipv4_statistics_dict_buffer["outErrorPackets"]["type"] = "Property"
                            interface_subinterface_ipv4_statistics_dict_buffer["outErrorPackets"]["value"] = int(element_text)
                            interface_subinterface_ipv4_statistics_dict_buffer["outErrorPackets"]["observedAt"] = observed_at
                        outDiscardedPackets = statistics.get("out-discarded-packets")
                        if outDiscardedPackets is not None:
                            element_text = outDiscardedPackets
                            interface_subinterface_ipv4_statistics_dict_buffer["outDiscardedPackets"] = {}
                            interface_subinterface_ipv4_statistics_dict_buffer["outDiscardedPackets"]["type"] = "Property"
                            interface_subinterface_ipv4_statistics_dict_buffer["outDiscardedPackets"]["value"] = int(element_text)
                            interface_subinterface_ipv4_statistics_dict_buffer["outDiscardedPackets"]["observedAt"] = observed_at
                        outPackets = statistics.get("out-packets")
                        if outPackets is not None:
                            element_text = outPackets
                            interface_subinterface_ipv4_statistics_dict_buffer["outPackets"] = {}
                            interface_subinterface_ipv4_statistics_dict_buffer["outPackets"]["type"] = "Property"
                            interface_subinterface_ipv4_statistics_dict_buffer["outPackets"]["value"] = int(element_text)
                            interface_subinterface_ipv4_statistics_dict_buffer["outPackets"]["observedAt"] = observed_at
                        outOctets = statistics.get("out-octets")
                        if outOctets is not None:
                            element_text = outOctets
                            interface_subinterface_ipv4_statistics_dict_buffer["outOctets"] = {}
                            interface_subinterface_ipv4_statistics_dict_buffer["outOctets"]["type"] = "Property"
                            interface_subinterface_ipv4_statistics_dict_buffer["outOctets"]["value"] = int(element_text)
                            interface_subinterface_ipv4_statistics_dict_buffer["outOctets"]["observedAt"] = observed_at
                        lastClear = statistics.get("last-clear")
                        if lastClear is not None:
                            element_text = lastClear
                            interface_subinterface_ipv4_statistics_dict_buffer["lastClear"] = {}
                            interface_subinterface_ipv4_statistics_dict_buffer["lastClear"]["type"] = "Property"
                            interface_subinterface_ipv4_statistics_dict_buffer["lastClear"]["value"] = element_text
                            interface_subinterface_ipv4_statistics_dict_buffer["lastClear"]["observedAt"] = observed_at
                        dict_buffers.append(interface_subinterface_ipv4_statistics_dict_buffer)
                    dict_buffers.append(interface_subinterface_ipv4_dict_buffer)
                ipv6 = subinterface.get("ipv6")
                if ipv6 is not None and len(ipv6) != 0:
                    interface_subinterface_ipv6_dict_buffer = {}
                    interface_subinterface_ipv6_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceIpv6:" + ":".join(interface_subinterface_dict_buffer["id"].split(":")[3:])
                    interface_subinterface_ipv6_dict_buffer["type"] = "InterfaceSubinterfaceIpv6"
                    interface_subinterface_ipv6_dict_buffer["isPartOf"] = {}
                    interface_subinterface_ipv6_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_subinterface_ipv6_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                    interface_subinterface_ipv6_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    adminState = ipv6.get("admin-state")
                    if adminState is not None:
                        element_text = adminState
                        interface_subinterface_ipv6_dict_buffer["adminState"] = {}
                        interface_subinterface_ipv6_dict_buffer["adminState"]["type"] = "Property"
                        interface_subinterface_ipv6_dict_buffer["adminState"]["value"] = element_text
                        interface_subinterface_ipv6_dict_buffer["adminState"]["observedAt"] = observed_at
                    ipv6_address = ipv6.get("address")
                    if ipv6_address is not None and len(ipv6_address) != 0:
                        for address in ipv6_address:
                            interface_subinterface_ipv6_address_dict_buffer = {}
                            interface_subinterface_ipv6_address_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceIpv6Address:" + ":".join(interface_subinterface_ipv6_dict_buffer["id"].split(":")[3:])
                            interface_subinterface_ipv6_address_dict_buffer["type"] = "InterfaceSubinterfaceIpv6Address"
                            interface_subinterface_ipv6_address_dict_buffer["isPartOf"] = {}
                            interface_subinterface_ipv6_address_dict_buffer["isPartOf"]["type"] = "Relationship"
                            interface_subinterface_ipv6_address_dict_buffer["isPartOf"]["object"] = interface_subinterface_ipv6_dict_buffer["id"]
                            interface_subinterface_ipv6_address_dict_buffer["isPartOf"]["observedAt"] = observed_at
                            ipPrefix = address.get("ip-prefix")
                            if ipPrefix is not None:
                                element_text = ipPrefix
                                interface_subinterface_ipv6_address_dict_buffer["ipPrefix"] = {}
                                interface_subinterface_ipv6_address_dict_buffer["ipPrefix"]["type"] = "Property"
                                interface_subinterface_ipv6_address_dict_buffer["ipPrefix"]["value"] = element_text
                                interface_subinterface_ipv6_address_dict_buffer["ipPrefix"]["observedAt"] = observed_at
                            type = address.get("type")
                            if type is not None:
                                element_text = type
                                interface_subinterface_ipv6_address_dict_buffer["type"] = {}
                                interface_subinterface_ipv6_address_dict_buffer["type"]["type"] = "Property"
                                interface_subinterface_ipv6_address_dict_buffer["type"]["value"] = element_text
                                interface_subinterface_ipv6_address_dict_buffer["type"]["observedAt"] = observed_at
                            anycastGw = address.get("anycast-gw")
                            if anycastGw is not None:
                                element_text = anycastGw
                                interface_subinterface_ipv6_address_dict_buffer["anycastGw"] = {}
                                interface_subinterface_ipv6_address_dict_buffer["anycastGw"]["type"] = "Property"
                                interface_subinterface_ipv6_address_dict_buffer["anycastGw"]["value"] = eval(str(element_text).capitalize())
                                interface_subinterface_ipv6_address_dict_buffer["anycastGw"]["observedAt"] = observed_at
                            origin = address.get("origin")
                            if origin is not None:
                                element_text = origin
                                interface_subinterface_ipv6_address_dict_buffer["origin"] = {}
                                interface_subinterface_ipv6_address_dict_buffer["origin"]["type"] = "Property"
                                interface_subinterface_ipv6_address_dict_buffer["origin"]["value"] = element_text
                                interface_subinterface_ipv6_address_dict_buffer["origin"]["observedAt"] = observed_at
                            primary = address.get("primary")
                            if primary is not None:
                                element_text = primary
                                interface_subinterface_ipv6_address_dict_buffer["primary"] = {}
                                interface_subinterface_ipv6_address_dict_buffer["primary"]["type"] = "Property"
                                interface_subinterface_ipv6_address_dict_buffer["primary"]["value"] = element_text
                                interface_subinterface_ipv6_address_dict_buffer["primary"]["observedAt"] = observed_at
                            status = address.get("status")
                            if status is not None:
                                element_text = status
                                interface_subinterface_ipv6_address_dict_buffer["status"] = {}
                                interface_subinterface_ipv6_address_dict_buffer["status"]["type"] = "Property"
                                interface_subinterface_ipv6_address_dict_buffer["status"]["value"] = element_text
                                interface_subinterface_ipv6_address_dict_buffer["status"]["observedAt"] = observed_at
                            dict_buffers.append(interface_subinterface_ipv6_address_dict_buffer)
                    statistics = ipv6.get("statistics")
                    if statistics is not None and len(statistics) != 0:
                        interface_subinterface_ipv6_statistics_dict_buffer = {}
                        interface_subinterface_ipv6_statistics_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceIpv6Statistics:" + ":".join(interface_subinterface_ipv6_dict_buffer["id"].split(":")[3:])
                        interface_subinterface_ipv6_statistics_dict_buffer["type"] = "InterfaceSubinterfaceIpv6Statistics"
                        interface_subinterface_ipv6_statistics_dict_buffer["isPartOf"] = {}
                        interface_subinterface_ipv6_statistics_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_subinterface_ipv6_statistics_dict_buffer["isPartOf"]["object"] = interface_subinterface_ipv6_dict_buffer["id"]
                        interface_subinterface_ipv6_statistics_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        inPackets = statistics.get("in-packets")
                        if inPackets is not None:
                            element_text = inPackets
                            interface_subinterface_ipv6_statistics_dict_buffer["inPackets"] = {}
                            interface_subinterface_ipv6_statistics_dict_buffer["inPackets"]["type"] = "Property"
                            interface_subinterface_ipv6_statistics_dict_buffer["inPackets"]["value"] = int(element_text)
                            interface_subinterface_ipv6_statistics_dict_buffer["inPackets"]["observedAt"] = observed_at
                        inOctets = statistics.get("in-octets")
                        if inOctets is not None:
                            element_text = inOctets
                            interface_subinterface_ipv6_statistics_dict_buffer["inOctets"] = {}
                            interface_subinterface_ipv6_statistics_dict_buffer["inOctets"]["type"] = "Property"
                            interface_subinterface_ipv6_statistics_dict_buffer["inOctets"]["value"] = int(element_text)
                            interface_subinterface_ipv6_statistics_dict_buffer["inOctets"]["observedAt"] = observed_at
                        inErrorPackets = statistics.get("in-error-packets")
                        if inErrorPackets is not None:
                            element_text = inErrorPackets
                            interface_subinterface_ipv6_statistics_dict_buffer["inErrorPackets"] = {}
                            interface_subinterface_ipv6_statistics_dict_buffer["inErrorPackets"]["type"] = "Property"
                            interface_subinterface_ipv6_statistics_dict_buffer["inErrorPackets"]["value"] = int(element_text)
                            interface_subinterface_ipv6_statistics_dict_buffer["inErrorPackets"]["observedAt"] = observed_at
                        inDiscardedPackets = statistics.get("in-discarded-packets")
                        if inDiscardedPackets is not None:
                            element_text = inDiscardedPackets
                            interface_subinterface_ipv6_statistics_dict_buffer["inDiscardedPackets"] = {}
                            interface_subinterface_ipv6_statistics_dict_buffer["inDiscardedPackets"]["type"] = "Property"
                            interface_subinterface_ipv6_statistics_dict_buffer["inDiscardedPackets"]["value"] = int(element_text)
                            interface_subinterface_ipv6_statistics_dict_buffer["inDiscardedPackets"]["observedAt"] = observed_at
                        inTerminatedPackets = statistics.get("in-terminated-packets")
                        if inTerminatedPackets is not None:
                            element_text = inTerminatedPackets
                            interface_subinterface_ipv6_statistics_dict_buffer["inTerminatedPackets"] = {}
                            interface_subinterface_ipv6_statistics_dict_buffer["inTerminatedPackets"]["type"] = "Property"
                            interface_subinterface_ipv6_statistics_dict_buffer["inTerminatedPackets"]["value"] = int(element_text)
                            interface_subinterface_ipv6_statistics_dict_buffer["inTerminatedPackets"]["observedAt"] = observed_at
                        inTerminatedOctets = statistics.get("in-terminated-octets")
                        if inTerminatedOctets is not None:
                            element_text = inTerminatedOctets
                            interface_subinterface_ipv6_statistics_dict_buffer["inTerminatedOctets"] = {}
                            interface_subinterface_ipv6_statistics_dict_buffer["inTerminatedOctets"]["type"] = "Property"
                            interface_subinterface_ipv6_statistics_dict_buffer["inTerminatedOctets"]["value"] = int(element_text)
                            interface_subinterface_ipv6_statistics_dict_buffer["inTerminatedOctets"]["observedAt"] = observed_at
                        inForwardedPackets = statistics.get("in-forwarded-packets")
                        if inForwardedPackets is not None:
                            element_text = inForwardedPackets
                            interface_subinterface_ipv6_statistics_dict_buffer["inForwardedPackets"] = {}
                            interface_subinterface_ipv6_statistics_dict_buffer["inForwardedPackets"]["type"] = "Property"
                            interface_subinterface_ipv6_statistics_dict_buffer["inForwardedPackets"]["value"] = int(element_text)
                            interface_subinterface_ipv6_statistics_dict_buffer["inForwardedPackets"]["observedAt"] = observed_at
                        inForwardedOctets = statistics.get("in-forwarded-octets")
                        if inForwardedOctets is not None:
                            element_text = inForwardedOctets
                            interface_subinterface_ipv6_statistics_dict_buffer["inForwardedOctets"] = {}
                            interface_subinterface_ipv6_statistics_dict_buffer["inForwardedOctets"]["type"] = "Property"
                            interface_subinterface_ipv6_statistics_dict_buffer["inForwardedOctets"]["value"] = int(element_text)
                            interface_subinterface_ipv6_statistics_dict_buffer["inForwardedOctets"]["observedAt"] = observed_at
                        inMatchedRaPackets = statistics.get("in-matched-ra-packets")
                        if inMatchedRaPackets is not None:
                            element_text = inMatchedRaPackets
                            interface_subinterface_ipv6_statistics_dict_buffer["inMatchedRaPackets"] = {}
                            interface_subinterface_ipv6_statistics_dict_buffer["inMatchedRaPackets"]["type"] = "Property"
                            interface_subinterface_ipv6_statistics_dict_buffer["inMatchedRaPackets"]["value"] = int(element_text)
                            interface_subinterface_ipv6_statistics_dict_buffer["inMatchedRaPackets"]["observedAt"] = observed_at
                        outForwardedPackets = statistics.get("out-forwarded-packets")
                        if outForwardedPackets is not None:
                            element_text = outForwardedPackets
                            interface_subinterface_ipv6_statistics_dict_buffer["outForwardedPackets"] = {}
                            interface_subinterface_ipv6_statistics_dict_buffer["outForwardedPackets"]["type"] = "Property"
                            interface_subinterface_ipv6_statistics_dict_buffer["outForwardedPackets"]["value"] = int(element_text)
                            interface_subinterface_ipv6_statistics_dict_buffer["outForwardedPackets"]["observedAt"] = observed_at
                        outForwardedOctets = statistics.get("out-forwarded-octets")
                        if outForwardedOctets is not None:
                            element_text = outForwardedOctets
                            interface_subinterface_ipv6_statistics_dict_buffer["outForwardedOctets"] = {}
                            interface_subinterface_ipv6_statistics_dict_buffer["outForwardedOctets"]["type"] = "Property"
                            interface_subinterface_ipv6_statistics_dict_buffer["outForwardedOctets"]["value"] = int(element_text)
                            interface_subinterface_ipv6_statistics_dict_buffer["outForwardedOctets"]["observedAt"] = observed_at
                        outOriginatedPackets = statistics.get("out-originated-packets")
                        if outOriginatedPackets is not None:
                            element_text = outOriginatedPackets
                            interface_subinterface_ipv6_statistics_dict_buffer["outOriginatedPackets"] = {}
                            interface_subinterface_ipv6_statistics_dict_buffer["outOriginatedPackets"]["type"] = "Property"
                            interface_subinterface_ipv6_statistics_dict_buffer["outOriginatedPackets"]["value"] = int(element_text)
                            interface_subinterface_ipv6_statistics_dict_buffer["outOriginatedPackets"]["observedAt"] = observed_at
                        outOriginatedOctets = statistics.get("out-originated-octets")
                        if outOriginatedOctets is not None:
                            element_text = outOriginatedOctets
                            interface_subinterface_ipv6_statistics_dict_buffer["outOriginatedOctets"] = {}
                            interface_subinterface_ipv6_statistics_dict_buffer["outOriginatedOctets"]["type"] = "Property"
                            interface_subinterface_ipv6_statistics_dict_buffer["outOriginatedOctets"]["value"] = int(element_text)
                            interface_subinterface_ipv6_statistics_dict_buffer["outOriginatedOctets"]["observedAt"] = observed_at
                        outErrorPackets = statistics.get("out-error-packets")
                        if outErrorPackets is not None:
                            element_text = outErrorPackets
                            interface_subinterface_ipv6_statistics_dict_buffer["outErrorPackets"] = {}
                            interface_subinterface_ipv6_statistics_dict_buffer["outErrorPackets"]["type"] = "Property"
                            interface_subinterface_ipv6_statistics_dict_buffer["outErrorPackets"]["value"] = int(element_text)
                            interface_subinterface_ipv6_statistics_dict_buffer["outErrorPackets"]["observedAt"] = observed_at
                        outDiscardedPackets = statistics.get("out-discarded-packets")
                        if outDiscardedPackets is not None:
                            element_text = outDiscardedPackets
                            interface_subinterface_ipv6_statistics_dict_buffer["outDiscardedPackets"] = {}
                            interface_subinterface_ipv6_statistics_dict_buffer["outDiscardedPackets"]["type"] = "Property"
                            interface_subinterface_ipv6_statistics_dict_buffer["outDiscardedPackets"]["value"] = int(element_text)
                            interface_subinterface_ipv6_statistics_dict_buffer["outDiscardedPackets"]["observedAt"] = observed_at
                        outPackets = statistics.get("out-packets")
                        if outPackets is not None:
                            element_text = outPackets
                            interface_subinterface_ipv6_statistics_dict_buffer["outPackets"] = {}
                            interface_subinterface_ipv6_statistics_dict_buffer["outPackets"]["type"] = "Property"
                            interface_subinterface_ipv6_statistics_dict_buffer["outPackets"]["value"] = int(element_text)
                            interface_subinterface_ipv6_statistics_dict_buffer["outPackets"]["observedAt"] = observed_at
                        outOctets = statistics.get("out-octets")
                        if outOctets is not None:
                            element_text = outOctets
                            interface_subinterface_ipv6_statistics_dict_buffer["outOctets"] = {}
                            interface_subinterface_ipv6_statistics_dict_buffer["outOctets"]["type"] = "Property"
                            interface_subinterface_ipv6_statistics_dict_buffer["outOctets"]["value"] = int(element_text)
                            interface_subinterface_ipv6_statistics_dict_buffer["outOctets"]["observedAt"] = observed_at
                        lastClear = statistics.get("last-clear")
                        if lastClear is not None:
                            element_text = lastClear
                            interface_subinterface_ipv6_statistics_dict_buffer["lastClear"] = {}
                            interface_subinterface_ipv6_statistics_dict_buffer["lastClear"]["type"] = "Property"
                            interface_subinterface_ipv6_statistics_dict_buffer["lastClear"]["value"] = element_text
                            interface_subinterface_ipv6_statistics_dict_buffer["lastClear"]["observedAt"] = observed_at
                        dict_buffers.append(interface_subinterface_ipv6_statistics_dict_buffer)
                    dict_buffers.append(interface_subinterface_ipv6_dict_buffer)
                anycast_gw = subinterface.get("anycast-gw")
                if anycast_gw is not None and len(anycast_gw) != 0:
                    interface_subinterface_anycast_gw_dict_buffer = {}
                    interface_subinterface_anycast_gw_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceAnycastGw:" + ":".join(interface_subinterface_dict_buffer["id"].split(":")[3:])
                    interface_subinterface_anycast_gw_dict_buffer["type"] = "InterfaceSubinterfaceAnycastGw"
                    interface_subinterface_anycast_gw_dict_buffer["isPartOf"] = {}
                    interface_subinterface_anycast_gw_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_subinterface_anycast_gw_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                    interface_subinterface_anycast_gw_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    virtualRouterId = anycast_gw.get("virtual-router-id")
                    if virtualRouterId is not None:
                        element_text = virtualRouterId
                        if interface_subinterface_anycast_gw_dict_buffer["id"].split(":")[-1] != int(element_text):
                            interface_subinterface_anycast_gw_dict_buffer["id"] = interface_subinterface_anycast_gw_dict_buffer["id"] + ":" + int(element_text)
                        interface_subinterface_anycast_gw_dict_buffer["virtualRouterId"] = {}
                        interface_subinterface_anycast_gw_dict_buffer["virtualRouterId"]["type"] = "Property"
                        interface_subinterface_anycast_gw_dict_buffer["virtualRouterId"]["value"] = int(element_text)
                        interface_subinterface_anycast_gw_dict_buffer["virtualRouterId"]["observedAt"] = observed_at
                    anycastGwMac = anycast_gw.get("anycast-gw-mac")
                    if anycastGwMac is not None:
                        element_text = anycastGwMac
                        interface_subinterface_anycast_gw_dict_buffer["anycastGwMac"] = {}
                        interface_subinterface_anycast_gw_dict_buffer["anycastGwMac"]["type"] = "Property"
                        interface_subinterface_anycast_gw_dict_buffer["anycastGwMac"]["value"] = element_text
                        interface_subinterface_anycast_gw_dict_buffer["anycastGwMac"]["observedAt"] = observed_at
                    anycastGwMacOrigin = anycast_gw.get("anycast-gw-mac-origin")
                    if anycastGwMacOrigin is not None:
                        element_text = anycastGwMacOrigin
                        interface_subinterface_anycast_gw_dict_buffer["anycastGwMacOrigin"] = {}
                        interface_subinterface_anycast_gw_dict_buffer["anycastGwMacOrigin"]["type"] = "Property"
                        interface_subinterface_anycast_gw_dict_buffer["anycastGwMacOrigin"]["value"] = element_text
                        interface_subinterface_anycast_gw_dict_buffer["anycastGwMacOrigin"]["observedAt"] = observed_at
                    dict_buffers.append(interface_subinterface_anycast_gw_dict_buffer)
                statistics = subinterface.get("statistics")
                if statistics is not None and len(statistics) != 0:
                    interface_subinterface_statistics_dict_buffer = {}
                    interface_subinterface_statistics_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceStatistics:" + ":".join(interface_subinterface_dict_buffer["id"].split(":")[3:])
                    interface_subinterface_statistics_dict_buffer["type"] = "InterfaceSubinterfaceStatistics"
                    interface_subinterface_statistics_dict_buffer["isPartOf"] = {}
                    interface_subinterface_statistics_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_subinterface_statistics_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                    interface_subinterface_statistics_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    inPackets = statistics.get("in-packets")
                    if inPackets is not None:
                        element_text = inPackets
                        interface_subinterface_statistics_dict_buffer["inPackets"] = {}
                        interface_subinterface_statistics_dict_buffer["inPackets"]["type"] = "Property"
                        interface_subinterface_statistics_dict_buffer["inPackets"]["value"] = int(element_text)
                        interface_subinterface_statistics_dict_buffer["inPackets"]["observedAt"] = observed_at
                    inOctets = statistics.get("in-octets")
                    if inOctets is not None:
                        element_text = inOctets
                        interface_subinterface_statistics_dict_buffer["inOctets"] = {}
                        interface_subinterface_statistics_dict_buffer["inOctets"]["type"] = "Property"
                        interface_subinterface_statistics_dict_buffer["inOctets"]["value"] = int(element_text)
                        interface_subinterface_statistics_dict_buffer["inOctets"]["observedAt"] = observed_at
                    inErrorPackets = statistics.get("in-error-packets")
                    if inErrorPackets is not None:
                        element_text = inErrorPackets
                        interface_subinterface_statistics_dict_buffer["inErrorPackets"] = {}
                        interface_subinterface_statistics_dict_buffer["inErrorPackets"]["type"] = "Property"
                        interface_subinterface_statistics_dict_buffer["inErrorPackets"]["value"] = int(element_text)
                        interface_subinterface_statistics_dict_buffer["inErrorPackets"]["observedAt"] = observed_at
                    inDiscardedPackets = statistics.get("in-discarded-packets")
                    if inDiscardedPackets is not None:
                        element_text = inDiscardedPackets
                        interface_subinterface_statistics_dict_buffer["inDiscardedPackets"] = {}
                        interface_subinterface_statistics_dict_buffer["inDiscardedPackets"]["type"] = "Property"
                        interface_subinterface_statistics_dict_buffer["inDiscardedPackets"]["value"] = int(element_text)
                        interface_subinterface_statistics_dict_buffer["inDiscardedPackets"]["observedAt"] = observed_at
                    inTerminatedPackets = statistics.get("in-terminated-packets")
                    if inTerminatedPackets is not None:
                        element_text = inTerminatedPackets
                        interface_subinterface_statistics_dict_buffer["inTerminatedPackets"] = {}
                        interface_subinterface_statistics_dict_buffer["inTerminatedPackets"]["type"] = "Property"
                        interface_subinterface_statistics_dict_buffer["inTerminatedPackets"]["value"] = int(element_text)
                        interface_subinterface_statistics_dict_buffer["inTerminatedPackets"]["observedAt"] = observed_at
                    inTerminatedOctets = statistics.get("in-terminated-octets")
                    if inTerminatedOctets is not None:
                        element_text = inTerminatedOctets
                        interface_subinterface_statistics_dict_buffer["inTerminatedOctets"] = {}
                        interface_subinterface_statistics_dict_buffer["inTerminatedOctets"]["type"] = "Property"
                        interface_subinterface_statistics_dict_buffer["inTerminatedOctets"]["value"] = int(element_text)
                        interface_subinterface_statistics_dict_buffer["inTerminatedOctets"]["observedAt"] = observed_at
                    inForwardedPackets = statistics.get("in-forwarded-packets")
                    if inForwardedPackets is not None:
                        element_text = inForwardedPackets
                        interface_subinterface_statistics_dict_buffer["inForwardedPackets"] = {}
                        interface_subinterface_statistics_dict_buffer["inForwardedPackets"]["type"] = "Property"
                        interface_subinterface_statistics_dict_buffer["inForwardedPackets"]["value"] = int(element_text)
                        interface_subinterface_statistics_dict_buffer["inForwardedPackets"]["observedAt"] = observed_at
                    inForwardedOctets = statistics.get("in-forwarded-octets")
                    if inForwardedOctets is not None:
                        element_text = inForwardedOctets
                        interface_subinterface_statistics_dict_buffer["inForwardedOctets"] = {}
                        interface_subinterface_statistics_dict_buffer["inForwardedOctets"]["type"] = "Property"
                        interface_subinterface_statistics_dict_buffer["inForwardedOctets"]["value"] = int(element_text)
                        interface_subinterface_statistics_dict_buffer["inForwardedOctets"]["observedAt"] = observed_at
                    inMatchedRaPackets = statistics.get("in-matched-ra-packets")
                    if inMatchedRaPackets is not None:
                        element_text = inMatchedRaPackets
                        interface_subinterface_statistics_dict_buffer["inMatchedRaPackets"] = {}
                        interface_subinterface_statistics_dict_buffer["inMatchedRaPackets"]["type"] = "Property"
                        interface_subinterface_statistics_dict_buffer["inMatchedRaPackets"]["value"] = int(element_text)
                        interface_subinterface_statistics_dict_buffer["inMatchedRaPackets"]["observedAt"] = observed_at
                    outForwardedPackets = statistics.get("out-forwarded-packets")
                    if outForwardedPackets is not None:
                        element_text = outForwardedPackets
                        interface_subinterface_statistics_dict_buffer["outForwardedPackets"] = {}
                        interface_subinterface_statistics_dict_buffer["outForwardedPackets"]["type"] = "Property"
                        interface_subinterface_statistics_dict_buffer["outForwardedPackets"]["value"] = int(element_text)
                        interface_subinterface_statistics_dict_buffer["outForwardedPackets"]["observedAt"] = observed_at
                    outForwardedOctets = statistics.get("out-forwarded-octets")
                    if outForwardedOctets is not None:
                        element_text = outForwardedOctets
                        interface_subinterface_statistics_dict_buffer["outForwardedOctets"] = {}
                        interface_subinterface_statistics_dict_buffer["outForwardedOctets"]["type"] = "Property"
                        interface_subinterface_statistics_dict_buffer["outForwardedOctets"]["value"] = int(element_text)
                        interface_subinterface_statistics_dict_buffer["outForwardedOctets"]["observedAt"] = observed_at
                    outOriginatedPackets = statistics.get("out-originated-packets")
                    if outOriginatedPackets is not None:
                        element_text = outOriginatedPackets
                        interface_subinterface_statistics_dict_buffer["outOriginatedPackets"] = {}
                        interface_subinterface_statistics_dict_buffer["outOriginatedPackets"]["type"] = "Property"
                        interface_subinterface_statistics_dict_buffer["outOriginatedPackets"]["value"] = int(element_text)
                        interface_subinterface_statistics_dict_buffer["outOriginatedPackets"]["observedAt"] = observed_at
                    outOriginatedOctets = statistics.get("out-originated-octets")
                    if outOriginatedOctets is not None:
                        element_text = outOriginatedOctets
                        interface_subinterface_statistics_dict_buffer["outOriginatedOctets"] = {}
                        interface_subinterface_statistics_dict_buffer["outOriginatedOctets"]["type"] = "Property"
                        interface_subinterface_statistics_dict_buffer["outOriginatedOctets"]["value"] = int(element_text)
                        interface_subinterface_statistics_dict_buffer["outOriginatedOctets"]["observedAt"] = observed_at
                    outErrorPackets = statistics.get("out-error-packets")
                    if outErrorPackets is not None:
                        element_text = outErrorPackets
                        interface_subinterface_statistics_dict_buffer["outErrorPackets"] = {}
                        interface_subinterface_statistics_dict_buffer["outErrorPackets"]["type"] = "Property"
                        interface_subinterface_statistics_dict_buffer["outErrorPackets"]["value"] = int(element_text)
                        interface_subinterface_statistics_dict_buffer["outErrorPackets"]["observedAt"] = observed_at
                    outDiscardedPackets = statistics.get("out-discarded-packets")
                    if outDiscardedPackets is not None:
                        element_text = outDiscardedPackets
                        interface_subinterface_statistics_dict_buffer["outDiscardedPackets"] = {}
                        interface_subinterface_statistics_dict_buffer["outDiscardedPackets"]["type"] = "Property"
                        interface_subinterface_statistics_dict_buffer["outDiscardedPackets"]["value"] = int(element_text)
                        interface_subinterface_statistics_dict_buffer["outDiscardedPackets"]["observedAt"] = observed_at
                    outPackets = statistics.get("out-packets")
                    if outPackets is not None:
                        element_text = outPackets
                        interface_subinterface_statistics_dict_buffer["outPackets"] = {}
                        interface_subinterface_statistics_dict_buffer["outPackets"]["type"] = "Property"
                        interface_subinterface_statistics_dict_buffer["outPackets"]["value"] = int(element_text)
                        interface_subinterface_statistics_dict_buffer["outPackets"]["observedAt"] = observed_at
                    outOctets = statistics.get("out-octets")
                    if outOctets is not None:
                        element_text = outOctets
                        interface_subinterface_statistics_dict_buffer["outOctets"] = {}
                        interface_subinterface_statistics_dict_buffer["outOctets"]["type"] = "Property"
                        interface_subinterface_statistics_dict_buffer["outOctets"]["value"] = int(element_text)
                        interface_subinterface_statistics_dict_buffer["outOctets"]["observedAt"] = observed_at
                    lastClear = statistics.get("last-clear")
                    if lastClear is not None:
                        element_text = lastClear
                        interface_subinterface_statistics_dict_buffer["lastClear"] = {}
                        interface_subinterface_statistics_dict_buffer["lastClear"]["type"] = "Property"
                        interface_subinterface_statistics_dict_buffer["lastClear"]["value"] = element_text
                        interface_subinterface_statistics_dict_buffer["lastClear"]["observedAt"] = observed_at
                    dict_buffers.append(interface_subinterface_statistics_dict_buffer)
                bridge_table = subinterface.get("bridge-table")
                if bridge_table is not None and len(bridge_table) != 0:
                    interface_subinterface_bridge_table_dict_buffer = {}
                    interface_subinterface_bridge_table_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceBridgeTable:" + ":".join(interface_subinterface_dict_buffer["id"].split(":")[3:])
                    interface_subinterface_bridge_table_dict_buffer["type"] = "InterfaceSubinterfaceBridgeTable"
                    interface_subinterface_bridge_table_dict_buffer["isPartOf"] = {}
                    interface_subinterface_bridge_table_dict_buffer["isPartOf"]["type"] = "Relationship"
                    interface_subinterface_bridge_table_dict_buffer["isPartOf"]["object"] = interface_subinterface_dict_buffer["id"]
                    interface_subinterface_bridge_table_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    discardUnknownSrcMac = bridge_table.get("discard-unknown-src-mac")
                    if discardUnknownSrcMac is not None:
                        element_text = discardUnknownSrcMac
                        interface_subinterface_bridge_table_dict_buffer["discardUnknownSrcMac"] = {}
                        interface_subinterface_bridge_table_dict_buffer["discardUnknownSrcMac"]["type"] = "Property"
                        interface_subinterface_bridge_table_dict_buffer["discardUnknownSrcMac"]["value"] = eval(str(element_text).capitalize())
                        interface_subinterface_bridge_table_dict_buffer["discardUnknownSrcMac"]["observedAt"] = observed_at
                    mac_limit = bridge_table.get("mac-limit")
                    if mac_limit is not None and len(mac_limit) != 0:
                        interface_subinterface_bridge_table_mac_limit_dict_buffer = {}
                        interface_subinterface_bridge_table_mac_limit_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceBridgeTableMacLimit:" + ":".join(interface_subinterface_bridge_table_dict_buffer["id"].split(":")[3:])
                        interface_subinterface_bridge_table_mac_limit_dict_buffer["type"] = "InterfaceSubinterfaceBridgeTableMacLimit"
                        interface_subinterface_bridge_table_mac_limit_dict_buffer["isPartOf"] = {}
                        interface_subinterface_bridge_table_mac_limit_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_subinterface_bridge_table_mac_limit_dict_buffer["isPartOf"]["object"] = interface_subinterface_bridge_table_dict_buffer["id"]
                        interface_subinterface_bridge_table_mac_limit_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        maximumEntries = mac_limit.get("maximum-entries")
                        if maximumEntries is not None:
                            element_text = maximumEntries
                            interface_subinterface_bridge_table_mac_limit_dict_buffer["maximumEntries"] = {}
                            interface_subinterface_bridge_table_mac_limit_dict_buffer["maximumEntries"]["type"] = "Property"
                            interface_subinterface_bridge_table_mac_limit_dict_buffer["maximumEntries"]["value"] = int(element_text)
                            interface_subinterface_bridge_table_mac_limit_dict_buffer["maximumEntries"]["observedAt"] = observed_at
                        warningThresholdPct = mac_limit.get("warning-threshold-pct")
                        if warningThresholdPct is not None:
                            element_text = warningThresholdPct
                            interface_subinterface_bridge_table_mac_limit_dict_buffer["warningThresholdPct"] = {}
                            interface_subinterface_bridge_table_mac_limit_dict_buffer["warningThresholdPct"]["type"] = "Property"
                            interface_subinterface_bridge_table_mac_limit_dict_buffer["warningThresholdPct"]["value"] = int(element_text)
                            interface_subinterface_bridge_table_mac_limit_dict_buffer["warningThresholdPct"]["observedAt"] = observed_at
                        dict_buffers.append(interface_subinterface_bridge_table_mac_limit_dict_buffer)
                    mac_learning = bridge_table.get("mac-learning")
                    if mac_learning is not None and len(mac_learning) != 0:
                        interface_subinterface_bridge_table_mac_learning_dict_buffer = {}
                        interface_subinterface_bridge_table_mac_learning_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceBridgeTableMacLearning:" + ":".join(interface_subinterface_bridge_table_dict_buffer["id"].split(":")[3:])
                        interface_subinterface_bridge_table_mac_learning_dict_buffer["type"] = "InterfaceSubinterfaceBridgeTableMacLearning"
                        interface_subinterface_bridge_table_mac_learning_dict_buffer["isPartOf"] = {}
                        interface_subinterface_bridge_table_mac_learning_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_subinterface_bridge_table_mac_learning_dict_buffer["isPartOf"]["object"] = interface_subinterface_bridge_table_dict_buffer["id"]
                        interface_subinterface_bridge_table_mac_learning_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        adminState = mac_learning.get("admin-state")
                        if adminState is not None:
                            element_text = adminState
                            interface_subinterface_bridge_table_mac_learning_dict_buffer["adminState"] = {}
                            interface_subinterface_bridge_table_mac_learning_dict_buffer["adminState"]["type"] = "Property"
                            interface_subinterface_bridge_table_mac_learning_dict_buffer["adminState"]["value"] = element_text
                            interface_subinterface_bridge_table_mac_learning_dict_buffer["adminState"]["observedAt"] = observed_at
                        aging = mac_learning.get("aging")
                        if aging is not None and len(aging) != 0:
                            interface_subinterface_bridge_table_mac_learning_aging_dict_buffer = {}
                            interface_subinterface_bridge_table_mac_learning_aging_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceBridgeTableMacLearningAging:" + ":".join(interface_subinterface_bridge_table_mac_learning_dict_buffer["id"].split(":")[3:])
                            interface_subinterface_bridge_table_mac_learning_aging_dict_buffer["type"] = "InterfaceSubinterfaceBridgeTableMacLearningAging"
                            interface_subinterface_bridge_table_mac_learning_aging_dict_buffer["isPartOf"] = {}
                            interface_subinterface_bridge_table_mac_learning_aging_dict_buffer["isPartOf"]["type"] = "Relationship"
                            interface_subinterface_bridge_table_mac_learning_aging_dict_buffer["isPartOf"]["object"] = interface_subinterface_bridge_table_mac_learning_dict_buffer["id"]
                            interface_subinterface_bridge_table_mac_learning_aging_dict_buffer["isPartOf"]["observedAt"] = observed_at
                            adminState = aging.get("admin-state")
                            if adminState is not None:
                                element_text = adminState
                                interface_subinterface_bridge_table_mac_learning_aging_dict_buffer["adminState"] = {}
                                interface_subinterface_bridge_table_mac_learning_aging_dict_buffer["adminState"]["type"] = "Property"
                                interface_subinterface_bridge_table_mac_learning_aging_dict_buffer["adminState"]["value"] = element_text
                                interface_subinterface_bridge_table_mac_learning_aging_dict_buffer["adminState"]["observedAt"] = observed_at
                            dict_buffers.append(interface_subinterface_bridge_table_mac_learning_aging_dict_buffer)
                        dict_buffers.append(interface_subinterface_bridge_table_mac_learning_dict_buffer)
                    mac_duplication = bridge_table.get("mac-duplication")
                    if mac_duplication is not None and len(mac_duplication) != 0:
                        interface_subinterface_bridge_table_mac_duplication_dict_buffer = {}
                        interface_subinterface_bridge_table_mac_duplication_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceBridgeTableMacDuplication:" + ":".join(interface_subinterface_bridge_table_dict_buffer["id"].split(":")[3:])
                        interface_subinterface_bridge_table_mac_duplication_dict_buffer["type"] = "InterfaceSubinterfaceBridgeTableMacDuplication"
                        interface_subinterface_bridge_table_mac_duplication_dict_buffer["isPartOf"] = {}
                        interface_subinterface_bridge_table_mac_duplication_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_subinterface_bridge_table_mac_duplication_dict_buffer["isPartOf"]["object"] = interface_subinterface_bridge_table_dict_buffer["id"]
                        interface_subinterface_bridge_table_mac_duplication_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        action = mac_duplication.get("action")
                        if action is not None:
                            element_text = action
                            interface_subinterface_bridge_table_mac_duplication_dict_buffer["action"] = {}
                            interface_subinterface_bridge_table_mac_duplication_dict_buffer["action"]["type"] = "Property"
                            interface_subinterface_bridge_table_mac_duplication_dict_buffer["action"]["value"] = element_text
                            interface_subinterface_bridge_table_mac_duplication_dict_buffer["action"]["observedAt"] = observed_at
                        dict_buffers.append(interface_subinterface_bridge_table_mac_duplication_dict_buffer)
                    statistics = bridge_table.get("srl_nokia-interfaces-bridge-table-statistics:statistics")
                    if statistics is not None and len(statistics) != 0:
                        interface_subinterface_bridge_table_statistics_dict_buffer = {}
                        interface_subinterface_bridge_table_statistics_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceBridgeTableStatistics:" + ":".join(interface_subinterface_bridge_table_dict_buffer["id"].split(":")[3:])
                        interface_subinterface_bridge_table_statistics_dict_buffer["type"] = "InterfaceSubinterfaceBridgeTableStatistics"
                        interface_subinterface_bridge_table_statistics_dict_buffer["isPartOf"] = {}
                        interface_subinterface_bridge_table_statistics_dict_buffer["isPartOf"]["type"] = "Relationship"
                        interface_subinterface_bridge_table_statistics_dict_buffer["isPartOf"]["object"] = interface_subinterface_bridge_table_dict_buffer["id"]
                        interface_subinterface_bridge_table_statistics_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        activeEntries = statistics.get("active-entries")
                        if activeEntries is not None:
                            element_text = activeEntries
                            interface_subinterface_bridge_table_statistics_dict_buffer["activeEntries"] = {}
                            interface_subinterface_bridge_table_statistics_dict_buffer["activeEntries"]["type"] = "Property"
                            interface_subinterface_bridge_table_statistics_dict_buffer["activeEntries"]["value"] = int(element_text)
                            interface_subinterface_bridge_table_statistics_dict_buffer["activeEntries"]["observedAt"] = observed_at
                        totalEntries = statistics.get("total-entries")
                        if totalEntries is not None:
                            element_text = totalEntries
                            interface_subinterface_bridge_table_statistics_dict_buffer["totalEntries"] = {}
                            interface_subinterface_bridge_table_statistics_dict_buffer["totalEntries"]["type"] = "Property"
                            interface_subinterface_bridge_table_statistics_dict_buffer["totalEntries"]["value"] = int(element_text)
                            interface_subinterface_bridge_table_statistics_dict_buffer["totalEntries"]["observedAt"] = observed_at
                        failedEntries = statistics.get("failed-entries")
                        if failedEntries is not None:
                            element_text = failedEntries
                            interface_subinterface_bridge_table_statistics_dict_buffer["failedEntries"] = {}
                            interface_subinterface_bridge_table_statistics_dict_buffer["failedEntries"]["type"] = "Property"
                            interface_subinterface_bridge_table_statistics_dict_buffer["failedEntries"]["value"] = int(element_text)
                            interface_subinterface_bridge_table_statistics_dict_buffer["failedEntries"]["observedAt"] = observed_at
                        statistics_mac_type = statistics.get("mac-type")
                        if statistics_mac_type is not None and len(statistics_mac_type) != 0:
                            for mac_type in statistics_mac_type:
                                interface_subinterface_bridge_table_statistics_mac_type_dict_buffer = {}
                                interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSubinterfaceBridgeTableStatisticsMacType:" + ":".join(interface_subinterface_bridge_table_statistics_dict_buffer["id"].split(":")[3:])
                                interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["type"] = "InterfaceSubinterfaceBridgeTableStatisticsMacType"
                                interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["isPartOf"] = {}
                                interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["isPartOf"]["type"] = "Relationship"
                                interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["isPartOf"]["object"] = interface_subinterface_bridge_table_statistics_dict_buffer["id"]
                                interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                type = mac_type.get("type")
                                if type is not None:
                                    element_text = type
                                    interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["type"] = {}
                                    interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["type"]["type"] = "Property"
                                    interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["type"]["value"] = element_text
                                    interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["type"]["observedAt"] = observed_at
                                activeEntries = mac_type.get("active-entries")
                                if activeEntries is not None:
                                    element_text = activeEntries
                                    interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["activeEntries"] = {}
                                    interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["activeEntries"]["type"] = "Property"
                                    interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["activeEntries"]["value"] = int(element_text)
                                    interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["activeEntries"]["observedAt"] = observed_at
                                totalEntries = mac_type.get("total-entries")
                                if totalEntries is not None:
                                    element_text = totalEntries
                                    interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["totalEntries"] = {}
                                    interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["totalEntries"]["type"] = "Property"
                                    interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["totalEntries"]["value"] = int(element_text)
                                    interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["totalEntries"]["observedAt"] = observed_at
                                failedEntries = mac_type.get("failed-entries")
                                if failedEntries is not None:
                                    element_text = failedEntries
                                    interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["failedEntries"] = {}
                                    interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["failedEntries"]["type"] = "Property"
                                    interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["failedEntries"]["value"] = int(element_text)
                                    interface_subinterface_bridge_table_statistics_mac_type_dict_buffer["failedEntries"]["observedAt"] = observed_at
                                dict_buffers.append(interface_subinterface_bridge_table_statistics_mac_type_dict_buffer)
                        dict_buffers.append(interface_subinterface_bridge_table_statistics_dict_buffer)
                    dict_buffers.append(interface_subinterface_bridge_table_dict_buffer)
                dict_buffers.append(interface_subinterface_dict_buffer)
        sflow = interface.get("sflow")
        if sflow is not None and len(sflow) != 0:
            interface_sflow_dict_buffer = {}
            interface_sflow_dict_buffer["id"] = "urn:ngsi-ld:InterfaceSflow:" + ":".join(interface_dict_buffer["id"].split(":")[3:])
            interface_sflow_dict_buffer["type"] = "InterfaceSflow"
            interface_sflow_dict_buffer["isPartOf"] = {}
            interface_sflow_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_sflow_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
            interface_sflow_dict_buffer["isPartOf"]["observedAt"] = observed_at
            adminState = sflow.get("admin-state")
            if adminState is not None:
                element_text = adminState
                interface_sflow_dict_buffer["adminState"] = {}
                interface_sflow_dict_buffer["adminState"]["type"] = "Property"
                interface_sflow_dict_buffer["adminState"]["value"] = element_text
                interface_sflow_dict_buffer["adminState"]["observedAt"] = observed_at
            dict_buffers.append(interface_sflow_dict_buffer)
        dict_buffers.append(interface_dict_buffer)
platform = None
if json_data.get("platform")is not None:
    platform = json_data.get("platform")
elif json_data.get("srl_nokia-platform:platform")is not None:
    platform = json_data.get("srl_nokia-platform:platform")
if platform is not None and len(platform) != 0:
    if "linecard" in list(platform.keys()):
        platform = platform.get("linecard")
    elif "srl_nokia-platform-lc:linecard" in list(platform.keys()):
        platform = platform.get("srl_nokia-platform-lc:linecard")
    for linecard in platform:
        if linecard is not None and len(linecard) != 0:
            linecard_dict_buffer = {}
            linecard_dict_buffer["id"] = "urn:ngsi-ld:Linecard:" + source
            linecard_dict_buffer["type"] = "Linecard"
            slot = linecard.get("srl_nokia-platform-lc:slot")
            if slot is not None:
                element_text = slot
                linecard_dict_buffer["slot"] = {}
                linecard_dict_buffer["slot"]["type"] = "Property"
                linecard_dict_buffer["slot"]["value"] = int(element_text)
                linecard_dict_buffer["slot"]["observedAt"] = observed_at
            adminState = linecard.get("srl_nokia-platform-lc:admin-state")
            if adminState is not None:
                element_text = adminState
                linecard_dict_buffer["adminState"] = {}
                linecard_dict_buffer["adminState"]["type"] = "Property"
                linecard_dict_buffer["adminState"]["value"] = element_text
                linecard_dict_buffer["adminState"]["observedAt"] = observed_at
            operState = linecard.get("srl_nokia-platform-lc:oper-state")
            if operState is not None:
                element_text = operState
                linecard_dict_buffer["operState"] = {}
                linecard_dict_buffer["operState"]["type"] = "Property"
                linecard_dict_buffer["operState"]["value"] = element_text
                linecard_dict_buffer["operState"]["observedAt"] = observed_at
            lastBooted = linecard.get("srl_nokia-platform-lc:last-booted")
            if lastBooted is not None:
                element_text = lastBooted
                linecard_dict_buffer["lastBooted"] = {}
                linecard_dict_buffer["lastBooted"]["type"] = "Property"
                linecard_dict_buffer["lastBooted"]["value"] = element_text
                linecard_dict_buffer["lastBooted"]["observedAt"] = observed_at
            lastBootedReason = linecard.get("last-booted-reason")
            if lastBootedReason is not None and len(lastBootedReason) != 0:
                element_text = lastBootedReason
                if element_text is not None:
                    linecard_dict_buffer["lastBootedReason"] = {}
                    linecard_dict_buffer["lastBootedReason"]["type"] = "Relationship"
                    linecard_dict_buffer["lastBootedReason"]["object"] = "urn:ngsi-ld:YANGIdentity:" + element_text
                    linecard_dict_buffer["lastBootedReason"]["observedAt"] = observed_at
            lastChange = linecard.get("srl_nokia-platform-lc:last-change")
            if lastChange is not None:
                element_text = lastChange
                linecard_dict_buffer["lastChange"] = {}
                linecard_dict_buffer["lastChange"]["type"] = "Property"
                linecard_dict_buffer["lastChange"]["value"] = element_text
                linecard_dict_buffer["lastChange"]["observedAt"] = observed_at
            partNumber = linecard.get("srl_nokia-platform-lc:part-number")
            if partNumber is not None:
                element_text = partNumber
                linecard_dict_buffer["partNumber"] = {}
                linecard_dict_buffer["partNumber"]["type"] = "Property"
                linecard_dict_buffer["partNumber"]["value"] = element_text
                linecard_dict_buffer["partNumber"]["observedAt"] = observed_at
            removable = linecard.get("srl_nokia-platform-lc:removable")
            if removable is not None:
                element_text = removable
                linecard_dict_buffer["removable"] = {}
                linecard_dict_buffer["removable"]["type"] = "Property"
                linecard_dict_buffer["removable"]["value"] = eval(str(element_text).capitalize())
                linecard_dict_buffer["removable"]["observedAt"] = observed_at
            failureReason = linecard.get("srl_nokia-platform-lc:failure-reason")
            if failureReason is not None:
                element_text = failureReason
                linecard_dict_buffer["failureReason"] = {}
                linecard_dict_buffer["failureReason"]["type"] = "Property"
                linecard_dict_buffer["failureReason"]["value"] = element_text
                linecard_dict_buffer["failureReason"]["observedAt"] = observed_at
            cleiCode = linecard.get("srl_nokia-platform-lc:clei-code")
            if cleiCode is not None:
                element_text = cleiCode
                linecard_dict_buffer["cleiCode"] = {}
                linecard_dict_buffer["cleiCode"]["type"] = "Property"
                linecard_dict_buffer["cleiCode"]["value"] = element_text
                linecard_dict_buffer["cleiCode"]["observedAt"] = observed_at
            serialNumber = linecard.get("srl_nokia-platform-lc:serial-number")
            if serialNumber is not None:
                element_text = serialNumber
                linecard_dict_buffer["serialNumber"] = {}
                linecard_dict_buffer["serialNumber"]["type"] = "Property"
                linecard_dict_buffer["serialNumber"]["value"] = element_text
                linecard_dict_buffer["serialNumber"]["observedAt"] = observed_at
            manufacturedDate = linecard.get("srl_nokia-platform-lc:manufactured-date")
            if manufacturedDate is not None:
                element_text = manufacturedDate
                linecard_dict_buffer["manufacturedDate"] = {}
                linecard_dict_buffer["manufacturedDate"]["type"] = "Property"
                linecard_dict_buffer["manufacturedDate"]["value"] = element_text
                linecard_dict_buffer["manufacturedDate"]["observedAt"] = observed_at
            bios = linecard.get("srl_nokia-platform-lc:bios")
            if bios is not None and len(bios) != 0:
                linecard_bios_dict_buffer = {}
                linecard_bios_dict_buffer["id"] = "urn:ngsi-ld:LinecardBios:" + ":".join(linecard_dict_buffer["id"].split(":")[3:])
                linecard_bios_dict_buffer["type"] = "LinecardBios"
                linecard_bios_dict_buffer["isPartOf"] = {}
                linecard_bios_dict_buffer["isPartOf"]["type"] = "Relationship"
                linecard_bios_dict_buffer["isPartOf"]["object"] = linecard_dict_buffer["id"]
                linecard_bios_dict_buffer["isPartOf"]["observedAt"] = observed_at
                manufacturer = bios.get("manufacturer")
                if manufacturer is not None:
                    element_text = manufacturer
                    linecard_bios_dict_buffer["manufacturer"] = {}
                    linecard_bios_dict_buffer["manufacturer"]["type"] = "Property"
                    linecard_bios_dict_buffer["manufacturer"]["value"] = element_text
                    linecard_bios_dict_buffer["manufacturer"]["observedAt"] = observed_at
                softwareVersion = bios.get("software-version")
                if softwareVersion is not None:
                    element_text = softwareVersion
                    linecard_bios_dict_buffer["softwareVersion"] = {}
                    linecard_bios_dict_buffer["softwareVersion"]["type"] = "Property"
                    linecard_bios_dict_buffer["softwareVersion"]["value"] = element_text
                    linecard_bios_dict_buffer["softwareVersion"]["observedAt"] = observed_at
                dict_buffers.append(linecard_bios_dict_buffer)
            rebootingAt = linecard.get("srl_nokia-platform-lc:rebooting-at")
            if rebootingAt is not None:
                element_text = rebootingAt
                linecard_dict_buffer["rebootingAt"] = {}
                linecard_dict_buffer["rebootingAt"]["type"] = "Property"
                linecard_dict_buffer["rebootingAt"]["value"] = element_text
                linecard_dict_buffer["rebootingAt"]["observedAt"] = observed_at
            type = linecard.get("srl_nokia-platform-lc:type")
            if type is not None:
                element_text = type
                linecard_dict_buffer["type"] = {}
                linecard_dict_buffer["type"]["type"] = "Property"
                linecard_dict_buffer["type"]["value"] = element_text
                linecard_dict_buffer["type"]["observedAt"] = observed_at
            linecard_forwarding_complex = linecard.get("srl_nokia-platform-lc:forwarding-complex")
            if linecard_forwarding_complex is not None and len(linecard_forwarding_complex) != 0:
                for forwarding_complex in linecard_forwarding_complex:
                    linecard_forwarding_complex_dict_buffer = {}
                    linecard_forwarding_complex_dict_buffer["id"] = "urn:ngsi-ld:LinecardForwardingComplex:" + ":".join(linecard_dict_buffer["id"].split(":")[3:])
                    linecard_forwarding_complex_dict_buffer["type"] = "LinecardForwardingComplex"
                    linecard_forwarding_complex_dict_buffer["isPartOf"] = {}
                    linecard_forwarding_complex_dict_buffer["isPartOf"]["type"] = "Relationship"
                    linecard_forwarding_complex_dict_buffer["isPartOf"]["object"] = linecard_dict_buffer["id"]
                    linecard_forwarding_complex_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    name = forwarding_complex.get("name")
                    if name is not None:
                        element_text = name
                        if linecard_forwarding_complex_dict_buffer["id"].split(":")[-1] != element_text:
                            linecard_forwarding_complex_dict_buffer["id"] = linecard_forwarding_complex_dict_buffer["id"] + ":" + element_text
                        linecard_forwarding_complex_dict_buffer["name"] = {}
                        linecard_forwarding_complex_dict_buffer["name"]["type"] = "Property"
                        linecard_forwarding_complex_dict_buffer["name"]["value"] = element_text
                        linecard_forwarding_complex_dict_buffer["name"]["observedAt"] = observed_at
                    interfaces = forwarding_complex.get("interfaces")
                    if interfaces is not None:
                        element_text = interfaces
                        linecard_forwarding_complex_dict_buffer["interfaces"] = {}
                        linecard_forwarding_complex_dict_buffer["interfaces"]["type"] = "Property"
                        linecard_forwarding_complex_dict_buffer["interfaces"]["value"] = element_text
                        linecard_forwarding_complex_dict_buffer["interfaces"]["observedAt"] = observed_at
                    operState = forwarding_complex.get("oper-state")
                    if operState is not None:
                        element_text = operState
                        linecard_forwarding_complex_dict_buffer["operState"] = {}
                        linecard_forwarding_complex_dict_buffer["operState"]["type"] = "Property"
                        linecard_forwarding_complex_dict_buffer["operState"]["value"] = element_text
                        linecard_forwarding_complex_dict_buffer["operState"]["observedAt"] = observed_at
                    lastBooted = forwarding_complex.get("last-booted")
                    if lastBooted is not None:
                        element_text = lastBooted
                        linecard_forwarding_complex_dict_buffer["lastBooted"] = {}
                        linecard_forwarding_complex_dict_buffer["lastBooted"]["type"] = "Property"
                        linecard_forwarding_complex_dict_buffer["lastBooted"]["value"] = element_text
                        linecard_forwarding_complex_dict_buffer["lastBooted"]["observedAt"] = observed_at
                    lastBootedReason = forwarding_complex.get("last-booted-reason")
                    if lastBootedReason is not None and len(lastBootedReason) != 0:
                        element_text = lastBootedReason
                        if element_text is not None:
                            linecard_forwarding_complex_dict_buffer["lastBootedReason"] = {}
                            linecard_forwarding_complex_dict_buffer["lastBootedReason"]["type"] = "Relationship"
                            linecard_forwarding_complex_dict_buffer["lastBootedReason"]["object"] = "urn:ngsi-ld:YANGIdentity:" + element_text
                            linecard_forwarding_complex_dict_buffer["lastBootedReason"]["observedAt"] = observed_at
                    lastChange = forwarding_complex.get("last-change")
                    if lastChange is not None:
                        element_text = lastChange
                        linecard_forwarding_complex_dict_buffer["lastChange"] = {}
                        linecard_forwarding_complex_dict_buffer["lastChange"]["type"] = "Property"
                        linecard_forwarding_complex_dict_buffer["lastChange"]["value"] = element_text
                        linecard_forwarding_complex_dict_buffer["lastChange"]["observedAt"] = observed_at
                    partNumber = forwarding_complex.get("part-number")
                    if partNumber is not None:
                        element_text = partNumber
                        linecard_forwarding_complex_dict_buffer["partNumber"] = {}
                        linecard_forwarding_complex_dict_buffer["partNumber"]["type"] = "Property"
                        linecard_forwarding_complex_dict_buffer["partNumber"]["value"] = element_text
                        linecard_forwarding_complex_dict_buffer["partNumber"]["observedAt"] = observed_at
                    removable = forwarding_complex.get("removable")
                    if removable is not None:
                        element_text = removable
                        linecard_forwarding_complex_dict_buffer["removable"] = {}
                        linecard_forwarding_complex_dict_buffer["removable"]["type"] = "Property"
                        linecard_forwarding_complex_dict_buffer["removable"]["value"] = eval(str(element_text).capitalize())
                        linecard_forwarding_complex_dict_buffer["removable"]["observedAt"] = observed_at
                    fabric = forwarding_complex.get("fabric")
                    if fabric is not None and len(fabric) != 0:
                        linecard_forwarding_complex_fabric_dict_buffer = {}
                        linecard_forwarding_complex_fabric_dict_buffer["id"] = "urn:ngsi-ld:LinecardForwardingComplexFabric:" + ":".join(linecard_forwarding_complex_dict_buffer["id"].split(":")[3:])
                        linecard_forwarding_complex_fabric_dict_buffer["type"] = "LinecardForwardingComplexFabric"
                        linecard_forwarding_complex_fabric_dict_buffer["isPartOf"] = {}
                        linecard_forwarding_complex_fabric_dict_buffer["isPartOf"]["type"] = "Relationship"
                        linecard_forwarding_complex_fabric_dict_buffer["isPartOf"]["object"] = linecard_forwarding_complex_dict_buffer["id"]
                        linecard_forwarding_complex_fabric_dict_buffer["isPartOf"]["observedAt"] = observed_at
                        availability = fabric.get("availability")
                        if availability is not None:
                            element_text = availability
                            linecard_forwarding_complex_fabric_dict_buffer["availability"] = {}
                            linecard_forwarding_complex_fabric_dict_buffer["availability"]["type"] = "Property"
                            linecard_forwarding_complex_fabric_dict_buffer["availability"]["value"] = int(element_text)
                            linecard_forwarding_complex_fabric_dict_buffer["availability"]["observedAt"] = observed_at
                        utilizationIngress = fabric.get("utilization-ingress")
                        if utilizationIngress is not None:
                            element_text = utilizationIngress
                            linecard_forwarding_complex_fabric_dict_buffer["utilizationIngress"] = {}
                            linecard_forwarding_complex_fabric_dict_buffer["utilizationIngress"]["type"] = "Property"
                            linecard_forwarding_complex_fabric_dict_buffer["utilizationIngress"]["value"] = int(element_text)
                            linecard_forwarding_complex_fabric_dict_buffer["utilizationIngress"]["observedAt"] = observed_at
                        utilizationEgress = fabric.get("utilization-egress")
                        if utilizationEgress is not None:
                            element_text = utilizationEgress
                            linecard_forwarding_complex_fabric_dict_buffer["utilizationEgress"] = {}
                            linecard_forwarding_complex_fabric_dict_buffer["utilizationEgress"]["type"] = "Property"
                            linecard_forwarding_complex_fabric_dict_buffer["utilizationEgress"]["value"] = int(element_text)
                            linecard_forwarding_complex_fabric_dict_buffer["utilizationEgress"]["observedAt"] = observed_at
                        dict_buffers.append(linecard_forwarding_complex_fabric_dict_buffer)
                    forwarding_complex_pipeline = forwarding_complex.get("pipeline")
                    if forwarding_complex_pipeline is not None and len(forwarding_complex_pipeline) != 0:
                        for pipeline in forwarding_complex_pipeline:
                            linecard_forwarding_complex_pipeline_dict_buffer = {}
                            linecard_forwarding_complex_pipeline_dict_buffer["id"] = "urn:ngsi-ld:LinecardForwardingComplexPipeline:" + ":".join(linecard_forwarding_complex_dict_buffer["id"].split(":")[3:])
                            linecard_forwarding_complex_pipeline_dict_buffer["type"] = "LinecardForwardingComplexPipeline"
                            linecard_forwarding_complex_pipeline_dict_buffer["isPartOf"] = {}
                            linecard_forwarding_complex_pipeline_dict_buffer["isPartOf"]["type"] = "Relationship"
                            linecard_forwarding_complex_pipeline_dict_buffer["isPartOf"]["object"] = linecard_forwarding_complex_dict_buffer["id"]
                            linecard_forwarding_complex_pipeline_dict_buffer["isPartOf"]["observedAt"] = observed_at
                            index = pipeline.get("index")
                            if index is not None:
                                element_text = index
                                if "." + str(element_text) not in linecard_forwarding_complex_pipeline_dict_buffer["id"].split(":")[-1]:
                                    linecard_forwarding_complex_pipeline_dict_buffer["id"] = linecard_forwarding_complex_pipeline_dict_buffer["id"] + "." + str(element_text)
                                linecard_forwarding_complex_pipeline_dict_buffer["index"] = {}
                                linecard_forwarding_complex_pipeline_dict_buffer["index"]["type"] = "Property"
                                linecard_forwarding_complex_pipeline_dict_buffer["index"]["value"] = element_text
                                linecard_forwarding_complex_pipeline_dict_buffer["index"]["observedAt"] = observed_at
                            pipeline_counters = pipeline.get("pipeline-counters")
                            if pipeline_counters is not None and len(pipeline_counters) != 0:
                                host_interface_block = pipeline_counters.get("host-interface-block")
                                if host_interface_block is not None and len(host_interface_block) != 0:
                                    packet_extraction = host_interface_block.get("packet-extraction")
                                    if packet_extraction is not None and len(packet_extraction) != 0:
                                        linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer = {}
                                        linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["id"] = "urn:ngsi-ld:LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtraction:" + ":".join(linecard_forwarding_complex_pipeline_dict_buffer["id"].split(":")[3:])
                                        linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["type"] = "LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtraction"
                                        linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["isPartOf"] = {}
                                        linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["isPartOf"]["type"] = "Relationship"
                                        linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["isPartOf"]["object"] = linecard_forwarding_complex_pipeline_dict_buffer["id"]
                                        linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                        extractedPackets = packet_extraction.get("extracted-packets")
                                        if extractedPackets is not None:
                                            element_text = extractedPackets
                                            linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["extractedPackets"] = {}
                                            linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["extractedPackets"]["type"] = "Property"
                                            linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["extractedPackets"]["value"] = int(element_text)
                                            linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["extractedPackets"]["observedAt"] = observed_at
                                        extractedOctets = packet_extraction.get("extracted-octets")
                                        if extractedOctets is not None:
                                            element_text = extractedOctets
                                            linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["extractedOctets"] = {}
                                            linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["extractedOctets"]["type"] = "Property"
                                            linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["extractedOctets"]["value"] = int(element_text)
                                            linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["extractedOctets"]["observedAt"] = observed_at
                                        packet_extraction_extraction_reason = packet_extraction.get("extraction-reason")
                                        if packet_extraction_extraction_reason is not None and len(packet_extraction_extraction_reason) != 0:
                                            for extraction_reason in packet_extraction_extraction_reason:
                                                linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer = {}
                                                linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["id"] = "urn:ngsi-ld:LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtractionExtractionReason:" + ":".join(linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["id"].split(":")[3:])
                                                linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["type"] = "LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtractionExtractionReason"
                                                linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["isPartOf"] = {}
                                                linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["isPartOf"]["type"] = "Relationship"
                                                linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["isPartOf"]["object"] = linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer["id"]
                                                linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["isPartOf"]["observedAt"] = observed_at
                                                reason = extraction_reason.get("reason")
                                                if reason is not None and len(reason) != 0:
                                                    element_text = reason
                                                    if element_text is not None:
                                                        linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["reason"] = {}
                                                        linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["reason"]["type"] = "Relationship"
                                                        linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["reason"]["object"] = "urn:ngsi-ld:YANGIdentity:" + element_text
                                                        linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["reason"]["observedAt"] = observed_at
                                                extractedPackets = extraction_reason.get("extracted-packets")
                                                if extractedPackets is not None:
                                                    element_text = extractedPackets
                                                    linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["extractedPackets"] = {}
                                                    linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["extractedPackets"]["type"] = "Property"
                                                    linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["extractedPackets"]["value"] = int(element_text)
                                                    linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["extractedPackets"]["observedAt"] = observed_at
                                                extractedOctets = extraction_reason.get("extracted-octets")
                                                if extractedOctets is not None:
                                                    element_text = extractedOctets
                                                    linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["extractedOctets"] = {}
                                                    linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["extractedOctets"]["type"] = "Property"
                                                    linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["extractedOctets"]["value"] = int(element_text)
                                                    linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer["extractedOctets"]["observedAt"] = observed_at
                                                dict_buffers.append(linecard_forwarding_complex_pipeline_packet_extraction_extraction_reason_dict_buffer)
                                        dict_buffers.append(linecard_forwarding_complex_pipeline_packet_extraction_dict_buffer)
                            dict_buffers.append(linecard_forwarding_complex_pipeline_dict_buffer)
                    dict_buffers.append(linecard_forwarding_complex_dict_buffer)
            softwareVersion = linecard.get("software-version")
            if softwareVersion is not None:
                element_text = softwareVersion
                linecard_dict_buffer["softwareVersion"] = {}
                linecard_dict_buffer["softwareVersion"]["type"] = "Property"
                linecard_dict_buffer["softwareVersion"]["value"] = element_text
                linecard_dict_buffer["softwareVersion"]["observedAt"] = observed_at
            locatorState = linecard.get("srl_nokia-platform-lc:locator-state")
            if locatorState is not None:
                element_text = locatorState
                linecard_dict_buffer["locatorState"] = {}
                linecard_dict_buffer["locatorState"]["type"] = "Property"
                linecard_dict_buffer["locatorState"]["value"] = element_text
                linecard_dict_buffer["locatorState"]["observedAt"] = observed_at
            power = linecard.get("srl_nokia-platform-lc:power")
            if power is not None and len(power) != 0:
                linecard_power_dict_buffer = {}
                linecard_power_dict_buffer["id"] = "urn:ngsi-ld:LinecardPower:" + ":".join(linecard_dict_buffer["id"].split(":")[3:])
                linecard_power_dict_buffer["type"] = "LinecardPower"
                linecard_power_dict_buffer["isPartOf"] = {}
                linecard_power_dict_buffer["isPartOf"]["type"] = "Relationship"
                linecard_power_dict_buffer["isPartOf"]["object"] = linecard_dict_buffer["id"]
                linecard_power_dict_buffer["isPartOf"]["observedAt"] = observed_at
                allocated = power.get("allocated")
                if allocated is not None:
                    element_text = allocated
                    linecard_power_dict_buffer["allocated"] = {}
                    linecard_power_dict_buffer["allocated"]["type"] = "Property"
                    linecard_power_dict_buffer["allocated"]["value"] = int(element_text)
                    linecard_power_dict_buffer["allocated"]["observedAt"] = observed_at
                used = power.get("used")
                if used is not None:
                    element_text = used
                    linecard_power_dict_buffer["used"] = {}
                    linecard_power_dict_buffer["used"]["type"] = "Property"
                    linecard_power_dict_buffer["used"]["value"] = int(element_text)
                    linecard_power_dict_buffer["used"]["observedAt"] = observed_at
                required = power.get("required")
                if required is not None:
                    element_text = required
                    linecard_power_dict_buffer["required"] = {}
                    linecard_power_dict_buffer["required"]["type"] = "Property"
                    linecard_power_dict_buffer["required"]["value"] = int(element_text)
                    linecard_power_dict_buffer["required"]["observedAt"] = observed_at
                dict_buffers.append(linecard_power_dict_buffer)
            temperature = linecard.get("srl_nokia-platform-lc:temperature")
            if temperature is not None and len(temperature) != 0:
                linecard_temperature_dict_buffer = {}
                linecard_temperature_dict_buffer["id"] = "urn:ngsi-ld:LinecardTemperature:" + ":".join(linecard_dict_buffer["id"].split(":")[3:])
                linecard_temperature_dict_buffer["type"] = "LinecardTemperature"
                linecard_temperature_dict_buffer["isPartOf"] = {}
                linecard_temperature_dict_buffer["isPartOf"]["type"] = "Relationship"
                linecard_temperature_dict_buffer["isPartOf"]["object"] = linecard_dict_buffer["id"]
                linecard_temperature_dict_buffer["isPartOf"]["observedAt"] = observed_at
                instant = temperature.get("instant")
                if instant is not None:
                    element_text = instant
                    linecard_temperature_dict_buffer["instant"] = {}
                    linecard_temperature_dict_buffer["instant"]["type"] = "Property"
                    linecard_temperature_dict_buffer["instant"]["value"] = int(element_text)
                    linecard_temperature_dict_buffer["instant"]["observedAt"] = observed_at
                maximum = temperature.get("maximum")
                if maximum is not None:
                    element_text = maximum
                    linecard_temperature_dict_buffer["maximum"] = {}
                    linecard_temperature_dict_buffer["maximum"]["type"] = "Property"
                    linecard_temperature_dict_buffer["maximum"]["value"] = int(element_text)
                    linecard_temperature_dict_buffer["maximum"]["observedAt"] = observed_at
                maximumTime = temperature.get("maximum-time")
                if maximumTime is not None:
                    element_text = maximumTime
                    linecard_temperature_dict_buffer["maximumTime"] = {}
                    linecard_temperature_dict_buffer["maximumTime"]["type"] = "Property"
                    linecard_temperature_dict_buffer["maximumTime"]["value"] = element_text
                    linecard_temperature_dict_buffer["maximumTime"]["observedAt"] = observed_at
                alarmStatus = temperature.get("alarm-status")
                if alarmStatus is not None:
                    element_text = alarmStatus
                    linecard_temperature_dict_buffer["alarmStatus"] = {}
                    linecard_temperature_dict_buffer["alarmStatus"]["type"] = "Property"
                    linecard_temperature_dict_buffer["alarmStatus"]["value"] = eval(str(element_text).capitalize())
                    linecard_temperature_dict_buffer["alarmStatus"]["observedAt"] = observed_at
                margin = temperature.get("margin")
                if margin is not None:
                    element_text = margin
                    linecard_temperature_dict_buffer["margin"] = {}
                    linecard_temperature_dict_buffer["margin"]["type"] = "Property"
                    linecard_temperature_dict_buffer["margin"]["value"] = int(element_text)
                    linecard_temperature_dict_buffer["margin"]["observedAt"] = observed_at
                dict_buffers.append(linecard_temperature_dict_buffer)
            dict_buffers.append(linecard_dict_buffer)

output_file = open("dict_buffers_queries.json", 'w')
output_file.write(json.dumps(dict_buffers[::-1], indent=4))
output_file.close()
dict_buffers.clear()
