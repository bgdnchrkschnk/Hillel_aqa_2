my_name = 'BoHDan CheRKaScHENkO Is Hillel LectoR'


print(my_name.isupper()) # all letters upper -> bool
print(my_name.islower()) # all letters lower -> bool
print(my_name.istitle()) # each first letter of word is Upper and other letters are lower -> bool


my_name_lower = my_name.lower() # make all letters lower -> new str
my_name_upper = my_name.upper() # make all letters upper -> new str
my_name_title = my_name.title() # make each first letter of word is Upper and other letters are lower  -> new str
my_name_capital = my_name.capitalize()  # make first letter of first word is Upper and other letters are lower  -> new str
my_name_swapped = my_name.swapcase() # invert letters registry -> new str

print(my_name_lower)
print(my_name_upper)
print(my_name_title)
print(my_name_capital)
print(my_name_swapped)
