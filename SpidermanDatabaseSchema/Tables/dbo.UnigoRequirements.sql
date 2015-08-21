CREATE TABLE [dbo].[UnigoRequirements]
(
[UnigoRequirementId] [int] NOT NULL IDENTITY(1, 1),
[UnigoLeadId] [int] NOT NULL,
[AttributeId] [int] NOT NULL,
[AttributeValue] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[UnigoRequirements] ADD CONSTRAINT [PK_UnigoRequirements] PRIMARY KEY CLUSTERED  ([UnigoRequirementId]) ON [PRIMARY]
GO
