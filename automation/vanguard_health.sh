#!/bin/bash
echo "========================================================================"
echo "                VANGUARD SYSTEM HEALTH CHECK"
echo "========================================================================"
echo "Date: $(date)"
echo "Host: $(hostname)"
echo "User: $(whoami)"
echo ""
echo "==== SYSTEM UPTIME ===="
uptime

echo ""
echo "==== DISK USAGE ===="
df -h /
echo ""
echo "==== NETWORK STATUS ===="
ip addr show | grep "inet "

echo ""
echo "==== PING TEST ===="
ping -c 1 8.8.8.8

