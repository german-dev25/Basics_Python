# 1) Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open('text_task1.txt', 'w') as work_file:
    while True:
        user_input = input('Введите текст для записи в файл или пустую строку для остановки\n')
        if not user_input:
            break
        print(user_input, file=work_file)
        # work_file.writelines(user_input + '\n')


# заметки. создание нового файла с уник номером
# work_file = open('task1_{}.txt'.format(i), 'r')
# i = 0
# i += 1
