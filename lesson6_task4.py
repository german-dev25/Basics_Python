# 4) Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).  А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police

    def go(self):
        print('{} едет'.format(self.name))

    def stop(self):
        print('{} стоит'.format(self.name))

    def turn_left(self):
        print('{} поворачивает влево'.format(self.name))

    def turn_right(self):
        print('{} поворачивает вправо'.format(self.name))

    def show_speed(self):
        print('Скорость {} - {} км/ч'.format(self.name, self.speed))

    def police(self):
        if self.is_police:
            print('{} - полицейская машина'.format(self.name))
        else:
            print('{} - не полицейская машина'.format(self.name))


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.max_speed = 60

    def show_speed(self):
        print('Скорость {} - {} км/ч'.format(self.name, self.speed))
        if self.speed > self.max_speed:
            excess = self.speed - self.max_speed
            print('\tСкорость {} превышает допустимую {} на {} км/ч'.format(self.name, self.max_speed, excess))


class SportCar(Car):
    # def __init__(self, speed, color, name, is_police):
    #     super().__init__(speed, color, name, is_police)
    pass


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.max_speed = 40

    def show_speed(self):
        print('Скорость {} - {} км/ч'.format(self.name, self.speed))
        if self.speed > self.max_speed:
            excess = self.speed - self.max_speed
            print('\tСкорость {} превышает допустимую {} на {} км/ч'.format(self.name, self.max_speed, excess))


class PoliceCar(Car):
    # def __init__(self, speed, color, name, is_police):
    #     super().__init__(speed, color, name, is_police)
    pass


mercedes = TownCar(90, 'Черный', 'Mercedes', False)
ferrari = SportCar(120, 'Красный', 'Ferrari', False)
belaz = WorkCar(45, 'Желтый', 'Белаз', False)
bobik = PoliceCar(50, 'Серый', 'Бобик', True)

print(mercedes.max_speed)
print(ferrari.name)
print(belaz.color)
print(bobik.is_police)

# .go()
mercedes.go()
bobik.go()

# .stop()
ferrari.stop()
belaz.stop()

# .turn_left()
mercedes.turn_left()
ferrari.turn_left()

# .turn_right()
belaz.turn_right()
bobik.turn_right()

# .show_speed()
mercedes.show_speed()
ferrari.show_speed()
belaz.show_speed()
bobik.show_speed()

# .police()
mercedes.police()
ferrari.police()
belaz.police()
bobik.police()
