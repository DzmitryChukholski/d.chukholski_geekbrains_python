"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

# Python 3.8, система 64x
# Поскольку в прошлый раз занимаемый объём памяти получался нулевой для примера я решил взять разные типы сортировки
# из урока 7, вот только всё равно они показали нулевые результаты. Очень странные реультаты показывают быстрая
# и вставка, я так полагаю это значит что быстрая лучше всех, а вставка хуже всех. Пытался увеличить размер массива
# чтобы было нагляднее, вот только пузырёк делался минут 20 и так и не отсортировал, так что пришлось отказаться

from memory_profiler import profile
import random


@profile()
def fast_sort(lst_obj):
    def quick_sort(lst_obj):
        if len(lst_obj) <= 1:
            return lst_obj
        else:
            q = random.choice(lst_obj)
            L = []
            M = []
            R = []
            for elem in lst_obj:
                if elem < q:
                    L.append(elem)
                elif elem > q:
                    R.append(elem)
                else:
                    M.append(elem)
            return quick_sort(L) + M + quick_sort(R)
    return quick_sort


@profile()
def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


@profile()
def insertion_sort(lst_obj):
    for i in range(len(lst_obj)):
        v = lst_obj[i]
        j = i

        while (lst_obj[j-1] > v) and (j > 0):

            lst_obj[j] = lst_obj[j-1]
            j = j - 1

        lst_obj[j] = v
    return lst_obj


@profile()
def cocktail_sort(lst_obj):
    left = 0
    right = len(lst_obj) - 1
    while left <= right:
        for i in range(left, right):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        right -= 1
        for i in range(right, left, -1):
            if lst_obj[i-1] > lst_obj[i]:
                lst_obj[i], lst_obj[i-1] = lst_obj[i-1], lst_obj[i]
        left += 1
    return lst_obj


unsorted_list = [random.randint(0, 1000) for i in range(1000)]
print('Быстрая сортировка\n_________________________________________________________________')
fast_sort(unsorted_list[:])
print('_________________________________________________________________')
print('Пузырьковая сортировка\n_________________________________________________________________')
bubble_sort(unsorted_list[:])
print('_________________________________________________________________')
print('Сортировка вставкой\n_________________________________________________________________')
insertion_sort(unsorted_list[:])
print('_________________________________________________________________')
print('Шейкерная сортировка\n_________________________________________________________________')
cocktail_sort(unsorted_list[:])
print('_________________________________________________________________')

"""
Быстрая сортировка
_________________________________________________________________
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    25     18.7 MiB     18.7 MiB           1   @profile()
    26                                         def fast_sort(lst_obj):
    27     18.7 MiB      0.0 MiB           1       def quick_sort(lst_obj):
    28                                                 if len(lst_obj) <= 1:
    29                                                     return lst_obj
    30                                                 else:
    31                                                     q = random.choice(lst_obj)
    32                                                     L = []
    33                                                     M = []
    34                                                     R = []
    35                                                     for elem in lst_obj:
    36                                                         if elem < q:
    37                                                             L.append(elem)
    38                                                         elif elem > q:
    39                                                             R.append(elem)
    40                                                         else:
    41                                                             M.append(elem)
    42                                                     return quick_sort(L) + M + quick_sort(R)
    43     18.7 MiB      0.0 MiB           1       return quick_sort
_________________________________________________________________

Пузырьковая сортировка
_________________________________________________________________
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    46     18.7 MiB     18.7 MiB           1   @profile()
    47                                         def bubble_sort(lst_obj):
    48     18.7 MiB      0.0 MiB           1       n = 1
    49     18.7 MiB      0.0 MiB        1000       while n < len(lst_obj):
    50     18.7 MiB      0.0 MiB      500499           for i in range(len(lst_obj)-n):
    51     18.7 MiB      0.0 MiB      499500               if lst_obj[i] > lst_obj[i+1]:
    52     18.7 MiB      0.0 MiB      252610                   lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
    53     18.7 MiB      0.0 MiB         999           n += 1
    54     18.7 MiB      0.0 MiB           1       return lst_obj
_________________________________________________________________

Сортировка вставкой
_________________________________________________________________
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    57     18.7 MiB     18.7 MiB           1   @profile()
    58                                         def insertion_sort(lst_obj):
    59     18.7 MiB     -3.3 MiB        1001       for i in range(len(lst_obj)):
    60     18.7 MiB     -3.2 MiB        1000           v = lst_obj[i]
    61     18.7 MiB     -3.2 MiB        1000           j = i
    62                                         
    63     18.7 MiB  -1671.8 MiB      253610           while (lst_obj[j-1] > v) and (j > 0):
    64                                         
    65     18.7 MiB  -1668.5 MiB      252610               lst_obj[j] = lst_obj[j-1]
    66     18.7 MiB  -1668.6 MiB      252610               j = j - 1
    67                                         
    68     18.7 MiB     -3.3 MiB        1000           lst_obj[j] = v
    69     18.7 MiB     -0.1 MiB           1       return lst_obj
_________________________________________________________________

Шейкерная сортировка
_________________________________________________________________
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    72     18.7 MiB     18.7 MiB           1   @profile()
    73                                         def cocktail_sort(lst_obj):
    74     18.7 MiB      0.0 MiB           1       left = 0
    75     18.7 MiB      0.0 MiB           1       right = len(lst_obj) - 1
    76     18.7 MiB      0.0 MiB         501       while left <= right:
    77     18.7 MiB      0.0 MiB      250500           for i in range(left, right):
    78     18.7 MiB      0.0 MiB      250000               if lst_obj[i] > lst_obj[i+1]:
    79     18.7 MiB      0.0 MiB      126043                   lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
    80     18.7 MiB      0.0 MiB         500           right -= 1
    81     18.7 MiB      0.0 MiB      250000           for i in range(right, left, -1):
    82     18.7 MiB      0.0 MiB      249500               if lst_obj[i-1] > lst_obj[i]:
    83     18.7 MiB      0.0 MiB      126567                   lst_obj[i], lst_obj[i-1] = lst_obj[i-1], lst_obj[i]
    84     18.7 MiB      0.0 MiB         500           left += 1
    85     18.7 MiB      0.0 MiB           1       return lst_obj
_________________________________________________________________
"""