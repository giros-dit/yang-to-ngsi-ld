'''
pyang plugin -- CANDIL XML Parser Generator.

Given one or several YANG modules, it dynamically generates the code of an XML parser
that is able to read data modeled by these modules and is also capable of creating
instances of Pydantic classes from the NGSI-LD-backed OpenAPI generation.

Version: 0.3.1.

Author: Networking and Virtualization Research Group (GIROS DIT-UPM) -- https://dit.upm.es/~giros
'''

import optparse
import pdb
import re
import sys

from pyang import plugin
from pyang import statements

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
            optparse.make_option('--candil-xml-parser-generator-help', dest='print_help', action='store_true', help='Prints help and usage.'),
            optparse.make_option('--candil-xml-parser-generator-input-mode', dest='input_mode', action='store', help='Defines reading mode for input XML data.'),
            optparse.make_option('--candil-xml-parser-generator-output-mode', dest='output_mode', action='store', help='Defines writing mode for output dictionary buffers.'),
            optparse.make_option('--candil-xml-parser-generator-kafka-server', dest='kafka_server', action='store', help='Defines the Kafka server to use (in socket format).'),
            optparse.make_option('--candil-xml-parser-generator-kafka-input-topic', dest='kafka_input_topic', action='store', help='Defines Kafka\'s input topic to use for reading XML data.'),
            optparse.make_option('--candil-xml-parser-generator-kafka-output-topic', dest='kafka_output_topic', action='store', help='Defines Kafka\'s output topic to use for writing dictionary buffers.')
        ]
        g = optparser.add_option_group('CANDIL XML Parser Generator - Execution options')
        g.add_options(optlist)

    def setup_ctx(self, ctx):
        if ctx.opts.print_help:
            print_help()
            sys.exit(0)

    def setup_fmt(self, ctx):
        ctx.implicit_errors = False

    def emit(self, ctx, modules, fd):
        generate_python_xml_parser_code(ctx, modules, fd)

def print_help():
    '''
    Prints plugin's help information.
    '''
    print('''
Pyang plugin - CANDIL XML Parser Generator (candil-xml-parser-generator).
Given one or several YANG modules, this plugin generates the Python code of an XML parser
that is able to read data modeled by these YANG modules and is also able to generate
the data structures of the identified NGSI-LD Entities. These data structures are valid
according to the OpenAPI generation.

Usage:
pyang -f candil-xml-parser-generator <base_module.yang> [augmenting_module_1.yang] [augmenting_module_2.yang] ... [augmenting_module_N.yang] > <output_file.py>
    ''')
          
def generate_python_xml_parser_code(ctx, modules, fd):
    '''
    Processes YANG modules and generates the corresponding Python XML parser code for data modeled by these YANG modules.
    '''

    # Use PDB to debug the code with pdb.set_trace().

    # CONSTANTS:

    # Reading modes for input XML data.
    INPUT_MODE_FILE = "file" # -> Input XML data filepath is specified as an invocation argument.
    INPUT_MODE_KAFKA = "kafka" # -> Input XML data is read from a Kafka topic.
    
    # Writing modes for output dictionary buffers.
    OUTPUT_MODE_STDOUT = "stdout" # -> Output dictionary buffers are written to stdout (terminal). Can be redirected to a file.
    OUTPUT_MODE_KAFKA = "kafka" # -> Output dictionary buffers are written to a Kafka topic.

    # NOTE: from ietf-yang-types@2023-01-23.yang.
    # If there are several conversion steps, the value is always the final type.
    IETF_YANG_TYPES_TO_BASE_YANG_TYPES = {
        'yang:counter32': 'uint32',
        'yang:zero-based-counter32': 'uint32',
        'yang:counter64': 'uint64',
        'yang:zero-based-counter64': 'uint64',
        'yang:gauge32': 'uint32',
        'yang:gauge64': 'uint64',
        'yang:object-identifier': 'string',
        'yang:object-identifier-128': 'string',
        'yang:date-and-time': 'string',
        'yang:date-with-zone-offset': 'string',
        'yang:date-no-zone': 'string',
        'yang:time-with-zone-offset': 'string',
        'yang:time-no-zone': 'string',
        'yang:hours32': 'int32',
        'yang:minutes32': 'int32',
        'yang:seconds32': 'int32',
        'yang:centiseconds32': 'int32',
        'yang:miliseconds32': 'int32',
        'yang:microseconds32': 'int32',
        'yang:microseconds64': 'int64',
        'yang:nanoseconds32': 'int32',
        'yang:nanoseconds64': 'int64',
        'yang:timeticks': 'uint32',
        'yang:timestamp': 'uint32',
        'yang:phys-address': 'string',
        'yang:mac-address': 'string',
        'yang:xpath1.0': 'string',
        'yang:hex-string': 'string',
        'yang:uuid': 'string',
        'yang:dotted-quad': 'string',
        'yang:language-tag': 'string',
        'yang:yang-identifier': 'string'
    }

    # NOTE: from ietf-inet-types@2021-02-22.yang.
    IETF_INET_TYPES_TO_BASE_YANG_TYPES = {
        'inet:ip-version': 'enumeration',
        'inet:dscp': 'uint8',
        'inet:ipv6-flow-label': 'uint32',
        'inet:port-number': 'uint16',
        'inet:as-number': 'uint32',
        'inet:ip-address': 'union',
        'inet:ipv4-address': 'string',
        'inet:ipv6-address': 'string',
        'inet:ip-address-no-zone': 'union',
        'inet:ipv4-address-no-zone': 'string',
        'inet:ipv6-address-no-zone': 'string',
        'inet:ip-prefix': 'union',
        'inet:ipv4-prefix': 'string',
        'inet:ipv6-prefix': 'string',
        'inet:ip-address-and-prefix': 'union',
        'inet:ipv4-address-and-prefix': 'string',
        'inet:ipv6-address-and-prefix': 'string',
        'inet:domain-name': 'string',
        'inet:host-name': 'string',
        'inet:host': 'union',
        'inet:uri': 'string',
        'inet:email-address': 'string'
    }

    # NOTE: from ietf-ip@2018-02-22.yang.
    IETF_IP_TYPES_TO_BASE_YANG_TYPES = {
        'ip-address-origin': 'enumeration',
        'neighbor-origin': 'enumeration'
    }

    # NOTE: from netflow-v9.yang and netflow-v9-agg.yang.
    NETFLOW_V9_TYPES_TO_BASE_YANG_TYPES = {
        'net-v9:prefix-length-ipv4': 'uint8',
        'net-v9:prefix-length-ipv6': 'uint8',
        'net-v9:protocol-type': 'enumeration',
        'net-v9:engine-type': 'enumeration',
        'net-v9:top-label-type': 'enumeration',
        'net-v9:forwarding-status-type': 'enumeration',
        'net-v9:igmp-type': 'enumeration',
        'net-v9:sampling-mode-type': 'enumeration',
        'net-v9:ip-version-type': 'enumeration',
        'net-v9:direction-type': 'enumeration',
        'net-v9:tcp-flags-type': 'bits',
        'per-decimal': 'decimal64'
    }

    # NOTE: from ietf-network.yang. 
    IETF_NETWORK_TYPES_TO_BASE_YANG_TYPES = {
        "node-id": "string",
        "network-id": "string"
    } 

    # NOTE: from ietf-network-topology.yang. 
    IETF_NETWORK_TOPOLOGY_TYPES_TO_BASE_YANG_TYPES = {
        "link-id": "string",
        "tp-id": "string"
    }

    # NOTE: NGSI-LD types are Python "types" (as per this particular implementation).
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

    INDENTATION_LEVEL = '    '

    IMPORT_STATEMENTS = [
        'import sys\n',
        'import xml.etree.ElementTree as et\n',
        'from kafka import KafkaConsumer, KafkaProducer'
    ]

    READING_INSTRUCTIONS_FILE = [
        'xml = sys.argv[1]\n',
        'tree = et.parse(xml)\n',
        'root = tree.getroot()\n',
        'dict_buffers = []'
    ]

    if (ctx.opts.kafka_server is not None) and (ctx.opts.kafka_input_topic is not None):
        READING_INSTRUCTIONS_KAFKA = [
            'dict_buffers = []\n',
            'consumer = KafkaConsumer(\'' + ctx.opts.kafka_input_topic + '\', bootstrap_servers=[\'' + ctx.opts.kafka_server + '\'])\n',
            'while True:\n',
            INDENTATION_LEVEL + 'for message in consumer:\n',
            2 * INDENTATION_LEVEL + 'xml = str(message.value.decode(\'utf-8\'))\n',
            2 * INDENTATION_LEVEL + 'root = et.fromstring(xml)'
        ]

    WRITING_INSTRUCTIONS_STDOUT = [
        'print(dict_buffers[::-1])'
    ]

    if (ctx.opts.kafka_server is not None) and (ctx.opts.kafka_output_topic is not None):
        WRITING_INSTRUCTIONS_KAFKA = [
            2 * INDENTATION_LEVEL + 'producer = KafkaProducer([\'' + ctx.opts.kafka_server + '\'])\n',
            2 * INDENTATION_LEVEL + 'producer.send(\'' + ctx.opts.kafka_output_topic + '\', value=str(dict_buffers[::-1]).encode(\'utf-8\'))\n',
            2 * INDENTATION_LEVEL + 'producer.flush()\n',
            2 * INDENTATION_LEVEL + 'dict_buffers.clear()'
        ]

    # AUXILIARY FUNCTIONS: 

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
    
    def yang_to_ngsi_ld_types_conversion(element_type: str) -> str:
        '''
        Auxiliary function.
        Returns the NGSI-LD type (in Python implementation) given the YANG type of an element/node in a YANG module.
        '''
        base_yang_type = ''
        if (IETF_YANG_TYPES_TO_BASE_YANG_TYPES.get(element_type) is not None):
            base_yang_type = IETF_YANG_TYPES_TO_BASE_YANG_TYPES[element_type]
        elif (IETF_INET_TYPES_TO_BASE_YANG_TYPES.get(element_type) is not None):
            base_yang_type = IETF_INET_TYPES_TO_BASE_YANG_TYPES[element_type]
        elif (IETF_IP_TYPES_TO_BASE_YANG_TYPES.get(element_type) is not None):
            base_yang_type = IETF_IP_TYPES_TO_BASE_YANG_TYPES[element_type]
        elif (NETFLOW_V9_TYPES_TO_BASE_YANG_TYPES.get(element_type) is not None):
            base_yang_type = NETFLOW_V9_TYPES_TO_BASE_YANG_TYPES[element_type]
        elif (IETF_NETWORK_TYPES_TO_BASE_YANG_TYPES.get(element_type) is not None):
            base_yang_type = IETF_NETWORK_TYPES_TO_BASE_YANG_TYPES[element_type]
        elif (IETF_NETWORK_TOPOLOGY_TYPES_TO_BASE_YANG_TYPES.get(element_type) is not None):
            base_yang_type = IETF_NETWORK_TOPOLOGY_TYPES_TO_BASE_YANG_TYPES[element_type]
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

    def generate_parser_code(element, parent_element_arg, entity_path: str, depth_level: int):
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
        if (is_enclosing_container(element) == True) and (is_deprecated(element) == False):
            subelements = element.i_children
            if (subelements is not None):
                for subelement in subelements:
                    if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                        generate_parser_code(subelement, None, None, depth_level)
        elif (is_entity(element) == True) and (is_deprecated(element) == False):
            if (parent_element_arg is None): # 1st level Entity.
                fd.write('\n' + INDENTATION_LEVEL * depth_level + 'for ' + str(element.arg).replace('-', '_') + ' in root.findall(\".//{' + element_namespace + '}' + str(element.arg) + '\"):')
                depth_level += 1
                fd.write('\n' + INDENTATION_LEVEL * depth_level + current_path.replace('-', '_') + 'dict_buffer = {}')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"id\"] = \"urn:ngsi-ld:' + camelcase_element_arg + ':\"')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"type\"] = \"' + camelcase_element_arg + '\"')
            else: # 2nd level Entity onwards.
                fd.write('\n' + INDENTATION_LEVEL * depth_level + 'for ' + str(element.arg).replace('-', '_') + ' in ' + str(parent_element_arg).replace('-', '_') + '.findall(\".//{' + element_namespace + '}' + str(element.arg) + '\"):')
                depth_level += 1
                fd.write('\n' + INDENTATION_LEVEL * depth_level + current_path.replace('-', '_') + 'dict_buffer = {}')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"id\"] = \"urn:ngsi-ld:' + camelcase_element_arg + ':\" + ' + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"].split(\":\")[-1]')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"type\"] = \"' + camelcase_element_arg + '\"')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"isPartOf\"] = {}')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"isPartOf\"][\"type\"] = \"Relationship\"')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + current_path.replace('-', '_') + 'dict_buffer[\"isPartOf\"][\"object\"] = ' + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"]')
            subelements = element.i_children
            if (subelements is not None):
                for subelement in subelements:
                    if (subelement is not None) and (subelement.keyword in statements.data_definition_keywords):
                        generate_parser_code(subelement, element.arg, current_path, depth_level)
            fd.write('\n' + INDENTATION_LEVEL * depth_level + 'dict_buffers.append(' + current_path.replace('-', '_') + 'dict_buffer)')
        elif (is_property(element) == True) and (is_deprecated(element) == False):
            fd.write('\n' + INDENTATION_LEVEL * depth_level + camelcase_element_arg + ' ' + '=' + ' ' + str(parent_element_arg).replace('-', '_') + '.find(\".//{' + element_namespace + '}' + str(element.arg) + '\")')
            fd.write('\n' + INDENTATION_LEVEL * depth_level + 'if ' + camelcase_element_arg + ' is not None:')
            ngsi_ld_type = yang_to_ngsi_ld_types_conversion(str(element.search_one('type')).replace('type ', ''))
            text_format = element_text_type_formatting(ngsi_ld_type, 'element_text')
            fd.write('\n' + INDENTATION_LEVEL * depth_level + INDENTATION_LEVEL + 'element_text = ' + camelcase_element_arg + '.text')
            fd.write('\n' + INDENTATION_LEVEL * depth_level + INDENTATION_LEVEL + 'if element_text is not None:')
            if (str(element.arg) == 'name'):
                fd.write('\n' + INDENTATION_LEVEL * depth_level + INDENTATION_LEVEL * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"] = ' + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"id\"] + ' + text_format)
            fd.write('\n' + INDENTATION_LEVEL * depth_level + INDENTATION_LEVEL * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"] = {}')
            fd.write('\n' + INDENTATION_LEVEL * depth_level + INDENTATION_LEVEL * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"type\"] = \"Property\"')
            fd.write('\n' + INDENTATION_LEVEL * depth_level + INDENTATION_LEVEL * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"value\"] = ' + text_format)
        elif (is_relationship(element) == True) and (is_deprecated(element) == False):
            if (str(element.arg) != 'type'):
                fd.write('\n' + INDENTATION_LEVEL * depth_level + camelcase_element_arg + ' ' + '=' + ' ' + str(parent_element_arg).replace('-', '_') + '.find(\".//{' + element_namespace + '}' + str(element.arg) + '\")')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + 'if ' + camelcase_element_arg + ' is not None:')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + INDENTATION_LEVEL + 'element_text = ' + camelcase_element_arg + '.text')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + INDENTATION_LEVEL + 'if element_text is not None:')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + INDENTATION_LEVEL * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"] = {}')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + INDENTATION_LEVEL * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"type\"] = \"Relationship\"')
                fd.write('\n' + INDENTATION_LEVEL * depth_level + INDENTATION_LEVEL * 2 + current_path.replace(str(element.arg) + '_', '').replace('-', '_') + 'dict_buffer[\"' + camelcase_element_arg + '\"][\"object\"] = \"urn:ngsi-ld:' + str(parent_element_arg).replace('-', '_').capitalize() + ':\" + element_text')
    
    # -- Generate XML parser Python code --

    # Generate base import statements (standard Python libraries and such):
    for import_statement in IMPORT_STATEMENTS:
        fd.write(import_statement)

    fd.write('\n\n')

    # Generate reading instructions for the XML parser (depending on the input mode):
    if (ctx.opts.input_mode is not None) and (ctx.opts.input_mode == INPUT_MODE_FILE):
        for line in READING_INSTRUCTIONS_FILE:
            fd.write(line)
    if (ctx.opts.input_mode is not None) and (ctx.opts.input_mode == INPUT_MODE_KAFKA):
        for line in READING_INSTRUCTIONS_KAFKA:
            fd.write(line)
    
    fd.write('\n')

    # Generate XML parser code (element data retrieval and transformation to generate dictionary buffers):
    depth_level = 0
    for module in modules:
        elements = module.i_children
        if (elements is not None):
            if (ctx.opts.input_mode is not None) and (ctx.opts.input_mode == INPUT_MODE_FILE):
                depth_level = 0
            if (ctx.opts.input_mode is not None) and (ctx.opts.input_mode == INPUT_MODE_KAFKA):
                depth_level = 2
            for element in elements:
                if (element is not None) and (element.keyword in statements.data_definition_keywords):
                    generate_parser_code(element, None, None, depth_level)
    
    fd.write('\n\n')

    # Generate writing instructions for the XML parser (depending on the output mode):
    if (ctx.opts.output_mode is not None) and (ctx.opts.output_mode == OUTPUT_MODE_STDOUT):
        for line in WRITING_INSTRUCTIONS_STDOUT:
            fd.write(line)
    if (ctx.opts.output_mode is not None) and (ctx.opts.output_mode == OUTPUT_MODE_KAFKA):
        for line in WRITING_INSTRUCTIONS_KAFKA:
            fd.write(line)
    
    fd.write('\n')

    fd.close()
