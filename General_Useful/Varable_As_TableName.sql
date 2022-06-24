DECLARE @exp_dte  DATE    = '2015-12-31';
DECLARE @tab_name SYSNAME = '[dbo].' + QUOTENAME('BIK_' + FORMAT(@exp_dte, 'yyyyMM'));

IF OBJECT_ID (@tab_name, N'U') IS NOT NULL
BEGIN
   EXEC('DROP TABLE' +  @tab_name);
END

DECLARE @sql NVARCHAR(MAX) = N'SELECT DISTINCT *
                               INTO @tab_name
                               FROM table_x';

SET @sql = REPLACE(@sql, '@tab_name', @tab_name);

EXEC [dbo].[sp_executesql] @sql;

--------https://stackoverflow.com/questions/35985778/how-to-use-variable-as-table-name-in-select-into-statement

declare @exp_dte as date;
set @exp_dte='2015-12-31';

declare @tab_mth as nvarchar(max);
set @tab_mth=year(@exp_dte)*100+month(@exp_dte);


declare @tab_name as nvarchar(max)
set @tab_name='mis_anl.dbo.BIK_' + @tab_mth


declare @sql1 nvarchar(max)
set @sql1='drop table '+@tab_name;

IF exists(select 1 from information_schema.tables where table_name=@tab_name)
begin
   exec(@sql1);
   end

declare @sql nvarchar(max)
set @sql='
select distinct
*
into '+@tab_name+'
from table_x'

exec (@sql)
