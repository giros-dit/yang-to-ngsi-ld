# Custom Dockerfile for gnmi-json-parser-queries-with-ngsi-ld-instantiator

FROM ubuntu:latest

RUN apt update && apt -y dist-upgrade && apt -y autoremove && apt autoclean

RUN apt install --no-install-recommends -y bash net-tools iputils-ping python3 python3-pip

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install poetry

RUN mkdir -p /opt/gnmi-json-parser-queries-with-ngsi-ld-instantiator

WORKDIR /opt/gnmi-json-parser-queries-with-ngsi-ld-instantiator

COPY ./docker/gnmi-json-parser-queries-with-ngsi-ld-instantiator .

WORKDIR /opt/gnmi-json-parser-queries-with-ngsi-ld-instantiator/ngsi-ld-models

RUN poetry install

WORKDIR /opt/gnmi-json-parser-queries-with-ngsi-ld-instantiator

RUN poetry install

RUN cp candil-yang-identities-generator.py /root/.cache/pypoetry/virtualenvs/openconfig-ngsi-ld-instantiator-queries-*/lib/python3.10/site-packages/pyang/plugins/

ENTRYPOINT ["poetry", "run", "python", "-u", "candil_openconfig_interfaces_ngsi_ld_instantiator.py"]
