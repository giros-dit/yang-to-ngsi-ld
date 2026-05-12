#!/bin/bash

echo 'Destroying containerlab topology with Nokia SR Linux routers...'

sudo containerlab destroy --topo routing-testbed.yaml
sudo rm -Rf clab-routing-testbed/
sudo ovs-vsctl del-br s1
sudo ovs-vsctl del-br s2
sudo ovs-vsctl del-br s3

echo 'Done!'

echo ''
echo ''

echo 'All done!'
