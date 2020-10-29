"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""

from random import randint
from statistics import median
import timeit


def my_median(unsorted_array):
    cashe = []
    for i in unsorted_array:
        left = 0
        right = 0
        buffer = 0
        for j in range(len(unsorted_array)):
            if i > unsorted_array[j]:
                left += 1
            elif i < unsorted_array[j]:
                right += 1
            else:
                buffer += 1
        if left == right or left+buffer/2 == right or left == right+buffer/2 or buffer >= len(unsorted_array)//2+1:
            return i
        # Кэш был добавлен поскольку оказалось что при опеделённых обстоятельствах алгоритм не справляется,
        # поэтому нужно дополнительное условие, но оно действительно только если ни один элемент
        # не отвечает всем остальным условиям, поэтому пришлось делать такие танцы с бубном
        if (buffer >= len(unsorted_array)//2 and (left > 0 or right > 0)):
            cashe.append(i)
    return cashe[0]


num_of_num = int(input('Введите число m: '))
unsorted_array = [randint(-100, 100) for i in range(2 * num_of_num + 1)]
print(f'Исходный массив:      {unsorted_array}')
print(f'Сортированный массив: {sorted(unsorted_array[:])}')
print(f'Медианное значение согласно встроенной функции равняется:      {median(unsorted_array)}')
print(f'Медианное значение согласно написанной мною функции равняется: {my_median(unsorted_array)}')

"""
Моё решение работает без сортировки массива, однако проведя замеры по времени были получены следующие результаты:

Медианное значение находится в центре массива:
встроенный - 0.47075449999999996
мой - 6.2558729
гномы - 1.0674103

Медианное значение находится в начале массива:
встроенный - 0.508700000000001
мой - 1.224746999999999
гномы - 3.2299084999999996

Медианное значение находится в конце массива:
встроенный - 0.5006907999999992
мой - 10.907258400000002
гномы - 3.5276964

Делаем вывод что предложенное мною решение очень сильно зависит от положения медианного значения внутри массива.
В идеальных для моего решения условиях, когда медианное значения располагается первым в массиве, решение не столь
значительно уступает встроенной функции и даже превосходит гномов, однако чем дальше медианное значение отходит 
от начала массива, тем катастрофичнее становится разрыв между данным решением и встроенной функцией
"""

# Ну и поскольку сейчас 2:21, а мне всё ещё не спится так как я окончательно сбил режим, то попробуем и гномов


def gnome(unsorted_array):
    i, size = 1, len(unsorted_array)
    while i < size:
        if unsorted_array[i - 1] <= unsorted_array[i]:
            i += 1
        else:
            unsorted_array[i - 1], unsorted_array[i] = unsorted_array[i], unsorted_array[i - 1]
            if i > 1:
                i -= 1
    return unsorted_array


print(f'Медианное значение согласно гномьей сортировке равняется:      {gnome(unsorted_array[:])[(num_of_num*2+1)//2]}')

# Этот алгоритм я использовал для тестирования своей функции
"""while True:
    unsorted_array = [randint(-100, 100) for i in range(2 * num_of_num + 1)]
    a = my_median(unsorted_array)
    print(a)
    if a == None or a != median(unsorted_array):
        print('___________________________')
        print(unsorted_array)
        print(median(unsorted_array))
        print(a)
        b = int('Дай мне ошибку')"""

# А это таймеры если интересно глянуть
"""
print(timeit.timeit('median([1, 2, 3, 4, 5, 6, 7])', 'from __main__ import median, unsorted_array'))
print(timeit.timeit('my_median([1, 2, 3, 4, 5, 6, 7])', 'from __main__ import my_median, unsorted_array'))
print(timeit.timeit('gnome([1, 2, 3, 4, 5, 6, 7])', 'from __main__ import gnome, unsorted_array'))
print(timeit.timeit('median([4, 2, 3, 1, 5, 6, 7])', 'from __main__ import median, unsorted_array'))
print(timeit.timeit('my_median([4, 2, 3, 1, 5, 6, 7])', 'from __main__ import my_median, unsorted_array'))
print(timeit.timeit('gnome([4, 2, 3, 1, 5, 6, 7])', 'from __main__ import gnome, unsorted_array'))
print(timeit.timeit('median([1, 2, 3, 7, 5, 6, 4])', 'from __main__ import median, unsorted_array'))
print(timeit.timeit('my_median([1, 2, 3, 7, 5, 6, 4])', 'from __main__ import my_median, unsorted_array'))
print(timeit.timeit('gnome([1, 2, 3, 7, 5, 6, 4])', 'from __main__ import gnome, unsorted_array'))
"""
