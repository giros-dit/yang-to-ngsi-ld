# Custom Dockerfile for gnmi-json-parser-queries-with-ngsi-ld-instantiator-materialization

#FROM ubuntu:latest
FROM ubuntu:22.04

RUN apt update && apt -y dist-upgrade && apt -y autoremove && apt autoclean

RUN apt install --no-install-recommends -y bash net-tools iputils-ping python3 python3-pip

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install poetry

RUN mkdir -p /opt/gnmi-json-parser-queries-with-ngsi-ld-instantiator-materialization

WORKDIR /opt/gnmi-json-parser-queries-with-ngsi-ld-instantiator-materialization

COPY ./docker/gnmi-json-parser-queries-with-ngsi-ld-instantiator-materialization .

WORKDIR /opt/gnmi-json-parser-queries-with-ngsi-ld-instantiator-materialization/ngsi-ld-models

RUN poetry install --no-root

WORKDIR /opt/gnmi-json-parser-queries-with-ngsi-ld-instantiator-materialization

RUN poetry install --no-root

RUN cp candil-yang-identities-generator.py /root/.cache/pypoetry/virtualenvs/gnmi-json-parser-queries-with-ngsi-ld-*/lib/python3.10/site-packages/pyang/plugins/

ENTRYPOINT ["poetry", "run", "python", "-u", "candil_openconfig_interfaces_ngsi_ld_instantiator.py"]
