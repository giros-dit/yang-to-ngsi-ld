'''
pyang plugin -- CANDIL XML Parser Generator.

Given one or several YANG modules, it dynamically generates the code of an XML parser
that is able to read data modeled by these modules and is also capable of creating
instances of Pydantic classes from the NGSI-LD-backed OpenAPI generation.

Version: 0.5.7.

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

# Reading modes for input XML data.
INPUT_MODE_FILE = "file" # -> Input XML data filepath is specified as an invocation argument.
INPUT_MODE_KAFKA = "kafka" # -> Input XML data is read from a Kafka topic.
    
# Writing modes for output dictionary buffers.
OUTPUT_MODE_PRINT = "print" # -> Output dictionary buffers are printed to stdout (terminal).
OUTPUT_MODE_FILE = "file" # -> Output dictionary buffers are written to a file.
OUTPUT_MODE_KAFKA = "kafka" # -> Output dictionary buffers are written to a Kafka topic.

### --- ###

def pyang_plugin_init():
    plugin.register_plugin(CandilXmlParserGeneratorPlugin())

class CandilXmlParserGeneratorPlugin(plugin.PyangPlugin):
    def __init__(self):
        plugin.PyangPlugin.__init__(self, 'candil-xml-parser-generator')

    def add_output_format(self, fmts):
        self.multiple_modules = True
        fmts['candil-xml-parser-generator'] = self
    
    def add_opts(self, optparser):
        optlist = [
            optparse.make_option('--candil-xml-parser-generator-help', dest='candil_xml_parser_generator_help', action='store_true', help='Prints help and usage.'),
            optparse.make_option('--candil-xml-parser-generator-input-mode', dest='candil_xml_parser_generator_input_mode', action='store', help='Defines the input mode for the XML parser.'),
            optparse.make_option('--candil-xml-parser-generator-output-mode', dest='candil_xml_parser_generator_output_mode', action='store', help='Defines the output mode for the XML parser.'),
            optparse.make_option('--candil-xml-parser-generator-kafka-server', dest='candil_xml_parser_generator_kafka_server', action='store', help='Only when using Kafka, specifies the endpoint of the server that the XML parser will use.'),
            optparse.make_option('--candil-xml-parser-generator-kafka-input-topic', dest='candil_xml_parser_generator_kafka_input_topic', action='store', help='Only when using Kafka, specifies the input topic that the XML parser will use.'),
            optparse.make_option('--candil-xml-parser-generator-kafka-output-topic', dest='candil_xml_parser_generator_kafka_output_topic', action='store', help='Only when using Kafka, specifies the output topic that the XML parser will use.')
        ]
        g = optparser.add_option_group('CANDIL XML Parser Generator specific options')
        g.add_options(optlist)

    def setup_ctx(self, ctx):
        if ctx.opts.candil_xml_parser_generator_help:
            print_help()
            sys.exit(0)

    def setup_fmt(self, ctx):
        ctx.implicit_errors = False

    def emit(self, ctx, modules, fd):
        generate_python_xml_parser_code(ctx, modules, fd)

def print_help():
    '''
    Prints execution help.
    '''
    print('''
Pyang plugin - CANDIL XML Parser Generator (candil-xml-parser-generator).
Given one or several YANG modules, this plugin generates the Python code of an XML parser
that is able to read data modeled by these YANG modules and is also able to generate
the data structures (dictionary buffers) of the identified NGSI-LD Entities.

Usage:
pyang -f candil-xml-parser-generator [OPTIONS] <base_module.yang> [augmenting_module_1.yang] [augmenting_module_2.yang] ... [augmenting_module_N.yang] [> <output_file.py>]

OPTIONS:
    --candil-xml-parser-generator-input-mode=MODE --> Defines where the XML parser will read input XML data from. Valid values: file, kafka.
    --candil-xml-parser-generator-output-mode=MODE --> Defines where the XML parser will output dictionary buffers to. Valid values: file, print or kafka.
    --candil-xml-parser-generator-kafka-server=SOCKET --> Only when using Kafka, specifies the socket (<ip_or_hostname>:<port>) where the Kafka server is reachable to the XML parser.
    --candil-xml-parser-generator-kafka-input-topic=TOPIC --> Only when using Kafka for the input mode, specifies the name of the topic where the XML parser will read input XML data from.
    --candil-xml-parser-generator-kafka-output-topic=TOPIC --> Only when using Kafka for the output mode, specifies the name of the topic where the XML parser will output dictionary buffers to.
    ''')
          
def generate_python_xml_parser_code(ctx, modules, fd):
    '''
    Processes YANG modules and generates the corresponding Python XML parser code for data modeled by these YANG modules.
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
        'union': 'String'
    }

    INDENTATION_BLOCK = '    '

    BASE_IMPORT_STATEMENTS = [
        'import json\n',
        'import xml.etree.ElementTree as et',
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
        'xml = sys.argv[1]\n',
        'tree = et.parse(xml)\n',
        'root = tree.getroot()\n',
        'observed_at = root[0].text\n',
        'dict_buffers = []'
    ]

    if (ctx.opts.candil_xml_parser_generator_kafka_server is not None) and \
        (ctx.opts.candil_xml_parser_generator_kafka_input_topic is not None):
        READING_INSTRUCTIONS_KAFKA = [
            'dict_buffers = []\n',
            'consumer = KafkaConsumer(\'' + ctx.opts.candil_xml_parser_generator_kafka_input_topic + '\', bootstrap_servers=[\'' + ctx.opts.candil_xml_parser_generator_kafka_server + '\'])\n',
            'while True:\n',
            INDENTATION_BLOCK + 'for message in consumer:\n',
            2 * INDENTATION_BLOCK + 'xml = str(message.value.decode(\'utf-8\'))\n',
            2 * INDENTATION_BLOCK + 'root = et.fromstring(xml)\n',
            2 * INDENTATION_BLOCK + 'observed_at = root[0].text'
        ]
        

    WRITING_INSTRUCTIONS_PRINT = [
        'print(json.dumps(dict_buffers[::-1], indent=4))\n',
        'dict_buffers.clear()'
    ]

    WRITING_INSTRUCTIONS_FILE = [
        'output_file = open(\"dict_buffers.json\", \'w\')\n',
        'output_file.write(json.dumps(dict_buffers[::-1], indent=4))\n',
        'output_file.close()\n',
        'dict_buffers.clear()'
    ]

    if (ctx.opts.candil_xml_parser_generator_kafka_server is not None) and \
        (ctx.opts.candil_xml_parser_generator_kafka_output_topic is not None):
        WRITING_INSTRUCTIONS_KAFKA = [
            2 * INDENTATION_BLOCK + 'producer = KafkaProducer(bootstrap_servers=[\'' + ctx.opts.candil_xml_parser_generator_kafka_server + '\'])\n',
            2 * INDENTATION_BLOCK + 'producer.send(\'' + ctx.opts.candil_xml_parser_generator_kafka_output_topic + '\', value=json.dumps(dict_buffers[::-1], indent=4).encode(\'utf-8\'))\n',
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
                        if (typedef_type not in YANG_PRIMITIVE_TYPES) and ('ref' not in typedef_type):
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
        an XML file given the NGSI-LD type of that particular element.
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
            return 'eval(' + element_text + '.capitalize())'
    
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
    
    def is_list_get_key(element) -> str:
        '''
        Auxiliary function.
        Checks if an element matches a YANG data node of type list and obtains its key if so.
        '''
        key = None
        if (element.keyword == 'list'):
            key = element.i_key[0].arg
        return key
    
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

    def generate_parser_code(element, parent_element_arg, entity_path: str, camelcase_entity_path: str, camelcase_entity_list: list, depth_level: int, typedefs_dict: dict, key: str):
        '''
        Auxiliary function.
        Recursively generates the XML parser code.
        '''
        camelcase_element_arg = to_camelcase(str(element.keyword), str(element.arg))
        element_namespace = str(element.i_module.search_one('namespace').arg)
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
                        if (parent_element_arg is None):
                            generate_parser_code(subelement, None, None, None, list(), depth_level, typedefs_dict, key)
                        elif subelement.keyword == 'list': 
                            fd.write('\n' + INDENTATION_BLOCK * depth_level + str(element.arg).replace('-', '_') + ' ' + '=' + ' ' + str(parent_element_arg).replace('-', '_') + '.find(\".//{' + element_namespace + '}' + str(element.arg) + '\")')
                            fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if ' + str(element.arg).replace('-', '_') + ' is not None:')
                            depth_level += 1
                            generate_parser_code(subelement, element.arg, entity_path, None, list(), depth_level, typedefs_dict, key)
        ### --- ###

        ### NGSI-LD ENTITY IDENTIFICATION ###
        elif (is_entity(element) == True) and (is_deprecated(element) == False):
            current_camelcase_path = ''
            if (camelcase_entity_path is None):
                current_camelcase_path = to_camelcase(str(element.keyword), str(element.arg))
            else:
                current_camelcase_path = camelcase_entity_path + to_camelcase(str(element.keyword), str(element.arg))
            camelcase_entity_list.append(current_camelcase_path)
            if (parent_element_arg is None): # 1st level Entity.
                fd.write('\n' + INDENTATION_BLOCK * depth_level + 'for ' + str(element.arg).replace('-', '_') + ' in root.findall(\".//{' + element_namespace + '}' + str(element.arg) + '\"):')
                depth_level += 1
                fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer = {}')
                fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"id\"] = \"urn:ngsi-ld:' + current_camelcase_path + '\"')
                fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"type\"] = \"' + current_camelcase_path + '\"')
            else: # 2nd level Entity onwards.
                fd.write('\n' + INDENTATION_BLOCK * depth_level + 'for ' + str(element.arg).replace('-', '_') + ' in ' + str(parent_element_arg).replace('-', '_') + '.findall(\".//{' + element_namespace + '}' + str(element.arg) + '\"):')
                depth_level += 1
                fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer = {}')
                fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"id\"] = \"urn:ngsi-ld:' + current_camelcase_path + ':\" + ":".join(' + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"].split(\":\")[3:])')
                fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"type\"] = \"' + current_camelcase_path + '\"')
                fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"isPartOf\"] = {}')
                fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"isPartOf\"][\"type\"] = \"Relationship\"')
                fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"isPartOf\"][\"object\"] = ' + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"]')
                fd.write('\n' + INDENTATION_BLOCK * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"isPartOf\"][\"observedAt\"] = observed_at')
            subelements = element.i_children
            key = is_list_get_key(element)
            if (subelements is not None):
                for subelement in subelements:
                    if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                        generate_parser_code(subelement, element.arg, current_path, current_camelcase_path, camelcase_entity_list, depth_level, typedefs_dict, key)
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
                                    generate_parser_code(subelement, parent_element_arg, current_path, camelcase_entity_path, camelcase_entity_list, depth_level, typedefs_dict, key)
        ### --- ###

        ### NGSI-LD PROPERTY IDENTIFICATION ###
        elif (is_property(element, typedefs_dict) == True) and (is_deprecated(element) == False):
            fd.write('\n' + INDENTATION_BLOCK * depth_level + camelcase_element_arg + ' ' + '=' + ' ' + str(parent_element_arg).replace('-', '_') + '.find(\".//{' + element_namespace + '}' + str(element.arg) + '\")')
            fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if ' + camelcase_element_arg + ' is not None:')
            ngsi_ld_type = yang_to_ngsi_ld_types_conversion(str(element.search_one('type')).replace('type ', '').split(":")[-1], typedefs_dict)
            text_format = element_text_type_formatting(ngsi_ld_type, 'element_text')
            fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK + 'element_text = ' + camelcase_element_arg + '.text')
            fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK + 'if element_text is not None:')
            if key != None and key == str(element.arg):
                fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"] = ' + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"] + \":\" + ' + text_format)
            #elif ('name'.casefold() in str(element.arg)) or ('id'.casefold() in str(element.arg).casefold()):
            #    fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"] = ' + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"] + \":\" + ' + text_format)
            fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"] = {}')
            fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"type\"] = \"Property\"')
            fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"value\"] = ' + text_format)
            fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"observedAt\"] = observed_at')
            config = is_config_element(element)
            if config == True:
                fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"datasetId\"] = \"urn:ngsi-ld:configuration\"')
            else:
                fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"datasetId\"] = \"urn:ngsi-ld:operational\"')
        ### --- ###
        
        ### NGSI-LD RELATIONSHIP IDENTIFICATION ###
        elif (is_relationship(element, typedefs_dict) == True) and (is_deprecated(element) == False):
            pointer = element.i_leafref_ptr[0]
            pointer_parent = pointer.parent
            camelcase_pointer_parent = to_camelcase(str(pointer_parent.keyword), str(pointer_parent.arg))
            matches = [] # The best match should always be the first element appended into the list: index 0.
            for camelcase_entity in camelcase_entity_list:
                if camelcase_pointer_parent in camelcase_entity:
                    matches.append(camelcase_entity)
            fd.write('\n' + INDENTATION_BLOCK * depth_level + camelcase_element_arg + ' ' + '=' + ' ' + str(parent_element_arg).replace('-', '_') + '.find(\".//{' + element_namespace + '}' + str(element.arg) + '\")')
            fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if ' + camelcase_element_arg + ' is not None:')
            fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK + 'element_text = ' + camelcase_element_arg + '.text')
            fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK + 'if element_text is not None:')
            fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"] = {}')
            fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"type\"] = \"Relationship\"')
            fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"object\"] = \"urn:ngsi-ld:' + matches[0] + "\"" + ' + \":\" + element_text')
            fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"observedAt\"] = observed_at')
            config = is_config_element(element)
            if config == True:
                fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"datasetId\"] = \"urn:ngsi-ld:configuration\"')
            else:
                fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"datasetId\"] = \"urn:ngsi-ld:operational\"')
        ### --- ###

        ### NGSI-LD YANG IDENTITY IDENTIFICATION ###
        elif (is_yang_identity(element, typedefs_dict) == True) and (is_deprecated(element) == False):
            fd.write('\n' + INDENTATION_BLOCK * depth_level + camelcase_element_arg + ' ' + '=' + ' ' + str(parent_element_arg).replace('-', '_') + '.find(\".//{' + element_namespace + '}' + str(element.arg) + '\")')
            fd.write('\n' + INDENTATION_BLOCK * depth_level + 'if ' + camelcase_element_arg + ' is not None:')
            ngsi_ld_type = yang_to_ngsi_ld_types_conversion(str(element.search_one('type')).replace('type ', '').split(":")[-1], typedefs_dict)
            text_format = element_text_type_formatting(ngsi_ld_type, 'element_text')
            fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK + 'element_text = ' + camelcase_element_arg + '.text')
            fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK + 'if element_text is not None:')
            if (str(element.arg) == 'type'):
                yang_identity_name = str(element.parent.arg) + str(element.arg).capitalize()
            else:
                yang_identity_name = str(element.arg)
            fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + yang_identity_name + '\"] = {}')
            fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + yang_identity_name + '\"][\"type\"] = \"Relationship\"')
            fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + yang_identity_name + '\"][\"object\"] = \"urn:ngsi-ld:YANGIdentity\" + \":\" + element_text')
            fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + yang_identity_name + '\"][\"observedAt\"] = observed_at')
            config = is_config_element(element)
            if config == True:
                fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + yang_identity_name + '\"][\"datasetId\"] = \"urn:ngsi-ld:configuration\"')
            else:
                fd.write('\n' + INDENTATION_BLOCK * depth_level + INDENTATION_BLOCK * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + yang_identity_name + '\"][\"datasetId\"] = \"urn:ngsi-ld:operational\"')
        ### --- ###
    
    ### --- ###

    # Generate import statements (standard Python libraries and such):
    for import_statement in BASE_IMPORT_STATEMENTS:
        fd.write(import_statement)
    fd.write('\n')
    if (ctx.opts.candil_xml_parser_generator_input_mode == INPUT_MODE_FILE) or \
        (ctx.opts.candil_xml_parser_generator_output_mode == OUTPUT_MODE_FILE):
        for line in FILE_IMPORT_STATEMENTS:
            fd.write(line)
            fd.write('\n')
    if (ctx.opts.candil_xml_parser_generator_input_mode == INPUT_MODE_KAFKA):
        for line in KAFKA_INPUT_IMPORT_STATEMENTS:
            fd.write(line)
            fd.write('\n')
    if (ctx.opts.candil_xml_parser_generator_output_mode == OUTPUT_MODE_KAFKA):
        for line in KAFKA_OUTPUT_IMPORT_STATEMENTS:
            fd.write(line)
            fd.write('\n')

    fd.write('\n')

    # Generate reading instructions for the XML parser (depending on the input mode):
    if (ctx.opts.candil_xml_parser_generator_input_mode == INPUT_MODE_FILE):
        for line in READING_INSTRUCTIONS_FILE:
            fd.write(line)
    if (ctx.opts.candil_xml_parser_generator_input_mode == INPUT_MODE_KAFKA):
        for line in READING_INSTRUCTIONS_KAFKA:
            fd.write(line)
    
    fd.write('\n')

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

    # Generate XML parser code (element data retrieval and transformation to generate dictionary buffers):
    depth_level = 0
    for module in modules:
        elements = module.i_children
        if (elements is not None):
            if (ctx.opts.candil_xml_parser_generator_input_mode == INPUT_MODE_FILE):
                depth_level = 0
            if (ctx.opts.candil_xml_parser_generator_input_mode == INPUT_MODE_KAFKA):
                depth_level = 2
            for element in elements:
                if (element is not None) and (element.keyword in statements.data_definition_keywords):
                    generate_parser_code(element, None, None, None, list(), depth_level, typedefs_dict, None)
    
    fd.write('\n\n')

    # Generate writing instructions for the XML parser (depending on the output mode):
    if (ctx.opts.candil_xml_parser_generator_output_mode == OUTPUT_MODE_FILE):
        for line in WRITING_INSTRUCTIONS_FILE:
            fd.write(line)
    if (ctx.opts.candil_xml_parser_generator_output_mode == OUTPUT_MODE_PRINT):
        for line in WRITING_INSTRUCTIONS_PRINT:
            fd.write(line)
    if (ctx.opts.candil_xml_parser_generator_output_mode == OUTPUT_MODE_KAFKA):
        for line in WRITING_INSTRUCTIONS_KAFKA:
            fd.write(line)
    
    fd.write('\n')
    fd.close()
