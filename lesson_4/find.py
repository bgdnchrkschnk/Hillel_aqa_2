my_name = "My name is Bohdan and i am glad to be here"



name_start_index: int = my_name.find('^')
print(name_start_index)
# print(my_name[name_start_index:name_start_index + 6])
# print(sent.find('Boh'))
#
#
#
# погане рішення
# bool_is_bohdan_in = bool(my_name.find("Bof"))
# print(bool_is_bohdan_in)
# bool_is_My = bool(my_name.find('M'), 0, -1)
# print("M", my_name.find('M'))
#
is_bohdan_in_str: bool = False

my_name_lower: str = my_name.lower()
if my_name_lower.find('bohdan') >= 0:
    is_bohdan_in_str = True
    print(f'Bohdan in the sentence')
#
# # альтернативний варіант
#

# if 'Byg' in sent:
#     print('Bohdan in the sentence')

# example_str = "My name is Bohdan"
# is_index = example_str.find('is')
# len_word = len("is")
# #
# result_sent = example_str[:is_index]  # розділити до слова is
# print('Cut before is:   ', result_sent)
# #
# result_sent = example_str[is_index + len_word:]  # +2 бо is має довжину 2, поганий варіант
# print('Name:   ', result_sent)
#
#

# print(sent.find("is"))
# search_word = 'name'
# # print(sent.split("."))
#
# # надрукувати все після слова search_word
# search_word_index = sent.find(search_word)  # шукаю індекс початку цього слова(перша зустріч цього слова)
# len_of_search_word = len(search_word)  # довжина слова після якого треба друкувати
# final_index = search_word_index + len_of_search_word  # знаходжу індекс піля search_word
# result_sent = sent[final_index:] # роблю слайс[search_word_index + len(search_word):]
# print(result_sent)
