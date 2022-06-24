CREATE FUNCTION [dbo].Circle(@Radius int)
RETURNS real
AS
BEGIN
DECLARE
@Area real
SET @Area=3.14*@Radius*@Radius
RETURN @Area
END


SELECT [dbo].Circle(5) AS Area