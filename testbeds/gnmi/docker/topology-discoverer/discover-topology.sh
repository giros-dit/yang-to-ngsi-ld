#!/bin/bash

interval=$2

if [[ "$1" == "ceos-scenario" ]]; then
    while true; do
        java -jar topology-driver-1.0.jar /opt/topology-data/ceos-scenario/clab-telemetry-testbed-ceos-ceos-4hosts/topology-data.json topology-data-compliant-yang.json topology-data-compliant-yang.xml
        sleep 0.5
        poetry run python -u candil_topology_discoverer_ngsi_ld_instantiator.py
        sleep $interval
    done
elif [[ "$1" == "srlinux-scenario" ]]; then
    while true; do
        java -jar topology-driver-1.0.jar /opt/topology-data/srlinux-scenario/clab-telemetry-testbed-srl-srl-4hosts/topology-data.json topology-data-compliant-yang.json topology-data-compliant-yang.xml
        sleep 0.5
        poetry run python -u candil_topology_discoverer_ngsi_ld_instantiator.py
        sleep $interval
    done
elif [[ "$1" == "xrv9k-scenario" ]]; then
    while true; do
        java -jar topology-driver-1.0.jar /opt/topology-data/xrv9k-scenario/clab-telemetry-testbed-xrv9k-ceos-4hosts/topology-data.json topology-data-compliant-yang.json topology-data-compliant-yang.xml
        sleep 0.5
        poetry run python -u candil_topology_discoverer_ngsi_ld_instantiator.py
        sleep $interval
    done
fi