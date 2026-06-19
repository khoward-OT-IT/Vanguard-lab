#!/usr/bin/env python3
# try_basics.py
# Learning try/except before we build fault_logger.py

try:
	result = int(input("Enter a number : "))
	print(f"You entered: {result}")
except ValueError:
	print("That was not a number. Script handled it gracefully.")


