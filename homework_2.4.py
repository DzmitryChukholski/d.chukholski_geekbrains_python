'''4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове.'''

string1 = input('Введите строку: ').split()
print(string1)

for i, j in enumerate(string1,1):
    print(i,j[:10])