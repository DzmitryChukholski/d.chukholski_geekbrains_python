"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

# Ускорить получилось, особенно это заметно при увеличении количества повторений в массиве,
# потому что он не проверяет заново то, что уже проверил

import timeit
array = [1, 3, 1, 3, 4, 5, 1, 3, 1, 3, 4, 5, 1, 3, 1, 3, 4, 5, 1, 3, 1, 3, 4, 5, 1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    m = 0
    num = 0
    list_of_numbers = set(array)
    for i in list_of_numbers:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


print(f"func_1: {timeit.timeit('func_1()', setup='from __main__ import func_1, array')}")
print(f"func_2: {timeit.timeit('func_2()', setup='from __main__ import func_2, array')}")
print(f"func_3: {timeit.timeit('func_3()', setup='from __main__ import func_3, array')}")

print(func_1())
print(func_2())
print(func_3())
