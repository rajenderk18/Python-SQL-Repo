#! python3


# Import os module
import os
import time

def main():
    # Ask the user to enter string to search
    search_path = input("Enter directory path to search : ")
    # file_type = input("File Type : ")
    search_str = input("Enter the search string : ")
    modification_date = input("Enter the file modification date : ")
    find_error(search_path, search_str, modification_date)


def find_error(search_path, search_str, modification_date):
    # Append a directory separator if not already present
    if not (search_path.endswith("/") or search_path.endswith("\\")):
        search_path = search_path + "\\"

    # If path does not exist, set search path to current directory
    if not os.path.exists(search_path):
        search_path = "."

    # Repeat for each file in the directory
    # for fname in os.listdir(path=search_path):
    for root, dirs, files in os.walk(search_path):
            for file in files:

                # Apply file type filter
                if file.endswith("statistics.txt") or file.endswith("properties") or file.endswith("log") or file.endswith("zip") or file.endswith("xls"):
                # if str(file).find("statistics") != -1:
                #     print(file)
                    pass
                else:
                    pass
                    filePath = os.path.join(root, file)
                    # print(filePath)

                    modificationTime = time.strftime('%m/%d/%Y', time.localtime(os.path.getmtime(filePath)))
                    # print("Last Modified Time : ", modificationTime)

                    if modification_date == modificationTime:

                        print(filePath)
                        print("Last Modified Time : ", modificationTime)
                        # Open file for reading
                        # with open(filePath, "r") as fo:
                        #     newline_breaks = ""
                        #     for line1 in fo:
                        #         stripped_line = line1.replace('~', "\n")
                        #         newline_breaks += stripped_line
                        #     # print(newline_breaks)

                        findReplace(filePath, '~', '\n')
                        fo = open(filePath)

                        # Read the first line from the file
                        line = fo.readline()

                        # Initialize counter for line number
                        line_no = 1

                        # Loop until EOF
                        while line != '':
                            # Search for string in line
                            index = line.find(search_str)
                            if (index != -1):
                                print(file, "[", line_no, ",", index, "] ", line, sep="")

                            # Read next line
                            line = fo.readline()

                            # Increment line counter
                            line_no += 1
                        # Close the files
                        fo.close()
                        findReplace(filePath, '\n', '~')


def findReplace(target_file, find, replace):
    # Read in the file
    with open(target_file, 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(find, replace)

    # Write the file out again
    with open(target_file, 'w') as file:
        file.write(filedata)



if __name__ == '__main__':
    main()
