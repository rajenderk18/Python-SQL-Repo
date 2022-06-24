import os
import stat
import time
import datetime


def main():
    filePath = 'U:/teststring/B79000/statistics.txt'

    # print("**** Get last modification time using os.stat() ****")
    #
    # fileStatsObj = os.stat(filePath)
    #
    # modificationTime = time.ctime(fileStatsObj[stat.ST_MTIME])
    #
    # print("Last Modified Time : ", modificationTime)

    # print("**** Get last modification time using os.path.getmtime() & time.localtime() ****")

    # Get file's Last modification time stamp only in terms of seconds since epoch
    # modTimesinceEpoc = os.path.getmtime(filePath)

    # # Convert seconds since epoch to readable timestamp
    # modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
    #
    # print("Last Modified Time : ", modificationTime)

    # Convert seconds since epoch to Date only
    modificationTime = time.strftime('%m/%d/%Y', time.localtime(os.path.getmtime(filePath)))

    print("Last Modified Time : ", modificationTime)

    # print("**** Get last modification time using os.path.getmtime() & datetime.fromtimestamp() ****")
    #
    # modTimesinceEpoc = os.path.getmtime(filePath)
    #
    # modificationTime = datetime.datetime.fromtimestamp(modTimesinceEpoc).strftime('%Y-%m-%d %H:%M:%S')
    #
    # print("Last Modified Time : ", modificationTime)
    #
    # modificationTime = datetime.datetime.fromtimestamp(modTimesinceEpoc).strftime('%c')
    #
    # print("Last Modified Time : ", modificationTime)
    # print("**** Get last modification time in UTC Timezone ****")
    # modTimesinceEpoc = os.path.getmtime(filePath)
    #
    # modificationTime = datetime.datetime.utcfromtimestamp(modTimesinceEpoc).strftime('%Y-%m-%d %H:%M:%S')
    #
    # print("Last Modified Time : ", modificationTime, ' UTC')


if __name__ == '__main__':
    main()
