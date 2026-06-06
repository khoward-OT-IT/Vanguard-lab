#!/usr/bin/env python3

device_status = "error"

if device_status == "online":
	print("Device is up - no action needed")
elif device_status == "degraded":
	print("Device is responding slowly - investigate")
else:
	print("Device is unreachable - trigger alert")


