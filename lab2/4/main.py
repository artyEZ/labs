import numpy
import pandas as pd
import datetime
import os
from typing import Union
import autopep8


def formatted_file(input_file: str) -> pd.DataFrame:
    df = pd.read_csv(input_file)
    df["Day"] = pd.to_datetime(df.Day, format="%Y-%m-%d")
    return df


def get_data_xy(input_file: str, input_file_x: str, input_file_y: str,
                date: datetime.date) -> Union[numpy.float64, None]:
    if os.path.exists(input_file_x) and os.path.exists(input_file_y):

        formatted_file(input_file)
        df_x = pd.read_csv(input_file_x)
        df_y = pd.read_csv(input_file_y)
        index = -1
        for i in range(0, df_x.shape[0], 1):
            if df_x["Day"].iloc[i].replace("-", "") == str(date).replace("-", ""):
                index = i
                break
        if index >= 0:
            return df_y.iloc[index]["Exchange rate"]
        return None
    raise FileNotFoundError


if __name__ == "__main__":
    file = "C:/Users/artyo/Desktop/dataset.csv"
    file_x = "C:/Users/artyo/PycharmProjects/labs/lab2/1/X.csv"
    file_y = "C:/Users/artyo/PycharmProjects/labs/lab2/1/Y.csv"

    exist_date = datetime.date(2022, 9, 15)
    print(get_data_xy(file, file_x, file_y, exist_date))
