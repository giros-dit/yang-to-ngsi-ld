# Custom Dockerfile for gnmi-json-parser-notifications-with-ngsi-ld-instantiator-virtualization

#FROM ubuntu:latest
FROM ubuntu:22.04

RUN apt update && apt -y dist-upgrade && apt -y autoremove && apt autoclean

RUN apt install --no-install-recommends -y bash net-tools iputils-ping python3 python3-pip

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install poetry

RUN mkdir -p /opt/gnmi-json-parser-notifications-with-ngsi-ld-instantiator-virtualization

WORKDIR /opt/gnmi-json-parser-notifications-with-ngsi-ld-instantiator-virtualization

COPY ./docker/gnmi-json-parser-notifications-with-ngsi-ld-instantiator-virtualization .

WORKDIR /opt/gnmi-json-parser-notifications-with-ngsi-ld-instantiator-virtualization/ngsi-ld-models

RUN poetry install --no-root

WORKDIR /opt/gnmi-json-parser-notifications-with-ngsi-ld-instantiator-virtualization

RUN poetry install --no-root

ENTRYPOINT ["poetry", "run", "python", "-u", "candil_openconfig_interfaces_ngsi_ld_instantiator.py"]
