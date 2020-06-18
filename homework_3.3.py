"""3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов."""

#Да, решение наркоманское, но мне захотелось поприкалываться

def my_func(a,b,c):
    try:
        result = [float(a),float(b),float(c)]
        result.sort(reverse=1)
        return result[0]+result[1]
    except ValueError:
        return 'Неверные данные'

print(my_func(input('Введите первое число: '),input('Введите второе число: '),input('Введите третье число: ')))
