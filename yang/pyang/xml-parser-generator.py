"""
pyang plugin -- XML Parser Generator.

Given one or several YANG modules, it dynamically generates the code of an XML parser
(in a ".py" Python script file) that is able to read network telemetry from a device
in XML format and is also capable of creating instances of Pydantic classes from the
NGSI-LD-backed OpenAPI generation.

Version: 0.0.5.

Author: Networking and Virtualization Research Group (GIROS DIT-UPM) -- https://dit.upm.es/~giros
"""

import optparse
import sys
import re
import pdb
import json
import os

from pyang import plugin
from pyang import statements
from pyang import util

def pyang_plugin_init():
    plugin.register_plugin(XmlParserGeneratorPlugin())

class XmlParserGeneratorPlugin(plugin.PyangPlugin):
    def __init__(self):
        plugin.PyangPlugin.__init__(self, 'xml-parser-generator')

    def add_output_format(self, fmts):
        self.multiple_modules = True
        fmts['xml-parser-generator'] = self

    def setup_ctx(self, ctx):
        """
        Setups plugin's context.
        Do nothing for now.
        Code from tree plugin:
        if ctx.opts.help:
            print_help()
            sys.exit(0)
        """

    def setup_fmt(self, ctx):
        ctx.implicit_errors = False

    def emit(self, ctx, modules, fd):
        emit_python_code(ctx, modules, fd)

def print_help():
    """
    Prints plugin's help information.
    """
    print("""
            TO-DO
        """)
          
def emit_python_code(ctx, modules, fd):
    """
    Processes YANG modules and generates the corresponding XML parser code for data modeled with those YANG modules.
    """

    # Use PDB to debug the code with pdb.set_trace().

    # CONSTANTS:

    # NOTE: From ietf-yang-types@2023-01-23.yang.
    # If there are several conversion steps, the value is always the final type.
    IETF_YANG_TYPES_TO_PRIMITIVE_YANG_TYPES = {
        "yang:counter32": "uint32",
        "yang:zero-based-counter32": "uint32",
        "yang:counter64": "uint64",
        "yang:zero-based-counter64": "uint64",
        "yang:gauge32": "uint32",
        "yang:gauge64": "uint64",
        "yang:object-identifier": "string",
        "yang:object-identifier-128": "string",
        "yang:date-and-time": "string",
        "yang:date-with-zone-offset": "string",
        "yang:date-no-zone": "string",
        "yang:time-with-zone-offset": "string",
        "yang:time-no-zone": "string",
        "yang:hours32": "int32",
        "yang:minutes32": "int32",
        "yang:seconds32": "int32",
        "yang:centiseconds32": "int32",
        "yang:miliseconds32": "int32",
        "yang:microseconds32": "int32",
        "yang:microseconds64": "int64",
        "yang:nanoseconds32": "int32",
        "yang:nanoseconds64": "int64",
        "yang:timeticks": "uint32",
        "yang:timestamp": "uint32",
        "yang:phys-address": "string",
        "yang:mac-address": "string",
        "yang:xpath1.0": "string",
        "yang:hex-string": "string",
        "yang:uuid": "string",
        "yang:dotted-quad": "string",
        "yang:language-tag": "string",
        "yang:yang-identifier": "string"
    }

    # NOTE: NGSI-LD types are Python "types" (given this particular implementation).
    PRIMITIVE_YANG_TYPES_TO_NGSI_LD_TYPES = {
        "int8": "Integer",
        "int16": "Integer",
        "int32": "Integer",
        "int64": "Integer",
        "uint8": "Integer",
        "uint16": "Integer",
        "uint32": "Integer",
        "uint64": "Integer",
        "decimal64": "Integer",
        "string": "String",
        "boolean": "Boolean",
        "enum": "String",
        "enumeration": "String",
        "bit": "List(String)",
        "binary": "String",
        "empty": "String"
    }

    INDENTATION_LEVEL = '    '

    BASE_IMPORT_STATEMENTS = [
        "import sys",
        "import xml.etree.ElementTree as et",
        "import logging",
        "import logging.config",
        "import yaml",
        "import os",
        "import time",
        "import re",
        "import subprocess",
        "import pdb",
        "import ngsi_ld_client",
        "from fastapi import FastAPI, Request, status",
        "from ngsi_ld_client.api_client import ApiClient as NGSILDClient",
        "from ngsi_ld_client.configuration import Configuration as NGSILDConfiguration",
        "from ngsi_ld_client.exceptions import ApiException"
    ]

    XML_PARSER_BASE_OPERATIONS = [
        "xml_file = sys.argv[1]",    
        "tree = et.parse(xml_file)",
        "root = tree.getroot()"
    ]

    # AUXILIARY FUNCTIONS: 

    def to_camel_case(element_keyword: str, element_arg: str) -> str:
        """
        Auxiliary function.
        Returns the CamelCase representation of element_name according to the YANG to NGSI-LD translation conventions.
        """
        if (element_keyword is None) or (element_arg is None):
            return element_arg
        else:
            if (element_keyword == 'module'):
                return element_arg
            if (element_keyword == 'container') or (element_keyword == 'list'):
                return element_arg.capitalize()
            if (element_keyword == 'leaf') or (element_keyword == 'leaf-list'):
                return re.sub(r"(-)(\w)", lambda m: m.group(2).upper(), element_arg)
    
    def yang_to_ngsi_ld_types_conversion(element_type: str) -> str:
        '''
        Auxiliary function.
        Returns the NGSI-LD type (in Python implementation) given the YANG type of an element/node in a YANG module.
        '''
        if (element_type in IETF_YANG_TYPES_TO_PRIMITIVE_YANG_TYPES):
            primitive_yang_type = IETF_YANG_TYPES_TO_PRIMITIVE_YANG_TYPES[element_type]
            return PRIMITIVE_YANG_TYPES_TO_NGSI_LD_TYPES[primitive_yang_type]
        else:
            return PRIMITIVE_YANG_TYPES_TO_NGSI_LD_TYPES[element_type]
    
    def element_text_type_formatting(ngsi_ld_type: str, element_text: str) -> str:
        '''
        Auxiliary function.
        Returns a String with the Python code that implements the correct formatting for the value/text of an element in
        an XML file given the NGSI-LD type of that particular element.
        '''
        if (ngsi_ld_type == "String"):
            return element_text
        elif (ngsi_ld_type == "Integer"):
            return 'int(' + element_text + ')'
        elif (ngsi_ld_type == "Boolean"):
            return element_text + '.capitalize()'
    
    def is_enclosing_container(element):
        """
        Auxiliary function.
        Checks if an element is an "enclosing container":
        - It is a container AND
        - It only has one child AND
        - This child is a list.
        """
        result = False
        if (element.keyword == 'container') and (len(element.i_children) == 1) and (element.i_children[0].keyword == 'list'):
            result = True
        return result

    def is_deprecated(element):
        """
        Auxiliary function.
        Checks if an element is deprecated.
        """
        result = False
        status = element.search_one('status')
        if (status is not None) and (status.arg == 'deprecated'):
            result = True
        return result
    
    def is_entity(element):
        """
        Auxiliary function.
        Checks if an element matches the YANG to NGSI-LD translation convention for an Entity.
        """
        result = False
        if (element.keyword in ['container', 'list']):
            result = True
        return result
    
    def is_property(element):
        """
        Auxiliary function.
        Checks if an element matches the YANG to NGSI-LD translation convention for a Property.
        """
        result = False
        if (element.keyword in ['leaf-list', 'leaf']) and ('ref' not in str(element.search_one('type'))):
            result = True
        return result
    
    def is_relationship(element):
        """
        Auxiliary function.
        Checks if an element matches the YANG to NGSI-LD translation convention for a Relationship.
        """
        result = False
        if (element.keyword in ['leaf-list', 'leaf']) and ('ref' in str(element.search_one('type'))):
            result = True
        return result
    
    def generate_entity_import_statements_and_dict_buffers(element):
        '''
        Auxiliary function.
        Recursively generates import statements and dictionary buffer lists
        for identified NGSI-LD Entities within the YANG module.
        A dictionary buffer stores a valid representation of a NGSI-LD Entity with 
        its properties and relationships.
        Dictionary buffer lists store dictionary buffers of different NGSI-LD Entities
        of the same type.
        '''
        camelized_element_arg = to_camel_case(str(element.keyword), str(element.arg))
        if (is_enclosing_container(element) == True) and (is_deprecated(element) == False):
            subelements = element.i_children
            if (subelements is not None):
                for subelement in subelements:
                    if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                        generate_entity_import_statements_and_dict_buffers(subelement)
        elif (is_entity(element) == True) and (is_deprecated(element) == False):
            fd.write('\n' + 'from ngsi_ld_models.models.' + str(element.arg) + " import " + camelized_element_arg)
            fd.write('\n' + str(element.arg) + '_dict_buffers = []')
            fd.write('\n')
            subelements = element.i_children
            if (subelements is not None):
                for subelement in subelements:
                    if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                        generate_entity_import_statements_and_dict_buffers(subelement)

    def generate_parser_code(element, module_namespace, parent_element_arg, depth_level):
        """
        Auxiliary function.
        Recursively generates the XML parser code.
        """
        camelized_element_arg = to_camel_case(str(element.keyword), str(element.arg))
        if element.i_module.i_modulename == module.i_modulename:
            name = str(element.arg)
        else:
            name = element.i_module.i_prefix + ':' + str(element.arg)
        if (is_enclosing_container(element) == True) and (is_deprecated(element) == False):
            subelements = element.i_children
            if (subelements is not None):
                for subelement in subelements:
                    if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                        generate_parser_code(subelement, module_namespace, None, 0)
        elif (is_entity(element) == True) and (is_deprecated(element) == False):
            if (parent_element_arg is None): # 1st level Entity.
                fd.write('\n' + 'for ' + str(element.arg) + ' in root.findall(\".//{' + module_namespace + '}' + str(element.arg) + '\"):')
                depth_level += 1
                fd.write('\n' + INDENTATION_LEVEL * depth_level + str(element.arg) + '_dict_buffer = {}')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + str(element.arg) + '_dict_buffer[\"id\"] = \"urn:ngsi-ld:' + camelized_element_arg + ':\"')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + str(element.arg) + '_dict_buffer[\"type\"] = \"' + camelized_element_arg + '\"')
            else: # 2nd level Entity onwards.
                fd.write('\n' + INDENTATION_LEVEL * depth_level + 'for ' + str(element.arg) + ' in ' + str(parent_element_arg) + '.findall(\".//{' + module_namespace + '}' + str(element.arg) + '\"):')
                depth_level += 1
                fd.write('\n' + INDENTATION_LEVEL * depth_level + str(element.arg) + '_dict_buffer = {}')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + str(element.arg) + '_dict_buffer[\"id\"] = \"urn:ngsi-ld:' + camelized_element_arg + ':\" + ' + str(parent_element_arg) + '_dict_buffer[\"name\"][\"value\"]')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + str(element.arg) + '_dict_buffer[\"type\"] = \"' + camelized_element_arg + '\"')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + str(element.arg) + '_dict_buffer[\"isPartOf\"] = {}')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + str(element.arg) + '_dict_buffer[\"isPartOf\"][\"type\"] = \"Relationship\"')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + str(element.arg) + '_dict_buffer[\"isPartOf\"][\"object\"] = \"urn:ngsi-ld:' + str(parent_element_arg).capitalize() + ':\" + ' + str(parent_element_arg) + '_dict_buffer[\"name\"][\"value\"]')
            subelements = element.i_children
            if (subelements is not None):
                for subelement in subelements:
                    if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                        generate_parser_code(subelement, module_namespace, element.arg, depth_level)
            fd.write('\n' + INDENTATION_LEVEL * depth_level + str(element.arg) + '_dict_buffers.append(' + str(element.arg) + '_dict_buffer)')
        elif (is_property(element) == True) and (is_deprecated(element) == False):
            fd.write('\n' + INDENTATION_LEVEL * depth_level + camelized_element_arg + " " + "=" + " " + str(parent_element_arg) + ".find(\".//{"+module_namespace+"}"+str(element.arg)+"\")")
            fd.write('\n' + INDENTATION_LEVEL * depth_level + 'if ' + camelized_element_arg + ' is not None:')
            ngsi_ld_type = yang_to_ngsi_ld_types_conversion(str(element.search_one('type')).replace("type ", ""))
            text_format = element_text_type_formatting(ngsi_ld_type, 'element_text')
            fd.write('\n' + INDENTATION_LEVEL * depth_level + INDENTATION_LEVEL + 'element_text = ' + camelized_element_arg + '.text')
            if (str(element.arg) == 'name'):
                fd.write('\n' + INDENTATION_LEVEL * depth_level + INDENTATION_LEVEL + str(parent_element_arg) + '_dict_buffer[\"id\"] = ' + str(parent_element_arg) + '_dict_buffer[\"id\"] + ' + text_format)
            fd.write('\n' + INDENTATION_LEVEL * depth_level + INDENTATION_LEVEL + str(parent_element_arg) + '_dict_buffer[\"' + camelized_element_arg + '\"] = {}')
            fd.write('\n' + INDENTATION_LEVEL * depth_level + INDENTATION_LEVEL + str(parent_element_arg) + '_dict_buffer[\"' + camelized_element_arg + '\"][\"type\"] = \"Property\"')
            fd.write('\n' + INDENTATION_LEVEL * depth_level + INDENTATION_LEVEL + str(parent_element_arg) + '_dict_buffer[\"' + camelized_element_arg + '\"][\"value\"] = ' + text_format)
        elif (is_relationship(element) == True) and (is_deprecated(element) == False):
            if (str(element.arg) != 'type'):
                fd.write('\n' + INDENTATION_LEVEL * depth_level + camelized_element_arg + " " + "=" + " " + str(parent_element_arg) + ".find(\".//{"+module_namespace+"}"+str(element.arg)+"\")")
                fd.write('\n' + INDENTATION_LEVEL * depth_level + 'if ' + camelized_element_arg + ' is not None:')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + INDENTATION_LEVEL + 'element_text = ' + camelized_element_arg + '.text')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + INDENTATION_LEVEL + str(parent_element_arg) + '_dict_buffer[\"' + camelized_element_arg + '\"] = {}')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + INDENTATION_LEVEL + str(parent_element_arg) + '_dict_buffer[\"' + camelized_element_arg + '\"][\"type\"] = \"Relationship\"')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + INDENTATION_LEVEL + str(parent_element_arg) + '_dict_buffer[\"' + camelized_element_arg + '\"][\"object\"] = \"urn:ngsi-ld:' + str(parent_element_arg).capitalize() + ':\" + element_text')
    
    # Generate XML parser Python code:
    for import_statement in BASE_IMPORT_STATEMENTS:
        fd.write(import_statement)
        fd.write("\n")

    fd.write("\n")

    for line in XML_PARSER_BASE_OPERATIONS:
        fd.write(line)
        fd.write("\n")

    for module in modules:
        module_namespace = str(module.search_one('namespace').arg)
        elements = module.i_children
        if (elements is not None):
            for element in elements:
                if (element is not None) and (element.keyword in statements.data_definition_keywords):
                    generate_entity_import_statements_and_dict_buffers(element)
                    generate_parser_code(element, module_namespace, None, 0)
    
    fd.write("\n")
