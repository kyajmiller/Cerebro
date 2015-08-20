CREATE TABLE [dbo].[Tests]
(
[TestId] [int] NOT NULL IDENTITY(1, 1),
[Regex] [varchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[AttributeId] [int] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[Tests] ADD CONSTRAINT [PK_Tests] PRIMARY KEY CLUSTERED  ([TestId]) ON [PRIMARY]
GO
