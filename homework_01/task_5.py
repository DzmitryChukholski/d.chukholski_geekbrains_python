"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""


# я знаю что не красиво писать по-русски, но мне очень лень переводить поскольку сейчас час ночи,
# я накуренный и слушаю Тессу Вайлет, поэтому сорри
class stopka:
    tarelki = 0
    stopki = 0
    max_v_stopke = 10

    def __init__(self, tarelki, stopki, max_v_stopke):
        self.tarelki = tarelki
        self.stopki = stopki
        self.max_v_stopke = max_v_stopke

    def __str__(self):
        return f'Тарелок в стопке {self.tarelki}, стопок {self.stopki}, максимум тарелок в стопке {self.max_v_stopke}'

    def add_tareloczku(self, tarelki):
        self.tarelki = self.tarelki + tarelki
        while self.tarelki >= self.max_v_stopke:
            self.stopki += 1
            self.tarelki = self.tarelki - self.max_v_stopke
        print(self)

    def remove_tareloczku(self, tarelki):
        self.tarelki = self.tarelki - tarelki
        while self.tarelki < 0:
            self.stopki -= 1
            self.tarelki = self.max_v_stopke - abs(self.tarelki)
        print(self)


stopoczka = stopka(1, 2, 10)
while True:
    stopoczka.add_tareloczku(int(input('Сколько добавить? ')))
    stopoczka.remove_tareloczku(int(input('Сколько убрать? ')))