CREATE TABLE [dbo].[GrantForwardRequirements]
(
[GrantForwardRequirementId] [int] NOT NULL IDENTITY(1, 1),
[GrantForwardId] [int] NOT NULL,
[AttributeId] [int] NOT NULL,
[AttributeValue] [varchar] (900) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[GrantForwardRequirements] ADD CONSTRAINT [PK_GrantForwardRequirements] PRIMARY KEY CLUSTERED  ([GrantForwardRequirementId]) ON [PRIMARY]
GO
