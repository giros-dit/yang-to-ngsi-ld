#!/bin/sh

set -e

# activate our virtual environment here
. /venv/bin/activate

exec uvicorn netconf_notifier_tester_virtualization_periodic_context_broker.main:app --host 0.0.0.0 \
     --port 8082 --reload \
     --log-config netconf_notifier_tester_virtualization_periodic_context_broker/config/log.yaml
