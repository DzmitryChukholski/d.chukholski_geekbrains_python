"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

rus_lines = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
eng_lines = {}
with open('for_homework_5-4.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        line = line.split(' — ')
        line[1] = int(line[1])
        eng_lines.update({line[0]: line[1]})
with open('for_homework_5-4-rus.txt', 'w', encoding='UTF-8') as file:
    for key, value in eng_lines.items():
        file.write(f'{rus_lines[value]} — {value} \n')
