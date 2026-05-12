#!/bin/bash

USAGE="
Usage:
./docker-stats.sh <interval>
    being:
        <interval>: the interval in seconds between each docker container health check iteration..
    
    Example: ./docker-stats.sh 5 or ./docker-stats.sh 5 & (for running the script in background)
"

if [[ $# -ne 1 ]]; then
    echo ""
    echo "ERROR: incorrect number of parameters."
    echo "$USAGE"
    exit 1
fi

while true; do
    docker stats --no-stream -a >> docker-stats-gnmi-testbed.csv
    sleep $1
done