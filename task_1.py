"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""

from collections import namedtuple

res = namedtuple('Resume', 'name one two three four')
company_num = int(input('Введите количество компаний: '))
company_list = []

for i in range(company_num):
    name = input(f'Введите имя компании номер {i+1}: ')
    money = input(f'Через пробел введите прибыль за кварталы компании номер {i+1}: ').split()
    company = res(name=name, one=money[0], two=money[1], three=money[2], four=money[3])
    company_list.append(company)

all_mid_money = 0
for i in company_list:
    mid_money = (int(i.one) + int(i.two) + int(i.three) + int(i.four))
    all_mid_money += mid_money

all_mid_money /= company_num
print(f'Средняя годовая прибыль всех предприятий: {all_mid_money}')
profit_list = []
loser_list = []

for i in company_list:
    mid_money = (int(i.one) + int(i.two) + int(i.three) + int(i.four))
    if mid_money >= all_mid_money:
        profit_list.append(i.name)
    elif mid_money < all_mid_money:
        loser_list.append(i.name)

print('Предприятия, с прибылью выше среднего значения:', end=' ')
for i in profit_list:
    print(i, end=' ')
print()
print('Предприятия, с прибылью ниже среднего значения:', end=' ')
for i in loser_list:
    print(i, end=' ')
