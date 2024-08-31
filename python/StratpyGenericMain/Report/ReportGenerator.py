from abc import ABC, abstractmethod
import pandas as pd


class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self, data: pd.DataFrame, output_format: str, custom_file_name: str, sheet_names=None):
        pass
