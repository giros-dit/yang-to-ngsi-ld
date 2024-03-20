#!/bin/bash

interval=30

if [[ "$1" == "ceos-scenario" ]]; then
    while true; do
        java -jar topology-driver-1.0.jar /opt/topology-data/ceos-scenario/clab-telemetry-testbed-ceos-ceos-4hosts/topology-data.json topology-data-compliant-yang.json topology-data-compliant-yang.xml
        sleep 1
        poetry run python -u candil_topology_discoverer_ngsi_ld_instantiator.py
        sleep $interval
    done
elif [[ "$1" == "srlinux-scenario" ]]; then
    while true; do
        java -jar topology-driver-1.0.jar /opt/topology-data/srlinux-scenario/clab-telemetry-testbed-srl-srl-4hosts/topology-data.json topology-data-compliant-yang.json topology-data-compliant-yang.xml
        sleep 1
        poetry run python -u candil_topology_discoverer_ngsi_ld_instantiator.py
        sleep $interval
    done
fi