"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib


class files:
    name = str()
    my_hash = str()
    salt = 'Не забудь почистить историю'

    def __init__(self, my_name):
        self.name = str(my_name)
        self.my_hash = hashlib.sha256(self.name.encode() + self.salt.encode()).hexdigest()

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.my_hash == other.my_hash


vk = files('vk.com')
youtube = files('youtube.com')
pornhub = files('pornhub.com')
list_for_cache = [vk, youtube, pornhub]

while True:
    my_file = str(input('Давай проверим есть ли у меня твой сайт\nВведи его название: '))
    file_for_check = files(my_file)
    if file_for_check in list_for_cache:
        print('Это у меня уже есть')
    else:
        list_for_cache.append(file_for_check)
        print(f'Такого у меня небыло, но теперь добавил. Вот весь список:')
        for i in list_for_cache:
            print(i, end=' / ')
        print()
