#!/bin/bash

echo 'Destroying containerlab topology with Cisco IOS XE CSR1000v and Arista cEOS routers with 3 hosts and GoFlow2...'

sudo containerlab destroy --topo telemetry-testbed-xe-ceos-3hosts-gf2.yaml

sudo rm .telemetry-testbed-xe-ceos-3hosts-gf2.yaml.bak
sudo rm -Rf clab-telemetry-testbed-xe-ceos-3hosts-gf2/

echo 'Done!'

echo ''
echo ''

echo 'All done!'
