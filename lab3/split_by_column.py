import pandas as pd
import os


def write_to_file(input_file: str, output_directory: str) -> None:
    """

    :param output_directory:
    :param input_file: Start file with dataset
    :return: Nothing
    """
    if os.path.exists(input_file):

        if not os.path.exists(os.path.join(output_directory, 'divide_data_output')):
            os.mkdir(os.path.join(output_directory, 'divide_data_output'))

        df = pd.read_csv(input_file)
        df["Day"].to_csv(os.path.join(output_directory, 'divide_data_output', 'X.csv'), index=False)
        df["Exchange rate"].to_csv(os.path.join(output_directory, 'divide_data_output', 'Y.csv'), index=False)

    else:
        raise FileNotFoundError

