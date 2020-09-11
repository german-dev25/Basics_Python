# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('text_task2.txt', 'r') as work_file:

    # for each line
    num_of_lines = 0
    for line in work_file:
        num_of_lines += 1
        print(str(line), end='')
        print('Строка {}, количество слов - {} \n'.format(num_of_lines, len(line.split())))

    # for all lines
    work_file.seek(0)
    print('Общее количество: \nстрок - {}'.format(len(list(work_file))))
    work_file.seek(0)
    all_lines = str(work_file.readlines()).split()
    print('слов - {}\n'.format(len(all_lines)))

# difficult to read
# print('слов - {}'.format(len(list(str(work_file.readlines()).split()))))

