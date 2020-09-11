# 3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('text_task3.txt', 'r') as work_file:
    min_pay = float(input('Введите оклад, по которому определить у кого из сотрудников меньше введенного значения: '))
    min_pay_worker = ''
    average_pay = 0
    workers = 0

    for line in work_file:
        workers += 1
        worker = line.split()
        if float(worker[1]) < min_pay:
            min_pay_worker += worker[0] + ' '
        average_pay += float(worker[1])

    print('Оклад меньше {:.02f} руб. у сотрудников: {}'.format(min_pay, ', '.join(min_pay_worker.split())))
    print('Средний оклад всех сотрудников {:.02f}'.format(average_pay/workers))