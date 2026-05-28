#!/bin/bash
# Esempi strumenti IP
echo "CIDR to range: 192.168.1.0/24"
lumix en iptools cidr-to-range 192.168.1.0/24
echo "IP 192.168.1.1 in binario:"
lumix en iptools ip-to-bin 192.168.1.1
echo "Netmask per 10.0.0.0/8:"
lumix en iptools netmask 10.0.0.0/8

