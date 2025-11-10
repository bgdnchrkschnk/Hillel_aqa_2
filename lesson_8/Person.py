class Person:
    head = 1 # attribute of class
    def __init__(self, first_name, last_name, age, is_married: bool):
        self.first_name = first_name # attribute of instance of class
        self.last_name = last_name
        self.age = age
        self.is_married = is_married
        self.friends = []



volodymyr_zelensky = Person("Volodymyr", "Zelensky", 43, True)
friends_to_add = ["Donald Trump", "Oleksandr Usyk", "Volodymyr Klitchko"]

for friend_name in friends_to_add:
    volodymyr_zelensky.friends.append(friend_name)


print(volodymyr_zelensky.friends)