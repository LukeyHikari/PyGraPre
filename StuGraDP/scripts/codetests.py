import os.path as op
import os
import pandas as pd
import csv

directory = os.getcwd()
directory = directory + r'\\Sheets\\'
filetype = r".csv"

school_year = '2020-2021' #input(r'School year:')
section = 'Aguinaldo' #input(r'Section:')

file_exists = op.exists(directory)

if file_exists:
    print("This directory already exists")
else:
    os.makedirs(directory + school_year + r'\\' + section)

sydirectory = directory + school_year + r'\\' + section + r'\\'

fields = ['Written Task Status']
test = pd.read_csv(sydirectory + 'log.csv')
test.loc[0, "Written Task Status"] = True
print(test)
test.to_csv(sydirectory + 'log.csv', index = False)


