SET QUOTED_IDENTIFIER OFF
GO
SET ANSI_NULLS OFF
GO
CREATE FUNCTION [dbo].[RegexMatch] (@input [nvarchar] (max), @pattern [nvarchar] (max))
RETURNS [bit]
WITH EXECUTE AS CALLER
EXTERNAL NAME [SqlRegEx].[UserDefinedFunctions].[RegexMatch]
GO
