'''
XML Parser based on the ElementTree XML library.
Sample for ietf-interfaces with interface + statistics.
Reference documentation: https://docs.python.org/3/library/xml.etree.elementtree.html
Version 0.2.0
'''

import xml.etree.ElementTree as et
import logging
import logging.config
import yaml
import os
import re
import subprocess
import pdb

import ngsi_ld_client
from ngsi_ld_models.models.interface import Interface
from ngsi_ld_models.models.statistics import Statistics
from ngsi_ld_client.models.entity_input import EntityInput

from fastapi import FastAPI, Request, status
from ngsi_ld_client.api_client import ApiClient as NGSILDClient
from ngsi_ld_client.configuration import Configuration as NGSILDConfiguration
from ngsi_ld_client.exceptions import ApiException

## -- BEGIN LOGGING CONFIGURATION -- ##

with open('logging.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)

## -- END LOGGING CONFIGURATION -- ##

## -- BEGIN CONSTANTS -- ##

# Entity definitions:
INTERFACE_ENTITY_DEFINITION = "{urn:ietf:params:xml:ns:yang:ietf-interfaces}interface"
STATISTICS_ENTITY_DEFINITION = "{urn:ietf:params:xml:ns:yang:ietf-interfaces}statistics"

# NGSI-LD Context Broker:
BROKER_URI = os.getenv("BROKER_URI", "http://localhost:1026/ngsi-ld/v1")

# Context Catalog:
CONTEXT_CATALOG_URI = os.getenv("CONTEXT_CATALOG_URI", "http://context-catalog:8080/context.jsonld")

# Interface Property types:
INTERFACE_PROPERTY_TYPES = {
    "id": "String",
    "type": "String",
    "scope": "String",
    "location": "String",
    "observationSpace": "String",
    "operationSpace": "String",
    "createdAt": "String",
    "modifiedAt": "String",
    "deletedAt": "String",
    "name": "String",
    "description": "String",
    "enabled": "Boolean",
    "linkUpDownTrapEnable": "String",
    "adminStatus": "String",
    "operStatus": "String",
    "lastChange": "String",
    "ifIndex": "Integer",
    "physAddress": "String",
    "speed": "Integer",
    "higherLayerIf": "String",
    "lowerLayerIf": "String"
}

# Statistics Property types:
STATISTICS_PROPERTY_TYPES = {
    "id": "String",
    "type": "String",
    "scope": "String",
    "location": "String",
    "observationSpace": "String",
    "operationSpace": "String",
    "createdAt": "String",
    "modifiedAt": "String",
    "deletedAt": "String",
    "isPartOf": "String",
    "discontinuityTime": "String",
    "inOctets": "Integer",
    "inUnicastPkts": "Integer",
    "inBroadcastPkts": "Integer",
    "inMulticastPkts": "Integer",
    "inDiscards": "Integer",
    "inErrors": "Integer",
    "inUnknownProtos": "Integer",
    "outOctets": "Integer",
    "outUnicastPkts": "Integer",
    "outBroadcastPkts": "Integer",
    "outMulticastPkts": "Integer",
    "outDiscards": "Integer",
    "outErrors": "Integer"
}

## -- END CONSTANTS -- ##

## -- BEGIN IDENTIFICATION SEQUENCES -- ##

interface_id_seq = 0
statistics_id_seq = 0

## -- END IDENTIFICATION SEQUENCES -- ##

## -- BEGIN DICTIONARY BUFFER LISTS -- ##

interface_dict_buffers = []
statistics_dict_buffers = []

## -- END DICTIONARY BUFFER LISTS -- ##

def check_and_return_property_value(entity_def: str, element_tag: str, element_text: str):
    if (entity_def == INTERFACE_ENTITY_DEFINITION):
        property_type = INTERFACE_PROPERTY_TYPES[element_tag] # element_tag must be previously splitted to remove the namespace.
        if (property_type == "String"):
            return element_text
        elif (property_type == "Integer"):
            return int(element_text)
        elif (property_type == "Boolean"):
            if (element_text == "true"):
                return True
            else:
                return False
    if (entity_def == STATISTICS_ENTITY_DEFINITION):
        property_type = STATISTICS_PROPERTY_TYPES[element_tag] # element_tag must be previously splitted to remove the namespace.
        if (property_type == "String"):
            return element_text
        elif (property_type == "Integer"):
            return int(element_text)
        elif (property_type == "Boolean"):
            if (element_text == "true"):
                return True
            else:
                return False

def create_ngsi_ld_entity(entity):
    # Init NGSI-LD Client
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

    api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

    entity_input = entity.to_dict()

    logger.info("Interface object representation: %s\n" % entity_input)

    logger.info("EntityInput object representation: %s\n" % EntityInput.from_dict(entity_input))

    try:
        # Create NGSI-LD entity of type Sensor: POST /entities
        api_instance.create_entity(entity_input=EntityInput.from_dict(entity_input))
    except Exception as e:
        logger.exception("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)

def is_entity(element_len: int) -> bool:
    result = False
    if (element_len > 0):
        result = True
    return result

def is_property(element_len: int) -> bool:
    result = False
    if (element_len == 0):
        result = True
    return result

def to_camel_case(element_tag: str, element_len: int) -> str:
    if (element_tag is None) or (element_len is None):
        return element_tag
    else:
        if (is_entity(element_len) == True):
            return element_tag.capitalize()
        if (is_property(element_len) == True):
            return re.sub(r"(-)(\w)", lambda m: m.group(2).upper(), element_tag)

def print_data_recursively(element):
    element_len = len(element)
    if (is_entity(element_len) == True):
        print(to_camel_case(element.tag.split("}")[1], element_len) + " is an Entity")
    if (is_property(element_len) == True):
        print(to_camel_case(element.tag.split("}")[1], element_len) + " is a Property with value: " + element.text)
    for child in element:
        print_data_recursively(child)

def get_data_recursively(element, parent_element_tag, dict_buffer):
    element_tag = str(element.tag)
    element_text = str(element.text)
    element_len = len(element)
    if (is_entity(element_len) == True):
        if (element_tag == INTERFACE_ENTITY_DEFINITION):
            global interface_id_seq
            interface_dict_buffer = {}
            interface_dict_buffer["id"] = "urn:ngsi-ld:Interface:" + str(interface_id_seq)
            interface_dict_buffer["type"] = "Interface"
            parent_element_tag = element_tag
            for child in element:
                get_data_recursively(child, parent_element_tag, interface_dict_buffer)
            interface_dict_buffers.append(interface_dict_buffer)
            interface_id_seq = interface_id_seq + 1
        if (element_tag == STATISTICS_ENTITY_DEFINITION):
            global statistics_id_seq
            statistics_dict_buffer = {}
            statistics_dict_buffer["id"] = "urn:ngsi-ld:Statistics:" +  str(statistics_id_seq)
            statistics_dict_buffer["type"] = "Statistics"
            statistics_dict_buffer["isPartOf"] = {}
            statistics_dict_buffer["isPartOf"]["type"] = "Relationship"
            statistics_dict_buffer["isPartOf"]["object"] = "urn:ngsi-ld:Interface:" + str(statistics_id_seq)
            parent_element_tag = element_tag
            for child in element:
                get_data_recursively(child, parent_element_tag, statistics_dict_buffer)
            statistics_dict_buffers.append(statistics_dict_buffer)
            statistics_id_seq = statistics_id_seq + 1
    if (is_property(element_len) == True):
        element_tag = to_camel_case(element_tag.split("}")[1], element_len)
        if (element_tag != "type"): # The 'type' tag value in the XML file does not work as of now, it must be 'Interface' before creating the NGSI-LD Entity.
            if (element_tag == 'lowerLayerIf'): # This is identified as a Property though is a Relationship - must be addressed. 
                dict_buffer[element_tag] = {}
                dict_buffer[element_tag]["type"] = "Relationship"
                dict_buffer[element_tag]["object"] = "urn:ngsi-ld:Interface:" + str(interface_id_seq - 1)
            elif (element_tag == 'higherLayerIf'): # This is identified as a Property though is a Relationship - must be addressed.
                dict_buffer[element_tag] = {}
                dict_buffer[element_tag]["type"] = "Relationship"
                dict_buffer[element_tag]["object"] = "urn:ngsi-ld:Interface:" + str(interface_id_seq + 1)
            else:
                dict_buffer[element_tag] = {}
                dict_buffer[element_tag]["type"] = "Property"
                dict_buffer[element_tag]["value"] = check_and_return_property_value(parent_element_tag, element_tag, element_text)

tree = et.parse('sample-ietf-interfaces.xml')

root = tree.getroot()

for child in root:
    get_data_recursively(child, None, None)

# Print Interface dictionary buffers:
print("## -- INTERFACE DICTIONARY BUFFERS -- ##\n")
for interface_dict_buffer in interface_dict_buffers:
    print(interface_dict_buffer)
    print("\n")
    
print("## -- ##\n")

# Print Statistics dictionary buffers:
print("## -- STATISTICS DICTIONARY BUFFERS -- ##\n")
for statistics_dict_buffer in statistics_dict_buffers:
    print(statistics_dict_buffer)
    print("\n")

print("## -- ##\n")

# Create Interface NGSI-LD Entities:
print("## -- CREATING INTERFACE NGSI-LD ENTITIES -- ##\n")
for interface_dict_buffer in interface_dict_buffers:
    interface = Interface.from_dict(interface_dict_buffer)
    create_ngsi_ld_entity(interface)
    print("\n")
    
# Create Statistics NGSI-LD Entities:
print("## -- CREATING STATISTICS NGSI-LD ENTITIES -- ##\n")
for statistics_dict_buffer in statistics_dict_buffers:
    statistics = Statistics.from_dict(statistics_dict_buffer)
    create_ngsi_ld_entity(statistics)
    print("\n")

# pdb.set_trace()
