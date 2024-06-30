# Custom Dockerfile for fake-ncclient-collector-queries

FROM ubuntu:latest

RUN apt update && apt -y dist-upgrade && apt -y autoremove && apt autoclean

RUN apt install --no-install-recommends -y bash net-tools iputils-ping python3 python3-pip curl iperf3

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install kafka-python

RUN mkdir -p /opt/fake-gnmic-collector-queries

WORKDIR /opt/fake-gnmic-collector-queries

COPY * /opt/fake-gnmic-collector-queries/