'''Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.'''

a = 0
while a<=0:
    a = float(input('Введите результат первого дня '))
b = float(input('Введите желаемый результат '))
i = 1

while a < b:
    a = a*1.1
    i += 1

print(f'Результат будет достигнут на {i} день')