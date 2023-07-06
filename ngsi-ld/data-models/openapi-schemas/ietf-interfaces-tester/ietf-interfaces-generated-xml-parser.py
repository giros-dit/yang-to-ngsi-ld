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
import ngsi_ld_client
from fastapi import FastAPI, Request, status
from ngsi_ld_client.api_client import ApiClient as NGSILDClient
from ngsi_ld_client.configuration import Configuration as NGSILDConfiguration
from ngsi_ld_client.exceptions import ApiException

xml_file = sys.argv[1]
tree = et.parse(xml_file)
root = tree.getroot()

from ngsi_ld_models.models.interface import Interface
interface_dict_buffers = []

from ngsi_ld_models.models.statistics import Statistics
statistics_dict_buffers = []

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
        statistics_dict_buffer = {}
        statistics_dict_buffer["id"] = "urn:ngsi-ld:Statistics:" + interface_dict_buffer["name"]["value"]
        statistics_dict_buffer["type"] = "Statistics"
        statistics_dict_buffer["isPartOf"] = {}
        statistics_dict_buffer["isPartOf"]["type"] = "Relationship"
        statistics_dict_buffer["isPartOf"]["object"] = "urn:ngsi-ld:Interface:" + interface_dict_buffer["name"]["value"]
        discontinuityTime = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}discontinuity-time")
        if discontinuityTime is not None:
            element_text = discontinuityTime.text
            statistics_dict_buffer["discontinuityTime"] = {}
            statistics_dict_buffer["discontinuityTime"]["type"] = "Property"
            statistics_dict_buffer["discontinuityTime"]["value"] = element_text
        inOctets = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-octets")
        if inOctets is not None:
            element_text = inOctets.text
            statistics_dict_buffer["inOctets"] = {}
            statistics_dict_buffer["inOctets"]["type"] = "Property"
            statistics_dict_buffer["inOctets"]["value"] = int(element_text)
        inUnicastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-unicast-pkts")
        if inUnicastPkts is not None:
            element_text = inUnicastPkts.text
            statistics_dict_buffer["inUnicastPkts"] = {}
            statistics_dict_buffer["inUnicastPkts"]["type"] = "Property"
            statistics_dict_buffer["inUnicastPkts"]["value"] = int(element_text)
        inBroadcastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-broadcast-pkts")
        if inBroadcastPkts is not None:
            element_text = inBroadcastPkts.text
            statistics_dict_buffer["inBroadcastPkts"] = {}
            statistics_dict_buffer["inBroadcastPkts"]["type"] = "Property"
            statistics_dict_buffer["inBroadcastPkts"]["value"] = int(element_text)
        inMulticastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-multicast-pkts")
        if inMulticastPkts is not None:
            element_text = inMulticastPkts.text
            statistics_dict_buffer["inMulticastPkts"] = {}
            statistics_dict_buffer["inMulticastPkts"]["type"] = "Property"
            statistics_dict_buffer["inMulticastPkts"]["value"] = int(element_text)
        inDiscards = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-discards")
        if inDiscards is not None:
            element_text = inDiscards.text
            statistics_dict_buffer["inDiscards"] = {}
            statistics_dict_buffer["inDiscards"]["type"] = "Property"
            statistics_dict_buffer["inDiscards"]["value"] = int(element_text)
        inErrors = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-errors")
        if inErrors is not None:
            element_text = inErrors.text
            statistics_dict_buffer["inErrors"] = {}
            statistics_dict_buffer["inErrors"]["type"] = "Property"
            statistics_dict_buffer["inErrors"]["value"] = int(element_text)
        inUnknownProtos = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-unknown-protos")
        if inUnknownProtos is not None:
            element_text = inUnknownProtos.text
            statistics_dict_buffer["inUnknownProtos"] = {}
            statistics_dict_buffer["inUnknownProtos"]["type"] = "Property"
            statistics_dict_buffer["inUnknownProtos"]["value"] = int(element_text)
        outOctets = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-octets")
        if outOctets is not None:
            element_text = outOctets.text
            statistics_dict_buffer["outOctets"] = {}
            statistics_dict_buffer["outOctets"]["type"] = "Property"
            statistics_dict_buffer["outOctets"]["value"] = int(element_text)
        outUnicastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-unicast-pkts")
        if outUnicastPkts is not None:
            element_text = outUnicastPkts.text
            statistics_dict_buffer["outUnicastPkts"] = {}
            statistics_dict_buffer["outUnicastPkts"]["type"] = "Property"
            statistics_dict_buffer["outUnicastPkts"]["value"] = int(element_text)
        outBroadcastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-broadcast-pkts")
        if outBroadcastPkts is not None:
            element_text = outBroadcastPkts.text
            statistics_dict_buffer["outBroadcastPkts"] = {}
            statistics_dict_buffer["outBroadcastPkts"]["type"] = "Property"
            statistics_dict_buffer["outBroadcastPkts"]["value"] = int(element_text)
        outMulticastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-multicast-pkts")
        if outMulticastPkts is not None:
            element_text = outMulticastPkts.text
            statistics_dict_buffer["outMulticastPkts"] = {}
            statistics_dict_buffer["outMulticastPkts"]["type"] = "Property"
            statistics_dict_buffer["outMulticastPkts"]["value"] = int(element_text)
        outDiscards = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-discards")
        if outDiscards is not None:
            element_text = outDiscards.text
            statistics_dict_buffer["outDiscards"] = {}
            statistics_dict_buffer["outDiscards"]["type"] = "Property"
            statistics_dict_buffer["outDiscards"]["value"] = int(element_text)
        outErrors = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-errors")
        if outErrors is not None:
            element_text = outErrors.text
            statistics_dict_buffer["outErrors"] = {}
            statistics_dict_buffer["outErrors"]["type"] = "Property"
            statistics_dict_buffer["outErrors"]["value"] = int(element_text)
        statistics_dict_buffers.append(statistics_dict_buffer)
    interface_dict_buffers.append(interface_dict_buffer)