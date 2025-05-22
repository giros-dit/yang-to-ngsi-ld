#!/bin/sh

set -e

# activate our virtual environment here
. /venv/bin/activate

exec uvicorn netconf_network_controller_virtualization.main:app --host 0.0.0.0 \
     --port 8089 --reload \
     --log-config netconf_network_controller_virtualization/config/log.yaml
