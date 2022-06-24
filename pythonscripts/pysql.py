import pyodbc

cnxn = pyodbc.connect(r'Driver=SQL Server;Server=PP-DB02\SQL01;Database=PDF_LINK;Trusted_Connection=yes;')
cursor = cnxn.cursor()
sql = "INSERT INTO [PDF_LINK].[dbo].[eob] ([link], [EncounterID] ) VALUES (  ?, ? )"
parameter = ('21', '21')
cursor.execute(sql, parameter)
cnxn.commit()
# cursor.execute(sql, ('32', '2'))
cursor.execute(sql, ('42', '2'))
# cursor.execute("SELECT * FROM eob")
# while 1:
#     row = cursor.fetchone()
#     if not row:
#         break
#     print(row.link)
cnxn.close()