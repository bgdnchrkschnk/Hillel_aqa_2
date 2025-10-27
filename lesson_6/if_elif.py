from pprint import pprint

from mprof import print_usage

person = dict(name = "Oleksandr",
age = 8,
is_vip = False,
)

pprint(person)

# if True: # if condition (bool)
#     print("It works!")
#
# if False: # if condition (bool)
#     print("It doest not work!")


# is_adult: bool = age >= 18

# if 60 > age >= 18: # bool(age)
#     print("Person is is adult!")
# elif age >=60:
#     print("Person is mature!")
# elif 10 < age < 18:
#     print("Person is is younger!")
# elif is_vip is True or (name == "Oleksandr" and age == 8):
#     print("Person is is vipping!")
# else:
#     print("Person is TOO young for our club!")









# amount = float(input("Enter the transaction amount: "))
#
# if amount > 0:
#     print("This is an income.")
# elif amount < 0:
#     print("This is an expense.")
# else:
#     print("The amount is zero — no transaction occurred.")
#
# card_type = input("Enter card type (Visa / MasterCard / Other): ").lower()
# amount = float(input("Enter transaction amount: "))
#
# if amount <= 0:
#     print("Invalid transaction amount.")
# elif card_type == "visa":
#     print(f"Visa card used. Amount charged: ${amount}")
# elif card_type == "mastercard":
#     print(f"MasterCard used. Amount charged: ${amount}")
# else:
#     print(f"Other card type used. Amount charged: ${amount}")