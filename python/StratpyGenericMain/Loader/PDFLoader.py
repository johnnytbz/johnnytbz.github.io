import pandas as pd
import pdfplumber

from Loader.DataLoader import DataLoader


class PDFLoader(DataLoader):
    def load_data(self, filepath, **kwargs):
        with pdfplumber.open(filepath) as pdf:
            all_text = []
            for page in pdf.pages:
                all_text.append(page.extract_text())
        lines = [line.strip().split('\t') for line in "\n".join(all_text).splitlines()]
        df = pd.DataFrame(lines[1:], columns=lines[0])
        return df
