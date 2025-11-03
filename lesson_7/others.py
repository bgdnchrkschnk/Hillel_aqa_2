list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]


set_of_numbers = set(list_of_numbers)
frozenset_of_numbers = frozenset(list_of_numbers)


# print(set_of_numbers, type(set_of_numbers))
# print(frozenset_of_numbers, type(frozenset_of_numbers))


#-------------------
string_number: str = "10"
float_number: float = 10.9

# print(int(string_number), type(int(string_number)))
# print(int(float_number), type(int(float_number)))

class Animal:
    ...

class Dog(Animal):
    ...

dog: Dog = Dog()




# print(
#     isinstance(dog, Animal)
# )
#
# print(
#     type(dog) == Animal
# )

# print(
#     issubclass(str, object),
# )
# map(func, iterable)
new_list_of_numbers_square = list(map(lambda x: x ** 2, list_of_numbers))
# print(new_list_of_numbers_square)
#
#
# print(
#     max(new_list_of_numbers_square),
# )


list_to_100: list[int] = list(range(0, 101, 10))
print(list_to_100)


reverse_1 = list_to_100[::-1]
reverse_2 = list(reversed(list_to_100))
# print(reverse_2)
# print(reverse_1)

names = ["Bohdan", "Alex", "Diana", "Kyrylo"]
ages = [29, 35, 18]
professions = ["Python", "Java"]

print(list(zip(names, ages, professions)))


dict_of_person_ages = {name: age for name, age in zip(names, ages)}
print(dict_of_person_ages)



def build_sql_query(table, **kwargs):
    query = f"SELECT * FROM {table}"
    if kwargs:
        for k, v in kwargs.items():
            query += f" WHERE {k} = {v}"
    return query

print(
    build_sql_query(table="transactions", status='active')
)