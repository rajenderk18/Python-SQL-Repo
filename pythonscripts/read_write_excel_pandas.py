import pandas as pd

df = pd.read_excel('H:\HRA_Codes\General_Python_Script\General_Python_Script\\22.xlsx')

# print whole sheet data
# print(df.head())

# Sort the value according to file name used
df = df.sort_values('col 3', ascending = True)
print(df)

# Get unique name of files in a list
names=df['col 3'].unique().tolist()

# Create multiple files using for loop
for x in names:
  print(x)
  df[df['col 3'] == x].to_excel(str(x) + '.xlsx')


