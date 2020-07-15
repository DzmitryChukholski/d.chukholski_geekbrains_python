"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в
виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""


class DateError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Date:
    day = int()
    month = int()
    year = int()
    date_str = ''

    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def convert_to_int(cls, string):
        date = cls(string)
        split_it = date.date_str.split('-')
        date.day = int(split_it[0])
        date.month = int(split_it[1])
        date.year = int(split_it[2])
        return date

    @staticmethod
    def valid_date(date):
        if date.month < 1 or date.month > 12:
            raise DateError('Неверный номер месяца')
        day_31 = [1, 3, 5, 7, 8, 10, 12]
        day_30 = [4, 6, 9, 11]
        if date.day < 1:
            raise DateError('Неверный номер дня')
        elif date.month in day_31 and date.day > 31:
            raise DateError('Неверный номер дня')
        elif date.month in day_30 and date.day > 30:
            raise DateError('Неверный номер дня')
        elif date.month == 2 and date.day > 29:
            raise DateError('Неверный номер дня')


my_date = Date.convert_to_int('25-4-1994')
my_date.valid_date(my_date)
print(f'Число: {my_date.day}\nМесяц: {my_date.month}\nГод: {my_date.year}')
