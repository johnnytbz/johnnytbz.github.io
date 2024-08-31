import pandas as pd

from Loader.DataLoader import DataLoader


class CSVLoader(DataLoader):
    def load_data(self, filepath, **kwargs):
        return pd.read_csv(filepath, **kwargs)
