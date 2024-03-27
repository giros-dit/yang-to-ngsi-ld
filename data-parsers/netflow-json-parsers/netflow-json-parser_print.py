import json
import numpy as np
from datetime import datetime
import sys

json_payload = sys.argv[1]
dict_buffers = []
with open(json_payload) as f:
    data = json.load(f)
    timestamp = data["netflow-v9:netflow"]["collector-goflow2"]["time-received"]
    timestamp_sec = int(timestamp) / 1000.0
    datetime_ms = datetime.fromtimestamp(timestamp_sec)
    observed_at = str(datetime_ms)[:-3] + 'Z'

if data.get("netflow")is not None:
    netflow = data.get("netflow")
elif data.get("netflow-v9:netflow")is not None:
    netflow = data.get("netflow-v9:netflow")
if netflow is not None and len(netflow) != 0:
    collector_goflow2 = netflow.get("collector-goflow2")
    if collector_goflow2 is not None and len(collector_goflow2) != 0:
        collector_goflow2_dict_buffer = {}
        collector_goflow2_dict_buffer["id"] = "urn:ngsi-ld:CollectorGoflow2"
        collector_goflow2_dict_buffer["type"] = "CollectorGoflow2"
        timeReceived = collector_goflow2.get("time-received")
        if timeReceived is not None:
            element_text = timeReceived
            collector_goflow2_dict_buffer["timeReceived"] = {}
            collector_goflow2_dict_buffer["timeReceived"]["type"] = "Property"
            collector_goflow2_dict_buffer["timeReceived"]["value"] = int(element_text)
            collector_goflow2_dict_buffer["timeReceived"]["observedAt"] = observed_at
        samplerAddress = collector_goflow2.get("sampler-address")
        if samplerAddress is not None:
            element_text = samplerAddress
            if collector_goflow2_dict_buffer["id"].split(":")[-1] != element_text:
                collector_goflow2_dict_buffer["id"] = collector_goflow2_dict_buffer["id"] + ":" + str(element_text)
            collector_goflow2_dict_buffer["samplerAddress"] = {}
            collector_goflow2_dict_buffer["samplerAddress"]["type"] = "Property"
            collector_goflow2_dict_buffer["samplerAddress"]["value"] = element_text
            collector_goflow2_dict_buffer["samplerAddress"]["observedAt"] = observed_at
        samplerAddressIpv6 = collector_goflow2.get("sampler-address-ipv6")
        if samplerAddressIpv6 is not None:
            element_text = samplerAddressIpv6
            if collector_goflow2_dict_buffer["id"].split(":")[-1] != element_text:
                collector_goflow2_dict_buffer["id"] = collector_goflow2_dict_buffer["id"] + ":" + str(element_text)
            collector_goflow2_dict_buffer["samplerAddressIpv6"] = {}
            collector_goflow2_dict_buffer["samplerAddressIpv6"]["type"] = "Property"
            collector_goflow2_dict_buffer["samplerAddressIpv6"]["value"] = element_text
            collector_goflow2_dict_buffer["samplerAddressIpv6"]["observedAt"] = observed_at
        dict_buffers.append(collector_goflow2_dict_buffer)
if data.get("netflow")is not None:
    netflow = data.get("netflow")
elif data.get("netflow-v9:netflow")is not None:
    netflow = data.get("netflow-v9:netflow")
if netflow is not None and len(netflow) != 0:
    export_packet = netflow.get("export-packet")
    if export_packet is not None and len(export_packet) != 0:
        export_packet_dict_buffer = {}
        export_packet_dict_buffer["id"] = "urn:ngsi-ld:ExportPacket"
        export_packet_dict_buffer["type"] = "ExportPacket"
        sequenceNumber = export_packet.get("sequence-number")
        if sequenceNumber is not None:
            element_text = sequenceNumber
            if export_packet_dict_buffer["id"].split(":")[-1] != int(element_text):
                export_packet_dict_buffer["id"] = export_packet_dict_buffer["id"] + ":" + str(element_text)
            export_packet_dict_buffer["sequenceNumber"] = {}
            export_packet_dict_buffer["sequenceNumber"]["type"] = "Property"
            export_packet_dict_buffer["sequenceNumber"]["value"] = int(element_text)
            export_packet_dict_buffer["sequenceNumber"]["observedAt"] = observed_at
        count = export_packet.get("count")
        if count is not None:
            element_text = count
            export_packet_dict_buffer["count"] = {}
            export_packet_dict_buffer["count"]["type"] = "Property"
            export_packet_dict_buffer["count"]["value"] = int(element_text)
            export_packet_dict_buffer["count"]["observedAt"] = observed_at
        systemUptime = export_packet.get("system-uptime")
        if systemUptime is not None:
            element_text = systemUptime
            export_packet_dict_buffer["systemUptime"] = {}
            export_packet_dict_buffer["systemUptime"]["type"] = "Property"
            export_packet_dict_buffer["systemUptime"]["value"] = int(element_text)
            export_packet_dict_buffer["systemUptime"]["observedAt"] = observed_at
        unixSeconds = export_packet.get("unix-seconds")
        if unixSeconds is not None:
            element_text = unixSeconds
            export_packet_dict_buffer["unixSeconds"] = {}
            export_packet_dict_buffer["unixSeconds"]["type"] = "Property"
            export_packet_dict_buffer["unixSeconds"]["value"] = int(element_text)
            export_packet_dict_buffer["unixSeconds"]["observedAt"] = observed_at
        sourceId = export_packet.get("source-id")
        if sourceId is not None:
            element_text = sourceId
            if export_packet_dict_buffer["id"].split(":")[3] != int(element_text):
                export_packet_dict_buffer["id"] = ":".join(export_packet_dict_buffer["id"].split(":")[:3]) + ":" + str(element_text) + ":" + ":".join(export_packet_dict_buffer["id"].split(":")[3:])
            export_packet_dict_buffer["sourceId"] = {}
            export_packet_dict_buffer["sourceId"]["type"] = "Property"
            export_packet_dict_buffer["sourceId"]["value"] = int(element_text)
            export_packet_dict_buffer["sourceId"]["observedAt"] = observed_at
        export_packet_flow_data_record = export_packet.get("flow-data-record")
        if export_packet_flow_data_record is not None and len(export_packet_flow_data_record) != 0:
            for flow_data_record in export_packet_flow_data_record:
                export_packet_flow_data_record_dict_buffer = {}
                export_packet_flow_data_record_dict_buffer["id"] = "urn:ngsi-ld:ExportPacketFlowDataRecord:" + ":".join(export_packet_dict_buffer["id"].split(":")[3:])
                export_packet_flow_data_record_dict_buffer["type"] = "ExportPacketFlowDataRecord"
                export_packet_flow_data_record_dict_buffer["isPartOf"] = {}
                export_packet_flow_data_record_dict_buffer["isPartOf"]["type"] = "Relationship"
                export_packet_flow_data_record_dict_buffer["isPartOf"]["object"] = export_packet_dict_buffer["id"]
                export_packet_flow_data_record_dict_buffer["isPartOf"]["observedAt"] = observed_at
                flowId = flow_data_record.get("flow-id")
                if flowId is not None:
                    element_text = flowId
                    if export_packet_flow_data_record_dict_buffer["id"].split(":")[-1] != int(element_text):
                        export_packet_flow_data_record_dict_buffer["id"] = export_packet_flow_data_record_dict_buffer["id"] + ":" + str(element_text)
                    export_packet_flow_data_record_dict_buffer["flowId"] = {}
                    export_packet_flow_data_record_dict_buffer["flowId"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["flowId"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["flowId"]["observedAt"] = observed_at
                bytesIn = flow_data_record.get("bytes-in")
                if bytesIn is not None:
                    element_text = bytesIn
                    export_packet_flow_data_record_dict_buffer["bytesIn"] = {}
                    export_packet_flow_data_record_dict_buffer["bytesIn"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["bytesIn"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["bytesIn"]["observedAt"] = observed_at
                bytesOut = flow_data_record.get("bytes-out")
                if bytesOut is not None:
                    element_text = bytesOut
                    export_packet_flow_data_record_dict_buffer["bytesOut"] = {}
                    export_packet_flow_data_record_dict_buffer["bytesOut"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["bytesOut"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["bytesOut"]["observedAt"] = observed_at
                pktsIn = flow_data_record.get("pkts-in")
                if pktsIn is not None:
                    element_text = pktsIn
                    export_packet_flow_data_record_dict_buffer["pktsIn"] = {}
                    export_packet_flow_data_record_dict_buffer["pktsIn"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["pktsIn"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["pktsIn"]["observedAt"] = observed_at
                pktsOut = flow_data_record.get("pkts-out")
                if pktsOut is not None:
                    element_text = pktsOut
                    export_packet_flow_data_record_dict_buffer["pktsOut"] = {}
                    export_packet_flow_data_record_dict_buffer["pktsOut"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["pktsOut"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["pktsOut"]["observedAt"] = observed_at
                flows = flow_data_record.get("flows")
                if flows is not None:
                    element_text = flows
                    export_packet_flow_data_record_dict_buffer["flows"] = {}
                    export_packet_flow_data_record_dict_buffer["flows"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["flows"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["flows"]["observedAt"] = observed_at
                protocol = flow_data_record.get("protocol")
                if protocol is not None:
                    element_text = protocol
                    export_packet_flow_data_record_dict_buffer["protocol"] = {}
                    export_packet_flow_data_record_dict_buffer["protocol"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["protocol"]["value"] = element_text
                    export_packet_flow_data_record_dict_buffer["protocol"]["observedAt"] = observed_at
                srcTos = flow_data_record.get("src-tos")
                if srcTos is not None:
                    element_text = srcTos
                    export_packet_flow_data_record_dict_buffer["srcTos"] = {}
                    export_packet_flow_data_record_dict_buffer["srcTos"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["srcTos"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["srcTos"]["observedAt"] = observed_at
                dstTos = flow_data_record.get("dst-tos")
                if dstTos is not None:
                    element_text = dstTos
                    export_packet_flow_data_record_dict_buffer["dstTos"] = {}
                    export_packet_flow_data_record_dict_buffer["dstTos"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["dstTos"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["dstTos"]["observedAt"] = observed_at
                tcpFlags = flow_data_record.get("tcp-flags")
                if tcpFlags is not None:
                    element_text = tcpFlags
                    export_packet_flow_data_record_dict_buffer["tcpFlags"] = {}
                    export_packet_flow_data_record_dict_buffer["tcpFlags"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["tcpFlags"]["value"] = list(element_text)
                    export_packet_flow_data_record_dict_buffer["tcpFlags"]["observedAt"] = observed_at
                srcPort = flow_data_record.get("src-port")
                if srcPort is not None:
                    element_text = srcPort
                    export_packet_flow_data_record_dict_buffer["srcPort"] = {}
                    export_packet_flow_data_record_dict_buffer["srcPort"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["srcPort"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["srcPort"]["observedAt"] = observed_at
                dstPort = flow_data_record.get("dst-port")
                if dstPort is not None:
                    element_text = dstPort
                    export_packet_flow_data_record_dict_buffer["dstPort"] = {}
                    export_packet_flow_data_record_dict_buffer["dstPort"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["dstPort"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["dstPort"]["observedAt"] = observed_at
                snmpIn = flow_data_record.get("snmp-in")
                if snmpIn is not None:
                    element_text = snmpIn
                    export_packet_flow_data_record_dict_buffer["snmpIn"] = {}
                    export_packet_flow_data_record_dict_buffer["snmpIn"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["snmpIn"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["snmpIn"]["observedAt"] = observed_at
                snmpOut = flow_data_record.get("snmp-out")
                if snmpOut is not None:
                    element_text = snmpOut
                    export_packet_flow_data_record_dict_buffer["snmpOut"] = {}
                    export_packet_flow_data_record_dict_buffer["snmpOut"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["snmpOut"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["snmpOut"]["observedAt"] = observed_at
                bytesOutMul = flow_data_record.get("bytes-out-mul")
                if bytesOutMul is not None:
                    element_text = bytesOutMul
                    export_packet_flow_data_record_dict_buffer["bytesOutMul"] = {}
                    export_packet_flow_data_record_dict_buffer["bytesOutMul"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["bytesOutMul"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["bytesOutMul"]["observedAt"] = observed_at
                pktsOutMul = flow_data_record.get("pkts-out-mul")
                if pktsOutMul is not None:
                    element_text = pktsOutMul
                    export_packet_flow_data_record_dict_buffer["pktsOutMul"] = {}
                    export_packet_flow_data_record_dict_buffer["pktsOutMul"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["pktsOutMul"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["pktsOutMul"]["observedAt"] = observed_at
                firstSwitched = flow_data_record.get("first-switched")
                if firstSwitched is not None:
                    element_text = firstSwitched
                    export_packet_flow_data_record_dict_buffer["firstSwitched"] = {}
                    export_packet_flow_data_record_dict_buffer["firstSwitched"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["firstSwitched"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["firstSwitched"]["observedAt"] = observed_at
                lastSwitched = flow_data_record.get("last-switched")
                if lastSwitched is not None:
                    element_text = lastSwitched
                    export_packet_flow_data_record_dict_buffer["lastSwitched"] = {}
                    export_packet_flow_data_record_dict_buffer["lastSwitched"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["lastSwitched"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["lastSwitched"]["observedAt"] = observed_at
                minPktLen = flow_data_record.get("min-pkt-len")
                if minPktLen is not None:
                    element_text = minPktLen
                    export_packet_flow_data_record_dict_buffer["minPktLen"] = {}
                    export_packet_flow_data_record_dict_buffer["minPktLen"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["minPktLen"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["minPktLen"]["observedAt"] = observed_at
                maxPktLen = flow_data_record.get("max-pkt-len")
                if maxPktLen is not None:
                    element_text = maxPktLen
                    export_packet_flow_data_record_dict_buffer["maxPktLen"] = {}
                    export_packet_flow_data_record_dict_buffer["maxPktLen"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["maxPktLen"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["maxPktLen"]["observedAt"] = observed_at
                icmpType = flow_data_record.get("icmp-type")
                if icmpType is not None:
                    element_text = icmpType
                    export_packet_flow_data_record_dict_buffer["icmpType"] = {}
                    export_packet_flow_data_record_dict_buffer["icmpType"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["icmpType"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["icmpType"]["observedAt"] = observed_at
                igmpType = flow_data_record.get("igmp-type")
                if igmpType is not None:
                    element_text = igmpType
                    export_packet_flow_data_record_dict_buffer["igmpType"] = {}
                    export_packet_flow_data_record_dict_buffer["igmpType"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["igmpType"]["value"] = element_text
                    export_packet_flow_data_record_dict_buffer["igmpType"]["observedAt"] = observed_at
                samplerName = flow_data_record.get("sampler-name")
                if samplerName is not None:
                    element_text = samplerName
                    if export_packet_flow_data_record_dict_buffer["id"].split(":")[-1] != element_text:
                        export_packet_flow_data_record_dict_buffer["id"] = export_packet_flow_data_record_dict_buffer["id"] + ":" + str(element_text)
                    export_packet_flow_data_record_dict_buffer["samplerName"] = {}
                    export_packet_flow_data_record_dict_buffer["samplerName"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["samplerName"]["value"] = element_text
                    export_packet_flow_data_record_dict_buffer["samplerName"]["observedAt"] = observed_at
                samplingInterval = flow_data_record.get("sampling-interval")
                if samplingInterval is not None:
                    element_text = samplingInterval
                    export_packet_flow_data_record_dict_buffer["samplingInterval"] = {}
                    export_packet_flow_data_record_dict_buffer["samplingInterval"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["samplingInterval"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["samplingInterval"]["observedAt"] = observed_at
                samplingAlgorithm = flow_data_record.get("sampling-algorithm")
                if samplingAlgorithm is not None:
                    element_text = samplingAlgorithm
                    export_packet_flow_data_record_dict_buffer["samplingAlgorithm"] = {}
                    export_packet_flow_data_record_dict_buffer["samplingAlgorithm"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["samplingAlgorithm"]["value"] = element_text
                    export_packet_flow_data_record_dict_buffer["samplingAlgorithm"]["observedAt"] = observed_at
                flowActiveTout = flow_data_record.get("flow-active-tout")
                if flowActiveTout is not None:
                    element_text = flowActiveTout
                    export_packet_flow_data_record_dict_buffer["flowActiveTout"] = {}
                    export_packet_flow_data_record_dict_buffer["flowActiveTout"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["flowActiveTout"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["flowActiveTout"]["observedAt"] = observed_at
                flowInactiveTout = flow_data_record.get("flow-inactive-tout")
                if flowInactiveTout is not None:
                    element_text = flowInactiveTout
                    export_packet_flow_data_record_dict_buffer["flowInactiveTout"] = {}
                    export_packet_flow_data_record_dict_buffer["flowInactiveTout"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["flowInactiveTout"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["flowInactiveTout"]["observedAt"] = observed_at
                engineType = flow_data_record.get("engine-type")
                if engineType is not None:
                    element_text = engineType
                    export_packet_flow_data_record_dict_buffer["engineType"] = {}
                    export_packet_flow_data_record_dict_buffer["engineType"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["engineType"]["value"] = element_text
                    export_packet_flow_data_record_dict_buffer["engineType"]["observedAt"] = observed_at
                engineId = flow_data_record.get("engine-id")
                if engineId is not None:
                    element_text = engineId
                    export_packet_flow_data_record_dict_buffer["engineId"] = {}
                    export_packet_flow_data_record_dict_buffer["engineId"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["engineId"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["engineId"]["observedAt"] = observed_at
                totBytesExp = flow_data_record.get("tot-bytes-exp")
                if totBytesExp is not None:
                    element_text = totBytesExp
                    export_packet_flow_data_record_dict_buffer["totBytesExp"] = {}
                    export_packet_flow_data_record_dict_buffer["totBytesExp"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["totBytesExp"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["totBytesExp"]["observedAt"] = observed_at
                totPktsExp = flow_data_record.get("tot-pkts-exp")
                if totPktsExp is not None:
                    element_text = totPktsExp
                    export_packet_flow_data_record_dict_buffer["totPktsExp"] = {}
                    export_packet_flow_data_record_dict_buffer["totPktsExp"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["totPktsExp"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["totPktsExp"]["observedAt"] = observed_at
                totFlowsExp = flow_data_record.get("tot-flows-exp")
                if totFlowsExp is not None:
                    element_text = totFlowsExp
                    export_packet_flow_data_record_dict_buffer["totFlowsExp"] = {}
                    export_packet_flow_data_record_dict_buffer["totFlowsExp"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["totFlowsExp"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["totFlowsExp"]["observedAt"] = observed_at
                flowSamplerId = flow_data_record.get("flow-sampler-id")
                if flowSamplerId is not None:
                    element_text = flowSamplerId
                    export_packet_flow_data_record_dict_buffer["flowSamplerId"] = {}
                    export_packet_flow_data_record_dict_buffer["flowSamplerId"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["flowSamplerId"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["flowSamplerId"]["observedAt"] = observed_at
                flowSamplerMode = flow_data_record.get("flow-sampler-mode")
                if flowSamplerMode is not None:
                    element_text = flowSamplerMode
                    export_packet_flow_data_record_dict_buffer["flowSamplerMode"] = {}
                    export_packet_flow_data_record_dict_buffer["flowSamplerMode"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["flowSamplerMode"]["value"] = element_text
                    export_packet_flow_data_record_dict_buffer["flowSamplerMode"]["observedAt"] = observed_at
                flowSamplerRandom = flow_data_record.get("flow-sampler-random")
                if flowSamplerRandom is not None:
                    element_text = flowSamplerRandom
                    export_packet_flow_data_record_dict_buffer["flowSamplerRandom"] = {}
                    export_packet_flow_data_record_dict_buffer["flowSamplerRandom"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["flowSamplerRandom"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["flowSamplerRandom"]["observedAt"] = observed_at
                minTtl = flow_data_record.get("min-ttl")
                if minTtl is not None:
                    element_text = minTtl
                    export_packet_flow_data_record_dict_buffer["minTtl"] = {}
                    export_packet_flow_data_record_dict_buffer["minTtl"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["minTtl"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["minTtl"]["observedAt"] = observed_at
                maxTtl = flow_data_record.get("max-ttl")
                if maxTtl is not None:
                    element_text = maxTtl
                    export_packet_flow_data_record_dict_buffer["maxTtl"] = {}
                    export_packet_flow_data_record_dict_buffer["maxTtl"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["maxTtl"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["maxTtl"]["observedAt"] = observed_at
                srcMacIn = flow_data_record.get("src-mac-in")
                if srcMacIn is not None:
                    element_text = srcMacIn
                    export_packet_flow_data_record_dict_buffer["srcMacIn"] = {}
                    export_packet_flow_data_record_dict_buffer["srcMacIn"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["srcMacIn"]["value"] = element_text
                    export_packet_flow_data_record_dict_buffer["srcMacIn"]["observedAt"] = observed_at
                dstMacIn = flow_data_record.get("dst-mac-in")
                if dstMacIn is not None:
                    element_text = dstMacIn
                    export_packet_flow_data_record_dict_buffer["dstMacIn"] = {}
                    export_packet_flow_data_record_dict_buffer["dstMacIn"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["dstMacIn"]["value"] = element_text
                    export_packet_flow_data_record_dict_buffer["dstMacIn"]["observedAt"] = observed_at
                srcMacOut = flow_data_record.get("src-mac-out")
                if srcMacOut is not None:
                    element_text = srcMacOut
                    export_packet_flow_data_record_dict_buffer["srcMacOut"] = {}
                    export_packet_flow_data_record_dict_buffer["srcMacOut"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["srcMacOut"]["value"] = element_text
                    export_packet_flow_data_record_dict_buffer["srcMacOut"]["observedAt"] = observed_at
                dstMacOut = flow_data_record.get("dst-mac-out")
                if dstMacOut is not None:
                    element_text = dstMacOut
                    export_packet_flow_data_record_dict_buffer["dstMacOut"] = {}
                    export_packet_flow_data_record_dict_buffer["dstMacOut"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["dstMacOut"]["value"] = element_text
                    export_packet_flow_data_record_dict_buffer["dstMacOut"]["observedAt"] = observed_at
                ipVersion = flow_data_record.get("ip-version")
                if ipVersion is not None:
                    element_text = ipVersion
                    export_packet_flow_data_record_dict_buffer["ipVersion"] = {}
                    export_packet_flow_data_record_dict_buffer["ipVersion"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["ipVersion"]["value"] = element_text
                    export_packet_flow_data_record_dict_buffer["ipVersion"]["observedAt"] = observed_at
                direction = flow_data_record.get("direction")
                if direction is not None:
                    element_text = direction
                    export_packet_flow_data_record_dict_buffer["direction"] = {}
                    export_packet_flow_data_record_dict_buffer["direction"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["direction"]["value"] = element_text
                    export_packet_flow_data_record_dict_buffer["direction"]["observedAt"] = observed_at
                ifName = flow_data_record.get("if-name")
                if ifName is not None:
                    element_text = ifName
                    if export_packet_flow_data_record_dict_buffer["id"].split(":")[-1] != element_text:
                        export_packet_flow_data_record_dict_buffer["id"] = export_packet_flow_data_record_dict_buffer["id"] + ":" + str(element_text)
                    export_packet_flow_data_record_dict_buffer["ifName"] = {}
                    export_packet_flow_data_record_dict_buffer["ifName"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["ifName"]["value"] = element_text
                    export_packet_flow_data_record_dict_buffer["ifName"]["observedAt"] = observed_at
                ifDesc = flow_data_record.get("if-desc")
                if ifDesc is not None:
                    element_text = ifDesc
                    export_packet_flow_data_record_dict_buffer["ifDesc"] = {}
                    export_packet_flow_data_record_dict_buffer["ifDesc"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["ifDesc"]["value"] = element_text
                    export_packet_flow_data_record_dict_buffer["ifDesc"]["observedAt"] = observed_at
                fragOffset = flow_data_record.get("frag-offset")
                if fragOffset is not None:
                    element_text = fragOffset
                    export_packet_flow_data_record_dict_buffer["fragOffset"] = {}
                    export_packet_flow_data_record_dict_buffer["fragOffset"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["fragOffset"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["fragOffset"]["observedAt"] = observed_at
                forwardingStatus = flow_data_record.get("forwarding-status")
                if forwardingStatus is not None:
                    element_text = forwardingStatus
                    export_packet_flow_data_record_dict_buffer["forwardingStatus"] = {}
                    export_packet_flow_data_record_dict_buffer["forwardingStatus"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["forwardingStatus"]["value"] = element_text
                    export_packet_flow_data_record_dict_buffer["forwardingStatus"]["observedAt"] = observed_at
                postipDscp = flow_data_record.get("postip-dscp")
                if postipDscp is not None:
                    element_text = postipDscp
                    export_packet_flow_data_record_dict_buffer["postipDscp"] = {}
                    export_packet_flow_data_record_dict_buffer["postipDscp"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["postipDscp"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["postipDscp"]["observedAt"] = observed_at
                replFactorMul = flow_data_record.get("repl-factor-mul")
                if replFactorMul is not None:
                    element_text = replFactorMul
                    export_packet_flow_data_record_dict_buffer["replFactorMul"] = {}
                    export_packet_flow_data_record_dict_buffer["replFactorMul"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["replFactorMul"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["replFactorMul"]["observedAt"] = observed_at
                ipv4 = flow_data_record.get("ipv4")
                if ipv4 is not None and len(ipv4) != 0:
                    export_packet_flow_data_record_ipv4_dict_buffer = {}
                    export_packet_flow_data_record_ipv4_dict_buffer["id"] = "urn:ngsi-ld:ExportPacketFlowDataRecordIpv4:" + ":".join(export_packet_flow_data_record_dict_buffer["id"].split(":")[3:])
                    export_packet_flow_data_record_ipv4_dict_buffer["type"] = "ExportPacketFlowDataRecordIpv4"
                    export_packet_flow_data_record_ipv4_dict_buffer["isPartOf"] = {}
                    export_packet_flow_data_record_ipv4_dict_buffer["isPartOf"]["type"] = "Relationship"
                    export_packet_flow_data_record_ipv4_dict_buffer["isPartOf"]["object"] = export_packet_flow_data_record_dict_buffer["id"]
                    export_packet_flow_data_record_ipv4_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    srcAddress = ipv4.get("src-address")
                    if srcAddress is not None:
                        element_text = srcAddress
                        export_packet_flow_data_record_ipv4_dict_buffer["srcAddress"] = {}
                        export_packet_flow_data_record_ipv4_dict_buffer["srcAddress"]["type"] = "Property"
                        export_packet_flow_data_record_ipv4_dict_buffer["srcAddress"]["value"] = element_text
                        export_packet_flow_data_record_ipv4_dict_buffer["srcAddress"]["observedAt"] = observed_at
                    dstAddress = ipv4.get("dst-address")
                    if dstAddress is not None:
                        element_text = dstAddress
                        export_packet_flow_data_record_ipv4_dict_buffer["dstAddress"] = {}
                        export_packet_flow_data_record_ipv4_dict_buffer["dstAddress"]["type"] = "Property"
                        export_packet_flow_data_record_ipv4_dict_buffer["dstAddress"]["value"] = element_text
                        export_packet_flow_data_record_ipv4_dict_buffer["dstAddress"]["observedAt"] = observed_at
                    srcMask = ipv4.get("src-mask")
                    if srcMask is not None:
                        element_text = srcMask
                        export_packet_flow_data_record_ipv4_dict_buffer["srcMask"] = {}
                        export_packet_flow_data_record_ipv4_dict_buffer["srcMask"]["type"] = "Property"
                        export_packet_flow_data_record_ipv4_dict_buffer["srcMask"]["value"] = int(element_text)
                        export_packet_flow_data_record_ipv4_dict_buffer["srcMask"]["observedAt"] = observed_at
                    dstMask = ipv4.get("dst-mask")
                    if dstMask is not None:
                        element_text = dstMask
                        export_packet_flow_data_record_ipv4_dict_buffer["dstMask"] = {}
                        export_packet_flow_data_record_ipv4_dict_buffer["dstMask"]["type"] = "Property"
                        export_packet_flow_data_record_ipv4_dict_buffer["dstMask"]["value"] = int(element_text)
                        export_packet_flow_data_record_ipv4_dict_buffer["dstMask"]["observedAt"] = observed_at
                    srcPrefix = ipv4.get("src-prefix")
                    if srcPrefix is not None:
                        element_text = srcPrefix
                        export_packet_flow_data_record_ipv4_dict_buffer["srcPrefix"] = {}
                        export_packet_flow_data_record_ipv4_dict_buffer["srcPrefix"]["type"] = "Property"
                        export_packet_flow_data_record_ipv4_dict_buffer["srcPrefix"]["value"] = element_text
                        export_packet_flow_data_record_ipv4_dict_buffer["srcPrefix"]["observedAt"] = observed_at
                    dstPrefix = ipv4.get("dst-prefix")
                    if dstPrefix is not None:
                        element_text = dstPrefix
                        export_packet_flow_data_record_ipv4_dict_buffer["dstPrefix"] = {}
                        export_packet_flow_data_record_ipv4_dict_buffer["dstPrefix"]["type"] = "Property"
                        export_packet_flow_data_record_ipv4_dict_buffer["dstPrefix"]["value"] = element_text
                        export_packet_flow_data_record_ipv4_dict_buffer["dstPrefix"]["observedAt"] = observed_at
                    nextHop = ipv4.get("next-hop")
                    if nextHop is not None:
                        element_text = nextHop
                        export_packet_flow_data_record_ipv4_dict_buffer["nextHop"] = {}
                        export_packet_flow_data_record_ipv4_dict_buffer["nextHop"]["type"] = "Property"
                        export_packet_flow_data_record_ipv4_dict_buffer["nextHop"]["value"] = element_text
                        export_packet_flow_data_record_ipv4_dict_buffer["nextHop"]["observedAt"] = observed_at
                    identification = ipv4.get("identification")
                    if identification is not None:
                        element_text = identification
                        export_packet_flow_data_record_ipv4_dict_buffer["identification"] = {}
                        export_packet_flow_data_record_ipv4_dict_buffer["identification"]["type"] = "Property"
                        export_packet_flow_data_record_ipv4_dict_buffer["identification"]["value"] = int(element_text)
                        export_packet_flow_data_record_ipv4_dict_buffer["identification"]["observedAt"] = observed_at
                    dict_buffers.append(export_packet_flow_data_record_ipv4_dict_buffer)
                ipv6 = flow_data_record.get("ipv6")
                if ipv6 is not None and len(ipv6) != 0:
                    export_packet_flow_data_record_ipv6_dict_buffer = {}
                    export_packet_flow_data_record_ipv6_dict_buffer["id"] = "urn:ngsi-ld:ExportPacketFlowDataRecordIpv6:" + ":".join(export_packet_flow_data_record_dict_buffer["id"].split(":")[3:])
                    export_packet_flow_data_record_ipv6_dict_buffer["type"] = "ExportPacketFlowDataRecordIpv6"
                    export_packet_flow_data_record_ipv6_dict_buffer["isPartOf"] = {}
                    export_packet_flow_data_record_ipv6_dict_buffer["isPartOf"]["type"] = "Relationship"
                    export_packet_flow_data_record_ipv6_dict_buffer["isPartOf"]["object"] = export_packet_flow_data_record_dict_buffer["id"]
                    export_packet_flow_data_record_ipv6_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    srcAddress = ipv6.get("src-address")
                    if srcAddress is not None:
                        element_text = srcAddress
                        export_packet_flow_data_record_ipv6_dict_buffer["srcAddress"] = {}
                        export_packet_flow_data_record_ipv6_dict_buffer["srcAddress"]["type"] = "Property"
                        export_packet_flow_data_record_ipv6_dict_buffer["srcAddress"]["value"] = element_text
                        export_packet_flow_data_record_ipv6_dict_buffer["srcAddress"]["observedAt"] = observed_at
                    dstAddress = ipv6.get("dst-address")
                    if dstAddress is not None:
                        element_text = dstAddress
                        export_packet_flow_data_record_ipv6_dict_buffer["dstAddress"] = {}
                        export_packet_flow_data_record_ipv6_dict_buffer["dstAddress"]["type"] = "Property"
                        export_packet_flow_data_record_ipv6_dict_buffer["dstAddress"]["value"] = element_text
                        export_packet_flow_data_record_ipv6_dict_buffer["dstAddress"]["observedAt"] = observed_at
                    srcMask = ipv6.get("src-mask")
                    if srcMask is not None:
                        element_text = srcMask
                        export_packet_flow_data_record_ipv6_dict_buffer["srcMask"] = {}
                        export_packet_flow_data_record_ipv6_dict_buffer["srcMask"]["type"] = "Property"
                        export_packet_flow_data_record_ipv6_dict_buffer["srcMask"]["value"] = int(element_text)
                        export_packet_flow_data_record_ipv6_dict_buffer["srcMask"]["observedAt"] = observed_at
                    dstMask = ipv6.get("dst-mask")
                    if dstMask is not None:
                        element_text = dstMask
                        export_packet_flow_data_record_ipv6_dict_buffer["dstMask"] = {}
                        export_packet_flow_data_record_ipv6_dict_buffer["dstMask"]["type"] = "Property"
                        export_packet_flow_data_record_ipv6_dict_buffer["dstMask"]["value"] = int(element_text)
                        export_packet_flow_data_record_ipv6_dict_buffer["dstMask"]["observedAt"] = observed_at
                    nextHop = ipv6.get("next-hop")
                    if nextHop is not None:
                        element_text = nextHop
                        export_packet_flow_data_record_ipv6_dict_buffer["nextHop"] = {}
                        export_packet_flow_data_record_ipv6_dict_buffer["nextHop"]["type"] = "Property"
                        export_packet_flow_data_record_ipv6_dict_buffer["nextHop"]["value"] = element_text
                        export_packet_flow_data_record_ipv6_dict_buffer["nextHop"]["observedAt"] = observed_at
                    flowLabel = ipv6.get("flow-label")
                    if flowLabel is not None:
                        element_text = flowLabel
                        export_packet_flow_data_record_ipv6_dict_buffer["flowLabel"] = {}
                        export_packet_flow_data_record_ipv6_dict_buffer["flowLabel"]["type"] = "Property"
                        export_packet_flow_data_record_ipv6_dict_buffer["flowLabel"]["value"] = int(element_text)
                        export_packet_flow_data_record_ipv6_dict_buffer["flowLabel"]["observedAt"] = observed_at
                    optHeaders = ipv6.get("opt-headers")
                    if optHeaders is not None:
                        element_text = optHeaders
                        export_packet_flow_data_record_ipv6_dict_buffer["optHeaders"] = {}
                        export_packet_flow_data_record_ipv6_dict_buffer["optHeaders"]["type"] = "Property"
                        export_packet_flow_data_record_ipv6_dict_buffer["optHeaders"]["value"] = int(element_text)
                        export_packet_flow_data_record_ipv6_dict_buffer["optHeaders"]["observedAt"] = observed_at
                    dict_buffers.append(export_packet_flow_data_record_ipv6_dict_buffer)
                mpls = flow_data_record.get("mpls")
                if mpls is not None and len(mpls) != 0:
                    export_packet_flow_data_record_mpls_dict_buffer = {}
                    export_packet_flow_data_record_mpls_dict_buffer["id"] = "urn:ngsi-ld:ExportPacketFlowDataRecordMpls:" + ":".join(export_packet_flow_data_record_dict_buffer["id"].split(":")[3:])
                    export_packet_flow_data_record_mpls_dict_buffer["type"] = "ExportPacketFlowDataRecordMpls"
                    export_packet_flow_data_record_mpls_dict_buffer["isPartOf"] = {}
                    export_packet_flow_data_record_mpls_dict_buffer["isPartOf"]["type"] = "Relationship"
                    export_packet_flow_data_record_mpls_dict_buffer["isPartOf"]["object"] = export_packet_flow_data_record_dict_buffer["id"]
                    export_packet_flow_data_record_mpls_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    palRd = mpls.get("pal-rd")
                    if palRd is not None:
                        element_text = palRd
                        export_packet_flow_data_record_mpls_dict_buffer["palRd"] = {}
                        export_packet_flow_data_record_mpls_dict_buffer["palRd"]["type"] = "Property"
                        export_packet_flow_data_record_mpls_dict_buffer["palRd"]["value"] = int(element_text)
                        export_packet_flow_data_record_mpls_dict_buffer["palRd"]["observedAt"] = observed_at
                    prefixLen = mpls.get("prefix-len")
                    if prefixLen is not None:
                        element_text = prefixLen
                        export_packet_flow_data_record_mpls_dict_buffer["prefixLen"] = {}
                        export_packet_flow_data_record_mpls_dict_buffer["prefixLen"]["type"] = "Property"
                        export_packet_flow_data_record_mpls_dict_buffer["prefixLen"]["value"] = int(element_text)
                        export_packet_flow_data_record_mpls_dict_buffer["prefixLen"]["observedAt"] = observed_at
                    topLabelType = mpls.get("top-label-type")
                    if topLabelType is not None:
                        element_text = topLabelType
                        export_packet_flow_data_record_mpls_dict_buffer["topLabelType"] = {}
                        export_packet_flow_data_record_mpls_dict_buffer["topLabelType"]["type"] = "Property"
                        export_packet_flow_data_record_mpls_dict_buffer["topLabelType"]["value"] = element_text
                        export_packet_flow_data_record_mpls_dict_buffer["topLabelType"]["observedAt"] = observed_at
                    topLabelIp = mpls.get("top-label-ip")
                    if topLabelIp is not None:
                        element_text = topLabelIp
                        export_packet_flow_data_record_mpls_dict_buffer["topLabelIp"] = {}
                        export_packet_flow_data_record_mpls_dict_buffer["topLabelIp"]["type"] = "Property"
                        export_packet_flow_data_record_mpls_dict_buffer["topLabelIp"]["value"] = element_text
                        export_packet_flow_data_record_mpls_dict_buffer["topLabelIp"]["observedAt"] = observed_at
                    label1 = mpls.get("label-1")
                    if label1 is not None:
                        element_text = label1
                        export_packet_flow_data_record_mpls_dict_buffer["label1"] = {}
                        export_packet_flow_data_record_mpls_dict_buffer["label1"]["type"] = "Property"
                        export_packet_flow_data_record_mpls_dict_buffer["label1"]["value"] = int(element_text)
                        export_packet_flow_data_record_mpls_dict_buffer["label1"]["observedAt"] = observed_at
                    label2 = mpls.get("label-2")
                    if label2 is not None:
                        element_text = label2
                        export_packet_flow_data_record_mpls_dict_buffer["label2"] = {}
                        export_packet_flow_data_record_mpls_dict_buffer["label2"]["type"] = "Property"
                        export_packet_flow_data_record_mpls_dict_buffer["label2"]["value"] = int(element_text)
                        export_packet_flow_data_record_mpls_dict_buffer["label2"]["observedAt"] = observed_at
                    label3 = mpls.get("label-3")
                    if label3 is not None:
                        element_text = label3
                        export_packet_flow_data_record_mpls_dict_buffer["label3"] = {}
                        export_packet_flow_data_record_mpls_dict_buffer["label3"]["type"] = "Property"
                        export_packet_flow_data_record_mpls_dict_buffer["label3"]["value"] = int(element_text)
                        export_packet_flow_data_record_mpls_dict_buffer["label3"]["observedAt"] = observed_at
                    label4 = mpls.get("label-4")
                    if label4 is not None:
                        element_text = label4
                        export_packet_flow_data_record_mpls_dict_buffer["label4"] = {}
                        export_packet_flow_data_record_mpls_dict_buffer["label4"]["type"] = "Property"
                        export_packet_flow_data_record_mpls_dict_buffer["label4"]["value"] = int(element_text)
                        export_packet_flow_data_record_mpls_dict_buffer["label4"]["observedAt"] = observed_at
                    label5 = mpls.get("label-5")
                    if label5 is not None:
                        element_text = label5
                        export_packet_flow_data_record_mpls_dict_buffer["label5"] = {}
                        export_packet_flow_data_record_mpls_dict_buffer["label5"]["type"] = "Property"
                        export_packet_flow_data_record_mpls_dict_buffer["label5"]["value"] = int(element_text)
                        export_packet_flow_data_record_mpls_dict_buffer["label5"]["observedAt"] = observed_at
                    label6 = mpls.get("label-6")
                    if label6 is not None:
                        element_text = label6
                        export_packet_flow_data_record_mpls_dict_buffer["label6"] = {}
                        export_packet_flow_data_record_mpls_dict_buffer["label6"]["type"] = "Property"
                        export_packet_flow_data_record_mpls_dict_buffer["label6"]["value"] = int(element_text)
                        export_packet_flow_data_record_mpls_dict_buffer["label6"]["observedAt"] = observed_at
                    label7 = mpls.get("label-7")
                    if label7 is not None:
                        element_text = label7
                        export_packet_flow_data_record_mpls_dict_buffer["label7"] = {}
                        export_packet_flow_data_record_mpls_dict_buffer["label7"]["type"] = "Property"
                        export_packet_flow_data_record_mpls_dict_buffer["label7"]["value"] = int(element_text)
                        export_packet_flow_data_record_mpls_dict_buffer["label7"]["observedAt"] = observed_at
                    label8 = mpls.get("label-8")
                    if label8 is not None:
                        element_text = label8
                        export_packet_flow_data_record_mpls_dict_buffer["label8"] = {}
                        export_packet_flow_data_record_mpls_dict_buffer["label8"]["type"] = "Property"
                        export_packet_flow_data_record_mpls_dict_buffer["label8"]["value"] = int(element_text)
                        export_packet_flow_data_record_mpls_dict_buffer["label8"]["observedAt"] = observed_at
                    label9 = mpls.get("label-9")
                    if label9 is not None:
                        element_text = label9
                        export_packet_flow_data_record_mpls_dict_buffer["label9"] = {}
                        export_packet_flow_data_record_mpls_dict_buffer["label9"]["type"] = "Property"
                        export_packet_flow_data_record_mpls_dict_buffer["label9"]["value"] = int(element_text)
                        export_packet_flow_data_record_mpls_dict_buffer["label9"]["observedAt"] = observed_at
                    label10 = mpls.get("label-10")
                    if label10 is not None:
                        element_text = label10
                        export_packet_flow_data_record_mpls_dict_buffer["label10"] = {}
                        export_packet_flow_data_record_mpls_dict_buffer["label10"]["type"] = "Property"
                        export_packet_flow_data_record_mpls_dict_buffer["label10"]["value"] = int(element_text)
                        export_packet_flow_data_record_mpls_dict_buffer["label10"]["observedAt"] = observed_at
                    dict_buffers.append(export_packet_flow_data_record_mpls_dict_buffer)
                bgp = flow_data_record.get("bgp")
                if bgp is not None and len(bgp) != 0:
                    export_packet_flow_data_record_bgp_dict_buffer = {}
                    export_packet_flow_data_record_bgp_dict_buffer["id"] = "urn:ngsi-ld:ExportPacketFlowDataRecordBgp:" + ":".join(export_packet_flow_data_record_dict_buffer["id"].split(":")[3:])
                    export_packet_flow_data_record_bgp_dict_buffer["type"] = "ExportPacketFlowDataRecordBgp"
                    export_packet_flow_data_record_bgp_dict_buffer["isPartOf"] = {}
                    export_packet_flow_data_record_bgp_dict_buffer["isPartOf"]["type"] = "Relationship"
                    export_packet_flow_data_record_bgp_dict_buffer["isPartOf"]["object"] = export_packet_flow_data_record_dict_buffer["id"]
                    export_packet_flow_data_record_bgp_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    srcAs = bgp.get("src-as")
                    if srcAs is not None:
                        element_text = srcAs
                        export_packet_flow_data_record_bgp_dict_buffer["srcAs"] = {}
                        export_packet_flow_data_record_bgp_dict_buffer["srcAs"]["type"] = "Property"
                        export_packet_flow_data_record_bgp_dict_buffer["srcAs"]["value"] = int(element_text)
                        export_packet_flow_data_record_bgp_dict_buffer["srcAs"]["observedAt"] = observed_at
                    dstAs = bgp.get("dst-as")
                    if dstAs is not None:
                        element_text = dstAs
                        export_packet_flow_data_record_bgp_dict_buffer["dstAs"] = {}
                        export_packet_flow_data_record_bgp_dict_buffer["dstAs"]["type"] = "Property"
                        export_packet_flow_data_record_bgp_dict_buffer["dstAs"]["value"] = int(element_text)
                        export_packet_flow_data_record_bgp_dict_buffer["dstAs"]["observedAt"] = observed_at
                    nextHop = bgp.get("next-hop")
                    if nextHop is not None:
                        element_text = nextHop
                        export_packet_flow_data_record_bgp_dict_buffer["nextHop"] = {}
                        export_packet_flow_data_record_bgp_dict_buffer["nextHop"]["type"] = "Property"
                        export_packet_flow_data_record_bgp_dict_buffer["nextHop"]["value"] = element_text
                        export_packet_flow_data_record_bgp_dict_buffer["nextHop"]["observedAt"] = observed_at
                    nextHopIpv6 = bgp.get("next-hop-ipv6")
                    if nextHopIpv6 is not None:
                        element_text = nextHopIpv6
                        export_packet_flow_data_record_bgp_dict_buffer["nextHopIpv6"] = {}
                        export_packet_flow_data_record_bgp_dict_buffer["nextHopIpv6"]["type"] = "Property"
                        export_packet_flow_data_record_bgp_dict_buffer["nextHopIpv6"]["value"] = element_text
                        export_packet_flow_data_record_bgp_dict_buffer["nextHopIpv6"]["observedAt"] = observed_at
                    srcTrafficId = bgp.get("src-traffic-id")
                    if srcTrafficId is not None:
                        element_text = srcTrafficId
                        export_packet_flow_data_record_bgp_dict_buffer["srcTrafficId"] = {}
                        export_packet_flow_data_record_bgp_dict_buffer["srcTrafficId"]["type"] = "Property"
                        export_packet_flow_data_record_bgp_dict_buffer["srcTrafficId"]["value"] = int(element_text)
                        export_packet_flow_data_record_bgp_dict_buffer["srcTrafficId"]["observedAt"] = observed_at
                    dstTrafficId = bgp.get("dst-traffic-id")
                    if dstTrafficId is not None:
                        element_text = dstTrafficId
                        export_packet_flow_data_record_bgp_dict_buffer["dstTrafficId"] = {}
                        export_packet_flow_data_record_bgp_dict_buffer["dstTrafficId"]["type"] = "Property"
                        export_packet_flow_data_record_bgp_dict_buffer["dstTrafficId"]["value"] = int(element_text)
                        export_packet_flow_data_record_bgp_dict_buffer["dstTrafficId"]["observedAt"] = observed_at
                    dict_buffers.append(export_packet_flow_data_record_bgp_dict_buffer)
                vlan = flow_data_record.get("vlan")
                if vlan is not None and len(vlan) != 0:
                    export_packet_flow_data_record_vlan_dict_buffer = {}
                    export_packet_flow_data_record_vlan_dict_buffer["id"] = "urn:ngsi-ld:ExportPacketFlowDataRecordVlan:" + ":".join(export_packet_flow_data_record_dict_buffer["id"].split(":")[3:])
                    export_packet_flow_data_record_vlan_dict_buffer["type"] = "ExportPacketFlowDataRecordVlan"
                    export_packet_flow_data_record_vlan_dict_buffer["isPartOf"] = {}
                    export_packet_flow_data_record_vlan_dict_buffer["isPartOf"]["type"] = "Relationship"
                    export_packet_flow_data_record_vlan_dict_buffer["isPartOf"]["object"] = export_packet_flow_data_record_dict_buffer["id"]
                    export_packet_flow_data_record_vlan_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    srcId = vlan.get("src-id")
                    if srcId is not None:
                        element_text = srcId
                        export_packet_flow_data_record_vlan_dict_buffer["srcId"] = {}
                        export_packet_flow_data_record_vlan_dict_buffer["srcId"]["type"] = "Property"
                        export_packet_flow_data_record_vlan_dict_buffer["srcId"]["value"] = int(element_text)
                        export_packet_flow_data_record_vlan_dict_buffer["srcId"]["observedAt"] = observed_at
                    dstId = vlan.get("dst-id")
                    if dstId is not None:
                        element_text = dstId
                        export_packet_flow_data_record_vlan_dict_buffer["dstId"] = {}
                        export_packet_flow_data_record_vlan_dict_buffer["dstId"]["type"] = "Property"
                        export_packet_flow_data_record_vlan_dict_buffer["dstId"]["value"] = int(element_text)
                        export_packet_flow_data_record_vlan_dict_buffer["dstId"]["observedAt"] = observed_at
                    dict_buffers.append(export_packet_flow_data_record_vlan_dict_buffer)
                permanent_flow = flow_data_record.get("permanent-flow")
                if permanent_flow is not None and len(permanent_flow) != 0:
                    export_packet_flow_data_record_permanent_flow_dict_buffer = {}
                    export_packet_flow_data_record_permanent_flow_dict_buffer["id"] = "urn:ngsi-ld:ExportPacketFlowDataRecordPermanentFlow:" + ":".join(export_packet_flow_data_record_dict_buffer["id"].split(":")[3:])
                    export_packet_flow_data_record_permanent_flow_dict_buffer["type"] = "ExportPacketFlowDataRecordPermanentFlow"
                    export_packet_flow_data_record_permanent_flow_dict_buffer["isPartOf"] = {}
                    export_packet_flow_data_record_permanent_flow_dict_buffer["isPartOf"]["type"] = "Relationship"
                    export_packet_flow_data_record_permanent_flow_dict_buffer["isPartOf"]["object"] = export_packet_flow_data_record_dict_buffer["id"]
                    export_packet_flow_data_record_permanent_flow_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    bytesIn = permanent_flow.get("bytes-in")
                    if bytesIn is not None:
                        element_text = bytesIn
                        export_packet_flow_data_record_permanent_flow_dict_buffer["bytesIn"] = {}
                        export_packet_flow_data_record_permanent_flow_dict_buffer["bytesIn"]["type"] = "Property"
                        export_packet_flow_data_record_permanent_flow_dict_buffer["bytesIn"]["value"] = int(element_text)
                        export_packet_flow_data_record_permanent_flow_dict_buffer["bytesIn"]["observedAt"] = observed_at
                    pktsIn = permanent_flow.get("pkts-in")
                    if pktsIn is not None:
                        element_text = pktsIn
                        export_packet_flow_data_record_permanent_flow_dict_buffer["pktsIn"] = {}
                        export_packet_flow_data_record_permanent_flow_dict_buffer["pktsIn"]["type"] = "Property"
                        export_packet_flow_data_record_permanent_flow_dict_buffer["pktsIn"]["value"] = int(element_text)
                        export_packet_flow_data_record_permanent_flow_dict_buffer["pktsIn"]["observedAt"] = observed_at
                    dict_buffers.append(export_packet_flow_data_record_permanent_flow_dict_buffer)
                application = flow_data_record.get("application")
                if application is not None and len(application) != 0:
                    export_packet_flow_data_record_application_dict_buffer = {}
                    export_packet_flow_data_record_application_dict_buffer["id"] = "urn:ngsi-ld:ExportPacketFlowDataRecordApplication:" + ":".join(export_packet_flow_data_record_dict_buffer["id"].split(":")[3:])
                    export_packet_flow_data_record_application_dict_buffer["type"] = "ExportPacketFlowDataRecordApplication"
                    export_packet_flow_data_record_application_dict_buffer["isPartOf"] = {}
                    export_packet_flow_data_record_application_dict_buffer["isPartOf"]["type"] = "Relationship"
                    export_packet_flow_data_record_application_dict_buffer["isPartOf"]["object"] = export_packet_flow_data_record_dict_buffer["id"]
                    export_packet_flow_data_record_application_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    desc = application.get("desc")
                    if desc is not None:
                        element_text = desc
                        export_packet_flow_data_record_application_dict_buffer["desc"] = {}
                        export_packet_flow_data_record_application_dict_buffer["desc"]["type"] = "Property"
                        export_packet_flow_data_record_application_dict_buffer["desc"]["value"] = element_text
                        export_packet_flow_data_record_application_dict_buffer["desc"]["observedAt"] = observed_at
                    tag = application.get("tag")
                    if tag is not None:
                        element_text = tag
                        export_packet_flow_data_record_application_dict_buffer["tag"] = {}
                        export_packet_flow_data_record_application_dict_buffer["tag"]["type"] = "Property"
                        export_packet_flow_data_record_application_dict_buffer["tag"]["value"] = element_text
                        export_packet_flow_data_record_application_dict_buffer["tag"]["observedAt"] = observed_at
                    name = application.get("name")
                    if name is not None:
                        element_text = name
                        if export_packet_flow_data_record_application_dict_buffer["id"].split(":")[-1] != element_text:
                            export_packet_flow_data_record_application_dict_buffer["id"] = export_packet_flow_data_record_application_dict_buffer["id"] + ":" + str(element_text)
                        export_packet_flow_data_record_application_dict_buffer["name"] = {}
                        export_packet_flow_data_record_application_dict_buffer["name"]["type"] = "Property"
                        export_packet_flow_data_record_application_dict_buffer["name"]["value"] = element_text
                        export_packet_flow_data_record_application_dict_buffer["name"]["observedAt"] = observed_at
                    dict_buffers.append(export_packet_flow_data_record_application_dict_buffer)
                layer2_pkt_section = flow_data_record.get("layer2-pkt-section")
                if layer2_pkt_section is not None and len(layer2_pkt_section) != 0:
                    export_packet_flow_data_record_layer2_pkt_section_dict_buffer = {}
                    export_packet_flow_data_record_layer2_pkt_section_dict_buffer["id"] = "urn:ngsi-ld:ExportPacketFlowDataRecordLayer2PktSection:" + ":".join(export_packet_flow_data_record_dict_buffer["id"].split(":")[3:])
                    export_packet_flow_data_record_layer2_pkt_section_dict_buffer["type"] = "ExportPacketFlowDataRecordLayer2PktSection"
                    export_packet_flow_data_record_layer2_pkt_section_dict_buffer["isPartOf"] = {}
                    export_packet_flow_data_record_layer2_pkt_section_dict_buffer["isPartOf"]["type"] = "Relationship"
                    export_packet_flow_data_record_layer2_pkt_section_dict_buffer["isPartOf"]["object"] = export_packet_flow_data_record_dict_buffer["id"]
                    export_packet_flow_data_record_layer2_pkt_section_dict_buffer["isPartOf"]["observedAt"] = observed_at
                    offset = layer2_pkt_section.get("offset")
                    if offset is not None:
                        element_text = offset
                        export_packet_flow_data_record_layer2_pkt_section_dict_buffer["offset"] = {}
                        export_packet_flow_data_record_layer2_pkt_section_dict_buffer["offset"]["type"] = "Property"
                        export_packet_flow_data_record_layer2_pkt_section_dict_buffer["offset"]["value"] = int(element_text)
                        export_packet_flow_data_record_layer2_pkt_section_dict_buffer["offset"]["observedAt"] = observed_at
                    size = layer2_pkt_section.get("size")
                    if size is not None:
                        element_text = size
                        export_packet_flow_data_record_layer2_pkt_section_dict_buffer["size"] = {}
                        export_packet_flow_data_record_layer2_pkt_section_dict_buffer["size"]["type"] = "Property"
                        export_packet_flow_data_record_layer2_pkt_section_dict_buffer["size"]["value"] = int(element_text)
                        export_packet_flow_data_record_layer2_pkt_section_dict_buffer["size"]["observedAt"] = observed_at
                    data = layer2_pkt_section.get("data")
                    if data is not None:
                        element_text = data
                        export_packet_flow_data_record_layer2_pkt_section_dict_buffer["data"] = {}
                        export_packet_flow_data_record_layer2_pkt_section_dict_buffer["data"]["type"] = "Property"
                        export_packet_flow_data_record_layer2_pkt_section_dict_buffer["data"]["value"] = element_text
                        export_packet_flow_data_record_layer2_pkt_section_dict_buffer["data"]["observedAt"] = observed_at
                    dict_buffers.append(export_packet_flow_data_record_layer2_pkt_section_dict_buffer)
                flowDuration = flow_data_record.get("netflow-v9-agg:flow-duration")
                if flowDuration is not None:
                    element_text = flowDuration
                    export_packet_flow_data_record_dict_buffer["flowDuration"] = {}
                    export_packet_flow_data_record_dict_buffer["flowDuration"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["flowDuration"]["value"] = int(element_text)
                    export_packet_flow_data_record_dict_buffer["flowDuration"]["observedAt"] = observed_at
                bytesInPerSecond = flow_data_record.get("netflow-v9-agg:bytes-in-per-second")
                if bytesInPerSecond is not None:
                    element_text = bytesInPerSecond
                    export_packet_flow_data_record_dict_buffer["bytesInPerSecond"] = {}
                    export_packet_flow_data_record_dict_buffer["bytesInPerSecond"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["bytesInPerSecond"]["value"] = float(element_text)
                    export_packet_flow_data_record_dict_buffer["bytesInPerSecond"]["observedAt"] = observed_at
                bytesOutPerSecond = flow_data_record.get("netflow-v9-agg:bytes-out-per-second")
                if bytesOutPerSecond is not None:
                    element_text = bytesOutPerSecond
                    export_packet_flow_data_record_dict_buffer["bytesOutPerSecond"] = {}
                    export_packet_flow_data_record_dict_buffer["bytesOutPerSecond"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["bytesOutPerSecond"]["value"] = float(element_text)
                    export_packet_flow_data_record_dict_buffer["bytesOutPerSecond"]["observedAt"] = observed_at
                pktsInPerSecond = flow_data_record.get("netflow-v9-agg:pkts-in-per-second")
                if pktsInPerSecond is not None:
                    element_text = pktsInPerSecond
                    export_packet_flow_data_record_dict_buffer["pktsInPerSecond"] = {}
                    export_packet_flow_data_record_dict_buffer["pktsInPerSecond"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["pktsInPerSecond"]["value"] = float(element_text)
                    export_packet_flow_data_record_dict_buffer["pktsInPerSecond"]["observedAt"] = observed_at
                pktsOutPerSecond = flow_data_record.get("netflow-v9-agg:pkts-out-per-second")
                if pktsOutPerSecond is not None:
                    element_text = pktsOutPerSecond
                    export_packet_flow_data_record_dict_buffer["pktsOutPerSecond"] = {}
                    export_packet_flow_data_record_dict_buffer["pktsOutPerSecond"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["pktsOutPerSecond"]["value"] = float(element_text)
                    export_packet_flow_data_record_dict_buffer["pktsOutPerSecond"]["observedAt"] = observed_at
                bytesInPerPacket = flow_data_record.get("netflow-v9-agg:bytes-in-per-packet")
                if bytesInPerPacket is not None:
                    element_text = bytesInPerPacket
                    export_packet_flow_data_record_dict_buffer["bytesInPerPacket"] = {}
                    export_packet_flow_data_record_dict_buffer["bytesInPerPacket"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["bytesInPerPacket"]["value"] = float(element_text)
                    export_packet_flow_data_record_dict_buffer["bytesInPerPacket"]["observedAt"] = observed_at
                bytesOutPerPacket = flow_data_record.get("netflow-v9-agg:bytes-out-per-packet")
                if bytesOutPerPacket is not None:
                    element_text = bytesOutPerPacket
                    export_packet_flow_data_record_dict_buffer["bytesOutPerPacket"] = {}
                    export_packet_flow_data_record_dict_buffer["bytesOutPerPacket"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["bytesOutPerPacket"]["value"] = float(element_text)
                    export_packet_flow_data_record_dict_buffer["bytesOutPerPacket"]["observedAt"] = observed_at
                ratioBytesInPerOut = flow_data_record.get("netflow-v9-agg:ratio-bytes-in-per-out")
                if ratioBytesInPerOut is not None:
                    element_text = ratioBytesInPerOut
                    export_packet_flow_data_record_dict_buffer["ratioBytesInPerOut"] = {}
                    export_packet_flow_data_record_dict_buffer["ratioBytesInPerOut"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["ratioBytesInPerOut"]["value"] = float(element_text)
                    export_packet_flow_data_record_dict_buffer["ratioBytesInPerOut"]["observedAt"] = observed_at
                ratioPktsInPerOut = flow_data_record.get("netflow-v9-agg:ratio-pkts-in-per-out")
                if ratioPktsInPerOut is not None:
                    element_text = ratioPktsInPerOut
                    export_packet_flow_data_record_dict_buffer["ratioPktsInPerOut"] = {}
                    export_packet_flow_data_record_dict_buffer["ratioPktsInPerOut"]["type"] = "Property"
                    export_packet_flow_data_record_dict_buffer["ratioPktsInPerOut"]["value"] = float(element_text)
                    export_packet_flow_data_record_dict_buffer["ratioPktsInPerOut"]["observedAt"] = observed_at
                dict_buffers.append(export_packet_flow_data_record_dict_buffer)
        dict_buffers.append(export_packet_dict_buffer)

print(json.dumps(dict_buffers[::-1], indent=4))
dict_buffers.clear()
