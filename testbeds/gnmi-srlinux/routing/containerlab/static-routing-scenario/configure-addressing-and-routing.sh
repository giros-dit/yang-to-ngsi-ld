#!/bin/bash
echo 'Configuring IP addressing and static routing on Nokia SR Linux routers...'

#Configuring interface IP address on R1
echo '{"IF_NAME": "ethernet-1/2", "IF_IP_PREFIX": "10.10.10.1/30"}' | \
  gnmic -a clab-routing-testbed-r1:57400 -u admin -p NokiaSrl1! \
  --skip-verify set --request-file configure_ip_address.yaml --request-vars -
echo '{"IF_NAME": "ethernet-1/3", "IF_IP_PREFIX": "10.10.11.1/30"}' | \
  gnmic -a clab-routing-testbed-r1:57400 -u admin -p NokiaSrl1! \
  --skip-verify set --request-file configure_ip_address.yaml --request-vars -

#Configuring interface IP routing on R1
echo '{"Name_NextHop": "r1-to-r2", "IP_NextHop": "10.10.10.2", "Target_IP_Prefix": "192.168.2.0/24"}' | \
  gnmic -a clab-routing-testbed-r1:57400 -u admin -p NokiaSrl1! \
  --skip-verify set --request-file configure_ip_routing.yaml --request-vars -
echo '{"Name_NextHop": "r1-to-r3", "IP_NextHop": "10.10.11.2", "Target_IP_Prefix": "192.168.3.0/24"}' | \
  gnmic -a clab-routing-testbed-r1:57400 -u admin -p NokiaSrl1! \
  --skip-verify set --request-file configure_ip_routing.yaml --request-vars -

#Configuring interface IP address on R2
echo '{"IF_NAME": "ethernet-1/2", "IF_IP_PREFIX": "10.10.10.2/30"}' | \
  gnmic -a clab-routing-testbed-r2:57400 -u admin -p NokiaSrl1! \
  --skip-verify set --request-file configure_ip_address.yaml --request-vars -
echo '{"IF_NAME": "ethernet-1/3", "IF_IP_PREFIX": "10.10.12.1/30"}' | \
  gnmic -a clab-routing-testbed-r2:57400 -u admin -p NokiaSrl1! \
  --skip-verify set --request-file configure_ip_address.yaml --request-vars -

#Configuring interface IP routing on R2
echo '{"Name_NextHop": "r2-to-r1", "IP_NextHop": "10.10.10.1", "Target_IP_Prefix": "192.168.1.0/24"}' | \
  gnmic -a clab-routing-testbed-r2:57400 -u admin -p NokiaSrl1! \
  --skip-verify set --request-file configure_ip_routing.yaml --request-vars -
echo '{"Name_NextHop": "r2-to-r3", "IP_NextHop": "10.10.12.2", "Target_IP_Prefix": "192.168.3.0/24"}' | \
  gnmic -a clab-routing-testbed-r2:57400 -u admin -p NokiaSrl1! \
  --skip-verify set --request-file configure_ip_routing.yaml --request-vars -

#Configuring interface IP address on R3
echo '{"IF_NAME": "ethernet-1/2", "IF_IP_PREFIX": "10.10.11.2/30"}' | \
  gnmic -a clab-routing-testbed-r3:57400 -u admin -p NokiaSrl1! \
  --skip-verify set --request-file configure_ip_address.yaml --request-vars -
echo '{"IF_NAME": "ethernet-1/3", "IF_IP_PREFIX": "10.10.12.2/30"}' | \
  gnmic -a clab-routing-testbed-r3:57400 -u admin -p NokiaSrl1! \
  --skip-verify set --request-file configure_ip_address.yaml --request-vars -

#Configuring interface IP routing on R3
echo '{"Name_NextHop": "r3-to-r1", "IP_NextHop": "10.10.11.1", "Target_IP_Prefix": "192.168.1.0/24"}' | \
  gnmic -a clab-routing-testbed-r3:57400 -u admin -p NokiaSrl1! \
  --skip-verify set --request-file configure_ip_routing.yaml --request-vars -
echo '{"Name_NextHop": "r3-to-r2", "IP_NextHop": "10.10.12.1", "Target_IP_Prefix": "192.168.2.0/24"}' | \
  gnmic -a clab-routing-testbed-r3:57400 -u admin -p NokiaSrl1! \
  --skip-verify set --request-file configure_ip_routing.yaml --request-vars -