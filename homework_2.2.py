'''2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().'''

List1 = input('Введите элементы списка через пробел: ').split()

if len(List1) & 1:
    ListLen = len(List1)-1
else:
    ListLen = len(List1)

for i in range(0,ListLen,2):
    a = List1[i+1]
    List1[i+1] = List1[i]
    List1[i] = a

print(List1)