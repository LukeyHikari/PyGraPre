import csv
import os.path as op
import os

def qcsvcreate(sy, sec, numstud):
    school_year = sy #input(r'School year:')
    section = sec #input(r'Section:')
    noofstudents = numstud #input(r'No. Of Students:')
    noofstudents = int(noofstudents)
    directory = os.getcwd()
    directory = directory + r'\\Sheets\\' + school_year + r'\\' + section

    file_exists = op.exists(directory)

    if file_exists:
        print("Section exists. Creating CSVs")
    else:
        print("Section does not exist")

    sydirectory = directory + r'\\'

    with open(sydirectory + "Q1.csv", 'w', newline='') as file:
        fieldnames = ['Performance Task Status', 'Written Task Status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for _ in range(10):
            writer.writerow({'Performance Task Status': False, 'Written Task Status': False})

    with open(sydirectory + "Q2.csv", 'w', newline='') as file:
        fieldnames = ['Performance Task Status', 'Written Task Status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for _ in range(10):
            writer.writerow({'Performance Task Status': False, 'Written Task Status': False})

    with open(sydirectory + "Q3.csv", 'w', newline='') as file:
        fieldnames = ['Performance Task Status', 'Written Task Status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for _ in range(10):
            writer.writerow({'Performance Task Status': False, 'Written Task Status': False})

    with open(sydirectory + "Q4.csv", 'w', newline='') as file:
        fieldnames = ['Performance Task Status', 'Written Task Status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for _ in range(10):
            writer.writerow({'Performance Task Status': False, 'Written Task Status': False})

    with open(sydirectory + "Number of Students and Activities.csv", 'w', newline='') as file:
        fieldnames = ['No. of Students', 'No. of PT', 'No. of WT']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'No. of Students': noofstudents, 'No. of PT': 10, 'No. of WT': 10})