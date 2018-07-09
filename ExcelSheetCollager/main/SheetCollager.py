"""
Excel or Ods Sheet Collage is based on the input of the user.
"""
import pandas as pd

# Global Variables
from pandas import ExcelWriter

excelFilePathIs = ""
sheetsFoundAre = []
sheetData = []


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
    idxStartIs = 0
    startIs = 0
    stopIs = 0
    for idx, eachSheetData in enumerate(sheetData):
        print("Writing : ", idx + 1, "/", len(sheetData))
        idxStartIs = range(len(eachSheetData.index))
        startIs = startIs + idxStartIs.start
        stopIs = stopIs + idxStartIs.stop
        print(idxStartIs.start, " ", idxStartIs.step, " ", idxStartIs.stop)
        eachSheetData.to_excel(workbook, 'Sheet1', header=None, index=False,
                               startcol=startIs, startrow=stopIs)
    workbook.close()


def get_all_sheet_names(df):
    global sheetsFoundAre
    sheetsFoundAre = df.sheet_names
    print(df.sheet_names)


get_user_input()
set_excel_path()
read_excel_file()
write_sheet_data_to_excel()
