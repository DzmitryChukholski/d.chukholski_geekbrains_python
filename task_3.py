"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""

import hashlib


def hast_it(my_string):
    return hashlib.sha256(my_string.encode()).hexdigest()


my_string = str(input('Дай мне строку: '))
my_set = set()

for i in range(len(my_string)):
    for j in range(len(my_string), i, -1):
        if my_string[i:j] != my_string:
            my_set.add(hast_it(my_string[i:j]))

print(f'Количество подстрок в твоей строке равняется {len(my_set)}')
