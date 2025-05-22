#!/bin/sh

set -e

# activate our virtual environment here
. /venv/bin/activate

exec uvicorn query_tester_materialization.main:app --host 0.0.0.0 \
     --port 8083 --reload \
     --log-config query_tester_materialization/config/log.yaml
