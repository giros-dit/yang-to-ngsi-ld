# Custom Dockerfile for ngsi-ld-cleaner

FROM ubuntu:latest

RUN apt update && apt -y dist-upgrade && apt -y autoremove && apt autoclean

RUN apt install --no-install-recommends -y bash net-tools iputils-ping python3 python3-pip

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install poetry

RUN mkdir -p /opt/ngsi-ld-cleaner

WORKDIR /opt/ngsi-ld-cleaner

COPY ./docker/ngsi-ld-cleaner .

WORKDIR /opt/ngsi-ld-cleaner

RUN poetry install