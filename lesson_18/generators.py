# generator function, generator comprehension
import csv


# # скінчений
# def get_names():
#     yield "Bohdan" # point
#     yield "Bob"
#

# generator = get_names() # generator object
#
# first_name = next(generator)
# second_name = next(generator)

# Кожен генератор є ітератором


# нескінчений
def get_free_user_id():
    id = 1
    while True:
        yield id
        id += 1


generator_user_ids = get_free_user_id()

# print(next(generator_user_ids))
# print(next(generator_user_ids))
# print(next(generator_user_ids))
# print(next(generator_user_ids))
# print(next(generator_user_ids))
# print(next(generator_user_ids))
# print(next(generator_user_ids))
# print(next(generator_user_ids))
# print(next(generator_user_ids))



def get_names():
    for name in ("Alex", "Bob", "Michael", "Chris"):
        yield name


gen_names = get_names()

print(next(gen_names))
print(next(gen_names))
print(next(gen_names))
# -------------------------- generator comprehension

# big_list_range: list[int] = [n for n in range(10000000000000)] - надто великий обсяг

big_generator_range = (n for n in range(10000000000000)) # generator comprehension

# print(next(big_generator_range))
# print(next(big_generator_range))
# print(next(big_generator_range))


# classic standart way
with open(...) as f:
    data = f.read()


# generator read
def read_line_by_line(path):
    with open(path) as f:
        for line in f.read():
            yield line

