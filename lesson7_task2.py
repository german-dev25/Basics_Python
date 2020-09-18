# 2) Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calc_material(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def calc_material(self):
        return print(self.size / 6.5 + 0.5)


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def calc_material(self):
        return print(2 * self.height + 0.3)


coat = Coat(5)
suit = Suit(6)

suit.calc_material
coat.calc_material
