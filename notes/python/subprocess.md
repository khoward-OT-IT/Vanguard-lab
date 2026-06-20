# subprocess

Allows Python to run terminal commands from inside a script.

import subprocess

result = subprocess.run(
    ["command", "flag", "argument"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

subprocess.run() executes the command and waits for it to finish.
The command is passed as a list - each word is a separate item.
DEVNULL throws away output so it doesn't print to screen.
result.returncode == 0 means success.
result.returncode == 1 means failure.

Example - ping one device:
result = subprocess.run(
    ["ping", "-c", "1", ip],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

"ip" in quotes = literal word ip (bug)
ip without quotes = variable holding the IP address (correct)
