import tkinter as tk
# from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import time
import xlwt
from xlwt import Workbook
import xlsxwriter
import pyodbc
import pandas as pd
from datetime import datetime
from time import gmtime, strftime

start = time.time()

root = tk.Tk()
root.title('HRA\'s File Link Creator for 3M/UB04/EOB')
root.resizable(0, 0)
# root.iconbitmap('icon.ico')

canvas1 = tk.Canvas(root, width=650, height=600, bg='lightsteelblue2', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='1280A - Report fixed-length Output Generator', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(300, 40, window=label1)

labelCreator = tk.Label(root, text='Created By: Rajender Kumar ', bg='lightsteelblue2')
labelCreator.config(font=('helvetica', 8))
canvas1.create_window(350, 80, window=labelCreator)

label2 = tk.Label(root, text=' ', bg='lightsteelblue2')
label2.config(font=('helvetica', 12))
canvas1.create_window(250, 440, window=label2)


label3 = tk.Label(root, text='Copyright © National Employee Benefits Administrators, Inc. ', bg='lightsteelblue2')
label3.config(font=('helvetica', 12))
canvas1.create_window(250, 500, window=label3)

labelPath = tk.Label(root, text='File Path: ', width = 250, bg='lightsteelblue2')
labelPath.config(font=('helvetica', 12))
canvas1.create_window(150, 120, window=labelPath)

filePath = tk.StringVar()
textboxPath = tk.Entry (root, textvariable = filePath)
canvas1.create_window(400, 120, width = 250, window=textboxPath)
print(filePath)
# labelName = tk.Label(root, text='Table Name: ', width = 250, bg='lightsteelblue2')
# labelName.config(font=('helvetica', 12))
# canvas1.create_window(150, 160, window=labelName)
#
# tblName = tk.StringVar(root)
# textboxName = tk.Entry(root, textvariable = tblName)
# canvas1.create_window(400, 160, width=250, window=textboxName)
#
#
# labelType = tk.Label(root, text='File Type: ', width = 250, bg='lightsteelblue2')
# labelType.config(font=('helvetica', 12))
# canvas1.create_window(150, 200, window=labelType)

# fileType = tk.StringVar(root, value=".xls")
# textboxType = tk.OptionMenu(root, ".xls", ".html")
# canvas1.create_window(400, 200, width=250, window=textboxType)


# Create a Tkinter variable
tkvar = tk.StringVar(root)


# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)



def CreateFile():
    global start
    global fileName
    fileName = filePath
    label2.configure(text= 'I am creating ' + fileName.get() + '. Please wait...')
    print("file path is: " + str(fileName.get()))

    df = pd.read_csv(str(fileName.get()))

    # df.head()

    ######## Change some columns as required by the client ########
    df.iloc[:, 4] = df.iloc[:, 4].astype(str).str.pad(9, fillchar='0')      # df['PARTICIPA']
    df.iloc[:, 9] = df.iloc[:, 9].astype(str).str.split('.').str[0].astype(str).str.pad(7, fillchar='0') + \
                    df.iloc[:, 9].astype(str).str.split('.').str[1].astype(str).str.pad(2, fillchar='0', side="right")  ## df['CONTRIB']
    df.iloc[:, 13] = df.iloc[:, 13].astype(str).str.pad(4, fillchar='0', side="left")      # df['SUB PLAN NUMBER']
    df.iloc[:, 14] = df.iloc[:, 14].astype(str).apply(lambda x: x.replace(',,,,', ''))      #name
    df.iloc[:, 14] = df.iloc[:, 14].astype(str).apply(lambda x: x.replace(',,,,,', ''))     #name
    df.iloc[:, 14] = df.iloc[:, 14].astype(str).apply(lambda x: x.replace(',,,', ''))       #name
    df.iloc[:, 14] = df.iloc[:, 14].astype(str).apply(lambda x: x.replace(',,', ''))        #name
    df.iloc[:, 25] = df.iloc[:, 25].astype(str).str.pad(2, fillchar='0')                    # df['EMPLOYEE STATUS']
    df.iloc[:, 30] = df.iloc[:, 30].astype(str).apply(lambda x: x.replace('NaN', ''))         # df['FILLER5']
    df.iloc[:, 30] = df.iloc[:, 30].fillna('')                                                # df['FILLER5']
    df = df.fillna('')
    df = df.applymap(lambda x: str(x).strip())

    ######## Complete the required padding as by layout ########
    df.iloc[:, 0] = df.iloc[:, 0].astype(str).str.pad(3, fillchar=' ', side="right")  # df['TRA']
    df.iloc[:, 1] = df.iloc[:, 1].astype(str).str.pad(2, fillchar=' ', side="right")  # df['FI']
    df.iloc[:, 2] = df.iloc[:, 2].astype(str).str.pad(6, fillchar=' ', side="right")  # df['PLAN N']
    df.iloc[:, 3] = df.iloc[:, 3].astype(str).str.pad(3, fillchar=' ', side="right")  # df['FIL']
    df.iloc[:, 4] = df.iloc[:, 4].astype(str).str.pad(9, fillchar=' ', side="right")  # df['PARTICIPA']
    df.iloc[:, 5] = df.iloc[:, 5].astype(str).str.pad(11, fillchar=' ', side="right")  # df['FILLER     ']
    df.iloc[:, 6] = df.iloc[:, 6].astype(str).str.pad(1, fillchar=' ', side="right")  # df['F']
    df.iloc[:, 7] = df.iloc[:, 7].astype(str).str.pad(2, fillchar=' ', side="right")  # df['IN']
    df.iloc[:, 8] = df.iloc[:, 8].astype(str).str.pad(1, fillchar=' ', side="right")  # df['S']
    df.iloc[:, 9] = df.iloc[:, 9].astype(str).str.pad(9, fillchar=' ', side="right")  # df['CONTRIB']
    df.iloc[:, 10] = df.iloc[:, 10].astype(str).str.pad(60, fillchar=' ', side="right")  # FILLER2
    df.iloc[:, 11] = df.iloc[:, 11].astype(str).str.pad(8, fillchar=' ', side="right")  # df['PAY PERIOD END DATE']
    df.iloc[:, 12] = df.iloc[:, 12].astype(str).str.pad(1, fillchar=' ', side="right")  # I
    df.iloc[:, 13] = df.iloc[:, 13].astype(str).str.pad(4, fillchar=' ', side="right")  # df['SUB PLAN NUMBER']
    df.iloc[:, 14] = df.iloc[:, 14].astype(str).str.pad(30, fillchar=' ', side="right")  # NAME
    df.iloc[:, 15] = df.iloc[:, 15].astype(str).str.pad(30, fillchar=' ', side="right")  # ADDRESS 1
    df.iloc[:, 16] = df.iloc[:, 16].astype(str).str.pad(30, fillchar=' ', side="right")  # ADDRESS 2
    df.iloc[:, 17] = df.iloc[:, 17].astype(str).str.pad(18, fillchar=' ', side="right")  # df['CITY              ']
    df.iloc[:, 18] = df.iloc[:, 18].astype(str).str.pad(2, fillchar=' ', side="right")  # df['ST']
    df.iloc[:, 19] = df.iloc[:, 19].astype(str).str.pad(9, fillchar=' ', side="right")  # df['ZIP C']
    # df['ZIP C'].astype(str).str.pad(10,fillchar='0')
    df.iloc[:, 21] = df.iloc[:, 21].astype(str).str.pad(8, fillchar=' ', side="right")  # df['DATE OF BIRTH']
    df.iloc[:, 22] = df.iloc[:, 22].astype(str).str.pad(16, fillchar=' ', side="right")  # FILLER3
    # df['FILLER2          '] = df['FILLER2          '].astype(str).str.pad(16,fillchar=' ')
    df.iloc[:, 23] = df.iloc[:, 23].astype(str).str.pad(1, fillchar=' ', side="right")  # df['MARITAL STATUS']
    df.iloc[:, 24] = df.iloc[:, 24].astype(str).str.pad(1, fillchar=' ', side="right")  # df['GENDER CODE']
    df.iloc[:, 25] = df.iloc[:, 25].astype(str).str.pad(2, fillchar=' ', side="right")  # df['EMPLOYEE STATUS']
    df.iloc[:, 26] = df.iloc[:, 26].astype(str).str.pad(8, fillchar=' ', side="right")  # df['EMPLOYEE']
    df.iloc[:, 27] = df.iloc[:, 27].astype(str).str.pad(1, fillchar=' ', side="right")  # df['P']
    df.iloc[:, 28] = df.iloc[:, 28].astype(str).str.pad(75, fillchar=' ',
                                                        side="right")  # # df['FILLER4']
    df.iloc[:, 29] = df.iloc[:, 29].astype(str).str.pad(8, fillchar=' ', side="right")  # df['CHECK DATE']
    df.iloc[:, 30] = df.iloc[:, 30].astype(str).str.pad(380, fillchar=' ', side="right")  # FILLER5

    
    # contrib_sum = df.iloc[:, 9].sum()
    # contrib_sum = [sum(float(x) for x in string.split()) for string in df.iloc[:, 9]]
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    df_contrib = df.iloc[:, 9]
    print("df iloc contrib columnm is: ")
    # print(df.iloc[:, 9])
    df_contrib = df_contrib.apply(pd.to_numeric)
    # print(df_contrib)
    contrib_sum = df_contrib.sum()
    
    print("Contribution sum is: ")
    print(contrib_sum)
    ######## Write file to a text file & Replace all nan value and separator (|) in the file ########
    # Write file to a text file
    output_file = str(fileName.get()).replace(".csv", "") + '.txt'
    print(output_file)
    df.to_csv(output_file, header=None, index=None, sep='|')

    # read input file
    fin = open(output_file, "rt")
    # read file contents to string
    data = fin.read()
    # replace all occurrences of the required string
    data = data.replace('nan', '   ')
    data = data.replace('|', '')
    # close the input file
    fin.close()
    # open the input file in write mode
    fin = open(output_file, "wt")
    # overrite the input file with the resulting data
    fin.write(data)
    # close the file
    fin.close()

    ################## Header Trailer add #################

    """ Insert given string as a new line at the beginning of a file """
    # define name of temporary dummy file
    dummy_file = output_file + '.bak'

    print("Dummy file is:")
    print(dummy_file)

    if os.path.exists(dummy_file):
        os.remove(dummy_file)

    # if os.path.exists(str(output_file)[:-3] + "txt"):
    #     os.remove(str(output_file)[:-3] + "txt")

    # open original file in read mode and dummy file in write mode
    with open(output_file, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Create Header for the file
        todaydate = datetime.today().strftime('%Y%m%d')
        todaydatetime = strftime("%Y%m%d%H%M%S", gmtime())
        header = '001COMBINED  300410    ' + todaydatetime + 'PV01                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          '

        # Write given line to the dummy file
        write_obj.write(header + '\n')
        # Read lines from original file one by one and append them to the dummy file
        i = 0
        for line in read_obj:
            write_obj.write(line)
            i = i + 1

        # Create trailer for the file
        str_len = str(i)
        if len(str_len) == 1: 
            str_len  = '00000000' + str_len 
        elif len(str_len) == 2: 
            str_len  = '0000000' + str_len 
        elif len(str_len) == 3: 
            str_len  = '000000' + str_len 
        elif len(str_len) == 4: 
            str_len  = '00000' + str_len         
        elif len(str_len) == 5: 
            str_len  = '0000' + str_len   
        elif len(str_len) == 6: 
            str_len  = '000' + str_len 
        elif len(str_len) == 7: 
            str_len  = '00' + str_len 
        elif len(str_len) == 8: 
            str_len  = '0' + str_len   

        contrib_sum = str(contrib_sum)
        if len(contrib_sum) == 1: 
            contrib_sum  = '000000000' + contrib_sum 
        elif len(contrib_sum) == 2: 
            contrib_sum  = '00000000' + contrib_sum  
        elif len(contrib_sum) == 3: 
            contrib_sum  = '0000000' + contrib_sum 
        elif len(contrib_sum) == 4: 
            contrib_sum  = '000000' + contrib_sum     
        elif len(contrib_sum) == 5: 
            contrib_sum  = '00000' + contrib_sum  
        elif len(contrib_sum) == 6: 
            contrib_sum  = '0000' + contrib_sum  
        elif len(contrib_sum) == 7: 
            contrib_sum  = '000' + contrib_sum  
        elif len(contrib_sum) == 8: 
            contrib_sum  = '00' + contrib_sum  
        elif len(contrib_sum) == 9: 
            contrib_sum  = '0' + contrib_sum                  

        trailer = '999COMBINED  300410    ' + todaydatetime + str_len + ' ' + contrib_sum + ' ' + '00000000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              '
        # Write given line to the dummy file
        write_obj.write(trailer)

        # remove original file
    #     os.remove(file_name)

    output_path = "\\".join(str(output_file).split("\\")[:-1])
    print("output_path is: " + output_path)

    final_output_file = "C300410A.txt"
    final_output_file_with_path = output_path + '\\' + final_output_file
    print("final_output_file_with_path is: " + final_output_file_with_path)

    if os.path.exists(final_output_file_with_path):
        os.remove(final_output_file_with_path)

    # Rename dummy file as the original file
    os.rename(dummy_file, final_output_file_with_path)


    ##################Header Trailer add close #################


    done = time.time()
    elapsed = done - start
    label2.configure(text='File. created. Time Taken (millisecond): ' + str(elapsed))
    print('File  ' + fileName.get() + '. created. Time Taken: ' + str(elapsed))
    print('------------------------------')

CreateButton = tk.Button(text="      Create File     ", command=CreateFile, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(300, 280, window=CreateButton)
def exitApplication():
    MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',icon='warning')
    if MsgBox == 'yes':
        root.destroy()

exitButton = tk.Button(root, text='       Exit Application     ', command=exitApplication, bg='brown', fg='white',font=('helvetica', 12, 'bold'))
canvas1.create_window(290, 340, window=exitButton)



root.mainloop()