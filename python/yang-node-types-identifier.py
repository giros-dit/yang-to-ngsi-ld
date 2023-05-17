# Python script: yang-node-types-identifier.py.
# Author: David Martínez García.
# Author: Networking and Virtualization Research Group (GIROS DIT-UPM).
# Version: 0.1.
#
# Reads a YANG file in text mode and, by processing it line by line,
# identifies the types of all data nodes in the module.
# It doesn't require any external libraries or dependencies.
# The result is stored in a dictionary and written to a JSON file.
# As of now, it only identifies the following data types: container, list, leaf-list and leaf;
# although it works for any other type that may be defined in the YANG module.

import sys
import json

def parse_yang_file(yang_file_path: str) -> dict:
    yang = open(yang_file_path, 'r')
    node_types = ['container', 'list', 'leaf-list', 'leaf']
    result = {}
    lines = yang.readlines()
    for line in lines:
        line = line.strip()
        line = line.split()
        if len(line) == 3 and line[2] == '{' and line[0] in node_types:
            print(line[1] + ' is of type ' + line[0])
            result[line[1]] = line[0]
            print('Added to dictionary\n')
    return result

def write_node_types_dictionary_to_file(output_file_path: str, node_types_dict: dict) -> None:
    output_file = open(output_file_path, 'w+')
    output_file.write(json.dumps(node_types_dict))

if len(sys.argv) < 3:
    print("Error: incorrect arguments.")
    print("Usage: python3 yang-node-type-identifier.py <path-to-yang-file> <path-to-output-file>")
    print("<path-to-yang-file>: absolute or relative path to the YANG file to process.")
    print("<path-to-output-file>: absolute or relative path where to store the dictionary with the identified data node types (JSON file)")
    print("Example: python3 yang-node-type-identifier.py yang/ietf-interfaces.yang output/ietf-interfaces.json")
    exit(1)
else:
    yang_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

node_types_dict = parse_yang_file(yang_file_path)
write_node_types_dictionary_to_file(output_file_path, node_types_dict)

