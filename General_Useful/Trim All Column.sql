USE [1240]
GO
DROP PROCEDURE usp_trim_all_string_columns
GO
CREATE PROCEDURE usp_trim_all_string_columns
@schema_Table_name VARCHAR(MAX)
AS
DECLARE @SQL AS VARCHAR(MAX)
 
SET @SQL=STUFF((SELECT ', ' + QUOTENAME([name])
+ ' = LTRIM(RTRIM(' + QUOTENAME([name]) + '))' FROM
sys.columns WHERE object_id=object_id(@schema_Table_name)
AND system_type_id IN(35,99,167,175,231,29)
FOR XML PATH('')),1,1,'')
--PRINT @SQL
 
SET @SQL = 'UPDATE ' + @schema_Table_name + ' SET' + @SQL
PRINT @SQL
 
--EXEC(@SQL)
GO

/*
---- To find out system type id for different datatype, use below query
SELECT system_type_id, name
FROM sys.types
WHERE system_type_id = user_type_id
*/

EXEC usp_trim_all_string_columns '[dbo].[ZenithFile1]'
GO