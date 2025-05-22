# Custom Dockerfile for fake-goflow2-collector

#FROM ubuntu:latest
FROM ubuntu:22.04

RUN apt update && apt -y dist-upgrade && apt -y autoremove && apt autoclean

RUN apt install --no-install-recommends -y bash net-tools iputils-ping python3 python3-pip curl iperf3

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install kafka-python==2.1.5

RUN mkdir -p /opt/fake-goflow2-collector

WORKDIR /opt/fake-goflow2-collector

COPY * /opt/fake-goflow2-collector/