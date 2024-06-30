#!/bin/bash

echo 'Destroying containerlab topology with Cisco IOS XE CSR1000v and Arista cEOS routers with 4 hosts...'

sudo containerlab destroy --topo telemetry-testbed-xe-ceos-4hosts.yaml

sudo rm .telemetry-testbed-xe-ceos-4hosts.yaml.bak
sudo rm -Rf clab-telemetry-testbed-xe-ceos-4hosts/

echo 'Done!'

echo ''
echo ''

echo 'All done!'
