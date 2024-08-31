from datetime import datetime
from Report.ReportGenerator import ReportGenerator
import pandas as pd


class TxtReportGenerator(ReportGenerator):
    def __init__(self, separator=','):
        """
        Initialize the TxtReportGenerator class.
        :param separator: The separator between columns, default is '|'
        """
        self.separator = separator

    def generate_report(self, data: pd.DataFrame, output_format='txt', custom_file_name='report_DDMMYYYY'):
        """
        DataFrame Export to a text file.

        :param data: DataFrame to be exported
        :param output_path: path of output file
        """
        current_date_ddmmyyyy = datetime.now().strftime('%d%m%Y')
        custom_file_name = custom_file_name.replace('DDMMYYYY', current_date_ddmmyyyy)
        output_path = f"{custom_file_name}.{output_format}"
        with open(output_path, 'w', encoding='utf-8') as file:
            # Convert the DataFrame to a string, setting appropriate alignment and formatting
            report = self._format_dataframe(data)
            file.write(report)

    def _format_dataframe(self, df: pd.DataFrame) -> str:
        """
        Format a DataFrame as a string.

        :param df: DataFrame to be formatted
        :return: Formatted string
        """
        # Get the maximum width of each column for alignment
        col_widths = {col: df[col].astype(str).map(len).max() for col in df.columns}
        col_widths_header = {col: len(col) for col in df.columns}

        # header
        header = self.separator.join([f"{col.ljust(col_widths_header[col])}" for col in df.columns])

        # Create each row of data
        rows = []
        for _, row in df.iterrows():
            row_str = self.separator.join([f"{str(row[col]).strip().ljust(col_widths[col])}" for col in df.columns])
            rows.append(row_str)

        # Merge all parts
        report = f"{header}\n" + "\n".join(rows)
        return report
