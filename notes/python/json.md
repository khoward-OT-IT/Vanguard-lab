# JSON

JSON = JavaScript Object Notation
Universal data exchange format.
Both humans and programs can read it.

Made of two Python structures:
- Dictionaries: {"key": "value"}
- Lists: ["item1", "item2"]

Rules:
- Double quotes only, never single
- Comma after every item except the last
- No trailing commas

Converting JSON in Python:
json.load(f)      = file to dictionary
json.loads(text)  = string to dictionary

Reading a JSON file:
import json
with open("file.json", "r") as f:
    data = json.load(f)

JSONDecodeError = syntax problem in your JSON
Usually a missing comma or wrong quote type

Real world use:
- API responses come back as JSON strings
- Config files stored as JSON
- Network device data returned as JSON
- device_list.json stores our device config
