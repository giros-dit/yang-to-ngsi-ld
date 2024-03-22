#!/bin/bash

echo 'Running softflowd ...'

docker exec clab-telemetry-testbed-xe-ceos-4hosts-r1 bash -c "/usr/local/sbin/softflowd -d -i eth1 -v 9 -t maxlife=30s -T ether -n goflow2:9995" &

sleep 1

echo 'Done!'
