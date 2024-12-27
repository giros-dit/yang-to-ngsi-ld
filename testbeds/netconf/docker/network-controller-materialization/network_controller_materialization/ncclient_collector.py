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
Main function to convert a Pydantic instance to XML schema from NETCONF for ncclient get-config operations
'''
def generate_netconf_xml_config(xpath: str, all_context_data: Optional[dict]) -> str:

    root = None
    current_element = None

    processed_all_context_data = {}
    for key, value in all_context_data.items():
        if isinstance(value, str):  
            if ":" in value and not value.startswith(("urn:", "http:", "https:")):
                processed_all_context_data[key] = "/" + value.split(":", 1)[1]
            else:
                processed_all_context_data[key] = value
        elif isinstance(value, list): 
            processed_all_context_data[key] = [
                ("/" + v.split(":", 1)[1] if ":" in v and not v.startswith(("urn:", "http:", "https:")) else v) 
                if isinstance(v, str) else v 
                for v in value
            ]
        else: 
            processed_all_context_data[key] = value

    is_match = False
    match_key = None
    if "[" in xpath and "]" in xpath:
        xpath_filter = re.sub(r"\[.*?\]", "", xpath)
    else:
        xpath_filter = xpath
    for key, value in processed_all_context_data.items():
        if isinstance(value, str):
            if value == xpath_filter:
                is_match = True
                match_key = key
                break
        elif isinstance(value, list): 
            for v in value:
                if v == xpath_filter:
                    is_match = True
                    match_key = key
                    break
    
    if is_match: #if xpath in processed_all_context_data.values():
        search_original_context_data = all_context_data[match_key]
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

        # Apply YANG module namespaces
        #et.register_namespace('', str("urn:ietf:params:xml:ns:yang:"+ns)) 
        #root.set("xmlns", str("urn:ietf:params:xml:ns:yang:"+ns))
    
    # We return the XML as a string
    return et.tostring(root, encoding="unicode", method='xml')

'''
Function for triggering NETCONF RPC Get and Get-Config operations with needed parameters.
'''
def get_operation(host: str, port: str, username: str, password: str, family: str, xpath: str, option: str, all_context_data: Optional[dict] = None, hostKeyVerify: Optional[bool] = False):
    
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

    if option == "config" or option == "edit-config":
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

        interface_filter = generate_netconf_xml_config(xpath=xpath, all_context_data=all_context_data)
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
            logger.exception(f"Error for establishing the Get operation: {e}")
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
                logger.info("\nThe X-Path is incorrect or not supported by the network device " + host + ".")
                session.close_session()
                return
        except Exception as e:
            logger.exception(f"Error for establishing the Get Config operation: {e}")
            session.close_session()
            return

    session.close_session()

    producer = KafkaProducer(bootstrap_servers=['kafka:9092'])
    reply = str(reply.data_xml)
    root = et.fromstring(reply)

    # A new subelement is added to the NETCONF notification: operation.
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
    if option == "config" or option == "edit-config":
        operation.text = "get_config"
    else:   
        operation.text = "get"

    query_xml = et.tostring(root, encoding='unicode')
    logger.info(query_xml)
    producer.send('interfaces-state-subscriptions', value=query_xml.encode('utf-8'))
    logger.info("I have sent it to a Kafka topic named interfaces-state-subscriptions")
    logger.info("The eventTime element of the query reply is: " + eventTime.text)
    producer.flush()
    
'''
Function for triggering NETCONF RPC YANG-Push subscriptions with needed parameters.
DEPRECATED! The corresponding function is within the main.py program.
'''
def subscribe_operation(host: str, port: str, username: str, password: str, family: str, xpath: str, period: str):
    r = {
        "host": host,
        "port": port,
        "username": username,
        "password": password,
        "hostkey_verify": False,
        "device_params": {"name": family}
    }

    logger.info("Hello, this is the ncclient-collector for " + host + " for subscriptions...")

    session = manager.connect(**r)

    logger.info("I have successfully established a session with ID# " + session.session_id)

    xpath = xpath
    subscription = "period"
    period = period


    # When building the RPC request XML, use dampening-period for on-change notifications (when supported).
    # Otherwise, use period and specify an integer value for the time in centiseconds.

    rpc = """

        <establish-subscription xmlns="urn:ietf:params:xml:ns:yang:ietf-event-notifications"
        xmlns:yp="urn:ietf:params:xml:ns:yang:ietf-yang-push">
            <stream>yp:yang-push</stream>
            <yp:xpath-filter>{0}</yp:xpath-filter>
            <yp:{1}>{2}</yp:{1}>
        </establish-subscription>

    """.format(xpath, subscription, period)


    try:
        request = session.dispatch(to_ele(rpc))
        logger.info("I have subscribed myself to get periodic YANG-Push notifications for X-Path " + xpath + " of network device " + host)
        logger.info(request)
        data_element = et.fromstring(str(request)).find('.//{urn:ietf:params:xml:ns:netconf:base:1.0}data')
        if data_element is None or len(data_element) == 0:
            logger.info("\nThe X-Path is incorrect or not supported by the network device " + host + ".")
            session.close_session()
            return
    except Exception as e:
        logger.error(f"Error for establishing the subscription: {str(e)}")
        session.close_session()
        return
    
    producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

    while True:
        sub_data = session.take_notification()
        logger.info("\nI have received a notification!" + "\n")

        if (sub_data != None):
            notification_xml = str(sub_data.notification_xml)
            root = et.fromstring(notification_xml)
            # A new subelement is added to the NETCONF notification: fromDevice.
            # It is the name of the device that is sending the notification.
            # WARNING: This is not defined in the specification.
            from_device = et.SubElement(root, 'fromDevice')
            from_device.text = host

            # A new subelement is added to the NETCONF notification: operation.
            # It is the name of the operation.
            # WARNING: This is not defined in the specification.
            operation = et.SubElement(root, 'operation')
            operation.text = "subscription"

            eventTime = root[0].text

            notification_xml = et.tostring(root, encoding='unicode')
            producer.send('interfaces-state-subscriptions', value=notification_xml.encode('utf-8'))
            logger.info("I have sent it to a Kafka topic named interfaces-state-subscriptions")
            logger.info("The eventTime element of the notification is: " + eventTime)
            producer.flush()

'''
Function to convert string from camelcase format (e.g., linkUpDownTrapEnable) to kebabcase format (e.g., link-up-down-trap-enable)
'''
def camel_to_kebab(camel_str):
    # Insert a space before any uppercase letter that is not at the start of the word
    kebab_str = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', camel_str)
    # Convert the whole string to lowercase
    return kebab_str.lower()

# Recursive function to generate XML from a Pydantic model
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
            elif isinstance(value, dict): # If it is a dictionary, we manage its keys and values
                if "value" in value:
                    # We check if the value is boolean and transform it to lowercase
                    if isinstance(value["value"], bool):
                        child.text = str(value["value"]).lower()
                    else:
                        child.text = str(value["value"])
                else:
                    # If it has no "value", we skip the element
                    continue
            elif isinstance(value, list):  # If it is a list, we iterate over the elements
                for item in value:
                    item_element = Element(camel_to_kebab(field[:-1]))  # We use the kebabcase format for labels
                    if isinstance(item, BaseModel):
                        pydantic_to_xml(item_element, item)
                    else:
                        item_element.text = str(item)
                    child.append(item_element)
            else:
               # If it is a primitive value, we convert it to text
                child.text = str(value) if value is not None else ""
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
        schema_tags = config

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
    return tostring(config, encoding="unicode")

'''
Function for triggering NETCONF RPC Set operation with needed parameters.
'''
def set_operation(host: str, port: str, username: str, password: str, family: str, instance: BaseModel, xpath: str, all_context_data: Optional[dict], hostKeyVerify: Optional[bool] = False):
    r = {
        "host": host,
        "port": port,
        "username": username,
        "password": password,
        "hostkey_verify": hostKeyVerify,
        "device_params": {"name": family}
    }

    config_xml_schema = generate_netconf_xml_set(xpath=xpath, instance=instance, all_context_data=all_context_data)

    logger.info("XML data schema: " + str(config_xml_schema))

    logger.info("Hello, this is the ncclient-collector for " + host + " for SET operations...")

    session = manager.connect(**r)
    logger.info("I have successfully established a session with ID# " + session.session_id)

    # Execute the edit-config RPC
    try:
        reply = session.edit_config(target="running", config=config_xml_schema)
        logger.info(reply)
    except Exception as e:
        logger.exception(f"Error for establishing the Set Config operation: {e}")

    session.close_session()