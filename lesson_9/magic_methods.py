import requests


class User:
    def __init__(self, nickname, age, sex):
        self.nickname = nickname
        self.age = age
        self.sex = sex
        self.hobbies = []
        self.friends = []

    def say_hello(self):
        print(f"Hello, i am {self.nickname}, i am {self.age} years old")

    def add_hobby(self, hobby):
        self.hobbies.append(hobby)

    def __str__(self): # print for user side
        return f"User {self.nickname}, {self.age} years old"

    def __repr__(self): # for debugging (dev side)
        return f"User(nickname={self.nickname}, age={self.age}, sex={self.sex})"

    def __len__(self):
        return len(self.nickname)

    def __gt__(self, other):
        return self.age > other.age

    def __add__(self, other):
        return self.friends.append(other)

    def __eq__(self, other_object_of_user):
        return self.nickname == other_object_of_user.nickname and self.age == other_object_of_user.age

    def __getattribute__(self, attribute): # when reading existing instance attribute
        if attribute == "friends":
            raise PermissionError("You can't get friend friends")
        print(f"Getting attribute {attribute}")
        return object.__getattribute__(self, attribute)

    def __getattr__(self, item): # when reading not existing instance attribute
        print(f"___getattr__ {item}")
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value): # when setting or editing instance attribute
        print(f"___setattr__ {key} {value}")
        if key == "music_genre" and value == "shanson":
            raise ValueError("You can't set this music genre")
        return object.__setattr__(self, key, value)

    def __delattr__(self, item): # when deleting instance attribute
        print(f"___delattr__ {item}")
        requests.post(url="https://test-audit.com/audit-delete", json={"item": item, object: id(self)})
        if item == "music_genre":
            raise ValueError("You can't delete music genre")
        return object.__delattr__(self, item)



bohdan = User("bohdan", 29, "male")
# bohdan_2 = User("bohdan", 29, "male")
# ella = User("ella", 21, "female")
# nikita = User("nikita", 21, "male")
#
# len_bohdan = len(bohdan)
# len_ella = len(ella)
#
# bohdan + ella
# bohdan + nikita
# print(bohdan.friends)
#
#
#
# print(bohdan == ella)
# print(bohdan == nikita)
# print(bohdan == bohdan_2)




