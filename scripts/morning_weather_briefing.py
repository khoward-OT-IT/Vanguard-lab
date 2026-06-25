#!/usr/bin/env python3
# morning_weather_briefing.py
# Combines network scan + weather into one daily briefing
# Vanguard Command - Morning Briefing System

import subprocess
import datetime
import json
import urllib.request

LOG_FILE = "briefing_log.txt"

def get_timestamp():
	return datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")

def ping_device(ip):
	result = subprocess.run(
		["ping", "-c", "1", ip],
		stdout=subprocess.DEVNULL,
		stderr=subprocess.DEVNULL
	)
	return result.returncode == 0

def get_weather(city):
	url = (
		f"https://api.open-meteo.com/v1/forecast"
		f"?latitude={city['lat']}"
		f"&longitude={city['lon']}"
		f"&current_weather=true"
	)

	with urllib.request.urlopen(url) as response:
		data = json.loads(response.read())
	temp_c = data["current_weather"]["temperature"]
	temp_f = round((temp_c * 9/5) + 32)
	wind = data["current_weather"]["windspeed"]
	return temp_f, wind

devices = []
with open("device_list.json", "r") as f:
	data = json.load(f)
	devices = data["devices"]

cities = [
	{"name": "Indianapolis, Indiana", "lat": "39.7691", "lon": "-86.1580"},
	{"name": "Phoenix, Arizona", "lat": "33.4484", "lon": "-112.0740"},
	{"name": "Raleigh, NC", "lat": "35.7796", "lon": "-78.6382"},
	{"name": "Huntsville, Alabama", "lat": "34.7304", "lon": "-86.5861"}
]

print("=" *44)
print("VANGUARD COMMAND - MORNING BRIEFING")
print(f"{get_timestamp()}")
print("=" * 44)

print("\nNETWORK STATUS:")
for device in devices:
	status = "OK  " if ping_device(device["ip"]) else "FAULT"
	print(f"  {status} - {device['ip']} {device['name']}")

print("\nWEATHER - RELOCATION TARGETS:")
best_city = None
best_temp = 999

for city in cities:
	try:
		temp_f, wind = get_weather(city)
		alert = " HEAT" if temp_f > 95 else ""
		print(f"  {city['name']}: {temp_f}F | Wind: {wind} km/h{alert}")
		if temp_f < best_temp:
			best_temp = temp_f
			best_city = city["name"]
	except Exception as e:
		print(f"  {city['name']}: ERROR - {e}")

print(f"\nBest weather today: {best_city}")
print("=" * 44)

