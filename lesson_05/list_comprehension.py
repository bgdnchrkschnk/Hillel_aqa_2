numbers_from_0_to_100 = list(range(0, 101, 2))
print(numbers_from_0_to_100)

numbers_from_0_to_100 = []

for number in range(0, 101):
    if number % 2 == 0:
        numbers_from_0_to_100.append(number)
else:
    print(numbers_from_0_to_100)

# list comprehension
numbers_from_0_to_100_2 = [number for number in range(0, 101, 2) if number % 2 == 0]

print(numbers_from_0_to_100_2)

numbers_from_0_to_100_2_multiplied = [number*2 for number in range(0, 101, 2) if number % 2 == 0]

print(numbers_from_0_to_100_2_multiplied)


words = ["яблуко", "груша", "апельсин"]
word_lengths = [f"{word} - len is {len(word)}" for word in words]
print(word_lengths)


weekdays: list[str] = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

weekdays_filtered = [day for day in weekdays if not day in ['Sat', 'Sun']]
print(weekdays_filtered)