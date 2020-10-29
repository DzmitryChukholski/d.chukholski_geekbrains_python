"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

from random import randint
import timeit


def reverse_bubble(array):
    i = 1
    while i < len(array):
        for j in range(len(array)-i):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        i += 1
    return array


def reverse_bubble_2(array):
    for i in range(len(array)):
        change_nums = 0
        for j in range(len(array)-i-1):
            if array[j] < array[j+1]:
                change_nums += 1
                array[j], array[j+1] = array[j+1], array[j]
        if change_nums == 0:
            return array
    return array


unsorted_array = []
for i in range(10):
    unsorted_array.append(randint(-100, 100))

bubble_sorted = reverse_bubble(unsorted_array[:])
bubble_sorted_2 = reverse_bubble_2(unsorted_array[:])
print(f'Исходный массив:               {unsorted_array}\nСортированный первым способом: {bubble_sorted}\n'
      f'сортированный вторым способом: {bubble_sorted_2}')

time_1 = timeit.timeit('reverse_bubble(unsorted_array[:])', 'from __main__ import reverse_bubble, unsorted_array',
                       number=100000)
time_2 = timeit.timeit('reverse_bubble_2(unsorted_array[:])', 'from __main__ import reverse_bubble_2, unsorted_array',
                       number=100000)

print(f'Время выполнения сортировки первого типа: {time_1}\nВремя выполнения сортировки второго типа: {time_2}')

"""Предложенный вариант доработки эффективен лишь в том случае если правая часть массива отсортирована.
Если же в правой части массива оказывается элемент который должен после сортировки находиться слева эффективность
доработанного варианта становится аналогичной недоработанному и при этом введённый счётчик изменений дополнительно 
замедлил программу. While был заменён на For что не дало видимых изменений."""
