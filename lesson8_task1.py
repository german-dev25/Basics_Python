# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью спе циальных карточек, на которых отмечены числа, и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
#
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
#
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка. Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
#
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#     Если цифра есть на карточке - она зачеркивается и игра продолжается.
#     Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#     Если цифра есть на карточке - игрок проигрывает и игра завершается.
#     Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
#
# Пример одного хода:
#
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 87     - 14    11
#       16 49    55 88    77
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
#
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
#
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html

from random import randint


def make_numbers(max_len, max_num):
    list_el = []
    while len(list_el) < max_len:
        new = randint(1, max_num)
        if new not in list_el:
            list_el.append(new)
    return list_el


class Cards:
    def __init__(self, name):
        self._name = name
        self._max_num_of_nums = 15
        self._nums_of_card = make_numbers(self._max_num_of_nums, 90)
        self._card_field = []

        # make card - list of uniques numbers with zeros
        for i in range(0, 3):
            # working with slice 0-5, 5-10, 10-15. sort and insert Zero
            card_slice = sorted(self._nums_of_card[5 * i: 5 * (i + 1)])
            for j in range(0, 4):
                index = randint(0, len(card_slice))
                card_slice.insert(index, 0)
            self._card_field += card_slice

    def __str__(self):
        result_card = '{:-^27}\n'.format(self._name)
        temp_line = ''
        for index, number in enumerate(self._card_field):
            if number == 0:
                temp_line += '  '
            elif number == -1:
                temp_line += ' -'
            else:
                temp_line += '{:2}'.format(str(number))

            if (index + 1) % 9 == 0:
                result_card += '{: ^26}\n'.format(temp_line)
                temp_line = ''
            else:
                temp_line += ' '
        result_card += '{:-^27}\n'.format('')
        return str(result_card)

    def __contains__(self, item):
        return item in self._card_field

    def check_num(self, num):
        for index, item in enumerate(self._card_field):
            if item == num:
                self._card_field[index] = -1

    def empty_card(self):
        return set(self._card_field) == {0, -1}


class Game:
    def __init__(self):
        self._user_card = Cards(' Игрок ')
        self._comp_card = Cards(' Компьютер ')
        self._num_kegs = 90
        self._kegs = make_numbers(self._num_kegs, self._num_kegs)

    def game_round(self):
        keg = self._kegs.pop()
        print('Бочонок с номером: {}. Осталось еще: {} бочонков'.format(keg, len(self._kegs)))
        print(self._user_card)
        print(self._comp_card)

        user_answer = input('Зачеркнуть цифру? (y/n) ').lower().strip()
        if user_answer == 'y' and keg not in self._user_card or user_answer != 'y' and keg in self._user_card:
            return 1

        if keg in self._comp_card:
            self._comp_card.check_num(keg)
            if self._comp_card.empty_card():
                return 1

        if keg in self._user_card:
            self._user_card.check_num(keg)
            if self._user_card.empty_card():
                return 2
        return 0
        # if return: 0 - continue // 1 - computer win // 2 - user win


game = Game()
while True:
    switch = game.game_round()
    if switch == 1:
        print('Вы проиграли')
        break
    elif switch == 2:
        print('Вы выиграли')
        break
