import json
import random

import requests
from faker import Faker

fake = Faker()


# --------------------- .dumps() - from python dict to json string

# def get_phone_ua_number():
#     result = f"+380{random.choice(["97, 98, 63, 50"])}" + "".join([])

person: dict = {
    "name": fake.name(),
    "email": fake.email(),
    "phone": fake.phone_number(),
    "address": fake.address(),
    "is_married": random.choice([True, False]),
    "degree": None,
    "friends": ("Andriy", "Oleg"),
}

person_json: str = json.dumps(person, indent=4)



# -------------------------- .dump() - convert python dict to json file
#
# with open()



