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
for interface in root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}interface"):
    name = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}name")
    if name is not None: print(name.text)
    description = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}description")
    if description is not None: print(description.text)
    type = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}type")
    if type is not None: print(type.text)
    enabled = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}enabled")
    if enabled is not None: print(enabled.text)
    linkUpDownTrapEnable = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}link-up-down-trap-enable")
    if linkUpDownTrapEnable is not None: print(linkUpDownTrapEnable.text)
    adminStatus = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}admin-status")
    if adminStatus is not None: print(adminStatus.text)
    operStatus = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}oper-status")
    if operStatus is not None: print(operStatus.text)
    lastChange = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}last-change")
    if lastChange is not None: print(lastChange.text)
    ifIndex = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}if-index")
    if ifIndex is not None: print(ifIndex.text)
    physAddress = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}phys-address")
    if physAddress is not None: print(physAddress.text)
    higherLayerIf = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}higher-layer-if")
    if higherLayerIf is not None: print(higherLayerIf.text)
    lowerLayerIf = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}lower-layer-if")
    if lowerLayerIf is not None: print(lowerLayerIf.text)
    speed = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}speed")
    if speed is not None: print(speed.text)
    from ngsi_ld_models.models.statistics import Statistics
    statistics_dict_buffers = []
    for statistics in interface.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}statistics"):
        discontinuityTime = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}discontinuity-time")
        if discontinuityTime is not None: print(discontinuityTime.text)
        inOctets = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-octets")
        if inOctets is not None: print(inOctets.text)
        inUnicastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-unicast-pkts")
        if inUnicastPkts is not None: print(inUnicastPkts.text)
        inBroadcastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-broadcast-pkts")
        if inBroadcastPkts is not None: print(inBroadcastPkts.text)
        inMulticastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-multicast-pkts")
        if inMulticastPkts is not None: print(inMulticastPkts.text)
        inDiscards = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-discards")
        if inDiscards is not None: print(inDiscards.text)
        inErrors = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-errors")
        if inErrors is not None: print(inErrors.text)
        inUnknownProtos = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-unknown-protos")
        if inUnknownProtos is not None: print(inUnknownProtos.text)
        outOctets = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-octets")
        if outOctets is not None: print(outOctets.text)
        outUnicastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-unicast-pkts")
        if outUnicastPkts is not None: print(outUnicastPkts.text)
        outBroadcastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-broadcast-pkts")
        if outBroadcastPkts is not None: print(outBroadcastPkts.text)
        outMulticastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-multicast-pkts")
        if outMulticastPkts is not None: print(outMulticastPkts.text)
        outDiscards = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-discards")
        if outDiscards is not None: print(outDiscards.text)
        outErrors = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-errors")
        if outErrors is not None: print(outErrors.text)