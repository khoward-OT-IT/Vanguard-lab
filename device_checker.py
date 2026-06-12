#!/usr/bin/env python3

# This program asks a user to input a device name , checks to see if that device is in the listed devices.
# If it is, it stays online.If not says not found, until the user types quit.

devices = ["switch", "router", "server", "HMI", "VFD", "PLC"]



while True:
	user_input = input("Please enter a network device: ") 
	if user_input == "quit":
		break
	elif user_input in devices:
		print(f"{user_input} - ONLINE")
	else:
		print(f"{user_input} - NOT FOUND")


