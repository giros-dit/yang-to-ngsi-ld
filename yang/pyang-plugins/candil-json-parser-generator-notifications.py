'''
pyang plugin -- CANDIL JSON Parser Generator for telemetry notifications received from a gNMI Subscription RPC.

Given one or several YANG modules, it dynamically generates the code of an JSON parser
that is able to read data modeled by these modules and is also capable of creating
instances of Pydantic classes from the NGSI-LD-backed OpenAPI generation.

Version: 1.0.3.

Author: Networking and Virtualization Research Group (GIROS DIT-UPM) -- https://dit.upm.es/~giros
'''

import optparse
import pdb
import re
import sys
import json

from pyang import plugin
from pyang import statements

### PLUGIN CONSTANTS ###

# Reading modes for input JSON data.
INPUT_MODE_FILE = "file" # -> Input JSON data filepath is specified as an invocation argument.
INPUT_MODE_KAFKA = "kafka" # -> Input JSON data is read from a Kafka topic.
    
# Writing modes for output dictionary buffers.
OUTPUT_MODE_PRINT = "print" # -> Output dictionary buffers are printed to stdout (terminal).
OUTPUT_MODE_FILE = "file" # -> Output dictionary buffers are written to a file.
OUTPUT_MODE_KAFKA = "kafka" # -> Output dictionary buffers are written to a Kafka topic.

PARENT_YANG_MODULE = "" # -> Parent YANG module
ENTITY_TYPE_LIST = [] # -> It includes all the different types of entities generated throughout all the YANG modules that are processed

### --- ###

def pyang_plugin_init():
    plugin.register_plugin(CandilJsonParserGeneratorPlugin())

class CandilJsonParserGeneratorPlugin(plugin.PyangPlugin):
    def __init__(self):
        plugin.PyangPlugin.__init__(self, 'candil-json-parser-generator-notifications')

    def add_output_format(self, fmts):
        self.multiple_modules = True
        fmts['candil-json-parser-generator-notifications'] = self
    
    def add_opts(self, optparser):
        optlist = [
            optparse.make_option('--candil-json-parser-generator-notifications-help', dest='candil_json_parser_generator_notifications_help', action='store_true', help='Prints help and usage.'),
            optparse.make_option('--candil-json-parser-generator-notifications-input-mode', dest='candil_json_parser_generator_notifications_input_mode', action='store', help='Defines the input mode for the JSON parser.'),
            optparse.make_option('--candil-json-parser-generator-notifications-output-mode', dest='candil_json_parser_generator_notifications_output_mode', action='store', help='Defines the output mode for the JSON parser.'),
            optparse.make_option('--candil-json-parser-generator-notifications-kafka-server', dest='candil_json_parser_generator_notifications_kafka_server', action='store', help='Only when using Kafka, specifies the endpoint of the server that the JSON parser will use.'),
            optparse.make_option('--candil-json-parser-generator-notifications-kafka-input-topic', dest='candil_json_parser_generator_notifications_kafka_input_topic', action='store', help='Only when using Kafka, specifies the input topic that the JSON parser will use.'),
            optparse.make_option('--candil-json-parser-generator-notifications-kafka-output-topic', dest='candil_json_parser_generator_notifications_kafka_output_topic', action='store', help='Only when using Kafka, specifies the output topic that the JSON parser will use.'),
            optparse.make_option('--candil-json-parser-generator-notifications-combined-mode', dest='candil_json_parser_generator_notifications_combined_mode', action='store', help='Combine dictionary buffers by means of id and type fields.')
        ]
        g = optparser.add_option_group('CANDIL JSON Parser Generator specific options')
        g.add_options(optlist)

    def setup_ctx(self, ctx):
        if ctx.opts.candil_json_parser_generator_notifications_help:
            print_help()
            sys.exit(0)

    def setup_fmt(self, ctx):
        ctx.implicit_errors = False

    def emit(self, ctx, modules, fd):
        generate_python_json_parser_code(ctx, modules, fd)

def print_help():
    '''
    Prints execution help.
    '''
    print('''
Pyang plugin - CANDIL JSON Parser Generator (candil-json-parser-generator-notifications).
Given one or several YANG modules, this plugin generates the Python code of an JSON parser
that is able to read data modeled by these YANG modules and is also able to generate
the data structures (dictionary buffers) of the identified NGSI-LD Entities.

Usage:
pyang -f candil-json-parser-generator-notifications [OPTIONS] <base_module.yang> [augmenting_module_1.yang] [augmenting_module_2.yang] ... [augmenting_module_N.yang] [> <output_file.py>]

OPTIONS:
    --candil-json-parser-generator-notifications-input-mode=MODE --> Defines where the JSON parser will read input JSON data from. Valid values: file, kafka.
    --candil-json-parser-generator-notifications-output-mode=MODE --> Defines where the JSON parser will output dictionary buffers to. Valid values: file, print or kafka.
    --candil-json-parser-generator-notifications-kafka-server=SOCKET --> Only when using Kafka, specifies the socket (<ip_or_hostname>:<port>) where the Kafka server is reachable to the JSON parser.
    --candil-json-parser-generator-notifications-kafka-input-topic=TOPIC --> Only when using Kafka for the input mode, specifies the name of the topic where the JSON parser will read input JSON data from.
    --candil-json-parser-generator-notifications-kafka-output-topic=TOPIC --> Only when using Kafka for the output mode, specifies the name of the topic where the JSON parser will output dictionary buffers to.
    --candil-json-parser-generator-notifications-combine-mode=ON --> Combine dictionary buffers by means of id and type fields.
    ''')
          
def generate_python_json_parser_code(ctx, modules, fd):
    '''
    Processes YANG modules and generates the corresponding Python JSON parser code for data modeled by these YANG modules.
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

    # NOTE: NGSI-LD types are Python types (as per this particular implementation).
    BASE_YANG_TYPES_TO_NGSI_LD_TYPES = {
        'int8': 'Integer',
        'int16': 'Integer',
        'int32': 'Integer',
        'int64': 'Integer',
        'uint8': 'Integer',
        'uint16': 'Integer',
        'uint32': 'Integer',
        'uint64': 'Integer',
        'decimal64': 'Number',
        'string': 'String',
        'boolean': 'Boolean',
        'enumeration': 'String',
        'bits': 'String[]',
        'binary': 'String',
        'empty': 'String',
        'union': 'String',
        'leafref': 'String'
    }

    INDENTATION_BLOCK = '    '

    BASE_IMPORT_STATEMENTS = [
        'import json\n',
        'import numpy as np\n',
        'from collections import defaultdict'
    ]

    FILE_IMPORT_STATEMENTS = [
        'import sys'
    ]

    KAFKA_INPUT_IMPORT_STATEMENTS = [
        'from kafka import KafkaConsumer'
    ]

    KAFKA_OUTPUT_IMPORT_STATEMENTS = [
        'from kafka import KafkaProducer'
    ]

    READING_INSTRUCTIONS_FILE = [
        'json_payload = sys.argv[1]\n',
        'dict_buffers = []\n',
        '\n',
        'with open(json_payload) as f:\n',
        INDENTATION_BLOCK + 'data = json.load(f)'
    ]

    if (ctx.opts.candil_json_parser_generator_notifications_kafka_server is not None) and \
        (ctx.opts.candil_json_parser_generator_notifications_kafka_input_topic is not None):
        READING_INSTRUCTIONS_KAFKA = [
            'dict_buffers = []\n',
            '\n',
            'consumer = KafkaConsumer(\'' + ctx.opts.candil_json_parser_generator_notifications_kafka_input_topic + '\', bootstrap_servers=[\'' + ctx.opts.candil_json_parser_generator_notifications_kafka_server + '\'], value_deserializer=lambda x: json.loads(x.decode(\'utf-8\')))\n',
            'while True:\n',
            INDENTATION_BLOCK + 'for message in consumer:\n',
            2 * INDENTATION_BLOCK + 'data = message.value'
        ]
        
    WRITING_COMBINED_BUFFER_FILE = [
        'dict_buffer_combinated = defaultdict(dict)\n',
        'for dict_buffer in dict_buffers:\n',
        INDENTATION_BLOCK + 'key = (dict_buffer["id"], dict_buffer["type"])\n',
        INDENTATION_BLOCK + 'if key not in dict_buffer_combinated:\n',
        2 * INDENTATION_BLOCK + 'dict_buffer_combinated[key] = dict_buffer\n',
        INDENTATION_BLOCK + 'else:\n',
        2 * INDENTATION_BLOCK + 'dict_buffer_combinated[key].update(dict_buffer)\n',
        'dict_buffers = list(dict_buffer_combinated.values())\n'
    ]

    WRITING_COMBINED_BUFFER_KAFKA = [
        2 * INDENTATION_BLOCK +'dict_buffer_combinated = defaultdict(dict)\n',
        2 * INDENTATION_BLOCK + 'for dict_buffer in dict_buffers:\n',
        3 * INDENTATION_BLOCK + 'key = (dict_buffer["id"], dict_buffer["type"])\n',
        3 * INDENTATION_BLOCK + 'if key not in dict_buffer_combinated:\n',
        4 * INDENTATION_BLOCK + 'dict_buffer_combinated[key] = dict_buffer\n',
        3 * INDENTATION_BLOCK + 'else:\n',
        4 * INDENTATION_BLOCK + 'dict_buffer_combinated[key].update(dict_buffer)\n',
        2 * INDENTATION_BLOCK + 'dict_buffers = list(dict_buffer_combinated.values())\n'
    ]

    WRITING_INSTRUCTIONS_PRINT = [
        'print(json.dumps(dict_buffers[::-1], indent=4))\n',
        'dict_buffers.clear()'
    ]

    WRITING_INSTRUCTIONS_FILE = [
        'output_file = open(\"dict_buffers_notifications.json\", \'w\')\n',
        'output_file.write(json.dumps(dict_buffers[::-1], indent=4))\n',
        'output_file.close()\n',
        'dict_buffers.clear()'
    ]

    if (ctx.opts.candil_json_parser_generator_notifications_kafka_server is not None) and \
        (ctx.opts.candil_json_parser_generator_notifications_kafka_output_topic is not None):
        WRITING_INSTRUCTIONS_KAFKA = [
            2 * INDENTATION_BLOCK + 'producer = KafkaProducer(bootstrap_servers=[\'' + ctx.opts.candil_json_parser_generator_notifications_kafka_server + '\'])\n',
            2 * INDENTATION_BLOCK + 'producer.send(\'' + ctx.opts.candil_json_parser_generator_notifications_kafka_output_topic + '\', value=json.dumps(dict_buffers[::-1], indent=4).encode(\'utf-8\'))\n',
            2 * INDENTATION_BLOCK + 'producer.flush()\n',
            2 * INDENTATION_BLOCK + 'dict_buffers.clear()'
        ]

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
            if (element_keyword == 'leaf') or (element_keyword == 'leaf-list'):
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
                        if (typedef_type not in YANG_PRIMITIVE_TYPES) and ('-ref' not in typedef_type ) and (typedef_type != 'leafref'):
                            primitive_typedefs_dict[typedef_name] = defined_typedefs_dict[typedef_type]
                        else:
                            primitive_typedefs_dict[typedef_name] = typedef_type
        return primitive_typedefs_dict
    
    def yang_to_ngsi_ld_types_conversion(element_type: str, typedefs_dict: dict) -> str:
        '''
        Auxiliary function.
        Returns the NGSI-LD type (in Python implementation) given the YANG type of an element/node in a YANG module.
        '''
        if (element_type == 'identityref'):
            return 'String'
        else:
            base_yang_type = ''
            if (typedefs_dict.get(element_type) is not None):
                base_yang_type = typedefs_dict[element_type]
            else:
                base_yang_type = element_type
            return BASE_YANG_TYPES_TO_NGSI_LD_TYPES[base_yang_type]

    def element_text_type_formatting(ngsi_ld_type: str, element_text: str) -> str:
        '''
        Auxiliary function.
        Returns a String with the Python code that implements the correct formatting for the value/text of an element in
        an JSON file given the NGSI-LD type of that particular element.
        '''
        if (ngsi_ld_type == 'String'):
            return element_text
        elif (ngsi_ld_type == 'String[]'):
            return 'list(' + element_text + ')'
        elif (ngsi_ld_type == 'Integer'):
            return 'int(' + element_text + ')'
        elif (ngsi_ld_type == 'Number'):
            return 'float(' + element_text + ')'
        elif (ngsi_ld_type == 'Boolean'):
            return 'eval(str(' + str(element_text) + ').capitalize())'
    
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
    
    def is_config_element(element) -> bool:
        '''
        Auxiliary function.
        Checks if an element is a YANG config element.
        '''
        result = False
        if (element.i_config == True):
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
    
    def is_property(element, typedefs_dict: dict) -> bool:
        '''
        Auxiliary function.
        Checks if an element matches the YANG to NGSI-LD translation convention for a Property.
        '''
        result = False
        if (element.keyword in ['leaf-list', 'leaf']):
            element_type = str(element.search_one('type')).replace('type ', '').split(':')[-1]
            if (element_type in YANG_PRIMITIVE_TYPES) or \
                ((typedefs_dict.get(element_type) is not None) and (('-ref' not in typedefs_dict.get(element_type)) and (typedefs_dict.get(element_type) != 'leafref'))):
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
                ((typedefs_dict.get(element_type) is not None) and (('-ref' in typedefs_dict.get(element_type) or (typedefs_dict.get(element_type) == 'leafref')))):
                result = True
        return result

    def get_yang_module_data_nodes(element, yang_data_nodes_list: list) -> list:
        '''
        Auxiliary recursive function.
        Recursively gets all YANG data nodes.
        '''
        if element.keyword in ['container', 'list', 'choice']:
            subelements = element.i_children
            if (subelements is not None):
                for subelement in subelements:
                    if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords) and (is_deprecated(subelement) == False):  
                        if str(subelement.keyword) == 'choice':
                            yang_data_nodes_list.append(subelement.arg)
                            cases = subelement.i_children
                            if (cases is not None):
                                for case in cases:
                                    if (case is not None) and (case.keyword in statements.data_definition_keywords) and (is_deprecated(case) == False):
                                        case_subelements = case.i_children
                                        if (case_subelements is not None):
                                            for case_subelement in case_subelements:
                                                if (case_subelement is not None) and (case_subelement.keyword in statements.data_definition_keywords):
                                                    yang_data_nodes_list.append(case_subelement.arg)
                                                    get_yang_module_data_nodes(case_subelement, yang_data_nodes_list)
                        elif str(subelement.keyword) in ['container', 'list']:
                            yang_data_nodes_list.append(subelement.arg) 
                            get_yang_module_data_nodes(subelement, yang_data_nodes_list)
                        else:
                            yang_data_nodes_list.append(subelement.arg) 
        elif element.keyword in ['leaf-list', 'leaf']:
            yang_data_nodes_list.append(element.arg) 
        
        return yang_data_nodes_list
    
    def generate_parser_code(element, parent_element_arg, entity_path: str, camelcase_entity_path: str, depth_level: int, typedefs_dict: dict, transition_element, modules_name: list, position: int):
        '''
        Auxiliary function.
        Recursively generates the JSON parser code.
        '''
        global PARENT_YANG_MODULE
        global ENTITY_TYPE_LIST
        camelcase_element_arg = to_camelcase(str(element.keyword), str(element.arg))
        yang_module_namespace = str(element.i_module.search_one('namespace').arg)
        yang_module_name = str(element.i_module.arg)

        if len(modules_name) == 0:
            PARENT_YANG_MODULE = yang_module_name
            modules_name.append(PARENT_YANG_MODULE)
        
        current_path = ''
        if (entity_path is None):
            current_path = str(element.arg) + '_'
        else:
            current_path = entity_path + str(element.arg) + '_'
        
        ### ENCLOSING CONTAINER IDENTIFICATION ###
        if (is_enclosing_container(element) == True) and (is_deprecated(element) == False):
            subelements = element.i_children
            first_subelement = True
            if (subelements is not None):
                for subelement in subelements:
                    if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                        if parent_element_arg is None:
                            fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if parent_path[' + str(position) + '] == "' + str(yang_module_name) + ':' + str(element.arg) + '" or ' + 'parent_path[' + str(position) + '] == "' + str(element.arg) + '":')
                            depth_level += 1
                            position += 1
                            generate_parser_code(subelement, None, None, None, depth_level, typedefs_dict, element, modules_name, position)
                        else:
                            current_camelcase_path = ''
                            if (camelcase_entity_path is None):
                                current_camelcase_path = to_camelcase(str(element.keyword), str(subelement.arg))
                            else:
                                current_camelcase_path = camelcase_entity_path + to_camelcase(str(element.keyword), str(element.arg)) 
                            if subelement.keyword == 'container':
                                if first_subelement == True:
                                    if yang_module_name != PARENT_YANG_MODULE:
                                        for module_name in modules_name:
                                            if parent_element_arg == module_name.split(":")[-1]:
                                                modules_name.append(yang_module_name + ":" + element.arg)
                                        if str(yang_module_name + ":" + element.arg) not in modules_name:
                                            modules_name.append(yang_module_name + ":" + element.arg)
                                            fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if parent_path[' + str(position) + '] == "' + str(yang_module_name) + ':' + str(element.arg) + '" or ' + 'parent_path[' + str(position) + '] == "' + str(element.arg) + '":')
                                        else:
                                            fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if parent_path[' + str(position) + '] == "' + str(element.arg) + '":')
                                    else:
                                        fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if parent_path[' + str(position) + '] == "' + str(element.arg) + '":')
                                    first_subelement = False

                                depth_level += 1
                                position += 1
                                generate_parser_code(subelement, element.arg, entity_path, current_camelcase_path, depth_level, typedefs_dict, None, modules_name, position)
                            elif subelement.keyword == 'list':
                                if first_subelement == True:
                                    if yang_module_name != PARENT_YANG_MODULE:
                                        for module_name in modules_name:
                                            if parent_element_arg == module_name.split(":")[-1]:
                                                modules_name.append(yang_module_name + ":" + element.arg)
                                                modules_name.append(yang_module_name + ":" + subelement.arg)
                                        if str(yang_module_name + ":" + element.arg) not in modules_name:
                                            modules_name.append(yang_module_name + ":" + element.arg)
                                            modules_name.append(yang_module_name + ":" + subelement.arg)
                                            fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if parent_path[' + str(position) + '] == "' + str(yang_module_name) + ':' + str(element.arg) + '" or ' + 'parent_path[' + str(position) + '] == "' + str(element.arg) + '":')
                                        else:
                                            fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if parent_path[' + str(position) + '] == "' + str(element.arg) + '":')
                                    else:
                                        fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if parent_path[' + str(position) + '] == "' + str(element.arg) + '":')
                                    first_subelement = False

                                depth_level += 1  
                                position += 1                              
                                generate_parser_code(subelement, parent_element_arg, entity_path, current_camelcase_path, depth_level, typedefs_dict, element, modules_name, position)

                        
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
                    actual_position = 0
                    if(transition_element is not None):
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if parent_path[' + position + '] == "' + str(transition_element.arg) + '" or ' + 'parent_path[' + str(position) + '] == "' + str(yang_module_name) + ':' + str(transition_element.arg) + '":')
                        depth_level += 1
                        actual_position = position
                        position += 1
                    else:
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if parent_path[' + str(position) + '] == "' + str(element.arg) + '" or ' + 'parent_path[' + str(position) + '] == "' + str(yang_module_name) + ':' + str(element.arg) + '":')
                        depth_level += 1
                        actual_position = position
                        position += 1
                        
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer = {}')

                    if element.search_one('key') != None:
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if \"' + str(current_path + element.search_one('key').arg).replace('-', '_') + '\" in iteration_keys:')
                        depth_level += 1
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"id\"] = \"urn:ngsi-ld:' + current_camelcase_path + ':\" + source + ' + '\":" +  iteration_keys.get(\"' + str(current_path + element.search_one('key').arg) + '\"' + ')')
                        depth_level -= 1
                    else: 
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"id\"] = \"urn:ngsi-ld:' + current_camelcase_path + ':\" + source')

                    fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"type\"] = \"' + current_camelcase_path + '\"')
                    depth_level -= 1
                    subelements = element.i_children
                    if (subelements is not None):
                        for subelement in subelements:
                            if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                                generate_parser_code(subelement, element.arg, current_path, current_camelcase_path, depth_level, typedefs_dict, None, modules_name, position)
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "if len(parent_path) - 1 == " + str(actual_position) + ":")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + 'dict_buffers.append(' + current_path.replace('-', '_') + 'dict_buffer)')
                elif element.keyword in ['list']:
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if parent_path[' + str(position) + '] == "' + str(element.arg) + '" or ' + 'parent_path[' + str(position) + '] == "' + str(yang_module_name) + ':' + str(element.arg) + '":')
                    actual_position = position
                    position += 1      
                    depth_level += 1 
                        
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer = {}')
                    
                    if element.search_one('key') != None:
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if \"' + str(current_path + element.search_one('key').arg).replace('-', '_') + '\" in iteration_keys:')
                        depth_level += 1
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"id\"] = \"urn:ngsi-ld:' + current_camelcase_path + ':\" + source + ' + '\":" +  iteration_keys.get(\"' + str(current_path + element.search_one('key').arg) + '\"' + ')')
                        depth_level -= 1
                    else: 
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"id\"] = \"urn:ngsi-ld:' + current_camelcase_path + ':\" + source')
                    
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"type\"] = \"' + current_camelcase_path + '\"')
                    depth_level -= 1
                    subelements = element.i_children
                    if (subelements is not None):
                        for subelement in subelements:
                            if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                                generate_parser_code(subelement, element.arg, current_path, current_camelcase_path, depth_level, typedefs_dict, None, modules_name, position)
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "if len(parent_path) - 1 == " + str(actual_position) + ":")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + 'dict_buffers.append(' + current_path.replace('-', '_') + 'dict_buffer)')
            else: # 2nd level Entity onwards.
                if element.keyword in ['container']:
                    if yang_module_name != PARENT_YANG_MODULE:
                        for module_name in modules_name:
                            if parent_element_arg == module_name.split(":")[-1]:
                                modules_name.append(yang_module_name + ":" + element.arg)
                        if str(yang_module_name + ":" + element.arg) not in modules_name:
                            modules_name.append(yang_module_name + ":" + element.arg)
                            fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if parent_path[' + str(position) + '] == "' + str(yang_module_name) + ':' + str(element.arg) + '":')
                            depth_level += 1
                            actual_position = position
                            position += 1 
                        else:
                            fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if parent_path[' + str(position) + '] == "' + str(element.arg) + '":')    
                            depth_level += 1
                            actual_position = position
                            position += 1 
                    else:
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if parent_path[' + str(position) + '] == "' + str(element.arg) + '":')
                        depth_level += 1
                        actual_position = position
                        position += 1 

                    fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer = {}')

                    if element.search_one('key') != None:
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if \"' + str(current_path + element.search_one('key').arg).replace('-', '_') + '\" in iteration_keys:')
                        depth_level += 1
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"id\"] = \"urn:ngsi-ld:' + current_camelcase_path + ':\" + source + ' + '\":" + iteration_keys.get(\"' + str(current_path + element.search_one('key').arg) + '\"' + ')')
                        depth_level -= 1
                    else:
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"id\"] = \"urn:ngsi-ld:' + current_camelcase_path + ':\" + ":".join(' + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"].split(\":\")[3:])')
                                        
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"type\"] = \"' + current_camelcase_path + '\"')
                    
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if len(parent_path) - 1 == ' + str(actual_position) + " or len(parent_path) - 1 == " + str(actual_position + 1) + ":")
                    depth_level += 1

                    fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"isPartOf\"] = {}')
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"isPartOf\"][\"type\"] = \"Relationship\"')
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"isPartOf\"][\"object\"] = ' + current_path.replace(str(element.arg) + '_', '').replace('-', '_') +  'dict_buffer[\"id\"]')
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"isPartOf\"][\"observedAt\"] = observed_at')
                    
                    subelements = element.i_children
                    if (subelements is not None):
                        for subelement in subelements:
                            if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                                generate_parser_code(subelement, element.arg, current_path, current_camelcase_path, depth_level, typedefs_dict, None, modules_name, position)
                    
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "if len(parent_path) - 1 == " + str(actual_position) + ":")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + 'dict_buffers.append(' + current_path.replace('-', '_') + 'dict_buffer)')
                elif element.keyword in ['list']:
                    if yang_module_name != PARENT_YANG_MODULE:
                        for module_name in modules_name:
                            if parent_element_arg == module_name.split(":")[-1]:
                                modules_name.append(yang_module_name + ":" + element.arg)
                        if str(yang_module_name + ":" + element.arg) not in modules_name:
                            modules_name.append(yang_module_name + ":" + element.arg)
                            fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if parent_path[' + str(position) + '] == "' + str(yang_module_name) + ':' + str(element.arg) + '":')
                            depth_level += 1
                            actual_position = position
                            position += 1 
                        else:
                            fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if parent_path[' + str(position) + '] == "' + str(element.arg) + '":')    
                            depth_level += 1
                            actual_position = position
                            position += 1 
                    else:
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if parent_path[' + str(position) + '] == "' + str(element.arg) + '":')
                        depth_level += 1
                        actual_position = position
                        position += 1 

                    fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer = {}')

                    if element.search_one('key') != None:
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if \"' + str(current_path + element.search_one('key').arg).replace('-', '_') + '\" in iteration_keys:')
                        depth_level += 1
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"id\"] = \"urn:ngsi-ld:' + current_camelcase_path + ':\" + source + ' + '\":" + iteration_keys.get(\"' + str(current_path + element.search_one('key').arg) + '\"' + ')')
                        depth_level -= 1
                    else:
                        fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"id\"] = \"urn:ngsi-ld:' + current_camelcase_path + ':\" + ":".join(' + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"].split(\":\")[3:])')
 
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"type\"] = \"' + current_camelcase_path + '\"')
                    
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if len(parent_path) - 1 == ' + str(actual_position) + " or len(parent_path) - 1 == " + str(actual_position + 1) + ":")
                    depth_level += 1

                    fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"isPartOf\"] = {}')
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"isPartOf\"][\"type\"] = \"Relationship\"')
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"isPartOf\"][\"object\"] = ' + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"]')
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"isPartOf\"][\"observedAt\"] = observed_at')
                    
                    subelements = element.i_children
                    if (subelements is not None):
                        for subelement in subelements:
                            if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                                generate_parser_code(subelement, element.arg, current_path, current_camelcase_path, depth_level, typedefs_dict, None, modules_name, position)
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + "if len(parent_path) - 1 == " + str(actual_position) + ":")
                    depth_level += 1
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + 'dict_buffers.append(' + current_path.replace('-', '_') + 'dict_buffer)')
        ### --- ###

        ### YANG CHOICE IDENTIFICATION: IT CONTAINS NGSI-LD PROPERTIES ###
        elif (is_choice(element) == True) and (is_deprecated(element) == False):
            current_path = current_path.replace(str(element.arg) + '_', '')
            '''
            Children of "choice" elements are "case" subelements.
            These subelements have "leaf" or "leaf-list" children, which match
            for NGSI-LD properties. Therefore, we need to deep dive two times in the
            element tree.
            '''
            subelements = element.i_children
            if (subelements is not None):
                for subelement in subelements:
                    if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                        subelements = subelement.i_children
                        if (subelements is not None):
                            for subelement in subelements:
                                if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                                    generate_parser_code(subelement, parent_element_arg, current_path, camelcase_entity_path, depth_level, typedefs_dict)
        ### --- ###
                                    
        ### NGSI-LD PROPERTY IDENTIFICATION ###
        elif (is_property(element, typedefs_dict) == True) and (is_deprecated(element) == False):
            fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if child_node == "' + str(element.arg) + '":')
            ngsi_ld_type = yang_to_ngsi_ld_types_conversion(str(element.search_one('type')).replace('type ', '').split(":")[-1], typedefs_dict)
            text_format = element_text_type_formatting(ngsi_ld_type, 'element_text')

            if ('name'.casefold() in str(element.arg)) or ('id'.casefold() in str(element.arg).casefold()):
                fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK + 'if ' + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"].split(\":\")[-1]' + ' != ' + text_format + ":")  
                fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK + INDENTATION_BLOCK + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"] = ' + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"] + ":" + ' + text_format)
            if ('index'.casefold() == str(element.arg)):
                text_format = str(text_format)
                fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK + 'if ' + '\".\"' + ' + str(element_text) not in ' + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"].split(\":\")[-1]:')
                fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK + INDENTATION_BLOCK + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"] = ' + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"] + ' + '\".\"' + ' + str(element_text)')
            
            fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK + current_path.replace('_' + str(element.arg) + '_', '_', 1).replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"] = {}')
            fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK + current_path.replace('_' + str(element.arg) + '_', '_', 1).replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"type\"] = \"Property\"')
            fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK + current_path.replace('_' + str(element.arg) + '_', '_', 1).replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"value\"] = ' + text_format)
            fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK + current_path.replace('_' + str(element.arg) + '_', '_', 1).replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"observedAt\"] = observed_at')
            config = is_config_element(element)
            if config == True:
                fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK + current_path.replace('_' + str(element.arg) + '_', '_', 1).replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"datasetId\"] = \"urn:ngsi-ld:configuration\"')
            else:
                fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK + current_path.replace('_' + str(element.arg) + '_', '_', 1).replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"datasetId\"] = \"urn:ngsi-ld:operational\"')
        ### --- ###
        
        ### NGSI-LD RELATIONSHIP IDENTIFICATION ###
        elif (is_relationship(element, typedefs_dict) == True) and (is_deprecated(element) == False):

            current_camelcase_path = ''

            if (yang_data_nodes_list.count(str(element.arg))) > 1 or (str(element.arg) == 'type'):
                current_camelcase_path = camelcase_entity_path + str(re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), element.arg.capitalize()))
            else:
                current_camelcase_path = str(re.sub(r'(-)(\w)', lambda m: m.group(2).upper(), element.arg.capitalize()))

            pointer = element.i_leafref_ptr[0]
            pointer_parent = pointer.parent
            camelcase_pointer_parent = to_camelcase(str(pointer_parent.keyword), str(pointer_parent.arg))
            
            matches = [] # Best match is always the first element appended into the list: index 0.
            for camelcase_entity in ENTITY_TYPE_LIST:
                if camelcase_pointer_parent == camelcase_entity_path + camelcase_entity:
                    matches.append(camelcase_entity)

            if len(matches) == 0:
                childs = element.parent.i_children
                matched_childs = 0
                if (childs is not None) and (camelcase_entity_path + camelcase_pointer_parent) != current_camelcase_path:
                    has_childs = True
                    element_aux = element
                    iterations = 0
                    while has_childs == True:
                        for child in childs:
                            if child.arg == str(pointer_parent.arg):
                                matched_childs += 1
                                break
                        
                        if matched_childs == 0:
                            for child in childs:
                                    if is_entity(child) == True:
                                        subchilds = child.i_children
                                        if (subchilds is not None):
                                            iterations += 1
                                            for subchild in subchilds:
                                                if subchild.arg == str(pointer_parent.arg):
                                                    matched_childs += 1
                        
                        if matched_childs > 0:    
                            if iterations > 0:
                                for camelcase_entity in ENTITY_TYPE_LIST:
                                    
                                    if camelcase_pointer_parent == camelcase_entity or camelcase_pointer_parent in camelcase_entity:
                                        matches.append(camelcase_entity)

                                if len(matches) == 0:
                                    relationship_camelcase_path = camelcase_pointer_parent
                                else:
                                    relationship_camelcase_path = matches[0]  

                            else:
                                relationship_camelcase_path = camelcase_entity_path + camelcase_pointer_parent
                                ENTITY_TYPE_LIST.append(relationship_camelcase_path)
                            
                            has_childs = False
                        else:
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
                    for camelcase_entity in ENTITY_TYPE_LIST:
                        if camelcase_pointer_parent == camelcase_entity or camelcase_pointer_parent in camelcase_entity:
                            matches.append(camelcase_entity)

                    if len(matches) == 0:
                        relationship_camelcase_path = camelcase_pointer_parent
                    else:
                        relationship_camelcase_path = matches[0]
            else:
                relationship_camelcase_path = matches[0]

            ngsi_ld_type = yang_to_ngsi_ld_types_conversion(str(element.search_one('type')).replace('type ', '').split(":")[-1], typedefs_dict)
            text_format = element_text_type_formatting(ngsi_ld_type, 'element_text')

            fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if len(parent_path) - 1 == ' + str(position-1) + " or len(parent_path) - 1 == " + str(position) + ":")
            depth_level += 1

            if ('name'.casefold() in str(element.arg)) or ('id'.casefold() in str(element.arg).casefold()):
                fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if ' + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"].split(\":\")[-1]' + ' != ' + text_format + ":")  
                fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"] = ' + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"] + ":" + ' + text_format)
            if ('index'.casefold() == str(element.arg)):
                text_format = str(text_format)
                fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if ' + '\".\"' + ' + str(element_text) not in ' + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"].split(\":\")[-1]:') 
                fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"] = ' + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"] + ' + '\".\"' + ' + str(element_text)')
            if ('interface'.casefold() == str(element.arg)):
                text_format = str(text_format)
                fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if ' + entity_path.replace('-', '_') + 'dict_buffer[\"id\"].split(\":\")[-1]' + ' != ' + text_format + ":") 
                fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK + entity_path.replace('-', '_') + 'dict_buffer[\"id\"] = ' + entity_path.replace('-', '_') + 'dict_buffer[\"id\"] + ":" + ' + text_format) 
            if ('subinterface'.casefold() == str(element.arg)):
                text_format = str(text_format)
                fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if ' + '\".\"' + ' + str(element_text) not in ' + entity_path.replace('-', '_') + 'dict_buffer[\"id\"].split(\":\")[-1]:')  
                fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK + entity_path.replace('-', '_') + 'dict_buffer[\"id\"] = ' + entity_path.replace('-', '_') + 'dict_buffer[\"id\"] + ' + '\".\"' + ' + str(element_text)')
            if ('ip'.casefold() == str(element.arg)):
                fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if ' + '\":\"' + ' in element_text:')
                fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK + 'element_text = element_text.replace(\":\",\".\")')
                fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if ' + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"].split(\":\")[-1]' + ' != ' + text_format + ":")  
                fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"] = ' + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"] + ' + '\":\"' + ' + ' + text_format)
            
            if ('interface'.casefold() == str(element.arg) or 'subinterface'.casefold() == str(element.arg)):
                fd.write('\n' + INDENTATION_BLOCK * depth_level + entity_path.replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"] = {}')
                fd.write('\n' + INDENTATION_BLOCK * depth_level + entity_path.replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"type\"] = \"Relationship\"')
                fd.write('\n' + INDENTATION_BLOCK * depth_level + entity_path.replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"object\"] = \"urn:ngsi-ld:' + relationship_camelcase_path + ':\" + ":".join(' + entity_path.replace('-', '_') + 'dict_buffer[\"id\"].split(\":\")[3:])')
                fd.write('\n' + INDENTATION_BLOCK * depth_level + entity_path.replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"observedAt\"] = observed_at')
                config = is_config_element(element)
                if config == True:
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + entity_path.replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"datasetId\"] = \"urn:ngsi-ld:configuration\"')
                else:
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + entity_path.replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"datasetId\"] = \"urn:ngsi-ld:operational\"')
            else:
                fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('_' + str(element.arg) + '_', '_', 1).replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"] = {}')
                fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('_' + str(element.arg) + '_', '_', 1).replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"type\"] = \"Relationship\"')
                fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('_' + str(element.arg) + '_', '_', 1).replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"object\"] = \"urn:ngsi-ld:' + relationship_camelcase_path + ':\" + ":".join(' + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"].split(\":\")[3:])')
                fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('_' + str(element.arg) + '_', '_', 1).replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"observedAt\"] = observed_at')
                config = is_config_element(element)
                if config == True:
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('_' + str(element.arg) + '_', '_', 1).replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"datasetId\"] = \"urn:ngsi-ld:configuration\"')
                else:
                    fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('_' + str(element.arg) + '_', '_', 1).replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"datasetId\"] = \"urn:ngsi-ld:operational\"')
        ### --- ###

    
    ### --- ###

    # Generate import statements (standard Python libraries and such):
    for import_statement in BASE_IMPORT_STATEMENTS:
        fd.write(import_statement)
    fd.write('\n')
    if (ctx.opts.candil_json_parser_generator_notifications_input_mode == INPUT_MODE_FILE) or \
        (ctx.opts.candil_json_parser_generator_notifications_output_mode == OUTPUT_MODE_FILE):
        for line in FILE_IMPORT_STATEMENTS:
            fd.write(line)
            fd.write('\n')
    if (ctx.opts.candil_json_parser_generator_notifications_input_mode == INPUT_MODE_KAFKA):
        for line in KAFKA_INPUT_IMPORT_STATEMENTS:
            fd.write(line)
            fd.write('\n')
    if (ctx.opts.candil_json_parser_generator_notifications_output_mode == OUTPUT_MODE_KAFKA):
        for line in KAFKA_OUTPUT_IMPORT_STATEMENTS:
            fd.write(line)
            fd.write('\n')

    fd.write('\n')

    # Generate reading instructions for the JSON parser (depending on the input mode):
    if (ctx.opts.candil_json_parser_generator_notifications_input_mode == INPUT_MODE_FILE):
        for line in READING_INSTRUCTIONS_FILE:
            fd.write(line)
    if (ctx.opts.candil_json_parser_generator_notifications_input_mode == INPUT_MODE_KAFKA):
        for line in READING_INSTRUCTIONS_KAFKA:
            fd.write(line)
    
    fd.write('\n')
    
    if (ctx.opts.candil_json_parser_generator_notifications_input_mode == INPUT_MODE_FILE):
        depth_level = 0
    if (ctx.opts.candil_json_parser_generator_notifications_input_mode == INPUT_MODE_KAFKA):
        depth_level = 2
    
    fd.write('\n' + depth_level * INDENTATION_BLOCK + "for item in data:")
    fd.write('\n' + depth_level * INDENTATION_BLOCK + INDENTATION_BLOCK + "parent_paths = []")
    fd.write('\n' + depth_level * INDENTATION_BLOCK + INDENTATION_BLOCK + "child_nodes = []")
    fd.write('\n' + depth_level * INDENTATION_BLOCK + INDENTATION_BLOCK + "values = []")
    fd.write('\n' + depth_level * INDENTATION_BLOCK + INDENTATION_BLOCK + "iteration_keys = {}")
    fd.write('\n' + depth_level * INDENTATION_BLOCK + INDENTATION_BLOCK + "for key, value in item[\'values\'].items():")
    fd.write('\n' + depth_level * INDENTATION_BLOCK + INDENTATION_BLOCK + INDENTATION_BLOCK + "parent_paths.append(key.split(\"/\")[1:-1])")
    fd.write('\n' + depth_level * INDENTATION_BLOCK + INDENTATION_BLOCK + INDENTATION_BLOCK + "child_nodes.append(key.split(\"/\")[-1])")
    fd.write('\n' + depth_level * INDENTATION_BLOCK + INDENTATION_BLOCK + INDENTATION_BLOCK + "values.append(value)")
    fd.write('\n' + depth_level * INDENTATION_BLOCK + INDENTATION_BLOCK + 'source = "-".join(item[\'tags\'][\'source\'].split("-")[1:-1]) + ":" + str(item[\'tags\'][\'source\'].split("-")[-1])')
    fd.write('\n' + depth_level * INDENTATION_BLOCK + INDENTATION_BLOCK + "timestamp_data = int(item[\'timestamp\'])")
    fd.write('\n' + depth_level * INDENTATION_BLOCK + INDENTATION_BLOCK + "datetime_ns = np.datetime64(timestamp_data, \'ns\')")
    fd.write('\n' + depth_level * INDENTATION_BLOCK + INDENTATION_BLOCK + "observed_at = str(datetime_ns.astype(\'datetime64[ms]\')) + \'Z\'")
    fd.write('\n' + depth_level * INDENTATION_BLOCK + INDENTATION_BLOCK + "for i_key, i_value in item[\'tags\'].items():")
    fd.write('\n' + depth_level * INDENTATION_BLOCK + INDENTATION_BLOCK + INDENTATION_BLOCK + "if i_key != \'source\' and i_key != \'subscription-name\':")
    fd.write('\n' + depth_level * INDENTATION_BLOCK + INDENTATION_BLOCK + INDENTATION_BLOCK + INDENTATION_BLOCK + "iteration_keys[" + 'i_key' + "] = " + 'i_value')

    fd.write('\n')

    fd.write('\n' + depth_level * INDENTATION_BLOCK + INDENTATION_BLOCK + "for element_text, child_node, parent_path in zip(values, child_nodes, parent_paths):")
             
    # Find typedefs, including those from modules in import sentences:
    typedef_modules = []
    position = 0
    for module in modules:
        typedef_modules.append(module)
        imports = module.search('import')
        for i in imports:
            submodule = ctx.get_module(i.arg)
            if submodule is not None:
                typedef_modules.append(submodule)
    typedef_modules = list(dict.fromkeys(typedef_modules)) # Delete duplicates.
    typedefs_dict = typedefs_discovering(typedef_modules)

    # Get all data nodes for the evaluated YANG modules
    yang_data_nodes_list = []
    for module in modules:
        elements = module.i_children
        if (elements is not None):
            for element in elements:
                if (element is not None) and (element.keyword in statements.data_definition_keywords):
                    yang_data_nodes_list.append(element.arg)
                    get_yang_module_data_nodes(element, yang_data_nodes_list)

    # Generate JSON parser code (element data retrieval and transformation to generate dictionary buffers):
    depth_level = 0
    for module in modules:
        elements = module.i_children
        if (elements is not None):
            if (ctx.opts.candil_json_parser_generator_notifications_input_mode == INPUT_MODE_FILE):
                depth_level = 2
            if (ctx.opts.candil_json_parser_generator_notifications_input_mode == INPUT_MODE_KAFKA):
                depth_level = 4
            for element in elements:
                if (element is not None) and (element.keyword in statements.data_definition_keywords):
                    generate_parser_code(element, None, None, None, depth_level, typedefs_dict, None, list(), position)
    
    fd.write('\n\n')

    if (ctx.opts.candil_json_parser_generator_notifications_combined_mode == "ON" and (ctx.opts.candil_json_parser_generator_notifications_output_mode == OUTPUT_MODE_FILE or ctx.opts.candil_json_parser_generator_notifications_output_mode == OUTPUT_MODE_PRINT)):
       for line in WRITING_COMBINED_BUFFER_FILE:
            fd.write(line)
    
    if (ctx.opts.candil_json_parser_generator_notifications_combined_mode == "ON" and ctx.opts.candil_json_parser_generator_notifications_output_mode == OUTPUT_MODE_KAFKA):
       for line in WRITING_COMBINED_BUFFER_KAFKA:
            fd.write(line)

    fd.write('\n')

    # Generate writing instructions for the JSON parser (depending on the output mode):
    if (ctx.opts.candil_json_parser_generator_notifications_output_mode == OUTPUT_MODE_FILE):
        for line in WRITING_INSTRUCTIONS_FILE:
            fd.write(line)
    if (ctx.opts.candil_json_parser_generator_notifications_output_mode == OUTPUT_MODE_PRINT):
        for line in WRITING_INSTRUCTIONS_PRINT:
            fd.write(line)
    if (ctx.opts.candil_json_parser_generator_notifications_output_mode == OUTPUT_MODE_KAFKA):
        for line in WRITING_INSTRUCTIONS_KAFKA:
            fd.write(line)
    
    fd.write('\n')
    fd.close()