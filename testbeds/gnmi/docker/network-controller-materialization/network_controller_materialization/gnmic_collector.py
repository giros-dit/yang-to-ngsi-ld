import sys
import re
from typing import Optional
import logging

from kafka import KafkaProducer

from ncclient import manager
from ncclient.xml_ import to_ele

import xml.etree.ElementTree as et
from xml.etree.ElementTree import Element, SubElement, tostring
from pydantic import BaseModel

import time
import datetime
from dateutil import parser
#from datetime import datetime
from datetime import datetime as dtime

import yaml
#import json
import csv
import ujson as json
import subprocess
import numpy as np

logger = logging.getLogger(__name__)

producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

performance_measurements_file = open("/opt/network-controller-materialization/network_controller_materialization/performance_measurements_operation.csv", "w", newline='')
csv_writer = csv.writer(performance_measurements_file)
csv_header = ["notified_at", "translation_started_at", "translation_finished_at", "translation_time", "mean_translation_time", "min_translation_time", "max_translation_time", 
              "operation_started_at", "operation_finished_at", "operation_time", "mean_operation_time", "min_operation_time", "max_operation_time",  "processing_time_since_notified_at", 
              "mean_processing_time_since_notified_at", "min_processing_time_since_notified_at", "max_processing_time_since_notified_at", "notifications_received"]
csv_writer.writerow(csv_header)   

translation_delta_times = []
operation_delta_times = []
processing_delta_times = []

'''
Get XPath from Context Catalog by searching the context registry key (i.e., the entity type URI field):
'''
def get_xpath_in_context_catalog(entity_type: str, all_context_data: Optional[dict]):

    xpath = ""
    entity_type_short = ""

    for key, value in all_context_data.items():
        if value == entity_type:
            entity_type_short = key
            xpath = "/" + value#.split(":", 1)[1]
            logger.info(f"XPath {xpath} relative to NGSI-LD Entity value {entity_type} was found!")
            break
    else:
        logger.info(f"XPath relative to NGSI-LD Entity value {entity_type} was not found!")

    return xpath, entity_type_short

'''
Build XPath with keys if the NGSI-LD entity ID is provided:
'''
def get_xpath_with_keys(xpath: str, entity_id: str, all_context_registries: Optional[list]) -> str:
    
    xpath_with_keys = ""
    
    xpath_split = xpath.split("/")

    subxpaths = []
    partial_xpaths = []
    
    if len(xpath_split) > 2 and xpath_split[0] == "":
        subxpaths.append("/" + xpath_split[1])
        subxpaths.extend(xpath_split[2:])  
    else:
        subxpaths.append("/" + xpath_split[1])
    
    for i in range(1, len(xpath_split)):
        partial_xpath = "/".join(xpath_split[:i+1]) # Build acumulative partial_xpath
        partial_xpaths.append(partial_xpath) # Add partial_xpath su partial_xpaths list

    entity_id_split = entity_id.split(":")
    index = entity_id_split.index(entity_id_split[2])
    entity_id_split = entity_id_split[index+1:]
    index = 1
    value_match = False
    for subxpath, partial_xpath in zip(subxpaths, partial_xpaths):
        for context_registry in all_context_registries:
            for key, value in context_registry["@context"].items():
                if ":" in value:
                    value = "/" + value#.split(":", 1)[1]
                if value == partial_xpath:
                    value_match = True
                    if "key" in context_registry:
                        key = context_registry["key"]
                        if xpath_with_keys == "":
                            xpath_with_keys = xpath_with_keys + subxpath + "[" + key + "='" + entity_id_split[index] + "']"
                        else:
                            xpath_with_keys = xpath_with_keys + "/" + subxpath + "[" + key + "='" + entity_id_split[index] + "']"
                        index = index + 1
                        break
                    else:
                        if xpath_with_keys == "":
                            xpath_with_keys = xpath_with_keys + subxpath
                        else:
                            xpath_with_keys = xpath_with_keys + "/" + subxpath
                        break
            
            if value_match:
                break

        if value_match == False:
            if xpath_with_keys == "":
                xpath_with_keys = xpath_with_keys + subxpath
            else:
                xpath_with_keys = xpath_with_keys + "/" + subxpath
            
            if subxpath == subxpaths[-1]:
                break
        
        value_match = False
    
    return xpath_with_keys

'''
Discover if the NGSI-LD Entity is configurable or not by providing the entity type in the long form (i.e., the entity type URI).
'''
def discover_config_entity_by_uri(entity_type: str, all_context_registries: Optional[list]) -> bool:
    
    short_entity_type = None
    configurable = False

    for context_registry in all_context_registries:
        if entity_type in context_registry["@context"].values():
            for key, value in context_registry["@context"].items():
                if value == entity_type:
                    short_entity_type = key
                    break
            if short_entity_type != None and "config" in context_registry.keys():
                config_elements = context_registry["config"]
                for config_element in config_elements:
                    if short_entity_type == config_element:
                        configurable = True
                        logger.info("Entity type " + entity_type + " is configurable!")
                        break

    if short_entity_type != None and configurable == False:
        logger.info("Entity type " + entity_type + " is not configurable!")

    return configurable

def update_gnmic_query_config(yaml_file, output_file, host, port, username, password, xpath):
    
    with open(yaml_file, 'r') as file:
        config = yaml.safe_load(file)
    
    address = f"{host}:{str(port)}"
    config['address'] = address
    config['username'] = username
    config['password'] = password
    
    if 'get-path' not in config:
        config['get-path'] = []
    xpath = f'{xpath}'
    config['get-path'] = [f"{xpath}"]

    with open(output_file, 'w') as file:
        yaml.dump(config, file, default_flow_style=False)
    
    print(f"gNMIc YAML configuration file {output_file} updated successfully!")

'''
Function for triggering gNMI RPC Get and Get-Config operations with needed parameters.
'''
def get_operation(host: str, port: str, username: str, password: str,  entity_type: str, entity_id: str, option: str, notified_at: str, all_context_data: Optional[dict] = None, all_context_registries: Optional[list] = None):

    # Load the YAML configuration file
    yaml_file = '/opt/network-controller-materialization/network_controller_materialization/gnmic-templates/gnmic_query_template.yaml'
    output_file = '/opt/network-controller-materialization/network_controller_materialization/gnmic-templates/gnmic_query_template_updated.yaml'
    
    translation_datetime_start = datetime.datetime.now(datetime.timezone.utc)
    xpath, entity_type_short = get_xpath_in_context_catalog(entity_type=entity_type, all_context_data=all_context_data)
    
    if entity_id != None:
        xpath = get_xpath_with_keys(xpath=xpath, entity_id=entity_id, all_context_registries=all_context_registries)

    # Update the YAML configuration file with the new address, username, and password
    update_gnmic_query_config(yaml_file, output_file, host, port, username, password, xpath)
    
    notified_at = parser.parse(notified_at)
    
    translation_datetime_stop = datetime.datetime.now(datetime.timezone.utc)
    translation_delta_time = (translation_datetime_stop - translation_datetime_start).total_seconds()
    translation_delta_times.append(translation_delta_time)
    
    operation_datetime_start = datetime.datetime.now(datetime.timezone.utc)

    with open(output_file, 'r') as file:
        config = yaml.safe_load(file)
    
    query = subprocess.run(["gnmic", "get", "--config",  "/opt/network-controller-materialization/network_controller_materialization/gnmic-templates/gnmic_query_template_updated.yaml"], capture_output=True, text=True, check=True, start_new_session=True)

    operation_datetime_stop = datetime.datetime.now(datetime.timezone.utc)
    operation_delta_time = (operation_datetime_stop - operation_datetime_start).total_seconds()
    operation_delta_times.append(operation_delta_time)

    processing_delta_time = (operation_datetime_stop - notified_at).total_seconds()
    processing_delta_times.append(processing_delta_time)

    #logger.info(query.stdout.strip().encode('utf-8'))
    query_output = json.loads(query.stdout.strip())
    epoch_time_data = int(query_output[0]["timestamp"])
    datetime_ns_data = np.datetime64(epoch_time_data, 'ns')
    timestamp_data = str(datetime_ns_data.astype('datetime64[ms]')) + 'Z'
    #timestamp_data = int(query.stdout.strip().encode('utf-8')[0]["timestamp"])
    logger.info("The original epoch time of the query reply is: " + str(epoch_time_data))
    logger.info("The original datetime of the query reply is: " + str(datetime_ns_data))
    logger.info("The original timestamp of the query reply is: " + timestamp_data)

    #datetime_ns = np.datetime64(timestamp_data, 'ns')
    #timestamp = str(datetime_ns.astype('datetime64[ms]')) + 'Z'
    current_epoch_time = int(time.time() * 1_000_000_000) #time.perf_counter_ns()
    datetime_ns = np.datetime64(current_epoch_time, 'ns')
    timestamp = str(datetime_ns.astype('datetime64[ms]')) + 'Z'
    logger.info("The current epoch time of the query reply is: " + str(current_epoch_time))
    logger.info("The current datetime of the query reply is: " + str(datetime_ns))
    logger.info("The current timestamp of the query reply is: " + timestamp)
    ##query.stdout.strip().encode('utf-8')[0]["timestamp"] = datetime_ns
    query_output[0]["timestamp"] = current_epoch_time

    #producer = KafkaProducer(bootstrap_servers=['kafka:9092'])
    ##producer.send('interfaces-state-queries', value=query.stdout.strip().encode('utf-8'))
    #producer.send('interfaces-state-queries', value=json.dumps(query_output).encode('utf-8'))
    producer.send('interfaces-state-queries', value=query_output)
    logger.info("I have sent it to a Kafka topic named interfaces-state-queries")
    ##logger.info("The timestamp of the query reply is: " + timestamp)
    producer.flush()

    csv_data = [notified_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), translation_datetime_start.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), translation_datetime_stop.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), str(translation_delta_time * 1e3) + " ms",
                str((sum(translation_delta_times)/len(translation_delta_times)) * 1e3) + " ms", str(min(translation_delta_times) * 1e3) + " ms", str(max(translation_delta_times) * 1e3) + " ms", operation_datetime_start.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), 
                operation_datetime_stop.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), str(operation_delta_time * 1e3) + " ms", str((sum(operation_delta_times)/len(operation_delta_times)) * 1e3) + " ms", str(min(operation_delta_times) * 1e3) + " ms", 
                str(max(operation_delta_times) * 1e3) + " ms", str(processing_delta_time * 1e3) + " ms", str((sum(processing_delta_times)/len(processing_delta_times)) * 1e3) + " ms", str(min(processing_delta_times) * 1e3) + " ms", 
                str(max(processing_delta_times) * 1e3) + " ms", str(len(processing_delta_times))]
    csv_writer.writerow(csv_data)
    performance_measurements_file.flush()