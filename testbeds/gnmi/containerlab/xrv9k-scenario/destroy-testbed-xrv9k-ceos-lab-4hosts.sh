#!/bin/bash

echo 'Destroying containerlab topology with Cisco XRv9K and Arista cEOS routers with 4 hosts...'

sudo containerlab destroy --topo telemetry-testbed-xrv9k-ceos-4hosts.yaml

sudo rm .telemetry-testbed-xrv9k-ceos-4hosts.yaml.bak
sudo rm -Rf clab-telemetry-testbed-xrv9k-ceos-4hosts/

echo 'Done!'

echo ''
echo ''

echo 'All done!'
