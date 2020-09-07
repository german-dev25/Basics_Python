# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
# при котором повторение элементов списка будет прекращено.

from itertools import count, cycle


def try_count(start, stop):
    try:
        for el_count in count(int(start)):
            if el_count > int(stop):
                break
            else:
                print(el_count, end=' ')
    except ValueError:
        print('Необходимо ввести число')


def list_cycle(repeat, list_for_cycle):
    i = 1
    for el_cycle in cycle(list_for_cycle):
        if i > int(repeat):
            break
        print(el_cycle, end=' ')
        i += 1


try_count(input('Введите стартовое число: '),
          input('Введите, до какого числа сделать вывод: '))

list_cycle(input('\nВведите, сколько раз повторить элементы списка: '),
           [123, 'ABC', 2.0, True])
