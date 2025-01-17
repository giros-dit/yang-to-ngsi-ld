# Custom Dockerfile for fake-ncclient-collector-subscriptions

FROM ubuntu:22.04

RUN apt update && apt -y dist-upgrade && apt -y autoremove && apt autoclean

RUN apt install --no-install-recommends -y bash net-tools iputils-ping python3 python3-pip

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install kafka-python

RUN mkdir -p /opt/fake-gnmic-collector-subscriptions

WORKDIR /opt/fake-gnmic-collector-subscriptions

COPY * /opt/fake-gnmic-collector-subscriptions/