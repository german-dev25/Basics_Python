# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

# Ver. 1. method title + lambda

int_func = lambda word: word.title()
print(int_func('text'))

our_string = 'a string consisting of words and spaces'
map_from_string = map(int_func, our_string.split())
new_string = ' '.join(list(map_from_string))
print(new_string)

# # so much brackets... and look hard. but it's work. 1 string
# print(' '.join(list(map(lambda word: word.title(), 'a string consisting of words and spaces'.split()))))


# # Ver. 2. Not method title()
# def int_func_word(word):
#     list_word = list(word)
#     list_word[0] = list_word[0].upper()
#     return ''.join(list_word)
#
#
# def int_func_string(string):
#     list_words = list(string.split())
#     for i, word in enumerate(list_words):
#         list_words[i] = int_func_word(word)
#     return ' '.join(list_words)
#
#
# print(int_func_word('text'))
#
# our_string = 'a string consisting of words and spaces . interesting'
# print(int_func_string(our_string))


# # Ver. 3. Method "title()" and functions
# def int_func_word(word):
#     return word.title()
#
#
# def int_func_string(string):
#     return string.title()
#
#
# one_word = 'text'
# one_string = 'a string consisting of words and spaces'
#
# print(int_func_word(one_word))
# print('Легким движением руки строка "{}" с методом title() превращается в "{}"'
#       .format(one_string, int_func_string(one_string)))
#
