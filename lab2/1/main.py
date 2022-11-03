import csv
import pandas as pd

# my_file_for_dates = open("X.csv", "w+")
# my_file_for_dates.close()
#
# my_file_for_data = open("Y.csv", "w+")
# my_file_for_data.close()
#
# file = "C:/Users/artyo/Desktop/dataset.csv"
# df = pd.read_csv(file)


def write_to_file(input_file: str) -> None:
    df = pd.read_csv(input_file)

    row_number = len(df.index)
    column_day_data = df["Day"].tolist()
    column_data_data = df["Exchange rate"].tolist()

    f = open(input_file)
    for i in range(row_number):
        with open("X.csv", "a", newline="") as f:
            writer = csv.writer(f, delimiter="\n")
            writer.writerow([column_day_data[i]])

        with open("Y.csv", "a", newline="") as f:
            writer = csv.writer(f, delimiter="\n")
            writer.writerow([column_data_data[i]])
    f.close()


if __name__ == "__main__":
    my_file_for_dates = open("X.csv", "w+")
    my_file_for_data = open("Y.csv", "w+")
    file = "C:/Users/artyo/Desktop/dataset.csv"

    write_to_file(file)


