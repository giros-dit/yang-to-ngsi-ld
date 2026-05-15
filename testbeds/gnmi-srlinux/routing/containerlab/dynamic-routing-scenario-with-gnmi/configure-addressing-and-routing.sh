#!/bin/bash
echo 'Configuring IP addressing and static routing on Nokia SR Linux routers...'

#Configuring interface IP address on R1
echo '{"IF_NAME": "ethernet-1/2", "IF_IP_PREFIX": "10.10.10.1/30"}' | \
  gnmic -a clab-routing-testbed-r1:57400 -u admin -p NokiaSrl1! \
  --skip-verify set --request-file configure_ip_address.yaml --request-vars -
echo '{"IF_NAME": "ethernet-1/3", "IF_IP_PREFIX": "10.10.11.1/30"}' | \
  gnmic -a clab-routing-testbed-r1:57400 -u admin -p NokiaSrl1! \
  --skip-verify set --request-file configure_ip_address.yaml --request-vars -

#Configuring OSPF on R1
echo '{"Router_ID": "1.1.1.1", "Area_ID": "0.0.0.1", "IF_NAME": "ethernet-1/1"}' | \
gnmic -a clab-routing-testbed-r1:57400 \
-u admin -p NokiaSrl1! --skip-verify \
set --request-file configure_ip_routing.yaml --request-vars -

echo '{"Router_ID": "1.1.1.1", "Area_ID": "0.0.0.1", "IF_NAME": "ethernet-1/2"}' | \
gnmic -a clab-routing-testbed-r1:57400 \
-u admin -p NokiaSrl1! --skip-verify \
set --request-file configure_ip_routing.yaml --request-vars -

echo '{"Router_ID": "1.1.1.1", "Area_ID": "0.0.0.1", "IF_NAME": "ethernet-1/3"}' | \
gnmic -a clab-routing-testbed-r1:57400 \
-u admin -p NokiaSrl1! --skip-verify \
set --request-file configure_ip_routing.yaml --request-vars -

#Configuring interface IP address on R2
echo '{"IF_NAME": "ethernet-1/2", "IF_IP_PREFIX": "10.10.10.2/30"}' | \
  gnmic -a clab-routing-testbed-r2:57400 -u admin -p NokiaSrl1! \
  --skip-verify set --request-file configure_ip_address.yaml --request-vars -
echo '{"IF_NAME": "ethernet-1/3", "IF_IP_PREFIX": "10.10.12.1/30"}' | \
  gnmic -a clab-routing-testbed-r2:57400 -u admin -p NokiaSrl1! \
  --skip-verify set --request-file configure_ip_address.yaml --request-vars -

#Configuring OSPF on R2
echo '{"Router_ID": "2.2.2.2", "Area_ID": "0.0.0.1", "IF_NAME": "ethernet-1/1"}' | \
gnmic -a clab-routing-testbed-r2:57400 \
-u admin -p NokiaSrl1! --skip-verify \
set --request-file configure_ip_routing.yaml --request-vars -

echo '{"Router_ID": "2.2.2.2", "Area_ID": "0.0.0.1", "IF_NAME": "ethernet-1/2"}' | \
gnmic -a clab-routing-testbed-r2:57400 \
-u admin -p NokiaSrl1! --skip-verify \
set --request-file configure_ip_routing.yaml --request-vars -

echo '{"Router_ID": "2.2.2.2", "Area_ID": "0.0.0.1", "IF_NAME": "ethernet-1/3"}' | \
gnmic -a clab-routing-testbed-r2:57400 \
-u admin -p NokiaSrl1! --skip-verify \
set --request-file configure_ip_routing.yaml --request-vars -

#Configuring interface IP address on R3
echo '{"IF_NAME": "ethernet-1/2", "IF_IP_PREFIX": "10.10.11.2/30"}' | \
  gnmic -a clab-routing-testbed-r3:57400 -u admin -p NokiaSrl1! \
  --skip-verify set --request-file configure_ip_address.yaml --request-vars -
echo '{"IF_NAME": "ethernet-1/3", "IF_IP_PREFIX": "10.10.12.2/30"}' | \
  gnmic -a clab-routing-testbed-r3:57400 -u admin -p NokiaSrl1! \
  --skip-verify set --request-file configure_ip_address.yaml --request-vars -

#Configuring OSPF on R3
echo '{"Router_ID": "3.3.3.3", "Area_ID": "0.0.0.1", "IF_NAME": "ethernet-1/1"}' | \
gnmic -a clab-routing-testbed-r3:57400 \
-u admin -p NokiaSrl1! --skip-verify \
set --request-file configure_ip_routing.yaml --request-vars -

echo '{"Router_ID": "3.3.3.3", "Area_ID": "0.0.0.1", "IF_NAME": "ethernet-1/2"}' | \
gnmic -a clab-routing-testbed-r3:57400 \
-u admin -p NokiaSrl1! --skip-verify \
set --request-file configure_ip_routing.yaml --request-vars -

echo '{"Router_ID": "3.3.3.3", "Area_ID": "0.0.0.1", "IF_NAME": "ethernet-1/3"}' | \
gnmic -a clab-routing-testbed-r3:57400 \
-u admin -p NokiaSrl1! --skip-verify \
set --request-file configure_ip_routing.yaml --request-vars -