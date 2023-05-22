# NGSI-LD Data Models

The NGSI-LD protocol encodes data using the JSON-LD format. For this reason, data models associated with NGSI-LD entities can be formally specified using JSON schema.

In this repository, we provide JSON schemas arranged per domain. For example, the [schemas/interfaces](schemas/interfaces/) folder, contains data models derived from the NGSI-LD information model that captures context information related to the interfaces of a model-based network device supporting the [_ietf-interfaces_ YANG module](../../yang/modules/ietf-interfaces%402018-02-20.yang) as depicted [here](../information-models/interfaces-ngsi-ld-schema-if-reduced.png).

## Repository structure

The structure of the repository is arranged into the following main folders:
- `schemas`: Contains JSON schemas for each domain, e.g., [IETF Interfaces JSON schema](schemas/interfaces/interface.json).
- `examples`: Contains examples of JSON-LD payloads for each domain, e.g., [IETF Interface example](examples/interfaces/interface/example-normalized.json).
- `context`: Contains JSON-LD context vocabulary for each domain, e.g., [IETF Interfaces Context](context/interfaces/context.jsonld).
- `bindings`: Contains Python class bindings (using [`pydantic`](https://docs.pydantic.dev/latest/) library) for each domain, e.g., [Interface class](bindings/interfaces/interface.py).
- `tests`: Contains Python unit tests that allow to validate example JSON-LD payloads against the respective class bindings, e.g., [IETF Interfaces tests](tests/interfaces.py).

## NGSI-LD Core (meta model)

When defining domain-specific JSON schemas, these must inherit the NGSI-LD meta model, which in is also known as the core domain. The meta model defines the foundational NGSI-LD elements Entity, Property, and Relationship.

In this sense, ETSI CIM exposes a public GitLab repository that contains [JSON schemas for the NGSI-LD API](https://forge.etsi.org/rep/NGSI-LD/NGSI-LD/-/tree/master/schema). However, the current specification of the [meta model](https://forge.etsi.org/rep/NGSI-LD/NGSI-LD/-/blob/master/schema/Entity.json) contains errors in its JSON schema, specifically in the `definitions.Property.properties.value.oneOf` line. Therefore, we decided to locally "fork" these JSON schemas and made the necessary adjustments to make the schemas valid. This local fork can be found in the [entity.json](schemas/entity.json) file.

In addition,[common.json](schemas/common.json), [geometry.json](schemas/geometry.json),[subscription.json](schemas/subscription.json), and [notification.json](schemas/notification.json) schemas file have been forked from [upstream](https://forge.etsi.org/rep/NGSI-LD/NGSI-LD/-/tree/master/schema). Files have been modified to reference local files, and also, the `format: uri` has been removed as this format is not compatible with `pydantic` library.

## How to generate Python bindings from JSON schema

Once we have defined JSON schemas for data models, we want to parse and validate NGSI-LD payloads that follow the specified data models in programatic way. To this end, we must generate class bindings from JSON schemas using the Python programming language. The [datamode-code-generator](https://koxudaxi.github.io/datamodel-code-generator/) is a tool to generate `pydantic` models from OpenAPI and JSON schema specifications.

### Poetry installation and configuration

This repository includes a [`poetry`](https://python-poetry.org) manifest that can be leveraged to run `datamode-code-generator` within an isolated virtual environment. To do so, follow these steps:

1. Download and install `poetry` by following the [official documentacion](https://python-poetry.org/docs/master/#installing-with-the-official-installer).
2. Make sure you have the right Python version for this project (Python>3.9 in this case):
     ```bash
    $ sudo apt-get install python3.9
    ```
3. Install `distutils` package for your specific Python release:
    ```bash
    $ sudo apt-get install python3-distutils
    ```
4. Install `python-is-python3` package (symlinks /usr/bin/python to Python3 as specified in [link 1](https://askubuntu.com/questions/1296790/python-is-python3-package-in-ubuntu-20-04-what-is-it-and-what-does-it-actually) and [link 2](https://stackoverflow.com/questions/61921940/running-poetry-fails-with-usr-bin-env-python-no-such-file-or-directory)):
    ```bash
    $ sudo apt-get install python-is-python3
    ```
5. Enable virtual environment for your specific Python release:
    ```bash
    $ poetry env use 3.9
    ```
6. Setup the virtual environment with poetry:
    ```bash
    $ poetry shell
    $ poetry install
    ```
The virtual environment is now prepared and activated to be used.

### Code generation

For our use case, we generate these models from the JSON schemas defined for each domain as follows:
```bash
$ datamodel-codegen --input schemas --input-file-type jsonschema --output bindings --aliases datamodel-codegen/aliases.json --custom-template-dir datamodel-codegen/templates
```
This command will generate Python class bindings for all JSON schemas found within the [`schemas` folder](schemas/).

### Validation tests

For validating example JSON-LD payloads (e.g., [IETF Interfaces examples](examples/interfaces/)) against the autogenerated Python class bindings, run 
the Python unit test as follows:
```bash
$ python tests/interfaces.py
```
