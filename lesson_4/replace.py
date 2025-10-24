# replace

# sent = 'My name is Bohdan. Really is Bohdan'
#
# new_sent = sent.replace('is', 'are')
# print(new_sent)
# print(sent)
#
# sent = sent.replace('Bohdan', 'Alex')
# print(sent)

string_one = "               Hillel school is   thye best        "
splited: list = string_one.split()

prepared_list_of_names: list[str] = ["Andrew", "Donald"]
result = ' '.join(prepared_list_of_names) # протилежно .split()
print(result)





# print(string_one.rstrip()) # справа
# print(string_one.lstrip()) # зліва
# print(string_one.strip()) # зліва і справа

set: set = {"Hello", "friend", "55", "44.5"}
int_var: str = "55f"

for value in set:
    if value.isalpha():
        print(value)
