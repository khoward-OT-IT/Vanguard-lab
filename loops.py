#!/usr/bin/env python3
# This program demonstrates while loops, break, and continue

start = int(input("Enter a starting number: "))
x = start

while x < 6:
    if x == 3:
        print("Skipping 3 with continue")
        x = x + 1
        continue
    if x == 5:
        print("Hit 5, breaking loop")
        break
    print(x)
    x = x + 1

if start >= 6:
    print("Please enter a number less than 6 next time.")
