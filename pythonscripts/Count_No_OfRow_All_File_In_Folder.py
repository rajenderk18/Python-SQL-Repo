# import os
# path = 'U:\\Count_File\\test'
# for filename in os.listdir(path):
#     with open(filename, 'r', encoding="latin-1") as fileObj:
#         # -1 to exclude the header
#         print("Rows Counted {} in the csv {}:".format(len(fileObj.readlines()) - 1, filename))


import glob
import pandas as pd

files = glob.glob('U:/1280/010422/GV00_Eldorado_20220329/*.txt')

d = {f: sum(1 for line in open(f, encoding="latin-1")) for f in files}

print (pd.Series(d))

# print (pd.Series(d).rename('rows').rename_axis('filename').reset_index())