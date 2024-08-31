from Loader.CSVLoader import CSVLoader
from Loader.DataLoader import DataLoader
from Loader.ExcelLoader import ExcelLoader
from Loader.JSONLoader import JSONLoader
from Loader.TxtLoader import TxtLoader

# from Loader.PDFLoader import PDFLoader


def load_files(file_configs):
    data_tables = {}
    for file_config in file_configs:
        loader_class = globals()[file_config['loader']]
        loader = loader_class()
        if 'separator' in file_config:
            data_tables[file_config['name']] = loader.load_data(file_config['filepath'],
                                                                separator=file_config['separator'])
        else:
            data_tables[file_config['name']] = loader.load_data(file_config['filepath'])
    return data_tables
