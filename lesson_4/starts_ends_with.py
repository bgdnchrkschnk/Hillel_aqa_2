

my_str: str = 'Would yyou tell me, please, which way t much care where ——" said Alice. ASD. Alice.'

is_startswith_would: bool = my_str.startswith("Would")

print(bool(-5))
print(bool(1))
print(bool(0))

is_endwith_alice: bool = my_str.endswith("Alice.")
# print(is_startswith_would)
# print(is_endwith_alice)

list_of_words: list[str] = my_str.split()
print(list_of_words)
for word in list_of_words:
    if word.endswith("e"):
        print(word)



# is_start_with_alice: bool = sent.endswith('Alice.')
# print(sent.startswith('Would'))  # True
# print(sent.startswith('Could'))  # False
# print(sent.endswith('Alice'))  # False
# print(sent.endswith('Alice.'))  # True
# print(sent.endswith('Shmalice'))  # False
# print(is_start_with_alice)
# print(sent.split())
# for word in sent.split(): # list
#     print(f'is {word} starts with s: {word.endswith("l")}')

returns_urls = ['www.simple.com/asd?a=b', 'www.simple.com/asd?', 'www.simple.com/xxxxxxx?a=b', 'www.s1imple.com/asd?a=b']
expected_start = 'www.simple.com'

index = 0
for url in returns_urls:
    if url.startswith(expected_start) is True:
        print(f'BAD CASE in position {index}: {url}')

    index += 1  # index = index + 1




