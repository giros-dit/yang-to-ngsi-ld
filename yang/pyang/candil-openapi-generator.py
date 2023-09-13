'''
pyang plugin -- CANDIL OpenAPI Generator.

Given one or several YANG modules, it dynamically generates their OpenAPI specification.

Version: 0.0.1.

Author: Networking and Virtualization Research Group (GIROS DIT-UPM) -- https://dit.upm.es/~giros
'''

import optparse
import pdb
import re
import sys
import yaml

from pyang import plugin
from pyang import statements

def pyang_plugin_init():
    plugin.register_plugin(CandilOpenApiGeneratorPlugin())

class CandilOpenApiGeneratorPlugin(plugin.PyangPlugin):
    def __init__(self):
        plugin.PyangPlugin.__init__(self, 'candil-openapi-generator')

    def add_output_format(self, fmts):
        self.multiple_modules = True
        fmts['candil-openapi-generator'] = self
    
    def add_opts(self, optparser):
        optlist = [
            optparse.make_option('--candil-oapig-help', dest='print_oapig_help', action='store_true', help='Prints help and usage.')
        ]
        g = optparser.add_option_group('CANDIL OpenAPI Generator - Execution options')
        g.add_options(optlist)

    def setup_ctx(self, ctx):
        if ctx.opts.print_oapig_help:
            print_oapig_help()
            sys.exit(0)

    def setup_fmt(self, ctx):
        ctx.implicit_errors = False

    def emit(self, ctx, modules, fd):
        generate_openapi_spec(ctx, modules, fd)

def print_oapig_help():
    '''
    Prints plugin's help information.
    '''
    print('''
Pyang plugin - CANDIL OpenAPI Generator (candil-openapi-generator).
Given one or several YANG modules, this plugin generates their OpenAPI specification in YAML format.

Usage:
pyang -f candil-openapi-generator <base_module.yang> [augmenting_module_1.yang] [augmenting_module_2.yang] ... [augmenting_module_N.yang] > <output_file.yaml>
    ''')
          
def generate_openapi_spec(ctx, modules, fd):
    '''
    Processes YANG modules and generates the corresponding OpenAPI specification in YAML format.
    '''

    # Use PDB to debug the code with pdb.set_trace().

    # CONSTANTS:

    INDENTATION_LEVEL = '    '

    # AUXILIARY FUNCTIONS:
    
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

    # Generate OpenAPI specification:
    for module in modules:
        elements = module.i_children
        if (elements is not None):
            for element in elements:
                if (element is not None) and (element.keyword in statements.data_definition_keywords):
                    # Function call TBD. Do nothing for now.
                    print(None)
