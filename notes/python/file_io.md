# File I/O

Opening files in Python uses the with statement.

with open("filename.txt", "a") as f:
    f.write("text to write\n")

Modes:
- "r" = read only
- "w" = write, overwrites existing content
- "a" = append, adds to bottom, never overwrites

with closes the file automatically even if script crashes.
\n = newline character, starts a new line in the file

Reading a file:
with open("filename.txt", "r") as f:
    lines = f.readlines()

readlines() returns a list where each line is one item.
len(lines) tells you how many lines are in the file.
