from openpyxl import workbook
from openpyxl import worksheet
from openpyxl import Workbook
from openpyxl import load_workbook
import os.path as op 
import os
import csv
from tkinter import *
from tkinter.ttk import *
import UI
from UI import App
from tkinter import ttk
from tkinter import StringVar
from tkinter import Entry

def addstuds(sy, sec):
    school_year = sy #input(r'School Year:')
    section = sec #input(r'Section:')
    app = App()
    ib = app.get_inputbox()

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

    def testprint():
        sname = ib.get()
        ib.delete(0,'end')
        ib.unbind('<Return>')
        return sname
    def testconf():
        ib.unbind()
        return ''

    if file_exists:
        print("Adding Students")
        i = 1
        noStuds = noStuds + 1
        while i < noStuds:
            #this is causing errors
            #try using a variable.trace("w", continue) function later on
            studentname = ib.bind('<Return>', testprint)#input(r'Student Full Name:')
            confirmation = ib.bind('<Return>', testconf)#input(r'Press ENTER if the student name is right')
            if confirmation == '':
                wb = load_workbook(filedestination)
                sheet = wb[r'Quarter 1']
                studcell = sheet.cell(row = i+2, column = 1)
                studcell.value = studentname
                sheet = wb[r'Quarter 2']
                studcell = sheet.cell(row = i+2, column = 1)
                studcell.value = studentname
                sheet = wb[r'Quarter 3']
                studcell = sheet.cell(row = i+2, column = 1)
                studcell.value = studentname
                sheet = wb[r'Quarter 4']
                studcell = sheet.cell(row = i+2, column = 1)
                studcell.value = studentname
                wb.save(filename = filedestination)
            else:
                i = i - 1
            i = i + 1
        wb = load_workbook(filedestination)
        sheet = wb[r'Quarter 1']
        maxcell = sheet.cell(row = noStuds+2, column = 1)
        maxcell.value = "Highest Possible Grade"
        sheet = wb[r'Quarter 2']
        maxcell = sheet.cell(row = noStuds+2, column = 1)
        maxcell.value = "Highest Possible Grade"
        sheet = wb[r'Quarter 3']
        maxcell = sheet.cell(row = noStuds+2, column = 1)
        maxcell.value = "Highest Possible Grade"
        sheet = wb[r'Quarter 4']
        maxcell = sheet.cell(row = noStuds+2, column = 1)
        maxcell.value = "Highest Possible Grade"
        wb.save(filename = filedestination)
        
    else:
        print("School Year does not Exist")
