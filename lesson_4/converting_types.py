number_string: str = "50"
number_int: int = int(number_string)

number_float_string: str = "50.28"
number_float: float = float(number_float_string)


print(number_int + 50)
print(number_float_string, type(number_float_string))
print(number_float, type(number_float))


list_of_names = ["Bohdan", "Anton", "Denys"]
tuple_of_names: tuple = tuple(list_of_names)

converted_tuple_to_list: list = list(tuple_of_names)

print(list_of_names)
print(tuple_of_names)
print(converted_tuple_to_list)

my_string = ""

# list_of_letters: list = list(my_string)
# tuple_of_letters: tuple = tuple(list_of_letters)
#
# print(list_of_letters)
# print(tuple_of_letters)


is_my_string_not_empty: bool = bool(my_string)

print(is_my_string_not_empty)

if not my_string: # bool(my_string)
    print(f"my_string is empty: {my_string}")
else:
    print(f"my_string is not empty: {my_string}")