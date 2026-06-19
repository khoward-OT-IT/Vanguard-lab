#!usr/bin/env python3
# file_basics.py
# Learning to write to a file before we build fault_logger.py


with open("test_log.txt", "a") as log_file:
	log_file.write("This is a test log entry.\n")

print("Entry written.")

