SET QUOTED_IDENTIFIER OFF
GO
SET ANSI_NULLS OFF
GO
CREATE FUNCTION [dbo].[RegexReplaceSqlBoolean] (@input [nvarchar] (max), @pattern [nvarchar] (max), @replacement [nvarchar] (max))
RETURNS [nvarchar] (max)
WITH EXECUTE AS CALLER
EXTERNAL NAME [SqlRegEx].[UserDefinedFunctions].[RegexReplaceSqlBoolean]
GO
