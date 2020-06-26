"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

# если я правильно понял числа должны быть введены одной строкой

with open('for_homework_5-5.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Введите набор чисел разделённых пробелом: '))
with open('for_homework_5-5.txt', 'r', encoding='UTF-8') as file:
    numbers = file.readline().split()
numbers_sum = 0
try:
    for i in numbers:
        numbers_sum += float(i)
    print(f'Сумма введённых числе равна: {numbers_sum}')
except ValueError:
    print('Введены неверные данные')
