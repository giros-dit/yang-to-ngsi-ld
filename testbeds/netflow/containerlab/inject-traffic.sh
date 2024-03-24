#!/bin/bash

docker cp traffic.sh clab-telemetry-testbed-xe-ceos-4hosts-pc11:.

sleep 1

docker exec clab-telemetry-testbed-xe-ceos-4hosts-pc11 bash -c "./traffic.sh"

sleep 1