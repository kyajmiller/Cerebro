CREATE TABLE [dbo].[CheggRequirements]
(
[CheggRequirementId] [int] NOT NULL IDENTITY(1, 1),
[CheggLeadId] [int] NOT NULL,
[AttributeId] [int] NOT NULL,
[AttributeValue] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[CheggRequirements] ADD CONSTRAINT [PK_CheggRequirements] PRIMARY KEY CLUSTERED  ([CheggRequirementId]) ON [PRIMARY]
GO
