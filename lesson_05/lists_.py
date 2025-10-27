#append - adding to last
weekdays: list[str] = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

...
# weekdays.append("Sat") # adding element in list on last position
# weekdays.append("Sat") # adding element in list on last position
# weekdays.append("Sat") # adding element in list on last position

# for i in range(3):
#     weekdays.append("Sat")
# print(weekdays)

# ----------------------------------------------

# insert - add to special index
# weekdays: list[str] = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
weekdays.insert(0, "Sunday")

# print(weekdays)

# -----------------------------------------------
# extend - extend one list with another
weekdays: list[str] = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
weekdays_copy = weekdays.copy()
weekends: list[str] = ['Sat', "Sun"]

weekdays_copy.extend(weekends)
# print(weekdays_copy)
# -----------------------------------------------
# remove - deleting some element

weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', "Tue"]
weekdays.append("Sat")
print(weekdays)
weekdays.remove("Tue")
print(weekdays)
print(weekdays[::-1].pop())
