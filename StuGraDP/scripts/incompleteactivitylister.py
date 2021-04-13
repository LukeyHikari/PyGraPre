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
    csvquartername = ""
    file_exists = op.exists(directory)
    incacts = []
    if file_exists:
        print("Section Exists. Proceeding to Checking")
    else:
        print("Section does not exist.")

    sydirectory = directory + school_year + r'\\' + section + r'\\'

    if quarter == 'Quarter 1':
        csvquartername = "Q1"
    elif quarter == 'Quarter 2':
        csvquartername = "Q2"
    elif quarter == 'Quarter 3':
        csvquartername = "Q3"
    elif quarter == 'Quarter 4':
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
                print(i+1,"Incomplete")
                incacts.append(i+1)
            else:
                print(i+1,"Complete")

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
                print(i+1,"Incomplete")
                incacts.append(i+1)
            else:
                print(i+1,"Complete")

    return(incacts)