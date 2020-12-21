from openpyxl import workbook
from openpyxl import worksheet
from openpyxl import Workbook
from openpyxl import load_workbook
import os.path as op 
import os
import csv
import pandas as pd 

def ptaskadd(sy, sec, actno, qt):
    school_year = sy #input(r'School Year:')
    section = sec #input(r'Section:')
    activityno = actno #int(input(r'Activity Number:'))
    quarter = qt #input(r'Quarter:')

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

    with open(sydirectory + 'Number of Students and Activities.csv', 'rt') as f:
        data = csv.DictReader(f)
        for row in data:
            noStuds = row['No. of Students']
            noStuds = int(noStuds)

    filedestination = sydirectory + section + filetype

    file_exists = op.isfile(filedestination)

    wb = Workbook()

    if file_exists:
        print("Adding to Performance Tasks")
        wb = Workbook()
        wb = load_workbook(filedestination)
        sheet = wb[sheetname]
        highestpossiblegrade = int(input(r'Highest Possible Grade:'))
        i = 1
        noStuds = noStuds + 1
        while i < noStuds:   
            studentgrade = int(input(r'Student Grade:'))
            displaygrade = str(studentgrade)
            print(r'Inputted Grade:' + r'' + displaygrade)
            confirmation = input(r'Press ENTER if the grade is right')
            if confirmation == '':
                if studentgrade > highestpossiblegrade:
                    print("Inputted Grade Exceeds Highest Possible Grade")
                    print("Please reenter this student's grade")
                    i = i - 1
                else:
                    studcell = sheet.cell(row = i+2, column = activityno + 1)
                    studcell.value = studentgrade               
            else:
                i = i - 1
            i = i + 1
        maxcell = sheet.cell(row = noStuds+2, column = activityno+1)
        maxcell.value = highestpossiblegrade
        wb.save(filename = filedestination)
        
    else:
        print("School Year does not Exist")

    #Logger
    print(r"Checking if all students are graded")
    wb = Workbook()
    wb = load_workbook(filedestination, read_only = True)
    sheet = wb[sheetname]

    if quarter == '1':
        csvquartername = "Q1"
    elif quarter == '2':
        csvquartername = "Q2"
    elif quarter == '3':
        csvquartername = "Q3"
    elif quarter == '4':
        csvquartername = "Q4"
    quartercsv = sydirectory + csvquartername + r'.csv'

    for x in range(noStuds-1):
        checkingcell = sheet.cell(row = x + 3, column = activityno + 1).value
        if checkingcell > 0:
            df = pd.read_csv(quartercsv)
            df.loc[activityno - 1, "Performance Task Status"] = True
            df.to_csv(quartercsv, index = False)
        elif checkingcell == 0:
            print(r"A student was not graded")
            df = pd.read_csv(quartercsv)
            df.loc[activityno - 1, "Performance Task Status"] = False
            df.to_csv(quartercsv, index = False)
            break