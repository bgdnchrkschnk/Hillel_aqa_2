from typing import Optional

person_info_prepared = {"name": "donald",
               "surname": "trump",
               "age": 75
}

def print_person_bio() -> None:
    """
    The function prints the person's bio.'
    :return: None
    """
    text: str = f"The person is {person_info_prepared['name']}, {person_info_prepared['surname']}. His age is {person_info_prepared['age']}"
    print(text)


# print_person_bio()


# -------------------

def get_person_bio() -> str:
    """
    The function returns the person's bio.
    :return: a string bio value
    """
    text: str = f"The person is {person_info_prepared['name'].title()}, {person_info_prepared['surname'].title()}. His age is {person_info_prepared['age']}"
    return text

result = get_person_bio()
# print(result)

# -----------------------------------

def get_person_bio_with_param(person_info: dict) -> str:
    """
    The function returns the person's bio.
    :param person_info: a dict of person name, surname, age
    :return: a string bio value
    """
    text: str = f"The person is {person_info['name'].title()}, {person_info['surname'].title()}. His age is {person_info['age']}"
    return text

# result = get_person_bio_with_param(person_info_prepared)
# print(result)

def get_person_bio_with_param_default_none(person_info: dict = "No person data") -> str:
    """
    The function returns the person's bio.
    :param person_info: a dict of person name, surname, age
    :return: a string bio value
    """
    if type(person_info) == dict:
        text: str = f"The person is {person_info['name'].title()}, {person_info['surname'].title()}. His age is {person_info['age']}"
    elif type(person_info) == str:
        text = person_info
    return text

result = get_person_bio_with_param_default_none()
# print(result)


def make_payment(user_to_id: int, amount_uah: int = 1):
    print(f"Making a payment to user_id-{user_to_id} to {amount_uah} uah....")


# make_payment(user_to_id=50)

# ---------------------------------------
def print_args(*args):
    # print(args, type(args))
    for arg in args: # args - tuple
        print(arg)

# Приклад виклику функції
# print_args(1, "hello", 3.14, [1, 2, 3], None, {1, 2})


def calculate_sum_of_numbers(*args) -> None:
    sum_of_args = 0
    for arg in args:
        if type(arg) == int or type(arg) == float:
            sum_of_args += arg
    print(sum_of_args)

# calculate_sum_of_numbers(56, 3748, "njkfnse", 2398.47, -786)


def get_persion_bio_(person_info: dict, **kwargs) -> str:
    print(kwargs)
    text: str = f"The person is {person_info['name'].title()}, {person_info['surname'].title()}. His age is {person_info['age']}"
    for param_name in kwargs:
        if param_name == 'additional_info':
            text += '='.join({k:v for k, v in kwargs[param_name].items()})
    print(text)


# get_persion_bio_(person_info=person_info_prepared, additional_info={"is_married": True}, is_president=True)


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# print_kwargs(name='name', surname='surname', age=25)


def print_args_and_kwargs(*args, **kwargs):
    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Приклад виклику функції
# print_args_and_kwargs(1, "hello", 3.14, name="John", age=25)

# def print_info(name: str, age = None):
#     print(f"The person is {name}, {age}")


def sub_numbers(a, b, c=None):
    return a - b

result = sub_numbers(a=5,b=5,c=2)
# print(result)


def square_angles_classical(a, b, c) -> int | float:
    sum_of_args = a + b + c
    return sum_of_args


square_angles = lambda a, b, c: a + b + c

# print(
#     square_angles(b=1, a=3, c=4),
# )

# all() рахує до кожного bool(element) == True
# print(
#     all([10, -25, ""])
# )


# any() рахує до хочаб одного bool(element) == True
# print(
#     any([1, 0, ""])
# )


# ------------------
number = 0
is_callable = callable(square_angles_classical)
# print(is_callable)

# print(
#     dir(number)
# )

names = ["Bohdan", "Denys", "Andriy"]
names_ids = {}


for index, name in enumerate(names):
    names_ids[index] = name
else:
    print(names_ids)

# print(list(enumerate(names)))