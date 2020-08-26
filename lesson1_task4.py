# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_int = int(input('Введите целое положительное число: '))

max_int = user_int % 10
go_int = user_int // 10
while go_int > 0:
    if go_int % 10 > max_int:
        max_int = go_int % 10
    go_int = go_int // 10
print('Самое большая цифра в числе ', user_int, ' это - ', max_int)
