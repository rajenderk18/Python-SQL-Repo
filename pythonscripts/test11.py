data = """3526 HIGH ST, SACRAMENTO, 95838, CA, 2, 1, 836, Residential, Wed May 21 00:00:00 EDT 2008, 59222, 38.631913, -121.434879
51 OMAHA CT, SACRAMENTO, 95823, CA, 3, 1, 1167, Residential, Wed May 21 00:00:00 EDT 2008, 68212, 38.478902, -121.431028
2796 BRANCH ST, SACRAMENTO, 95815, CA, 2, 1, 796, Residential, Wed May 21 00:00:00 EDT 2008, 68880, 38.618305, -121.443839
2805 JANETTE WAY, SACRAMENTO, 95815, CA, 2, 1, 852, Residential, Wed May 21 00:00:00 EDT 2008, 69307, 38.616835, -121.439146
6001 MCMAHON DR, SACRAMENTO, 95824, CA, 2, 1, 797, Residential, Wed May 21 00:00:00 EDT 2008, 81900, 38.51947, -121.435768"""

# max-width per column, column == key, width == value
w = {}
lines = data.splitlines()
for line in lines:
    for col_nr, col in enumerate(line.strip().split(",")):
        w[col_nr] = max( w.get(col_nr,0), len(col))

print(w)
# w == {0: 16, 1: 11,  2:  6, 3: 3,   4:  2,   5: 2,
#       6:  5, 7: 12,  8: 29, 9: 6,  10: 10,  11: 12}

# write file
with open("file.txt","w") as f:
    for line in lines:
        for col_nr, col in enumerate(line.strip().split(",")):
            # the :<{w[col_nr]+5}} - part is left-adjusting to certain width
            f.write(f"{col:<{w[col_nr]+5}}") # 5 additional spaces
        f.write("\n")

with open("file.txt","r") as f:
    print(f.read())