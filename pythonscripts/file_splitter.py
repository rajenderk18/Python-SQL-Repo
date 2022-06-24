# csvfile = open('U:\\Load 1250csv\\DB_PensionHistoryDetail.CSV', 'r').readlines()
csvfile = open('U:\\Load 1250csv\\DB_PensionHistoryDetail.CSV', 'r').readlines()

filename = 1
for i in range(len(csvfile)):
    if i % 1000000 == 0:
        open(str(filename) + '.csv', 'w+').writelines(csvfile[i:i+1000000])
        filename += 1