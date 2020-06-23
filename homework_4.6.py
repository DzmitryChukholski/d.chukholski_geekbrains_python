"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено."""

from itertools import count
from itertools import cycle

# для прерывания итератора "а" скажем чтобы генерировались первые 15 чисел
start_el = int(input('Введите стартовое число: '))
for el in count(start_el):
    if el - start_el > 15:
        print()
        break
    else:
        print(el, end=' ')

# для прерывания итератора "б" пользователь вводит количество повторений, список определён заранее
robot_list = ['ABB', 'FANUC', 'KUKA', 'MOTOMAN', 'OMRON', 'Universal_Robots', 'Stäubli']
i = 0
j = int(input('Введите количество повторений элементов списка: '))
for el in cycle(robot_list):
    if i >= j:
        print()
        break
    print(el, end=' ')
    i += 1
