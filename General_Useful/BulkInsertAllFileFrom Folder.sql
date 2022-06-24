---- ----------------Instruction-------------------------------
---- This script can be used to load all csv file under a folder into sql server.
---- The condition is file name should not have any space (' ') or hypen ('-'), file should be comma-separated. File should be either csv or txt.
---- if the file is delimeted by any other character like (|, \t, *, . etc), you can always replace the delimiter by comman using the python script "N:\Conversion Files\SQL\NEBA_Projects\Python\Find_Replace.py". You need to change file path and character (delimiter) you want to change in the script. Run the script and it will replace in all file uder the particular folder.

---- ------SQL query changes before execution -----------------
---- All file to be imported should be stored locally on the server.
---- Change the database name under which you want to import all files in USE DB line (Ususally first non-comment line)
---- Change the file path in the variable @path below
---- Change the prefix (like GV_, BD_ etc) in select query if you want to attach specific prefix before table name.
---- 

use [1250]

--BULK INSERT MULTIPLE FILES From a Folder 
drop table if exists allfilenames
--a table to loop thru filenames drop table ALLFILENAMES
CREATE TABLE ALLFILENAMES(WHICHPATH VARCHAR(255),WHICHFILE varchar(255))

--some variables
declare @filename varchar(255),
        @path     varchar(255),
        @sql      varchar(8000),
        @cmd      varchar(1000)


--get the list of files to process:
SET @path = 'D:\convdata\1250\GV00_FINAL_DataFiles_12_29_2021\'
SET @cmd = 'dir ' + @path + '*.csv /b'
INSERT INTO  ALLFILENAMES(WHICHFILE)
EXEC Master..xp_cmdShell @cmd
UPDATE ALLFILENAMES SET WHICHPATH = @path where WHICHPATH is null

delete from ALLFILENAMES where  WHICHFILE is null
--SELECT replace(whichfile,'.csv',''),* FROM dbo.ALLFILENAMES


--cursor loop
declare c1 cursor for SELECT WHICHPATH,WHICHFILE FROM ALLFILENAMES where WHICHFILE like '%.csv%' order by WHICHFILE desc
open c1
fetch next from c1 into @path,@filename
While @@fetch_status <> -1
  begin
  --bulk insert won't take a variable name, so make a sql and execute it instead:
   set @sql = 

   'select * into '+ CONCAT('GV_', Replace(@filename, '.csv',''))+'
    from openrowset(''MSDASQL''
    ,''Driver={Microsoft Access Text Driver (*.txt, *.csv)}''
    ,''select * from '+@Path+@filename+''')' 


print @sql
exec (@sql)

  fetch next from c1 into @path,@filename
  end
close c1
deallocate c1