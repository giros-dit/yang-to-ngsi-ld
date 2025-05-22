# Custom Dockerfile for netflow-json-parser-with-ngsi-ld-instantiator-simple

#FROM ubuntu:latest
FROM ubuntu:22.04

RUN apt update && apt -y dist-upgrade && apt -y autoremove && apt autoclean

RUN apt install --no-install-recommends -y bash net-tools iputils-ping python3 python3-pip

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install poetry

RUN mkdir -p /opt/netflow-json-parser-with-ngsi-ld-instantiator-simple

WORKDIR /opt/netflow-json-parser-with-ngsi-ld-instantiator-simple

COPY ./docker/netflow-json-parser-with-ngsi-ld-instantiator-simple .

WORKDIR /opt/netflow-json-parser-with-ngsi-ld-instantiator-simple/ngsi-ld-models

RUN poetry install --no-root

WORKDIR /opt/netflow-json-parser-with-ngsi-ld-instantiator-simple

RUN poetry install --no-root

ENTRYPOINT ["poetry", "run", "python", "-u", "candil_netflow_ngsi_ld_instantiator.py"]
