"""
Задание 7.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""


class desk:
    basic_queue = []
    ok_queue = []
    not_ok_queue = []

    def __init__(self, *args):
        for i in args:
            self.basic_queue.append(i)

    def try_to_solve_from_basic(self):
        if input('\n' + 'Успешно? Y/N ') == 'Y':
            self.ok_queue.insert(0,self.basic_queue.pop())
        else:
            self.not_ok_queue.insert(0, self.basic_queue.pop())
        self.print_me()

    def try_to_solve_from_nok(self):
        if len(self.not_ok_queue) > 0:
            if input('\n' + 'Успешно? Y/N ') == 'Y':
                self.ok_queue.insert(0, self.not_ok_queue.pop())
            self.print_me()
        else:
            print('Очередь NOK пуста')

    def print_me(self):
        print('basic queue:', end=' ')
        for i in self.basic_queue:
            print(i, end=' ')
        print('\n' + 'ok queue:', end=' ')
        for i in self.ok_queue:
            print(i, end=' ')
        print('\n' + 'not ok queue:', end=' ')
        for i in self.not_ok_queue:
            print(i, end=' ')


class task:
    name = str
    status = 'basic'

    def __init__(self, name):
        self.name = str(name)

    def __str__(self):
        return self.name


task_1 = task('task_1')
task_2 = task('task_2')
task_3 = task('task_3')
task_4 = task('task_4')
task_5 = task('task_5')

desk_1 = desk(task_1, task_2, task_3, task_4, task_5)
desk_1.try_to_solve_from_basic()
desk_1.try_to_solve_from_basic()
desk_1.try_to_solve_from_basic()
desk_1.try_to_solve_from_basic()
desk_1.try_to_solve_from_basic()
desk_1.try_to_solve_from_nok()
desk_1.try_to_solve_from_nok()
desk_1.try_to_solve_from_nok()
desk_1.try_to_solve_from_nok()
desk_1.try_to_solve_from_nok()
