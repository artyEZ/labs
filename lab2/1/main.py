import csv
import pandas as pd
from typing import NoReturn


def formatted_file(input_file: str) -> NoReturn:
    df = pd.read_csv(input_file)
    df["Day"] = pd.to_datetime(df.Day, format="%Y-%m-%d")  # превращаю Str to datatime64[ns]
    df["Date"] = df["Day"].dt.date
    del df["Day"]
    print(df)


# def write_to_file(input_file: str, output_file: str) -> NoReturn:
#     df = pd.read_csv(input_file)
#     row_number = len(df.index)
#     column_day_data = df["Day"].tolist()
#     column_data_data = df["Exchange rate"].tolist()
#
#     f = open(input_file)
#     for i in range(row_number):
#         with open(output_file, "a", newline="") as input_file:
#             writer = csv.writer(input_file, delimiter="\n")
#             writer.writerow([column_day_data[i]])
#     f.close()


# РЕАЛИЗАЦИЯ ФУНКЦИИ#
if __name__ == "__main__":
    try:
        file_from = "C:/Users/artyo/Desktop/dataset.csv"
        file_to = "X.csv"
        formatted_file(file_from)
        # write_to_file(file_from, file_to)

    except FileNotFoundError:
        print("No such file exists!")

    try:
        file_from = "C:/Users/artyo/Desktop/dataset.csv"
        formatted_file(file_from)
        file_to = "Y.csv"
        # write_to_file(file_from, file_to)

    except FileNotFoundError:
        print("No such file exists!")
