# YANG to NGSI-LD for Descriptive NDT
Repository with source code, artifacts and documentation about YANG to NGSI-LD translation. This translation process is the baseline for modeling a *Descriptive Network Digital Twin (NDT)* solution by means of the NGSI-LD standard specified by ETSI ISG CIM.

## Descriptive NDT architecture
The proposed *Descriptive NDT* architecture covers the core elements of NDT described by the IETF [[1](https://datatracker.ietf.org/doc/html/draft-irtf-nmrg-network-digital-twin-arch-05)] and the *descriptive twin* vision provided by ETSI ISG CIM and its NGSI-LD standard specification [[2](https://www.etsi.org/deliver/etsi_gr/CIM/001_099/017/01.01.01_60/gr_CIM017v010101p.pdf)].The solution proposes an automated methodology for mapping data from network the management domain to a digitalized representation, following a data materialization approach supported by the NGSI-LD standard. 

![DescriptiveNDT-Arch-DataMaterialization](resources/images/DescriptiveNDT-Arch-DataMaterialization.png)

### Descriptive NDT prototype implementation
The implementation of this *Descriptive NDT* architecture is mainly based on the use of the OpenAPI Specification (OAS) compatible with the NGSI-LD API [3]. The OAS allows modeling the NDT data schemas, as well as generate a client library with programmable code that makes use of the NGSI-LD API and the generated schemas for instantiating the resulting NDT data. The related programming code is implemented in Python, a language that also facilitates the libraries (e.g., *pyang* [4], *yangtools* [5], and *pydantic* [6]) to parse the YANG Modeled Data to complete the mapping process to NGSI-LD Modeled Data. 

![YANG-to-NGSI-LD-translation](resources/images/YANG-to-NGSI-LD-translation.png)

The prototype separates its functionality into two main planes: *NDT Generator Plane* and *NDT Data Pipeline Plane*. The *NDT Generator Plane* general functionality consists in processing the native data models of the Real-World Network (i.e., *YANG Schemas*) in order to generate different programmed artifacts that allow performing the YANG to NGSI-LD translation in an autonomous way. Then, the *NDT Data Pipeline Plane* makes use of the programmed artifacts to be able to parse the raw configuration and operational data coming from network assets and generate NGSI-LD compliant data.

## Developed _pyang_ plugins:
- [candil-ngsi-ld-context-generator.py](yang/pyang-plugins/candil-ngsi-ld-context-generator.py): given one or several YANG modules, it generates the corresponding NGSI-LD context files in ```.jsonld``` format.
- [candil-xml-parser-generator.py](yang/pyang-plugins/candil-xml-parser-generator.py): given one or several YANG modules, it generates the Python code of an XML parser that reads data modeled by these modules and generates the corresponding NGSI-LD Entity data structures (dictionary buffers). XML Parser Generator for operational status and configuration information received from NETCONF Query RPCs, and also for telemetry notifications received from NETCONF YANG-Push Subscriptions.
- [candil-yang-identities-generator.py](yang/pyang-plugins/candil-yang-identities-generator.py): given one or several YANG modules, it generates the corresponding NGSI-LD Entity data structures (dictionary buffers) for YANG identities.
- [candil-json-parser-generator-queries.py](yang/pyang-plugins/candil-json-parser-generator-queries.py): given one or several YANG modules, it generates the Python code of an JSON parser that reads data modeled by these modules and generates the corresponding NGSI-LD Entity data structures (dictionary buffers). JSON Parser Generator for operational status and configuration information received from gNMI Query RPCs.
- [candil-json-parser-generator-notifications.py](yang/pyang-plugins/candil-json-parser-generator-notifications.py): given one or several YANG modules, it generates the Python code of an JSON parser that reads data modeled by these modules and generates the corresponding NGSI-LD Entity data structures (dictionary buffers). JSON Parser Generator for telemetry notifications received from gNMI Subscription RPCs.
- [candil-openapi-schemas-generator.py](yang/pyang-plugins/candil-openapi-schemas-generator.py): given one or several YANG modules, it dynamically generates the relative OpenAPI Schemas according to the OpenAPI specification for NGSI-LD API V1.6.1.
- [candil-json-parser-generator.py](yang/pyang-plugins/candil-json-parser-generator.py): given one or several YANG modules, it generates the Python code of an JSON parser that reads data modeled by these modules and generates the corresponding NGSI-LD Entity data structures (dictionary buffers). JSON Parser Generator for non-gNMI data modeled according to YANG modules. This means it is valid for data in JSON format that does not come from the gNMI protocol but is supported by IETF YANG models, OpenConfig YANG models, or vendor proprietary YANG models. ```Supported extra data sources: NetFlow v9 and Network Topologies```.

## Developed _yangtools_ artifacts:
- [TopologyDriver.java](yang/yang-tools-artifacts/topology-discoverer/topology-driver/src/main/java/upm/dit/giros/TopologyDriver.java): Java application based on the YANG Tools library for parsing data from network topology descriptor based on the ContainerLab [7] simulation testbed and mapping it to YANG-compliant data according to the ietf-network and ietf-network-topology YANG data models ([RFC 8345](https://datatracker.ietf.org/doc/html/rfc8345)).
  
## Documentation and links
1. ETSI, “Context Information Management (CIM); Feasibility of NGSI-LD for Digital Twins,” *GR CIM 017 v1.1.1*, ETSI, Dec. 2022.
2. C. Zhou et al., “Network Digital Twin: Concepts and Reference Architecture,” *Internet-Draft draft-irtf-nmrg-network-digital-twin-arch-05*, Internet Engineering Task Force, Mar. 2024. Work in Progress.
3. OpenAPI specification for the NGSI-LD API specified by ETSI ISG CIM 009: https://forge.etsi.org/rep/cim/ngsi-ld-openapi/-/tree/1.6.1
4. pyang: https://github.com/mbj4668/pyang
5. YANG Tools: https://github.com/opendaylight/yangtools
6. pydantic: https://docs.pydantic.dev/latest/
7. ContainerLab: https://containerlab.dev/
8. pyangbind: https://github.com/robshakir/pyangbind
9. poetry: https://python-poetry.org
