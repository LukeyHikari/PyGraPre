import os.path as op 
import os
import openpyxl
import csv
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer

def preprocess(sy,st,qt):
    school_year = sy #"2020-2021"
    section = st #"Agoncillo"
    quarter = qt #"Quarter 1"
    sheetname = quarter

    ErrorCodes = []

    directoryraw = os.getcwd()
    directory = directoryraw + r'\\Sheets\\'
    filetype = r'.xlsx'
    sydirectory = directory + school_year + r'\\' + section + r'\\'
    exportfolder = directoryraw + r'\\Quarterly Grades\\'
    sheetdirectory = sydirectory + section + filetype

    exgradescsvdir = exportfolder+section+"_"+quarter+"_"+school_year+".csv"

    preprocesseddatadir = sydirectory + r'PreprocessedData\\'
    ppdatadir = op.exists(preprocesseddatadir)

    if ppdatadir:
        print("PreProcessed Data Directory Already Exists")
    else:
        os.makedirs(preprocesseddatadir)

    nadataframe = None
    stqtdata = None
    stqtdata = pd.read_csv(exgradescsvdir,header=0)
    stqtdata.reset_index(drop=True,inplace=True)
    stqtdata.fillna(0)

    labelencoder = LabelEncoder()
    stqtdata['Student_Names_Cat'] = labelencoder.fit_transform(stqtdata['Student_Names'])
    stqtdata

    enc = OneHotEncoder(handle_unknown='ignore')
    enc_df = pd.DataFrame(enc.fit_transform(stqtdata[['Student_Names']]).toarray())
    stqtdata = stqtdata.join(enc_df)
    stqtdata

    finalcsvdir = preprocesseddatadir + r'Preprocessed Grades of ' + quarter + r'.csv'
    stqtdata.to_csv(finalcsvdir, index=False)
