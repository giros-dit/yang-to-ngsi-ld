"""
pyang plugin -- NGSI-LD Context generator.

Generates the NGSI-LD context(s) associated with a YANG module file following the defined guidelines and conventions.
The results are written to individual .jsonld files: one for every NGSI-LD Entity.

Version: 0.2.6.

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
    Processes a YANG module and generates the corresponding NGSI-LD context(s) in JSON format.
    """

    # Use PDB to debug the code with pdb.set_trace().

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
                
    def generate_context(element, module_name, module_urn, xpath, ngsi_ld_context):
        """
        Auxiliary function.
        Recursively generates the NGSI-LD context(s) given a YANG data node (element) and the X-Path.
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
                        generate_context(subelement, module_name, module_urn, xpath + name + "/", None)
        elif (is_entity(element) == True) and (is_deprecated(element) == False):
                json_ld = {}
                json_ld["@context"] = []
                ngsi_ld_context = {}
                ngsi_ld_context[module_name] = module_urn + '/'
                ngsi_ld_context[to_camel_case(str(element.keyword), str(element.arg))] = xpath + name 
                subelements = element.i_children
                if (subelements is not None):
                    for subelement in subelements:
                        if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                            generate_context(subelement, module_name, module_urn, xpath + name + '/', ngsi_ld_context)
                ngsi_ld_context["isPartOf"] = IS_PART_OF_URI
                json_ld["@context"].append(ngsi_ld_context)
                json_ld["@context"].append(NGSI_LD_CORE_CONTEXT_URI)
                # Help: https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output
                filename = "ngsi-ld-context/" + xpath.replace("/", "_").replace(":", "_") + str(element.arg) + ".jsonld"
                os.makedirs(os.path.dirname(filename), exist_ok=True)
                file = open(filename, "w")
                file.write(json.dumps(json_ld, indent=4) + '\n')
                fd.write("NGSI-LD Context written to " + file.name + "\n")
        elif (is_property(element) == True) and (is_deprecated(element) == False):
            ngsi_ld_context[to_camel_case(str(element.keyword), str(element.arg))] = xpath + name
        elif (is_relationship(element) == True) and (is_deprecated(element) == False):
            ngsi_ld_context[to_camel_case(str(element.keyword), str(element.arg))] = xpath + name
    
    # Generate NGSI-LD Context:
    for module in modules:
        module_name = str(module.arg)
        module_urn = str(module.search_one('namespace').arg)
        xpath = module_name + ":"
        elements = module.i_children
        if (elements is not None):
            for element in elements:
                if (element is not None) and (element.keyword in statements.data_definition_keywords):
                    generate_context(element, module_name, module_urn, xpath, None)
