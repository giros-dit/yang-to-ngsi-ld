#!/bin/sh

set -e

# activate our virtual environment here
. /venv/bin/activate

exec uvicorn multi_query_tester.main:app --host 0.0.0.0 \
     --port 8083 --reload \
     --log-config multi_query_tester/config/log.yaml