'''
pyang plugin -- CANDIL NGSI-LD Context Generator.

Generates the NGSI-LD context files associated with a YANG module file following the defined guidelines and conventions.
The results are written to individual .jsonld files: one for every NGSI-LD Entity.

Version: 0.3.8.

Author: Networking and Virtualization Research Group (GIROS DIT-UPM) -- https://dit.upm.es/~giros
'''

### HELP REFERENCES ###

### [1] https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output

### --- ###

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
            optparse.make_option('--candil-ngsi-ld-context-generator-help', dest='candil_ngsi_ld_context_generator_help', action='store_true', help='Prints help and usage.')
        ]
        g = optparser.add_option_group('CANDIL NGSI-LD Context Generator specific options')
        g.add_options(optlist)

    def setup_ctx(self, ctx):
        if ctx.opts.candil_ngsi_ld_context_generator_help:
            print_help()
            sys.exit(0)

    def setup_fmt(self, ctx):
        ctx.implicit_errors = False

    def emit(self, ctx, modules, fd):
        generate_ngsi_ld_context(ctx, modules, fd)

def print_help():
    '''
    Prints execution help.
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
    # pdb.set_trace()

    ### FUNCTION CONSTANTS ###

    IETF_YANG_URI = "http://ietf.yang.org#"
    YANG_IDENTITY_BROADER_URI = "http://www.w3.org/2004/02/skos/core#broader"
    NGSI_LD_CORE_CONTEXT_URI = "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.6.jsonld"

    ### --- ###

    ### AUXILIARY FUNCTIONS ###

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
            if (keyword == 'leaf') or (keyword == 'leaf-list') or (keyword == 'choice'):
                return re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), element_name)
    
    def is_enclosing_container(element) -> bool:
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
    
    def is_deprecated(element) -> bool:
        '''
        Auxiliary function.
        Checks if an element is deprecated.
        '''
        result = False
        status = element.search_one('status')
        if (status is not None) and (status.arg == 'deprecated'):
            result = True
        return result

    def is_entity(element) -> bool:
        '''
        Auxiliary function.
        Checks if an element matches the YANG to NGSI-LD translation convention for an Entity.
        '''
        result = False
        if (element.keyword in ['container', 'list']):
            result = True
        return result
    
    def is_choice(element) -> bool:
        '''
        Auxiliary function.
        Checks if an element is a YANG choice.
        '''
        result = False
        if (element.keyword == 'choice'):
            result = True
        return result
    
    def is_property(element) -> bool:
        '''
        Auxiliary function.
        Checks if an element matches the YANG to NGSI-LD translation convention for a Property.
        '''
        result = False
        if (element.keyword in ['leaf-list', 'leaf']):
            element_type = str(element.search_one('type')).replace('type ', '').split(':')[-1]
            if ('ref' not in element_type):
                result = True
        return result
    
    def is_relationship(element) -> bool:
        '''
        Auxiliary function.
        Checks if an element matches the YANG to NGSI-LD translation convention for a Relationship.
        '''
        result = False
        if (element.keyword in ['leaf-list', 'leaf']):
            element_type = str(element.search_one('type')).replace('type ', '').split(':')[-1]
            if ('ref' in element_type) and (element_type != 'identityref'):
                result = True
        return result

    def is_yang_identity(element) -> bool:
        '''
        Auxiliary function.
        Checks if an element matches the YANG to NGSI-LD translation convention for a YANG Identity.
        NOTE: YANG Identities are NGSI-LD Entities, but since they are either leaf-lists or leaves, they
        have no children, and therefore they are processed differently.
        '''
        result = False
        element_type = str(element.search_one('type')).replace('type ', '').split(':')[-1]
        if (element_type == 'identityref'):
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
            if element.parent.i_module.i_modulename != element.i_module.i_modulename:
                name = element.i_module.i_modulename + ':' + str(element.arg)
                #name = element.i_module.i_prefix + ':' + str(element.arg)
            else:
                 name = str(element.arg)
        
        ### ENCLOSING CONTAINER IDENTIFICATION ###
        if (is_enclosing_container(element) == True) and (is_deprecated(element) == False):
            subelements = element.i_children
            if (subelements is not None):
                for subelement in subelements:
                    if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                        generate_context(subelement, module_name, module_urn, xpath + name + '/', None, None)
        ### --- ###

        ### NGSI-LD ENTITY IDENTIFICATION ###
        elif (is_entity(element) == True) and (is_deprecated(element) == False):
            current_camelcase_path = ''
            if (camelcase_entity_path is None):
                current_camelcase_path = to_camelcase(str(element.keyword), str(element.arg))
            else:
                current_camelcase_path = camelcase_entity_path + to_camelcase(str(element.keyword), str(element.arg))
            json_ld = {}
            ngsi_ld_context = {}
            ngsi_ld_context[module_name] = module_urn + '/'
            if element.i_module.i_modulename != module.i_modulename:
                ngsi_ld_context[str(element.i_module.i_modulename)] = element.i_module.search_one('namespace').arg + '/'
            ngsi_ld_context[current_camelcase_path] = xpath + name
            subelements = element.i_children
            if (subelements is not None):
                for subelement in subelements:
                    if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                        generate_context(subelement, module_name, module_urn, xpath + name + '/', current_camelcase_path, ngsi_ld_context)
            json_ld["@context"] = ngsi_ld_context
            filename = 'ngsi-ld-context/' + xpath.replace('/', '_').replace(':', '_') + name.replace(':', '_') + '.jsonld'
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            file = open(filename, 'w')
            file.write(json.dumps(json_ld, indent=4) + '\n')
            fd.write('NGSI-LD Context written to ' + file.name + '\n')
        ### --- ###

        ### YANG CHOICE IDENTIFICATION: IT CONTAINS NGSI-LD PROPERTIES ###
        elif (is_choice(element) == True) and (is_deprecated(element) == False):
            current_camelcase_path = to_camelcase(str(element.keyword), str(element.arg))
            subelements = element.i_children
            #ngsi_ld_context[to_camelcase(str(element.keyword), str(element.arg))] = xpath + name
            if (subelements is not None):
                for subelement in subelements:
                    subelements = subelement.i_children
                    if (subelements is not None):
                        for subelement in subelements:
                            if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                                generate_context(subelement, module_name, module_urn, xpath + name + '/', current_camelcase_path, ngsi_ld_context)
        ### --- ###

        ### NGSI-LD PROPERTY IDENTIFICATION ###
        elif (is_property(element) == True) and (is_deprecated(element) == False):
            ngsi_ld_context[to_camelcase(str(element.keyword), str(element.arg))] = xpath + name
        ### --- ###

        ### NGSI-LD RELATIONSHIP IDENTIFICATION ###
        elif (is_relationship(element) == True) and (is_deprecated(element) == False):
            ngsi_ld_context[to_camelcase(str(element.keyword), str(element.arg))] = xpath + name
        ### --- ###

        ### NGSI-LD YANG IDENTITY IDENTIFICATION ###
        elif (is_yang_identity(element) == True) and (is_deprecated(element) == False):
            yang_identity_json_ld = {}
            yang_identity_context = []
            yang_identity_ngsi_ld_context = {}
            yang_identity_ngsi_ld_context["ietf-yang"] = IETF_YANG_URI
            yang_identity_ngsi_ld_context["YANGIdentity"] = "ietf-yang:YANGIdentity"
            yang_identity_ngsi_ld_context["description"] = "ietf-yang:description"
            yang_identity_ngsi_ld_context["identifier"] = "ietf-yang:identifier"
            yang_identity_ngsi_ld_context["namespace"] = "ietf-yang:namespace"
            yang_identity_ngsi_ld_context["broader"] = YANG_IDENTITY_BROADER_URI
            yang_identity_context.append(yang_identity_ngsi_ld_context)
            yang_identity_context.append(NGSI_LD_CORE_CONTEXT_URI)
            yang_identity_json_ld["@context"] = yang_identity_context
            yang_identity_filename = 'ngsi-ld-context/' + xpath.replace('/', '_').replace(':', '_') +  name.replace(':', '_') + '.jsonld'
            os.makedirs(os.path.dirname(yang_identity_filename), exist_ok=True)
            yang_identity_file = open(yang_identity_filename, 'w')
            yang_identity_file.write(json.dumps(yang_identity_json_ld, indent=4) + '\n')
            fd.write('NGSI-LD Context written to ' + yang_identity_file.name + '\n')
        ### --- ###
    
    ### --- ###
    
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
