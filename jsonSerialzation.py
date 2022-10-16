import json

from yaml import serialize;

people = [
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  },
  {
    "name": "Eli Jones",
    "username": "ejones",
    "phone": {
      "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
  }
]

# SERIALIZING 
# dump() used to serialize and convert it into a json file 
with open('dir/peopleWithIndent.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)

# dumps() converts the object into a string but do not creates a json file 
people_json = json.dumps(people)
print(people_json)

# DESERIALIZING 
with open('dir/peopleWithIndent.json', 'r') as people_json:
    people = json.load(people_json)
  
print("Converted Successfully")