import pandas as pd
import datetime
import os


def get_data_xy(input_file_x: str, input_file_y: str, date: datetime.date):
    if os.path.exists(input_file_x) and os.path.exists(input_file_y):
        df_x = pd.read_csv(input_file_x)
        df_y = pd.read_csv(input_file_y)
        print(df_x)

        for i in range(df_x.shape[0]):
            if df_x["Data"].iloc[i].replace("-", "") == str(date).replace("-", ""):
                index = i
                break
        if index >= 0:
            return df_y.iloc[index]
        return None

        # if ()

    raise FileNotFoundError


if __name__ == "__main__":
    file_x = "C:/Users/artyo/PycharmProjects/labs/lab2/1/X.csv"
    file_y = "C:/Users/artyo/PycharmProjects/labs/lab2/1/Y.csv"

    exist_date = datetime.date(2020, 2, 3)
    # print(exist_date)
    get_data_xy(file_x, file_y, exist_date)
