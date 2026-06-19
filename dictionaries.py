#!/usr/bin/env python3

# This script will be a dictionary. Mapping key to value pairs.

devices = {
		"router" : "192.168.1.1",
		"switch" : "192.168.1.2",
		"HMI" : "192.168.1.3",
		"VFD" : "192.168.1.4"
	}
print(devices["router"])

devices["PLC"] = "192.168.1.5"

for device, ip in devices.items():
	print(f"{device} : {ip}")


