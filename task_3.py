"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""

from _collections import deque
import timeit


def append_check(example):
    for i in range(100):
        example.append(i)


def get_check(example):
    for i in range(100):
        a = example[i]


def pop_check(example):
    for i in range(100):
        example.pop()


my_list = []
my_deque = deque()

print(f"my_list app: {timeit.timeit('append_check(my_list)', setup='from __main__ import append_check, my_list')}")
print(f"my_deque app: {timeit.timeit('append_check(my_deque)', setup='from __main__ import append_check, my_deque')}")

print(f"my_list get: {timeit.timeit('get_check(my_list)', setup='from __main__ import get_check, my_list')}")
print(f"my_deque get: {timeit.timeit('get_check(my_deque)', setup='from __main__ import get_check, my_deque')}")

print(f"my_list pop: {timeit.timeit('pop_check(my_list)', setup='from __main__ import pop_check, my_list')}")
print(f"my_deque pop: {timeit.timeit('pop_check(my_deque)', setup='from __main__ import pop_check, my_deque')}")

"""
Похоже документация не врёт:
my_list app: 12.9952534
my_deque app: 9.5339218

my_list get: 5.527873400000001
my_deque get: 6.096322400000002

my_list pop: 8.212461300000001
my_deque pop: 7.191897200000007
"""