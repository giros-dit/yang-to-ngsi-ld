'''
pyang plugin -- CANDIL NGSI-LD Identities Generator.

Discovers YANG Identities within a YANG module and generates the data structures
(dictionary buffers) of their corresponding NGSI-LD Entities.

Version: 0.0.4.

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

# PLUGIN CONSTANTS:

# Writing modes for output dictionary buffers.
OUTPUT_MODE_FILE = "file" # -> Output dictionary buffers are written to a file.
OUTPUT_MODE_KAFKA = "kafka" # -> Output dictionary buffers are written to a Kafka topic.

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
            optparse.make_option('--candil-yang-identities-generator-help', dest='candil_yang_identities_generator_help', action='store_true', help='Prints help and usage.'),
            optparse.make_option('--candil-yang-identities-generator-output-mode', dest='candil_yang_identities_generator_output_mode', action='store', help='Defines the output mode for dictionary buffers.'),
            optparse.make_option('--candil-yang-identities-generator-kafka-server', dest='candil_yang_identities_generator_kafka_server', action='store', help='Only when using Kafka, specifies the endpoint of the server to use.'),
            optparse.make_option('--candil-yang-identities-generator-kafka-topic', dest='candil_yang_identities_generator_kafka_topic', action='store', help='Only when using Kafka, specifies the output topic to use.'),
            optparse.make_option('--candil-yang-identities-generator-mgmt-protocol', dest='candil_yang_identities_generator_mgmt_protocol', action='store', help='Defines the network management protocol (i.e., NETCONF or gNMI).')
        ]
        g = optparser.add_option_group('CANDIL YANG Identities Generator specific options')
        g.add_options(optlist)

    def setup_ctx(self, ctx):
        if ctx.opts.candil_yang_identities_generator_help:
            print_help()
            sys.exit(0)

    def setup_fmt(self, ctx):
        ctx.implicit_errors = False

    def emit(self, ctx, modules, fd):
        generate_yang_identities(ctx, modules, fd)

def print_help():
    '''
    Prints execution help.
    '''
    print('''
Pyang plugin - CANDIL YANG Identities Generator (candil-yang-identities-generator).
Discovers YANG Identities within a YANG module and generates the data structures
(dictionary buffers) of their corresponding NGSI-LD Entities.

Usage:
pyang -f candil-yang-identities-generator [OPTIONS] <module.yang>

OPTIONS:
    --candil-yang-identities-generator-output-mode=MODE --> Defines where to output the representation of NGSI-LD Entities to (dictionary buffers). Valid values: file or kafka.
    --candil-yang-identities-generator-kafka-server=SOCKET --> Only when using Kafka, specifies the socket (<ip_or_hostname>:<port>) where the Kafka server is reachable.
    --candil-yang-identities-generator-kafka-topic=TOPIC --> Only when using Kafka, specifies the output topic for the representation of NGSI-LD Entities (dictionary buffers).
    --candil-yang-identities-generator-mgmt-protocol=<netconf/gnmi> -> Defines the network management protocol (i.e., NETCONF or gNMI).
    ''')

def generate_yang_identities(ctx, modules, fd):
    '''
    Processes YANG modules, discovers YANG Identities and generates their corresponding NGSI-LD Entities.
    '''

    # Use PDB to debug the code with pdb.set_trace().
    # pdb.set_trace()

    # YANG Identities are represented as dictionary buffers that are stored in a list.
    dict_buffers = []

    # All modules are stored in a list, including those specified in import sentences.
    identity_modules = []
    for module in modules:
        identity_modules.append(module)
        imports = module.search('import')
        for i in imports:
            submodule = ctx.get_module(i.arg)
            if submodule is not None:
                identity_modules.append(submodule)
    identity_modules = list(dict.fromkeys(identity_modules)) # Delete duplicates (if there are any).

    # Every single module is processed.
    for module in identity_modules:
        namespace = str(module.search_one('namespace').arg)

        '''
        Select the prefix of the YANGIdentity depending of the network management protocol (i.e., NETCONF or gNMI).
         - In NETCONF Query RPCs the YANG Indentity value comes as "yang_module_prefix:identity_name".
         - In gNMI Query RPCs the YANG Identity value comes as "yang_module_name:identity_name".               
        '''
        if (ctx.opts.candil_yang_identities_generator_mgmt_protocol == "netconf"):
            prefix = str(module.i_prefix)
        elif (ctx.opts.candil_yang_identities_generator_mgmt_protocol == "gnmi"):
            prefix = str(module.i_modulename)
        
        identities = module.i_identities # The variable "identities" is a dictionary.
        if identities is not None:
            for identity_name in identities: # "identity_name" is the key for iterating over the dictionary.
                identity_dict_buffer = {}
                identity_dict_buffer["id"] = "urn:ngsi-ld:YANGIdentity:" + prefix + ":" + identity_name
                identity_dict_buffer["type"] = "YANGIdentity"
                description = str(identities[identity_name].search_one('description')).replace('description ', '').replace('\n', ' ')
                if description == "None":
                    description = "There is no description for this identity in the YANG module."
                identity_dict_buffer["description"] = {}
                identity_dict_buffer["description"]["type"] = "Property"
                identity_dict_buffer["description"]["value"] = description
                identity_dict_buffer["identifier"] = {}
                identity_dict_buffer["identifier"]["type"] = "Property"
                identity_dict_buffer["identifier"]["value"] = identity_name
                identity_dict_buffer["namespace"] = {}
                identity_dict_buffer["namespace"]["type"] = "Property"
                identity_dict_buffer["namespace"]["value"] = namespace
                base = str(identities[identity_name].search_one('base')).replace('base ', '')
                # When there is no "base" statement, the variable stores the "None" string.
                # Otherwise, it stores the "parent" identity name.
                if base != "None":     
                    if ":" not in base:
                        # If the "parent" identity name does not contain the prefix, it is added in order to build the relationship.
                        base = prefix + ":" + base
                    elif base.split(":")[0] != prefix:
                        '''
                        If the prefix of identity name does not contain the real prefix (i.e., "yang_module_name" por gNMI or "yang_module_prefix" for NETCONF), 
                        it is replaced accordingly in order to build the relationship.
                        '''
                        base = prefix + ":" + base.split(":")[-1]
                    identity_dict_buffer["broader"] = {}
                    identity_dict_buffer["broader"]["type"] = "Relationship"
                    identity_dict_buffer["broader"]["object"] = "urn:ngsi-ld:YANGIdentity:" + base
                dict_buffers.append(identity_dict_buffer)

    # Depending on the output mode, dictionary buffers are written either to a file or to a Kafka topic.
    if (ctx.opts.candil_yang_identities_generator_output_mode == OUTPUT_MODE_FILE):
        output_file = open("YANGIdentities.json", "w")
        output_file.write(json.dumps(dict_buffers, indent=4))
        dict_buffers.clear()
        sys.exit(0)
    if (ctx.opts.candil_yang_identities_generator_output_mode == OUTPUT_MODE_KAFKA):
        if (ctx.opts.candil_yang_identities_generator_kafka_server is not None) and \
        (ctx.opts.candil_yang_identities_generator_kafka_topic is not None):
            producer = KafkaProducer(bootstrap_servers=[ctx.opts.candil_yang_identities_generator_kafka_server])
            producer.send(ctx.opts.candil_yang_identities_generator_kafka_topic, value=json.dumps(dict_buffers, indent=4).encode("utf-8"))
            producer.flush()
            dict_buffers.clear()
            sys.exit(0)
