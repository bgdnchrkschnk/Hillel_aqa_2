from pprint import pprint

person_info: dict = {
    "name": "Bohdan",
    "age": 29,
    "is_employed": True,
    "friends": [
        {
            "name": "Vladislav",
            "age": 28,
            "is_employed": False,
            "friends": []
        },
        {
            "name": "Mykyta",
            "age": 27,
            "is_employed": None,
            "friends": []
        }
    ]
}

persion_additional_info: dict = {"profession": "AQA", "exp": 5}

person_info.update(persion_additional_info)
print(person_info)
# try:
#     print(person_info["address"])
# except KeyError:
#     print("No such key")

address = person_info.get('address', "No such key")
# print(address)

person_info['age'] = 30
# pprint(person_info)


person_info_keys = person_info.keys()
person_info_values = person_info.values()

# print(person_info_keys, person_info_values)
#
# for key in person_info:
#     if len(str(person_info[key])) <= 10:
#         print(key, person_info[key])

poped_key = person_info.pop("age")
# print(poped_key)
# print(person_info)

# for value in person_info.values():
    # print(value)

# for key, value in person_info.items(): # [(key, value), (key, value)]
    # print(key, value)

# if found_name:='Bohdan' in person_info.values():
#     print(f"Bohdan is {found_name}")


# my_dict = dict(ключ1='значення1', ключ2='значення2')
# print(my_dict)
# print(person_info)
# pprint(person_info)
#
# name_of_person = person_info["name"]
# is_employed = person_info["is_employed"]
# friends = person_info["friends"]
# print(f"name_of_person: {name_of_person} and is_employed: {is_employed}. His friends: {friends}")
# name_of_first_friend = person_info["friends"][0]['name']
# print(f"name_of_first_friend: {name_of_first_friend}")
#
#
# for friend_dict in person_info["friends"]:
#     name = friend_dict["name"]
#     age = friend_dict["age"]
#     is_employed = friend_dict["is_employed"]
#     print("FRIENDS-"*80)
#     print(f"name: {name}, age: {age}, is_employed: {is_employed}")
#
#
# dict_example = {
#     # []: "list",
#     # {}: "dict",
#     # set(): "set"
# }
# print(dict_example)