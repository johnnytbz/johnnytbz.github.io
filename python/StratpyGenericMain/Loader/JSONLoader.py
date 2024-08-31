from Loader.DataLoader import DataLoader
import pandas as pd


class JSONLoader(DataLoader):
    def load_data(self, filepath):
        return pd.read_json(filepath)
