# Custom Dockerfile for topology-discoverer

#FROM ubuntu:latest
FROM ubuntu:22.04

RUN apt update --fix-missing && apt -y dist-upgrade && apt -y autoremove && apt autoclean

RUN apt install --no-install-recommends -y bash net-tools iputils-ping default-jre default-jdk python3 python3-pip

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install poetry

RUN mkdir -p /opt/topology-discoverer

WORKDIR /opt/topology-discoverer

COPY ./docker/topology-discoverer .

WORKDIR /opt/topology-discoverer/ngsi-ld-models

RUN poetry install --no-root

WORKDIR /opt/topology-discoverer

RUN poetry install --no-root

RUN chmod +x discover-topology.sh