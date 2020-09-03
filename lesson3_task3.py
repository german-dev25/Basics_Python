# 3) Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

# Ver.1
def my_func(a, b, c):
    """
    Search and remove min param. Then sum two params
    :param a, b, c: user's integers
    :return: sum of two biggest param
    """
    list_abc = [a, b, c]
    list_abc.remove(min(list_abc))
    return 'Сумма двух наибольших чисел: ', str(sum(list_abc))


a_user = int(input('Введите 1-е число: '))
b_user = int(input('Введите 2-е число: '))
c_user = int(input('Введите 3-е число: '))
print(''.join(my_func(a_user, b_user, c_user)))

# # Bad idea. Too many brackets....
# print(''.join(my_func((int(input('Введите 1-е число: '))),
#       (int(input('Введите 2-е число: '))),
#       (int(input('Введите 3-е число: '))))))


# # Ver.2 - with unpacking
# def my_func(a, b, c):
#     list_abc = [a, b, c]
#     list_abc.remove(min(list_abc))
#     return 'Сумма двух наибольших чисел: ', str(sum(list_abc))
#
#
# user_list = []
# for i in range(3):
#     user_list.insert(i, int(input('Введите {}-е число: '.format(i+1))))
#
# print(''.join(my_func(*user_list)))
