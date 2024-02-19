#!/bin/bash

echo 'Destroying containerlab topology with Cisco IOS XE CSR1000v routers and Keysight Ixia-C traffic generator...'

sudo containerlab destroy --topo ./topologies/telemetry-ixiac-lab.yaml

sudo rm .telemetry-ixiac-lab.yaml.bak
sudo rm -Rf clab-telemetry-ixiac-lab/

echo 'Done!'

echo ''
echo ''

echo 'All done!'
