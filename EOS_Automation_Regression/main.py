# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import os
from utilities.read_write_Data_excel import Read_Write_Data
read_excel = Read_Write_Data()
file_path=os.path.abspath('.') + "\\Downloads\\Returns 2024-05-30 11.20.03.xlsx"
value = read_excel.read_data(file_path,"Sheet1",2,1)
print("value")
print(value)
