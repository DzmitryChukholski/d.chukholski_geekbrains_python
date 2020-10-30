"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""

from memory_profiler import profile

# Программа из дз к занятию 2

@profile()
def reverse_me_please(my_num, reverse):
    def reverse_me(my_num, reverse):
        if my_num == 0:
            return int(reverse)
        else:
            reverse = str(reverse) + str(my_num % 10)
            return reverse_me(my_num // 10, reverse)

    return reverse_me(my_num, '')


my_num = 123456789
print(reverse_me_please(my_num, ''))

"""Подводный камень заключается в том, что при каждом рекурсивном вызове функции вызывается и профилировщик.
Решение - обернуть рекурсивную функцию в обычную и уже к ней применить профилировщик"""
