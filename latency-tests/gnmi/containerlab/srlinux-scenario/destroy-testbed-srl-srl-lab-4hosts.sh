#!/bin/bash

echo 'Destroying containerlab topology with Nokia SR Linux routers with 4 hosts...'

sudo containerlab destroy --topo telemetry-testbed-srl-srl-4hosts.yaml

sudo rm .telemetry-testbed-srl-srl-4hosts.yaml.bak
sudo rm -Rf clab-telemetry-testbed-srl-srl-4hosts/

echo 'Done!'

echo ''
echo ''

echo 'All done!'
