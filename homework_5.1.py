"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

with open('for_homework_5-1.txt', 'w', encoding='UTF-8') as file:
    while True:
        user_str = input('Введите строку: ')
        if user_str == '':
            break
        else:
            file.write(user_str + '\n')
