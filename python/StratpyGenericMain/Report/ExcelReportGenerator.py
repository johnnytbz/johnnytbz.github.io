import pandas as pd
from datetime import datetime
from Report.ReportGenerator import ReportGenerator


class ExcelReportGenerator(ReportGenerator):
    def __init__(self, sheet_names=None):
        """
        Initializes the ExcelReportGenerator class.
        :param sheet_names: List of sheet names. If None, 'Sheet1' is used by default.
        """
        self.sheet_names = sheet_names or ['Sheet1']

    def generate_report(self, data, output_format='xlsx', custom_file_name='report_DDMMYYYY', sheet_name='Sheet1'):
        """
        Export a DataFrame to an Excel file.
        :param data: DataFrames to export, where keys are worksheet names and values are DataFrames
        :param output_path: Path to the output file
        """
        current_date_ddmmyyyy = datetime.now().strftime('%d%m%Y')
        custom_file_name = custom_file_name.replace('DDMMYYYY', current_date_ddmmyyyy)

        if output_format.lower() == 'excel':
            output_format = 'xlsx'

        if output_format not in ['xlsx', 'xls']:
            raise ValueError(f"Invalid output format: {output_format}")

        output_path = f"{custom_file_name}.{output_format}"
        engine = 'xlsxwriter'

        with pd.ExcelWriter(output_path, engine=engine) as writer:
            data.to_excel(writer, sheet_name=sheet_name, index=False)

            worksheet = writer.sheets[sheet_name]
            for idx, col in enumerate(data.columns):
                max_length = max(data[col].astype(str).map(len).max(), len(col))
                worksheet.set_column(idx, idx, max_length)
