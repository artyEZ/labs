import pandas as pd
import datetime
import os

def get_data_xy(input_file_x: str, input_file_y:str, date: datatime.date):
    df = pd.read_csv(input_file)