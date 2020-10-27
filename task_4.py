"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
import timeit


def append_check(example):
    for i in range(10):
        example[str(i)] = i


def get_check(example):
    for i in example:
        example.get(i)


def get_items_check(example):
    example.items()


my_dict = {}
my_odict = OrderedDict()

print(f"my_dict app: {timeit.timeit('append_check(my_dict)', setup='from __main__ import append_check, my_dict')}")
print(f"my_odict app: {timeit.timeit('append_check(my_odict)', setup='from __main__ import append_check, my_odict')}")

print(f"my_dict get: {timeit.timeit('get_check(my_dict)', setup='from __main__ import get_check, my_dict')}")
print(f"my_odict get: {timeit.timeit('get_check(my_odict)', setup='from __main__ import get_check, my_odict')}")

print(f"my_dict get items: "
      f"{timeit.timeit('get_items_check(my_dict)',setup='from __main__ import get_items_check, my_dict')}")
print(f"my_odict get items: "
      f"{timeit.timeit('get_items_check(my_odict)', setup='from __main__ import get_items_check, my_odict')}")

"""
Выходит что словарь быстрее:
my_dict app: 2.821494
my_odict app: 3.5076622000000004

my_dict get: 0.9225721999999994
my_odict get: 1.1934708999999994

my_dict get items: 0.1748358999999997
my_odict get items: 0.17556120000000064
"""