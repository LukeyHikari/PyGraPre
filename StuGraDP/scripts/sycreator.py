from openpyxl import worksheet
from openpyxl import workbook
from openpyxl import Workbook
from openpyxl import load_workbook
import os.path as op 
import os
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment
import csvcreator as csvc

def sycreate(crsy, sy, sec, numstud):
    creating = crsy #input(r'New school year:')

    def centeractnumbers(quarter):
        wb = load_workbook(filedestination)
        ws = wb[quarter]
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

    def fillsheetq1():
        wb = load_workbook(filedestination)
        quarter = r'Quarter 1'
        ws = wb[quarter]
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
        centeractnumbers(quarter)
        wb.save(filename = filedestination)

    def fillsheetq2():
        wb = load_workbook(filedestination)
        quarter = r'Quarter 2'
        ws = wb[quarter]
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
        centeractnumbers(quarter)
        wb.save(filename = filedestination)

    def fillsheetq3():
        wb = load_workbook(filedestination)
        quarter = r'Quarter 3'
        ws = wb[quarter]
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
        centeractnumbers(quarter)
        wb.save(filename = filedestination)

    def fillsheetq4():
        wb = load_workbook(filedestination)
        quarter = r'Quarter 4'
        ws = wb[quarter]
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
        centeractnumbers(quarter)
        wb.save(filename = filedestination)

    if creating == "True":
        directory = os.getcwd()
        directory = directory + r'\\Sheets\\'
        filetype = r".xlsx"

        school_year = sy #input(r'School year:')
        section = sec #input(r'Section:')
        noofstudents = numstud #int(input(r'No. Of Students:'))
        file_exists = op.exists(directory)

        if file_exists:
            print("SY directory already exists")
            file_exists = op.exists(directory + school_year + r'\\' + section)
            if file_exists:
                print("Section Exists")
            else:
                os.makedirs(directory + school_year + r'\\' + section)     
        else:
            os.makedirs(directory + school_year + r'\\')

        sydirectory = directory + school_year + r'\\' + section + r'\\'

        filedestination = sydirectory + section + filetype

        file_exists = op.isfile(filedestination)

        if file_exists:
            print("This school year already exists")
        else:
            wb = Workbook()
            wb.save(filedestination)
            wb = load_workbook(filedestination)
            if section in wb.sheetnames:
                print("This section exists")
            else:
                wb.create_sheet("Quarter 1")
                wb.create_sheet("Quarter 2")
                wb.create_sheet("Quarter 3")
                wb.create_sheet("Quarter 4")
                print("Created the Quarterly Sheets")
                wb.save(filename = filedestination)
                csvc.qcsvcreate(school_year, section, noofstudents)
            fillsheetq1()
            fillsheetq2()
            fillsheetq3()
            fillsheetq4()
    
    else:
        pass

