import csv
from typing import List, Set, Dict
import mypy
import re
import pandas

file = "C:/Users/artyo/Desktop/dataset.csv"

df = pandas.read_csv(file)
df = df.rename(columns={"Day": "ID"})
print(df)



