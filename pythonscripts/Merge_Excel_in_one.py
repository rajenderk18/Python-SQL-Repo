import os
import pandas as pd
cwd = os.path.abspath('S:\\Raj_Old_SDrive\\MSN_Excel_From_Hospital\\Charges\\')
files = os.listdir(cwd)
df = pd.DataFrame()
for file in files:
    if file.endswith('.xlsx'):
        df = df.append(pd.read_excel(file), ignore_index=True)
df.head()
df.to_excel('total_sales.xlsx')