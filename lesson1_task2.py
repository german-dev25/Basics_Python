# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_seconds = int(input('Введите время в секундах: '))

time_hours = time_seconds // 3600
time_seconds -= time_hours * 3600
time_minutes = time_seconds // 60
time_seconds -= time_minutes * 60

print('%02d:%02d:%d' % (time_hours, time_minutes, time_seconds))
