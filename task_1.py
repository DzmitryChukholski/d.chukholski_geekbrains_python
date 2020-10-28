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

# Программы из дз к первому занятию, задание №3
# Python 3.8, система 64x

from memory_profiler import profile


class company:
    name = str
    money = int

    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __lt__(self, other):
        return self.money < other.money

    def __str__(self):
        return f'{self.name} {self.money}'


@profile()
def first():
    das_ist_dict = {'Яблочко': 999999, 'Груша': 400000, 'Тракторный завод': -1004, 'ИП Игорь Аркадьевич': 4,
                    'ООО Синий столб': 68, 'Бабушка на рынке': 312, 'ГазНефтьМеталлПроституткиАлюминийГрупп': 999998}
    val_1_list = []
    result = {}
    for value in das_ist_dict.values():
        val_1_list.append(value)
    val_1_list.sort()
    for i in range(0, 3):
        temp_val = val_1_list.pop()
        for key, value in das_ist_dict.items():
            if value == temp_val:
                result[key] = value
    return result


@profile()
def second():
    das_ist_dict = {'Яблочко': 999999, 'Груша': 400000, 'Тракторный завод': -1004, 'ИП Игорь Аркадьевич': 4,
                    'ООО Синий столб': 68, 'Бабушка на рынке': 312, 'ГазНефтьМеталлПроституткиАлюминийГрупп': 999998}
    val_2_dict = {}
    result = {}
    for key, value in das_ist_dict.items():
        val_2_dict[value] = key
    val_2_list = sorted(val_2_dict, reverse=True)
    for i in range(0, 3):
        result[val_2_dict[val_2_list[i]]] = val_2_list[i]
    return result


@profile()
def third():
    jabloczko = company(name='Яблочко', money=999999),
    grusza = company(name='Груша', money=400000),
    traktor = company(name='Тракторный завод', money=-1004),
    ip = company(name='ИП Игорь Аркадьевич', money=4),
    ooo = company(name='ООО Синий столб', money=68),
    babuszka = company(name='Бабушка на рынке', money=312),
    val_3_list = [jabloczko, grusza, traktor, ip, ooo, babuszka]
    val_3_list.sort(reverse=True)
    result = []
    for i in range(0, 3):
        result.append(val_3_list[i])
    return result


first()
second()
third()

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    38     18.7 MiB     18.7 MiB           1   @profile()
    39                                         def first():
    40     18.7 MiB      0.0 MiB           2       das_ist_dict = {'Яблочко': 999999, 'Груша': 400000, 'Тракторный завод': -1004, 'ИП Игорь Аркадьевич': 4,
    41     18.7 MiB      0.0 MiB           1                       'ООО Синий столб': 68, 'Бабушка на рынке': 312, 'ГазНефтьМеталлПроституткиАлюминийГрупп': 999998}
    42     18.7 MiB      0.0 MiB           1       val_1_list = []
    43     18.7 MiB      0.0 MiB           1       result = {}
    44     18.7 MiB      0.0 MiB           8       for value in das_ist_dict.values():
    45     18.7 MiB      0.0 MiB           7           val_1_list.append(value)
    46     18.7 MiB      0.0 MiB           1       val_1_list.sort()
    47     18.7 MiB      0.0 MiB           4       for i in range(0, 3):
    48     18.7 MiB      0.0 MiB           3           temp_val = val_1_list.pop()
    49     18.7 MiB      0.0 MiB          24           for key, value in das_ist_dict.items():
    50     18.7 MiB      0.0 MiB          21               if value == temp_val:
    51     18.7 MiB      0.0 MiB           3                   result[key] = value
    52     18.7 MiB      0.0 MiB           1       return result

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    55     18.8 MiB     18.8 MiB           1   @profile()
    56                                         def second():
    57     18.8 MiB      0.0 MiB           2       das_ist_dict = {'Яблочко': 999999, 'Груша': 400000, 'Тракторный завод': -1004, 'ИП Игорь Аркадьевич': 4,
    58     18.8 MiB      0.0 MiB           1                       'ООО Синий столб': 68, 'Бабушка на рынке': 312, 'ГазНефтьМеталлПроституткиАлюминийГрупп': 999998}
    59     18.8 MiB      0.0 MiB           1       val_2_dict = {}
    60     18.8 MiB      0.0 MiB           1       result = {}
    61     18.8 MiB      0.0 MiB           8       for key, value in das_ist_dict.items():
    62     18.8 MiB      0.0 MiB           7           val_2_dict[value] = key
    63     18.8 MiB      0.0 MiB           1       val_2_list = sorted(val_2_dict, reverse=True)
    64     18.8 MiB      0.0 MiB           4       for i in range(0, 3):
    65     18.8 MiB      0.0 MiB           3           result[val_2_dict[val_2_list[i]]] = val_2_list[i]
    66     18.8 MiB      0.0 MiB           1       return result

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    69     18.8 MiB     18.8 MiB           1   @profile()
    70                                         def third():
    71     18.8 MiB      0.0 MiB           1       jabloczko = company(name='Яблочко', money=999999),
    72     18.8 MiB      0.0 MiB           1       grusza = company(name='Груша', money=400000),
    73     18.8 MiB      0.0 MiB           1       traktor = company(name='Тракторный завод', money=-1004),
    74     18.8 MiB      0.0 MiB           1       ip = company(name='ИП Игорь Аркадьевич', money=4),
    75     18.8 MiB      0.0 MiB           1       ooo = company(name='ООО Синий столб', money=68),
    76     18.8 MiB      0.0 MiB           1       babuszka = company(name='Бабушка на рынке', money=312),
    77     18.8 MiB      0.0 MiB           1       val_3_list = [jabloczko, grusza, traktor, ip, ooo, babuszka]
    78     18.8 MiB      0.0 MiB           1       val_3_list.sort(reverse=True)
    79     18.8 MiB      0.0 MiB           1       result = []
    80     18.8 MiB      0.0 MiB           4       for i in range(0, 3):
    81     18.8 MiB      0.0 MiB           3           result.append(val_3_list[i])
    82     18.8 MiB      0.0 MiB           1       return result

"""

# Исходя из данных замеров можно сказать что все три решения являются эффективными с точки зрения потребляемой памяти
# Представленные решения не требуют оптимизации по памяти, а при выборе одного из решений следует руководствоваться
# иными параметрами, например скоростью выполнения
