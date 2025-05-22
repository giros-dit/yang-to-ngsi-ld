# Custom Dockerfile for netconf-xml-parser-with-ngsi-ld-instantiator

FROM ubuntu:22.04

RUN apt update && apt -y dist-upgrade && apt -y autoremove && apt autoclean

RUN apt install --no-install-recommends -y bash net-tools iputils-ping python3 python3-pip

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install poetry

RUN mkdir -p /opt/netconf-xml-parser-with-ngsi-ld-instantiator-materialization

WORKDIR /opt/netconf-xml-parser-with-ngsi-ld-instantiator-materialization

COPY ./docker/netconf-xml-parser-with-ngsi-ld-instantiator-materialization .

WORKDIR /opt/netconf-xml-parser-with-ngsi-ld-instantiator-materialization/ngsi-ld-models-ietf-interfaces

RUN poetry install --no-root

WORKDIR /opt/netconf-xml-parser-with-ngsi-ld-instantiator-materialization

RUN poetry install --no-root

ENTRYPOINT ["poetry", "run", "python", "-u", "xml-parser-with-ngsi-ld-instantiator.py"]
