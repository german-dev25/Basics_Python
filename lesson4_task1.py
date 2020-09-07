# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def full_pay(all_time, pay_hour, month_bonus):
    try:
        result = int(all_time) * int(pay_hour) + int(month_bonus)
        print('Заработная плата сотрудника: {}'.format(result))
    except ValueError:
        print('Нужно вводить числа')


name, work_hours, pay, bonus = argv
full_pay(work_hours, pay, bonus)

# argv.remove(name)
# full_pay(*argv)
