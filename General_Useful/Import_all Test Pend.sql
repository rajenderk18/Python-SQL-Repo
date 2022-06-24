---- ----------------Instruction-------------------------------
---- This script can be used to load all csv file under a folder into sql server.
---- The condition is file name should not have any space (' ') or hypen ('-'), file should be comma-separated. File should be either csv or txt and separated by comma (,) delimiter.
---- if the file is delimeted by any other character like (|, \t, *, . etc), you can always replace the delimiter by comman using the python script "N:\Conversion Files\SQL\NEBA_Projects\Python\Find_Replace.py". You need to change file path and character (delimiter) you want to change in the script. Run the script and it will replace in all file uder the particular folder.

---- ------SQL query changes before execution -----------------
---- All file to be imported should be stored locally on the server.
---- Change the database name under which you want to import all files in USE DB line (Ususally first non-comment line)
---- Change the file path in the variable @path below
---- Change the prefix (like GV_,  etc) in select query if you want to attach specific prefix before table name.
---- 
----[TestDB]
use [CLMHIST]

--BULK INSERT MULTIPLE FILES From a Folder 
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[allfilenames]'	) AND type in (N'U')) drop table allfilenames
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[NPend_1]'		) AND type in (N'U')) drop table NPend_1
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[NPend_2]'		) AND type in (N'U')) drop table NPend_2
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[HADetail1]'		) AND type in (N'U')) drop table HADetail1
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[HADetail2]'		) AND type in (N'U')) drop table HADetail2
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[cobf]'			) AND type in (N'U')) drop table cobf

--a table to loop thru filenames drop table ALLFILENAMES
CREATE TABLE ALLFILENAMES(WHICHPATH VARCHAR(255),WHICHFILE varchar(255))

--some variables
declare @filename varchar(255),
        @path     varchar(255),
        @sql      varchar(8000),
        @cmd      varchar(1000)


--get the list of files to process:
--- -D:\PendRaj\TestPendRaj\'
SET @path = '\\192.168.1.37\PendUpload\TestPend\'
SET @cmd = 'dir ' + @path + '*.csv /b'
INSERT INTO  ALLFILENAMES(WHICHFILE)
EXEC Master..xp_cmdShell @cmd
UPDATE ALLFILENAMES SET WHICHPATH = @path where WHICHPATH is null

delete from ALLFILENAMES where  WHICHFILE is null
--SELECT replace(whichfile,'.csv',''),* FROM dbo.ALLFILENAMES


--cursor loop
declare c1 cursor LOCAL for SELECT WHICHPATH,WHICHFILE FROM ALLFILENAMES where WHICHFILE like '%.csv%' order by WHICHFILE desc
open c1
fetch next from c1 into @path,@filename
While @@fetch_status <> -1
  begin
  --bulk insert won't take a variable name, so make a sql and execute it instead:
   set @sql = 

   'select * into '+ Replace(@filename, '.csv','')+'
    from openrowset(''MSDASQL''
    ,''Driver={Microsoft Access Text Driver (*.txt, *.csv)}''
    ,''select * from '+@Path+@filename+''')' 


print @sql
exec (@sql)

  fetch next from c1 into @path,@filename
  end
close c1
deallocate c1

---------------------CONCATENATE INTO ONE TABLE & DELETE -------------------

IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].NPend_03152022'		) AND type in (N'U')) drop table NPend_03152022 
 SELECT x.* 
   INTO NPend_03152022
   FROM 
 (
 Select *
   FROM [CLMHIST].[dbo].[NPend_1]
 UNION ALL
 Select *
   FROM [CLMHIST].[dbo].[NPend_2]
   ) x

print 'NPend_03152022 is created'

IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].COBF_03152022'		) AND type in (N'U')) drop table COBF_03152022
 Select *
 into COBF_03152022
   FROM [CLMHIST].[dbo].COBF
 
print 'COBF_03152022 is created'


--UPDATE HADetail1 SET [Procedure]				=replace([Procedure]		, ',', '');	
--UPDATE HADetail2 SET [Procedure]				=replace([Procedure]		, ',', '');
--UPDATE HADetail1 SET HADetail1				=replace([Total Billed Amt]		, ',', '');	
--UPDATE HADetail2 SET HADetail2				=replace([Total Covered Amount]	, ',', '');
--UPDATE HADetail1 SET HADetail1				=replace([Total Paid Amount]	, ',', '');	


ALTER TABLE HADetail1 ALTER COLUMN		[Procedure]				[nvarchar](255) NULL;
ALTER TABLE HADetail2 ALTER COLUMN		[Procedure]				[nvarchar](255) NULL;

IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].HADetail03152022'		) AND type in (N'U')) drop table HADetail03152022 
 SELECT x.* 
   INTO HADetail03152022
   FROM 
 (
 Select *
   FROM [CLMHIST].[dbo].HADetail1
 UNION ALL
 Select *
   FROM [CLMHIST].[dbo].HADetail2
   ) x

print 'HADetail03152022 is created'
 

 ----------------------CHANGE DATA TYPE---------------------------------
 --------------ALTER DATA TYPE OF PEND TABLE----------------------------

UPDATE NPend_03152022 SET [Days Since Entered]		=replace([Days Since Entered]	, ',', '');	
UPDATE NPend_03152022 SET [Days Since Recd]			=replace([Days Since Recd]		, ',', '');
UPDATE NPend_03152022 SET [Total Billed Amt]		=replace([Total Billed Amt]		, ',', '');	
UPDATE NPend_03152022 SET [Total Covered Amount]	=replace([Total Covered Amount]	, ',', '');
UPDATE NPend_03152022 SET [Total Paid Amount]		=replace([Total Paid Amount]	, ',', '');	


ALTER TABLE NPend_03152022 ALTER COLUMN	[Fund]						[nvarchar](255) NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[Claim Number]				[nvarchar](255) NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[Pend Code]					[nvarchar](255) NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[Status]					[nvarchar](255) NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[Member Ssn]				[float] NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[Individual Id]				[nvarchar](255) NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[Service Prov]				[nvarchar](255) NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[Alpha]						[nvarchar](255) NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[Date]						[nvarchar](255) NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[First From Date]			[datetime] NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[Days Since Entered]		[float] NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[Days Since Recd]			[float] NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[Reason Code]				[nvarchar](255) NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[Total Billed Amt]			[float] NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[Total Covered Amount]		[float] NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[Total Paid Amount]			[float] NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[Received Date]				[datetime] NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[Resolved Date]				[datetime] NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[Released Date]				[nvarchar](255) NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[Action Date]				[nvarchar](255) NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[Claim Operator]			[nvarchar](255) NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[Hld Operator]				[nvarchar](255) NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[Release Operator]			[nvarchar](255) NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[Resolved Oper]				[nvarchar](255) NULL;
ALTER TABLE NPend_03152022 ALTER COLUMN	[CLM-LINK Carrier Claim Id] [nvarchar](255) NULL


--------------------------CHANGE COBF DATATYPE------------------------------------------------

ALTER TABLE COBF_03152022 ALTER COLUMN	[Member No]			[float] NULL;
ALTER TABLE COBF_03152022 ALTER COLUMN	[Dep No]			[float] NULL;
ALTER TABLE COBF_03152022 ALTER COLUMN	[Member Name]		[nvarchar](255) NULL;
ALTER TABLE COBF_03152022 ALTER COLUMN	[Dependent Name]	[nvarchar](255) NULL;
ALTER TABLE COBF_03152022 ALTER COLUMN	[Fund]				[nvarchar](255) NULL;
ALTER TABLE COBF_03152022 ALTER COLUMN	[Cor Type]			[nvarchar](255) NULL;
ALTER TABLE COBF_03152022 ALTER COLUMN	[Type Description]	[nvarchar](255) NULL;
ALTER TABLE COBF_03152022 ALTER COLUMN	[Status]			[nvarchar](255) NULL;
ALTER TABLE COBF_03152022 ALTER COLUMN	[Create Date]		[datetime] NULL;
ALTER TABLE COBF_03152022 ALTER COLUMN	[Operator]			[nvarchar](255) NULL;
ALTER TABLE COBF_03152022 ALTER COLUMN	[Enclosure]			[nvarchar](255) NULL;
ALTER TABLE COBF_03152022 ALTER COLUMN	[Enc Description]	[nvarchar](255) NULL;
ALTER TABLE COBF_03152022 ALTER COLUMN	[Enc Value]			[nvarchar](255) NULL;
ALTER TABLE COBF_03152022 ALTER COLUMN	[Enc Date]			[datetime] NULL;
ALTER TABLE COBF_03152022 ALTER COLUMN	[Cmt Date]			[datetime] NULL;
ALTER TABLE COBF_03152022 ALTER COLUMN	[Cmt Operator]		[nvarchar](255) NULL

--------------------------CHANGE HADetail DATATYPE------------------------------------------------

ALTER TABLE HADetail03152022 ALTER COLUMN		[Group]					[float] NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Fund]					[nvarchar](255) NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Received Date]			[datetime] NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Issued Date]			[nvarchar](255) NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Claim No]				[nvarchar](255) NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Line No]				[float] NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Status]				[nvarchar](255) NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Procedure]				[nvarchar](255) NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Diag]					[nvarchar](255) NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[PS]					[float] NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Ben Code]				[nvarchar](255) NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Action Date]			[nvarchar](255) NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Billing Prov]			[float] NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Billing Prov NPI]		[float] NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Billing Provider Name] [nvarchar](255) NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Check No]				[float] NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Pay To]				[nvarchar](255) NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Incurred From]			[datetime] NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Incurred Thru]			[datetime] NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[TS]					[nvarchar](255) NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Qty]					[float] NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Billed]				[float] NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Pay Type]				[nvarchar](255) NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Covered]				[float] NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Allowed]				[float] NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Ann Ded]				[nvarchar](255) NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[CIR]					[float] NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Cob Adj]				[nvarchar](255) NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Net Cov]				[float] NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Paid]					[float] NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Total Billed Amt]		[float] NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Total Covered Amount]	[float] NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Patient]				[nvarchar](255) NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Total Paid Amount]		[float] NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Released Date]			[nvarchar](255) NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Days Since Recd]		[float] NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Claim Operator]		[nvarchar](255) NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Inelg Amount]			[float] NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[MemberID]				[nvarchar](255) NULL;
--ALTER TABLE HADetail03152022 ALTER COLUMN		[MemberID1]				[float] NULL;
ALTER TABLE HADetail03152022 ALTER COLUMN		[Claimant No]			[nvarchar](255) NULL;
--ALTER TABLE HADetail03152022 ALTER COLUMN		[Fund1]					[nvarchar](255) NULL

print 'ALL DATATYPE CHANGED SUCCESSFULLY'