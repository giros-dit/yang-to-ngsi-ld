"""
pyang plugin -- NGSI-LD Context generator.

Generates the NGSI-LD Contexts associated with a YANG module file following the defined guidelines and conventions.
It outputs the results into an individual .jsonld file for every NGSI-LD Entity.

Version: 0.2.0.

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
    plugin.register_plugin(NgsiLdContextPlugin())

class NgsiLdContextPlugin(plugin.PyangPlugin):
    def __init__(self):
        plugin.PyangPlugin.__init__(self, 'ngsi-ld-context')

    def add_output_format(self, fmts):
        self.multiple_modules = True
        fmts['ngsi-ld-context'] = self

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
        emit_ngsi_ld_context(ctx, modules, fd)

def print_help():
    """
    Prints plugin's help information.
    """
    print("""
            TO-DO
        """)
          
def emit_ngsi_ld_context(ctx, modules, fd):
    """
    Processes a YANG module and generates the corresponding NGSI-LD context in JSON format.
    It outputs the result in the command line.
    Use PDB to debug the code with pdb.set_trace().
    """

    # CONSTANTS:

    NGSI_LD_CORE_CONTEXT_URI = "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.6.jsonld/"
    IS_PART_OF_URI = "https://smartdatamodels.org/isPartOf"

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
        if (element.keyword in ['leaf-list', 'leaf']):
            result = True
        return result
                
    def generate_context(element, module_name, module_urn, xpath, ngsi_ld_context):
        """
        Auxiliary function.
        Recursively generates the NGSI-LD context given a YANG data node (element) and the X-Path.
        """
        if (is_enclosing_container(element) == True) and (is_deprecated(element) == False):
            subelements = element.i_children
            if (subelements is not None):
                for subelement in subelements:
                    if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                        generate_context(subelement, module_name, module_urn, xpath + ':' + element.arg, None)
        elif (is_entity(element) == True) and (is_deprecated(element) == False):
                json_ld = {}
                json_ld["@context"] = []
                ngsi_ld_context = {}
                ngsi_ld_context[module_name] = module_urn + '/'
                ngsi_ld_context[to_camel_case(str(element.keyword), str(element.arg))] = xpath + '/' + str(element.arg)
                subelements = element.i_children
                if (subelements is not None):
                    for subelement in subelements:
                        if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                            generate_context(subelement, module_name, module_urn, xpath + ":" + element.arg, ngsi_ld_context)
                json_ld["@context"].append(ngsi_ld_context)
                json_ld["@context"].append(NGSI_LD_CORE_CONTEXT_URI)
                json_ld["@context"].append(IS_PART_OF_URI)
                # Help: https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output 
                filename = "jsonld/" + module_name + "_" + to_camel_case(str(element.keyword), str(element.arg)) + ".jsonld"
                os.makedirs(os.path.dirname(filename), exist_ok=True)
                file = open(filename, "w")
                file.write(json.dumps(json_ld, indent=4) + '\n')
                fd.write("NGSI-LD Context written to " + file.name + "\n")
                # fd.write(json.dumps(json_ld, indent=4) + '\n')
        elif (is_property(element) == True) and (is_deprecated(element) == False):
            ngsi_ld_context[to_camel_case(str(element.keyword), str(element.arg))] = xpath + '/' + str(element.arg)   
    
    # Generate NGSI-LD Context:
    for module in modules:
        module_name = str(module.arg)
        module_keyword = str(module.keyword)
        module_urn = str(module.search_one('namespace').arg)
        xpath = module_urn.split(":")[-1]
        elements = module.i_children
        if (elements is not None):
            for element in elements:
                if (element is not None) and (element.keyword in statements.data_definition_keywords):
                    generate_context(element, module_name, module_urn, xpath, None)
