# YANG to NGSI-LD (for CANDIL)
Repository with source code, artifacts and documentation about YANG to NGSI-LD translation.

![](resources/images/YANG-to-NGSI-LD-translation.png)

## Developed _pyang_ plugins:
- [candil-ngsi-ld-context-generator.py](yang/pyang/candil-ngsi-ld-context-generator.py): given one or several YANG modules, it generates the corresponding NGSI-LD context files in ```.jsonld``` format.
- [candil-xml-parser-generator.py](yang/pyang/candil-xml-parser-generator.py): given one or several YANG modules, it generates the Python code of an XML parser that reads data modeled by these modules and generates the corresponding NGSI-LD Entity data structures (dictionary buffers). XML Parser Generator for operational status and configuration information received from NETCONF Query RPCs, and also for telemetry notifications received from NETCONF YANG-Push Subscriptions.
- [candil-yang-identities-generator.py](yang/pyang/candil-yang-identities-generator.py): given one or several YANG modules, it generates the corresponding NGSI-LD Entity data structures (dictionary buffers) for YANG identities.
- [candil-json-parser-generator-queries.py](yang/pyang/candil-json-parser-generator-queries.py): given one or several YANG modules, it generates the Python code of an JSON parser that reads data modeled by these modules and generates the corresponding NGSI-LD Entity data structures (dictionary buffers). JSON Parser Generator for operational status and configuration information received from a gNMI Query RPCs.
- [candil-json-parser-generator-notifications.py](yang/pyang/candil-json-parser-generator-notifications.py): given one or several YANG modules, it generates the Python code of an JSON parser that reads data modeled by these modules and generates the corresponding NGSI-LD Entity data structures (dictionary buffers). JSON Parser Generator for telemetry notifications received from a gNMI Subscription RPCs.
- [candil-openapi-schemas-generator.py](yang/pyang/candil-openapi-schemas-generator.py): given one or several YANG modules, it dynamically generates the relative OpenAPI Schemas according to the OpenAPI specification for NGSI-LD API V1.6.1.
- [candil-json-parser-generator.py](yang/pyang/candil-json-parser-generator.py): given one or several YANG modules, it generates the Python code of an JSON parser that reads data modeled by these modules and generates the corresponding NGSI-LD Entity data structures (dictionary buffers). JSON Parser Generator for non-gNMI data modelled according to YANG modules. This means it is valid for data in JSON format that does not come from the gNMI protocol but is supported by IETF YANG models, OpenConfig YANG models, or vendor proprietary YANG models. ```Supported data sources: NetFlow v9 and Network Topologies```.

## Documentation and links
- pyang: https://github.com/mbj4668/pyang
- pyangbind: https://github.com/robshakir/pyangbind
- pydantic: https://docs.pydantic.dev/latest/
- poetry: https://python-poetry.org
- OpenAPI specification for the NGSI-LD API specified by ETSI ISG CIM 009: https://forge.etsi.org/rep/NGSI-LD/NGSI-LD/-/tree/1.6.1
- YANG Tools: https://github.com/opendaylight/yangtools