from openpyxl import workbook
from openpyxl import worksheet
from openpyxl import Workbook
from openpyxl import load_workbook
import os.path as op 
import os
import csv

school_year = input(r'School Year:')
section = input(r'Section:')
activitytype = input(r'Activity Type:')
activityno = int(input(r'Activity Number:'))

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
wb = load_workbook(filedestination, read_only = True)
sheet = wb[section]

if activitytype == 'Performance':
        for x in range(noStuds):
            checkingcell = sheet.cell(row = x + 3, column = activityno + 1).value
            if checkingcell == 0:
                studentnamecell = sheet.cell(row = x + 3, column = 1).value
                activitynumber = str(activityno)
                print("This student is missing Performance Activity Number" + " " + activitynumber + ":", studentnamecell)
            
elif activitytype == 'Written':
        for x in range(noStuds):
            checkingcell = sheet.cell(row = x + 3, column = activityno + 11).value
            if checkingcell == 0:
                studentnamecell = sheet.cell(row = x + 3, column = 1).value
                activitynumber = str(activityno)
                print("This student is missing Performance Activity Number" + " " + activitynumber + ":", studentnamecell)