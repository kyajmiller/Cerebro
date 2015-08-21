CREATE TABLE [dbo].[RegExHelpers]
(
[RegExHelperId] [int] NOT NULL IDENTITY(1, 1),
[AttributeId] [int] NOT NULL,
[RegEx] [varchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[RegExHelper] [varchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[ValueToReturn] [varchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[RegExHelpers] ADD CONSTRAINT [PK_RegExHelpers] PRIMARY KEY CLUSTERED  ([RegExHelperId]) ON [PRIMARY]
GO
