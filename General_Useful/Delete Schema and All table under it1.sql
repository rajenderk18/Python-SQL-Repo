USE [1250]

DECLARE @sql NVARCHAR(max)

SELECT @sql = stuff((
			SELECT ', ' + quotename(table_schema) + '.' + quotename(table_name)
			FROM INFORMATION_SCHEMA.Tables
			WHERE table_name like 'EL_%'
			--table_schema = 'dbo'
AND TABLE_TYPE = 'BASE TABLE'
			ORDER BY table_name
			FOR XML path('')
			), 1, 2, '')

SET @sql = 'DROP TABLE ' + @sql

PRINT @sql

BEGIN TRANSACTION

--EXECUTE (@SQL)

ROLLBACK TRANSACTION