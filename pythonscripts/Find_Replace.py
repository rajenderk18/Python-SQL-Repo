import os, fnmatch
def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        # print("Parameter value are: " + directory)
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            print("File opened is: " + filepath)
            with open(filepath, encoding="utf8", errors='ignore') as f:
                s = f.read()
                print("File writing to: " + filepath)
            s = s.replace(find, replace)
            with open(filepath, "w", encoding="utf8", errors='ignore') as f:
                f.write(s)

findReplace('U:\\1280\\BasysData_20200728', '|', ',', '*.csv')
# findReplace('U:\Test', '"', '', '*y.csv')