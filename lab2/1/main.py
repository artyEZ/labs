import csv
import pandas as pd

my_file_for_dates = open("X.csv", "w+")
my_file_for_dates.close()

my_file_for_data = open("Y.csv", "w+")
my_file_for_data.close()

file = "C:/Users/artyo/Desktop/dataset.csv"
df = pd.read_csv(file)

row_number = len(df.index)
print(row_number)
column_day_data = df["Day"].tolist()
column_data_data = df["Exchange rate"].tolist()

f = open(file)
for i in range(row_number):
    with open("X.csv", "a", newline="") as file:
        writer = csv.writer(file, delimiter="\n")
        writer.writerow([column_day_data[i]])

    with open("Y.csv", "a", newline="") as file:
        writer = csv.writer(file, delimiter="\n")
        writer.writerow([column_data_data[i]])
f.close()
