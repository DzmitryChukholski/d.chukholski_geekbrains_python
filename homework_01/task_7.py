"""
Задание 5.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
"""


class check_it_please:
    string = str

    def __init__(self, string):
        my_string = string.split()
        new_string = ''
        for i in my_string:
            new_string += i
        self.string = new_string
        print(f'"{string}" {self.cheking()}')

    def cheking(self):
        for i in range(len(self.string)):
            if self.string[i] != self.string[-1 - i]:
                return 'это не палиндром'
        return 'это палиндром'


a = check_it_please('молоко делили ледоколом')
b = check_it_please('топот')
c = check_it_please('не топот')
d = check_it_please('белки съели мой шашлык')