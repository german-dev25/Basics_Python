# 2) Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# Ver.1


def print_user_data(name, second_name, birthday, city, mail, tel):
    """
    :param name: имя
    :param second_name: фамилия
    :param birthday: ДР
    :param city: город
    :param mail: эл почта
    :param tel: телефон
    :return: string with user's data
    """
    print(f'Фамилия Имя: {second_name}{name}. Город: {city}. День рождения {birthday}. Контакты: {tel}, {mail}')


print_user_data(
    second_name=input('Введите фамилию: '),
    name=input('Введите имя: '),
    mail=input('Введите почту: '),
    tel=input('Введите телефон: '),
    birthday=input('Введите день рождения: '),
    city=input('Введите город проживания: '))


# # Ver.2 - by kwargs
# def print_user_data(**kwargs):
#     return ' '.join(list(kwargs.values()))
#
#
# print(print_user_data(
#     name=input('Введите имя: '),
#     second_name=input('Введите фамилию: '),
#     birthday=input('Введите день рождения: '),
#     city=input('Введите город проживания: '),
#     mail=input('Введите почту: '),
#     tel=input('Введите телефон: ')))


# # Ver.3 - it's work :) (не совсем по заданию)
# # list unpack as arguments for function (find online)
#
#
# def print_user_data(*args):
#     return ' '.join(args)
#
#
# data_request = ('имя', 'фамилию', 'день рождения', 'город проживания', 'почту', 'телефон', )
# user_data_list = []
#
# for i, el in enumerate(data_request):
#     user_data_list.insert(i, input('Введите {}: '.format(el)))
#
# print(print_user_data(*user_data_list))  #  * - unpacking
