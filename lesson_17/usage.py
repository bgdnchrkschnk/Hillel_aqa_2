from my_package import *

print(add(2, 3))          # 5
print(subtract(5, 2))     # 3
print(normalize("  HI ")) # "hi"
print(capitalize_words("njkjenk"))

# capitalize_words не імпортується через *, бо його немає в __all__