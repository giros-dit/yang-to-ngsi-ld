"""
pyang plugin -- NGSI-LD Context generator.

Generates the NGSI-LD Context associated with a YANG module file following the defined guidelines and conventions.
It can output the result in the command line or save it in a .jsonld file.

Version: 0.0.2.

Author: Networking and Virtualization Research Group (GIROS DIT-UPM) -- https://dit.upm.es/~giros
"""

import optparse
import sys
import re
import pdb
import json

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
        if ctx.opts.help:
            print_help()
            sys.exit(0)
        """

    def setup_fmt(self, ctx):
        ctx.implicit_errors = False

    def emit(self, ctx, modules, fd):
        emit_ngsi_ld_context(ctx, modules, fd)

def print_help():
    print("""
            TO-DO
        """)
          
def emit_ngsi_ld_context(ctx, modules, fd):

    # Use PDB to debug the code:
    # pdb.set_trace()

    json_ld = {}
    json_ld['@context'] = []
    ngsi_ld_context = {}
    ngsi_ld_core_context_uri = "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.6.jsonld"

    def generate_context(element, fd):
        if (element is not None) and (element.keyword in statements.data_definition_keywords):
            return None
    
    def print_structure(element, fd):
        if (element is not None) and (element.keyword in statements.data_definition_keywords):
            fd.write(element.arg + ' is of type ' + element.keyword)
            if (element.keyword == 'leaf' or element.keyword == 'leaf-list'):
                fd.write(' and data type is ' + element.search_one('type').arg + '\n')
            else:
                fd.write('\n')
                subelements = element.i_children
                if subelements is not None:
                    for subelement in subelements:
                        status = subelement.search_one('status')
                        if (status is None) or (status.arg != 'deprecated'):
                            print_structure(subelement, fd)
    
    # Print YANG module structure:
    for module in modules:
        fd.write(module.arg + ' is of type ' + module.keyword + ' with URN: ' + module.search_one('namespace').arg + '\n\n')
        elements = module.i_children
        if (elements is not None):
            for element in elements:
                print_structure(element, fd)
        fd.write('\n\n')
