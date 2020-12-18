from openpyxl import worksheet
from openpyxl import workbook
from openpyxl import Workbook
from openpyxl import load_workbook
import os.path as op 
import os
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment

directory = os.getcwd()
directory = directory + r'\\Sheets\\'
filetype = r".xlsx"

creating = input(r'New school year:')
school_year = input(r'School year:')
section = input(r'Section:')

file_exists = op.exists(directory)

if file_exists:
    print("This directory already exists")
else:
    os.makedirs(directory + school_year + r'\\' + section)

sydirectory = directory + school_year + r'\\' + section + r'\\'

filedestination = sydirectory + section + filetype

file_exists = op.isfile(filedestination)

wb = Workbook()

if creating == "True":
    if file_exists:
        print("This school year already exists")
    else:
        wb = Workbook()
        wb.save(filedestination)
        wb = load_workbook(filedestination)
        if section in wb.sheetnames:
            print("This section exists")
        else:
            wb.create_sheet(section)
            print("Created sheet" + " " + section)
            wb.save(filename = filedestination)
        wb = load_workbook(filedestination)
        ws = wb[section]
        ws.merge_cells('B1:K1')
        ws.column_dimensions[get_column_letter(1)].width = 30
        cell = ws.cell(row = 1, column = 2)
        cell.value = 'Performance Task'
        cell.alignment = Alignment(horizontal = 'center', vertical = 'center')
        ws.merge_cells('L1:U1')
        cell = ws['L1']
        cell.value = 'Written Work'
        cell.alignment = Alignment(horizontal = 'center', vertical = 'center')
        cell = ws.cell(row = 2, column = 1)
        cell.value = "Student Names"
        cell.alignment = Alignment(horizontal = 'center', vertical = 'center')
        x = 1
        y = 2
        while x < 11:    
            cell = ws.cell(row = 2, column = y)
            cell.value = x
            cell.alignment = Alignment(horizontal = 'center', vertical = 'center')
            x = x+1
            y = y+1
        x = 1
        y = 12
        while x < 11:    
            cell = ws.cell(row = 2, column = y)
            cell.value = x
            cell.alignment = Alignment(horizontal = 'center', vertical = 'center')
            x = x+1
            y = y+1
        wb.save(filename = filedestination)
           
