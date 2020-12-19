import os.path as op
import os
import pandas as pd
import csv

directory = os.getcwd()
directory = directory + r'\\Sheets\\'
filetype = r".csv"
typeofactivity = input(r'Type Of Activity:')

school_year = input(r'School year:')
section = input(r'Section:')

file_exists = op.exists(directory)

if file_exists:
    print("This directory already exists")
else:
    os.makedirs(directory + school_year + r'\\' + section)

sydirectory = directory + school_year + r'\\' + section + r'\\'

if typeofactivity == 'Performance':
    with open(sydirectory + 'Number of Students and Activities.csv', 'rt') as f:
        data = csv.DictReader(f)
        for row in data:
            noPT = row['No. of PT']
            noPT = int(noPT)

    for i in range(noPT):
        df = pd.read_csv(sydirectory + 'log.csv')
        value =  df.loc[i, "Performance Task Status"]
        if value == False:
            print(i,"Incomplete")
        else:
            print(i,"Complete")

elif typeofactivity == 'Written':
    with open(sydirectory + 'Number of Students and Activities.csv', 'rt') as f:
        data = csv.DictReader(f)
        for row in data:
            noWT = row['No. of WT']
            noWT = int(noWT)

    for i in range(noWT):
        df = pd.read_csv(sydirectory + 'log.csv')
        value =  df.loc[i, "Written Task Status"]
        if value == False:
            print(i,"Incomplete")
        else:
            print(i,"Complete")