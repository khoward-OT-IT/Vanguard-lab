#!/usr/bin/env python3
# read_devices.py
# Reads device list from a JSON file instead of hardcoding it.

import json


with open("device_list.json", "r") as f:
	data = json.load(f)

devices = data["devices"]

for device in devices:
	print(f"Name: {device['name']}")
	print(f"IP:   {device['ip']}")
	print(f"Type: {device['type']}")
	print("---")

