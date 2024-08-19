from utilities import read_write_Data_excel
import unittest
import openpyxl
from EOS_Excelcode.excel_code import ExcelTest


class read_EOS_values(unittest.TestCase, ExcelTest):

    def read_dropdown_values(self, file_name, sheet_name):

        # filepath = "../TestData/p_wizard_test_data.xlsx"
        filepath = self.get_file_path_for_excel_file(file_name)

        DataDrivenClass = read_write_Data_excel.Read_Write_Data()
        # rows = DataDrivenClass.get_row_count(filepath, 'Class_values')
        rows = DataDrivenClass.get_row_count(filepath, sheet_name)
        data_list = []

        for r in range(2, rows + 1):
            drpdown_values = DataDrivenClass.read_data(filepath, sheet_name, r, 1)
            data_list.append(drpdown_values)
        print(data_list)
        return (data_list)