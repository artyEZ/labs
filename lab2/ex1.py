import csv
from typing import List, Set, Dict
import mypy
import re

my_file_for_dates = open("X.csv", "w+")
my_file_for_data = open("Y.csv", "w+")
file = "C:/Users/artyo/Desktop/dataset.csv"

f = open(file)
for line in f:
    splited_line = re.split(";", line)
    print(splited_line, end="")




