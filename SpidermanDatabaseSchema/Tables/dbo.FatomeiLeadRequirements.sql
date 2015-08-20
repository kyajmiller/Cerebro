CREATE TABLE [dbo].[FatomeiLeadRequirements]
(
[FatomeiLeadRequirementId] [int] NOT NULL IDENTITY(1, 1),
[FatomeiLeadId] [int] NOT NULL,
[AttributeId] [int] NOT NULL,
[AttributeValue] [varchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
