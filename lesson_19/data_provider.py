from faker import Faker
fake = Faker()
from random import choice


def get_create_user_request() -> dict:
    return {
        "name": fake.name(),
        "gender": choice(["male", "female"]),
        "email": fake.email(),
        "status": "active"
    }