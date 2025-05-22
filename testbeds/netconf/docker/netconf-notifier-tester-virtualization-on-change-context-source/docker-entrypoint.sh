#!/bin/sh

set -e

# activate our virtual environment here
. /venv/bin/activate

exec uvicorn netconf_notifier_tester_virtualization_on_change_context_source.main:app --host 0.0.0.0 \
     --port 8082 --reload \
     --log-config netconf_notifier_tester_virtualization_on_change_context_source/config/log.yaml
