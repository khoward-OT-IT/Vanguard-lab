#!usr/bin/env python3
# auto_ping_logger.py
# Automatically pings devices on my network and logs results.
# No manual input required, this runs itself!


import subprocess
import datetime
import os

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

def rotate_log():
	if os.path.exists(LOG_FILE):
		with open(LOG_FILE, "r") as f:
			lines = f.readlines()
		if len(lines) > 50:
			timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
			archive_name = f"ping_log_{timestamp}.txt"
			os.rename(LOG_FILE, archive_name)
			print(f"log rotated: {archive_name}")

rotate_log()


log_entry("--- Scan started ---")


reachable = 0
unreachable = 0

for device in devices:
	if ping_device(device):
		log_entry(f"OK - {device} is reachable")
		reachable += 1
	else:
		log_entry(f"FAULT - {device} is unreachable")
		unreachable += 1

log_entry(f"--- Scan Complete: {reachable} reachable, {unreachable} unreachable ---")


size = os.path.getsize(LOG_FILE)
print(f"Log file size: {size} bytes")

