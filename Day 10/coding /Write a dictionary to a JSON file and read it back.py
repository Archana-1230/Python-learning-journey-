#Write a dictionary to a JSON file and read it back.
#Concepts: json.dump(), json.load().

import json

# Dictionary to write
data = {"name": "Archana", "age": 22, "city": "Chennai"}

# Write to JSON
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Read from JSON
with open("data.json", "r") as f:
    result = json.load(f)

print(result)
