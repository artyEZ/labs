import csv
from typing import List, Set, Dict
import mypy
import re

my_file_for_dates = open("X.csv", "w+")
my_file_for_dates.close()

my_file_for_data = open("Y.csv", "w+")
my_file_for_data.close()

file = "C:/Users/artyo/Desktop/dataset.csv"

f = open(file)
for line in f:
    f_all_splited: list = line.split(";")
    for i in range(len(f_all_splited)):
        dates_from_splited_file: list = re.findall(r'(\d{4}\-\d{2}\-\d{2})', f_all_splited[i])
        data_from_splited_file: list = re.findall(r'(^\d+(?:[\.]\d+)?$)', f_all_splited[i])
        with open("X.csv", "a", newline="") as file:
            writer = csv.writer(file, delimiter="\n")
            if len(dates_from_splited_file) != 0:
                writer.writerow(*[dates_from_splited_file])
        with open("Y.csv", "a", newline="") as file:
            writer = csv.writer(file, delimiter="\n")
            if len(data_from_splited_file) != 0:
                writer.writerow(*[data_from_splited_file])
f.close()
