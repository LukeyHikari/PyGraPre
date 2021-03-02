import os.path as op
import os
import pandas as pd
import csv

def listincacts(atype, sy, sec, qt):
    directory = os.getcwd()
    directory = directory + r'\\Sheets\\'

    typeofactivity = atype #input(r'Type Of Activity:')
    school_year = sy #input(r'School year:')
    section = sec #input(r'Section:')
    quarter = qt #input(r'Quarter:')

    file_exists = op.exists(directory)

    if file_exists:
        print("This directory already exists")
    else:
        os.makedirs(directory + school_year + r'\\' + section)

    sydirectory = directory + school_year + r'\\' + section + r'\\'

    if quarter == '1':
        csvquartername = "Q1"
    elif quarter == '2':
        csvquartername = "Q2"
    elif quarter == '3':
        csvquartername = "Q3"
    elif quarter == '4':
        csvquartername = "Q4"
    quartercsv = sydirectory + csvquartername + r'.csv'


    if typeofactivity == 'Performance':
        with open(sydirectory + 'Number of Students and Activities.csv', 'rt') as f:
            data = csv.DictReader(f)
            for row in data:
                noPT = row['No. of PT']
                noPT = int(noPT)

        for i in range(noPT):
            df = pd.read_csv(quartercsv)
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
            df = pd.read_csv(quartercsv)
            value =  df.loc[i, "Written Task Status"]
            if value == False:
                print(i,"Incomplete")
            else:
                print(i,"Complete")