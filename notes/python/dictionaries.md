# Python Dictionaries - June 18 2026

## What a dictionary is
A dictionary stores key-value pairs. Like a phone book
where you look up a name to get a number. In Python,
curly braces hold the pairs: {"key": "value"}

## How to look up a value
Use the key in square brackets:
devices["router"]
This returns the value associated with that key.

## How to loop through all key-value pairs
Use .items() with a for loop:
for device, ip in devices.items():
    print(f"{device} : {ip}")
This gives you both the key and value each iteration.

## Real world use
Map device names to IP addresses
Map hostnames to status
Map ports to services
