from abc import ABC, abstractmethod


class ProcessingStrategy(ABC):

    @abstractmethod
    def process(self, data_tables, operations):
        """
        Abstract methods for processing tables.
        data_tables: A dictionary with table names as keys and DataFrames as values.
        operations: A list of operations to be performed on the data.
        Return value: The processed DataFrame.
        """
        pass
