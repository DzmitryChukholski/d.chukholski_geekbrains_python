"""6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""

with open('for_homework_5-6.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()

result_dict = {}
hours_hunter = ''

for line in content:
    text = line.split(':')
    all_hours = 0
    for i in text[1]:
        if i.isdigit():
            hours_hunter = hours_hunter + i
        else:
            try:
                all_hours = all_hours + int(hours_hunter)
            except:
                pass
            hours_hunter = ''
    result_dict.update({text[0]: all_hours})

print('Список предметов:')
for key, value in result_dict.items():
    # этот кусок программы нужен для правильного окончания в слове "час" на выводе
    a = value % 100
    b = value % 10
    if value <= 20:
        if a == 1:
            c = 'час'
        if (a >= 2) and (a <= 4):
            c = 'часа'
        if (a > 4) or (a == 0):
            c = 'часов'
    else:
        if b == 1:
            c = 'час'
        if (b >= 2) and (b <= 4):
            c = 'часа'
        if (b > 4) or (b == 0):
            c = 'часов'
    print(f'{key}: {value} {c}')
