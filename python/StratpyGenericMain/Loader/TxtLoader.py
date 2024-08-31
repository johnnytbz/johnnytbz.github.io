from Loader.DataLoader import DataLoader
import pandas as pd


class TxtLoader(DataLoader):
    def load_data(self, filepath, separator=','):
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        # Use the specified delimiter to split each row of data.
        data = [line.strip().split(separator) for line in lines]
        # Convert it to DataFrame
        df = pd.DataFrame(data[1:], columns=data[0])
        return df
