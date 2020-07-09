"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix.
Результатом сложения должна быть новая матрица."""

# чорд, несколько часов потратил в попытках заставить программу суммировать матрицы разной размерности
# и только потом вспомнил что так делать нельзя
# Хотя конечно можно это релизовать вставляя в пустые ячейки ноль


class Matrix:
    matrix = []

    def __init__(self, value):
        if str(type(value)) != str("<class 'list'>"):
            print('Ошибка: объект типа "матрица" должен содержать в себе список списков')
            raise ValueError
        for el in value:
            if str(type(el)) != str("<class 'list'>"):
                print('Ошибка: объект типа "матрица" должен содержать в себе список списков')
                raise ValueError
        for el in value:
            if len(el) != len(value[0]):
                print('Ошибка: матрица должна быть прямоугольной')
                raise ValueError
        self.matrix = value

    def __str__(self):
        result = str()
        for i in self.matrix:
            for el in i:
                result = result + str(el) + '\t'
            result = result + '\n'
        return result

    def __add__(self, other):
        new_matrix = []
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            print('Ошибка: сложение матриц возможно только при условии одинаковой размерности обоих матриц')
            raise ValueError
        for i in range(len(self.matrix)):
            new_matrix.append([])
            for j in range(len(self.matrix[0])):
                    new_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(new_matrix)


# Праивльное сложение матриц
a = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
b = Matrix([[9, 8, 7, 6], [5, 4, 3, 2], [1, 0, -1, -2], [-3, -4, -5, -6]])
print('Матрица а')
print(a)
print('Матрица b')
print(b)
c = a + b
print('Матрица c')
print(c)

# Неправильное сложение матриц
d = Matrix([[1, 2, 3], [5, 6, 7], [9, 10, 11], [13, 14, 15]])
e = Matrix([[9, 8, 7, 6], [5, 4, 3, 2], [1, 0, -1, -2], [-3, -4, -5, -6], [0, 0, 0, 0]])
print('Матрица d')
print(d)
print('Матрица e')
print(e)
f = d + e
print('Матрица f')
print(f)
