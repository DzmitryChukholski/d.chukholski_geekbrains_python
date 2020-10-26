"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""

import timeit
from functools import lru_cache


# эта функция зачем-то добавляет 0 в конце
def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

# Да, я не стал заморачиваться и нагуглил что есть готовый вариант
@lru_cache
def recursive_reverse_2(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


def recursive_reverse_3(number):
    return f'{str(number)[len(str(number))::-1]}'


@lru_cache()
def recursive_reverse_4(number):
    return f'{str(number)[len(str(number))::-1]}'


number = 123456789
print(f"recursive_reverse: "
      f"{timeit.timeit('recursive_reverse(number)', setup='from __main__ import recursive_reverse, number')}")
print(f"recursive_reverse_2: "
      f"{timeit.timeit('recursive_reverse_2(number)', setup='from __main__ import recursive_reverse_2, number')}")
print(f"recursive_reverse_3: "
      f"{timeit.timeit('recursive_reverse_3(number)', setup='from __main__ import recursive_reverse_3, number')}")
print(f"recursive_reverse_4: "
      f"{timeit.timeit('recursive_reverse_4(number)', setup='from __main__ import recursive_reverse_4, number')}")
