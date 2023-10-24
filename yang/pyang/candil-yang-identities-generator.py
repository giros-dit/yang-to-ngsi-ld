'''
pyang plugin -- CANDIL NGSI-LD Context Generator.

Discovers YANG Identities within a YANG module and generates their corresponding NGSI-LD Entities.

Version: 0.0.1.

Author: Networking and Virtualization Research Group (GIROS DIT-UPM) -- https://dit.upm.es/~giros
'''

import optparse
import pdb
import re
import sys
import json

from kafka import KafkaProducer

from pyang import plugin
from pyang import statements

def pyang_plugin_init():
    plugin.register_plugin(CandilYangIdentitiesGeneratorPlugin())

class CandilYangIdentitiesGeneratorPlugin(plugin.PyangPlugin):
    def __init__(self):
        plugin.PyangPlugin.__init__(self, 'candil-yang-identities-generator')

    def add_output_format(self, fmts):
        self.multiple_modules = True
        fmts['candil-yang-identities-generator'] = self
    
    def add_opts(self, optparser):
        optlist = [
            optparse.make_option('--candil-yang-identities-generator-help', dest='print_help', action='store_true', help='Prints help and usage.'),
            optparse.make_option('--candil-yang-identities-generator-output-mode', dest='output_mode', action='store', help='Defines writing mode for the representation of NGSI-LD Entities.'),
            optparse.make_option('--candil-yang-identities-generator-kafka-server', dest='kafka_server', action='store', help='Defines the Kafka server to use (in socket format: <ip_or_hostname>:<port>).'),
            optparse.make_option('--candil-yang-identities-generator-kafka-topic', dest='kafka_topic', action='store', help='Defines Kafka\'s output topic to use for writing the representation of NGSI-LD Entities.')
        ]
        g = optparser.add_option_group('CANDIL YANG Identities Generator - Execution options')
        g.add_options(optlist)

    def setup_ctx(self, ctx):
        if ctx.opts.print_help:
            print_help()
            sys.exit(0)

    def setup_fmt(self, ctx):
        ctx.implicit_errors = False

    def emit(self, ctx, modules, fd):
        generate_yang_identities(ctx, modules, fd)

def print_help():
    '''
    Prints plugin's help information.
    '''
    print('''
Pyang plugin - CANDIL YANG Identities Generator (candil-yang-identities-generator).
Discovers YANG Identities within a YANG module and generates their corresponding NGSI-LD Entities.

Usage:
pyang -f candil-yang-identities-generator [OPTIONS] <base_module.yang> [augmenting_module_1.yang] [augmenting_module_2.yang] ... [augmenting_module_N.yang]

OPTIONS:
    --candil-yang-identities-generator-output-mode=MODE --> **MANDATORY** Define where to write the representation of NGSI-LD Entities to. Valid values: file, print or kafka.
    --candil-yang-identities-generator-kafka-server=SOCKET --> Only when using Kafka, specify the socket (<ip_or_hostname>:<port>) where the Kafka server is reachable.
    --candil-yang-identities-generator-kafka-topic=TOPIC --> Only when using Kafka, specify the name of the topic where to write the representation of NGSI-LD Entities to.
    ''')

def generate_yang_identities(ctx, modules, fd):
    '''
    Processes YANG modules, discovers YANG Identities and generates their corresponding NGSI-LD Entities.
    NGSI-LD Entities are stored in a dictionary buffer.
    '''

    # Use PDB to debug the code with pdb.set_trace().
    # pdb.set_trace()

    # CONSTANTS:

    # Writing modes for output dictionary buffers.
    OUTPUT_MODE_PRINT = "print" # -> Output dictionary buffers are printed to stdout (terminal).
    OUTPUT_MODE_FILE = "file" # -> Output dictionary buffers are written to a file.
    OUTPUT_MODE_KAFKA = "kafka" # -> Output dictionary buffers are written to a Kafka topic.

    dict_buffers = []

    identity_modules = []
    for module in modules:
        identity_modules.append(module)
        imports = module.search('import')
        for i in imports:
            submodule = ctx.get_module(i.arg)
            if submodule is not None:
                identity_modules.append(submodule)
    identity_modules = list(dict.fromkeys(identity_modules)) # Delete duplicates.

    for module in identity_modules:
        namespace = str(module.search_one('namespace').arg)
        prefix = str(module.i_prefix)
        identities = module.i_identities
        if identities is not None:
            for identity_name in identities:
                identity_dict_buffer = {}

                identity_dict_buffer["id"] = "urn:ngsi-ld:YANGIdentity:" + prefix + ":" + identity_name
                identity_dict_buffer["type"] = "YANGIdentity"

                description = str(identities[identity_name].search_one('description'))\
                    .replace('description ', '')\
                    .replace('\n', ' ')
                identity_dict_buffer["description"] = {}
                identity_dict_buffer["description"]["type"] = "Property"
                identity_dict_buffer["description"]["value"] = description
                
                identity_dict_buffer["identifier"] = {}
                identity_dict_buffer["identifier"]["type"] = "Property"
                identity_dict_buffer["identifier"]["value"] = identity_name

                identity_dict_buffer["namespace"] = {}
                identity_dict_buffer["namespace"]["type"] = "Property"
                identity_dict_buffer["namespace"]["value"] = namespace

                base = str(identities[identity_name].search_one('base'))\
                    .replace('base ', '')
                if base != "None":
                    if ":" not in base:
                        base = prefix + ":" + base
                    identity_dict_buffer["broader"] = {}
                    identity_dict_buffer["broader"]["type"] = "Relationship"
                    identity_dict_buffer["broader"]["value"] = "urn:ngsi-ld:YANGIdentity:" + base

                dict_buffers.append(identity_dict_buffer)

                print(json.dumps(identity_dict_buffer, indent=4))
                
                print('\n')


