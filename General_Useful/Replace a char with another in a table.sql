USE [1250]--your database name
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE dbo.replace_char 
@char_to_replace char(1), --character to be replaced
@expected_char char(1),
@table_name nvarchar(128) --your table name 
AS 
BEGIN

--Variable declaration
DECLARE @Column_Count_1 int 
DECLARE @SQLString AS NVARCHAR(4000)
DECLARE @count int=1
DECLARE @column_name nvarchar(128)

--Getting the count of column
SET @SQLString=N'select @Column_Count=count(*)  from  '+ @table_name
EXEC sp_executesql  @SQLString
, N'@Column_Count int OUTPUT'
, @Column_Count = @Column_Count_1 OUTPUT

--Getting the actual column names into a temporary table
select  c.name as name
into #temp_column_names
from sys.tables t
join sys.columns c
on t.object_id=c.object_id
where t.name=@table_name

--Looping through each column to replace the required character
WHILE (@count<=@Column_Count_1)
BEGIN
--setting the column name
SET @column_name=(select top 1 name from 
    (select Row_number()over (order by name) as r_n_n, name                  
    from #temp_column_names) aa 
    where r_n_n >=@count)

--updating the rows
SET @SQLString =N'Update '  + @table_name
SET @SQLString= @SQLString + N' Set ' + @column_name
SET @SQLString= @SQLString + N' = replace('  + @column_name
SET @SQLString =@SQLString + N',''' +@char_to_replace
SET @SQLString=@SQLString + N''',''' +@expected_char
SET @SQLString=@SQLString + N''');'

EXEC(@SQLString); 

SET @count=@count+1;
END

--Dropping the temp table
DROP TABLE #temp_column_names

END
GO



----Execution of the above procedure
--
--EXEC dbo.replace_char @char_to_replace, @expected_char, @table_name
----In your case
--
--EXEC dbo.replace_char '"', '','GV_DB_PensionCheckHistory'
----Sample_1 is the table which I created.