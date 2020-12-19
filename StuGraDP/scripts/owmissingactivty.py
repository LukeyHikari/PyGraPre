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
studwmisact = input(r'Student with Missing Activity:')

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
sheet = wb[section]

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
                break
