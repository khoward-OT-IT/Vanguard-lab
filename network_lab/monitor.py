import os

print("--- Vanguard Network Monitor ---")
status = os.system("ping -c 1 8.8.8.8 > /dev/null")

if status == 0:
	print("Network Connection: ACTIVE")
else:
	print("Network Connection: DOWN")
