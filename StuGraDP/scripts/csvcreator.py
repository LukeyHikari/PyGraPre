import csv
import os.path as op
import os

directory = os.getcwd()
directory = directory + r'\\Sheets\\'
filetype = r".csv"

school_year = input(r'School year:')
section = input(r'Section:')
noofstudents = input(r'No. Of Students:')
noofstudents = int(noofstudents)

file_exists = op.exists(directory)

if file_exists:
    print("This directory already exists")
else:
    os.makedirs(directory + school_year + r'\\' + section)

sydirectory = directory + school_year + r'\\' + section + r'\\'

with open(sydirectory + "log.csv", 'w', newline='') as file:
    fieldnames = ['Performance Task Status', 'Written Task Status']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for x in range(10):
        writer.writerow({'Performance Task Status': False, 'Written Task Status': False})

with open(sydirectory + "Number of Students and Activities.csv", 'w', newline='') as file:
    fieldnames = ['No. of Students', 'No. of PT', 'No. of WT']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'No. of Students': noofstudents, 'No. of PT': 10, 'No. of WT': 10})