from Report.ReportGenerator import ReportGenerator
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from datetime import datetime


class PdfReportGenerator(ReportGenerator):
    def generate_report(self, data, output_format='pdf', custom_file_name='report_DDMMYYYY'):
        current_date_ddmmyyyy = datetime.now().strftime('%d%m%Y')
        custom_file_name = custom_file_name.replace('DDMMYYYY', current_date_ddmmyyyy)
        output_path = f"{custom_file_name}.{output_format}"

        doc = SimpleDocTemplate(output_path, pagesize=A4)
        elements = []
        styles = getSampleStyleSheet()

        table_data = [list(data.columns)] + data.values.tolist()
        table = Table(table_data)

        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        elements.append(table)
        elements.append(Spacer(1, 12))

        doc.build(elements)
