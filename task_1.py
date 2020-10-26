"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""


# не смог придумать как ускорить функцию, поэтому наоборот - замедлил её рекурсией
# интересно что если закомментить таймер функция работает нормально, но если включить таймер, то она сильно глючит

import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums, i=0, new_arr=[]):
    if i == len(nums) - 1:
        if nums[i] % 2 == 0:
            new_arr.append(i)
            i += 1
            return new_arr
        return
    else:
        if nums[i] % 2 == 0:
            new_arr.append(i)
            i += 1
            return func_2(nums, i)
        i += 1
        return func_2(nums, i)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(timeit.timeit('func_1(nums)', setup='from __main__ import func_1, nums'))
print(timeit.timeit('func_2(nums)', setup='from __main__ import func_2, nums'))

print(func_1(nums))
print(func_2(nums))
