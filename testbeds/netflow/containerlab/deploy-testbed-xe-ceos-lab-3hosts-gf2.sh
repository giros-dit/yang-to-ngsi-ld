#!/bin/bash

echo 'Deploying containerlab topology with Cisco IOS XE CSR1000v and Arista cEOS routers with 3 hosts and GoFlow2...'

sudo containerlab deploy --topo telemetry-testbed-xe-ceos-3hosts-gf2.yaml

echo 'Done!'

echo ''
echo ''

echo 'Configuring client "pc11" container...'

sudo docker exec -it clab-telemetry-testbed-xe-ceos-3hosts-gf2-pc11 ifconfig eth1 10.0.1.2 netmask 255.255.255.0
sudo docker exec -it clab-telemetry-testbed-xe-ceos-3hosts-gf2-pc11 ip route add 10.0.2.0/24 via 10.0.1.1 dev eth1

echo 'Done!'

echo ''
echo ''

echo 'Configuring client "goflow2" container...'

sudo docker exec -it clab-telemetry-testbed-xe-ceos-3hosts-gf2-goflow2 ifconfig eth1 10.0.1.3 netmask 255.255.255.0
sudo docker exec -it clab-telemetry-testbed-xe-ceos-3hosts-gf2-goflow2 ip route add 10.0.2.0/24 via 10.0.1.1 dev eth1

echo 'Done!'

echo ''
echo ''

echo 'Configuring client "pc21" container...'

sudo docker exec -it clab-telemetry-testbed-xe-ceos-3hosts-gf2-pc21 ifconfig eth1 10.0.2.2 netmask 255.255.255.0
sudo docker exec -it clab-telemetry-testbed-xe-ceos-3hosts-gf2-pc21 ip route add 10.0.1.0/24 via 10.0.2.1 dev eth1

echo 'Done!'

echo ''
echo ''

echo 'Configuring client "pc22" container...'

sudo docker exec -it clab-telemetry-testbed-xe-ceos-3hosts-gf2-pc22 ifconfig eth1 10.0.2.3 netmask 255.255.255.0
sudo docker exec -it clab-telemetry-testbed-xe-ceos-3hosts-gf2-pc22 ip route add 10.0.1.0/24 via 10.0.2.1 dev eth1

echo 'Done!'

echo ''
echo ''

echo 'All done!'
