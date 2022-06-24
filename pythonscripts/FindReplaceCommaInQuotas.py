import os, fnmatch
import re

def findReplace(directory, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        print("Parameter value are: " + directory)
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            print("File opened is: " + filepath)
            with open(filepath) as f:
                s = f.read()
                print("File opened is: " + filepath)
            # s = s.replace(find, replace)
            s = re.sub(r'"[^"]+"', lambda x: x.group().replace(',', ''), s)
            with open(filepath, "w") as f:
                f.write(s)

findReplace("U:\Load 1250csv\\test", "*.csv")