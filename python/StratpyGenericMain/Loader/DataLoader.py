from abc import ABC, abstractmethod


class DataLoader(ABC):

    @abstractmethod
    def load_data(self, filepath, **kwargs):
        """
        Load data and return a DataFrame.
        filepath: path to the data file.
        kwargs: optional parameters, such as delimiter, etc.
        Return value: pandas DataFrame object.
        """
        pass
