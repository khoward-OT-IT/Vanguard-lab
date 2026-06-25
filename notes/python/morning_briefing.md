# morning_weather_briefing.py

Combines network scanning and live weather API
into one unified daily briefing from the CLI.

## What it does:
1. Gets current timestamp
2. Pings all devices from device_list.json
3. Pulls live weather for 4 relocation cities
4. Finds the city with best temperature
5. Prints formatted briefing to screen

## New concepts used:
- return temp_f, wind = returning multiple values
  from one function
- best_temp = 999 = starting high so any real temp
  beats it on first comparison
- if temp_f < best_temp = comparison to find lowest
- "=" * 44 = prints 44 equal signs as a divider line
- % I in strftime = 12 hour clock format
- % p in strftime = AM or PM

## Builds on:
- subprocess ping from auto_ping_logger
- json.load() from device_list.json
- urllib and json.loads() from weather_check.py
- datetime timestamp from fault_logger
- try/except from try_basics.py

## Key insight:
Real automation engineering is combining
existing tools into unified systems.
Not always building from scratch.
