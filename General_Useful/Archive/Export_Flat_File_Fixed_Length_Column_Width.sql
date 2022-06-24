
USE [FunctionalDB_DontDelete]
GO
/****** Object:  UserDefinedFunction [dbo].[CharPad]    Script Date: 1/10/2015 11:38:27 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
/*
Script  : Character Padding Function; Assist with fixed width file creation
Server:  192.168.1.27\conversion
Version : 1.0 (03/01/2022)

*/

Create FUNCTION [dbo].[CharPad] (
     @Input VARCHAR(255)
    ,@OutputWidth INT
    ,@OutputAlign VARCHAR(5)
    ,@PadCharacter CHAR(1) )
RETURNS VARCHAR(255)
AS
BEGIN
DECLARE @Output VARCHAR(255)
DECLARE @InputWidth INT

SET @InputWidth = LEN(@Input)

IF @InputWidth > @OutputWidth
    BEGIN 
        IF @OutputAlign = 'LEFT'
            BEGIN
            SET @Output = LEFT(@Input,@OutputWidth)
            END
        IF @OutputAlign = 'RIGHT'
            BEGIN
            SET @Output = RIGHT(@Input,@OutputWidth)
            END
    END

IF @InputWidth < @OutputWidth 
    BEGIN 
        IF @OutputAlign = 'RIGHT'
            BEGIN
            SET @Output = REPLICATE(@PadCharacter, @OutputWidth - @InputWidth ) + @Input
            END
        IF @OutputAlign = 'LEFT'
            BEGIN
            SET @Output =@Input+ REPLICATE(@PadCharacter, @OutputWidth - @InputWidth )
            END
    END

IF @InputWidth = @OutputWidth 
    SET @Output = @Input

RETURN (@Output)
END