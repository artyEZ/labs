import pandas as pd
from typing import NoReturn
import os


def formatted_file(input_file: str) -> pd.DataFrame:
    """

    :param input_file: file with dataset
    :return: DataFrame with added column
    """
    df = pd.read_csv(input_file)

    df["Day"] = pd.to_datetime(df.Day, format="%Y-%m-%d")
    df["Day1"] = df["Day"].dt.date  # превращаю Str to datatime64[ns]
    df["Year"] = df["Day"].dt.year
    return df


def range_of_date(input_file: str) -> list:
    """
    :param input_file: file with dataset
    :return: list with first and last year in the dataset
    """
    df = formatted_file(input_file)

    start_range = df["Year"].iat[0]
    end_range = df["Year"].iat[-1]
    return [start_range, end_range]


def write_to_file(input_file: str, output_directory: str) -> NoReturn:
    """

    :param output_directory:
    :param input_file: file with dataset
    :return: Nothing
    """
    if os.path.exists(input_file):

        if not os.path.exists(os.path.join(output_directory, 'data_to_years_output')):
            os.mkdir(os.path.join(output_directory, 'data_to_years_output'))

        _range_of_years = range_of_date(input_file)

        for _years in range(_range_of_years[0], _range_of_years[1] - 1, -1):
            df = formatted_file(input_file)
            df = df[df["Year"] == _years]
            data = str(df["Day1"].iloc[0]).replace("-", "") + "_" + str(df["Day1"].iloc[df.shape[0] - 1])\
                .replace("-", "") + '.csv'
            del df["Year"]
            del df["Day1"]
            df.to_csv(os.path.join(output_directory, 'data_to_years_output', data), index=False)
    else:
        raise FileNotFoundError

