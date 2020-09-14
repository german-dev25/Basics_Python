# 3) Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name, self.surname, self.position = name, surname, position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income.get('wage') + self._income.get('bonus'))


pupkov = Position('Vasya', 'Pupkov', 'General', 100000, 20000)
print(pupkov.position)
pupkov.get_full_name()
pupkov.get_total_income()

ivanov = Position('Andrey', 'Ivanov', 'Manager', 50000, 10000)
print(ivanov.position)
ivanov.get_full_name()
ivanov.get_total_income()
