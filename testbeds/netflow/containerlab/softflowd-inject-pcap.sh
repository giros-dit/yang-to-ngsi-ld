#!/bin/bash

echo 'Running softflowd ...'

docker exec clab-telemetry-testbed-xe-ceos-4hosts-r1 bash -c "mkdir -p /usr/local/etc/softflowd"

docker cp capture+crypto+type2+8+vlan.pcap clab-telemetry-testbed-xe-ceos-4hosts-r1:/usr/local/etc/softflowd/.

sleep 1

docker exec clab-telemetry-testbed-xe-ceos-4hosts-r1 bash -c "/usr/local/sbin/softflowd -d -r /usr/local/etc/softflowd/capture+crypto+type2+8+vlan.pcap -v 9 -t maxlife=30s -T ether -n goflow2:9995" &

sleep 1

echo 'Done!'
