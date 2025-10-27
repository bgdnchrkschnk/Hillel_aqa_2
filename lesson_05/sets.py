import random

my_names: set[str] = {
    "Bohdan", "Kyrylo", "Diana"
}


# for name in my_names:
#     print(name)

# adding some value
my_names.add("Denys")
my_names.add("Denys")

# deleting random element
deleted_element =  my_names.pop() # randomly
# print(my_names)

# deleting a particular element - REMOVE
user_ids_failed: set = {124, 267, 3786, 3452}


user_ids_failed.remove(124)
print(user_ids_failed)

my_set = {1, 2, 3}
additional_elements = {3, 4, 5, 6}

# my_set.update(additional_elements)

# union
union_set = my_set.union(additional_elements)
union_set = my_set | additional_elements
# print(my_set, additional_elements)

# intersection
# intersected_elements = my_set.intersection(additional_elements)
intersected_elements = my_set & additional_elements
# print(intersected_elements)
# print(my_set, additional_elements)


#difference
difference_elements = my_set - additional_elements
difference_elements_2 = additional_elements - my_set
print(difference_elements)
print(difference_elements_2)
print(my_set, additional_elements)





my_names_list: list[str] = [
    "Bohdan", "Kyrylo", "Diana"
]

my_names_list.append("Denys")
my_names_list.append("Denys")
# print(my_names_list)

my_names_list = set(my_names_list)
# print(my_names_list)

#
# transactions: set = {("user_id", 285), ("user_id", 285)}


my_string: str = "Welcome home!"

my_string_set: set[str] = set(my_string)
print(my_string_set)


# set_comprehension
numbers = range(1, 11)
even_squared_numbers = {number**2 for number in numbers if number % 2 == 0}
print(even_squared_numbers)

# {4, 16}