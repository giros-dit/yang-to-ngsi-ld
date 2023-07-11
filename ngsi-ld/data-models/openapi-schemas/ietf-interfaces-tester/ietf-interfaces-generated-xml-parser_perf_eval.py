# Modified to include performance tests.

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
'''
import ngsi_ld_client
from fastapi import FastAPI, Request, status
from ngsi_ld_client.api_client import ApiClient as NGSILDClient
from ngsi_ld_client.configuration import Configuration as NGSILDConfiguration
from ngsi_ld_client.exceptions import ApiException
'''

xml_file = sys.argv[1]

# from ngsi_ld_models.models.interface import Interface
interface_dict_buffers = []

# from ngsi_ld_models.models.statistics import Statistics
interface_statistics_dict_buffers = []

parsing_exec_times = []
EXEC_TIMES = 1000

for i in range (0, EXEC_TIMES):
    start_time = time.perf_counter_ns()

    tree = et.parse(xml_file)
    root = tree.getroot()

    for interface in root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}interface"):
        interface_dict_buffer = {}
        interface_dict_buffer["id"] = "urn:ngsi-ld:Interface:"
        interface_dict_buffer["type"] = "Interface"
        name = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}name")
        if name is not None:
            element_text = name.text
            interface_dict_buffer["id"] = interface_dict_buffer["id"] + element_text
            interface_dict_buffer["name"] = {}
            interface_dict_buffer["name"]["type"] = "Property"
            interface_dict_buffer["name"]["value"] = element_text
        description = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}description")
        if description is not None:
            element_text = description.text
            interface_dict_buffer["description"] = {}
            interface_dict_buffer["description"]["type"] = "Property"
            interface_dict_buffer["description"]["value"] = element_text
        enabled = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}enabled")
        if enabled is not None:
            element_text = enabled.text
            interface_dict_buffer["enabled"] = {}
            interface_dict_buffer["enabled"]["type"] = "Property"
            interface_dict_buffer["enabled"]["value"] = element_text.capitalize()
        linkUpDownTrapEnable = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}link-up-down-trap-enable")
        if linkUpDownTrapEnable is not None:
            element_text = linkUpDownTrapEnable.text
            interface_dict_buffer["linkUpDownTrapEnable"] = {}
            interface_dict_buffer["linkUpDownTrapEnable"]["type"] = "Property"
            interface_dict_buffer["linkUpDownTrapEnable"]["value"] = element_text
        adminStatus = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}admin-status")
        if adminStatus is not None:
            element_text = adminStatus.text
            interface_dict_buffer["adminStatus"] = {}
            interface_dict_buffer["adminStatus"]["type"] = "Property"
            interface_dict_buffer["adminStatus"]["value"] = element_text
        operStatus = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}oper-status")
        if operStatus is not None:
            element_text = operStatus.text
            interface_dict_buffer["operStatus"] = {}
            interface_dict_buffer["operStatus"]["type"] = "Property"
            interface_dict_buffer["operStatus"]["value"] = element_text
        lastChange = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}last-change")
        if lastChange is not None:
            element_text = lastChange.text
            interface_dict_buffer["lastChange"] = {}
            interface_dict_buffer["lastChange"]["type"] = "Property"
            interface_dict_buffer["lastChange"]["value"] = element_text
        ifIndex = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}if-index")
        if ifIndex is not None:
            element_text = ifIndex.text
            interface_dict_buffer["ifIndex"] = {}
            interface_dict_buffer["ifIndex"]["type"] = "Property"
            interface_dict_buffer["ifIndex"]["value"] = int(element_text)
        physAddress = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}phys-address")
        if physAddress is not None:
            element_text = physAddress.text
            interface_dict_buffer["physAddress"] = {}
            interface_dict_buffer["physAddress"]["type"] = "Property"
            interface_dict_buffer["physAddress"]["value"] = element_text
        higherLayerIf = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}higher-layer-if")
        if higherLayerIf is not None:
            element_text = higherLayerIf.text
            interface_dict_buffer["higherLayerIf"] = {}
            interface_dict_buffer["higherLayerIf"]["type"] = "Relationship"
            interface_dict_buffer["higherLayerIf"]["object"] = "urn:ngsi-ld:Interface:" + element_text
        lowerLayerIf = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}lower-layer-if")
        if lowerLayerIf is not None:
            element_text = lowerLayerIf.text
            interface_dict_buffer["lowerLayerIf"] = {}
            interface_dict_buffer["lowerLayerIf"]["type"] = "Relationship"
            interface_dict_buffer["lowerLayerIf"]["object"] = "urn:ngsi-ld:Interface:" + element_text
        speed = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}speed")
        if speed is not None:
            element_text = speed.text
            interface_dict_buffer["speed"] = {}
            interface_dict_buffer["speed"]["type"] = "Property"
            interface_dict_buffer["speed"]["value"] = int(element_text)
        for statistics in interface.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}statistics"):
            interface_statistics_dict_buffer = {}
            interface_statistics_dict_buffer["id"] = "urn:ngsi-ld:Statistics:" + interface_dict_buffer["id"].split(":")[-1]
            interface_statistics_dict_buffer["type"] = "Statistics"
            interface_statistics_dict_buffer["isPartOf"] = {}
            interface_statistics_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_statistics_dict_buffer["isPartOf"]["object"] = "urn:ngsi-ld:Interface:" + interface_dict_buffer["name"]["value"]
            discontinuityTime = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}discontinuity-time")
            if discontinuityTime is not None:
                element_text = discontinuityTime.text
                interface_statistics_dict_buffer["discontinuityTime"] = {}
                interface_statistics_dict_buffer["discontinuityTime"]["type"] = "Property"
                interface_statistics_dict_buffer["discontinuityTime"]["value"] = element_text
            inOctets = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-octets")
            if inOctets is not None:
                element_text = inOctets.text
                interface_statistics_dict_buffer["inOctets"] = {}
                interface_statistics_dict_buffer["inOctets"]["type"] = "Property"
                interface_statistics_dict_buffer["inOctets"]["value"] = int(element_text)
            inUnicastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-unicast-pkts")
            if inUnicastPkts is not None:
                element_text = inUnicastPkts.text
                interface_statistics_dict_buffer["inUnicastPkts"] = {}
                interface_statistics_dict_buffer["inUnicastPkts"]["type"] = "Property"
                interface_statistics_dict_buffer["inUnicastPkts"]["value"] = int(element_text)
            inBroadcastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-broadcast-pkts")
            if inBroadcastPkts is not None:
                element_text = inBroadcastPkts.text
                interface_statistics_dict_buffer["inBroadcastPkts"] = {}
                interface_statistics_dict_buffer["inBroadcastPkts"]["type"] = "Property"
                interface_statistics_dict_buffer["inBroadcastPkts"]["value"] = int(element_text)
            inMulticastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-multicast-pkts")
            if inMulticastPkts is not None:
                element_text = inMulticastPkts.text
                interface_statistics_dict_buffer["inMulticastPkts"] = {}
                interface_statistics_dict_buffer["inMulticastPkts"]["type"] = "Property"
                interface_statistics_dict_buffer["inMulticastPkts"]["value"] = int(element_text)
            inDiscards = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-discards")
            if inDiscards is not None:
                element_text = inDiscards.text
                interface_statistics_dict_buffer["inDiscards"] = {}
                interface_statistics_dict_buffer["inDiscards"]["type"] = "Property"
                interface_statistics_dict_buffer["inDiscards"]["value"] = int(element_text)
            inErrors = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-errors")
            if inErrors is not None:
                element_text = inErrors.text
                interface_statistics_dict_buffer["inErrors"] = {}
                interface_statistics_dict_buffer["inErrors"]["type"] = "Property"
                interface_statistics_dict_buffer["inErrors"]["value"] = int(element_text)
            inUnknownProtos = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-unknown-protos")
            if inUnknownProtos is not None:
                element_text = inUnknownProtos.text
                interface_statistics_dict_buffer["inUnknownProtos"] = {}
                interface_statistics_dict_buffer["inUnknownProtos"]["type"] = "Property"
                interface_statistics_dict_buffer["inUnknownProtos"]["value"] = int(element_text)
            outOctets = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-octets")
            if outOctets is not None:
                element_text = outOctets.text
                interface_statistics_dict_buffer["outOctets"] = {}
                interface_statistics_dict_buffer["outOctets"]["type"] = "Property"
                interface_statistics_dict_buffer["outOctets"]["value"] = int(element_text)
            outUnicastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-unicast-pkts")
            if outUnicastPkts is not None:
                element_text = outUnicastPkts.text
                interface_statistics_dict_buffer["outUnicastPkts"] = {}
                interface_statistics_dict_buffer["outUnicastPkts"]["type"] = "Property"
                interface_statistics_dict_buffer["outUnicastPkts"]["value"] = int(element_text)
            outBroadcastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-broadcast-pkts")
            if outBroadcastPkts is not None:
                element_text = outBroadcastPkts.text
                interface_statistics_dict_buffer["outBroadcastPkts"] = {}
                interface_statistics_dict_buffer["outBroadcastPkts"]["type"] = "Property"
                interface_statistics_dict_buffer["outBroadcastPkts"]["value"] = int(element_text)
            outMulticastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-multicast-pkts")
            if outMulticastPkts is not None:
                element_text = outMulticastPkts.text
                interface_statistics_dict_buffer["outMulticastPkts"] = {}
                interface_statistics_dict_buffer["outMulticastPkts"]["type"] = "Property"
                interface_statistics_dict_buffer["outMulticastPkts"]["value"] = int(element_text)
            outDiscards = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-discards")
            if outDiscards is not None:
                element_text = outDiscards.text
                interface_statistics_dict_buffer["outDiscards"] = {}
                interface_statistics_dict_buffer["outDiscards"]["type"] = "Property"
                interface_statistics_dict_buffer["outDiscards"]["value"] = int(element_text)
            outErrors = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-errors")
            if outErrors is not None:
                element_text = outErrors.text
                interface_statistics_dict_buffer["outErrors"] = {}
                interface_statistics_dict_buffer["outErrors"]["type"] = "Property"
                interface_statistics_dict_buffer["outErrors"]["value"] = int(element_text)
            interface_statistics_dict_buffers.append(interface_statistics_dict_buffer)
        interface_dict_buffers.append(interface_dict_buffer)

    stop_time = time.perf_counter_ns()

    exec_time = stop_time - start_time

    print(f"ITERATION #{i} EXECUTION TIME: {exec_time} ns | {exec_time/1e3} µs | {exec_time/1e6} ms\n")

    parsing_exec_times.append(exec_time)

print(f"XML PARSING EXECUTION TIMES - SUMMARY (OVER {len(parsing_exec_times)} ITERATIONS)")
parsing_mean_exec_time = sum(parsing_exec_times)/len(parsing_exec_times)
parsing_min_exec_time = min(parsing_exec_times)
parsing_max_exec_time = max(parsing_exec_times)
parsing_total_exec_time = sum(parsing_exec_times)
print(f"MEAN VALUE: {parsing_mean_exec_time} ns | {parsing_mean_exec_time/1e3} µs | {parsing_mean_exec_time/1e6} ms")
print(f"MIN VALUE: {parsing_min_exec_time} ns | {parsing_min_exec_time/1e3} µs | {parsing_min_exec_time/1e6} ms")
print(f"MAX VALUE: {parsing_max_exec_time} ns | {parsing_max_exec_time/1e3} µs | {parsing_max_exec_time/1e6} ms")
print(f"TOTAL EXECUTION TIME: {parsing_total_exec_time} ns | {parsing_total_exec_time/1e3} µs | {parsing_total_exec_time/1e6} ms")
