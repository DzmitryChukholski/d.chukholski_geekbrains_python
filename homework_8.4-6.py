"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных."""


from abc import ABC, abstractmethod


class CountError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    inside = {}
    divisions = {'Администрация': {}, 'Бухгалтерия': {}}

    def take_in(self, *args):
        for obj in args:
            new_dict = {}
            new_name = f'ID{obj.el_id}'
            if new_name not in self.inside:
                for key, value in obj.el_dict.items():
                    new_dict[key] = value
                new_dict['Количество'] = int(input(f'Введите количество поступившего оборудования {new_name}: '))
                self.inside[new_name] = new_dict
            else:
                self.inside[new_name]['Количество'] += \
                    int(input(f'Введите количество поступившего оборудования {new_name}: '))

    def to_division(self, move_to, *args):
        for ID in args:
            if ID in self.inside == False:
                print('Оборудование отсутсвует на складе')
            elif ID in self.divisions[move_to]:
                counter = int(input(f'Введите количество оборудования {ID} для передачи в {move_to}: '))
                try:
                    if self.inside[ID]['Количество'] - counter < 0:
                        raise CountError('Недостаточно оборудования на складе')
                    self.divisions[move_to][ID]['Количество'] += counter
                    self.inside[ID]['Количество'] -= counter
                except CountError as ce:
                    print(ce)
            else:
                new_dict = {}
                counter = int(input(f'Введите количество оборудования {ID} для передачи в {move_to}: '))
                for key, value in self.inside.items():
                    new_dict[key] = value
                new_dict['Количество'] = counter
                try:
                    if self.inside[ID]['Количество'] - new_dict['Количество'] < 0:
                        raise CountError('Недостаточно оборудования на складе')
                    self.divisions[move_to][ID] = new_dict
                    self.inside[ID]['Количество'] -= new_dict['Количество']
                except CountError as ce:
                    print(ce)


class Equipment(ABC):
    el_id = str
    cost = float
    guarantee = int
    name = str
    el_dict = {}

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def make_dict(self):
        pass


class Printer(Equipment):
    color = bool
    time_for_sheet = int

    def __init__(self, name, el_id, cost, guarantee, color, time_for_sheet):
        self.name = name
        self.el_id = el_id
        self.cost = cost
        self.guarantee = guarantee
        self.color = color
        self.time_for_sheet = time_for_sheet
        self.make_dict()

    def make_dict(self):
        self.el_dict = {'name': self.name, 'id': self.el_id, 'cost': self.cost, 'guarantee': self.guarantee,
                        'color': self.color, 'time_for_sheet': self.time_for_sheet}


class Monitor(Equipment):
    resolution = str
    diag = float

    def __init__(self, name, el_id, cost, guarantee, resolution, diag):
        self.name = name
        self.el_id = el_id
        self.cost = cost
        self.guarantee = guarantee
        self.resolution = resolution
        self.diag = diag
        self.make_dict()

    def make_dict(self):
        self.el_dict = {'name': self.name, 'id': self.el_id, 'cost': self.cost, 'guarantee': self.guarantee,
                        'resolution': self.resolution, 'diagonal': self.diag}


class Speakers(Equipment):
    stereo = bool

    def __init__(self, name, el_id, cost, guarantee, stereo):
        self.name = name
        self.el_id = el_id
        self.cost = cost
        self.guarantee = guarantee
        self.stereo = stereo
        self.make_dict()

    def make_dict(self):
        self.el_dict = {'name': self.name, 'id': self.el_id, 'cost': self.cost, 'guarantee': self.guarantee,
                        'stereo': self.stereo}


Kanon_MG200 = Printer(name='Kanon_MG200', el_id='000001', cost=300, guarantee=18, color=True, time_for_sheet=2)
Ipson_LS12 = Printer(name='Ipson_LS12', el_id='000002', cost=1500, guarantee=6, color=False, time_for_sheet=12)
Suemens_ARFKJ24 = Monitor(name='Suemens_ARFKJ24', el_id='001001', cost=600, guarantee=12, resolution='1080p', diag=23)
Saisung_25KLG12 = Monitor(name='Saisung_25KLG12', el_id='001002', cost=4000, guarantee=24, resolution='2160p', diag=98)
BLM666 = Speakers(name='BLM666', el_id='002001', cost=100, guarantee=6, stereo=False)
Hiaomi_Hi12 = Speakers(name='Hiaomi_Hi12', el_id='002002', cost=25, guarantee=18, stereo=True)

warehouse = Warehouse()
warehouse.take_in(Kanon_MG200, Ipson_LS12, Suemens_ARFKJ24, Saisung_25KLG12, BLM666, Hiaomi_Hi12)
warehouse.take_in(Kanon_MG200, Suemens_ARFKJ24)
warehouse.to_division('Администрация', 'ID000001', 'ID001001', 'ID002001')
warehouse.to_division('Бухгалтерия', 'ID000002', 'ID001002', 'ID002002')
warehouse.to_division('Администрация', 'ID000001')

for key, value in warehouse.inside.items():
    print(key, value['Количество'])
print('-----------------------')
for key, value in warehouse.divisions.items():
    print(key)
    for key1, value1 in value.items():
        print(key1, value1['Количество'])
