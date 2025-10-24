# split ТІЛЬКИ для строк

my_str = '"Would            yyou tell me, please, which way t much care where ——" said Alice'

list_of_split_string: list[str] = my_str.split(',')
# print(list_of_split_string)

# for item in list_of_split_string:
#     print(item)

# print(list_of_split_string[1])


# first_split: list[str] = my_str.split(' ') # - невалідний варіант
# print(first_split)
# second_case: list[str] = my_str.split()  #  ['"Would', 'yyou', 'tell', 'me,', 'please,', 'which', 'way', 't', 'much', 'care', 'where', '——"', 'said', 'Alice']
# print(second_case)
# # second_case = sent.split()  #  пробіл по замовчуванню
# print(second_case)


# index = 0
# for value in second_case:  # syntax: for ім'я_змінноЇ in список(або строка, або словник, або тапл, .. ітерабельний об'єкт)):
#     new_element = f'index is {index} is element: {value}'
#     print(new_element)
#     index += 1 # index = index +1


# my_str = '"Would you tell me, please, which way t much care where ——" said Alice'
# my_phrases: list = my_str.split(',')
# print(my_phrases)
# ['"Would you tell me', ' please', ' which way t much care where ——" said Alice']
  # ctrl + /
# print(f'first phrase = {my_phrases[0]}')
# print(f'second phrase = {my_phrases[1]}')
# print(f'third phrase = {my_phrases[2]}')
#
#
# res = [
#     '"Would you tell me',   # 0 index
#     ' please',   # 1 index
#     ' which way t much care where ——" said Alice'  # 2 index


# ctrl + /   закоментувати виділенне
# ctrl + d   продублюватит рядок
# ctrl + alt + l вирівняти код по PEP8 cmd + opt + l
# mac - command замість ctrl
#