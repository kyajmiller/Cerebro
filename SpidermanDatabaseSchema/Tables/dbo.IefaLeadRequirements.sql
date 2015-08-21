CREATE TABLE [dbo].[IefaLeadRequirements]
(
[IefaLeadRequirementId] [int] NOT NULL IDENTITY(1, 1),
[IefaLeadId] [int] NOT NULL,
[AttributeId] [int] NOT NULL,
[AttributeValue] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[IefaLeadRequirements] ADD CONSTRAINT [PK_IefaLeadRequirements] PRIMARY KEY CLUSTERED  ([IefaLeadRequirementId]) ON [PRIMARY]
GO
