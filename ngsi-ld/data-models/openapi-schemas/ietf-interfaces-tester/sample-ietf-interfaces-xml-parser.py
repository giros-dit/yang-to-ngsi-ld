'''
XML Parser based on the ElementTree XML library.
Sample for ietf-interfaces with interface + statistics.
It doesn't parse IPv4/IPv6 information.
Reference documentation: https://docs.python.org/3/library/xml.etree.elementtree.html

Author: Networking and Virtualization Research Group (GIROS-DIT UPM).
Version: 0.2.7
'''

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

## -- BEGIN CONSTANTS DECLARATION -- ##

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

## -- END CONSTANTS DECLARATION -- ##

## -- BEGIN DICTIONARY BUFFER LISTS DECLARATION -- ##

interface_dict_buffers = []
statistics_dict_buffers = []

## -- END DICTIONARY BUFFER LISTS DECLARATION -- ##

## -- BEGIN PERFORMANCE MEASUREMENT (EXECUTION TIMES) LISTS DECLARATION -- #

parsing_exec_times = []
interface_entity_creation_exec_times = []
statistics_entity_creation_exec_times = []

## -- END PERFORMANCE MEASUREMENT (EXECUTION TIMES) LISTS DECLARATION -- #

## -- BEGIN FUNCTIONS DECLARATION -- ##

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


entity_infos = {}

ROOT_PREFIX =  "urn:ngsi-ld:Interface:" 
entity_infos[INTERFACE_ENTITY_DEFINITION] = {}
entity_infos[INTERFACE_ENTITY_DEFINITION]["hasPartOf"] = False
entity_infos[INTERFACE_ENTITY_DEFINITION]["type"] = "Interface"
entity_infos[INTERFACE_ENTITY_DEFINITION]["idPrefix"] = ""
entity_infos[INTERFACE_ENTITY_DEFINITION]["isPartOfPrefix"] = ""
entity_infos[INTERFACE_ENTITY_DEFINITION]["buffers"] = []

entity_infos[STATISTICS_ENTITY_DEFINITION] = {}
entity_infos[STATISTICS_ENTITY_DEFINITION]["hasPartOf"] = True
entity_infos[STATISTICS_ENTITY_DEFINITION]["type"] = "Statistics"
entity_infos[STATISTICS_ENTITY_DEFINITION]["idPrefix"] = "urn:ngsi-ld:Statistics:"
entity_infos[STATISTICS_ENTITY_DEFINITION]["isPartOfPrefix"] = ROOT_PREFIX
entity_infos[STATISTICS_ENTITY_DEFINITION]["buffers"] = []

def get_data_recursively(element, parent_element_tag, dict_buffer):
    element_tag = str(element.tag)
    element_text = str(element.text)
    element_len = len(element)

    if (element_tag in entity_infos.keys()):
        entity_info = entity_infos[element_tag]
        new_dict_buffer = {} 
        if (not entity_info["hasPartOf"]):
            new_dict_buffer["id"] = ""
            new_dict_buffer["type"] = entity_info["type"]
            for child in element:
                get_data_recursively(child, element_tag, new_dict_buffer)
            entity_info["buffers"].append(new_dict_buffer)
        else:
            new_dict_buffer["id"] = entity_info["idPrefix"] + dict_buffer["name"]["value"]
            new_dict_buffer["type"] = entity_info["type"]
            new_dict_buffer["isPartOf"] = {}
            new_dict_buffer["isPartOf"]["type"] = "Relationship"
            new_dict_buffer["isPartOf"]["object"] = entity_info["isPartOfPrefix"] + dict_buffer["name"]["value"]
            for child in element:
                get_data_recursively(child, element_tag, new_dict_buffer)
            entity_info["buffers"].append(new_dict_buffer)
    if (is_property(element_len) == True):
        element_tag = to_camel_case(element_tag.split("}")[1], element_len)
        if (element_tag == 'name'): # Element tag 'name' is only present in '<interface>'.
            dict_buffer["id"] = "urn:ngsi-ld:Interface:" + element.text
            dict_buffer[element_tag] = {}
            dict_buffer[element_tag]["type"] = "Property"
            dict_buffer[element_tag]["value"] = check_and_return_property_value(parent_element_tag, element_tag, element_text)
        elif (element_tag == 'lowerLayerIf'): # This is identified as a Property though is a Relationship - must be addressed. 
            dict_buffer[element_tag] = {}
            dict_buffer[element_tag]["type"] = "Relationship"
            dict_buffer[element_tag]["object"] = ROOT_PREFIX + element_text
        elif (element_tag == 'higherLayerIf'): # This is identified as a Property though is a Relationship - must be addressed.
            dict_buffer[element_tag] = {}
            dict_buffer[element_tag]["type"] = "Relationship"
            dict_buffer[element_tag]["object"] = ROOT_PREFIX + element_text
        else:
            if (element_tag != "type"):
                dict_buffer[element_tag] = {}
                dict_buffer[element_tag]["type"] = "Property"
                dict_buffer[element_tag]["value"] = check_and_return_property_value(parent_element_tag, element_tag, element_text)

## -- END FUNCTIONS DECLARATION -- #

## -- BEGIN MAIN CODE -- ##

# Help with performance measurements: https://erickmccollum.com/2021/10/31/three-ways-to-measure-python-performance.html

# Performance measurements over 1000 iterations of XML parsing (from file reading to data saving into dictionary buffers):

# for i in range(1, 1001):
REPETITIONS=1
for i in range(0, REPETITIONS):
    iteration_start_time = time.perf_counter_ns()

    tree = et.parse('sample-ietf-interfaces.xml')
    root = tree.getroot()
    for child in root:
        get_data_recursively(child, None, None)
    
    iteration_stop_time = time.perf_counter_ns()

    iteration_exec_time = iteration_stop_time - iteration_start_time

    print(f"ITERATION #{i} EXECUTION TIME: {iteration_exec_time} ns | {iteration_exec_time/1e3} µs | {iteration_exec_time/1e6} ms\n")
    
    parsing_exec_times.append(iteration_exec_time)

print(f"XML PARSING EXECUTION TIMES - SUMMARY (OVER {len(parsing_exec_times)} ITERATIONS)")
parsing_mean_exec_time = sum(parsing_exec_times)/len(parsing_exec_times)
parsing_min_exec_time = min(parsing_exec_times)
parsing_max_exec_time = max(parsing_exec_times)
print(f"MEAN VALUE: {parsing_mean_exec_time} ns | {parsing_mean_exec_time/1e3} µs | {parsing_mean_exec_time/1e6} ms")
print(f"MIN VALUE: {parsing_min_exec_time} ns | {parsing_min_exec_time/1e3} µs | {parsing_min_exec_time/1e6} ms")
print(f"MAX VALUE: {parsing_max_exec_time} ns | {parsing_max_exec_time/1e3} µs | {parsing_max_exec_time/1e6} ms")

# Print Interface dictionary buffers:
print("\n")
print("## -- INTERFACE DICTIONARY BUFFERS -- ##\n")
for interface_dict_buffer in entity_infos[INTERFACE_ENTITY_DEFINITION]["buffers"]:
    print(interface_dict_buffer)
    print("\n")
    
print("## -- ##\n")

# Print Statistics dictionary buffers:
print("## -- STATISTICS DICTIONARY BUFFERS -- ##\n")
for statistics_dict_buffer in entity_infos[STATISTICS_ENTITY_DEFINITION]["buffers"]:
    print(statistics_dict_buffer)
    print("\n")

print("## -- ##\n")

quit()

# Performance measurements for NGSI-LD entities creation:

# Interfaces:

interface_seq = 1
for interface_dict_buffer in interface_dict_buffers:
    interface_entity_creation_start_time = time.perf_counter_ns()

    interface_dict_buffer["id"] = interface_dict_buffer["id"] + ":" + str(interface_seq)
    interface = Interface.from_dict(interface_dict_buffer)
    create_ngsi_ld_entity(interface)

    interface_entity_creation_stop_time = time.perf_counter_ns()

    interface_entity_creation_exec_time = interface_entity_creation_stop_time - interface_entity_creation_start_time

    print(f"NGSI-LD INTERFACE ENTITY #{interface_seq} CREATION TIME: {interface_entity_creation_exec_time} ns | {interface_entity_creation_exec_time/1e3} µs | {interface_entity_creation_exec_time/1e6} ms\n")

    interface_entity_creation_exec_times.append(interface_entity_creation_exec_time)
    interface_seq+=1

print(f"NGSI-LD INTERFACE ENTITIES CREATION EXECUTION TIMES - SUMMARY (OVER {len(interface_dict_buffers)} DICTIONARY BUFFERS)")
interface_entity_creation_mean_exec_time = sum(interface_entity_creation_exec_times)/len(interface_entity_creation_exec_times)
interface_entity_creation_min_exec_time = min(interface_entity_creation_exec_times)
interface_entity_creation_max_exec_time = max(interface_entity_creation_exec_times)
print(f"MEAN VALUE: {interface_entity_creation_mean_exec_time} ns | {interface_entity_creation_mean_exec_time/1e3} µs | {interface_entity_creation_mean_exec_time/1e6} ms")
print(f"MIN VALUE: {interface_entity_creation_min_exec_time} ns | {interface_entity_creation_min_exec_time/1e3} µs | {interface_entity_creation_min_exec_time/1e6} ms")
print(f"MAX VALUE: {interface_entity_creation_max_exec_time} ns | {interface_entity_creation_max_exec_time/1e3} µs | {interface_entity_creation_max_exec_time/1e6} ms")

# Statistics:

statistics_seq = 1
for statistics_dict_buffer in statistics_dict_buffers:
    statistics_entity_creation_start_time = time.perf_counter_ns()

    statistics_dict_buffer["id"] = statistics_dict_buffer["id"] + ":" + str(statistics_seq)
    statistics = Statistics.from_dict(statistics_dict_buffer)
    create_ngsi_ld_entity(statistics)

    statistics_entity_creation_stop_time = time.perf_counter_ns()

    statistics_entity_creation_exec_time = statistics_entity_creation_stop_time - statistics_entity_creation_start_time

    print(f"NGSI-LD STATISTICS ENTITY #{statistics_seq} CREATION TIME: {statistics_entity_creation_exec_time} ns | {statistics_entity_creation_exec_time/1e3} µs | {statistics_entity_creation_exec_time/1e6} ms\n")

    statistics_entity_creation_exec_times.append(statistics_entity_creation_exec_time)
    statistics_seq+=1

print(f"NGSI-LD STATISTICS ENTITIES CREATION EXECUTION TIMES - SUMMARY (OVER {len(statistics_dict_buffers)} DICTIONARY BUFFERS)")
statistics_entity_creation_mean_exec_time = sum(statistics_entity_creation_exec_times)/len(statistics_entity_creation_exec_times)
statistics_entity_creation_min_exec_time = min(statistics_entity_creation_exec_times)
statistics_entity_creation_max_exec_time = max(statistics_entity_creation_exec_times)
print(f"MEAN VALUE: {statistics_entity_creation_mean_exec_time} ns | {statistics_entity_creation_mean_exec_time/1e3} µs | {statistics_entity_creation_mean_exec_time/1e6} ms")
print(f"MIN VALUE: {statistics_entity_creation_min_exec_time} ns | {statistics_entity_creation_min_exec_time/1e3} µs | {statistics_entity_creation_min_exec_time/1e6} ms")
print(f"MAX VALUE: {statistics_entity_creation_max_exec_time} ns | {statistics_entity_creation_max_exec_time/1e3} µs | {statistics_entity_creation_max_exec_time/1e6} ms")

'''

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
'''

# pdb.set_trace()

## -- END MAIN CODE -- ##
