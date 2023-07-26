import sys
import xml.etree.ElementTree as et
import yaml
import os
import time
import re
import subprocess
import pdb

xml_file = sys.argv[1]
tree = et.parse(xml_file)
root = tree.getroot()

dict_buffers = []

for collector_goflow2 in root.findall(".//{http://data-aggregator.com/ns/netflow}collector-goflow2"):
    collector_goflow2_dict_buffer = {}
    collector_goflow2_dict_buffer["id"] = "urn:ngsi-ld:Collector-goflow2:"
    collector_goflow2_dict_buffer["type"] = "Collector-goflow2"
    timeReceived = collector_goflow2.find(".//{http://data-aggregator.com/ns/netflow}time-received")
    if timeReceived is not None:
        element_text = timeReceived.text
        collector_goflow2_dict_buffer["timeReceived"] = {}
        collector_goflow2_dict_buffer["timeReceived"]["type"] = "Property"
        collector_goflow2_dict_buffer["timeReceived"]["value"] = int(element_text)
    samplerAddress = collector_goflow2.find(".//{http://data-aggregator.com/ns/netflow}sampler-address")
    if samplerAddress is not None:
        element_text = samplerAddress.text
        collector_goflow2_dict_buffer["samplerAddress"] = {}
        collector_goflow2_dict_buffer["samplerAddress"]["type"] = "Property"
        collector_goflow2_dict_buffer["samplerAddress"]["value"] = element_text
    samplerAddressIpv6 = collector_goflow2.find(".//{http://data-aggregator.com/ns/netflow}sampler-address-ipv6")
    if samplerAddressIpv6 is not None:
        element_text = samplerAddressIpv6.text
        collector_goflow2_dict_buffer["samplerAddressIpv6"] = {}
        collector_goflow2_dict_buffer["samplerAddressIpv6"]["type"] = "Property"
        collector_goflow2_dict_buffer["samplerAddressIpv6"]["value"] = element_text
    dict_buffers.append(collector_goflow2_dict_buffer)
for export_packet in root.findall(".//{http://data-aggregator.com/ns/netflow}export-packet"):
    export_packet_dict_buffer = {}
    export_packet_dict_buffer["id"] = "urn:ngsi-ld:Export-packet:"
    export_packet_dict_buffer["type"] = "Export-packet"
    sequenceNumber = export_packet.find(".//{http://data-aggregator.com/ns/netflow}sequence-number")
    if sequenceNumber is not None:
        element_text = sequenceNumber.text
        export_packet_dict_buffer["sequenceNumber"] = {}
        export_packet_dict_buffer["sequenceNumber"]["type"] = "Property"
        export_packet_dict_buffer["sequenceNumber"]["value"] = int(element_text)
    count = export_packet.find(".//{http://data-aggregator.com/ns/netflow}count")
    if count is not None:
        element_text = count.text
        export_packet_dict_buffer["count"] = {}
        export_packet_dict_buffer["count"]["type"] = "Property"
        export_packet_dict_buffer["count"]["value"] = int(element_text)
    systemUptime = export_packet.find(".//{http://data-aggregator.com/ns/netflow}system-uptime")
    if systemUptime is not None:
        element_text = systemUptime.text
        export_packet_dict_buffer["systemUptime"] = {}
        export_packet_dict_buffer["systemUptime"]["type"] = "Property"
        export_packet_dict_buffer["systemUptime"]["value"] = int(element_text)
    unixSeconds = export_packet.find(".//{http://data-aggregator.com/ns/netflow}unix-seconds")
    if unixSeconds is not None:
        element_text = unixSeconds.text
        export_packet_dict_buffer["unixSeconds"] = {}
        export_packet_dict_buffer["unixSeconds"]["type"] = "Property"
        export_packet_dict_buffer["unixSeconds"]["value"] = int(element_text)
    sourceId = export_packet.find(".//{http://data-aggregator.com/ns/netflow}source-id")
    if sourceId is not None:
        element_text = sourceId.text
        export_packet_dict_buffer["sourceId"] = {}
        export_packet_dict_buffer["sourceId"]["type"] = "Property"
        export_packet_dict_buffer["sourceId"]["value"] = int(element_text)
    for flow_data_record in export_packet.findall(".//{http://data-aggregator.com/ns/netflow}flow-data-record"):
        export_packet_flow_data_record_dict_buffer = {}
        export_packet_flow_data_record_dict_buffer["id"] = "urn:ngsi-ld:Flow-data-record:" + export_packet_dict_buffer["id"].split(":")[-1]
        export_packet_flow_data_record_dict_buffer["type"] = "Flow-data-record"
        export_packet_flow_data_record_dict_buffer["isPartOf"] = {}
        export_packet_flow_data_record_dict_buffer["isPartOf"]["type"] = "Relationship"
        export_packet_flow_data_record_dict_buffer["isPartOf"]["object"] = export_packet_dict_buffer["id"]
        flowId = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}flow-id")
        if flowId is not None:
            element_text = flowId.text
            export_packet_flow_data_record_dict_buffer["flowId"] = {}
            export_packet_flow_data_record_dict_buffer["flowId"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["flowId"]["value"] = int(element_text)
        bytesIn = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}bytes-in")
        if bytesIn is not None:
            element_text = bytesIn.text
            export_packet_flow_data_record_dict_buffer["bytesIn"] = {}
            export_packet_flow_data_record_dict_buffer["bytesIn"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["bytesIn"]["value"] = int(element_text)
        bytesOut = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}bytes-out")
        if bytesOut is not None:
            element_text = bytesOut.text
            export_packet_flow_data_record_dict_buffer["bytesOut"] = {}
            export_packet_flow_data_record_dict_buffer["bytesOut"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["bytesOut"]["value"] = int(element_text)
        pktsIn = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}pkts-in")
        if pktsIn is not None:
            element_text = pktsIn.text
            export_packet_flow_data_record_dict_buffer["pktsIn"] = {}
            export_packet_flow_data_record_dict_buffer["pktsIn"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["pktsIn"]["value"] = int(element_text)
        pktsOut = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}pkts-out")
        if pktsOut is not None:
            element_text = pktsOut.text
            export_packet_flow_data_record_dict_buffer["pktsOut"] = {}
            export_packet_flow_data_record_dict_buffer["pktsOut"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["pktsOut"]["value"] = int(element_text)
        flows = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}flows")
        if flows is not None:
            element_text = flows.text
            export_packet_flow_data_record_dict_buffer["flows"] = {}
            export_packet_flow_data_record_dict_buffer["flows"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["flows"]["value"] = int(element_text)
        protocol = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}protocol")
        if protocol is not None:
            element_text = protocol.text
            export_packet_flow_data_record_dict_buffer["protocol"] = {}
            export_packet_flow_data_record_dict_buffer["protocol"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["protocol"]["value"] = element_text
        srcTos = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}src-tos")
        if srcTos is not None:
            element_text = srcTos.text
            export_packet_flow_data_record_dict_buffer["srcTos"] = {}
            export_packet_flow_data_record_dict_buffer["srcTos"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["srcTos"]["value"] = int(element_text)
        dstTos = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}dst-tos")
        if dstTos is not None:
            element_text = dstTos.text
            export_packet_flow_data_record_dict_buffer["dstTos"] = {}
            export_packet_flow_data_record_dict_buffer["dstTos"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["dstTos"]["value"] = int(element_text)
        '''
        tcpFlags = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}tcp-flags")
        if tcpFlags is not None:
            element_text = tcpFlags.text
            export_packet_flow_data_record_dict_buffer["tcpFlags"] = {}
            export_packet_flow_data_record_dict_buffer["tcpFlags"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["tcpFlags"]["value"] = list(element_text)
        '''
        srcPort = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}src-port")
        if srcPort is not None:
            element_text = srcPort.text
            export_packet_flow_data_record_dict_buffer["srcPort"] = {}
            export_packet_flow_data_record_dict_buffer["srcPort"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["srcPort"]["value"] = int(element_text)
        dstPort = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}dst-port")
        if dstPort is not None:
            element_text = dstPort.text
            export_packet_flow_data_record_dict_buffer["dstPort"] = {}
            export_packet_flow_data_record_dict_buffer["dstPort"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["dstPort"]["value"] = int(element_text)
        snmpIn = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}snmp-in")
        if snmpIn is not None:
            element_text = snmpIn.text
            export_packet_flow_data_record_dict_buffer["snmpIn"] = {}
            export_packet_flow_data_record_dict_buffer["snmpIn"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["snmpIn"]["value"] = int(element_text)
        snmpOut = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}snmp-out")
        if snmpOut is not None:
            element_text = snmpOut.text
            export_packet_flow_data_record_dict_buffer["snmpOut"] = {}
            export_packet_flow_data_record_dict_buffer["snmpOut"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["snmpOut"]["value"] = int(element_text)
        bytesOutMul = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}bytes-out-mul")
        if bytesOutMul is not None:
            element_text = bytesOutMul.text
            export_packet_flow_data_record_dict_buffer["bytesOutMul"] = {}
            export_packet_flow_data_record_dict_buffer["bytesOutMul"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["bytesOutMul"]["value"] = int(element_text)
        pktsOutMul = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}pkts-out-mul")
        if pktsOutMul is not None:
            element_text = pktsOutMul.text
            export_packet_flow_data_record_dict_buffer["pktsOutMul"] = {}
            export_packet_flow_data_record_dict_buffer["pktsOutMul"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["pktsOutMul"]["value"] = int(element_text)
        firstSwitched = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}first-switched")
        if firstSwitched is not None:
            element_text = firstSwitched.text
            export_packet_flow_data_record_dict_buffer["firstSwitched"] = {}
            export_packet_flow_data_record_dict_buffer["firstSwitched"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["firstSwitched"]["value"] = int(element_text)
        lastSwitched = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}last-switched")
        if lastSwitched is not None:
            element_text = lastSwitched.text
            export_packet_flow_data_record_dict_buffer["lastSwitched"] = {}
            export_packet_flow_data_record_dict_buffer["lastSwitched"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["lastSwitched"]["value"] = int(element_text)
        minPktLen = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}min-pkt-len")
        if minPktLen is not None:
            element_text = minPktLen.text
            export_packet_flow_data_record_dict_buffer["minPktLen"] = {}
            export_packet_flow_data_record_dict_buffer["minPktLen"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["minPktLen"]["value"] = int(element_text)
        maxPktLen = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}max-pkt-len")
        if maxPktLen is not None:
            element_text = maxPktLen.text
            export_packet_flow_data_record_dict_buffer["maxPktLen"] = {}
            export_packet_flow_data_record_dict_buffer["maxPktLen"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["maxPktLen"]["value"] = int(element_text)
        icmpType = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}icmp-type")
        if icmpType is not None:
            element_text = icmpType.text
            export_packet_flow_data_record_dict_buffer["icmpType"] = {}
            export_packet_flow_data_record_dict_buffer["icmpType"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["icmpType"]["value"] = int(element_text)
        igmpType = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}igmp-type")
        if igmpType is not None:
            element_text = igmpType.text
            export_packet_flow_data_record_dict_buffer["igmpType"] = {}
            export_packet_flow_data_record_dict_buffer["igmpType"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["igmpType"]["value"] = element_text
        samplerName = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}sampler-name")
        if samplerName is not None:
            element_text = samplerName.text
            export_packet_flow_data_record_dict_buffer["samplerName"] = {}
            export_packet_flow_data_record_dict_buffer["samplerName"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["samplerName"]["value"] = element_text
        samplingInterval = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}sampling-interval")
        if samplingInterval is not None:
            element_text = samplingInterval.text
            export_packet_flow_data_record_dict_buffer["samplingInterval"] = {}
            export_packet_flow_data_record_dict_buffer["samplingInterval"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["samplingInterval"]["value"] = int(element_text)
        samplingAlgorithm = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}sampling-algorithm")
        if samplingAlgorithm is not None:
            element_text = samplingAlgorithm.text
            export_packet_flow_data_record_dict_buffer["samplingAlgorithm"] = {}
            export_packet_flow_data_record_dict_buffer["samplingAlgorithm"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["samplingAlgorithm"]["value"] = element_text
        flowActiveTout = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}flow-active-tout")
        if flowActiveTout is not None:
            element_text = flowActiveTout.text
            export_packet_flow_data_record_dict_buffer["flowActiveTout"] = {}
            export_packet_flow_data_record_dict_buffer["flowActiveTout"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["flowActiveTout"]["value"] = int(element_text)
        flowInactiveTout = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}flow-inactive-tout")
        if flowInactiveTout is not None:
            element_text = flowInactiveTout.text
            export_packet_flow_data_record_dict_buffer["flowInactiveTout"] = {}
            export_packet_flow_data_record_dict_buffer["flowInactiveTout"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["flowInactiveTout"]["value"] = int(element_text)
        engineType = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}engine-type")
        if engineType is not None:
            element_text = engineType.text
            export_packet_flow_data_record_dict_buffer["engineType"] = {}
            export_packet_flow_data_record_dict_buffer["engineType"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["engineType"]["value"] = element_text
        engineId = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}engine-id")
        if engineId is not None:
            element_text = engineId.text
            export_packet_flow_data_record_dict_buffer["engineId"] = {}
            export_packet_flow_data_record_dict_buffer["engineId"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["engineId"]["value"] = int(element_text)
        totBytesExp = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}tot-bytes-exp")
        if totBytesExp is not None:
            element_text = totBytesExp.text
            export_packet_flow_data_record_dict_buffer["totBytesExp"] = {}
            export_packet_flow_data_record_dict_buffer["totBytesExp"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["totBytesExp"]["value"] = int(element_text)
        totPktsExp = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}tot-pkts-exp")
        if totPktsExp is not None:
            element_text = totPktsExp.text
            export_packet_flow_data_record_dict_buffer["totPktsExp"] = {}
            export_packet_flow_data_record_dict_buffer["totPktsExp"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["totPktsExp"]["value"] = int(element_text)
        totFlowsExp = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}tot-flows-exp")
        if totFlowsExp is not None:
            element_text = totFlowsExp.text
            export_packet_flow_data_record_dict_buffer["totFlowsExp"] = {}
            export_packet_flow_data_record_dict_buffer["totFlowsExp"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["totFlowsExp"]["value"] = int(element_text)
        flowSamplerId = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}flow-sampler-id")
        if flowSamplerId is not None:
            element_text = flowSamplerId.text
            export_packet_flow_data_record_dict_buffer["flowSamplerId"] = {}
            export_packet_flow_data_record_dict_buffer["flowSamplerId"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["flowSamplerId"]["value"] = int(element_text)
        flowSamplerMode = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}flow-sampler-mode")
        if flowSamplerMode is not None:
            element_text = flowSamplerMode.text
            export_packet_flow_data_record_dict_buffer["flowSamplerMode"] = {}
            export_packet_flow_data_record_dict_buffer["flowSamplerMode"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["flowSamplerMode"]["value"] = element_text
        flowSamplerRandom = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}flow-sampler-random")
        if flowSamplerRandom is not None:
            element_text = flowSamplerRandom.text
            export_packet_flow_data_record_dict_buffer["flowSamplerRandom"] = {}
            export_packet_flow_data_record_dict_buffer["flowSamplerRandom"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["flowSamplerRandom"]["value"] = int(element_text)
        minTtl = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}min-ttl")
        if minTtl is not None:
            element_text = minTtl.text
            export_packet_flow_data_record_dict_buffer["minTtl"] = {}
            export_packet_flow_data_record_dict_buffer["minTtl"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["minTtl"]["value"] = int(element_text)
        maxTtl = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}max-ttl")
        if maxTtl is not None:
            element_text = maxTtl.text
            export_packet_flow_data_record_dict_buffer["maxTtl"] = {}
            export_packet_flow_data_record_dict_buffer["maxTtl"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["maxTtl"]["value"] = int(element_text)
        srcMacIn = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}src-mac-in")
        if srcMacIn is not None:
            element_text = srcMacIn.text
            export_packet_flow_data_record_dict_buffer["srcMacIn"] = {}
            export_packet_flow_data_record_dict_buffer["srcMacIn"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["srcMacIn"]["value"] = element_text
        dstMacIn = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}dst-mac-in")
        if dstMacIn is not None:
            element_text = dstMacIn.text
            export_packet_flow_data_record_dict_buffer["dstMacIn"] = {}
            export_packet_flow_data_record_dict_buffer["dstMacIn"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["dstMacIn"]["value"] = element_text
        srcMacOut = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}src-mac-out")
        if srcMacOut is not None:
            element_text = srcMacOut.text
            export_packet_flow_data_record_dict_buffer["srcMacOut"] = {}
            export_packet_flow_data_record_dict_buffer["srcMacOut"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["srcMacOut"]["value"] = element_text
        dstMacOut = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}dst-mac-out")
        if dstMacOut is not None:
            element_text = dstMacOut.text
            export_packet_flow_data_record_dict_buffer["dstMacOut"] = {}
            export_packet_flow_data_record_dict_buffer["dstMacOut"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["dstMacOut"]["value"] = element_text
        ipVersion = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}ip-version")
        if ipVersion is not None:
            element_text = ipVersion.text
            export_packet_flow_data_record_dict_buffer["ipVersion"] = {}
            export_packet_flow_data_record_dict_buffer["ipVersion"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["ipVersion"]["value"] = element_text
        direction = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}direction")
        if direction is not None:
            element_text = direction.text
            export_packet_flow_data_record_dict_buffer["direction"] = {}
            export_packet_flow_data_record_dict_buffer["direction"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["direction"]["value"] = element_text
        ifName = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}if-name")
        if ifName is not None:
            element_text = ifName.text
            export_packet_flow_data_record_dict_buffer["ifName"] = {}
            export_packet_flow_data_record_dict_buffer["ifName"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["ifName"]["value"] = element_text
        ifDesc = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}if-desc")
        if ifDesc is not None:
            element_text = ifDesc.text
            export_packet_flow_data_record_dict_buffer["ifDesc"] = {}
            export_packet_flow_data_record_dict_buffer["ifDesc"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["ifDesc"]["value"] = element_text
        fragOffset = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}frag-offset")
        if fragOffset is not None:
            element_text = fragOffset.text
            export_packet_flow_data_record_dict_buffer["fragOffset"] = {}
            export_packet_flow_data_record_dict_buffer["fragOffset"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["fragOffset"]["value"] = int(element_text)
        forwardingStatus = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}forwarding-status")
        if forwardingStatus is not None:
            element_text = forwardingStatus.text
            export_packet_flow_data_record_dict_buffer["forwardingStatus"] = {}
            export_packet_flow_data_record_dict_buffer["forwardingStatus"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["forwardingStatus"]["value"] = element_text
        postipDscp = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}postip-dscp")
        if postipDscp is not None:
            element_text = postipDscp.text
            export_packet_flow_data_record_dict_buffer["postipDscp"] = {}
            export_packet_flow_data_record_dict_buffer["postipDscp"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["postipDscp"]["value"] = int(element_text)
        replFactorMul = flow_data_record.find(".//{http://data-aggregator.com/ns/netflow}repl-factor-mul")
        if replFactorMul is not None:
            element_text = replFactorMul.text
            export_packet_flow_data_record_dict_buffer["replFactorMul"] = {}
            export_packet_flow_data_record_dict_buffer["replFactorMul"]["type"] = "Property"
            export_packet_flow_data_record_dict_buffer["replFactorMul"]["value"] = int(element_text)
        for ipv4 in flow_data_record.findall(".//{http://data-aggregator.com/ns/netflow}ipv4"):
            export_packet_flow_data_record_ipv4_dict_buffer = {}
            export_packet_flow_data_record_ipv4_dict_buffer["id"] = "urn:ngsi-ld:Ipv4:" + export_packet_flow_data_record_dict_buffer["id"].split(":")[-1]
            export_packet_flow_data_record_ipv4_dict_buffer["type"] = "Ipv4"
            export_packet_flow_data_record_ipv4_dict_buffer["isPartOf"] = {}
            export_packet_flow_data_record_ipv4_dict_buffer["isPartOf"]["type"] = "Relationship"
            export_packet_flow_data_record_ipv4_dict_buffer["isPartOf"]["object"] = export_packet_flow_data_record_dict_buffer["id"]
            srcAddress = ipv4.find(".//{http://data-aggregator.com/ns/netflow}src-address")
            if srcAddress is not None:
                element_text = srcAddress.text
                export_packet_flow_data_record_ipv4_dict_buffer["srcAddress"] = {}
                export_packet_flow_data_record_ipv4_dict_buffer["srcAddress"]["type"] = "Property"
                export_packet_flow_data_record_ipv4_dict_buffer["srcAddress"]["value"] = element_text
            dstAddress = ipv4.find(".//{http://data-aggregator.com/ns/netflow}dst-address")
            if dstAddress is not None:
                element_text = dstAddress.text
                export_packet_flow_data_record_ipv4_dict_buffer["dstAddress"] = {}
                export_packet_flow_data_record_ipv4_dict_buffer["dstAddress"]["type"] = "Property"
                export_packet_flow_data_record_ipv4_dict_buffer["dstAddress"]["value"] = element_text
            srcMask = ipv4.find(".//{http://data-aggregator.com/ns/netflow}src-mask")
            if srcMask is not None:
                element_text = srcMask.text
                export_packet_flow_data_record_ipv4_dict_buffer["srcMask"] = {}
                export_packet_flow_data_record_ipv4_dict_buffer["srcMask"]["type"] = "Relationship"
                export_packet_flow_data_record_ipv4_dict_buffer["srcMask"]["object"] = "urn:ngsi-ld:Ipv4:" + element_text
            dstMask = ipv4.find(".//{http://data-aggregator.com/ns/netflow}dst-mask")
            if dstMask is not None:
                element_text = dstMask.text
                export_packet_flow_data_record_ipv4_dict_buffer["dstMask"] = {}
                export_packet_flow_data_record_ipv4_dict_buffer["dstMask"]["type"] = "Relationship"
                export_packet_flow_data_record_ipv4_dict_buffer["dstMask"]["object"] = "urn:ngsi-ld:Ipv4:" + element_text
            srcPrefix = ipv4.find(".//{http://data-aggregator.com/ns/netflow}src-prefix")
            if srcPrefix is not None:
                element_text = srcPrefix.text
                export_packet_flow_data_record_ipv4_dict_buffer["srcPrefix"] = {}
                export_packet_flow_data_record_ipv4_dict_buffer["srcPrefix"]["type"] = "Relationship"
                export_packet_flow_data_record_ipv4_dict_buffer["srcPrefix"]["object"] = "urn:ngsi-ld:Ipv4:" + element_text
            dstPrefix = ipv4.find(".//{http://data-aggregator.com/ns/netflow}dst-prefix")
            if dstPrefix is not None:
                element_text = dstPrefix.text
                export_packet_flow_data_record_ipv4_dict_buffer["dstPrefix"] = {}
                export_packet_flow_data_record_ipv4_dict_buffer["dstPrefix"]["type"] = "Relationship"
                export_packet_flow_data_record_ipv4_dict_buffer["dstPrefix"]["object"] = "urn:ngsi-ld:Ipv4:" + element_text
            nextHop = ipv4.find(".//{http://data-aggregator.com/ns/netflow}next-hop")
            if nextHop is not None:
                element_text = nextHop.text
                export_packet_flow_data_record_ipv4_dict_buffer["nextHop"] = {}
                export_packet_flow_data_record_ipv4_dict_buffer["nextHop"]["type"] = "Property"
                export_packet_flow_data_record_ipv4_dict_buffer["nextHop"]["value"] = element_text
            identification = ipv4.find(".//{http://data-aggregator.com/ns/netflow}identification")
            if identification is not None:
                element_text = identification.text
                export_packet_flow_data_record_ipv4_dict_buffer["identification"] = {}
                export_packet_flow_data_record_ipv4_dict_buffer["identification"]["type"] = "Property"
                export_packet_flow_data_record_ipv4_dict_buffer["identification"]["value"] = int(element_text)
            dict_buffers.append(export_packet_flow_data_record_ipv4_dict_buffer)
        for ipv6 in flow_data_record.findall(".//{http://data-aggregator.com/ns/netflow}ipv6"):
            export_packet_flow_data_record_ipv6_dict_buffer = {}
            export_packet_flow_data_record_ipv6_dict_buffer["id"] = "urn:ngsi-ld:Ipv6:" + export_packet_flow_data_record_dict_buffer["id"].split(":")[-1]
            export_packet_flow_data_record_ipv6_dict_buffer["type"] = "Ipv6"
            export_packet_flow_data_record_ipv6_dict_buffer["isPartOf"] = {}
            export_packet_flow_data_record_ipv6_dict_buffer["isPartOf"]["type"] = "Relationship"
            export_packet_flow_data_record_ipv6_dict_buffer["isPartOf"]["object"] = export_packet_flow_data_record_dict_buffer["id"]
            srcAddress = ipv6.find(".//{http://data-aggregator.com/ns/netflow}src-address")
            if srcAddress is not None:
                element_text = srcAddress.text
                export_packet_flow_data_record_ipv6_dict_buffer["srcAddress"] = {}
                export_packet_flow_data_record_ipv6_dict_buffer["srcAddress"]["type"] = "Property"
                export_packet_flow_data_record_ipv6_dict_buffer["srcAddress"]["value"] = element_text
            dstAddress = ipv6.find(".//{http://data-aggregator.com/ns/netflow}dst-address")
            if dstAddress is not None:
                element_text = dstAddress.text
                export_packet_flow_data_record_ipv6_dict_buffer["dstAddress"] = {}
                export_packet_flow_data_record_ipv6_dict_buffer["dstAddress"]["type"] = "Property"
                export_packet_flow_data_record_ipv6_dict_buffer["dstAddress"]["value"] = element_text
            srcMask = ipv6.find(".//{http://data-aggregator.com/ns/netflow}src-mask")
            if srcMask is not None:
                element_text = srcMask.text
                export_packet_flow_data_record_ipv6_dict_buffer["srcMask"] = {}
                export_packet_flow_data_record_ipv6_dict_buffer["srcMask"]["type"] = "Relationship"
                export_packet_flow_data_record_ipv6_dict_buffer["srcMask"]["object"] = "urn:ngsi-ld:Ipv6:" + element_text
            dstMask = ipv6.find(".//{http://data-aggregator.com/ns/netflow}dst-mask")
            if dstMask is not None:
                element_text = dstMask.text
                export_packet_flow_data_record_ipv6_dict_buffer["dstMask"] = {}
                export_packet_flow_data_record_ipv6_dict_buffer["dstMask"]["type"] = "Relationship"
                export_packet_flow_data_record_ipv6_dict_buffer["dstMask"]["object"] = "urn:ngsi-ld:Ipv6:" + element_text
            nextHop = ipv6.find(".//{http://data-aggregator.com/ns/netflow}next-hop")
            if nextHop is not None:
                element_text = nextHop.text
                export_packet_flow_data_record_ipv6_dict_buffer["nextHop"] = {}
                export_packet_flow_data_record_ipv6_dict_buffer["nextHop"]["type"] = "Property"
                export_packet_flow_data_record_ipv6_dict_buffer["nextHop"]["value"] = element_text
            flowLabel = ipv6.find(".//{http://data-aggregator.com/ns/netflow}flow-label")
            if flowLabel is not None:
                element_text = flowLabel.text
                export_packet_flow_data_record_ipv6_dict_buffer["flowLabel"] = {}
                export_packet_flow_data_record_ipv6_dict_buffer["flowLabel"]["type"] = "Property"
                export_packet_flow_data_record_ipv6_dict_buffer["flowLabel"]["value"] = int(element_text)
            optHeaders = ipv6.find(".//{http://data-aggregator.com/ns/netflow}opt-headers")
            if optHeaders is not None:
                element_text = optHeaders.text
                export_packet_flow_data_record_ipv6_dict_buffer["optHeaders"] = {}
                export_packet_flow_data_record_ipv6_dict_buffer["optHeaders"]["type"] = "Property"
                export_packet_flow_data_record_ipv6_dict_buffer["optHeaders"]["value"] = int(element_text)
            dict_buffers.append(export_packet_flow_data_record_ipv6_dict_buffer)
        for mpls in flow_data_record.findall(".//{http://data-aggregator.com/ns/netflow}mpls"):
            export_packet_flow_data_record_mpls_dict_buffer = {}
            export_packet_flow_data_record_mpls_dict_buffer["id"] = "urn:ngsi-ld:Mpls:" + export_packet_flow_data_record_dict_buffer["id"].split(":")[-1]
            export_packet_flow_data_record_mpls_dict_buffer["type"] = "Mpls"
            export_packet_flow_data_record_mpls_dict_buffer["isPartOf"] = {}
            export_packet_flow_data_record_mpls_dict_buffer["isPartOf"]["type"] = "Relationship"
            export_packet_flow_data_record_mpls_dict_buffer["isPartOf"]["object"] = export_packet_flow_data_record_dict_buffer["id"]
            palRd = mpls.find(".//{http://data-aggregator.com/ns/netflow}pal-rd")
            if palRd is not None:
                element_text = palRd.text
                export_packet_flow_data_record_mpls_dict_buffer["palRd"] = {}
                export_packet_flow_data_record_mpls_dict_buffer["palRd"]["type"] = "Property"
                export_packet_flow_data_record_mpls_dict_buffer["palRd"]["value"] = int(element_text)
            prefixLen = mpls.find(".//{http://data-aggregator.com/ns/netflow}prefix-len")
            if prefixLen is not None:
                element_text = prefixLen.text
                export_packet_flow_data_record_mpls_dict_buffer["prefixLen"] = {}
                export_packet_flow_data_record_mpls_dict_buffer["prefixLen"]["type"] = "Relationship"
                export_packet_flow_data_record_mpls_dict_buffer["prefixLen"]["object"] = "urn:ngsi-ld:Mpls:" + element_text
            topLabelType = mpls.find(".//{http://data-aggregator.com/ns/netflow}top-label-type")
            if topLabelType is not None:
                element_text = topLabelType.text
                export_packet_flow_data_record_mpls_dict_buffer["topLabelType"] = {}
                export_packet_flow_data_record_mpls_dict_buffer["topLabelType"]["type"] = "Property"
                export_packet_flow_data_record_mpls_dict_buffer["topLabelType"]["value"] = element_text
            topLabelIp = mpls.find(".//{http://data-aggregator.com/ns/netflow}top-label-ip")
            if topLabelIp is not None:
                element_text = topLabelIp.text
                export_packet_flow_data_record_mpls_dict_buffer["topLabelIp"] = {}
                export_packet_flow_data_record_mpls_dict_buffer["topLabelIp"]["type"] = "Property"
                export_packet_flow_data_record_mpls_dict_buffer["topLabelIp"]["value"] = element_text
            label1 = mpls.find(".//{http://data-aggregator.com/ns/netflow}label-1")
            if label1 is not None:
                element_text = label1.text
                export_packet_flow_data_record_mpls_dict_buffer["label1"] = {}
                export_packet_flow_data_record_mpls_dict_buffer["label1"]["type"] = "Property"
                export_packet_flow_data_record_mpls_dict_buffer["label1"]["value"] = int(element_text)
            label2 = mpls.find(".//{http://data-aggregator.com/ns/netflow}label-2")
            if label2 is not None:
                element_text = label2.text
                export_packet_flow_data_record_mpls_dict_buffer["label2"] = {}
                export_packet_flow_data_record_mpls_dict_buffer["label2"]["type"] = "Property"
                export_packet_flow_data_record_mpls_dict_buffer["label2"]["value"] = int(element_text)
            label3 = mpls.find(".//{http://data-aggregator.com/ns/netflow}label-3")
            if label3 is not None:
                element_text = label3.text
                export_packet_flow_data_record_mpls_dict_buffer["label3"] = {}
                export_packet_flow_data_record_mpls_dict_buffer["label3"]["type"] = "Property"
                export_packet_flow_data_record_mpls_dict_buffer["label3"]["value"] = int(element_text)
            label4 = mpls.find(".//{http://data-aggregator.com/ns/netflow}label-4")
            if label4 is not None:
                element_text = label4.text
                export_packet_flow_data_record_mpls_dict_buffer["label4"] = {}
                export_packet_flow_data_record_mpls_dict_buffer["label4"]["type"] = "Property"
                export_packet_flow_data_record_mpls_dict_buffer["label4"]["value"] = int(element_text)
            label5 = mpls.find(".//{http://data-aggregator.com/ns/netflow}label-5")
            if label5 is not None:
                element_text = label5.text
                export_packet_flow_data_record_mpls_dict_buffer["label5"] = {}
                export_packet_flow_data_record_mpls_dict_buffer["label5"]["type"] = "Property"
                export_packet_flow_data_record_mpls_dict_buffer["label5"]["value"] = int(element_text)
            label6 = mpls.find(".//{http://data-aggregator.com/ns/netflow}label-6")
            if label6 is not None:
                element_text = label6.text
                export_packet_flow_data_record_mpls_dict_buffer["label6"] = {}
                export_packet_flow_data_record_mpls_dict_buffer["label6"]["type"] = "Property"
                export_packet_flow_data_record_mpls_dict_buffer["label6"]["value"] = int(element_text)
            label7 = mpls.find(".//{http://data-aggregator.com/ns/netflow}label-7")
            if label7 is not None:
                element_text = label7.text
                export_packet_flow_data_record_mpls_dict_buffer["label7"] = {}
                export_packet_flow_data_record_mpls_dict_buffer["label7"]["type"] = "Property"
                export_packet_flow_data_record_mpls_dict_buffer["label7"]["value"] = int(element_text)
            label8 = mpls.find(".//{http://data-aggregator.com/ns/netflow}label-8")
            if label8 is not None:
                element_text = label8.text
                export_packet_flow_data_record_mpls_dict_buffer["label8"] = {}
                export_packet_flow_data_record_mpls_dict_buffer["label8"]["type"] = "Property"
                export_packet_flow_data_record_mpls_dict_buffer["label8"]["value"] = int(element_text)
            label9 = mpls.find(".//{http://data-aggregator.com/ns/netflow}label-9")
            if label9 is not None:
                element_text = label9.text
                export_packet_flow_data_record_mpls_dict_buffer["label9"] = {}
                export_packet_flow_data_record_mpls_dict_buffer["label9"]["type"] = "Property"
                export_packet_flow_data_record_mpls_dict_buffer["label9"]["value"] = int(element_text)
            label10 = mpls.find(".//{http://data-aggregator.com/ns/netflow}label-10")
            if label10 is not None:
                element_text = label10.text
                export_packet_flow_data_record_mpls_dict_buffer["label10"] = {}
                export_packet_flow_data_record_mpls_dict_buffer["label10"]["type"] = "Property"
                export_packet_flow_data_record_mpls_dict_buffer["label10"]["value"] = int(element_text)
            dict_buffers.append(export_packet_flow_data_record_mpls_dict_buffer)
        for bgp in flow_data_record.findall(".//{http://data-aggregator.com/ns/netflow}bgp"):
            export_packet_flow_data_record_bgp_dict_buffer = {}
            export_packet_flow_data_record_bgp_dict_buffer["id"] = "urn:ngsi-ld:Bgp:" + export_packet_flow_data_record_dict_buffer["id"].split(":")[-1]
            export_packet_flow_data_record_bgp_dict_buffer["type"] = "Bgp"
            export_packet_flow_data_record_bgp_dict_buffer["isPartOf"] = {}
            export_packet_flow_data_record_bgp_dict_buffer["isPartOf"]["type"] = "Relationship"
            export_packet_flow_data_record_bgp_dict_buffer["isPartOf"]["object"] = export_packet_flow_data_record_dict_buffer["id"]
            srcAs = bgp.find(".//{http://data-aggregator.com/ns/netflow}src-as")
            if srcAs is not None:
                element_text = srcAs.text
                export_packet_flow_data_record_bgp_dict_buffer["srcAs"] = {}
                export_packet_flow_data_record_bgp_dict_buffer["srcAs"]["type"] = "Property"
                export_packet_flow_data_record_bgp_dict_buffer["srcAs"]["value"] = int(element_text)
            dstAs = bgp.find(".//{http://data-aggregator.com/ns/netflow}dst-as")
            if dstAs is not None:
                element_text = dstAs.text
                export_packet_flow_data_record_bgp_dict_buffer["dstAs"] = {}
                export_packet_flow_data_record_bgp_dict_buffer["dstAs"]["type"] = "Property"
                export_packet_flow_data_record_bgp_dict_buffer["dstAs"]["value"] = int(element_text)
            nextHop = bgp.find(".//{http://data-aggregator.com/ns/netflow}next-hop")
            if nextHop is not None:
                element_text = nextHop.text
                export_packet_flow_data_record_bgp_dict_buffer["nextHop"] = {}
                export_packet_flow_data_record_bgp_dict_buffer["nextHop"]["type"] = "Property"
                export_packet_flow_data_record_bgp_dict_buffer["nextHop"]["value"] = element_text
            nextHopIpv6 = bgp.find(".//{http://data-aggregator.com/ns/netflow}next-hop-ipv6")
            if nextHopIpv6 is not None:
                element_text = nextHopIpv6.text
                export_packet_flow_data_record_bgp_dict_buffer["nextHopIpv6"] = {}
                export_packet_flow_data_record_bgp_dict_buffer["nextHopIpv6"]["type"] = "Property"
                export_packet_flow_data_record_bgp_dict_buffer["nextHopIpv6"]["value"] = element_text
            srcTrafficId = bgp.find(".//{http://data-aggregator.com/ns/netflow}src-traffic-id")
            if srcTrafficId is not None:
                element_text = srcTrafficId.text
                export_packet_flow_data_record_bgp_dict_buffer["srcTrafficId"] = {}
                export_packet_flow_data_record_bgp_dict_buffer["srcTrafficId"]["type"] = "Property"
                export_packet_flow_data_record_bgp_dict_buffer["srcTrafficId"]["value"] = int(element_text)
            dstTrafficId = bgp.find(".//{http://data-aggregator.com/ns/netflow}dst-traffic-id")
            if dstTrafficId is not None:
                element_text = dstTrafficId.text
                export_packet_flow_data_record_bgp_dict_buffer["dstTrafficId"] = {}
                export_packet_flow_data_record_bgp_dict_buffer["dstTrafficId"]["type"] = "Property"
                export_packet_flow_data_record_bgp_dict_buffer["dstTrafficId"]["value"] = int(element_text)
            dict_buffers.append(export_packet_flow_data_record_bgp_dict_buffer)
        for vlan in flow_data_record.findall(".//{http://data-aggregator.com/ns/netflow}vlan"):
            export_packet_flow_data_record_vlan_dict_buffer = {}
            export_packet_flow_data_record_vlan_dict_buffer["id"] = "urn:ngsi-ld:Vlan:" + export_packet_flow_data_record_dict_buffer["id"].split(":")[-1]
            export_packet_flow_data_record_vlan_dict_buffer["type"] = "Vlan"
            export_packet_flow_data_record_vlan_dict_buffer["isPartOf"] = {}
            export_packet_flow_data_record_vlan_dict_buffer["isPartOf"]["type"] = "Relationship"
            export_packet_flow_data_record_vlan_dict_buffer["isPartOf"]["object"] = export_packet_flow_data_record_dict_buffer["id"]
            srcId = vlan.find(".//{http://data-aggregator.com/ns/netflow}src-id")
            if srcId is not None:
                element_text = srcId.text
                export_packet_flow_data_record_vlan_dict_buffer["srcId"] = {}
                export_packet_flow_data_record_vlan_dict_buffer["srcId"]["type"] = "Property"
                export_packet_flow_data_record_vlan_dict_buffer["srcId"]["value"] = int(element_text)
            dstId = vlan.find(".//{http://data-aggregator.com/ns/netflow}dst-id")
            if dstId is not None:
                element_text = dstId.text
                export_packet_flow_data_record_vlan_dict_buffer["dstId"] = {}
                export_packet_flow_data_record_vlan_dict_buffer["dstId"]["type"] = "Property"
                export_packet_flow_data_record_vlan_dict_buffer["dstId"]["value"] = int(element_text)
            dict_buffers.append(export_packet_flow_data_record_vlan_dict_buffer)
        for permanent_flow in flow_data_record.findall(".//{http://data-aggregator.com/ns/netflow}permanent-flow"):
            export_packet_flow_data_record_permanent_flow_dict_buffer = {}
            export_packet_flow_data_record_permanent_flow_dict_buffer["id"] = "urn:ngsi-ld:Permanent-flow:" + export_packet_flow_data_record_dict_buffer["id"].split(":")[-1]
            export_packet_flow_data_record_permanent_flow_dict_buffer["type"] = "Permanent-flow"
            export_packet_flow_data_record_permanent_flow_dict_buffer["isPartOf"] = {}
            export_packet_flow_data_record_permanent_flow_dict_buffer["isPartOf"]["type"] = "Relationship"
            export_packet_flow_data_record_permanent_flow_dict_buffer["isPartOf"]["object"] = export_packet_flow_data_record_dict_buffer["id"]
            bytesIn = permanent_flow.find(".//{http://data-aggregator.com/ns/netflow}bytes-in")
            if bytesIn is not None:
                element_text = bytesIn.text
                export_packet_flow_data_record_permanent_flow_dict_buffer["bytesIn"] = {}
                export_packet_flow_data_record_permanent_flow_dict_buffer["bytesIn"]["type"] = "Property"
                export_packet_flow_data_record_permanent_flow_dict_buffer["bytesIn"]["value"] = int(element_text)
            pktsIn = permanent_flow.find(".//{http://data-aggregator.com/ns/netflow}pkts-in")
            if pktsIn is not None:
                element_text = pktsIn.text
                export_packet_flow_data_record_permanent_flow_dict_buffer["pktsIn"] = {}
                export_packet_flow_data_record_permanent_flow_dict_buffer["pktsIn"]["type"] = "Property"
                export_packet_flow_data_record_permanent_flow_dict_buffer["pktsIn"]["value"] = int(element_text)
            dict_buffers.append(export_packet_flow_data_record_permanent_flow_dict_buffer)
        for application in flow_data_record.findall(".//{http://data-aggregator.com/ns/netflow}application"):
            export_packet_flow_data_record_application_dict_buffer = {}
            export_packet_flow_data_record_application_dict_buffer["id"] = "urn:ngsi-ld:Application:" + export_packet_flow_data_record_dict_buffer["id"].split(":")[-1]
            export_packet_flow_data_record_application_dict_buffer["type"] = "Application"
            export_packet_flow_data_record_application_dict_buffer["isPartOf"] = {}
            export_packet_flow_data_record_application_dict_buffer["isPartOf"]["type"] = "Relationship"
            export_packet_flow_data_record_application_dict_buffer["isPartOf"]["object"] = export_packet_flow_data_record_dict_buffer["id"]
            desc = application.find(".//{http://data-aggregator.com/ns/netflow}desc")
            if desc is not None:
                element_text = desc.text
                export_packet_flow_data_record_application_dict_buffer["desc"] = {}
                export_packet_flow_data_record_application_dict_buffer["desc"]["type"] = "Property"
                export_packet_flow_data_record_application_dict_buffer["desc"]["value"] = element_text
            tag = application.find(".//{http://data-aggregator.com/ns/netflow}tag")
            if tag is not None:
                element_text = tag.text
                export_packet_flow_data_record_application_dict_buffer["tag"] = {}
                export_packet_flow_data_record_application_dict_buffer["tag"]["type"] = "Property"
                export_packet_flow_data_record_application_dict_buffer["tag"]["value"] = element_text
            name = application.find(".//{http://data-aggregator.com/ns/netflow}name")
            if name is not None:
                element_text = name.text
                export_packet_flow_data_record_application_dict_buffer["id"] = export_packet_flow_data_record_application_dict_buffer["id"] + element_text
                export_packet_flow_data_record_application_dict_buffer["name"] = {}
                export_packet_flow_data_record_application_dict_buffer["name"]["type"] = "Property"
                export_packet_flow_data_record_application_dict_buffer["name"]["value"] = element_text
            dict_buffers.append(export_packet_flow_data_record_application_dict_buffer)
        for layer2_pkt_section in flow_data_record.findall(".//{http://data-aggregator.com/ns/netflow}layer2-pkt-section"):
            export_packet_flow_data_record_layer2_pkt_section_dict_buffer = {}
            export_packet_flow_data_record_layer2_pkt_section_dict_buffer["id"] = "urn:ngsi-ld:Layer2-pkt-section:" + export_packet_flow_data_record_dict_buffer["id"].split(":")[-1]
            export_packet_flow_data_record_layer2_pkt_section_dict_buffer["type"] = "Layer2-pkt-section"
            export_packet_flow_data_record_layer2_pkt_section_dict_buffer["isPartOf"] = {}
            export_packet_flow_data_record_layer2_pkt_section_dict_buffer["isPartOf"]["type"] = "Relationship"
            export_packet_flow_data_record_layer2_pkt_section_dict_buffer["isPartOf"]["object"] = export_packet_flow_data_record_dict_buffer["id"]
            offset = layer2_pkt_section.find(".//{http://data-aggregator.com/ns/netflow}offset")
            if offset is not None:
                element_text = offset.text
                export_packet_flow_data_record_layer2_pkt_section_dict_buffer["offset"] = {}
                export_packet_flow_data_record_layer2_pkt_section_dict_buffer["offset"]["type"] = "Property"
                export_packet_flow_data_record_layer2_pkt_section_dict_buffer["offset"]["value"] = int(element_text)
            size = layer2_pkt_section.find(".//{http://data-aggregator.com/ns/netflow}size")
            if size is not None:
                element_text = size.text
                export_packet_flow_data_record_layer2_pkt_section_dict_buffer["size"] = {}
                export_packet_flow_data_record_layer2_pkt_section_dict_buffer["size"]["type"] = "Property"
                export_packet_flow_data_record_layer2_pkt_section_dict_buffer["size"]["value"] = int(element_text)
            data = layer2_pkt_section.find(".//{http://data-aggregator.com/ns/netflow}data")
            if data is not None:
                element_text = data.text
                export_packet_flow_data_record_layer2_pkt_section_dict_buffer["data"] = {}
                export_packet_flow_data_record_layer2_pkt_section_dict_buffer["data"]["type"] = "Property"
                export_packet_flow_data_record_layer2_pkt_section_dict_buffer["data"]["value"] = element_text
            dict_buffers.append(export_packet_flow_data_record_layer2_pkt_section_dict_buffer)
        dict_buffers.append(export_packet_flow_data_record_dict_buffer)
    dict_buffers.append(export_packet_dict_buffer)

# Print dictionary buffers:

for buffer in dict_buffers[::-1]:
	print(buffer)
	print('\n')

