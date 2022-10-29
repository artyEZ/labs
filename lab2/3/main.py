import pandas as pd
from typing import NoReturn


def write_to_file(_df: pd.DataFrame, _mas: list[int]) -> NoReturn:
    lf = _df.loc[_mas[0]:_mas[-1]]
    data = str(lf["Day"].iloc[0]).replace("-", "") + "_" + str(lf["Day"].iloc[lf.shape[0] - 1]).replace("-", "")
    lf.to_csv(data + ".csv", index=False)


if __name__ == "__main__":

    file = "C:/Users/artyo/Desktop/dataset.csv"
    df = pd.read_csv(file)

    mas = list(range(5))
    index_list = df.shape[0]

    while index_list > 0:
        write_to_file(df, mas)
        mas = [i + 5 for i in mas]
        index_list = index_list - 5




