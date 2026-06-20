# try/except

Used to catch errors instead of crashing the script.

try:
    risky code here
except ErrorType:
    handle the error here

Common error types:
- ValueError: wrong data type (int("hello"))
- FileNotFoundError: file doesn't exist
- Exception: catches any error

The script continues running after the except block.
