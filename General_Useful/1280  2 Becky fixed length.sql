
---- ----------------Instruction-------------------------------
---- This script can be used to load all csv file under a folder into sql server.
---- The condition is file name should not have any space (' ') or hypen ('-'), file should be comma-separated. File should be either csv or csv.
---- if the file is delimeted by any other character like (|, \t, *, . etc), you can always replace the delimiter by comman using the python script "N:\Conversion Files\SQL\NEBA_Projects\Python\Find_Replace.py". You need to change file path and character (delimiter) you want to change in the script. Run the script and it will replace in all file uder the particular folder.

---- ------SQL query changes before execution -----------------
---- All file to be imported should be stored locally on the server.
---- Change the database name under which you want to import all files in USE DB line (Ususally first non-comment line)
---- Change the file path in the variable @path below
---- Change the prefix (like GV_, BD_ etc) in select query if you want to attach specific prefix before table name.
---- 

use [FunctionalDB_DontDelete]

IF OBJECT_ID('tempdb..#STEP1') IS NOT NULL																			DROP TABLE #STEP1
IF OBJECT_ID('tempdb..#STEP2') IS NOT NULL																			DROP TABLE #STEP2
IF OBJECT_ID('tempdb..#STEP3') IS NOT NULL																			DROP TABLE #STEP3

  -----------------------STEP 1 TO IMPORT THE CSV FILE-------------------------------------------------

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
			SET @path = 'D:\convdata\General\'
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


  -----------------------STEP 2 TO CONVERT THE SPECIFIED COLUMN-------------------------------------------------

SELECT  [TRA]
      ,[FI]
      ,[PLAN N]
      ,[FIL]
     -- ,[PARTICIPA]
	  ,case
		when LEN( [PARTICIPA] )= 6			then '000'	+cast([PARTICIPA] as varchar(9))
		when LEN( [PARTICIPA] )= 7			then '00'	+cast([PARTICIPA] as varchar(9)) 
		when LEN( [PARTICIPA] )= 8			then '0'	+cast([PARTICIPA] as varchar(9))
		when LEN( [PARTICIPA] )= 9			then		 cast([PARTICIPA] as varchar(9))
	  end as [PARTICIPA]
      ,[FILLER     ]
      ,[F]
      ,[IN]
      ,[S]
	  -- ,str(CONVERT(DECIMAL(9,2),[CONTRIB]), 9, 2)
	  --,str([CONTRIB], 9, 2)
	  ,case
	  when [CONTRIB]< 10								then '000000'	+REPLACE( cast(cast([CONTRIB] as decimal(9,2)) as varchar(10)) , '.', '')-- + '00'
	  when [CONTRIB]>= 10 and [CONTRIB]<100				then '00000'	+REPLACE( cast(cast([CONTRIB] as decimal(9,2)) as varchar(10)) , '.', '')-- + '00'
	  when [CONTRIB]>= 100 and [CONTRIB]<1000			then '0000'		+REPLACE( cast(cast([CONTRIB] as decimal(9,2)) as varchar(10)) , '.', '')-- + '00'
	  when [CONTRIB]>= 1000 and [CONTRIB]<10000			then '000'		+REPLACE( cast(cast([CONTRIB] as decimal(9,2)) as varchar(10)) , '.', '')-- + '00'
	  when [CONTRIB]>= 10000 and [CONTRIB]<100000		then '00'		+REPLACE( cast(cast([CONTRIB] as decimal(9,2)) as varchar(10)) , '.', '')-- + '00'
	  end as [CONTRIB]
      --,[CONTRIB]
      ,[FILLER1                                                        ]
      ,(
	  cast(year([PAY PERIOD END DATE]) as varchar(4))
	  +iif( len(cast(month([PAY PERIOD END DATE]) as varchar(2))) = 1, '0' + (cast(month([PAY PERIOD END DATE]) as varchar(2))), cast(month([PAY PERIOD END DATE]) as varchar(2)))
	  +iif( len(cast(day([PAY PERIOD END DATE]) as varchar(2))) = 1, '0' + (cast(day([PAY PERIOD END DATE]) as varchar(2))), cast(day([PAY PERIOD END DATE]) as varchar(2)))
	  ) as [PAY PERIOD END DATE]
      ,[I]
      ,'000' + cast([SUB PLAN NUMBER] as varchar(2)) as [SUB PLAN NUMBER]
	  --,CHARINDEX(',',([NAME                          ]))
      ,Left(Replace(
	  Replace(
			Replace(
			[NAME                          ]
			, ',,,,', '')
	  , ',,,', '')
	  , ',,', ''), charindex(',', [NAME                          ], (charindex(',', [NAME                          ], 1))+1)-1
	  ) + 
	  ' ' +
	  Right(Replace(
	  Replace(
			Replace(
			[NAME                          ]
			, ',,,,', '')
	  , ',,,', '')
	  , ',,', ''), charindex(',', Reverse([NAME                          ]))
	  )
	  as [NAME                          ]

	  -- ,[NAME                          ]
	 -- ,charindex(',', [NAME                          ], (charindex(',', [NAME                          ], 1))+1)
	 -- ,Replace(
	 -- Replace(
	--		[NAME                          ]
	 -- , ',,,', '')
	 -- , ',,', '')
	 -- as [NAME                          ]
	  --, Replace([NAME                          ], ',,,', '')
      ,[ADDRESS 1                     ]
      ,[ADDRESS 2                     ]
      ,[CITY              ]
      ,[ST]
      ,[ZIP C]
      ,[FILL]
	  ,(
	  cast(year([DATE OF BIRTH]) as varchar(4))
	  +iif( len(cast(month([DATE OF BIRTH]) as varchar(2))) = 1, '0' + (cast(month([DATE OF BIRTH]) as varchar(2))), cast(month([DATE OF BIRTH]) as varchar(2)))
	  +iif( len(cast(day([DATE OF BIRTH]) as varchar(2))) = 1, '0' + (cast(day([DATE OF BIRTH]) as varchar(2))), cast(day([DATE OF BIRTH]) as varchar(2)))
	  ) as [DATE OF BIRTH]
      
      ,[FILLER2          ]
      ,[MARITAL STATUS]
      ,[GENDER CODE]
	  ,'00' + cast([EMPLOYEE STATUS] as varchar(2)) as [EMPLOYEE STATUS]
      ,[EMPLOYEE]
      ,[P]
      ,[FILLER3                                                         ]
--	  ,(
--	  cast(year([CHECK DATE]) as varchar(4))
--	  +iif( len(cast(month([CHECK DATE]) as varchar(2))) = 1, '0' + (cast(month([CHECK DATE]) as varchar(2))), cast(month([CHECK DATE]) as varchar(2)))
--	  +iif( len(cast(day([CHECK DATE]) as varchar(2))) = 1, '0' + (cast(day([CHECK DATE]) as varchar(2))), cast(day([CHECK DATE]) as varchar(2)))
--	  ) as [CHECK DATE]

		,[CHECK DATE]
      ,[FILLER4                                                         ]
	  ,' ' as [FILLER5]
	  INTO #STEP1
  FROM [FunctionalDB_DontDelete].[dbo].[GV_1280A17]



  -----------------------STEP 3 TO MAKE FIXED LENGTH OF COLUMN-------------------------------------------------


  /****** Script for SelectTopNRows command from SSMS  ******/
SELECT  
	   dbo.CharPad (ISNULL( [TRA]																			, '' )		,3			,'LEFT',' ')	as  [TRA]																
      ,dbo.CharPad (ISNULL( [FI]																			, '' )		,2			,'LEFT',' ')	as  [FI]																
      ,dbo.CharPad (ISNULL( [PLAN N]																		, '' )		,6			,'LEFT',' ')	as  [PLAN N]															
      ,dbo.CharPad (ISNULL( [FIL]																			, '' )		,3			,'LEFT',' ')	as  [FIL]																
      ,dbo.CharPad (ISNULL( [PARTICIPA]																		, '' )		,9			,'LEFT',' ')	as  [PARTICIPA]															
      ,dbo.CharPad (ISNULL( [FILLER     ]																	, '' )		,11			,'LEFT',' ')	as  [FILLER     ]														
      ,dbo.CharPad (ISNULL( [F]																				, '' )		,1			,'LEFT',' ')	as  [F]																	
      ,dbo.CharPad (ISNULL( [IN]																			, '' )		,2			,'LEFT',' ')	as  [IN]																
      ,dbo.CharPad (ISNULL( [S]																				, '' )		,1			,'LEFT',' ')	as  [S]																	
      ,dbo.CharPad (ISNULL( [CONTRIB]																		, '' )		,9			,'LEFT',' ')	as  [CONTRIB]															
      ,dbo.CharPad (ISNULL( [FILLER1                                                        ]				, '' )		,60			,'LEFT',' ')	as  [FILLER1                                                        ]	
      ,dbo.CharPad (ISNULL( [PAY PERIOD END DATE]															, '' )		,8			,'LEFT',' ')	as  [PAY PERIOD END DATE]												
      ,dbo.CharPad (ISNULL( [I]																				, '' )		,1			,'LEFT',' ')	as  [I]																	
      ,dbo.CharPad (ISNULL( [SUB PLAN NUMBER]																, '' )		,4			,'LEFT',' ')	as  [SUB PLAN NUMBER]													
      ,dbo.CharPad (ISNULL( [NAME                          ]												, '' )		,30			,'LEFT',' ')	as  [NAME                          ]									
      ,dbo.CharPad (ISNULL( [ADDRESS 1                     ]												, '' )		,30			,'LEFT',' ')	as  [ADDRESS 1                     ]									
      ,dbo.CharPad (ISNULL( [ADDRESS 2                     ]												, '' )		,30			,'LEFT',' ')	as  [ADDRESS 2                     ]									
      ,dbo.CharPad (ISNULL( [CITY              ]															, '' )		,18			,'LEFT',' ')	as  [CITY              ]												
      ,dbo.CharPad (ISNULL( [ST]																			, '' )		,2			,'LEFT',' ')	as  [ST]																
      ,dbo.CharPad (ISNULL( [ZIP C]																			, '' )		,9			,'LEFT',' ')	as  [ZIP C]																
     --,dbo.CharPad (ISNULL( [FILL]																			, '' )		,4			,'LEFT',' ')	as  [FILL]																
      ,dbo.CharPad (ISNULL( [DATE OF BIRTH]																	, '' )		,8			,'LEFT',' ')	as  [DATE OF BIRTH]														
      ,dbo.CharPad (ISNULL( [FILLER2          ]																, '' )		,16			,'LEFT',' ')	as  [FILLER2          ]													
      ,dbo.CharPad (ISNULL( [MARITAL STATUS]																, '' )		,1			,'LEFT',' ')	as  [MARITAL STATUS]													
      ,dbo.CharPad (ISNULL( [GENDER CODE]																	, '' )		,1			,'LEFT',' ')	as  [GENDER CODE]														
      ,dbo.CharPad (ISNULL( [EMPLOYEE STATUS]																, '' )		,2			,'LEFT',' ')	as  [EMPLOYEE STATUS]													
      ,dbo.CharPad (ISNULL( [EMPLOYEE]																		, '' )		,8			,'LEFT',' ')	as  [EMPLOYEE]															
      ,dbo.CharPad (ISNULL( [P]																				, '' )		,1			,'LEFT',' ')	as  [P]																	
      ,dbo.CharPad (ISNULL( [FILLER3                                                         ]				, '' )		,75			,'LEFT',' ')	as  [FILLER3                                                         ]	
      ,dbo.CharPad (ISNULL( [CHECK DATE]																	, '' )		,8			,'LEFT',' ')	as  [CHECK DATE]														
      ,dbo.CharPad (ISNULL( [FILLER4                                                         ]				, '' )		,190		,'LEFT',' ')	as  [FILLER4                                                         ]	
	  ,dbo.CharPad (ISNULL( [FILLER5]																		, '' )		,190		,'LEFT',' ')	as  [FILLER5]	
   -- INTO #STEP2
  FROM #STEP1										
	   																										
																										