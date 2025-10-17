some_text = "I am lecture of \nPython QA Automation" # some comment

# some_text_2 triple quotes
some_text_2 = """
I am lecture of
Python QA Automation"""


# print(some_text)
# print(some_text_2)


a = 5; b = 4; c = 20

# print(a == b) # equal
# print(a != b) # not equal

# // and /
# print(4 / 2) # float
# print(4 // 2) # int
# print(11 % 3) # залишок від ділення
# print(4 ** 4) # приведення до степеню

# #-cmd+slash(/) or win (control+slash(/))


is_married = True
is_employed = False

# print(is_married and is_employed)
# print(is_married & is_employed)
#
# print(is_married or is_employed)
# print(is_married | is_employed)
#
# print(not is_married)


# ()
print( (2 + 2) * 2)
print()
my_tuple: tuple = (1, 2, 3) # кортеж (незмінний)

# []
my_list: list = [1, 2, 3] # список (змінний)
print(my_list[2])
print(my_tuple[1])

# {}
my_dict: dict = {"name": "Bohdan",
                 "age": 29,
                 "is_married": False} # словник - (немає дублікатів в ключах)
my_set: set = {1, 2 ,3 ,4, "Elon Musk", True, False, 2.05} # множина (рандомний порядок, немає дублікатів)


print("My name is", my_dict["name"])

if is_married is False:
    print("married")

def greetings():
    print("Hello!")

greetings()


some_str = "Hello! \tMy name is Bohdan"
print(some_str)
