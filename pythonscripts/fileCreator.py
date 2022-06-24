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

start = time.time()

root = tk.Tk()
root.title('HRA\'s File Link Creator for 3M/UB04/EOB')
root.resizable(0, 0)
# root.iconbitmap('icon.ico')

canvas1 = tk.Canvas(root, width=650, height=600, bg='lightsteelblue2', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='HRA\'s File Link Creator for 3M/UB04/EOB', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(300, 40, window=label1)

labelCreator = tk.Label(root, text='Created By: Rajender Kumar ', bg='lightsteelblue2')
labelCreator.config(font=('helvetica', 8))
canvas1.create_window(350, 80, window=labelCreator)

label2 = tk.Label(root, text=' ', bg='lightsteelblue2')
label2.config(font=('helvetica', 12))
canvas1.create_window(250, 440, window=label2)


label3 = tk.Label(root, text='Copyright © Healthcare Retroactive Audits ', bg='lightsteelblue2')
label3.config(font=('helvetica', 12))
canvas1.create_window(250, 500, window=label3)

labelPath = tk.Label(root, text='File Path: ', width = 250, bg='lightsteelblue2')
labelPath.config(font=('helvetica', 12))
canvas1.create_window(150, 120, window=labelPath)

filePath = tk.StringVar()
textboxPath = tk.Entry (root, textvariable = filePath)
canvas1.create_window(400, 120, width = 250, window=textboxPath)

labelName = tk.Label(root, text='Table Name: ', width = 250, bg='lightsteelblue2')
labelName.config(font=('helvetica', 12))
canvas1.create_window(150, 160, window=labelName)

tblName = tk.StringVar(root)
textboxName = tk.Entry(root, textvariable = tblName)
canvas1.create_window(400, 160, width=250, window=textboxName)


labelType = tk.Label(root, text='File Type: ', width = 250, bg='lightsteelblue2')
labelType.config(font=('helvetica', 12))
canvas1.create_window(150, 200, window=labelType)

# fileType = tk.StringVar(root, value=".xls")
# textboxType = tk.OptionMenu(root, ".xls", ".html")
# canvas1.create_window(400, 200, width=250, window=textboxType)


# Create a Tkinter variable
tkvar = tk.StringVar(root)

# Dictionary with options
choices = { '.xlsx','.html', '.csv', '.xls', '.sql'}
tkvar.set('.csv') # set the default option

popupMenu = tk.OptionMenu(root, tkvar, *choices)
canvas1.create_window(400, 200, width=250, window=popupMenu)

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
    #fileName = fileName + ".xls"

    # # Workbook is created
    # wb = Workbook()
    #
    # # add_sheet is used to create sheet.
    # a = wb.add_sheet('Sheet 1')

    # Creating .xls file
    if tkvar.get() == ".xls":
        a = open('%s.xls' % fileName.get(), "w")
        print('file opened')
        # a.write("File_Location\n")
        n=0
        for path, subdirs, files in os.walk('%s' %filePath.get()):
            for filename in files:
                n = n + 1
                f = os.path.join(path, filename)
                link = "=HYPERLINK(\"" + str(f) + "\")"
                # link = "<a href=\"file:///" + str(f) + "\">" + filename + "</a><br> "

                # a.write(link + os.linesep)
                a.write(link + '\n')
        print('write complete and ' + str(n) + " files link are created")

    # Creating HTML file
    elif tkvar.get() == ".html":
        a = open('%s.HTML' % fileName.get(), "w")
        print('file opened')
        # a.write("File_Location\n")
        n = 0
        for path, subdirs, files in os.walk('%s' % filePath.get()):
            for filename in files:
                n = n + 1
                f = os.path.join(path, filename)
                # link = "=HYPERLINK(\"" + str(f) + "\")"
                link = "<a href=\"file:///" + str(f) + "\" target=\"_blank\">" + filename + "</a><br> "

                # a.write(link + os.linesep)
                a.write(link + '\n')
        print('write complete and ' + str(n) + " files link are created")

    # Creating csv file
    elif tkvar.get() == ".csv":
        a = open('%s.csv' % fileName.get(), "w")
        print('file opened')
        # a.write("File_Location\n")
        n = 0
        for path, subdirs, files in os.walk('%s' %filePath.get()):
            for filename in files:
                n = n + 1
                f = os.path.join(path, filename)
                link = "=HYPERLINK(\"" + str(f) + "\")"
                # link = "<a href=\"file:///" + str(f) + "\">" + filename + "</a><br> "

                # a.write(link + os.linesep)
                a.write(link + '\n')
        print('write complete and ' + str(n) + " files link are created")

    # Creating Excel (XLS) file, this wil create xls file but it is not showing formula properly, so i am not using it.
    elif tkvar.get() == ".xlsxt":
        # Workbook is created
        wb = Workbook()

        # add_sheet is used to create sheet.
        a = wb.add_sheet('Sheet 1')
        # a = open('%s.csv' % fileName.get(), "w")
        print('file opened')
        # a.write("File_Location\n")
        n = 0
        for path, subdirs, files in os.walk('%s' %filePath.get()):
            for filename in files:
                n =n+1
                f = os.path.join(path, filename)
                link = "=HYPERLINK(\"" + str(f) + "\")"
                # link = "<a href=\"file:///" + str(f) + "\">" + filename + "</a><br> "

                # a.write(link + os.linesep)
                a.write(n, 0, link)
        wb.save('%s.xls' % fileName.get())
        print('write complete and ' + str(n) + " files link are created")

    # Creating Excel (XLSX) file
    elif tkvar.get() == ".xlsx":
        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook('%s.xlsx' % fileName.get())
        a = workbook.add_worksheet()

        # a = open('%s.csv' % fileName.get(), "w")
        print('file opened')
        # a.write("File_Location\n")
        n = 0
        for path, subdirs, files in os.walk('%s' %filePath.get()):
            for filename in files:
                n =n+1
                f = os.path.join(path, filename)
                link = "=HYPERLINK(\"" + str(f) + "\")"
                # link = "<a href=\"file:///" + str(f) + "\">" + filename + "</a><br> "

                # a.write(link + os.linesep)
                a.write(n, 0, link)
        workbook.close()
        # wb.save('%s.xls' % fileName.get())
        print('write complete and ' + str(n) + " files link are created")

    # Creating Excel (XLSX) file
    elif tkvar.get() == ".sql":

        cnxn = pyodbc.connect(r'Driver=SQL Server;Server=PP-DB02\SQL01;Database=PDF_LINK;Trusted_Connection=yes;')
        cursor = cnxn.cursor()
        print('file opened')
        # a.write("File_Location\n")
        n = 0
        for path, subdirs, files in os.walk('%s' % filePath.get()):
            for filename in files:
                n = n + 1
                f = os.path.join(path, filename)
                link = str(f)
                strfilename = str(filename)

                sql = "INSERT INTO [PDF_LINK].[dbo]." + tblName.get() +  " ([link], [EncounterID] ) VALUES (  ?, ? )"
                # print(sql)
                parameter =  (link, strfilename)
                # sql = "INSERT INTO [PDF_LINK].[dbo].[eob] ([link], [EncounterID] ) VALUES ", link, strfilename
                # print(sql)
                # cursor.execute("Select * from [PDF_LINK].[dbo].[eob]")
                if (tblName.get() == 'eob' or tblName.get() == 'ub04' or tblName.get() == 'report3m'):
                    cursor.execute(sql,parameter)
                    cnxn.commit()
                else:
                    messagebox.showerror("Wrong Table Name", "Table name can be only ub04, eob or report3m. Please enter again!")
        cnxn.close()
        print('write complete and ' + str(n) + " files link are created")

    done = time.time()
    elapsed = done - start
    label2.configure(text='File  ' + fileName.get() + '. created. Time Taken: ' + str(elapsed))
    print('File  ' + fileName.get() + '. created. Time Taken: ' + str(elapsed))
    print('------------------------------')

CreateButton = tk.Button(text="      Create File     ", command=CreateFile, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(300, 280, window=CreateButton)

# def getPath():
#     global read_file
#
#     import_file_path = filedialog.askopenfilename()
#     read_file = pd.read_excel(import_file_path)
#
#     labelPath = tk.Label(root, text='File Path: ', bg='lightsteelblue2')
#     labelPath.config(font=('helvetica', 12))
#     canvas1.create_window(150, 130, window=labelPath)
#
#     textboxPath = tk.Entry (root)
#     canvas1.create_window(300, 130, width = 250, window=textboxPath)
#
#     labelName = tk.Label(root, text='File Name: ', bg='lightsteelblue2')
#     labelName.config(font=('helvetica', 12))
#     canvas1.create_window(150, 180, window=labelName)
#
#     textboxName = tk.Entry(root)
#     canvas1.create_window(300, 180, width=250, window=textboxName)
#
# browseButton_Excel = tk.Button(text="      Import Excel File     ", command=getPath, bg='green', fg='white',
#                                font=('helvetica', 12, 'bold'))
# canvas1.create_window(550, 130, window=browseButton_Excel)
#
#
# def convertToCSV():
#     global read_file
#
#     export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
#     read_file.to_csv(export_file_path, index=None, header=True)
#
#
# saveAsButton_CSV = tk.Button(text='Convert Excel to CSV', command=convertToCSV, bg='green', fg='white',
#                              font=('helvetica', 12, 'bold'))
# canvas1.create_window(150, 180, window=saveAsButton_CSV)


def exitApplication():
    MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                       icon='warning')
    if MsgBox == 'yes':
        root.destroy()


exitButton = tk.Button(root, text='       Exit Application     ', command=exitApplication, bg='brown', fg='white',
                       font=('helvetica', 12, 'bold'))
canvas1.create_window(290, 340, window=exitButton)

# load = Image.open("logo3.png")
# new_image = Image.new("RGBA", load.size, "cyan") # Create a white rgba background (188,210,238)
# new_image.paste(load, (0, 0), load)              # Paste the image on the background. Go to the links given below for details.
# load1 = new_image.resize((100, 100))
# render = ImageTk.PhotoImage(load1)
# img = tk.Label(image=render, width = 100, height = 100)
# img.image = render
# img.place(x=550, y=500)

root.mainloop()