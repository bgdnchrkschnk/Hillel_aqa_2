# <iterable>
# list, set, str, tuple


l = [1, 2, 3]

#
# for element in l:
#     print(element)


my_iterator = iter(l) # iterator


# print(
#     next(my_iterator)
# )
#
#
# print(next(my_iterator))
#
# print(next(my_iterator))


# Створення ітератора для списку
my_iterable = iter([1, 2, 3, 4, 5])

# # Прохід по ітератору вручну
# print(next(my_iterable))  # Виведе: 1
# print(next(my_iterable))  # Виведе: 2
# print(next(my_iterable))  # Виведе: 3
# print(next(my_iterable))  # Виведе: 4
# print(next(my_iterable))  # Виведе: 5
#
# # Помилка StopIteration при спробі отримати наступний елемент
# try:
#     print(next(my_iterable))
# except StopIteration:
#     print("StopIteration: Ітератор закінчився")


# class MyIterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.current = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current < self.limit:
#             self.current += 1
#             return self.current
#         else:
#             raise StopIteration
#
# # Використання власного ітератора
# my_iterator = MyIterator(limit=10)
# for num in my_iterator:
#     print(num)


my_list = [1, 2, 3, 4, 5]


# for item in my_list: # iter(my_list)
#     print(item)

my_iterator_one = iter(my_list)
my_iterator_two = iter(my_list)



# next - get next item
print(next(my_iterator_one))
print(next(my_iterator_one))

print(next(my_iterator_two))


print(my_iterator_one)



test_data = [
    [214, 251, 266], ["test_1", "test_2", "test_3"]
]





