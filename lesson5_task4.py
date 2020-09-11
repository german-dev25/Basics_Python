# 4) Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open('text_task4.txt', 'r') as work_file:

    replacement_text = ['Один', 'Два', 'Три', 'Четыре']
    new_text = ''
    i = 0

    for line in work_file:
        text_line = line.split(' - ')
        text_line[0] = replacement_text[i]
        new_text += ' - '.join(text_line)
        i += 1

with open('new_text_task4.txt', 'w') as new_text_file:
    new_text_file.write(new_text)
