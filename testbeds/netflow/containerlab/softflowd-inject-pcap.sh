#!/bin/bash

USAGE="
Usage:
./softflowd-inject-pcap.sh <container-name>
    being:
        <container-name>: the name of the containerized service where to run the softflowd NetFlow Exporter injecting synthetic traffic.
    
    Example: ./softflowd-inject-pcap.sh clab-telemetry-testbed-xe-ceos-4hosts-r1
"

echo 'Running softflowd with synthetic traffic injected from a pcap file...'

if [[ $# -ne 1 ]]; then
    echo ""
    echo "ERROR: incorrect number of parameters."
    echo "$USAGE"
    exit 1
fi

docker exec $1 bash -c "mkdir -p /usr/local/etc/softflowd"

docker cp capture+crypto+type2+8+vlan.pcap $1:/usr/local/etc/softflowd/.

sleep 1

docker exec $1 bash -c "/usr/local/sbin/softflowd -d -r /usr/local/etc/softflowd/capture+crypto+type2+8+vlan.pcap -v 9 -t maxlife=30s -T ether -n goflow2:9995" &

sleep 1

echo 'Done!'