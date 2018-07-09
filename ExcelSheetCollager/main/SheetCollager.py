"""
Excel or Ods Sheet Collage is based on the input of the user.
"""
import pandas as pd

# Global Variables
from pandas import ExcelWriter

excelFilePathIs = ""
sheetsFoundAre = []
sheetData = []
leave_rows_between_sheet_merging = 2


def get_user_input():
    print("Getting user input")


def set_excel_path():
    global excelFilePathIs
    excelFilePathIs = "/home/suhaas/PycharmProjects/PychieWorks/ExcelSheetCollager/resources/TestSheetExceFormat.xlsx"
    print("Excel Path : ", excelFilePathIs)


def read_excel_file():
    xls = pd.ExcelFile(excelFilePathIs)
    get_all_sheet_names(xls)
    print("Sheets found : ", len(sheetsFoundAre))
    global sheetData
    for eachSheet in sheetsFoundAre:
        sheetData.append(pd.read_excel(xls, eachSheet))


def write_sheet_data_to_excel():
    print("Creating a new Sheet : \'hello.xlsx\'")
    workbook = ExcelWriter('hello.xlsx')
    # worksheet = workbook.add_worksheet()
    print("Merging Sheets")
    __start_col = 0
    __start_row = 0
    for idx, eachSheetData in enumerate(sheetData):
        print("Writing : ", idx + 1, "/", len(sheetData))
        sheet_range = range(len(eachSheetData.index))
        print(sheet_range.start, " ", sheet_range.step, " ", sheet_range.stop)
        eachSheetData.to_excel(workbook, 'Sheet1', header=True, index=False,
                               startcol=__start_col, startrow=__start_row)
        __start_col = __start_col + sheet_range.start
        __start_row = __start_row + sheet_range.stop + leave_rows_between_sheet_merging
    workbook.close()


def get_all_sheet_names(df):
    global sheetsFoundAre
    sheetsFoundAre = df.sheet_names
    print(df.sheet_names)


get_user_input()
set_excel_path()
read_excel_file()
write_sheet_data_to_excel()
