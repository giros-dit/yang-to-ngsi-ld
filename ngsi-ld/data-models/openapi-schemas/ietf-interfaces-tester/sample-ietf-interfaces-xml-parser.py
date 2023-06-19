'''
XML Parser based on the ElementTree XML library.
Sample for ietf-interfaces with interface + statistics (reduced version).
Reference documentation: https://docs.python.org/3/library/xml.etree.elementtree.html
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

## -- LOGGING CONFIGURATION --

with open('logging.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)


## -- BEGIN CONSTANTS --

# Entity definitions:
INTERFACE_ENTITY_DEFINITION = "{urn:ietf:params:xml:ns:yang:ietf-interfaces}interface"
STATISTICS_ENTITY_DEFINITION = "{urn:ietf:params:xml:ns:yang:ietf-interfaces}statistics"

# NGSI-LD Context Broker:
BROKER_URI = os.getenv("BROKER_URI", "http://localhost:1026/ngsi-ld/v1")

# Context Catalog:
CONTEXT_CATALOG_URI = os.getenv("CONTEXT_CATALOG_URI", "http://context-catalog:8080/context.jsonld")

## -- END CONSTANTS --

def create_entity(entity):
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

def get_data_recursively(element, json_buffer):
    element_tag = str(element.tag)
    element_text = str(element.text)
    element_len = len(element)
    if (is_entity(element_len) == True):
        json_buffer = {}
        for child in element:
            get_data_recursively(child, json_buffer)
        if (element_tag == INTERFACE_ENTITY_DEFINITION):
            interface = Interface.__pydantic_model__.parse_raw(json_buffer)
            create_entity(interface)
        elif (element_tag == STATISTICS_ENTITY_DEFINITION):
            statistics = Statistics.__pydantic_model__.parse_raw(json_buffer)
            create_entity(statistics)
    if (is_property(element_len) == True):
        json_buffer[to_camel_case(element_tag, element_len)] = element_text

tree = et.parse('sample-ietf-interfaces-reduced1.xml')

root = tree.getroot()

for child in root:
    get_data_recursively(child, None)

# pdb.set_trace()
