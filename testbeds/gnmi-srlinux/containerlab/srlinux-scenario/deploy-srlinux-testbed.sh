#!/bin/bash

echo 'Deploying containerlab topology with Nokia SR Linux routers...'

sudo containerlab deploy --topo srlinux-testbed.yaml

echo 'Done!'

echo ''
echo ''

echo 'Configuring client "pc1" container...'

sudo docker exec -it clab-srlinux-testbed-pc1 ifconfig eth1 10.0.1.2 netmask 255.255.255.0
sudo docker exec -it clab-srlinux-testbed-pc1 ip route add 10.0.2.0/24 via 10.0.1.1 dev eth1

echo 'Done!'

echo ''
echo ''

echo 'Configuring client "pc2" container...'

sudo docker exec -it clab-srlinux-testbed-pc2 ifconfig eth1 10.0.2.2 netmask 255.255.255.0
sudo docker exec -it clab-srlinux-testbed-pc2 ip route add 10.0.1.0/24 via 10.0.2.1 dev eth1

echo 'Done!'

echo ''
echo ''

echo 'All done!'
