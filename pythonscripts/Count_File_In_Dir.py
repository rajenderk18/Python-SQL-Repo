import os, os.path


dir = 'S:\\Claims EOB'
list = os.listdir(dir) # dir is your directory path
number_files = len(list)
# print (number_files)
print ('File in the directory including sub-directory: ' + str(number_files))
print (len([name for name in os.listdir('.') if os.path.isfile(name)]))

onlyfiles = next(os.walk(dir))[2] #dir is your directory path as string
number_files_Only = len(onlyfiles)
print ('File in the directory not including sub-directory: ' + str(number_files_Only))

path, dirs, files = next(os.walk(dir))
file_count = len(files)
print(file_count)

onlyfiles = next(os.walk(dir))[2] #dir is your directory path as string
print(len(onlyfiles))