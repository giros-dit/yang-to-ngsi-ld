#!/bin/bash

while true; do
    ping 10.0.1.1 -i 0.1 -c 5
    nmap -p 80 10.0.1.1
    nmap -p 443 10.0.1.1
    nmap -p 22 10.0.1.1
    ping 10.0.2.2 -i 0.1 -c 5
    nmap -p 80 10.0.2.2
    nmap -p 443 10.0.2.2
    nmap -p 22 10.0.2.2
    ping 10.0.1.3 -i 0.1 -c 5
    nmap -p 80 10.0.1.3
    nmap -p 443 10.0.1.3
    nmap -p 22 10.0.1.3
    sleep 1
done