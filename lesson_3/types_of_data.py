# TYPES OF DATA

# immutable types
my_int: int = 100
my_float: float = 3.14
my_string: str = "Hello World!"
my_tuple: tuple = (None, my_string, my_int, False, {})
none_type: None = None
is_true: bool = True
is_false: bool = False
my_frozenset: frozenset = {1, 2, 3, 34}

# mutable types
my_list: list = [None, my_string, my_int, False, {}]
my_dict: dict = {"name": "John",
                 "age": 18}
my_set: set = {1,2,3,4,5,5}


# print(my_list[4])
# print(my_tuple[2:4])
# print(my_string[6:-1])
# print(my_dict["age"])


print(len(my_string))
print(len(my_list))
print(len(my_dict))
print(len(my_set))


for current_letter in my_string:
    print(current_letter)

for _ in my_list:
    print(_)


string = "HELLO"
print(id(string))
string = ("HELLO+")
print(id(string))


l_1 = [1, 5, 10]
print(id(l_1))
l_1.append(2)
print(id(l_1))


l_1[1] = 6
print(l_1)
my_dict["name"] = "Mykola"
print(my_dict)


# print(5 ** 3)
# print(pow(5, 3))

a = 50
b = 0
c = 50

print(a > b)
print(a < b)
print(a == c)
print(a != c)
print(a >= b)
print(c <= a)


print(min(0,12,15,-5,3))
print(max(0,12,15,-5,3))

my_list: list = [1, 2, 3, 4, 5]
print(min(my_list))

# format string
profession: str = "QA Automation"
greeting = f"Hello, my name is {my_dict['name']}. I am {my_dict['age']} years old. I am {profession}"
print(greeting)

# raw string
greeting_raw = r"Hello, my name is \n{my_dict['name']}. \nI am {my_dict['age']} years old. I am {profession}"
print(greeting_raw)


# age = int(input("What is your age?")) # input -> str "18"
# print(age >= 18)
# print(age, ", good!")


print(int(2.8))
print(float(5))
print(str(500.75))
print(float("70.5"))
