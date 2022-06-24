import glob

read_files = glob.glob("N:\\Conversion Files\\1240 - Sheet Metal Local 20\\A. Data Conversion\\Original Data\\Zenith\\Additional Files\\*.txt")

with open("N:\\Conversion Files\\1240 - Sheet Metal Local 20\\A. Data Conversion\\Original Data\\Zenith\\Additional Files\\AdditionalCombinedClaimFile.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())