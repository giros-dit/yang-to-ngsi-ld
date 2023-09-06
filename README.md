# YANG to NGSI-LD (for CANDIL)
Repository with source code, artifacts and documentation about YANG to NGSI-LD translation.

![](resources/images/YANG-to-NGSI-LD-translation.png)

## Developed _pyang_ plugins:
- [candil-ngsi-ld-context-generator.py](yang/pyang/candil-ngsi-ld-context-generator.py): given one or several YANG modules, it generates the corresponding NGSI-LD context files in ```.jsonld``` format.
- [candil-xml-parser-generator.py](yang/pyang/candil-xml-parser-generator.py): given one or several YANG modules, it generates the Python code of an XML parser that reads data modeled by these modules and generates the corresponding NGSI-LD Entity data structures.

## Documentation and links
- pyang: https://github.com/mbj4668/pyang
- pyangbind: https://github.com/robshakir/pyangbind
- pydantic: https://docs.pydantic.dev/latest/
- poetry: https://python-poetry.org
- OpenAPI specification for the NGSI-LD API specified by ETSI ISG CIM 009: https://forge.etsi.org/rep/NGSI-LD/NGSI-LD/-/tree/1.6.1
