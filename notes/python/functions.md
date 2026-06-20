# Functions

Functions are reusable blocks of code you call by name.

def function_name(parameter):
    code goes here
    return value

def = defines the function
parameter = input the function receives
return = sends a value back to the caller

Two types:
- Print-only: just prints output, returns nothing
- Return-value: sends data back for use elsewhere

Example:
def log_entry(message):
    # does work with message
    # writes to file, prints to screen

Calling a function:
log_entry("Device is reachable")
ping_device("192.168.1.1")

Functions keep code organized and prevent repetition.
One function, one job.
