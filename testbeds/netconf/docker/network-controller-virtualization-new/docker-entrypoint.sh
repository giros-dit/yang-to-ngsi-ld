#!/bin/sh

set -e

# activate our virtual environment here
. /venv/bin/activate

exec uvicorn network_controller_virtualization_new.main:app --host 0.0.0.0 \
     --port 8089 --reload \
     --log-config network_controller_virtualization_new/config/log.yaml
