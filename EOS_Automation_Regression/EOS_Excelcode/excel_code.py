import pytest
import pandas as pd
import time
import unittest
import os


class ExcelTest:
    def get_file_path_for_excel_file(self, excel_file_name_without_xlsx_extension=""):
        excel_file_path = os.path.dirname(os.path.dirname(
            os.path.abspath(__file__))) + "\\EOS_Excel\\" + excel_file_name_without_xlsx_extension + ".xlsx"
        return excel_file_path

    def return_data(self, file_path=""):
        # xls = pd.ExcelFile('../Testing_excel/firms.xlsx')
        xls = pd.ExcelFile(file_path)
        data = {}
        for sheet_name in xls.sheet_names:
            df = xls.parse(sheet_name)
            data[sheet_name] = df
        return data
