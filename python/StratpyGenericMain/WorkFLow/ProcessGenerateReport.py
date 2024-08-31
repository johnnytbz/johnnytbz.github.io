from Report.CsvReportGenerator import CsvReportGenerator
from Report.ExcelReportGenerator import ExcelReportGenerator
from Report.PdfReportGenerator import PdfReportGenerator
from Report.TxtReportGenerator import TxtReportGenerator


def generate_report(file_configs, processed_data):
    output_format = file_configs['output_format']
    if output_format == 'xlsx' or output_format == 'xls':
        output_format = 'excel'
    generator_class = globals()[output_format.capitalize() + 'ReportGenerator']
    generator = generator_class()

    # Generate reports
    generator.generate_report(processed_data, file_configs['output_format'])
