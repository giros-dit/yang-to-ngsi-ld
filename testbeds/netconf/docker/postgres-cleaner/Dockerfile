# Custom Dockerfile for postgres-cleaner

FROM ubuntu:latest

RUN apt update && apt -y dist-upgrade && apt -y autoremove && apt autoclean

RUN apt install --no-install-recommends -y bash net-tools iputils-ping python3 python3-pip

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install psycopg2-binary python-dateutil urllib3 requests pyyaml

RUN mkdir -p /opt/postgres_cleaner

WORKDIR /opt/postgres_cleaner

COPY * /opt/postgres_cleaner