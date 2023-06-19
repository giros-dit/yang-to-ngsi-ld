'''
XML Parser based on the ElementTree XML library.
Reference documentation: https://docs.python.org/3/library/xml.etree.elementtree.html
'''

import xml.etree.ElementTree as et
import re
import subprocess
import pdb

tree = et.parse('../xml/sample-ietf-interfaces-reduced1.xml')

root = tree.getroot()

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

for child in root:
    print_data_recursively(child)

# pdb.set_trace()
