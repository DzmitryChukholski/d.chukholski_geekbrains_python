'''2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.'''

UserTime = int(input('Введите время в секундах: '))
print(f'Вы ввели время равное {UserTime//3600}ч:{UserTime//60%60}м:{UserTime%60}с')