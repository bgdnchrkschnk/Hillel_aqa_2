numbers = range(1, 11)

squares: dict = {number: number**2 for number in numbers if number % 2}

print(squares)