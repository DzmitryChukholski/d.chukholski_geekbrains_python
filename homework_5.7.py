"""7. Создать (не программно) текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""

# поскольку выход компании в ноль не является убытком
# прибыль таких компаний учитывается при расчёте средней

import json

company_dict = {}
good_company_counter = 0
all_profit = 0
with open('for_homework_5-7.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        line = line.split()
        line.pop(1)
        company_name = line.pop(0)
        company_profit = float(line[0])-float(line[1])
        if company_profit >= 0:
            all_profit += company_profit
            good_company_counter += 1
        company_dict.update({company_name: company_profit})
average_profit = all_profit / good_company_counter
average_profit_dict = {'average_profit': average_profit}
result_list = [company_dict, average_profit_dict]

with open('for_homework_5-7_json.json', 'w', encoding='UTF-8') as file_json:
    json.dump(result_list, file_json)
