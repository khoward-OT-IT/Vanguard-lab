#!/usr/bin/env python3
# weather_check.py
# Pulls currrent weather for multiple cities I'm considering relocating to, using Open-Meteo API
# No API key required

import urllib.request
import json

cities = [
	{"name": "Indianapolis, Indiana",	"lat": "39.7691", "lon": "-86.1580"},
	{"name": "Phoenix, Arizona",	"lat": "33.4484", "lon": "-112.0740"},
	{"name": "Raleigh, NC",	"lat": "35.7796", "lon": "-78.6382"},
	{"name": "Huntsville, Alabama",	"lat": "34.7304", "lon": "-86.5861"}
]

def get_weather(city):
	url = (
		f"https://api.open-meteo.com/v1/forecast"
		f"?latitude={city['lat']}"
		f"&longitude={city['lon']}"
		f"&current_weather=true"
	)
	with urllib.request.urlopen(url) as response:
		data = json.loads(response.read())
	return data ["current_weather"]

for city in cities:
	try:
		weather = get_weather(city)
		temp_f = round((weather["temperature"] * 9/5) + 32)
		wind = weather["windspeed"]
		print(f"{city['name']}: {temp_f}F | Wind: {wind} km/h")
	except Exception as e:
		print(f"{city['name']}: ERROR - {e}")
