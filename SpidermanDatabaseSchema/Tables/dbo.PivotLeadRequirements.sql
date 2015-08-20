CREATE TABLE [dbo].[PivotLeadRequirements]
(
[PivotLeadRequirementId] [int] NOT NULL IDENTITY(1, 1),
[PivotLeadId] [int] NOT NULL,
[AttributeId] [int] NOT NULL,
[AttributeValue] [varchar] (900) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[PivotLeadRequirements] ADD CONSTRAINT [PK_PivotLeadRequirements] PRIMARY KEY CLUSTERED  ([PivotLeadRequirementId]) ON [PRIMARY]
GO
