import os.path as op
import os
import pandas
import csv

directory = os.getcwd()
directory = directory + r'\\Sheets\\'
filetype = r".csv"

school_year = input(r'School year:')
section = input(r'Section:')

file_exists = op.exists(directory)

if file_exists:
    print("This directory already exists")
else:
    os.makedirs(directory + school_year + r'\\' + section)

sydirectory = directory + school_year + r'\\' + section + r'\\'


with open(sydirectory + 'Number of Students and Activities.csv', 'rt') as f:
    data = csv.DictReader(f)
    for row in data:
        noStuds = row['No. of Students']
        print (noStuds)

print(noStuds)
#df = pandas.read_csv(sydirectory + 'Number of Students and Activities.csv')
#value = df['No. of Students']
#if value < 3:
    #print (df['No. of Students'])


