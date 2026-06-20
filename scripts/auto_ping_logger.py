#!usr/bin/env python3
# auto_ping_logger.py
# Automatically pings devices on my network and logs results.
# No manual input required, this runs itself!


import subprocess
import datetime

LOG_FILE = "ping_log.txt"

devices = [
	"192.168.1.1",
	"192.168.1.10",
	"8.8.8.8",
	"192.168.1.99"
]

def log_entry(message):
	timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	entry = f"[{timestamp}] {message}\n"
	with open(LOG_FILE, "a") as log_file:
		log_file.write(entry)
	print(entry.strip())

def ping_device(ip):
	result = subprocess.run(
		["ping", "-c", "1", ip],
	stdout=subprocess.DEVNULL,
	stderr=subprocess.DEVNULL
	)
	return result.returncode == 0

log_entry("--- Scan started ---")

for device in devices:
	if ping_device(device):
		log_entry(f"OK - {device} is reachable")
	else:
		log_entry(f"FAULT - {device} is unreachable")

log_entry("--- Scan Complete ---")

