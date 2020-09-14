# 5) Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки {} (родительский класс)'.format(self.title))


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки {} (1-й дочерний класс)'.format(self.title))


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки {} (2-й дочерний класс)'.format(self.title))


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки {} (3-й дочерний класс)'.format(self.title))


stationery = Stationery('Stationery')
pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()
