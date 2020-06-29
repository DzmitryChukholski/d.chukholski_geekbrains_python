"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""

import sys


def calculatesalary(hours, RatePerHour, bonus):
    return hours * RatePerHour + bonus


_, hours, RatePerHour, bonus, *_otherarg = sys.argv

try:
    hours, RatePerHour, bonus = int(hours), int(RatePerHour), int(bonus)
    print(f'Зарплата сотрудника составляет {calculatesalary(hours, RatePerHour, bonus)}$')
except ValueError:
    print('Неверные данные')
