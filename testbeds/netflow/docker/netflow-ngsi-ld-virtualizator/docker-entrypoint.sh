#!/bin/sh

set -e

# activate our virtual environment here
. /venv/bin/activate

exec uvicorn netflow_ngsi_ld_virtualizator.main:app --host 0.0.0.0 \
     --port 8089 --reload \
     --log-config netflow_ngsi_ld_virtualizator/config/log.yaml
