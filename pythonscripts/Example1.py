from datetime import datetime
myFile = open('C:\Raj\General_Python_Script\\append.txt', 'a')
myFile.write('\nAccessed on ' + str(datetime.now()))