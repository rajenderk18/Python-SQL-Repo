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

start = time.time()

root = tk.Tk()
root.title('Header Footer Adder')
root.resizable(0, 0)
# root.iconbitmap('icon.ico')

canvas1 = tk.Canvas(root, width=650, height=600, bg='lightsteelblue2', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Header Footer Adder', bg='lightsteelblue2')
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

labelPath = tk.Label(root, text='File Path & Name: ', width = 250, bg='lightsteelblue2')
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
    label2.configure(text='I am creating ' + fileName.get() + '. Please wait...')
    print("file path is: " + str(fileName.get()))

    """ Insert given string as a new line at the beginning of a file """
    # define name of temporary dummy file
    dummy_file = fileName.get() + '.bak'

    if os.path.exists(dummy_file):
        os.remove(dummy_file)

    if os.path.exists(str(fileName.get())[:-3] + "csv"):
        os.remove(str(fileName.get())[:-3] + "csv")

    # open original file in read mode and dummy file in write mode
    with open(fileName.get(), 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Create Header for the file
        todaydate = datetime.today().strftime('%Y%m%d')
        header = '"H"|"' + todaydate + '"|"F"'

        # Write given line to the dummy file
        write_obj.write(header + '\n')
        # Read lines from original file one by one and append them to the dummy file
        i = 0
        for line in read_obj:
            write_obj.write(line)
            i = i + 1

        # Create trailer for the file
        trailer = '"T"|"' + str(i) + '"'
        # Write given line to the dummy file
        write_obj.write(trailer)

        # remove original file
    #     os.remove(file_name)
    # Rename dummy file as the original file
    # os.rename(dummy_file, str(fileName.get())[:-3] + "csv")

    output_file = str(fileName.get()).replace(".csv", "") + '.txt'
    print(output_file)

    output_path = "\\".join(str(output_file).split("\\")[:-1])
    print("output_path is: " + output_path)

    final_output_file = "NEBA-UA123_Eligibility_" + str(todaydate) + ".csv"
    final_output_file_with_path = output_path + '\\' + final_output_file
    print("final_output_file_with_path is: " + final_output_file_with_path)

    if os.path.exists(final_output_file_with_path):
        os.remove(final_output_file_with_path)

    # Rename dummy file as the original file
    os.rename(dummy_file, final_output_file_with_path)




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