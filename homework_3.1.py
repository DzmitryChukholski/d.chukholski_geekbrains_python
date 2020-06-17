"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""

while True:
    dividend = input('Введите делимое: ')
    divisor = input('Введите делитель: ')
    try:
        dividend = float(dividend)
        divisor = float(divisor)
        result = dividend / divisor
        break
    except ValueError:
        continue
    except ZeroDivisionError:
        result = float('inf')
        break

print(f'Результат деления равен {result}')