
my_str: str = 'Would     you tell me, please, which way t much care where ——" said Alice. ASD. Alice.'

words_my_str: list[str] = my_str.split()

print(words_my_str)

# for word in words_my_str:
#     print(word)

joined_my_str: str = ''.join(words_my_str)

print(joined_my_str)


tariffs = '1.2,1.5,1.5,1'

tariffs_list = tariffs.split(",")
print(tariffs_list)







#
# # join
#
# join_string = '|'.join(list_of_words)
# join_string = ' '.join(list_of_words)
#
# print(join_string)
#
# print('numbers', ', '.join(['1', '2', '3', '4']))
#
# print('numbers', ', '.join(['1']))


# string_int = "5.12f" # 5.12
# try:
#     result = float(string_int)
# except ValueError:
#     print("All good. Validation works")
#
#
# gotten_list = "11.2, 2.0,3.55,4,5"
# splitted: list = gotten_list.split(',')
# splitted.append('666')
# print(splitted)
# tuple_splitted: tuple = tuple(splitted)
# print(tuple_splitted)
#
#
#
#
# print(splitted)
#
# for item in tuple_splitted:
#     print(round(float(item)))


false_string: bool = False
#
#

if not false_string:
    print(bool(false_string))






# print(type(true_value), true_value)
# is_bool: bool = bool(true_value)
# print(type(is_bool), is_bool)

