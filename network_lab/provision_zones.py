import os

# The target folder we want to ensure exists
target = "/home/kris/vanguard/network_lab/zone_F"

print(f"Checking status: {target}")

if os.path.exists(target):
    print("Zone_F is already ONLINE.")
else:
    print("Zone_F NOT FOUND. Building now...")
    os.makedirs(target)
    print("SUCCESS: Zone_F is now integrated.")

