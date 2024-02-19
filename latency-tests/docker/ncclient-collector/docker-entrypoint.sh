#!/bin/sh

set -e

# activate our virtual environment here
. /venv/bin/activate

exec python csr-create-periodic-subscription-interfaces-state-kafka.py clab-telemetry-ixiac-lab-r1 GigabitEthernet1 100