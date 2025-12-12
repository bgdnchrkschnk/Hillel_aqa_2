import csv


data = [
    ['Name', 'Age', 'City', "is_married"],
    ['John', 30, 'New York', False],
    ['Alice', 25, 'Los Angeles', None],
    ['Bob', 18, 'Chicago', True] # str(element)
]


# write csv file

with open("example.csv", "w") as csvfile:

    writer = csv.writer(csvfile)
    writer.writerows(data) # write rows iterable[iterable]

# read csv file

with open("example.csv", "r") as csvfile:

    reader = list(csv.reader(csvfile)) # generator object
    header = reader[0]
    data: list[list[str]] = reader[1:]


    for index, row in enumerate(data): print(index, row)