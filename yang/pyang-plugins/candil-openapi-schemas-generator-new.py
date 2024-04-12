'''
pyang plugin -- CANDIL OpenAPI Schemas Generator.

Given one or several YANG modules, it dynamically generates the relative OpenAPI Schemas according to the OpenAPI specification for NGSI-LD API V1.6.1.

Version: 1.0.5.

Author: Networking and Virtualization Research Group (GIROS DIT-UPM) -- https://dit.upm.es/~giros
'''

import optparse
import pdb
import re
import sys
import json
import yaml

from pyang import plugin
from pyang import statements

### PLUGIN CONSTANTS ###
OPENAPI_URL = "https://raw.githubusercontent.com/giros-dit/python-ngsi-ld-client/1.6.1/schemas/ngsi-ld-api.yaml" # -> Consolidated OpenAPI spec. for NGSI-LD API v1.6.1
#OPENAPI_URL = "https://forge.etsi.org/rep/cim/NGSI-LD/-/raw/1.6.1/ngsi-ld-api.yaml" # -> Official OpenAPI spec. for NGSI-LD API v1.6.1
ENTITY_TYPE_LIST = [] # -> It includes all the different types of entities generated throughout all the YANG modules that are processed
### --- ###

def pyang_plugin_init():
    plugin.register_plugin(CandilXmlParserGeneratorPlugin())

class CandilXmlParserGeneratorPlugin(plugin.PyangPlugin):
    def __init__(self):
        plugin.PyangPlugin.__init__(self, 'candil-openapi-schemas-generator')

    def add_output_format(self, fmts):
        self.multiple_modules = True
        fmts['candil-openapi-schemas-generator'] = self
    
    def add_opts(self, optparser):
        optlist = [
            optparse.make_option('--candil-openapi-schemas-generator-help', dest='candil_openapi_schemas_generator_help', action='store_true', help='Prints help and usage.'),
        ]
        g = optparser.add_option_group('CANDIL OpenAPI Schemas Generator specific options')
        g.add_options(optlist)

    def setup_ctx(self, ctx):
        if ctx.opts.candil_openapi_schemas_generator_help:
            print_help()
            sys.exit(0)

    def setup_fmt(self, ctx):
        ctx.implicit_errors = False

    def emit(self, ctx, modules, fd):
        generate_python_openapi_schemas_generator_code(ctx, modules, fd)

def print_help():
    '''
    Prints execution help.
    '''
    print('''
Pyang plugin - CANDIL OpenAPI Schemas Generator (candil-openapi-schemas-generator).
Given one or several YANG modules, this plugin generates the OpenAPI schemas.

Usage:
pyang -f candil-openapi-schemas-generator [OPTIONS] <base_module.yang> [augmenting_module_1.yang] [augmenting_module_2.yang] ... [augmenting_module_N.yang] [> <output_file.yaml>]
    ''')
          
def generate_python_openapi_schemas_generator_code(ctx, modules, fd):
    '''
    Processes YANG modules and generates the corresponding OpenAPI schemas generator code for data modeled by these YANG modules.
    '''

    # Use PDB to debug the code with pdb.set_trace().
    # pdb.set_trace()

    ### FUNCTION CONSTANTS ###

    YANG_PRIMITIVE_TYPES = [
        "int8", "int16", "int32", "int64",
        "uint8", "uint16", "uint32", "uint64",
        "decimal64", "string", "boolean", "enumeration",
        "bits", "binary", "empty", "union"
    ]

    # NOTE: OpenAPI Schemas types.
    BASE_YANG_TYPES_TO_OPENAPI_SCHEMAS_TYPES = {
        'int8': 'integer',
        'int16': 'integer',
        'int32': 'integer',
        'int64': 'integer',
        'uint8': 'integer',
        'uint16': 'integer',
        'uint32': 'integer',
        'uint64': 'integer',
        'decimal64': 'number',
        'string': 'string',
        'boolean': 'boolean',
        'enumeration': 'enum',
        'bits': 'array',
        'binary': 'string',
        'empty': 'string',
        'union': 'string',
        'leafref': 'string'
    }

    # NOTE: OpenAPI Schemas formats.
    BASE_YANG_TYPES_TO_OPENAPI_SCHEMAS_FORMATS = {
        'int32': 'int32',
        'int64': 'int64',
        'bits': 'bits',
        'binary': 'binary'
    }

    INDENTATION_BLOCK = '  '

    ### --- ###

    ### AUXILIARY FUNCTIONS ###

    def to_camelcase(element_keyword: str, element_arg: str) -> str:
        '''
        Auxiliary function.
        Returns the CamelCase representation of element_arg according to the YANG to NGSI-LD translation conventions.
        '''
        if (element_keyword is None) or (element_arg is None):
            return element_arg
        else:
            if (element_keyword == 'module'):
                return element_arg
            if (element_keyword == 'container') or (element_keyword == 'list'):
                return re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), element_arg.capitalize())
            if (element_keyword == 'leaf') or (element_keyword == 'leaf-list') or (element_keyword == 'choice') or (element_keyword == 'case'):
                return re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), element_arg)
    
    def typedefs_discovering(modules) -> dict:
        '''
        Auxiliary function.
        Given a set of YANG modules, finds all typedefs defined in them and returns a Python
        dictionary with their conversions to primitive YANG types.
        '''
        defined_typedefs_dict = {}
        primitive_typedefs_dict = {}

        for module in modules: # First iteration retrieves the defined type.
            typedefs = module.search('typedef')
            if typedefs is not None:
                for typedef in typedefs:
                    if typedef is not None:
                        typedef_name = str(typedef.arg)
                        typedef_type = str(typedef.search_one('type').arg).split(':')[-1]
                        defined_typedefs_dict[typedef_name] = typedef_type
        
        for module in modules: # Second iteration retrieves the primitive type.
            typedefs = module.search('typedef')
            if typedefs is not None:
                for typedef in typedefs:
                    if typedef is not None:
                        typedef_name = str(typedef.arg)
                        typedef_type = str(typedef.search_one('type').arg).split(':')[-1]
                        if (typedef_type not in YANG_PRIMITIVE_TYPES) and ('ref' not in typedef_type):
                            primitive_typedefs_dict[typedef_name] = defined_typedefs_dict[typedef_type]
                        else:
                            primitive_typedefs_dict[typedef_name] = typedef_type
        return primitive_typedefs_dict
    
    def typedefs_pattern_discovering(modules) -> dict:
        '''
        Auxiliary function.
        Given a set of YANG modules, finds the patterns of all typedefs defined in them and returns a Python
        dictionary with their conversions to primitive YANG patterns.
        '''
        defined_typedefs_dict = {}
        patterns_defined_typedefs_dict = {}
        primitive_typedefs_dict = {}
        pattern_primitive_typedefs_dict = {}

        for module in modules: # First iteration retrieves the defined pattern.
            typedefs = module.search('typedef')
            if typedefs is not None:
                for typedef in typedefs:
                    if typedef is not None:
                        typedef_name = str(typedef.arg)
                        typedef_type = str(typedef.search_one('type').arg).split(':')[-1]
                        defined_typedefs_dict[typedef_name] = typedef_type
                        typedef_pattern = typedef.search_one('type').search_one('pattern')
                        if typedef_pattern != None:
                            typedef_pattern = str(typedef_pattern.arg)
                            patterns_defined_typedefs_dict[typedef_name] = typedef_pattern
        
        for module in modules: # Second iteration retrieves the primitive pattern.
            typedefs = module.search('typedef')
            if typedefs is not None:
                for typedef in typedefs:
                    if typedef is not None:
                        typedef_name = str(typedef.arg)
                        typedef_type = str(typedef.search_one('type').arg).split(':')[-1]
                        typedef_pattern = typedef.search_one('type').search_one('pattern')
                        if (typedef_type not in YANG_PRIMITIVE_TYPES) and ('ref' not in typedef_type):
                            primitive_typedefs_dict[typedef_name] = defined_typedefs_dict[typedef_type]
                            if typedef_pattern != None:
                                typedef_pattern = str(typedef_pattern.arg)
                                pattern_primitive_typedefs_dict[typedef_name] = patterns_defined_typedefs_dict[typedef_name]
                        else:
                            primitive_typedefs_dict[typedef_name] = typedef_type
                            if typedef_pattern != None:
                                typedef_pattern = str(typedef_pattern.arg)
                                pattern_primitive_typedefs_dict[typedef_name] = typedef_pattern

        return pattern_primitive_typedefs_dict

    def yang_to_openapi_schemas_types_conversion(element_type: str, typedefs_dict: dict) -> str:
        '''
        Auxiliary function.
        Returns the OpenAPI schemas type given the YANG type of an element/node in a YANG module.
        '''
        if (element_type == 'identityref'):
            return 'string'
        else:
            base_yang_type = ''
            if (typedefs_dict.get(element_type) is not None):
                base_yang_type = typedefs_dict[element_type]
            else:
                base_yang_type = element_type
            return BASE_YANG_TYPES_TO_OPENAPI_SCHEMAS_TYPES[base_yang_type]

    def yang_to_openapi_schemas_formats_conversion(element_type: str) -> str:
        '''
        Auxiliary function.
        Returns the OpenAPI schemas format given the YANG type of an element/node in a YANG module.
        '''
        if BASE_YANG_TYPES_TO_OPENAPI_SCHEMAS_FORMATS.get(element_type) is not None:
            return str(BASE_YANG_TYPES_TO_OPENAPI_SCHEMAS_FORMATS.get(element_type))
        else:
            return None
        
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
        if (str(element.keyword) == 'choice'):
            result = True
        return result
    
    def is_property(element, typedefs_dict: dict) -> bool:
        '''
        Auxiliary function.
        Checks if an element matches the YANG to NGSI-LD translation convention for a Property.
        '''
        result = False
        if (element.keyword in ['leaf-list', 'leaf']):
            element_type = str(element.search_one('type')).replace('type ', '').split(':')[-1]
            if (element_type in YANG_PRIMITIVE_TYPES) or \
                ((typedefs_dict.get(element_type) is not None) and ('ref' not in typedefs_dict.get(element_type))):
                result = True
        return result
    
    def is_relationship(element, typedefs_dict: dict) -> bool:
        '''
        Auxiliary function.
        Checks if an element matches the YANG to NGSI-LD translation convention for a Relationship.
        '''
        result = False

        if (element.keyword in ['leaf-list', 'leaf']):
            element_type = str(element.search_one('type')).replace('type ', '').split(':')[-1]
            if (element_type == 'leafref') or \
                ((typedefs_dict.get(element_type) is not None) and ('ref' in typedefs_dict.get(element_type))):
                result = True
        return result

    def is_datetime(element) -> bool:
        '''
        Auxiliary function.
        Checks if an element typedef matches to date-and-time.
        '''
        result = False
        if (element.keyword in ['leaf-list', 'leaf']):
            element_type = str(element.search_one('type')).replace('type ', '').split(':')[-1]
            if str(element_type) == "date-and-time":
                result = True
        return result

    def has_pattern(element, typedefs_pattern_dict: dict) -> bool:
        '''
        Auxiliary function.
        Checks if an element typedef has a pattern.
        '''
        result = False
        if (element.keyword in ['leaf-list', 'leaf']):
            element_type = str(element.search_one('type')).replace('type ', '').split(':')[-1]
            if typedefs_pattern_dict.get(element_type) is not None:
                result = True
        return result
    
    def get_yang_module_data_nodes(element, yang_data_nodes_list: list) -> list:
        '''
        Auxiliary recursive function.
        Recursively gets all YANG data nodes.
        '''
        if element.keyword in ['container', 'list', "choice"]:
            subelements = element.i_children
            if (subelements is not None):
                for subelement in subelements:
                    if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords) and (is_deprecated(subelement) == False):  
                        if str(subelement.keyword) == "choice":
                            cases = subelement.i_children
                            if (cases is not None):
                                for case in cases:
                                    if (case is not None) and (case.keyword in statements.data_definition_keywords) and (is_deprecated(case) == False):
                                        yang_data_nodes_list.append(case.arg)
                                        get_yang_module_data_nodes(case, yang_data_nodes_list)
                        else:
                            yang_data_nodes_list.append(subelement.arg) 
                            get_yang_module_data_nodes(subelement, yang_data_nodes_list)
        
        return yang_data_nodes_list

    def is_yang_identity(element, typedefs_dict: dict) -> bool:
        '''
        Auxiliary function.
        Checks if an element matches the YANG to NGSI-LD translation convention for a YANG Identity.
        NOTE: YANG Identities are NGSI-LD Entities, but since they are either leaf-lists or leaves, they
        have no children, and therefore they are processed differently.
        '''
        result = False
        if (element.keyword in ['leaf-list', 'leaf']):
            element_type = str(element.search_one('type')).replace('type ', '').split(':')[-1]
            if (element_type == 'identityref') or \
                ((typedefs_dict.get(element_type) is not None) and (typedefs_dict.get(element_type) == 'identityref')):
                result = True
        return result

    def generate_schemas(element, parent_element_arg, entity_path: str, camelcase_entity_path: str, depth_level: int, typedefs_dict: dict, typedefs_pattern_dict: dict, yang_data_nodes_list: list):
        '''
        Auxiliary function.
        Recursively generates the JSON parser code.
        '''
        global ENTITY_TYPE_LIST
        camelcase_element_arg = to_camelcase(str(element.keyword), str(element.arg))
        element_namespace = str(element.i_module.search_one('namespace').arg)
        yang_module_name = str(element.i_module.arg)
        
        current_path = ''
        if (entity_path is None):
            current_path = str(element.arg) + '_'
        else:
            current_path = entity_path + str(element.arg) + '_'
        
        ### ENCLOSING CONTAINER IDENTIFICATION ###
        if (is_enclosing_container(element) == True) and (is_deprecated(element) == False):
            subelements = element.i_children
            if (subelements is not None):
                for subelement in subelements:
                    if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                        if parent_element_arg is None:
                            generate_schemas(subelement, None, None, None, depth_level, typedefs_dict, typedefs_pattern_dict, yang_data_nodes_list)
                        else:
                            current_camelcase_path = ''
                            if (camelcase_entity_path is None):
                                current_camelcase_path = to_camelcase(str(element.keyword), str(subelement.arg))
                            else:
                                current_camelcase_path = camelcase_entity_path + to_camelcase(str(element.keyword), str(element.arg)) 
                            if subelement.keyword == 'container':
                                generate_schemas(subelement, element.arg, current_path, current_camelcase_path, depth_level, typedefs_dict, typedefs_pattern_dict, yang_data_nodes_list)
                            elif subelement.keyword == 'list':    
                                generate_schemas(subelement, parent_element_arg, current_path, current_camelcase_path, depth_level, typedefs_dict, typedefs_pattern_dict, yang_data_nodes_list)

                        
        ### NGSI-LD ENTITY IDENTIFICATION ###
        elif (is_entity(element) == True) and (is_deprecated(element) == False):
            current_camelcase_path = ''
            if (camelcase_entity_path is None):
                current_camelcase_path = to_camelcase(str(element.keyword), str(element.arg))
            else:
                current_camelcase_path = camelcase_entity_path + to_camelcase(str(element.keyword), str(element.arg))
            
            if current_camelcase_path not in ENTITY_TYPE_LIST:
                ENTITY_TYPE_LIST.append(current_camelcase_path)

            if (parent_element_arg is None): # 1st level Entity.
                if element.keyword in ['container']:
                    depth_level = 2
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + current_camelcase_path + ":")
                    depth_level += 1

                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: |")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + str(element.search_one('description').arg).replace('\n', '\n                ').replace('  ', ' '))
                    if element.search_one('reference') != None:
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + '\n        ' + 'Reference: ' + str(element.search_one('reference').arg).replace('\n', '\n                ').replace('  ', ' '))
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + '\n        ' + 'YANG module: ' + yang_module_name + '.yang')
                    depth_level -= 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "allOf:")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- $ref: \'" + OPENAPI_URL + "#/components/schemas/Entity\'")
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- type: object")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "properties:")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "type:")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: NGSI-LD Entity identifier. It has to be " + current_camelcase_path + ".")
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "type: string")
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "enum:")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- " +  current_camelcase_path)
                    depth_level -= 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "default: " + current_camelcase_path)
                    depth_level -= 1

                    subelements = element.i_children
                    subelement_list = []
                    if (subelements is not None):
                        for subelement in subelements:
                            if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords) and (subelement.keyword not in ['container', 'list']):
                                if str(subelement.arg) == "type":
                                     name_subelement = str(element.arg + str(subelement.arg.capitalize())).replace('-','')
                                     fd.write('\n' + INDENTATION_BLOCK * depth_level + name_subelement + ":")
                                     depth_level += 1
                                     ref_subelement = (current_camelcase_path + str(subelement.arg.capitalize())).replace('-','')
                                     fd.write('\n' + INDENTATION_BLOCK * depth_level +  "$ref: \'#/components/schemas/" + ref_subelement + "\'")
                                else:
                                    camelcase_subelement_arg = to_camelcase(str(subelement.keyword), str(subelement.arg))
                                    fd.write('\n' + INDENTATION_BLOCK * depth_level + camelcase_subelement_arg + ":")
                                    depth_level += 1
                                    if yang_data_nodes_list.count(str(subelement.arg)) > 1:
                                        fd.write('\n' + INDENTATION_BLOCK * depth_level +  "$ref: \'#/components/schemas/" + current_camelcase_path + str(re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), subelement.arg.capitalize())) + "\'")
                                    else:
                                        fd.write('\n' + INDENTATION_BLOCK * depth_level +  "$ref: \'#/components/schemas/" + re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), subelement.arg.capitalize()) + "\'")
                                depth_level -= 1
                    
                    depth_level -= 2
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- required:")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- type")
                    if 'name' in subelement_list:
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + "- name")
                    if (subelements is not None):
                        for subelement in subelements:
                            if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords) and (subelement.keyword not in ['container', 'list']):
                                mandatory = subelement.search_one('mandatory')
                                if mandatory != None:
                                    if str(mandatory.arg) == "true":
                                        if str(subelement.arg) == "type":
                                            name_subelement = str(element.arg + str(subelement.arg.capitalize())).replace('-','')
                                            fd.write('\n' + INDENTATION_BLOCK * depth_level + "- " + name_subelement)
                                        else:
                                            fd.write('\n' + INDENTATION_BLOCK * depth_level + "- " + to_camelcase(str(subelement.keyword), str(subelement.arg)))
                    if (subelements is not None):
                        for subelement in subelements:
                            if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                                generate_schemas(subelement, element.arg, current_path, current_camelcase_path, depth_level, typedefs_dict, typedefs_pattern_dict, yang_data_nodes_list)
                elif element.keyword in ['list']:    
                    depth_level = 2                
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + current_camelcase_path + ":")
                    depth_level += 1
                                        
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: |")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + str(element.search_one('description').arg).replace('\n', '\n                ').replace('  ', ' '))
                    if element.search_one('reference') != None:
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + '\n        ' + 'Reference: ' + str(element.search_one('reference').arg).replace('\n', '\n                ').replace('  ', ' '))
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + '\n        ' + 'YANG module: ' + yang_module_name + '.yang')
                    depth_level -= 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "allOf:")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- $ref: \'" + OPENAPI_URL + "#/components/schemas/Entity\'")
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- type: object")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "properties:")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "type:")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: NGSI-LD Entity identifier. It has to be " + current_camelcase_path + ".")
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "type: string")
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "enum:")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- " +  current_camelcase_path)
                    depth_level -= 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "default: " + current_camelcase_path)
                    depth_level -= 1

                    subelements = element.i_children
                    subelement_list = []
                    if (subelements is not None):
                        for subelement in subelements:
                            if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords) and (subelement.keyword not in ['container', 'list']):
                                if str(subelement.arg) == "type":
                                     name_subelement = str(element.arg + str(subelement.arg.capitalize())).replace('-','')
                                     fd.write('\n' + INDENTATION_BLOCK * depth_level + name_subelement + ":")
                                     depth_level += 1
                                     ref_subelement = (current_camelcase_path + str(subelement.arg.capitalize())).replace('-','')
                                     fd.write('\n' + INDENTATION_BLOCK * depth_level +  "$ref: \'#/components/schemas/" + ref_subelement + "\'")
                                else:
                                    camelcase_subelement_arg = to_camelcase(str(subelement.keyword), str(subelement.arg))
                                    subelement_list.append(camelcase_subelement_arg)
                                    fd.write('\n' + INDENTATION_BLOCK * depth_level + camelcase_subelement_arg + ":")
                                    depth_level += 1
                                        
                                    if yang_data_nodes_list.count(str(subelement.arg)) > 1:
                                        fd.write('\n' + INDENTATION_BLOCK * depth_level +  "$ref: \'#/components/schemas/" + current_camelcase_path + str(re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), subelement.arg.capitalize())) + "\'")
                                    else:
                                        fd.write('\n' + INDENTATION_BLOCK * depth_level +  "$ref: \'#/components/schemas/" + re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), subelement.arg.capitalize()) + "\'")
                                depth_level -= 1
                    depth_level -= 2
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- required:")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- type")
                    if 'name' in subelement_list:
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + "- name")
                    if (subelements is not None):
                        for subelement in subelements:
                            if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords) and (subelement.keyword not in ['container', 'list']):
                                mandatory = subelement.search_one('mandatory')
                                if mandatory != None:
                                    if str(mandatory.arg) == "true":
                                        if str(subelement.arg) == "type":
                                            name_subelement = str(element.arg + str(subelement.arg.capitalize())).replace('-','')
                                            fd.write('\n' + INDENTATION_BLOCK * depth_level + "- " + name_subelement)
                                        else:
                                            fd.write('\n' + INDENTATION_BLOCK * depth_level + "- " + to_camelcase(str(subelement.keyword), str(subelement.arg)))
                    if (subelements is not None):
                        for subelement in subelements:
                            if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                                generate_schemas(subelement, element.arg, current_path, current_camelcase_path, depth_level, typedefs_dict, typedefs_pattern_dict, yang_data_nodes_list)
            else: # 2nd level Entity onwards.
                if element.keyword in ['container']:
                    depth_level = 2
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + current_camelcase_path + ":")
                    depth_level += 1

                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: |")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + str(element.search_one('description').arg).replace('\n', '\n                ').replace('  ', ' '))
                    if element.search_one('reference') != None:
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + '\n        ' + 'Reference: ' + str(element.search_one('reference').arg).replace('\n', '\n                ').replace('  ', ' '))
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + '\n        ' + 'YANG module: ' + yang_module_name + '.yang')
                    depth_level -= 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "allOf:")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- $ref: \'" + OPENAPI_URL + "#/components/schemas/Entity\'")
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- type: object")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "properties:")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "type:")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: NGSI-LD Entity identifier. It has to be " + current_camelcase_path + ".")
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "type: string")
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "enum:")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- " +  current_camelcase_path)
                    depth_level -= 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "default: " + current_camelcase_path)
                    depth_level -= 1

                    subelements = element.i_children
                    subelement_list = []
                    if (subelements is not None):
                        for subelement in subelements:
                            if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords) and (subelement.keyword not in ['container', 'list']):
                                if str(subelement.arg) == "type":
                                     name_subelement = str(element.arg + str(subelement.arg.capitalize())).replace('-','')
                                     fd.write('\n' + INDENTATION_BLOCK * depth_level + name_subelement + ":")
                                     depth_level += 1
                                     ref_subelement = (current_camelcase_path + str(subelement.arg.capitalize())).replace('-','')
                                     fd.write('\n' + INDENTATION_BLOCK * depth_level +  "$ref: \'#/components/schemas/" + ref_subelement + "\'")
                                else:
                                    camelcase_subelement_arg = to_camelcase(str(subelement.keyword), str(subelement.arg))
                                    fd.write('\n' + INDENTATION_BLOCK * depth_level + camelcase_subelement_arg + ":")
                                    depth_level += 1
                                    if yang_data_nodes_list.count(str(subelement.arg)) > 1:
                                        fd.write('\n' + INDENTATION_BLOCK * depth_level +  "$ref: \'#/components/schemas/" + current_camelcase_path + str(re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), subelement.arg.capitalize())) + "\'")
                                    else:   
                                        fd.write('\n' + INDENTATION_BLOCK * depth_level +  "$ref: \'#/components/schemas/" + re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), subelement.arg.capitalize()) + "\'")
                                depth_level -= 1
                    
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "isPartOf:")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level +  "$ref: \'#/components/schemas/IsPartOf\'")
                    if(is_enclosing_container(element.parent) == True):
                        entity_type_parent = re.sub(r'_([^_]*)_$', '_', entity_path)
                        if(is_enclosing_container(element.parent.parent) == True): 
                            parent = element.parent.parent
                            while True:
                                if(is_enclosing_container(parent) == True):
                                    entity_type_parent = re.sub(r'_([^_]*)_$', '_', entity_type_parent)
                                    parent = parent.parent
                                else:
                                    break
                                
                        entity_type_parent = re.sub(r'(_)(\w)', lambda m: m.group(2).upper(), entity_type_parent.capitalize())
                        entity_type_parent = re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), entity_type_parent)
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: isPartOf Relationship with Entity type " + entity_type_parent.replace('_','') + ".")
                    else:
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: isPartOf Relationship with Entity type " + camelcase_entity_path + ".")                    
                    depth_level -= 1
                    depth_level -= 2
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- required:")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- type")
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- isPartOf")
                    if 'name' in subelement_list:
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + "- name")
                    if (subelements is not None):
                        for subelement in subelements:
                            if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords) and (subelement.keyword not in ['container', 'list']):
                                mandatory = subelement.search_one('mandatory')
                                if mandatory != None:
                                    if str(mandatory.arg) == "true":
                                        if str(subelement.arg) == "type":
                                            name_subelement = str(element.arg + str(subelement.arg.capitalize())).replace('-','')
                                            fd.write('\n' + INDENTATION_BLOCK * depth_level + "- " + name_subelement)
                                        else:
                                            fd.write('\n' + INDENTATION_BLOCK * depth_level + "- " + to_camelcase(str(subelement.keyword), str(subelement.arg)))
                                        
                    subelements = element.i_children
                    if (subelements is not None):
                        for subelement in subelements:
                            if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                                generate_schemas(subelement, element.arg, current_path, current_camelcase_path, depth_level, typedefs_dict, typedefs_pattern_dict, yang_data_nodes_list)

                elif element.keyword in ['list']:
                    depth_level = 2
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + current_camelcase_path + ":")
                    depth_level += 1
                                        
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: |")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + str(element.search_one('description').arg).replace('\n', '\n                ').replace('  ', ' '))
                    if element.search_one('reference') != None:
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + '\n        ' + 'Reference: ' + str(element.search_one('reference').arg).replace('\n', '\n                ').replace('  ', ' '))
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + '\n        ' + 'YANG module: ' + yang_module_name + '.yang')
                    depth_level -= 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "allOf:")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- $ref: \'" + OPENAPI_URL + "#/components/schemas/Entity\'")
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- type: object")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "properties:")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "type:")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: NGSI-LD Entity identifier. It has to be " + current_camelcase_path + ".")
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "type: string")
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "enum:")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- " +  current_camelcase_path)
                    depth_level -= 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "default: " + current_camelcase_path)
                    depth_level -= 1
                    
                    subelements = element.i_children
                    subelement_list = []
                    if (subelements is not None):
                        for subelement in subelements:
                            if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords) and (subelement.keyword not in ['container', 'list']):
                                if str(subelement.arg) == "type":
                                     name_subelement = str(element.arg + str(subelement.arg.capitalize())).replace('-','')
                                     fd.write('\n' + INDENTATION_BLOCK * depth_level + name_subelement + ":")
                                     depth_level += 1
                                     ref_subelement = (current_camelcase_path + str(subelement.arg.capitalize())).replace('-','')
                                     fd.write('\n' + INDENTATION_BLOCK * depth_level +  "$ref: \'#/components/schemas/" + ref_subelement + "\'")
                                else:
                                    camelcase_subelement_arg = to_camelcase(str(subelement.keyword), str(subelement.arg))
                                    fd.write('\n' + INDENTATION_BLOCK * depth_level + str(camelcase_subelement_arg) + ":")
                                    depth_level += 1
                                    if yang_data_nodes_list.count(str(subelement.arg)) > 1:
                                        fd.write('\n' + INDENTATION_BLOCK * depth_level +  "$ref: \'#/components/schemas/" + current_camelcase_path + str(re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), subelement.arg.capitalize())) + "\'")
                                    else:
                                        fd.write('\n' + INDENTATION_BLOCK * depth_level +  "$ref: \'#/components/schemas/" + re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), subelement.arg.capitalize()) + "\'")
                                depth_level -= 1
                    
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "isPartOf:")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level +  "$ref: \'#/components/schemas/IsPartOf\'")
                    if(is_enclosing_container(element.parent) == True):
                        entity_type_parent = re.sub(r'_([^_]*)_$', '_', entity_path)
                        if(is_enclosing_container(element.parent.parent) == True):
                            parent = element.parent.parent
                            while True:
                                if(is_enclosing_container(parent) == True):
                                    entity_type_parent = re.sub(r'_([^_]*)_$', '_', entity_type_parent)
                                    parent = parent.parent
                                else:
                                    break 

                        entity_type_parent = re.sub(r'(_)(\w)', lambda m: m.group(2).upper(), entity_type_parent.capitalize())
                        entity_type_parent = re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), entity_type_parent)
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: isPartOf Relationship with Entity type " + entity_type_parent.replace('_','') + ".")
                    else:
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: isPartOf Relationship with Entity type " + camelcase_entity_path + ".")
                    depth_level -= 1
                    depth_level -= 2
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- required:")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- type")
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- isPartOf")
                    if 'name' in subelement_list:
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + "- name")
                    if (subelements is not None):
                        for subelement in subelements:
                            if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords) and (subelement.keyword not in ['container', 'list']):
                                mandatory = subelement.search_one('mandatory')
                                if mandatory != None:
                                    if str(mandatory.arg) == "true":
                                        if str(subelement.arg) == "type":
                                            name_subelement = str(element.arg + str(subelement.arg.capitalize())).replace('-','')
                                            fd.write('\n' + INDENTATION_BLOCK * depth_level + "- " + name_subelement)
                                        else:
                                            fd.write('\n' + INDENTATION_BLOCK * depth_level + "- " + to_camelcase(str(subelement.keyword), str(subelement.arg)))
                    subelements = element.i_children
                    if (subelements is not None):
                        for subelement in subelements:
                            if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                                generate_schemas(subelement, element.arg, current_path, current_camelcase_path, depth_level, typedefs_dict, typedefs_pattern_dict, yang_data_nodes_list)
        ### --- ###
        
        ### YANG CHOICE IDENTIFICATION: IT CONTAINS NGSI-LD PROPERTIES ###
        elif (is_choice(element) == True) and (is_deprecated(element) == False):
            depth_level = 2
            current_camelcase_path = ''

            if (yang_data_nodes_list.count(str(element.arg)) > 1) or (str(element.arg) == 'type'):
                current_camelcase_path = camelcase_entity_path + str(re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), element.arg.capitalize()))
            else:
                current_camelcase_path = str(re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), element.arg.capitalize()))

            fd.write('\n' + INDENTATION_BLOCK * depth_level + current_camelcase_path + ":")
            depth_level += 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: |")
            depth_level += 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + str(element.search_one('description').arg).replace('\n', '\n                ').replace('  ', ' '))
            if element.search_one('reference') != None:
                fd.write('\n' + INDENTATION_BLOCK * depth_level + '\n        ' + 'Reference: ' + str(element.search_one('reference').arg).replace('\n', '\n                ').replace('  ', ' '))
            if element.search_one('units') != None:
                fd.write('\n' + INDENTATION_BLOCK * depth_level + '\n        ' + 'Units: ' + str(element.search_one('units').arg).replace('\n', '\n                ').replace('  ', ' '))
            fd.write('\n' + INDENTATION_BLOCK * depth_level + '\n        ' + 'YANG module: ' + yang_module_name + '.yang')
            depth_level -= 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "oneOf:")
            depth_level += 1

            cases = element.i_children
            if (cases is not None):
                for case in cases:
                    if (case is not None) and (case.keyword in statements.data_definition_keywords) and (str(case.keyword) == "case"):
                        choice_camelcase_path = ''

                        if (yang_data_nodes_list.count(str(case.arg)) > 1) or (str(case.arg) == 'type'):
                            choice_camelcase_path = current_camelcase_path + str(re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), case.arg.capitalize()))
                        else:
                            choice_camelcase_path = str(re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), case.arg.capitalize()))

                        fd.write('\n' + INDENTATION_BLOCK * depth_level +  "- $ref: \'#/components/schemas/" + choice_camelcase_path + "\'")

            depth_level -= 1
            if (cases is not None):
                for case in cases:
                    if (case is not None) and (case.keyword in statements.data_definition_keywords):
                        subelements = case.i_children
                        if (subelements is not None):
                            for subelement in subelements:
                                if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                                    generate_schemas(subelement, element.arg, current_path, current_camelcase_path, depth_level, typedefs_dict, typedefs_pattern_dict, yang_data_nodes_list)

        ### --- ###
        
        ### NGSI-LD PROPERTY IDENTIFICATION ###
        elif (is_property(element, typedefs_dict) == True) and (is_deprecated(element) == False):
            depth_level = 2

            current_camelcase_path = ''

            if (yang_data_nodes_list.count(str(element.arg)) > 1) or (str(element.arg) == 'type'):
                current_camelcase_path = camelcase_entity_path + str(re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), element.arg.capitalize()))
            else:
                current_camelcase_path = str(re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), element.arg.capitalize()))

            openapi_schema_type = yang_to_openapi_schemas_types_conversion(str(element.search_one('type')).replace('type ', '').split(":")[-1], typedefs_dict)
            openapi_schema_format = yang_to_openapi_schemas_formats_conversion(str(element.search_one('type')).replace('type ', '').split(":")[-1])

            fd.write('\n' + INDENTATION_BLOCK * depth_level + current_camelcase_path + ":")
            depth_level += 1
                        
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: |")
            depth_level += 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + str(element.search_one('description').arg).replace('\n', '\n                ').replace('  ', ' '))
            if element.search_one('reference') != None:
                fd.write('\n' + INDENTATION_BLOCK * depth_level + '\n        ' + 'Reference: ' + str(element.search_one('reference').arg).replace('\n', '\n                ').replace('  ', ' '))
            if element.search_one('units') != None:
                fd.write('\n' + INDENTATION_BLOCK * depth_level + '\n        ' + 'Units: ' + str(element.search_one('units').arg).replace('\n', '\n                ').replace('  ', ' '))
            fd.write('\n' + INDENTATION_BLOCK * depth_level + '\n        ' + 'YANG module: ' + yang_module_name + '.yang')
            depth_level -= 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "additionalProperties: false")
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "allOf:")
            depth_level += 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "- $ref: \'" + OPENAPI_URL + "#/components/schemas/Property\'")
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "- type: object")
            depth_level += 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "properties:")
            depth_level += 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "value:")
            depth_level += 1
            if str(openapi_schema_type) == "enum":
                fd.write('\n' + INDENTATION_BLOCK * depth_level + "type: " + "string")
                fd.write('\n' + INDENTATION_BLOCK * depth_level + "enum:")
                element_enums = element.search_one('type').search('enum')  
                             
                if len(element_enums) == 0:
                    element_enums = element.search_one('type').i_typedef.search_one('type').search('enum')

                depth_level += 1

                for element_enum in element_enums:
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- " + str(element_enum.arg))
                depth_level -= 1

                if element.search_one('default') is not None:
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "default: " + str(element.search_one('default').arg))
            else:
                if str(openapi_schema_type) == "array":
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "type: " + str(openapi_schema_type))
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "items:" )
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "type: string")
                else:
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "type: " + str(openapi_schema_type))
                if is_datetime(element) == True:
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "format: datetime") 
                if openapi_schema_format is not None:
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "format: " + openapi_schema_format)   
                if has_pattern(element, typedefs_pattern_dict) == True:
                    element_type = str(element.search_one('type')).replace('type ', '').split(':')[-1]
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "pattern: \'" + str(typedefs_pattern_dict.get(element_type)) + "\'")
                if element.search_one('default') is not None:
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "default: " + str(element.search_one('default').arg))   
                '''
                if element.search_one('maximum') is not None:
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "maximum: " + str(element.search_one('maximum').arg)) 
                if element.search_one('minimum') is not None:
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "minimum: " + str(element.search_one('minimum').arg)) 
                '''
                if element.search_one('type').search_one('range') != None:
                    element_type_range = str(element.search_one('type').search_one('range').arg)
                    minimum = element_type_range.split("..")[0]
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "minimum: " + minimum) 
                    maximum = element_type_range.split("..")[1]
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "maximum: " + maximum)

            if str(openapi_schema_type) == "array":
                depth_level -=1
            depth_level -= 2
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "required:")
            depth_level += 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "- value")
            depth_level -= 4
        ### --- ###
        
        ### NGSI-LD RELATIONSHIP IDENTIFICATION ###
        elif (is_relationship(element, typedefs_dict) == True) and (is_deprecated(element) == False):
            depth_level = 2

            current_camelcase_path = ''

            if (yang_data_nodes_list.count(str(element.arg))) > 1 or (str(element.arg) == 'type'):
                current_camelcase_path = camelcase_entity_path + str(re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), element.arg.capitalize()))
            else:
                current_camelcase_path = str(re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), element.arg.capitalize()))

            pointer = element.i_leafref_ptr[0]
            pointer_parent = pointer.parent
            camelcase_pointer_parent = to_camelcase(str(pointer_parent.keyword), str(pointer_parent.arg))

            #print("CHACHO " + camelcase_pointer_parent) 
            #print(camelcase_entity_path + " " + current_camelcase_path)

            matches = [] # Best match is always the first element appended into the list: index 0.
            for camelcase_entity in ENTITY_TYPE_LIST:
                if camelcase_pointer_parent == camelcase_entity_path + camelcase_entity:
                    matches.append(camelcase_entity)

            if len(matches) == 0:
                #print("CHACHO1")
                childs = element.parent.i_children
                matched_childs = 0
                if (childs is not None) and (camelcase_entity_path + camelcase_pointer_parent) != current_camelcase_path:
                    #print("CHACHO2")
                    has_childs = True
                    element_aux = element
                    iterations = 0
                    while has_childs == True:
                        for child in childs:
                            #print("child: " + child.arg)
                            #print("pointer-parent: " + str(pointer_parent.arg))
                            if child.arg == str(pointer_parent.arg):
                                matched_childs += 1
                                break
                        
                        if matched_childs == 0:
                            for child in childs:
                                    #pdb.set_trace()
                                    if is_entity(child) == True:
                                        subchilds = child.i_children
                                        if (subchilds is not None):
                                            iterations += 1
                                            for subchild in subchilds:
                                                #print("subchild: " + subchild.arg)
                                                #print("pointer-parent: " + str(pointer_parent.arg))
                                                if subchild.arg == str(pointer_parent.arg):
                                                    matched_childs += 1
                        
                        if matched_childs > 0:    
                            #print("CHACHO21")
                            if iterations > 0:
                                #print("CHACHO211")
                                for camelcase_entity in ENTITY_TYPE_LIST:
                                    
                                    if camelcase_pointer_parent == camelcase_entity or camelcase_pointer_parent in camelcase_entity:
                                        matches.append(camelcase_entity)
                                        #print(camelcase_entity)

                                
                                if len(matches) == 0:
                                    #print("CHACHO2111")
                                    relationship_camelcase_path = camelcase_pointer_parent
                                else:
                                    #print("CHACHO2112")
                                    relationship_camelcase_path = matches[0]  
                                 
                                '''
                                for camelcase_entity in ENTITY_TYPE_LIST:
                                    if camelcase_pointer_parent == camelcase_entity:
                                        relationship_camelcase_path = camelcase_pointer_parent
                                        ENTITY_TYPE_LIST.append(relationship_camelcase_path)
                                '''
                            else:
                                #print("CHACHO212")
                                relationship_camelcase_path = camelcase_entity_path + camelcase_pointer_parent
                                ENTITY_TYPE_LIST.append(relationship_camelcase_path)
                            
                            has_childs = False
                        else:
                            #print("CHACHO22")
                            iterations += 1
                            element_aux = element_aux.parent
                            if element_aux.parent is not None:
                                childs = element_aux.parent.i_children
                                if (childs is None):
                                    has_childs = False
                                    relationship_camelcase_path = camelcase_pointer_parent
                            else: 
                                has_childs = False
                                relationship_camelcase_path = camelcase_pointer_parent
                else:
                    #print("CHACHO3")
                    for camelcase_entity in ENTITY_TYPE_LIST:
                        if camelcase_pointer_parent == camelcase_entity or camelcase_pointer_parent in camelcase_entity:
                            matches.append(camelcase_entity)

                    if len(matches) == 0:
                        relationship_camelcase_path = camelcase_pointer_parent
                    else:
                        relationship_camelcase_path = matches[0]
            else:
                #print("CHACHO4")
                relationship_camelcase_path = matches[0]


            openapi_schema_type = yang_to_openapi_schemas_types_conversion(str(element.search_one('type')).replace('type ', '').split(":")[-1], typedefs_dict)
            openapi_schema_format = yang_to_openapi_schemas_formats_conversion(str(element.search_one('type')).replace('type ', '').split(":")[-1])

            fd.write('\n' + INDENTATION_BLOCK * depth_level + current_camelcase_path + ":")
            depth_level += 1
                    
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: |")
            depth_level += 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + str(element.search_one('description').arg).replace('\n', '\n                ').replace('  ', ' '))
            if element.search_one('reference') != None:
                fd.write('\n' + INDENTATION_BLOCK * depth_level + '\n        ' + 'Reference: ' + str(element.search_one('reference').arg).replace('\n', '\n                ').replace('  ', ' '))
            if element.search_one('units') != None:
                fd.write('\n' + INDENTATION_BLOCK * depth_level + '\n        ' + 'Units: ' + str(element.search_one('units').arg).replace('\n', '\n                ').replace('  ', ' '))
            fd.write('\n' + INDENTATION_BLOCK * depth_level + '\n        ' + 'YANG module: ' + yang_module_name + '.yang')
            depth_level -= 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "additionalProperties: false")
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "allOf:")
            depth_level += 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "- $ref: \'" + OPENAPI_URL + "#/components/schemas/Relationship\'")
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "- type: object")
            depth_level += 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "properties:")
            depth_level += 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "object:")
            depth_level += 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: Relationship with Entity type " + relationship_camelcase_path + ".")
            if str(openapi_schema_type) == "enum":
                fd.write('\n' + INDENTATION_BLOCK * depth_level + "type: " + "string")
                fd.write('\n' + INDENTATION_BLOCK * depth_level + "enum:")
                element_enums = element.search_one('type').search('enum')
                
                if len(element_enums) == 0:
                    element_enums = element.search_one('type').i_typedef.search_one('type').search('enum')

                depth_level += 1

                for element_enum in element_enums:
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- " + str(element_enum.arg))
                depth_level -= 1

                if element.search_one('default') is not None:
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "default: " + str(element.search_one('default').arg))
            else:
                if str(openapi_schema_type) == "array":
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "type: " + str(openapi_schema_type))
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "items:" )
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "type: string")
                else:
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "type: " + str(openapi_schema_type))
                if is_datetime(element) == True:
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "format: datetime") 
                if openapi_schema_format is not None:
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "format: " + openapi_schema_format)
                if has_pattern(element, typedefs_pattern_dict) == True:
                    element_type = str(element.search_one('type')).replace('type ', '').split(':')[-1]
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "pattern: \'" + str(typedefs_pattern_dict.get(element_type)) + "\'")
                if element.search_one('default') is not None:
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "default: " + str(element.search_one('default').arg))
                '''
                if element.search_one('maximum') is not None:
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "maximum: " + str(element.search_one('maximum').arg)) 
                if element.search_one('minimum') is not None:
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "minimum: " + str(element.search_one('minimum').arg)) 
                '''
                if element.search_one('type').search_one('range') != None:
                    element_type_range = str(element.search_one('type').search_one('range'))
                    minimum = element_type_range.split("..")[0]
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "minimum: " + minimum) 
                    maximum = element_type_range.split("..")[1]
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "maximum: " + maximum)
            
            if str(openapi_schema_type) == "array":
                depth_level -=1
            depth_level -= 2
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "required:")
            depth_level += 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "- object")
            depth_level -= 4
        ### --- ###

        ### NGSI-LD YANG IDENTITY IDENTIFICATION ###
        elif (is_yang_identity(element, typedefs_dict) == True) and (is_deprecated(element) == False):
            depth_level = 2

            yang_identity_name = ''

            if (yang_data_nodes_list.count(str(element.arg)) > 1) or (str(element.arg) == 'type'):
                yang_identity_name = camelcase_entity_path + str(re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), element.arg.capitalize()))
            else:
                yang_identity_name = str(re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), element.arg.capitalize()))

            openapi_schema_type = yang_to_openapi_schemas_types_conversion(str(element.search_one('type')).replace('type ', '').split(":")[-1], typedefs_dict)

            fd.write('\n' + INDENTATION_BLOCK * depth_level + yang_identity_name + ":")
            depth_level += 1
                                
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: |")
            depth_level += 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + str(element.search_one('description').arg).replace('\n', '\n                ').replace('  ', ' '))
            if element.search_one('reference') != None:
                fd.write('\n' + INDENTATION_BLOCK * depth_level + '\n        ' + 'Reference: ' + str(element.search_one('reference').arg).replace('\n', '\n                ').replace('  ', ' '))
            if element.search_one('units') != None:
                fd.write('\n' + INDENTATION_BLOCK * depth_level + '\n        ' + 'Units: ' + str(element.search_one('units').arg).replace('\n', '\n                ').replace('  ', ' '))
            fd.write('\n' + INDENTATION_BLOCK * depth_level + '\n        ' + 'YANG module: ' + yang_module_name + '.yang')
            depth_level -= 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "additionalProperties: false")
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "allOf:")
            depth_level += 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "- $ref: \'" + OPENAPI_URL + "#/components/schemas/Relationship\'")
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "- type: object")
            depth_level += 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "properties:")
            depth_level += 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "object:")
            depth_level += 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: Relationship with Entity type YANGIdentity.")

            if str(openapi_schema_type) == "string":
                fd.write('\n' + INDENTATION_BLOCK * depth_level + "type: " + "string")
            
            if element.search_one('default') is not None:
                fd.write('\n' + INDENTATION_BLOCK * depth_level + "default: urn:ngsi-ld:YANGIdentity:" + str(element.search_one('default').arg))

            depth_level -= 2
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "required:")
            depth_level += 1
            fd.write('\n' + INDENTATION_BLOCK * depth_level + "- object")
            depth_level -= 4
        ### --- ###
    
    ### --- ###

    aux_args = sys.argv[3:]
    args = []
    for arg in aux_args:
        args.append(arg.split('/')[-1])

    fd.write("openapi: 3.0.3")
    fd.write('\n' + "info:")
    fd.write('\n' + INDENTATION_BLOCK + "title: OpenAPI schemas for YANG data models " + ', '.join(map(str, args)) + ".") 
    fd.write('\n' + INDENTATION_BLOCK + "version: 1.0.0")
    fd.write('\n' + INDENTATION_BLOCK + "description: OpenAPI schemas for YANG data models compliant with the NGSI-LD OAS V1.6.1 metamodel according to ETSI GS CIM 009 V1.6.1.")
    fd.write('\n' + "paths: {}")
    fd.write('\n' + "components:")
    fd.write('\n' + INDENTATION_BLOCK + "schemas:")

    # Find typedefs, including those from modules in import sentences:
    typedef_modules = []

    for module in modules:
        typedef_modules.append(module)
        imports = module.search('import')
        for i in imports:
            submodule = ctx.get_module(i.arg)
            if submodule is not None:
                typedef_modules.append(submodule)
    typedef_modules = list(dict.fromkeys(typedef_modules)) # Delete duplicates.
    typedefs_dict = typedefs_discovering(typedef_modules)
    typedefs_pattern_dict = typedefs_pattern_discovering(typedef_modules)

    # Get all data nodes for the evaluated YANG modules
    yang_data_nodes_list = []
    #full_yang_data_nodes_list = []
    for module in modules:
        elements = module.i_children
        if (elements is not None):
            for element in elements:
                if (element is not None) and (element.keyword in statements.data_definition_keywords):
                    yang_data_nodes_list.append(element.arg)
                    get_yang_module_data_nodes(element, yang_data_nodes_list)
                    #full_yang_data_nodes_list.append(element.arg)
                    #full_yang_data_nodes_list.append(get_yang_module_data_nodes(element, yang_data_nodes_list))
                    
    # Generate OpenAPI generator code (element data retrieval and transformation to generate OpenAPI schemas):
    depth_level = 2
    
    for module in modules:
        elements = module.i_children
        if (elements is not None):
            for element in elements:
                if (element is not None) and (element.keyword in statements.data_definition_keywords):
                    generate_schemas(element, None, None, None, depth_level, typedefs_dict, typedefs_pattern_dict, yang_data_nodes_list)
    
    
    depth_level = 2

    fd.write('\n' + INDENTATION_BLOCK * depth_level + "YANGIdentity:")
    depth_level += 1

    fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: A representation schema for YANG Identities.")
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "allOf:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- $ref: \'" + OPENAPI_URL + "#/components/schemas/Entity\'")
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- type: object")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "properties:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "type:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: NGSI-LD Entity identifier. It has to be YANGIdentity.")
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "type: string")
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "enum:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- YANGIdentity")
    depth_level -= 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "default: YANGIdentity")
    depth_level -= 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "description:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "$ref: \'#/components/schemas/YANGIdentityDescription\'")
    depth_level -= 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "identifier:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "$ref: \'#/components/schemas/YANGIdentityIdentifier\'")
    depth_level -= 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "namespace:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "$ref: \'#/components/schemas/YANGIdentityNamespace\'")
    depth_level -= 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "broader:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "$ref: \'#/components/schemas/YANGIdentityBroader\'")
    depth_level -= 3
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- required:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- type")
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- description")
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- identifier")
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- namespace")

    depth_level = 2

    fd.write('\n' + INDENTATION_BLOCK * depth_level + "YANGIdentityDescription:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: NGSI-LD Relationship Type. YANG Identity description.")
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "additionalProperties: false")
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "allOf:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- $ref: \'" + OPENAPI_URL + "#/components/schemas/Property\'")
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- type: object")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "properties:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "value:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "type: string")
    depth_level -= 2
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "required:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- value")

    depth_level = 2

    fd.write('\n' + INDENTATION_BLOCK * depth_level + "YANGIdentityIdentifier:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: NGSI-LD Property Type. YANG Identity identifier.")
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "additionalProperties: false")
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "allOf:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- $ref: \'" + OPENAPI_URL + "#/components/schemas/Property\'")
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- type: object")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "properties:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "value:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "type: string")
    depth_level -= 2
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "required:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- value")

    depth_level = 2

    fd.write('\n' + INDENTATION_BLOCK * depth_level + "YANGIdentityNamespace:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: NGSI-LD Property Type. YANG Identity namespace.")
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "additionalProperties: false")
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "allOf:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- $ref: \'" + OPENAPI_URL + "#/components/schemas/Property\'")
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- type: object")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "properties:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "value:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "type: string")
    depth_level -= 2
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "required:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- value")
    
    depth_level = 2

    fd.write('\n' + INDENTATION_BLOCK * depth_level + "YANGIdentityBroader:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: NGSI-LD Relationship Type. The relationship to the base YANG Identity.")
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "additionalProperties: false")
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "allOf:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- $ref: \'" + OPENAPI_URL + "#/components/schemas/Relationship\'")
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- type: object")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "properties:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "object:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "type: string")
    depth_level -= 2
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "required:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- object")

    depth_level = 2
    
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "IsPartOf:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "description: NGSI-LD Relationship Type. A hierarchical relationship.")
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "additionalProperties: false")
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "allOf:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- $ref: \'" + OPENAPI_URL + "#/components/schemas/Relationship\'")
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- type: object")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "properties:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "object:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "type: string")
    depth_level -= 2
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "required:")
    depth_level += 1
    fd.write('\n' + INDENTATION_BLOCK * depth_level + "- object")

    fd.close()