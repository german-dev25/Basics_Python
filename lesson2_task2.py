# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = [1, 'abc', 2, True, 3, '456', 0, False, 7, ' ', 'нечетное']

i = 0
new_list = []

for el in my_list:
    new_list.insert(i + 1, el) if i % 2 == 0 else new_list.insert(i - 1, el)
    i = i + 1

print(my_list)
print(new_list)

# if i % 2 == 0:
#     new_list.insert(i + 1, el)
# else:
#     new_list.insert(i - 1, el)