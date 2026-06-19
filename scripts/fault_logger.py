#!/usr/bin/env python3
# fault_logger.py
# Combines try/except + file writing + time stamp
# Logs device faults to a persistent log file.


import datetime


LOG_FILE = "fault_log.txt"

devices =["192.168.1.1", "192.168.1.10", "192.168.1.99"]

def log_entry(message):
	timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	entry = f"[{timestamp}] {message}\n"
	with open(LOG_FILE,"a") as log_file:
		log_file.write(entry)
	print(entry.strip())

for device in devices:
	try:
		result = int(input(f"Enter status code for {device} (number only): "))
		if result == 0:
			log_entry(f"OK - {device} responded normally")
		else:
			log_entry(f"FAULT - {device} returned code {result}")
	except ValueError:
		log_entry(f"ERROR - {device} received invalid input")

print(f"\nLog saved to {LOG_FILE}")
