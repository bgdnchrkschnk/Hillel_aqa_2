import json
import random

import requests
from faker import Faker

fake = Faker()

person: dict = {
    "name": fake.name(),
    "email": fake.email(),
    "phone": fake.phone_number(),
    "address": fake.address(),
    "is_married": random.choice([True, False]),
    "degree": None,
    "friends": ("Andriy", "Oleg"),
}




# --------------------- .dumps() - from python dict to json string

# def get_phone_ua_number():
#     result = f"+380{random.choice(["97, 98, 63, 50"])}" + "".join([])


person_json: str = json.dumps(person, indent=4)

# -------------------------- .dump() - convert python dict to json file

with open("person.json", "w") as json_file:
    json.dump(person, json_file, indent=4)
    print(f"JSON file written to person.json")


# ------------------------------ .load() read from json file and convert to python dict
with open("person.json", "r") as json_file:
    person = json.load(json_file)
    print(f"JSON file read from person.json")
    print(type(person), person)


# ------------------------------ .loads() convert json string to python dict
json_object: str = """{
    "name": "David Marshall",
    "email": "james55@example.com",
    "phone": "001-272-376-5266x181",
    "address": "91120 Davidson PineAmbermouth, KS 66000",
    "is_married": false,
    "degree": null,
    "friends": [
        "Andriy",
        "Oleg"
    ]
}"""

json_converted_to_dict: dict = json.loads(json_object)
json_converted_to_dict['name'] = "Sergiy"

print(type(json_converted_to_dict), json_converted_to_dict)

json_final_str = json.dumps(json_converted_to_dict, indent=4)
print(json_final_str)


