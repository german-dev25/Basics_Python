# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input('Введите целое число n: ')

if int(n) < 10:
    result = int(n) * 123  # для случая n < 10 годится такой вариант, т.к. меньше вычислений
else:
    n = str(n)  # для счучая n > 10
    nn = n + n
    nnn = nn + n
    result = int(n) + int(nn) + int(nnn)

print('Сумма n + nn + nnn будет равна: ', result)
