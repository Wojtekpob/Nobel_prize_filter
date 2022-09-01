import argparse
import sys
import requests
from model import Laureat
from model_io import read_from_json, write_to_csv, write_to_yaml


def main(arguments):
    #Example of using a program:  python3 ./nobel.py http://staff.elka.pw.edu.pl/~knalecz/PIPR/laureates.json laureats.txt yaml --gender female --category physics
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument('file', help="where to save")
    parser.add_argument('format', help="what format to save to")
    parser.add_argument('--gender')
    parser.add_argument('--year')
    parser.add_argument('--category')
    args = parser.parse_args()
    url = args.url
    file = args.file
    format = args.format
    year = args.year
    gender = args.gender
    category = args.category
    request = requests.get(url).json()
    laureats = read_from_json(request)
    if year:
        laureats = include_year(laureats, year)
    if gender:
        if laureats:
            laureats = include_gender(laureats, gender)
    if category:
        if laureats:
            laureats = include_category(laureats, category)
    if not laureats:
        print("no laureats with such cryteria")
    else:
        with open(file, 'w') as file_handle:
            if format == 'csv':
                write_to_csv(file_handle, laureats)
            elif format == 'yaml':
                write_to_yaml(file_handle, laureats)


def include_year(laureats, year):
    only_that_year = []
    for lauerat in laureats:
        prizes = []
        for prize in lauerat.prizes:
            if prize.year == year:
                only_that_year.append(lauerat)
                prizes.append(prize)
                if lauerat not in only_that_year:
                    only_that_year.append(lauerat)
        lauerat.prizes = prizes
    return only_that_year


def include_gender(laureats, gender):
    only_that_gender = []
    for laureat in laureats:
        if laureat.gender == gender:
            only_that_gender.append(laureat)
            if laureat not in only_that_gender:
                only_that_gender.append(laureat)
    return only_that_gender


def include_category(laureats, category):
    only_that_category = []
    for lauerat in laureats:
        prizes = []
        for prize in lauerat.prizes:
            if prize.category == category:
                prizes.append(prize)
                if lauerat not in only_that_category:
                    only_that_category.append(lauerat)
        lauerat.prizes = prizes
    return only_that_category


if __name__ == '__main__':
    main(sys.argv)
