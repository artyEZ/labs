import csv
from typing import List, Set, Dict
import mypy
import re

my_file_for_dates = open("X.csv", "w+")
my_file_for_data = open("Y.csv", "w+")
file = "C:/Users/artyo/Desktop/dataset.csv"

# f = open(file)
# for line in f:
#     splited_line = re.split(";", line)
#     dates_from_splited_file = re.search(r'(\d{4}\-\d{2}\-\d{2})', splited_line[0])
#     print(dates_from_splited_file, end="")

f = open(file)
for line in f:
    f_all_splited = line.split(";")
    for i in range(len(f_all_splited)):
        dates_from_splited_file = re.findall(r'(\d{4}\-\d{2}\-\d{2})', f_all_splited[i])
        print(*dates_from_splited_file)




