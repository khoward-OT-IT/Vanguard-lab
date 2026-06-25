# os Module

import os

Gives Python access to operating system functions.
Lets your script interact with files and directories.

## File operations used so far:

os.path.exists("file.txt")
= checks if a file exists, returns True or False

os.path.getsize("file.txt")
= returns file size in bytes

os.rename("old_name.txt", "new_name.txt")
= renames a file, used for log rotation

## Common os operations:

os.getcwd()
= returns current working directory

os.listdir("path")
= lists files in a directory

os.makedirs("path", exist_ok=True)
= creates a directory, won't error if exists

## Real world use in our scripts:
- auto_ping_logger uses os.path.exists to check
  if log file exists before rotating
- os.path.getsize reports log file size in bytes
- os.rename archives old log with timestamp

## Key insight:
os module = Python talking to Linux directly
Same things you do in terminal, now in a script
