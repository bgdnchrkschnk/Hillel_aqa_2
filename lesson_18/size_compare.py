import sys

# Список
my_list = [num for num in range(1, 1000000)]
print(sys.getsizeof(my_list))

# Генератор
my_generator = (num for num in range(1, 1000000))
print(sys.getsizeof(my_generator))