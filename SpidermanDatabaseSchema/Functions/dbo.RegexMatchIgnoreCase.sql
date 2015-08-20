SET QUOTED_IDENTIFIER OFF
GO
SET ANSI_NULLS OFF
GO
CREATE FUNCTION [dbo].[RegexMatchIgnoreCase] (@input [nvarchar] (max), @pattern [nvarchar] (max))
RETURNS [bit]
WITH EXECUTE AS CALLER
EXTERNAL NAME [SqlRegEx].[UserDefinedFunctions].[RegexMatchIgnoreCase]
GO
