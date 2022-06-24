import tkinter as tk
# from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
# from PIL import Image, ImageTk
import os
import time
import shutil

start = time.time()

root = tk.Tk()
root.title('BASSAM\'s FILE MOVER & DATA VALIDATION')
root.resizable(0, 0)
# root.iconbitmap('icon.ico')

canvas1 = tk.Canvas(root, width=650, height=600, bg='lightsteelblue2', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='BASSAM\'s FILE MOVER & DATA VALIDATION', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(300, 60, window=label1)

label2 = tk.Label(root, text='Thank you for using me ', bg='lightsteelblue2')
label2.config(font=('helvetica', 12))
canvas1.create_window(250, 440, window=label2)


label3 = tk.Label(root, text='Copyright © Healthcare Retroactive Audits ', bg='lightsteelblue2')
label3.config(font=('helvetica', 12))
canvas1.create_window(250, 500, window=label3)

labelPath = tk.Label(root, text='Source Path: ', width = 250, bg='lightsteelblue2')
labelPath.config(font=('helvetica', 12))
canvas1.create_window(150, 130, window=labelPath)

srcPath = tk.StringVar()
textboxPath = tk.Entry (root, textvariable = srcPath)
canvas1.create_window(400, 130, width = 250, window=textboxPath)

labelName = tk.Label(root, text='Dst Path: ', width = 250, bg='lightsteelblue2')
labelName.config(font=('helvetica', 12))
canvas1.create_window(150, 170, window=labelName)

dstPath = tk.StringVar(root)
textboxName = tk.Entry(root, textvariable = dstPath)
canvas1.create_window(400, 170, width=250, window=textboxName)

labelName = tk.Label(root, text='fileName List: ', width = 250, bg='lightsteelblue2')
labelName.config(font=('helvetica', 12))
canvas1.create_window(150, 210, window=labelName)

fileName = tk.StringVar(root)
textboxName = tk.Entry(root, textvariable = fileName)
canvas1.create_window(400, 210, width=250, window=textboxName)

def CreateFile():
    global start, srcPath, dstPath, fileName

    print('src path is: ' + srcPath.get())
    print('dst path is: ' +dstPath.get())
    print('filename path is: ' +fileName.get())

    b1 = str(srcPath)
    print(type(b1))
    print(type(dstPath))
    print(type(fileName))

    count = 0

    try:
        with open(fileName.get()) as f:
            lines = f.read().splitlines()
        print(lines)

        for file_name in lines:
            try:
                shutil.move(os.path.join(srcPath.get(), file_name), os.path.join(dstPath.get(), file_name))
                count = count+1
                # label2.configure(text=str(count) + ' File moved.')
            except FileNotFoundError:
                print("file not available")

    except FileNotFoundError:
        print("Wrong file or file path")

    print('File moving complete')
    done = time.time()
    elapsed = done - start
    elapsed = round(elapsed, 2)
    label2.configure(text= str(count) + ' File moved. Time Taken: ' + str(elapsed))
    print(elapsed)

CreateButton = tk.Button(text="      Move Files     ", command=CreateFile, bg='green', fg='white', font=('helvetica', 12, 'bold'))
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