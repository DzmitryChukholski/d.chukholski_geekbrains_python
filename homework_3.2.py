"""2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""

def user_data_print(name,surname,year,city,email,phone):
    return f'Пользователя зовут {name} {surname}, он родился в {year} году, проживает в городе {city}, с ним можно связаться по электронной почте {email} либо по телефону {phone}'

user_data_template = {'name': ['имя',str],
                  'surname': ['фамилию',str],
                  'year': ['год рождения',int],
                  'city': ['город проживания',str],
                  'email': ['адрес электронной почты',str],
                  'phone': ['номер телефона',str]}

user_data = {}

for keys, value in user_data_template.items():
    user_data[keys]=value[1](input(f'Введите {value[0]} пользователя: '))

print(user_data_print(**user_data))