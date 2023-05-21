"""
pyang plugin -- NGSI-LD Context generator.

Generates a .jsonld file with the NGSI-LD Context associated with a YANG module file.

Version: 0.0.1.

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
        Do nothing for now
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
    
    def print_structure(element, fd):
        if element is not None:
            fd.write(element.arg + ' is of type ' + element.keyword)
            if (element.keyword == 'leaf' or element.keyword == 'leaf-list'):
                fd.write(' and data type is ' + element.search_one('type').arg + '\n')
            else:
                if (element.keyword == 'module'):
                    fd.write(' with URN: ' + element.search_one('namespace').arg + '\n\n')
                else:
                    fd.write('\n')
                subelements = element.i_children
                if subelements is not None:
                    for subelement in subelements:
                        #print_structure(subelement, fd)
                        status = subelement.search_one('status')
                        if (status is None) or (status.arg != 'deprecated'):
                            print_structure(subelement, fd)
            
    
    # pdb.set_trace()
    
    for module in modules:
        print_structure(module, fd)
    

