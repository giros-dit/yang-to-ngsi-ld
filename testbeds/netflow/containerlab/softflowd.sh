#!/bin/bash

USAGE="
Usage:
./softflowd.sh <container-name> <interface-name>
    being:
        <container-name>: the name of the containerized service where to run the softflowd NetFlow Exporter.
        <interface-name>: the name of the interface where capturing the network flows.
    
    Example: ./softflowd.sh clab-telemetry-testbed-xe-ceos-4hosts-r1 eth1
"

echo 'Running softflowd ...'

if [[ $# -ne 2 ]]; then
    echo ""
    echo "ERROR: incorrect number of parameters."
    echo "$USAGE"
    exit 1
fi

docker exec $1 bash -c "/usr/local/sbin/softflowd -d -i $2 -v 9 -t maxlife=30s -T ether -n goflow2:9995" &

sleep 1

echo 'Done!'