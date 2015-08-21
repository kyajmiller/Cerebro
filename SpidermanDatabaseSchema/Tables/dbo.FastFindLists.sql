CREATE TABLE [dbo].[FastFindLists]
(
[FastFindListId] [int] NOT NULL IDENTITY(1, 1),
[AttributeId] [int] NOT NULL,
[ValueShown] [varchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[OtherValuesToCheck] [varchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[FastFindLists] ADD CONSTRAINT [PK_FastFindLists] PRIMARY KEY CLUSTERED  ([FastFindListId]) ON [PRIMARY]
GO
