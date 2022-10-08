import csv
from typing import List, Set, Dict
import mypy
import re
import pandas as pd

my_file_for_dates = open("X.csv", "w+")
my_file_for_dates.close()

my_file_for_data = open("Y.csv", "w+")
my_file_for_data.close()

file = "C:/Users/artyo/Desktop/dataset.csv"
df = pd.read_csv(file)
# df_day_coloumn = df["Day"]
# print(df_day_coloumn)
row_number = len(df.index)
print(row_number)
column_day_data = df["Day"].tolist()
column_data_data = df["Exchange rate"].tolist()
#
f = open(file)
for i in range(row_number):
    # dates_from_splited_file: list = re.findall(r'(\d{4}\-\d{2}\-\d{2})', df_day_coloumn[i])
    # print(coloumn_day_data[i])
    # data_from_splited_file: list = re.findall(r'(^\d+(?:[\.]\d+)?$)', df_day_coloumn)
    with open("X.csv", "a", newline="") as file:
        writer = csv.writer(file, delimiter="\n")
    #     # if len(dates_from_splited_file) != 0:
        writer.writerow([column_day_data[i]])
    with open("Y.csv", "a", newline="") as file:
        writer = csv.writer(file, delimiter="\n")
    #     if len(data_from_splited_file) != 0:
        writer.writerow([column_data_data[i]])
f.close()
