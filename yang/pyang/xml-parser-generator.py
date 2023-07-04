"""
pyang plugin -- XML Parser Generator.

Given one or several YANG modules, it dynamically generates a XML parser (in a ".py" Python script file) that 
is able to read network telemetry from a device in XML format and is also capable of creating instances of 
Pydantic classes from the NGSI-LD-backed OpenAPI generation.

Version: 0.0.3.

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

    def to_camel_case(keyword: str, element_name: str) -> str:
        """
        Auxiliary function.
        Returns the CamelCase representation of element_name according to the YANG to NGSI-LD translation conventions.
        """
        if (keyword is None) or (element_name is None):
            return element_name
        else:
            if (keyword == 'module'):
                return element_name
            if (keyword == 'container') or (keyword == 'list'):
                return element_name.capitalize()
            if (keyword == 'leaf') or (keyword == 'leaf-list'):
                return re.sub(r"(-)(\w)", lambda m: m.group(2).upper(), element_name)
    
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
                
    def generate_xml_parser(element, module_namespace, parent_element_arg, is_parent_an_entity: bool):
        """
        Auxiliary function.
        Recursively generates the XML parser code.
        """

        if element.i_module.i_modulename == module.i_modulename:
            name = str(element.arg)
        else:
            name = element.i_module.i_prefix + ':' + str(element.arg)
        if (is_enclosing_container(element) == True) and (is_deprecated(element) == False):
            subelements = element.i_children
            if (subelements is not None):
                for subelement in subelements:
                    if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                        generate_xml_parser(subelement, module_namespace, None, None)
        elif (is_entity(element) == True) and (is_deprecated(element) == False):
            fd.write('\n' + 'from ngsi_ld_models.models.' + str(element.arg) + " import " + str(element.arg).capitalize())
            fd.write('\n' + str(element.arg) + '_dict_buffers = []')
            fd.write('\n' + 'for ' + str(element.arg) + ' in root.findall(\".//{' + module_namespace + '}' + str(element.arg) + '\"):')
            subelements = element.i_children
            if (subelements is not None):
                for subelement in subelements:
                    if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                        generate_xml_parser(subelement, module_namespace, element.arg, True)
        elif (is_property(element) == True) and (is_deprecated(element) == False):
            element_keyword = str(element.keyword)
            element_arg = str(element.arg)
            camelized_keyword = to_camel_case(element_keyword, element_arg)
            fd.write('\n' + INDENTATION_LEVEL + camelized_keyword + " " + "=" + " " + str(parent_element_arg) + ".find(\".//{"+module_namespace+"}"+str(element.arg)+"\")")
            fd.write('\n' + INDENTATION_LEVEL + 'if ' + camelized_keyword + ' is not None: print(' + to_camel_case(element_keyword, element_arg) + '.text)')
            
            # Keep old code just in case
            #fd.write('\n' + to_camel_case(element_keyword, element_arg) + " " + "=" + " " + "root.findall(\".//{"+module_namespace+"}"+str(element.arg)+"\")")
            #fd.write('\n' + 'for entry in ' + to_camel_case(element_keyword, element_arg) + ':')
            #fd.write('\n' + INDENTATION_LEVEL + 'print(entry.text)')
        elif (is_relationship(element) == True) and (is_deprecated(element) == False):
            element_keyword = str(element.keyword)
            element_arg = str(element.arg)
            camelized_keyword = to_camel_case(element_keyword, element_arg)
            fd.write('\n' + INDENTATION_LEVEL + to_camel_case(element_keyword, element_arg) + " " + "=" + " " + str(parent_element_arg) + ".find(\".//{"+module_namespace+"}"+str(element.arg)+"\")")
            fd.write('\n' + INDENTATION_LEVEL + 'if ' + camelized_keyword + ' is not None: print(' + to_camel_case(element_keyword, element_arg) + '.text)')
            
            # Keep old code just in case
            #fd.write('\n' + to_camel_case(element_keyword, element_arg) + " " + "=" + " " + "root.findall(\".//{"+module_namespace+"}"+str(element.arg)+"\")")
            #fd.write('\n' + 'for entry in ' + to_camel_case(element_keyword, element_arg) + ':')
            #fd.write('\n' + INDENTATION_LEVEL + 'print(entry.text)')
    
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
                    generate_xml_parser(element, module_namespace, None, None)
