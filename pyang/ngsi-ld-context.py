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
    printed_header = False

    def print_header(module):
        nonlocal printed_header
        if not printed_header:
            bstr = ""
            b = module.search_one('belongs-to')
            if b is not None:
                bstr = " (belongs-to %s)" % b.arg
            fd.write("%s: %s%s\n" % (module.keyword, module.arg, bstr))
            printed_header = True
    
    pdb.set_trace()
    
    for module in modules:
        if printed_header:
            fd.write("\n")
        childrens = [children for children in module.i_children
                     if children.keyword in statements.data_definition_keywords]
        if len(childrens) > 0:
            print_header(module)
            for children in childrens:
                fd.write(str(children) + "\n")
                grandsons = [grandson for grandson in children.i_children
                             if grandson.keyword in statements.data_definition_keywords]
                if len(grandsons) > 0:
                    for grandson in grandsons:
                        fd.write(str(grandson) + "\n")

