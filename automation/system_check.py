#!/usr/bin/env python3
import os
from datetime import datetime
print("=== VANGUARD SYSTEM CHECK ===")
print("Report generated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

os.system("hostname")
os.system("whoami")
os.system("uptime")
os.system("df -h /")

print("=== NETWORK STATUS ===")
os.system("ip addr show | grep 'inet '")
os.system("ping -c 1 8.8.8.8")

