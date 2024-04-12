#!/bin/bash

USAGE="
Usage:
./inject-traffic.sh <container-name>
    being:
        <container-name>: the name of the containerized host where to inject real traffic.
    
    Example: ./inject-traffic.sh clab-telemetry-testbed-xrv9k-ceos-4hosts-pc11
"

if [[ $# -ne 1 ]]; then
    echo ""
    echo "ERROR: incorrect number of parameters."
    echo "$USAGE"
    exit 1
fi

echo 'Injecting real traffic from $1 to r1 ...'

docker cp traffic.sh $1:.

sleep 1

docker exec $1 bash -c "./traffic.sh"

sleep 1