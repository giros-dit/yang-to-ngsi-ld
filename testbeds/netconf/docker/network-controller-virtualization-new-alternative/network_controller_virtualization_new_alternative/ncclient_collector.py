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
from datetime import datetime

logger = logging.getLogger(__name__)

'''
Get XPath from Context Catalog by searching the context registry key (i.e., the entity type field):
'''
def get_xpath_in_context_catalog(entity_type: str, all_context_data: Optional[dict]) -> str:

    xpath = ""

    if str(entity_type) in all_context_data:
        search_context_data = all_context_data[entity_type]
        xpath =  "/" + search_context_data.split(":", 1)[1]
        logger.info("XPath " + xpath + " relative to NGSI-LD Entity type " + entity_type + " was founded!")
    else:
        logger.info("XPath relative to NGSI-LD Entity type " + entity_type + " was not founded!")

    return xpath

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
            for key, value in context_registry.items():
                if ":" in value:
                    value = "/" + value.split(":", 1)[1]
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

def get_xpath_with_keys_full(xpath: str, all_context_registries: Optional[list]) -> str:
    
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

    value_match = False
    for subxpath, partial_xpath in zip(subxpaths, partial_xpaths):
        for context_registry in all_context_registries:
            for key, value in context_registry.items():
                if ":" in value:
                    value = "/" + value.split(":", 1)[1]
                if value == partial_xpath:
                    value_match = True
                    if "key" in context_registry:
                        key = context_registry["key"]
                        if xpath_with_keys == "":
                            xpath_with_keys = xpath_with_keys + subxpath + "[" + key + "='*']"
                        else:
                            xpath_with_keys = xpath_with_keys + "/" + subxpath + "[" + key + "='*']"
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
Main function to convert a Pydantic instance to XML schema from NETCONF for ncclient get-config operations
'''
def generate_netconf_xml_config(xpath: str, all_context_data: Optional[dict], entity_type: str) -> str:

    root = None
    current_element = None

    search_original_context_data = all_context_data[entity_type]
    search_processed_context_data = xpath

    original_components = search_original_context_data.split("/")

    processed_components = search_processed_context_data.strip("/").split("/")

    for original_component, processed_component in zip(original_components, processed_components):
        
        if ":" in processed_component:
            processed_component = processed_component.split(":")[1]

        # Check if it contains a filter (e.g., [name='Ethernet1'])
        if '[' in processed_component:
            tag, condition = processed_component.split('[')
            tag = tag.strip()
            condition = condition.strip(']').split('=')
            attr_name = condition[0].strip()
            attr_value = condition[1].strip().strip("'")
        else:
            tag = processed_component.strip()
            attr_name = None
            attr_value = None

        # Create the new element
        element = et.Element(tag)

        if ":" in original_component:
            ns = original_component.split(":")[0]
            et.register_namespace('', str("urn:ietf:params:xml:ns:yang:"+ns)) 
            element.set("xmlns", str("urn:ietf:params:xml:ns:yang:"+ns))

        # If there is an attribute, add it as text inside the element
        if attr_name and attr_value:
            if original_component != original_components[-1]:
                child = et.SubElement(element, attr_name)
                if attr_value != "*":
                    child.text = attr_value
            elif attr_value != "*":
                child = et.SubElement(element, attr_name)
                child.text = attr_value

        # If it is the first element, initialize the schema tree
        if root is None:
            root = element
        else:
            # If not the first element, add as child
            current_element.append(element)
        
        # Move the pointer to the current element
        current_element = element

    # We return the XML as a string
    return et.tostring(root, encoding="unicode", method='xml')

'''
Function for triggering NETCONF RPC Get and Get-Config operations with needed parameters.
'''
def get_operation(host: str, port: str, username: str, password: str, family: str, entity_type: str, entity_id: str, option: str, all_context_data: Optional[dict] = None, hostKeyVerify: Optional[bool] = False, sysAttrs: Optional[bool] = False, all_context_registries: Optional[list] = None):
    r = {
        "host": host,
        "port": port,
        "username": username,
        "password": password,
        "hostkey_verify": hostKeyVerify,
        "device_params": {"name": family}
    }

    logger.info("Hello, this is the ncclient-collector for " + host + " for GET operations...")
    
    session = manager.connect(**r)

    logger.info("I have successfully established a session with ID# " + session.session_id)

    xpath = get_xpath_in_context_catalog(entity_type=entity_type, all_context_data=all_context_data)
    
    if entity_id != None:
        xpath = get_xpath_with_keys(xpath=xpath, entity_id=entity_id, all_context_registries=all_context_registries)

    if option == "config":
        # Create a configuration filter
        '''
        interface_filter = """
        <interfaces
            xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>{0}</name>
            </interface>
        </interfaces>
        """.format(interface)
        '''
        '''
        interface_filter = f"""
        <interfaces
            xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                {"<name>" + str(interface) + "</name>" if interface is not None else ""}
            </interface>
        </interfaces>
        """
        '''
        if entity_id == None:
            xpath = get_xpath_with_keys_full(xpath=xpath, all_context_registries=all_context_registries)
        interface_filter = generate_netconf_xml_config(xpath=xpath, all_context_data=all_context_data, entity_type=entity_type)
        logger.info("XML data schema: " + str(interface_filter))
        try:
            # Execute the get-config RPC
            reply = session.get_config(source="running", filter=("subtree", interface_filter))

            logger.info("\nInterface configuration of network device " + host + " for X-Path " + xpath + ": \n")
            logger.info(reply)
            data_element = et.fromstring(str(reply)).find('.//{urn:ietf:params:xml:ns:netconf:base:1.0}data')
            if data_element is None or len(data_element) == 0:
                logger.info("\nThe requested config schema tree is incorrect or not supported by the network device " + host + ".")
                session.close_session()
                return
        except Exception as e:
            logger.exception(f"Error for establishing the Get Config operation: {e}")
            session.close_session()
            return
    
    elif option == "state":
        try:
            # Execute the get RPC
            # Create a filter
            '''
            interface_filter = """
            <interfaces-state
                xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface>
                    <name>{0}</name>
                </interface>
            </interfaces-state>
            """.format(interface)
            '''
            #reply = session.get(filter=("subtree", interface_filter)) 

            # Execute the get RPC
            reply = session.get(filter=('xpath', xpath))

            logger.info("\nInterface operational status of network device " + host + " for X-Path " + xpath + ": \n")
            logger.info(reply)
            data_element = et.fromstring(str(reply)).find('.//{urn:ietf:params:xml:ns:netconf:base:1.0}data')
            if data_element is None or len(data_element) == 0:
                logger.info("\nThe Xpath is incorrect or not supported by the network device " + host + ".")
                session.close_session()
                return
        except Exception as e:
            logger.exception(f"Error for establishing the Get operation: {e}")
            session.close_session()
            return

    session.close_session()

    producer = KafkaProducer(bootstrap_servers=['kafka:9092'])
    reply = str(reply.data_xml)
    root = et.fromstring(reply)

    # A new subelement is added to the NETCONF notification: evenTime.
    # It is the current date and time when the operation was realized.
    # WARNING: This is not defined in the specification.
    currentime = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f') + 'Z'
    eventTime = et.SubElement(root, 'eventTime')
    eventTime.text = str(currentime)
    
    # A new subelement is added to the NETCONF notification: fromDevice.
    # It is the name of the device that is sending the notification.
    # WARNING: This is not defined in the specification.
    from_device = et.SubElement(root, 'fromDevice')
    from_device.text = host

    # A new subelement is added to the NETCONF notification: operation.
    # It is the name of the operation.
    # WARNING: This is not defined in the specification.
    operation = et.SubElement(root, 'operation')
    if option == "config":
        operation.text = "get_config"
    else:   
        operation.text = "get"

    # A new subelement is added to the NETCONF notification: sysAttrs.
    # It is the system-attribute parameter value.
    # WARNING: This is not defined in the specification.
    sys_attrs = et.SubElement(root, 'sysAttrs')
    sys_attrs.text = str(sysAttrs)

    query_xml = et.tostring(root, encoding='unicode')
    logger.info(query_xml)
    producer.send('interfaces-state-subscriptions', value=query_xml.encode('utf-8'))
    logger.info("I have sent it to a Kafka topic named interfaces-state-subscriptions")
    logger.info("The eventTime element of the query reply is: " + eventTime.text)
    producer.flush()
    

'''
Function to convert string from camelcase format (e.g., linkUpDownTrapEnable) to kebabcase format (e.g., link-up-down-trap-enable)
'''
def camel_to_kebab(camel_str):
    # Insert a hyphen separator before any uppercase letter that is not at the start of the word
    kebab_str = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', camel_str)
    # Convert the whole string to lowercase
    return kebab_str.lower()

'''
Recursive function to generate XML schema from a Pydantic model
'''
def pydantic_to_xml(element, obj):
    if isinstance(obj, BaseModel):
        # We loop through all the fields of the Pydantic class
        for field, value in obj.model_dump(by_alias=True, exclude_unset=True, exclude_none=True).items():
             # We omit the 'id' and 'type' fields from the NGSI-LD model
            if field in ("id", "type"):
                continue

            kebab_field = camel_to_kebab(field)
            child = Element(kebab_field)
            # If the field is another Pydantic object, we make a recursive call
            if isinstance(value, BaseModel):
                pydantic_to_xml(child, value)
            elif isinstance(value, dict):  # If it is a dictionary, we manage its keys and values
                if "value" in value:
                    # We check if the value is boolean and transform it to lowercase
                    if isinstance(value["value"], bool):
                        child.text = str(value["value"]).lower()
                    else:
                        child.text = str(value["value"])
                else:
                    # If it has no "value", we skip the element
                    continue
            elif isinstance(value, list): # If it is a list, we iterate over the elements
                for item in value:
                    item_element = Element(camel_to_kebab(field[:-1]))   # We use the kebabcase format for labels
                    if isinstance(item, BaseModel):
                        pydantic_to_xml(item_element, item)
                    else:
                        item_element.text = str(item)
                    child.append(item_element)
            else:
                # If it is a primitive value, we convert it to text
                child.text = str(value) if value is not None else ""
            if element.find(str(child.tag)) is None:
                element.append(child)
    return element

'''
Main function to convert a Pydantic instance to XML schema from NETCONF with <config> structure for ncclient edit-config operations:
'''
def generate_netconf_xml_set(xpath: str, instance: BaseModel, all_context_data: Optional[dict]) -> str:
    
    # Initial structure <config>
    config = Element("config", xmlns="urn:ietf:params:xml:ns:netconf:base:1.0")
    schema_tags = None

    if str(instance.to_dict()["type"]) in all_context_data:
        search_context_data = all_context_data[instance.to_dict()["type"]]
        processed_context_data =  "/" + search_context_data.split(":", 1)[1]
        if "[" in xpath and "]" in xpath:
            xpath_filter = re.sub(r"\[.*?\]", "", xpath)
        else:
            xpath_filter = xpath
        
        if xpath_filter == processed_context_data:
            original_components = search_context_data.split("/")
            processed_components = xpath.strip("/").split("/")
            schema_tags = config
            for original_component, processed_component in zip(original_components, processed_components):

                # Check if it contains a filter (e.g., [name='Ethernet1'])
                if '[' in processed_component:
                    tag, condition = processed_component.split('[')
                    tag = tag.strip()
                    condition = condition.strip(']').split('=')
                    attr_name = condition[0].strip()
                    attr_value = condition[1].strip().strip("'")
                else:
                    tag = processed_component.strip()
                    attr_name = None
                    attr_value = None

                if ":" in original_component:
                    ns = original_component.split(":")[0]
                    # Add <tag> with YANG namespace
                    schema_tags = SubElement(schema_tags, original_component.split(":")[1], xmlns=str("urn:ietf:params:xml:ns:yang:"+ns))
                else:
                    # Add <tag>
                    schema_tags = SubElement(schema_tags, original_component)

                # If there is an attribute, add it as text inside the element
                if attr_name and attr_value:
                    tag = SubElement(schema_tags, attr_name)
                    tag.text = attr_value

    # We generate XML based on the Pydantic model inside lower level <tag>
    pydantic_to_xml(schema_tags, instance)
    
    # We return the XML as a string
    return tostring(config, encoding="unicode", method='xml')

'''
Function for triggering NETCONF RPC Set operation with needed parameters.
'''
def set_operation(host: str, port: str, username: str, password: str, family: str, instance: BaseModel, entity_type: str, entity_id: str, all_context_data: Optional[dict], hostKeyVerify: Optional[bool] = False, all_context_registries: Optional[list] = None):
    r = {
        "host": host,
        "port": port,
        "username": username,
        "password": password,
        "hostkey_verify": hostKeyVerify,
        "device_params": {"name": family}
    }

    xpath = get_xpath_in_context_catalog(entity_type=entity_type, all_context_data=all_context_data)
    if entity_id != None:
        xpath = get_xpath_with_keys(xpath=xpath, entity_id=entity_id, all_context_registries=all_context_registries)

    config_xml_schema = generate_netconf_xml_set(xpath=xpath, instance=instance, all_context_data=all_context_data)

    logger.info("XML data schema: " + str(config_xml_schema))

    logger.info("Hello, this is the ncclient-collector for " + host + " for SET operations...")

    session = manager.connect(**r)
    logger.info("I have successfully established a session with ID# " + session.session_id)

    # Execute the edit-config RPC
    try:
        reply = session.edit_config(target="running", config=config_xml_schema)
        #reply = session.edit_config(target="running", config=config_xml_schema, default_operation="replace")
        logger.info(reply)
    except Exception as e:
        logger.exception(f"Error for establishing the Set Config operation: {e}")

    session.close_session()