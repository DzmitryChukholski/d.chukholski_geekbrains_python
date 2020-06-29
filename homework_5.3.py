"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

# Позволю себе незначительно изменить условие,
# поскольку я привык считать оклад в деньгах.
# В качестве порогового значения будет 5000$
# Сумма выбрана чисто для сюжета файла

ponies = {}
count_employee = 0
salary_all = 0
with open('for_homework_5-3.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        line = line.split()
        ponies.update({line[0]: line[1]})
        count_employee += 1
print('Оклад менее 5000$ имеют:')
for key, value in ponies.items():
    if float(value) < 5000:
        print(key)
    salary_all += float(value)
salary_for_statistics = salary_all / count_employee
print(f'Средняя зарплата сотрудников составляет {salary_for_statistics:.2f}$')
