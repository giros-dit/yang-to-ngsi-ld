# Custom Dockerfile for xml-parser

FROM ubuntu:latest

RUN apt update && apt -y dist-upgrade && apt -y autoremove && apt autoclean

RUN apt install --no-install-recommends -y bash net-tools iputils-ping python3 python3-pip

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install kafka-python python-dateutil

RUN mkdir -p /opt/xml-parser

WORKDIR /opt/xml-parser

COPY xml-parser.py .
COPY docker-entrypoint.sh .

RUN chmod +x docker-entrypoint.sh

ENTRYPOINT ["/bin/bash", "docker-entrypoint.sh"]