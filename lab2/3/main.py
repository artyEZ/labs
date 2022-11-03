import pandas as pd
from typing import NoReturn


def formatted_file(input_file: str) -> pd.DataFrame:
    df = pd.read_csv(file)

    df["Day"] = pd.to_datetime(df.Day, format="%Y-%m-%d")
    df["Day1"] = df["Day"].dt.date  # превращаю Str to datatime64[ns]
    df["Year"] = df["Day"].dt.year
    df["Week"] = df["Day"].dt.isocalendar().week
    return df


def clear_file(df: pd.DataFrame) -> pd.DataFrame:
    del df["Year"]
    del df["Week"]
    del df["Day1"]
    return  df


def range_of_years(input_file: str) -> list:
    df = formatted_file(input_file)

    start_range = df["Year"].iat[0]
    end_range = df["Year"].iat[-1]
    return [start_range, end_range]


def range_of_weeks(df: pd.DataFrame) -> list:
    start_range = df["Week"].iat[0]
    end_range = df["Week"].iat[-1]
    return [start_range, end_range]


def write_to_file(input_file: str) -> pd.DataFrame:
    df = formatted_file(input_file)

    range_of_years_list = range_of_years(input_file)
    # print(range_of_years_list[1])
    for years in range(range_of_years_list[0], range_of_years_list[1] - 1, -1):

        lf = df[df["Year"] == years]
        range_of_weeks_list = range_of_weeks(lf)

        for weeks in range(range_of_weeks_list[0], range_of_weeks_list[1] - 1, -1):
            try:
                sf = lf[lf["Week"] == weeks]
                data = str(sf["Day1"].iloc[1]).replace("-", "") + "_" + str(sf["Day1"].iloc[-1]).replace("-", "")

                clear_file(sf)

                sf.to_csv(data + ".csv", index=False)
            except Exception:
                pass

    # data = str(lf["Day"].iloc[0]).replace("-", "") + "_" + str(lf["Day"].iloc[lf.shape[0] - 1]).replace("-", "")
    # lf.to_csv(data + ".csv", index=False)


if __name__ == "__main__":
    file = "C:/Users/artyo/Desktop/dataset.csv"
    # print(formatted_file(file))
    write_to_file(file)
