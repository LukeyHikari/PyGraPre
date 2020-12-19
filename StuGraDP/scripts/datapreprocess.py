import os.path as op 
import os
import openpyxl
import csv
import pandas as pd
import numpy as np

school_year = "2020-2021" #input(r'School Year:')
section = "Aguinaldo" #input(r'Section:')

directory = os.getcwd()
directory = directory + r'\\Sheets\\'
filetype = r".xlsx"
sydirectory = directory + school_year + r'\\' + section + r'\\'
sheetdirectory = sydirectory + section + filetype

df = pd.read_excel(sheetdirectory, sheet_name = section, engine ='openpyxl', header=1).reset_index() 
df = df.fillna(0)
df.to_csv(sydirectory + r'Dataframe.csv', index=False)
print(df)

df = pd.read_excel(sheetdirectory, sheet_name = section, engine ='openpyxl', header=1).reset_index() 
df = df.isnull()
df = df.any(axis=1)
print(df)
df.to_csv(sydirectory + r'Final Missing Student Activity Log.csv', index=False)