import os.path as op 
import os
import openpyxl
import csv
import pandas as pd
import numpy as np

def preprocessqtdata(sy, sec, qt):
    school_year = sy #input(r'School Year:')
    section = sec #input(r'Section:')
    quarter = qt #(r'Quarter:')

    if quarter == '1':
        sheetname = "Quarter 1"
    elif quarter == '2':
        sheetname = "Quarter 2"
    elif quarter == '3':
        sheetname = "Quarter 3"
    elif quarter == '4':
        sheetname = "Quarter 4"

    directory = os.getcwd()
    directory = directory + r'\\Sheets\\'
    filetype = r".xlsx"
    sydirectory = directory + school_year + r'\\' + section + r'\\'
    sheetdirectory = sydirectory + section + filetype

    df = pd.read_excel(sheetdirectory, sheet_name = sheetname, engine ='openpyxl', header=1).reset_index() 
    df = df.fillna(0)
    df.to_csv(sydirectory + r'Dataframe.csv', index=False)

def logstudmisacts(sy, sec, qt):
    school_year = sy #input(r'School Year:')
    section = sec #input(r'Section:')
    quarter = qt #(r'Quarter:')

    directory = os.getcwd()
    directory = directory + r'\\Sheets\\'
    filetype = r".xlsx"
    sydirectory = directory + school_year + r'\\' + section + r'\\'
    sheetdirectory = sydirectory + section + filetype

    if quarter == '1':
        sheetname = "Quarter 1"
    elif quarter == '2':
        sheetname = "Quarter 2"
    elif quarter == '3':
        sheetname = "Quarter 3"
    elif quarter == '4':
        sheetname = "Quarter 4"

    df = pd.read_excel(sheetdirectory, sheet_name = sheetname, engine ='openpyxl', header=1,).reset_index() 
    df = df.isnull()
    df = df.any(axis=1)
    print(df)
    df.to_csv(sydirectory + r'Final Missing Student Activity Log.csv', index=False)