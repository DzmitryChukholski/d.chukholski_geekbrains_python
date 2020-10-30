"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""

# Я хочу официально заявить что я ненавижу гитхаб. Я 9 часов, с 20:00 до 5:00, потратил на выполнение домашнего задания,
# сам с нуля написал своего Хаффмана, а потом, чтобы переделать дз к уроку 6, перешёл в его ветку и когда вернулся в
# ветку 8 урока оказалось что он всё удалил и вся моя работа пошла на смарку! Мне уже сказали что чтобы он так не делал
# я должен был лезть в какие-то ебеня и нажать там на какую-то кнопку, но тем не менее.
# Второй раз я Хаффмана писать не буду, переделаю то что в примере.

from collections import Counter, deque


class HaffmanString:
    __slots__ = ('original', 'haffman')

    def __init__(self, original):
        self.original = original
        self.haffman = self.haffman_code()

    def __str__(self):
        return f'Оригинальная строка: {self.original}\nЗакодированная строка: {self.haffman}'

    def __haffman_tree(self, original_string):
        elements = deque(sorted(Counter(original_string).items(), key=lambda item: item[1]))
        if len(elements) == 1:
            weight = elements[0][1]
            comb = {0: elements.popleft()[0], 1: None}
            elements.append((comb, weight))
        else:
            while len(elements) > 1:
                weight = elements[0][1] + elements[1][1]
                comb = {0: elements.popleft()[0],
                        1: elements.popleft()[0]}
                for i, _count in enumerate(elements):
                    if weight > _count[1]:
                        continue
                    else:
                        elements.insert(i, (comb, weight))
                        break
                else:
                    elements.append((comb, weight))
        return elements[0][0]

    def __make_haffman_code(self, tree, haffman_dict=dict(), path=''):
        if not isinstance(tree, dict):
            haffman_dict[tree] = path
        else:
            self.__make_haffman_code(tree[0], path=f'{path}0')
            self.__make_haffman_code(tree[1], path=f'{path}1')
        return haffman_dict

    def haffman_code(self):
        result_string = ''
        for i in self.original:
            result_string = f"{result_string} {self.__make_haffman_code(self.__haffman_tree(self.original))[i]}"
        return result_string


test_string = HaffmanString("beep boop beer!")
print(test_string)
"00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001"
