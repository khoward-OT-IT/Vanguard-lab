# APIs and urllib

API = Application Programming Interface
A way for your script to request data from an external
service over the internet. Response comes back as JSON.

import urllib.request
import json

def get_weather(city):
    url = f"https://api.example.com?param={city['lat']}"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
    return data["key"]

urllib.request.urlopen(url) = opens a URL like a file
json.loads() = converts JSON string to dictionary
json.load() = reads JSON from a file (different)

Tabs vs spaces:
Never mix them. Always use spaces in code.
Mixing causes invisible syntax errors.

Temperature conversion Celsius to Fahrenheit:
temp_f = round((celsius * 9/5) + 32)
