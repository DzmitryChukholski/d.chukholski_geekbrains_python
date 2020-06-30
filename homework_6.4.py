"""4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат."""


class Car:
    speed = 0
    color = 'white'
    name = 'unknown'
    is_police = False
    move = False  # определяет движется ли автомобиль

    def go(self):
        self.move = True
        self.speed = 5
        print(f'Автомобиль {self.name} цвета "{self.color}" начал движение')

    def stop(self):
        self.move = False
        self.speed = 0
        print(f'Автомобиль {self.name} цвета "{self.color}" завершил движение')

    def turn(self, direction):
        if self.move:
            print(f'Автомобиль {self.name} цвета "{self.color}" совершил поворот {direction}')
        else:
            print(f'Автомобиль {self.name} цвета "{self.color}" не движется')

    def show_speed(self):
        if not self.move:
            print(f'Автомобиль {self.name} цвета "{self.color}" не движется')
        elif self.speed > 0:
            print(f'Автомобиль {self.name} цвета "{self.color}" движется со скоростью {self.speed} км/ч')
        else:
            print(f'Автомобиль {self.name} цвета "{self.color}" движется задним ходом со скоростью {abs(self.speed)} км/ч')


class TownCar(Car):
    type = 'TownCar'

    def show_speed(self):
        if not self.move:
            print(f'Автомобиль {self.name} цвета "{self.color}" не движется')
        elif self.speed > 0:
            print(f'Автомобиль {self.name} цвета "{self.color}" движется со скоростью {self.speed} км/ч')
        else:
            print(f'Автомобиль {self.name} цвета "{self.color}" движется задним ходом со скоростью {abs(self.speed)} км/ч')
        if self.speed > 60 or self.speed < -60:
            print('ВНИМАНИЕ! Превышена максимально допустимая скорость движения')


class SportCar(Car):
    type = 'SportCar'


class WorkCar(Car):
    type = 'WorkCar'

    def show_speed(self):
        if not self.move:
            print(f'Автомобиль {self.name} цвета "{self.color}" не движется')
        elif self.speed > 0:
            print(f'Автомобиль {self.name} цвета "{self.color}" движется со скоростью {self.speed} км/ч')
        else:
            print(f'Автомобиль {self.name} цвета "{self.color}" движется задним ходом со скоростью {abs(self.speed)} км/ч')
        if self.speed > 40 or self.speed < -40:
            print('ВНИМАНИЕ! Превышена максимально допустимая скорость движения')


class PoliceCar(Car):
    type = 'PoliceCar'
    is_police = True


VW = TownCar()
VW.color = 'серый'
VW.name = 'VW Polo'

toyota = SportCar()
toyota.color = 'серебрянный'
toyota.name = 'Toyota Celica'

skoda = WorkCar()
skoda.color = 'белый'
skoda.name = 'Skoda Octavia'

bmw = PoliceCar()
bmw.color = 'Цветографическая схема согласно ГОСТ Р 50574-2002'
bmw.name = 'BMW 530d M Sport'

print('VW:')
VW.go()
VW.show_speed()
VW.turn('налево')
VW.speed = 25
VW.show_speed()
VW.speed = 65
VW.show_speed()
VW.stop()
VW.show_speed()
print()

print('Toyota:')
toyota.turn('налево')
toyota.go()
toyota.show_speed()
toyota.turn('направо')
toyota.speed = 180
toyota.show_speed()
toyota.stop()
toyota.speed = -15
toyota.go()
toyota.speed = -15
toyota.show_speed()
toyota.stop()
print()

print('Skoda:')
print(f'Это полицейский автомобиль? {skoda.is_police}')
skoda.go()
skoda.show_speed()
skoda.speed = 35
skoda.show_speed()
skoda.turn('направо')
skoda.speed = 45
skoda.show_speed()
skoda.stop()
print()

print('BMW:')
print(f'Это полицейский автомобиль? {bmw.is_police}')
bmw.show_speed()
bmw.go()
bmw.speed = 220
bmw.show_speed()
bmw.stop()
