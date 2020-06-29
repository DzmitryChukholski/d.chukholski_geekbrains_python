"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

with open('for_homework_5-2.txt', 'r', encoding='UTF-8') as file:
    count_lines = 0
    for line in file:
        count_lines += 1
    print(f'Количество строк в тексте равно {count_lines}')

    file.seek(0)
    content = file.readlines()
    count_lines = 1
    for line in content:
        count_words = len(line.split())
        print(f'В строке {count_lines} количество слов равно {count_words}')
        count_lines += 1
