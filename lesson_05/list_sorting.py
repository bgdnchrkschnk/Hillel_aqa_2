numbers = [5, 2, 8, 1, 3]
sorted_numbers = sorted(numbers, reverse=True)
print("Відсортований список:", sorted_numbers)

numbers.sort()
print("Відсортований список:", numbers)


words = ["яблуко", "апельсин", "банан", "груша", "слива"]

# Сортування за довжиною рядків
sorted_words = sorted(words, key=lambda x: len(x), reverse=True)

# Виведення результатів
print("Список, відсортований за довжиною рядків:", sorted_words)


my_range = range(0, 21, 2)
list_from_range = list(my_range)
print(list_from_range)



