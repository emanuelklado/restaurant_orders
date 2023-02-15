from pathlib import Path
import csv
from collections import Counter


data_dishes_list = []


def open_csv_file(path_to_file):
    with open(path_to_file, encoding="utf8") as file:
        file = csv.reader(file, delimiter=",", quotechar='"')
        for row in file:
            data_dishes_list.append(row)


def most_request_dish(name):
    dishes = []
    for person in data_dishes_list:
        if person[0] == name:
            dishes.append(person[1])
        favorite_dish = Counter(dishes)
    return favorite_dish.most_common()[0][0]


def hamburguer_counter_by_arnaldo():
    counter = 0
    for person in data_dishes_list:
        if person[0] == "arnaldo" and person[1] == "hamburguer":
            counter += 1
    return counter


def never_request_by_john():
    john_dishes = set()
    all_dishes = set()
    for dish in data_dishes_list:
        if dish[0] == "joao":
            john_dishes.add(dish[1])
        all_dishes.add(dish[1])
    return all_dishes.difference(john_dishes)


def days_never_showup():
    john_days = set()
    all_days = set()
    for day in data_dishes_list:
        if day[0] == "joao":
            john_days.add(day[2])
        all_days.add(day[2])
    return all_days.difference(john_days)


def read_csv_file(path_to_file):
    with open(path_to_file, encoding="utf8") as file:
        file = csv.reader(file, delimiter=",", quotechar='"')
        for row in file:
            data_dishes_list.append(row)
    return data_dishes_list


def get_results():
    results = [
        str(most_request_dish("maria")),
        f"\n{str(hamburguer_counter_by_arnaldo())}",
        f"\n{str(never_request_by_john())}",
        f"\n{str(days_never_showup())}",
    ]
    return results


def write_to_file(path_to_file, results):
    with open(path_to_file, "w") as file:
        file.writelines(results)


def analyze_log(path_to_file):
    if Path(path_to_file).suffix != ".csv":
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        read_csv_file(path_to_file)
        results = get_results()
        write_to_file("data/mkt_campaign.txt", results)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
