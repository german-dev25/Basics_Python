# 4) Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.


def my_func(x, y):
    return 1 / x ** abs(y)


def my_func_cycle(x, y):
    result = 1 / x
    for i in range(abs(y) - 1):
        result /= x
    return result


def my_func_recursion(x, y):
    if y == 0:
        return 1  # exit from recursion
    return (1 / x) * my_func_recursion(x, y + 1)


user_x, user_y = float(input('Введите действительное положительное число x: ')), \
                 int(input('Введите целое отрицательное число y: '))
while user_y >= 0:
    user_y = int(input('Введите целое отрицательное число y: '))

print('{} в степени {} будет равно: '.format(user_x, user_y))

print('- c ** = {:.5f}'.format(my_func(user_x, user_y)))
print('- без ** = {:.5f}'.format(my_func_cycle(user_x, user_y)))
print('- рекурсия = {:.5f}'.format(my_func_recursion(user_x, user_y)))
