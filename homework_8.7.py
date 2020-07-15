"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
и умножение созданных экземпляров. Проверьте корректность полученного результата."""

# Эммммм..... в задании можно было бы написать чем именно отличается сложение и умножение
# комплексных чисел от обычных, а то я это проходил в универе в 2012 году и ничего не помню уже.....

# (a + bi) + (c + di) = (a + c) + (b + d)i
# (a + bi) * (c + di) = (ac - bd) + (bc + ad)i


class ComplexNum:
    a = float()
    bi = float()

    def __init__(self, real, image):
        self.a = float(real)
        self.bi = float(image)

    def __add__(self, other):
        a = self.a + other.a
        bi = self.bi + other.bi
        new = ComplexNum(a, bi)
        return new

    def __mul__(self, other):
        a = self.a * other.a - self.bi * other.bi
        bi = self.bi * other.a + self.a * other.bi
        new = ComplexNum(a, bi)
        return new

    def __str__(self):
        return f'{self.a} + {self.bi}i'


a = ComplexNum(1, 2)
b = ComplexNum(3, 4)
print(a)
print(b)
print(a+b)
print(a*b)
