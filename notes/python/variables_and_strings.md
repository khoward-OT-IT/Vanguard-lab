# Variables and Strings

## Variables
Containers that store values.
Created with the assignment operator =

name = "Kris"
age = 44
is_engineer = True

## Data types:
- str: text in quotes "hello"
- int: whole number 42
- float: decimal number 3.14
- bool: True or False

## Strings
Text wrapped in quotes.
Single or double quotes both work but be consistent.

name = "Vanguard"

## f-strings
Format strings that embed variables.
Prefix with f and use curly braces.

print(f"Hello {name}")
print(f"Temp is {temp_f}F")

## String conversion
int("42")    = converts string to integer
str(42)      = converts integer to string
float("3.14") = converts string to float

## Input
input() always returns a string.
Must convert if you need a number:
result = int(input("Enter a number: "))

## Key rule:
Read nested functions inside-out.
Innermost runs first.
int(input("Enter: ")) = input runs first, then int converts it.
