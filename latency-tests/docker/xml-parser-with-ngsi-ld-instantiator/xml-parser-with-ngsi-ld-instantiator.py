import os
import logging
import logging.config
import pdb
import yaml
import json

from kafka import KafkaConsumer

import xml.etree.ElementTree as et

from dateutil import parser

import ngsi_ld_client

from ngsi_ld_models.models.interface import Interface
from ngsi_ld_models.models.interface_statistics import InterfaceStatistics
from ngsi_ld_models.models.interface_ipv4 import InterfaceIpv4
from ngsi_ld_models.models.interface_ipv4_address import InterfaceIpv4Address
from ngsi_ld_models.models.interface_ipv4_neighbor import InterfaceIpv4Neighbor
from ngsi_ld_models.models.interface_ipv6 import InterfaceIpv6
from ngsi_ld_models.models.interface_ipv6_address import InterfaceIpv6Address
from ngsi_ld_models.models.interface_ipv6_autoconf import InterfaceIpv6Autoconf
from ngsi_ld_models.models.interface_ipv6_neighbor import InterfaceIpv6Neighbor
from ngsi_ld_client.models.entity import Entity
from ngsi_ld_client.models.query_entity200_response_inner import QueryEntity200ResponseInner

from ngsi_ld_client.api_client import ApiClient as NGSILDClient
from ngsi_ld_client.configuration import Configuration as NGSILDConfiguration
from ngsi_ld_client.exceptions import ApiException

## -- BEGIN LOGGING CONFIGURATION -- ##

with open('logging.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)

## -- END LOGGING CONFIGURATION -- ##

## -- BEGIN CONSTANTS DECLARATION -- ##

# NGSI-LD Context Broker:
BROKER_URI = os.getenv("BROKER_URI", "http://scorpio:9090/ngsi-ld/v1")

# Context Catalog:
CONTEXT_CATALOG_URI = os.getenv("CONTEXT_CATALOG_URI", "http://context-catalog:8080/context.jsonld")

## -- END CONSTANTS DECLARATION -- ##

## -- BEGIN AUXILIARY FUNCTIONS -- ##

def parse_xml(message) -> list:
    dict_buffers = []

    xml = str(message.value.decode('utf-8'))
    root = et.fromstring(xml)

    # observedAt is the eventTime element from the XML notification
    observedAt = root[0].text

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
                interface_dict_buffer["name"]["observedAt"] = observedAt
        description = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}description")
        if description is not None:
            element_text = description.text
            if element_text is not None:
                interface_dict_buffer["description"] = {}
                interface_dict_buffer["description"]["type"] = "Property"
                interface_dict_buffer["description"]["value"] = element_text
                interface_dict_buffer["description"]["observedAt"] = observedAt
        type = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}type")
        if type is not None:
            element_text = type.text
            if element_text is not None:
                interface_dict_buffer["interfaceType"] = {}
                interface_dict_buffer["interfaceType"]["type"] = "Relationship"
                interface_dict_buffer["interfaceType"]["object"] = "urn:ngsi-ld:YANGIdentity:" + element_text
                interface_dict_buffer["interfaceType"]["observedAt"] = observedAt
        enabled = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}enabled")
        if enabled is not None:
            element_text = enabled.text
            if element_text is not None:
                interface_dict_buffer["enabled"] = {}
                interface_dict_buffer["enabled"]["type"] = "Property"
                interface_dict_buffer["enabled"]["value"] = eval(element_text.capitalize())
                interface_dict_buffer["enabled"]["observedAt"] = observedAt
        linkUpDownTrapEnable = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}link-up-down-trap-enable")
        if linkUpDownTrapEnable is not None:
            element_text = linkUpDownTrapEnable.text
            if element_text is not None:
                interface_dict_buffer["linkUpDownTrapEnable"] = {}
                interface_dict_buffer["linkUpDownTrapEnable"]["type"] = "Property"
                interface_dict_buffer["linkUpDownTrapEnable"]["value"] = element_text
                interface_dict_buffer["linkUpDownTrapEnable"]["observedAt"] = observedAt
        adminStatus = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}admin-status")
        if adminStatus is not None:
            element_text = adminStatus.text
            if element_text is not None:
                interface_dict_buffer["adminStatus"] = {}
                interface_dict_buffer["adminStatus"]["type"] = "Property"
                interface_dict_buffer["adminStatus"]["value"] = element_text
                interface_dict_buffer["adminStatus"]["observedAt"] = observedAt
        operStatus = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}oper-status")
        if operStatus is not None:
            element_text = operStatus.text
            if element_text is not None:
                interface_dict_buffer["operStatus"] = {}
                interface_dict_buffer["operStatus"]["type"] = "Property"
                interface_dict_buffer["operStatus"]["value"] = element_text
                interface_dict_buffer["operStatus"]["observedAt"] = observedAt
        lastChange = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}last-change")
        if lastChange is not None:
            element_text = lastChange.text
            if element_text is not None:
                interface_dict_buffer["lastChange"] = {}
                interface_dict_buffer["lastChange"]["type"] = "Property"
                interface_dict_buffer["lastChange"]["value"] = element_text
                interface_dict_buffer["lastChange"]["observedAt"] = observedAt
        ifIndex = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}if-index")
        if ifIndex is not None:
            element_text = ifIndex.text
            if element_text is not None:
                interface_dict_buffer["ifIndex"] = {}
                interface_dict_buffer["ifIndex"]["type"] = "Property"
                interface_dict_buffer["ifIndex"]["value"] = int(element_text)
                interface_dict_buffer["ifIndex"]["observedAt"] = observedAt
        physAddress = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}phys-address")
        if physAddress is not None:
            element_text = physAddress.text
            if element_text is not None:
                interface_dict_buffer["physAddress"] = {}
                interface_dict_buffer["physAddress"]["type"] = "Property"
                interface_dict_buffer["physAddress"]["value"] = element_text
                interface_dict_buffer["physAddress"]["observedAt"] = observedAt
        higherLayerIf = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}higher-layer-if")
        if higherLayerIf is not None:
            element_text = higherLayerIf.text
            if element_text is not None:
                interface_dict_buffer["higherLayerIf"] = {}
                interface_dict_buffer["higherLayerIf"]["type"] = "Relationship"
                interface_dict_buffer["higherLayerIf"]["object"] = "urn:ngsi-ld:Interface:" + element_text
                interface_dict_buffer["higherLayerIf"]["observedAt"] = observedAt
        lowerLayerIf = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}lower-layer-if")
        if lowerLayerIf is not None:
            element_text = lowerLayerIf.text
            if element_text is not None:
                interface_dict_buffer["lowerLayerIf"] = {}
                interface_dict_buffer["lowerLayerIf"]["type"] = "Relationship"
                interface_dict_buffer["lowerLayerIf"]["object"] = "urn:ngsi-ld:Interface:" + element_text
                interface_dict_buffer["lowerLayerIf"]["observedAt"] = observedAt
        speed = interface.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}speed")
        if speed is not None:
            element_text = speed.text
            if element_text is not None:
                interface_dict_buffer["speed"] = {}
                interface_dict_buffer["speed"]["type"] = "Property"
                interface_dict_buffer["speed"]["value"] = int(element_text)
                interface_dict_buffer["speed"]["observedAt"] = observedAt
        for statistics in interface.findall(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}statistics"):
            interface_statistics_dict_buffer = {}
            interface_statistics_dict_buffer["id"] = "urn:ngsi-ld:InterfaceStatistics:" + interface_dict_buffer["id"].split(":")[-1]
            interface_statistics_dict_buffer["type"] = "InterfaceStatistics"
            interface_statistics_dict_buffer["isPartOf"] = {}
            interface_statistics_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_statistics_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
            interface_statistics_dict_buffer["isPartOf"]["observedAt"] = observedAt
            discontinuityTime = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}discontinuity-time")
            if discontinuityTime is not None:
                element_text = discontinuityTime.text
                if element_text is not None:
                    interface_statistics_dict_buffer["discontinuityTime"] = {}
                    interface_statistics_dict_buffer["discontinuityTime"]["type"] = "Property"
                    interface_statistics_dict_buffer["discontinuityTime"]["value"] = element_text
                    interface_statistics_dict_buffer["discontinuityTime"]["observedAt"] = observedAt
            inOctets = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-octets")
            if inOctets is not None:
                element_text = inOctets.text
                if element_text is not None:
                    interface_statistics_dict_buffer["inOctets"] = {}
                    interface_statistics_dict_buffer["inOctets"]["type"] = "Property"
                    interface_statistics_dict_buffer["inOctets"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["inOctets"]["observedAt"] = observedAt
            inUnicastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-unicast-pkts")
            if inUnicastPkts is not None:
                element_text = inUnicastPkts.text
                if element_text is not None:
                    interface_statistics_dict_buffer["inUnicastPkts"] = {}
                    interface_statistics_dict_buffer["inUnicastPkts"]["type"] = "Property"
                    interface_statistics_dict_buffer["inUnicastPkts"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["inUnicastPkts"]["observedAt"] = observedAt
            inBroadcastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-broadcast-pkts")
            if inBroadcastPkts is not None:
                element_text = inBroadcastPkts.text
                if element_text is not None:
                    interface_statistics_dict_buffer["inBroadcastPkts"] = {}
                    interface_statistics_dict_buffer["inBroadcastPkts"]["type"] = "Property"
                    interface_statistics_dict_buffer["inBroadcastPkts"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["inBroadcastPkts"]["observedAt"] = observedAt
            inMulticastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-multicast-pkts")
            if inMulticastPkts is not None:
                element_text = inMulticastPkts.text
                if element_text is not None:
                    interface_statistics_dict_buffer["inMulticastPkts"] = {}
                    interface_statistics_dict_buffer["inMulticastPkts"]["type"] = "Property"
                    interface_statistics_dict_buffer["inMulticastPkts"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["inMulticastPkts"]["observedAt"] = observedAt
            inDiscards = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-discards")
            if inDiscards is not None:
                element_text = inDiscards.text
                if element_text is not None:
                    interface_statistics_dict_buffer["inDiscards"] = {}
                    interface_statistics_dict_buffer["inDiscards"]["type"] = "Property"
                    interface_statistics_dict_buffer["inDiscards"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["inDiscards"]["observedAt"] = observedAt
            inErrors = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-errors")
            if inErrors is not None:
                element_text = inErrors.text
                if element_text is not None:
                    interface_statistics_dict_buffer["inErrors"] = {}
                    interface_statistics_dict_buffer["inErrors"]["type"] = "Property"
                    interface_statistics_dict_buffer["inErrors"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["inErrors"]["observedAt"] = observedAt
            inUnknownProtos = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}in-unknown-protos")
            if inUnknownProtos is not None:
                element_text = inUnknownProtos.text
                if element_text is not None:
                    interface_statistics_dict_buffer["inUnknownProtos"] = {}
                    interface_statistics_dict_buffer["inUnknownProtos"]["type"] = "Property"
                    interface_statistics_dict_buffer["inUnknownProtos"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["inUnknownProtos"]["observedAt"] = observedAt
            outOctets = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-octets")
            if outOctets is not None:
                element_text = outOctets.text
                if element_text is not None:
                    interface_statistics_dict_buffer["outOctets"] = {}
                    interface_statistics_dict_buffer["outOctets"]["type"] = "Property"
                    interface_statistics_dict_buffer["outOctets"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["outOctets"]["observedAt"] = observedAt
            outUnicastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-unicast-pkts")
            if outUnicastPkts is not None:
                element_text = outUnicastPkts.text
                if element_text is not None:
                    interface_statistics_dict_buffer["outUnicastPkts"] = {}
                    interface_statistics_dict_buffer["outUnicastPkts"]["type"] = "Property"
                    interface_statistics_dict_buffer["outUnicastPkts"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["outUnicastPkts"]["observedAt"] = observedAt
            outBroadcastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-broadcast-pkts")
            if outBroadcastPkts is not None:
                element_text = outBroadcastPkts.text
                if element_text is not None:
                    interface_statistics_dict_buffer["outBroadcastPkts"] = {}
                    interface_statistics_dict_buffer["outBroadcastPkts"]["type"] = "Property"
                    interface_statistics_dict_buffer["outBroadcastPkts"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["outBroadcastPkts"]["observedAt"] = observedAt
            outMulticastPkts = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-multicast-pkts")
            if outMulticastPkts is not None:
                element_text = outMulticastPkts.text
                if element_text is not None:
                    interface_statistics_dict_buffer["outMulticastPkts"] = {}
                    interface_statistics_dict_buffer["outMulticastPkts"]["type"] = "Property"
                    interface_statistics_dict_buffer["outMulticastPkts"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["outMulticastPkts"]["observedAt"] = observedAt
            outDiscards = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-discards")
            if outDiscards is not None:
                element_text = outDiscards.text
                if element_text is not None:
                    interface_statistics_dict_buffer["outDiscards"] = {}
                    interface_statistics_dict_buffer["outDiscards"]["type"] = "Property"
                    interface_statistics_dict_buffer["outDiscards"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["outDiscards"]["observedAt"] = observedAt
            outErrors = statistics.find(".//{urn:ietf:params:xml:ns:yang:ietf-interfaces}out-errors")
            if outErrors is not None:
                element_text = outErrors.text
                if element_text is not None:
                    interface_statistics_dict_buffer["outErrors"] = {}
                    interface_statistics_dict_buffer["outErrors"]["type"] = "Property"
                    interface_statistics_dict_buffer["outErrors"]["value"] = int(element_text)
                    interface_statistics_dict_buffer["outErrors"]["observedAt"] = observedAt
            dict_buffers.append(interface_statistics_dict_buffer)
        for ipv4 in interface.findall(".//{urn:ietf:params:xml:ns:yang:ietf-ip}ipv4"):
            interface_ipv4_dict_buffer = {}
            interface_ipv4_dict_buffer["id"] = "urn:ngsi-ld:InterfaceIpv4:" + interface_dict_buffer["id"].split(":")[-1]
            interface_ipv4_dict_buffer["type"] = "InterfaceIpv4"
            interface_ipv4_dict_buffer["isPartOf"] = {}
            interface_ipv4_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_ipv4_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
            interface_ipv4_dict_buffer["isPartOf"]["observedAt"] = observedAt
            enabled = ipv4.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}enabled")
            if enabled is not None:
                element_text = enabled.text
                if element_text is not None:
                    interface_ipv4_dict_buffer["enabled"] = {}
                    interface_ipv4_dict_buffer["enabled"]["type"] = "Property"
                    interface_ipv4_dict_buffer["enabled"]["value"] = eval(element_text.capitalize())
                    interface_ipv4_dict_buffer["enabled"]["observedAt"] = observedAt
            forwarding = ipv4.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}forwarding")
            if forwarding is not None:
                element_text = forwarding.text
                if element_text is not None:
                    interface_ipv4_dict_buffer["forwarding"] = {}
                    interface_ipv4_dict_buffer["forwarding"]["type"] = "Property"
                    interface_ipv4_dict_buffer["forwarding"]["value"] = eval(element_text.capitalize())
                    interface_ipv4_dict_buffer["forwarding"]["observedAt"] = observedAt
            mtu = ipv4.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}mtu")
            if mtu is not None:
                element_text = mtu.text
                if element_text is not None:
                    interface_ipv4_dict_buffer["mtu"] = {}
                    interface_ipv4_dict_buffer["mtu"]["type"] = "Property"
                    interface_ipv4_dict_buffer["mtu"]["value"] = int(element_text)
                    interface_ipv4_dict_buffer["mtu"]["observedAt"] = observedAt
            for address in ipv4.findall(".//{urn:ietf:params:xml:ns:yang:ietf-ip}address"):
                interface_ipv4_address_dict_buffer = {}
                interface_ipv4_address_dict_buffer["id"] = "urn:ngsi-ld:InterfaceIpv4Address:" + interface_ipv4_dict_buffer["id"].split(":")[-1]
                interface_ipv4_address_dict_buffer["type"] = "InterfaceIpv4Address"
                interface_ipv4_address_dict_buffer["isPartOf"] = {}
                interface_ipv4_address_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_ipv4_address_dict_buffer["isPartOf"]["object"] = interface_ipv4_dict_buffer["id"]
                interface_ipv4_address_dict_buffer["isPartOf"]["observedAt"] = observedAt
                ip = address.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}ip")
                if ip is not None:
                    element_text = ip.text
                    if element_text is not None:
                        interface_ipv4_address_dict_buffer["ip"] = {}
                        interface_ipv4_address_dict_buffer["ip"]["type"] = "Property"
                        interface_ipv4_address_dict_buffer["ip"]["value"] = element_text
                        interface_ipv4_address_dict_buffer["ip"]["observedAt"] = observedAt
                origin = address.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}origin")
                if origin is not None:
                    element_text = origin.text
                    if element_text is not None:
                        interface_ipv4_address_dict_buffer["origin"] = {}
                        interface_ipv4_address_dict_buffer["origin"]["type"] = "Property"
                        interface_ipv4_address_dict_buffer["origin"]["value"] = element_text
                        interface_ipv4_address_dict_buffer["origin"]["observedAt"] = observedAt
                dict_buffers.append(interface_ipv4_address_dict_buffer)
            for neighbor in ipv4.findall(".//{urn:ietf:params:xml:ns:yang:ietf-ip}neighbor"):
                interface_ipv4_neighbor_dict_buffer = {}
                interface_ipv4_neighbor_dict_buffer["id"] = "urn:ngsi-ld:InterfaceIpv4Neighbor:" + interface_ipv4_dict_buffer["id"].split(":")[-1]
                interface_ipv4_neighbor_dict_buffer["type"] = "InterfaceIpv4Neighbor"
                interface_ipv4_neighbor_dict_buffer["isPartOf"] = {}
                interface_ipv4_neighbor_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_ipv4_neighbor_dict_buffer["isPartOf"]["object"] = interface_ipv4_dict_buffer["id"]
                interface_ipv4_neighbor_dict_buffer["isPartOf"]["observedAt"] = observedAt
                ip = neighbor.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}ip")
                if ip is not None:
                    element_text = ip.text
                    if element_text is not None:
                        interface_ipv4_neighbor_dict_buffer["ip"] = {}
                        interface_ipv4_neighbor_dict_buffer["ip"]["type"] = "Property"
                        interface_ipv4_neighbor_dict_buffer["ip"]["value"] = element_text
                        interface_ipv4_neighbor_dict_buffer["ip"]["observedAt"] = observedAt
                linkLayerAddress = neighbor.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}link-layer-address")
                if linkLayerAddress is not None:
                    element_text = linkLayerAddress.text
                    if element_text is not None:
                        interface_ipv4_neighbor_dict_buffer["linkLayerAddress"] = {}
                        interface_ipv4_neighbor_dict_buffer["linkLayerAddress"]["type"] = "Property"
                        interface_ipv4_neighbor_dict_buffer["linkLayerAddress"]["value"] = element_text
                        interface_ipv4_neighbor_dict_buffer["linkLayerAddress"]["observedAt"] = observedAt
                origin = neighbor.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}origin")
                if origin is not None:
                    element_text = origin.text
                    if element_text is not None:
                        interface_ipv4_neighbor_dict_buffer["origin"] = {}
                        interface_ipv4_neighbor_dict_buffer["origin"]["type"] = "Property"
                        interface_ipv4_neighbor_dict_buffer["origin"]["value"] = element_text
                        interface_ipv4_neighbor_dict_buffer["origin"]["observedAt"] = observedAt
                dict_buffers.append(interface_ipv4_neighbor_dict_buffer)
            dict_buffers.append(interface_ipv4_dict_buffer)
        for ipv6 in interface.findall(".//{urn:ietf:params:xml:ns:yang:ietf-ip}ipv6"):
            interface_ipv6_dict_buffer = {}
            interface_ipv6_dict_buffer["id"] = "urn:ngsi-ld:InterfaceIpv6:" + interface_dict_buffer["id"].split(":")[-1]
            interface_ipv6_dict_buffer["type"] = "InterfaceIpv6"
            interface_ipv6_dict_buffer["isPartOf"] = {}
            interface_ipv6_dict_buffer["isPartOf"]["type"] = "Relationship"
            interface_ipv6_dict_buffer["isPartOf"]["object"] = interface_dict_buffer["id"]
            interface_ipv6_dict_buffer["isPartOf"]["observedAt"] = observedAt
            enabled = ipv6.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}enabled")
            if enabled is not None:
                element_text = enabled.text
                if element_text is not None:
                    interface_ipv6_dict_buffer["enabled"] = {}
                    interface_ipv6_dict_buffer["enabled"]["type"] = "Property"
                    interface_ipv6_dict_buffer["enabled"]["value"] = eval(element_text.capitalize())
                    interface_ipv6_dict_buffer["enabled"]["observedAt"] = observedAt
            forwarding = ipv6.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}forwarding")
            if forwarding is not None:
                element_text = forwarding.text
                if element_text is not None:
                    interface_ipv6_dict_buffer["forwarding"] = {}
                    interface_ipv6_dict_buffer["forwarding"]["type"] = "Property"
                    interface_ipv6_dict_buffer["forwarding"]["value"] = eval(element_text.capitalize())
                    interface_ipv6_dict_buffer["forwarding"]["observedAt"] = observedAt
            mtu = ipv6.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}mtu")
            if mtu is not None:
                element_text = mtu.text
                if element_text is not None:
                    interface_ipv6_dict_buffer["mtu"] = {}
                    interface_ipv6_dict_buffer["mtu"]["type"] = "Property"
                    interface_ipv6_dict_buffer["mtu"]["value"] = int(element_text)
                    interface_ipv6_dict_buffer["mtu"]["observedAt"] = observedAt
            for address in ipv6.findall(".//{urn:ietf:params:xml:ns:yang:ietf-ip}address"):
                interface_ipv6_address_dict_buffer = {}
                interface_ipv6_address_dict_buffer["id"] = "urn:ngsi-ld:InterfaceIpv6Address:" + interface_ipv6_dict_buffer["id"].split(":")[-1]
                interface_ipv6_address_dict_buffer["type"] = "InterfaceIpv6Address"
                interface_ipv6_address_dict_buffer["isPartOf"] = {}
                interface_ipv6_address_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_ipv6_address_dict_buffer["isPartOf"]["object"] = interface_ipv6_dict_buffer["id"]
                interface_ipv6_address_dict_buffer["isPartOf"]["observedAt"] = observedAt
                ip = address.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}ip")
                if ip is not None:
                    element_text = ip.text
                    if element_text is not None:
                        interface_ipv6_address_dict_buffer["ip"] = {}
                        interface_ipv6_address_dict_buffer["ip"]["type"] = "Property"
                        interface_ipv6_address_dict_buffer["ip"]["value"] = element_text
                        interface_ipv6_address_dict_buffer["ip"]["observedAt"] = observedAt
                prefixLength = address.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}prefix-length")
                if prefixLength is not None:
                    element_text = prefixLength.text
                    if element_text is not None:
                        interface_ipv6_address_dict_buffer["prefixLength"] = {}
                        interface_ipv6_address_dict_buffer["prefixLength"]["type"] = "Property"
                        interface_ipv6_address_dict_buffer["prefixLength"]["value"] = int(element_text)
                        interface_ipv6_address_dict_buffer["prefixLength"]["observedAt"] = observedAt
                origin = address.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}origin")
                if origin is not None:
                    element_text = origin.text
                    if element_text is not None:
                        interface_ipv6_address_dict_buffer["origin"] = {}
                        interface_ipv6_address_dict_buffer["origin"]["type"] = "Property"
                        interface_ipv6_address_dict_buffer["origin"]["value"] = element_text
                        interface_ipv6_address_dict_buffer["origin"]["observedAt"] = observedAt
                status = address.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}status")
                if status is not None:
                    element_text = status.text
                    if element_text is not None:
                        interface_ipv6_address_dict_buffer["status"] = {}
                        interface_ipv6_address_dict_buffer["status"]["type"] = "Property"
                        interface_ipv6_address_dict_buffer["status"]["value"] = element_text
                        interface_ipv6_address_dict_buffer["status"]["observedAt"] = observedAt
                dict_buffers.append(interface_ipv6_address_dict_buffer)
            for neighbor in ipv6.findall(".//{urn:ietf:params:xml:ns:yang:ietf-ip}neighbor"):
                interface_ipv6_neighbor_dict_buffer = {}
                interface_ipv6_neighbor_dict_buffer["id"] = "urn:ngsi-ld:InterfaceIpv6Neighbor:" + interface_ipv6_dict_buffer["id"].split(":")[-1]
                interface_ipv6_neighbor_dict_buffer["type"] = "InterfaceIpv6Neighbor"
                interface_ipv6_neighbor_dict_buffer["isPartOf"] = {}
                interface_ipv6_neighbor_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_ipv6_neighbor_dict_buffer["isPartOf"]["object"] = interface_ipv6_dict_buffer["id"]
                interface_ipv6_neighbor_dict_buffer["isPartOf"]["observedAt"] = observedAt
                ip = neighbor.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}ip")
                if ip is not None:
                    element_text = ip.text
                    if element_text is not None:
                        interface_ipv6_neighbor_dict_buffer["ip"] = {}
                        interface_ipv6_neighbor_dict_buffer["ip"]["type"] = "Property"
                        interface_ipv6_neighbor_dict_buffer["ip"]["value"] = element_text
                        interface_ipv6_neighbor_dict_buffer["ip"]["observedAt"] = observedAt
                linkLayerAddress = neighbor.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}link-layer-address")
                if linkLayerAddress is not None:
                    element_text = linkLayerAddress.text
                    if element_text is not None:
                        interface_ipv6_neighbor_dict_buffer["linkLayerAddress"] = {}
                        interface_ipv6_neighbor_dict_buffer["linkLayerAddress"]["type"] = "Property"
                        interface_ipv6_neighbor_dict_buffer["linkLayerAddress"]["value"] = element_text
                        interface_ipv6_neighbor_dict_buffer["linkLayerAddress"]["observedAt"] = observedAt
                origin = neighbor.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}origin")
                if origin is not None:
                    element_text = origin.text
                    if element_text is not None:
                        interface_ipv6_neighbor_dict_buffer["origin"] = {}
                        interface_ipv6_neighbor_dict_buffer["origin"]["type"] = "Property"
                        interface_ipv6_neighbor_dict_buffer["origin"]["value"] = element_text
                        interface_ipv6_neighbor_dict_buffer["origin"]["observedAt"] = observedAt
                isRouter = neighbor.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}is-router")
                if isRouter is not None:
                    element_text = isRouter.text
                    if element_text is not None:
                        interface_ipv6_neighbor_dict_buffer["isRouter"] = {}
                        interface_ipv6_neighbor_dict_buffer["isRouter"]["type"] = "Property"
                        interface_ipv6_neighbor_dict_buffer["isRouter"]["value"] = element_text
                        interface_ipv6_neighbor_dict_buffer["isRouter"]["observedAt"] = observedAt
                state = neighbor.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}state")
                if state is not None:
                    element_text = state.text
                    if element_text is not None:
                        interface_ipv6_neighbor_dict_buffer["state"] = {}
                        interface_ipv6_neighbor_dict_buffer["state"]["type"] = "Property"
                        interface_ipv6_neighbor_dict_buffer["state"]["value"] = element_text
                        interface_ipv6_neighbor_dict_buffer["state"]["observedAt"] = observedAt
                dict_buffers.append(interface_ipv6_neighbor_dict_buffer)
            dupAddrDetectTransmits = ipv6.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}dup-addr-detect-transmits")
            if dupAddrDetectTransmits is not None:
                element_text = dupAddrDetectTransmits.text
                if element_text is not None:
                    interface_ipv6_dict_buffer["dupAddrDetectTransmits"] = {}
                    interface_ipv6_dict_buffer["dupAddrDetectTransmits"]["type"] = "Property"
                    interface_ipv6_dict_buffer["dupAddrDetectTransmits"]["value"] = int(element_text)
                    interface_ipv6_dict_buffer["dupAddrDetectTransmits"]["observedAt"] = observedAt
            for autoconf in ipv6.findall(".//{urn:ietf:params:xml:ns:yang:ietf-ip}autoconf"):
                interface_ipv6_autoconf_dict_buffer = {}
                interface_ipv6_autoconf_dict_buffer["id"] = "urn:ngsi-ld:InterfaceIpv6Autoconf:" + interface_ipv6_dict_buffer["id"].split(":")[-1]
                interface_ipv6_autoconf_dict_buffer["type"] = "InterfaceIpv6Autoconf"
                interface_ipv6_autoconf_dict_buffer["isPartOf"] = {}
                interface_ipv6_autoconf_dict_buffer["isPartOf"]["type"] = "Relationship"
                interface_ipv6_autoconf_dict_buffer["isPartOf"]["object"] = interface_ipv6_dict_buffer["id"]
                interface_ipv6_autoconf_dict_buffer["isPartOf"]["observedAt"] = observedAt
                createGlobalAddresses = autoconf.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}create-global-addresses")
                if createGlobalAddresses is not None:
                    element_text = createGlobalAddresses.text
                    if element_text is not None:
                        interface_ipv6_autoconf_dict_buffer["createGlobalAddresses"] = {}
                        interface_ipv6_autoconf_dict_buffer["createGlobalAddresses"]["type"] = "Property"
                        interface_ipv6_autoconf_dict_buffer["createGlobalAddresses"]["value"] = eval(element_text.capitalize())
                        interface_ipv6_autoconf_dict_buffer["createGlobalAddresses"]["observedAt"] = observedAt
                createTemporaryAddresses = autoconf.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}create-temporary-addresses")
                if createTemporaryAddresses is not None:
                    element_text = createTemporaryAddresses.text
                    if element_text is not None:
                        interface_ipv6_autoconf_dict_buffer["createTemporaryAddresses"] = {}
                        interface_ipv6_autoconf_dict_buffer["createTemporaryAddresses"]["type"] = "Property"
                        interface_ipv6_autoconf_dict_buffer["createTemporaryAddresses"]["value"] = eval(element_text.capitalize())
                        interface_ipv6_autoconf_dict_buffer["createTemporaryAddresses"]["observedAt"] = observedAt
                temporaryValidLifetime = autoconf.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}temporary-valid-lifetime")
                if temporaryValidLifetime is not None:
                    element_text = temporaryValidLifetime.text
                    if element_text is not None:
                        interface_ipv6_autoconf_dict_buffer["id"] = interface_ipv6_autoconf_dict_buffer["id"] + int(element_text)
                        interface_ipv6_autoconf_dict_buffer["temporaryValidLifetime"] = {}
                        interface_ipv6_autoconf_dict_buffer["temporaryValidLifetime"]["type"] = "Property"
                        interface_ipv6_autoconf_dict_buffer["temporaryValidLifetime"]["value"] = int(element_text)
                        interface_ipv6_autoconf_dict_buffer["temporaryValidLifetime"]["observedAt"] = observedAt
                temporaryPreferredLifetime = autoconf.find(".//{urn:ietf:params:xml:ns:yang:ietf-ip}temporary-preferred-lifetime")
                if temporaryPreferredLifetime is not None:
                    element_text = temporaryPreferredLifetime.text
                    if element_text is not None:
                        interface_ipv6_autoconf_dict_buffer["temporaryPreferredLifetime"] = {}
                        interface_ipv6_autoconf_dict_buffer["temporaryPreferredLifetime"]["type"] = "Property"
                        interface_ipv6_autoconf_dict_buffer["temporaryPreferredLifetime"]["value"] = int(element_text)
                        interface_ipv6_autoconf_dict_buffer["temporaryPreferredLifetime"]["observedAt"] = observedAt
                dict_buffers.append(interface_ipv6_autoconf_dict_buffer)
            dict_buffers.append(interface_ipv6_dict_buffer)
        dict_buffers.append(interface_dict_buffer)
    return dict_buffers[::-1]

def init_ngsi_ld_client():
    configuration = NGSILDConfiguration(host=BROKER_URI)
    configuration.debug = True
    ngsi_ld = NGSILDClient(configuration=configuration)

    ngsi_ld.set_default_header(
        header_name="Link",
        header_value='<{0}>; '
                    'rel="http://www.w3.org/ns/json-ld#context"; '
                    'type="application/ld+json"'.format(CONTEXT_CATALOG_URI)
    )

    ngsi_ld.set_default_header(
        header_name="Accept",
        header_value="application/json"
    )

    return ngsi_ld

def create_ngsi_ld_entity(ngsi_ld, entity) -> bool:
    result = False
    
    api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

    entity_input = entity.to_dict()

    logger.info("Entity object representation: %s\n" % Entity.from_dict(entity_input))
    logger.info("QueryEntity200ResponseInner object representation: %s\n" % QueryEntity200ResponseInner.from_dict(entity_input))

    query_entity_input = QueryEntity200ResponseInner.from_dict(entity_input)

    try:
        # Create NGSI-LD entity of type Sensor: POST /entities
        api_response = api_instance.create_entity(query_entity200_response_inner=query_entity_input)
        #logger.info(api_response.to_dict())
        result = True
    except Exception as e:
        logger.exception("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)
        result = False

    return result

def retrieve_ngsi_ld_entity(ngsi_ld, entity_id: str) -> bool:
    result = False

    api_instance = ngsi_ld_client.ContextInformationConsumptionApi(ngsi_ld)

    try:
        # Retrieve NGSI-LD Entity by id: GET /entities/{entityId}
        api_response = api_instance.retrieve_entity(entity_id)
        #logger.info(api_response.to_dict())
        result = True
    except Exception as e:
        logger.exception("Exception when calling ContextInformationConsumptionApi->retrieve_entity: %s\n" % e)
        result = False
    
    return result

def update_ngsi_ld_entity(ngsi_ld, entity_id: str, entity) -> bool:
    result = False

    api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

    entity_input = entity.to_dict()

    #logger.info("Entity object representation: %s\n" % Entity.from_dict(entity_input))

    try:
        # Update NGSI-LD Entity by id: PATCH /entities/{entityId}/attrs
        api_response = api_instance.update_entity(entity_id, entity=Entity.from_dict(entity_input))
        #logger.info(api_response.to_dict())
        result = True
    except Exception as e:
        logger.exception("Exception when calling ContextInformationProvisionApi->update_entity: %s\n" % e)
        result = False

    return result

def get_entity_class_object_by_type(dict_buffer: dict):
    type = dict_buffer['type']
    if type == 'Interface':
        entity = Interface.from_dict(dict_buffer)
    if type == 'InterfaceStatistics':
        entity = InterfaceStatistics.from_dict(dict_buffer)
    if type == 'InterfaceIpv4':
        entity = InterfaceIpv4.from_dict(dict_buffer)
    if type == 'InterfaceIpv4Address':
        entity = InterfaceIpv4Address.from_dict(dict_buffer)
    if type == 'InterfaceIpv4Neighbor':
        entity = InterfaceIpv4Neighbor.from_dict(dict_buffer)
    if type == 'InterfaceIpv6':
        entity = InterfaceIpv6.from_dict(dict_buffer)
    if type == 'InterfaceIpv6Address':
        entity = InterfaceIpv6Address.from_dict(dict_buffer)
    if type == 'InterfaceIpv6Autoconf':
        entity = InterfaceIpv6Autoconf.from_dict(dict_buffer)
    if type == 'InterfaceIpv6Neighbor':
        entity = InterfaceIpv6Neighbor.from_dict(dict_buffer)
    return entity

## -- END AUXILIARY FUNCTIONS -- ##

print("Hello, I am the XML parser for NETCONF notifications and the NGSI-LD instantiator")

print("I will consume messages (NETCONF notifications) from a Kafka topic named interfaces-state-subscriptions")

consumer = KafkaConsumer('interfaces-state-subscriptions', bootstrap_servers=['kafka:9092'])

print("I will process every single notification, parse them and create/update NGSI-LD entities accordingly")
print("These entities will be uploaded to the NGSI-LD broker")

print("Initializing the NGSI-LD client...")

ngsi_ld = init_ngsi_ld_client()

print("Done!")

while True:
    for message in consumer:
        print("I have consumed a new notification!")

        dict_buffers = parse_xml(message)

        print("I have parsed the XML and created the associated NGSI-LD-compliant data structures/dictionary buffers")

        print("I will now create the NGSI-LD entities from the data structures/dictionary buffers")

        for dict_buffer in dict_buffers:
            entity_id = dict_buffer['id']
            
            entity = get_entity_class_object_by_type(dict_buffer)

            print("Dictionary buffer contains information for entity " + entity_id)

            exists = retrieve_ngsi_ld_entity(ngsi_ld, entity_id)
            if exists == False:
                print("Entity " + entity_id + " DOES NOT EXIST. Trying to create it...")
                created = create_ngsi_ld_entity(ngsi_ld, entity)
                if created == False:
                    print("Entity " + entity_id + " COULD NOT BE CREATED")
                else:
                    print("Entity " + entity_id + " WAS SUCCESSFULLY CREATED")
            else:
                print("Entity " + entity_id + " DOES EXIST. Trying to update it...")
                updated = update_ngsi_ld_entity(ngsi_ld, entity_id, entity)
                if updated == False:
                    print("Entity " + entity_id + " COULD NOT BE UPDATED")
                else:
                    print("Entity " + entity_id + " WAS SUCCESSFULLY UPDATED")
        
        print("Iteration done! Waiting for the next notification...")