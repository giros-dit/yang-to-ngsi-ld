# Custom Dockerfile for xml-parser-with-ngsi-ld-instantiator

FROM ubuntu:22.04

RUN apt update && apt -y dist-upgrade && apt -y autoremove && apt autoclean

RUN apt install --no-install-recommends -y bash net-tools iputils-ping python3 python3-pip

RUN python3 -m pip install --upgrade pip 

RUN python3 -m pip install poetry 

RUN mkdir -p /opt/xml-parser-with-ngsi-ld-instantiator-virtualization

WORKDIR /opt/xml-parser-with-ngsi-ld-instantiator-virtualization

COPY ./docker/xml-parser-with-ngsi-ld-instantiator-virtualization .

WORKDIR /opt/xml-parser-with-ngsi-ld-instantiator-virtualization/ngsi-ld-models-ietf-interfaces

RUN poetry install

WORKDIR /opt/xml-parser-with-ngsi-ld-instantiator-virtualization

RUN poetry install

ENTRYPOINT ["poetry", "run", "python", "-u", "xml-parser-with-ngsi-ld-instantiator.py"]
