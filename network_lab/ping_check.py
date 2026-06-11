#!/usr/bin/env python3
# Simulated network device scanner
# Demonstrates break and continue in a real OT/IT context

devices = [
    "192.168.1.1",
    "192.168.1.2",
    "192.168.1.3",
    "192.168.1.4",
    "192.168.1.5"
]

maintenance = "192.168.1.3"
critical = "192.168.1.4"

for device in devices:
    if device == maintenance:
        print(f"{device} - SKIPPING, device in maintenance mode")
        continue
    if device == critical:
        print(f"{device} - CRITICAL DEVICE DOWN, stopping scan")
        break
    print(f"{device} - Scanning...")

print("Scan complete.")
