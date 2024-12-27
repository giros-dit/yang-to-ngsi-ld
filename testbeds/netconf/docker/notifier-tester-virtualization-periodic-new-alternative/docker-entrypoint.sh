#!/bin/sh

set -e

# activate our virtual environment here
. /venv/bin/activate

exec uvicorn notifier_tester_virtualization_periodic_new_alternative.main:app --host 0.0.0.0 \
     --port 8082 --reload \
     --log-config notifier_tester_virtualization_periodic_new_alternative/config/log.yaml
