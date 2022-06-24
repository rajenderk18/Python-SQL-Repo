
import webbrowser
import os, fnmatch
def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    print(result)
    return result

# result1 =[]
result1 = find('39c55*', 'S:/Claims EOB/Testfolder')

# print(resut1[0])
if result1:
    webbrowser.open_new(result1[0])
else:
    print("There is no Such file with the Encounter ID you entered")