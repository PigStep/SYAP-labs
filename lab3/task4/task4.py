# 4. Создать вручную и заполнить несколькими строками текстовый
# файл, в котором каждая строка будет содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой
# компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт
# средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и
# их прибылями, а также словарь со средней прибылью. Если фирма получила
# убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий
# файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit":
# 2000}]
# Подсказка: использовать менеджер контекста. – 1 балл (задача на
# оценку 10)

# Путь к файлу
import json


FIMRS_FILE = r"lab3\task4\firms.txt"
JSON_FILE = r"lab3\task4\companies.json"


def _read_companies(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return file.readlines()


def _get_profit(firm_line):
    _, _, profit, loss = firm_line.split()
    return int(profit) - int(loss)


def cout_average_profit(companies):
    profit_companies = [
        _get_profit(firm) for firm in companies if _get_profit(firm) > 0
    ]

    return sum(profit_companies) / len(profit_companies)


def _get_info(companies):
    companies_info = []
    for company in companies:
        name, type, profit, loss = company.split()
        companies_info.append((name, type, profit, loss))

    return companies_info


def get_companies_dict(companies):
    print(companies)
    companies_dict = {
        firm_name + firm_type: int(profit) - int(loss)
        for firm_name, firm_type, profit, loss in _get_info(companies)
    }
    companies_dict["average_profit"] = cout_average_profit(companies)
    return companies_dict


def save_to_json(companies_dict, json_file):
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(companies_dict, file, ensure_ascii=False)


if __name__ == "__main__":
    companies = _read_companies(FIMRS_FILE)
    companies_dict = get_companies_dict(companies)
    save_to_json(companies_dict, JSON_FILE)
