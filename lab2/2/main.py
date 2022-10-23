import csv
from typing import List, Set, Dict
import mypy
import re
import pandas as pd
from typing import NoReturn
import calendar

# Могу сравнивать даты

file = "C:/Users/artyo/Desktop/dataset.csv"

df = pd.read_csv(file)
df["Day"] = pd.to_datetime(df["Day"], format="%Y-%m-%d")  # превращаю Str to datatime64[ns]
# df["Day"] = df["Day"].dt.date

df["YearsFromDay"] = df["Day"].dt.year
print(df["YearsFromDay"])


# columns: list = df["Day"].tolist()
# print(columns)
# rows = df.index
# start_date = columns[0]
# end_date = columns[-1]


# for i in len(a):
#     print(a[i])

# if start_date > end_date:

# a = pd.bdate_range(start=start_date, end=end_date)
# print(a)
# print(type(start_date), end_date)
# daterange = pd.date_range(start_date, end_date, freq="D")
# print(daterange)

# for i in rows:
#     # if (df["Day"][i] = "2021" ):
#     row_info_day = (df.iloc[i]["Day"])
#     print(type(row_info_day))

# daterange = pd.date_range(start_date, end_date)
# len_of_columns = len(columns)
# for i in len(columns):


# start_date = datetime.date(2020, 1, 1)
# end_date = datetime.date(2020, 1, 4)
# delta = datetime.timedelta(days=1)
#
# while start_date <= end_date:
#     print(start_date)
#     start_date += delta
def year_from_date(input_file: str) -> NoReturn:
    data = pd.read_csv(input_file)
    data["Day"] = pd.to_datetime(df["Day"], format="%Y-%m-%d")  # превращаю Str to datatime64[ns]
    data["YearsFromDay"] = df["Day"].dt.year
#
# def name_for_file() -> str:
