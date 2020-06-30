"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров)."""


class Worker:
    name = ''
    surname = ''
    position = ''
    income = {'wage': 0, 'bonus': 0}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self.income['wage'] + self.income['bonus']


human1 = Position()
human1.name = 'Игорь'
human1.surname = 'Некрутой'
human1.position = 'Тот чувак слева от кулера'
human1.income = {'wage': 220, 'bonus': 15}

print(f'{human1.position} это {human1.get_full_name()}, его доход составляет {human1.get_total_income()}$')