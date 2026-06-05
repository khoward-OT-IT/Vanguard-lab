import os

# Define our target zones 
zones = ["zone_A", "zone_B", "zone_C", "zone_D", "zone_E"]

# Define the base directory path 
base = "/home/kris/vanguard/network_lab/"

print("--- Vanguard Zone Audit Starting ---")

for z in zones:
    path = os.path.join(base, z)
    if os.path.exists(path):
        print(f"STATUS: {z} is ONLINE")
    else:
        print(f"Alert: {z} is MISSING!")
