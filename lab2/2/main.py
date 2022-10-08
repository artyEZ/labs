import csv
from typing import List, Set, Dict
import mypy
import re
import pandas as pd

file = "C:/Users/artyo/Desktop/dataset.csv"

df = pd.read_csv(file)
columns: list = df["Day"].tolist()

rows = df.index
start_date = columns[0]
end_date = columns[-1]
daterange = pd.date_range(start_date, end_date)
for i in rows:
    # if (df["Day"][i] = "2021" ):
    print((df["Day"][i]))

# daterange = pd.date_range(start_date, end_date)
# len_of_columns = len(columns)
# for i in len(columns):
