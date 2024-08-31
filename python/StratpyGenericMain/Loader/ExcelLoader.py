from Loader.DataLoader import DataLoader
import pandas as pd


class ExcelLoader(DataLoader):
    def load_data(self, filepath):
        return pd.read_excel(filepath)
