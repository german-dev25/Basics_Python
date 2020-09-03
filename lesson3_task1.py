# 1) Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division(var_1, var_2):
    """
    :)
    :param var_1: numerator
    :param var_2: denominator
    :return: result of division
    """
    try:
        return float(var_1) / float(var_2)
    except ZeroDivisionError:
        return 'Ошибка. Деление на 0 невозможно'
    except ValueError:
        return 'Операция возможна только с числами'


print(division(input('Введите 1-е число: '), input('Введите 2-е число: ')))

# user_var_1 = input('Введите 1-е число: ')
# user_var_2 = input('Введите 2-е число: ')
# print(division(user_var_1, user_var_2)
