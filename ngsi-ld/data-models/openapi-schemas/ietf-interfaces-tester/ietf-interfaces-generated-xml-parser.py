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
name = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}name")
for entry in name:
    print(entry.text)
description = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}description")
for entry in description:
    print(entry.text)
type = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}type")
for entry in type:
    print(entry.text)
enabled = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}enabled")
for entry in enabled:
    print(entry.text)
linkUpDownTrapEnable = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}link-up-down-trap-enable")
for entry in linkUpDownTrapEnable:
    print(entry.text)
adminStatus = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}admin-status")
for entry in adminStatus:
    print(entry.text)
operStatus = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}oper-status")
for entry in operStatus:
    print(entry.text)
lastChange = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}last-change")
for entry in lastChange:
    print(entry.text)
ifIndex = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}if-index")
for entry in ifIndex:
    print(entry.text)
physAddress = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}phys-address")
for entry in physAddress:
    print(entry.text)
higherLayerIf = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}higher-layer-if")
for entry in higherLayerIf:
    print(entry.text)
lowerLayerIf = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}lower-layer-if")
for entry in lowerLayerIf:
    print(entry.text)
speed = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}speed")
for entry in speed:
    print(entry.text)
from ngsi_ld_models.models.statistics import Statistics
statistics_dict_buffers = []
discontinuityTime = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}discontinuity-time")
for entry in discontinuityTime:
    print(entry.text)
inOctets = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-octets")
for entry in inOctets:
    print(entry.text)
inUnicastPkts = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-unicast-pkts")
for entry in inUnicastPkts:
    print(entry.text)
inBroadcastPkts = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-broadcast-pkts")
for entry in inBroadcastPkts:
    print(entry.text)
inMulticastPkts = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-multicast-pkts")
for entry in inMulticastPkts:
    print(entry.text)
inDiscards = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-discards")
for entry in inDiscards:
    print(entry.text)
inErrors = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-errors")
for entry in inErrors:
    print(entry.text)
inUnknownProtos = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-unknown-protos")
for entry in inUnknownProtos:
    print(entry.text)
outOctets = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-octets")
for entry in outOctets:
    print(entry.text)
outUnicastPkts = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-unicast-pkts")
for entry in outUnicastPkts:
    print(entry.text)
outBroadcastPkts = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-broadcast-pkts")
for entry in outBroadcastPkts:
    print(entry.text)
outMulticastPkts = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-multicast-pkts")
for entry in outMulticastPkts:
    print(entry.text)
outDiscards = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-discards")
for entry in outDiscards:
    print(entry.text)
outErrors = root.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-errors")
for entry in outErrors:
    print(entry.text)