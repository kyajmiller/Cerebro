CREATE TABLE [dbo].[JustTests]
(
[JustTestId] [int] NOT NULL IDENTITY(1, 1),
[TestValue] [varchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[JustTests] ADD CONSTRAINT [PK_JustTests] PRIMARY KEY CLUSTERED  ([JustTestId]) ON [PRIMARY]
GO
