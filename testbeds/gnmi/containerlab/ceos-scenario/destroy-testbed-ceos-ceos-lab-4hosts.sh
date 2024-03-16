#!/bin/bash

echo 'Destroying containerlab topology with two Arista cEOS routers with 4 hosts...'

sudo containerlab destroy --topo telemetry-testbed-ceos-ceos-4hosts.yaml

sudo rm .telemetry-testbed-ceos-ceos-4hosts.yaml.bak
sudo rm -Rf clab-telemetry-testbed-ceos-ceos-4hosts/

echo 'Done!'

echo ''
echo ''

echo 'All done!'
