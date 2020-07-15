"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой."""


class UserZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


a = float(input('Введите делимое: '))
try:
    b = float(input('Введите делитель: '))
    if b == 0:
        raise UserZeroDivisionError('Деление на ноль невозможно')
    print(f'Результат равен {a/b}')
except UserZeroDivisionError as user_error:
    print(user_error)
