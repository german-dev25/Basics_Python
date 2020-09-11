# 7) Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json

firms_aver, profit, aver_profit, count_profit_firm = {}, {}, 0, 0
with open('text_task7.txt', 'r') as firms:
    for line in firms:
        firm = line.split()
        firm_name = ' '.join(firm[0:2])
        profit[firm_name] = int(firm[2]) - int(firm[3])
        if profit.setdefault(firm_name) >= 0:
            aver_profit += profit.setdefault(firm_name)
            count_profit_firm += 1
    if count_profit_firm != 0:
        firms_aver['Средняя прибыль'] = aver_profit / count_profit_firm
    else:
        firms_aver['Доходов нет'] = 0
    profit_list = profit, firms_aver

with open('lesson7.json', 'w', encoding='utf-8') as j:
    json.dump(profit_list, j)

# js_test = json.dumps(profit_list, ensure_ascii=False)
# print(js_test)
