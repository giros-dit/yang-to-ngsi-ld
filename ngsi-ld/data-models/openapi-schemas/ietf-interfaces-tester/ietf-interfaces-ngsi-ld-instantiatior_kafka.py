import os
import logging
import logging.config
import pdb
import yaml

from confluent_kafka import Consumer

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

# NGSI-LD Context Broker:
BROKER_URI = os.getenv("BROKER_URI", "http://localhost:1026/ngsi-ld/v1")

# Context Catalog:
CONTEXT_CATALOG_URI = os.getenv("CONTEXT_CATALOG_URI", "http://context-catalog:8080/context.jsonld")

## -- END CONSTANTS DECLARATION -- ##

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

    try:
        # Create NGSI-LD entity of type Sensor: POST /entities
        api_instance.create_entity(entity_input=EntityInput.from_dict(entity_input))
    except Exception as e:
        logger.exception("Exception when calling ContextInformationProvisionApi->create_entity: %s\n" % e)

'''
Consume from the 'dictionary-buffers' Kafka topic, identify NGSI-LD Entities, create their instances
and upsert them to the Orion-LD broker.
'''

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['dictionary-buffers'])

while True:
    message = consumer.poll()

    if message is None:
        continue
    if message.error():
        print("Consumer error: {}".format(message.error()))
        continue

    dict_buffers = eval(message.value().decode('utf-8'))

    for dict_buffer in dict_buffers:
        type = dict_buffer['type']
        if type == 'Interface':
            interface = Interface.from_dict(dict_buffer)
            create_ngsi_ld_entity(interface)
        if type == 'Statistics':
            statistics = Statistics.from_dict(dict_buffer)
            create_ngsi_ld_entity(statistics)
