#!/usr/bin/env python3

# This code will show me how to use functions that can be called later, and return values.

devices = ["switch", "router", "server", "HMI", "VFD"]

def  check_device(device):
	if device in devices:
		print(f"{device} - ONLINE")
	else:
		print(f"{device} - NOT FOUND")


check_device("router")
check_device("toaster")

def get_status(device):
	if device in devices:
		return "ONLINE"
	else:
		return "NOT FOUND"

result = get_status("router")
print(result)

