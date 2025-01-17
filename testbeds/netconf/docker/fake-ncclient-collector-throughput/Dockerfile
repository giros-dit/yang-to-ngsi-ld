# Custom Dockerfile for ncclient-collector

FROM ubuntu:22.04

RUN apt update && apt -y dist-upgrade && apt -y autoremove && apt autoclean

RUN apt install --no-install-recommends -y bash net-tools iputils-ping python3 python3-pip

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install ncclient kafka-python python-dateutil

RUN mkdir -p /opt/fake-ncclient-collector

WORKDIR /opt/fake-ncclient-collector

COPY * /opt/fake-ncclient-collector