'''
XML Parser based on the ElementTree XML and lxml libraries.
Reference documentation:
* ElementTree: https://docs.python.org/3/library/xml.etree.elementtree.html
* lxml: https://lxml.de/
'''

import xml.etree.ElementTree as et
import subprocess
import pdb

ns = {}

tree = et.parse('sample-ietf-interfaces.xml')

root = tree.getroot()

def print_data_recursively(element):
    print(element.tag.split("}")[1] + " " + element.text)
    for child in element:
        print_data_recursively(child)

for child in root:
    print_data_recursively(child)

# pdb.set_trace()
