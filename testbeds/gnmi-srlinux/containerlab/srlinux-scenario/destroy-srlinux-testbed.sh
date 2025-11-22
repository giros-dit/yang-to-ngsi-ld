#!/bin/bash

echo 'Destroying containerlab topology with Nokia SR Linux routers...'

sudo containerlab destroy --topo srlinux-testbed.yaml
sudo rm -Rf clab-srlinux-testbed/

echo 'Done!'

echo ''
echo ''

echo 'All done!'
