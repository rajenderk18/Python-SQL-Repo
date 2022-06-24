USE [CLMHIST]
GO

IF EXISTS(SELECT 1 FROM sys.procedures WHERE Name = 'sp_temp')
DROP PROCEDURE dbo.sp_temp

go

CREATE PROCEDURE sp_temp 
    @pendDate varChar(20)
AS
BEGIN

declare @table varchar(50)
declare @query nvarchar(500)

set @table = 'NPend_' + @pendDate
print 'the table name is' + @table

set @query = 'SELECT top 100 * FROM [dbo].[' + @table + ']'
print @query
EXEC sp_executesql @query

-----------------

set @table = 'HADetail' + @pendDate

print @table

set @query = 'SELECT top 100 * FROM [dbo].[' + @table + ']'
--select top 100 * from [dbo].[NPend_05122022]

print @query
EXEC sp_executesql @query


end


 