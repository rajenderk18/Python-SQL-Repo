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
import webbrowser
import fnmatch
import pyodbc
import subprocess

start = time.time()
cnxn = pyodbc.connect(r'Driver=SQL Server;Server=PP-DB02\SQL01;Database=PDF_LINK;Trusted_Connection=yes;')
cursor = cnxn.cursor()

root = tk.Tk()
root.title('UB04/EOB/3M Report Finder')
root.resizable(0, 0)
# root.iconbitmap('icon.ico')

canvas1 = tk.Canvas(root, width=650, height=850, bg='lightsteelblue2', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='UB04/EOB/3M Report Finder', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(300, 40, window=label1)

labelCreator = tk.Label(root, text='Created By: Rajender Kumar ', bg='lightsteelblue2')
labelCreator.config(font=('helvetica', 8))
canvas1.create_window(350, 80, window=labelCreator)

# #
# label2 = tk.Label(root, text='Created By: Rajender Kumar ', bg='lightsteelblue2')
# label2.config(font=('helvetica', 12))
# canvas1.create_window(250, 440, window=label2)
# #
#
# label3 = tk.Label(root, text='Copyright © Healthcare Retroactive Audits ', bg='lightsteelblue2')
# label3.config(font=('helvetica', 12))
# canvas1.create_window(250, 500, window=label3)


labelNeeded = tk.Label(root, text='File Neded: ', width = 250, bg='lightsteelblue2')
labelNeeded.config(font=('helvetica', 12))
canvas1.create_window(150, 120, window=labelNeeded)

# fileType = tk.StringVar(root, value=".xls")
# textboxType = tk.OptionMenu(root, ".xls", ".html")
# canvas1.create_window(400, 200, width=250, window=textboxType)


# Create a Tkinter variable
tkneeded = tk.StringVar(root)

# Dictionary with options
choicesNeeded = { 'EOB','UB04', 'report3M'}
tkneeded.set('UB04') # set the default option

popupMenuNeeded = tk.OptionMenu(root, tkneeded, *choicesNeeded)
canvas1.create_window(400, 120, width=250, window=popupMenuNeeded)

# on change dropdown value
def change_dropdown(*args):
    print( tkneeded.get() )

# link function to change dropdown
tkneeded.trace('w', change_dropdown)

labelEncID = tk.Label(root, text='Enter EncounterID: ', width = 250, bg='lightsteelblue2')
labelEncID.config(font=('helvetica', 12))
canvas1.create_window(150, 160, window=labelEncID)

fileEncID = tk.StringVar()
textboxEncID = tk.Entry (root, textvariable = fileEncID)
canvas1.create_window(400, 160, width = 250, window=textboxEncID)


labelType = tk.Label(root, text='Hospital Name: ', width = 250, bg='lightsteelblue2')
labelType.config(font=('helvetica', 12))
canvas1.create_window(150, 200, window=labelType)

# fileType = tk.StringVar(root, value=".xls")
# textboxType = tk.OptionMenu(root, ".xls", ".html")
# canvas1.create_window(400, 200, width=250, window=textboxType)


# Create a Tkinter variable
tkvar = tk.StringVar(root)

# Dictionary with options
choices = {'MSN','SHC', 'HVH', 'LAW', 'COL'}
tkvar.set('For Future Use') # set the default option

popupMenu = tk.OptionMenu(root, tkvar, *choices)
canvas1.create_window(400, 200, width=250, window=popupMenu)

# on change dropdown value
def change_dropdown_hospital(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown_hospital)


matchList = Listbox(root,
                  bg = "white",
                  height = "18",
                  activestyle = 'dotbox',
                  font = "Helvetica",
                  fg = "Blue")
canvas1.create_window(290, 520, width = 550, window=matchList)

# matchList.pack()
# match = []

def CreateFile():
    global match
    global start
    global fileName
    fileName = fileEncID
    match = []
    matchList.delete('0', 'end')
    # label2.configure(text= 'I am creating ' + fileName.get() + '. Please wait...')

    # if tkneeded.get() == "EOB":
    print("Selected File Type: " + tkneeded.get())
    sql = "SELECT [link] FROM [PDF_LINK].[dbo]." + tkneeded.get() + " where [EncounterID] like ?"
    # print(sql)
    # print('file opened')
    # a.write("File_Location\n")
    fileEncID1 = fileEncID.get() + "%"
    parameter = (fileEncID1)
    cursor.execute(sql, parameter)
    for row in cursor:
        match.append(row)

    matchList.insert(0, *match)

    done = time.time()
    elapsed = done - start
    print(elapsed)

def OpenFile():
    selection = matchList.curselection()
    print([matchList.get(i) for i in selection])
    str = ''
    for i in selection:
        str = str + matchList.get(i)
        # webbrowser.open_new(str)
        # print("Selected file is: " + str)
        clean_str = str.replace("('", '"')
        clean_str1 = clean_str.replace("', )", '"')
        # print("Selected Clean file is: " + clean_str1)
        subprocess.Popen(clean_str1, shell=True)
        # matchList.delete('0', 'end')

def exitApplication():
    MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if MsgBox == 'yes':
        root.destroy()

CreateButton = tk.Button(text="      Search File     ", command=CreateFile, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(300, 280, window=CreateButton)

OpenButton = tk.Button(text="      Open File     ", command=OpenFile, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(220, 780, window=OpenButton)

exitButton = tk.Button(root, text='       Exit Application     ', command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(420, 780, window=exitButton)

root.mainloop()