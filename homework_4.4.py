"""4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]"""

import random


def check_list(my_list, i):
    temp_list = [random_list[j] for j in range(0, len(random_list))]
    check_pos = temp_list.pop(i)
    return check_pos not in temp_list


random_list = [random.randint(0, 10) for i in range(0, random.randint(5, 15))]
result_list = [random_list[i] for i in range(0, len(random_list)) if check_list(random_list, i)]

print(f'Исходный список: {random_list}')
print(f'Результирующий список {result_list}')

