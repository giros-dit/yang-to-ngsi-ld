'''
pyang plugin -- CANDIL NGSI-LD Context Generator.

Generates the NGSI-LD context files associated with a YANG module file following the defined guidelines and conventions.
The results are written to individual .jsonld files: one for every NGSI-LD Entity.

Version: 0.3.3.

Author: Networking and Virtualization Research Group (GIROS DIT-UPM) -- https://dit.upm.es/~giros
'''

import json
import os
import optparse
import pdb
import re
import sys

from pyang import plugin
from pyang import statements

def pyang_plugin_init():
    plugin.register_plugin(CandilNgsiLdContextGeneratorPlugin())

class CandilNgsiLdContextGeneratorPlugin(plugin.PyangPlugin):
    def __init__(self):
        plugin.PyangPlugin.__init__(self, 'candil-ngsi-ld-context-generator')

    def add_output_format(self, fmts):
        self.multiple_modules = True
        fmts['candil-ngsi-ld-context-generator'] = self
    
    def add_opts(self, optparser):
        optlist = [
            optparse.make_option('--candil-ngsi-ld-context-generator-help', dest='print_ngsild_ctxg_help', action='store_true', help='Prints help and usage.')
        ]
        g = optparser.add_option_group('CANDIL NGSI-LD Context Generator - Execution options')
        g.add_options(optlist)

    def setup_ctx(self, ctx):
        if ctx.opts.print_ngsild_ctxg_help:
            print_ngsild_ctxg_help()
            sys.exit(0)

    def setup_fmt(self, ctx):
        ctx.implicit_errors = False

    def emit(self, ctx, modules, fd):
        generate_ngsi_ld_context(ctx, modules, fd)

def print_ngsild_ctxg_help():
    '''
    Prints plugin's help and usage information.
    '''
    print('''
Pyang plugin - CANDIL NGSI-LD Context Generator (candil-ngsi-ld-context-generator).
This plugin generates the NGSI-LD Context files associated with one or several YANG modules
(for augments) following the defined translation guidelines and conventions.
The resulting files are written in a specific subdirectory. Each identified NGSI-LD Entity
has its independent context file.

Usage:
pyang -f candil-ngsi-ld-context-generator <base_module.yang> [augmenting_module_1.yang] [augmenting_module_2.yang] ... [augmenting_module_N.yang]
    ''')
          
def generate_ngsi_ld_context(ctx, modules, fd):
    '''
    Processes a YANG module and generates the corresponding NGSI-LD context files in JSON-LD format.
    '''

    # Use PDB to debug the code with pdb.set_trace().

    # AUXILIARY FUNCTIONS: 

    def to_camelcase(keyword: str, element_name: str) -> str:
        '''
        Auxiliary function.
        Returns the CamelCase representation of element_name according to the YANG to NGSI-LD translation conventions.
        '''
        if (keyword is None) or (element_name is None):
            return element_name
        else:
            if (keyword == 'module'):
                return element_name
            if (keyword == 'container') or (keyword == 'list'):
                return re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), element_name.capitalize())
            if (keyword == 'leaf') or (keyword == 'leaf-list'):
                return re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), element_name)
    
    def is_enclosing_container(element):
        '''
        Auxiliary function.
        Checks if an element is an "enclosing container":
        - It is a container AND
        - It has one child or more AND
        - Each of one of them is either a container or a list.
        '''
        result = False
        individual_results = 0
        if (element.keyword != 'container'):
            return False
        else:
            if (len(element.i_children) >= 1):
                for subelement in element.i_children:
                    if (subelement.keyword in ['container', 'list']):
                        individual_results += 1
            if (len(element.i_children) == individual_results):
                result = True
            return result
    
    def is_deprecated(element):
        '''
        Auxiliary function.
        Checks if an element is deprecated.
        '''
        result = False
        status = element.search_one('status')
        if (status is not None) and (status.arg == 'deprecated'):
            result = True
        return result

    def is_entity(element):
        '''
        Auxiliary function.
        Checks if an element matches the YANG to NGSI-LD translation convention for an Entity.
        '''
        result = False
        if (element.keyword in ['container', 'list']):
            result = True
        return result
    
    def is_property(element):
        '''
        Auxiliary function.
        Checks if an element matches the YANG to NGSI-LD translation convention for a Property.
        '''
        result = False
        if (element.keyword in ['leaf-list', 'leaf']) and ('ref' not in str(element.search_one('type'))):
            result = True
        return result
    
    def is_relationship(element):
        '''
        Auxiliary function.
        Checks if an element matches the YANG to NGSI-LD translation convention for a Relationship.
        '''
        result = False
        if (element.keyword in ['leaf-list', 'leaf']) and ('ref' in str(element.search_one('type'))):
            result = True
        return result
                
    def generate_context(element, module_name: str, module_urn: str, xpath: str, camelcase_entity_path: str, ngsi_ld_context: dict):
        '''
        Auxiliary function.
        Recursively generates the NGSI-LD context(s) given a YANG data node (element) and the X-Path.
        '''
        if element.i_module.i_modulename == module.i_modulename:
            name = str(element.arg)
        else:
            name = element.i_module.i_prefix + ':' + str(element.arg)
        if (is_enclosing_container(element) == True) and (is_deprecated(element) == False):
            subelements = element.i_children
            if (subelements is not None):
                for subelement in subelements:
                    if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                        generate_context(subelement, module_name, module_urn, xpath + name + '/', None, None)
        elif (is_entity(element) == True) and (is_deprecated(element) == False):
                current_camelcase_path = ''
                if (camelcase_entity_path is None):
                    current_camelcase_path = to_camelcase(str(element.keyword), str(element.arg))
                else:
                    current_camelcase_path = camelcase_entity_path + to_camelcase(str(element.keyword), str(element.arg))
                json_ld = {}
                ngsi_ld_context = {}
                ngsi_ld_context[module_name] = module_urn + '/'
                ngsi_ld_context[current_camelcase_path] = xpath + name
                subelements = element.i_children
                if (subelements is not None):
                    for subelement in subelements:
                        if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                            generate_context(subelement, module_name, module_urn, xpath + name + '/', current_camelcase_path, ngsi_ld_context)
                json_ld["@context"] = ngsi_ld_context
                # Help: https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output
                filename = 'ngsi-ld-context/' + xpath.replace('/', '_').replace(':', '_') + name.replace(':', '_') + '.jsonld'
                os.makedirs(os.path.dirname(filename), exist_ok=True)
                file = open(filename, 'w')
                file.write(json.dumps(json_ld, indent=4) + '\n')
                fd.write('NGSI-LD Context written to ' + file.name + '\n')
        elif (is_property(element) == True) and (is_deprecated(element) == False):
            ngsi_ld_context[to_camelcase(str(element.keyword), str(element.arg))] = xpath + name
        elif (is_relationship(element) == True) and (is_deprecated(element) == False):
            ngsi_ld_context[to_camelcase(str(element.keyword), str(element.arg))] = xpath + name
    
    # Generate NGSI-LD Context:
    for module in modules:
        module_name = str(module.arg)
        module_urn = str(module.search_one('namespace').arg)
        xpath = module_name + ':'
        elements = module.i_children
        if (elements is not None):
            for element in elements:
                if (element is not None) and (element.keyword in statements.data_definition_keywords):
                    generate_context(element, module_name, module_urn, xpath, None, None)
