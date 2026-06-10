#! usr/bin/env python3

# This program counts from 1-5, then stops.

start = int(input("Enter a number starting number: "))
x = start
while x < 6:
	print(x)
	x = x + 1
if start >= 6:
	print("Please enter a number less than 6 next time.")

