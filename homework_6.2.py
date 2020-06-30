"""2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для
покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для
покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т"""


class Road:
    lenght = 0
    width = 0

    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def mass(self, MassForSM, high):
        return self.lenght * self.width * MassForSM * high


M1 = Road(20, 5000)
result = M1.mass(25, 5) / 1000
print(result, 'т"""')
