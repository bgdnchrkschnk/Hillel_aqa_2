from random import randint

from faker import Faker

from lesson_23.user import User

fake = Faker()


def get_new_user() -> User:
    # return User(**{"name": fake.name(), "age": randint(3, 99),})

    return User(name=fake.name(), age=randint(3, 99))



# -------------------------
# User(name="hjcd", age=256)
#
# user_dict = {"name": "ewhjf", "age": 356,}
# user_obj = User(**user_dict)