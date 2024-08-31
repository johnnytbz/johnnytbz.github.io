from Report.ReportGenerator import ReportGenerator
from datetime import datetime


class CsvReportGenerator(ReportGenerator):
    def generate_report(self, data, output_format='csv', custom_file_name='report_DDMMYYYY'):
        current_date_ddmmyyyy = datetime.now().strftime('%d%m%Y')
        custom_file_name = custom_file_name.replace('DDMMYYYY', current_date_ddmmyyyy)
        output_path = f"{custom_file_name}.{output_format}"
        data.to_csv(output_path, index=False)
