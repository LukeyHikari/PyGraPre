from openpyxl import workbook
from openpyxl import worksheet
from openpyxl import Workbook
from openpyxl import load_workbook
import os.path as op 
import os
import csv
import pandas as pd

def grademisact(sy, sec, qt, atype, anum, stud):
    school_year = sy #input(r'School Year:')
    section = sec #input(r'Section:')
    quarter = qt #input(r'Quarter:')
    activitytype = atype #input(r'Activity Type:')
    activityno = anum #int(input(r'Activity Number:'))
    studwmisact = stud #input(r'Student with Missing Activity:')

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
    wb = load_workbook(filedestination)
    sheet = wb[sheetname]
    if file_exists:
        if activitytype == 'Performance':
            for x in range(noStuds):
                    studentcell = sheet.cell(row = x + 3, column = 1).value
                    highestpossiblegrade = sheet.cell(row = noStuds+2, column = activityno+1).value
                    print("The highest possible grade of this activity is:", highestpossiblegrade)
                    if studentcell == studwmisact:
                        activitycell = sheet.cell(row = x + 3, column = activityno + 1)
                        studentgrade = int(input(r'Student Grade:'))
                        activitycell.value = studentgrade
                        wb.save(filename = filedestination)
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
                        break

        if activitytype == 'Written':
            for x in range(noStuds):
                    studentcell = sheet.cell(row = x + 3, column = 1).value
                    highestpossiblegrade = sheet.cell(row = noStuds+2, column = activityno+11).value
                    print("The highest possible grade of this activity is:", highestpossiblegrade)
                    if studentcell == studwmisact:
                        activitycell = sheet.cell(row = x + 3, column = activityno + 11)
                        studentgrade = int(input(r'Student Grade:'))
                        activitycell.value = studentgrade
                        wb.save(filename = filedestination)
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
                            checkingcell = sheet.cell(row = x + 3, column = activityno + 11).value
                            if checkingcell > 0:
                                df = pd.read_csv(quartercsv)
                                df.loc[activityno - 1, "Written Task Status"] = True
                                df.to_csv(quartercsv, index = False)
                            elif checkingcell == 0:
                                print(r"A student was not graded")
                                df = pd.read_csv(quartercsv)
                                df.loc[activityno - 1, "Written Task Status"] = False
                                df.to_csv(quartercsv, index = False)
                                break
                        break
    else:
        print("This SY or Section does not exist")