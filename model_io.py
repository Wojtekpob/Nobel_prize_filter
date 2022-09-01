import json
import yaml
import csv
from model import Laureat, Prize


def read_from_json(file_handle):
    # handle = json.load(file_handle)
    laureates = file_handle["laureates"]
    all_laureates = []
    for laureat in laureates:
        name = laureat["firstname"]
        surname = laureat["surname"]
        born = laureat["born"]
        died = laureat["died"]
        born_country = laureat["bornCountry"]
        born_city = laureat["bornCity"]
        gender = laureat["gender"]
        winnings = laureat["prizes"]
        prizes = [Prize(winning["year"], winning["category"], winning["motivation"]) for winning in winnings]
        all_laureates.append(Laureat(name, surname, born, died, born_country, born_city, gender, prizes))
    return all_laureates


def write_to_csv(file_handle, laureats):
    fieldnames = ["firstname", "surname", "born", "died", "bornCountry", "bornCity", "gender", "prizes"]
    writer = csv.DictWriter(file_handle, fieldnames)
    writer.writeheader()
    for laureat in laureats:
        name = laureat.name
        surname = laureat.surname
        born = laureat.born
        died = laureat.died
        born_country = laureat.born_country
        born_city = laureat.born_city
        gender = laureat.gender
        prizes = [(prize.year, prize.category, prize.motivation) for prize in laureat.prizes]
        writer.writerow({
            "firstname": name,
            "surname": surname,
            "born": born,
            "died": died,
            "bornCountry": born_country,
            "bornCity": born_city,
            "gender": gender,
            "prizes": prizes
        })


def write_to_yaml(file_handle, laureats):
    laureats_data = []
    for laureat in laureats:
        name = laureat.name
        surname = laureat.surname
        born = laureat.born
        died = laureat.died
        born_country = laureat.born_country
        born_city = laureat.born_city
        gender = laureat.gender
        prizes = [[prize.year, prize.category, prize.motivation] for prize in laureat.prizes]
        laureat_data = {
            "firstname": name,
            "surname": surname,
            "born": born,
            "died": died,
            "bornCountry": born_country,
            "bornCity": born_city,
            "gender": gender,
            "prizes": prizes
        }
        laureats_data.append(laureat_data)
    yaml.dump(laureats_data, file_handle)
