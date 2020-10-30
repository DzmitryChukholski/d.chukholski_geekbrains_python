"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""

# Да, вот это вот всё мне тоже пришлось переделывать заново.

# 1. Добавлена проверка вводимых значений, теперь допустимо вводить только int, при ошибочном вводе выдаёт ошибку и
# предлагает ввести новое значение
# 2. Добавлены слоты
# 3. Вместо валидации добавлена функция insert которая сама определяет в какую сторону должен быть добавлен потомок,
# поэтому запрещён вызов insert_left/right
# 4. Ранее была возможность имея корень 8 и левого потомка 4 поменять левого потомка на 3 и тогда четвёрка уходила тому
# влево, хотя должна была бы вправо - исправлено
# 5. Хотел добавить возможность при инициализации сразу объявлять потомков, но слишком многое пришлось бы менять +
# возникает проблема коллизии при добавлении элемента в уже существующую цепочку (хотя это тоже можно нормально
# прописать). Опущу этот момент, тем более что и так всё это делаю уже по второму кругу
# 6. Переопределён __str__. Выглядит хреново, но я не смог найти как увеличивать количество \t на каждом шаге,
# поэтому скобки в помощь


class BinaryTree:
    __slots__ = ('root', 'left_child', 'right_child')

    def __init__(self, root_obj):
        # корень
        try:
            self.root = int(root_obj)
        except ValueError:
            while type(root_obj) != int:
                root_obj = input('Вы ввели неверное значение. Значение может быть только целым числом.'
                                 '\nВведите новое значение: ')
                try:
                    root_obj = int(root_obj)
                    print(type(root_obj))
                    self.root = root_obj
                except:
                    continue
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    def __str__(self):
        return f'Корень {self.root}(\n\tЛевый потомок {self.left_child}\n\tПравый потомок {self.right_child}\n\t)'

    def insert(self, new_node):
        if new_node >= self.root:
            return self.__insert_right(new_node)
        else:
            return self.__insert_left(new_node)

    # добавить левого потомка
    def __insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            if self.left_child.root < new_node:
                tree_obj.left_child = self.left_child
            else:
                tree_obj.right_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def __insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            if self.right_child.root < new_node:
                tree_obj.left_child = self.right_child
            else:
                tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert(4)
r.insert(3)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert(12)
r.insert(16)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
print(r)
