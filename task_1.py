"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

# Кажется что-то пошло не по плану т.к. у меня список стабильно заполняется быстрее чем словарь

# Подсмотрел разбор дз и добавил поиск элемента


def give_me_time(func):
    import time
    start = time.time()
    func_res = func()
    end = time.time()
    #print(f'Результат выполнения функции: {func_res}')
    #print(f'Время выполнения функции: {end - start}')
    return end - start


@give_me_time
def make_list():
    my_list = []
    for i in range(10000):
        my_list.append(i)
        my_list.index(i)
    return my_list


@give_me_time
def make_dict():
    my_dict = {}
    for i in range(10000):
        my_dict[i] = i
        my_dict.get(i)
    return my_dict


a = 0
b = 0
for i in range(10000):
    a += make_list
    b += make_dict

print(f'Среднее время заполнения списка:  {a/10000}\nСреднее время заполнения словаря: {b/10000}')
