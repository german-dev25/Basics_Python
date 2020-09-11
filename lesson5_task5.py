# 5) Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('text_task5.txt', 'w+') as work_file:
    work_file.write(input('Введите числа, разделенные пробелами: '))
    work_file.seek(0)
    line = work_file.readline().split()
    print('Сумма чисел:', sum(list(map(int, line))))
