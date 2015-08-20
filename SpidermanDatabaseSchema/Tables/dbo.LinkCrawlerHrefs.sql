CREATE TABLE [dbo].[LinkCrawlerHrefs]
(
[LinkCrawlerHrefId] [int] NOT NULL IDENTITY(1, 1),
[QuestionId] [int] NOT NULL,
[LinkUrl] [varchar] (900) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[LinkName] [varchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[LinkDescription] [varchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[LinkBody] [varchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[ProcessUsed] [int] NULL,
[IsBadLink] [bit] NOT NULL CONSTRAINT [DF_LinkCrawlerHrefs_IsBadLink] DEFAULT ((0)),
[InsertDate] [datetime] NULL CONSTRAINT [DF_LinkCrawlerHrefs_InsertDate] DEFAULT (getdate()),
[UpdateDate] [datetime] NULL CONSTRAINT [DF_LinkCrawlerHrefs_UpdateDate] DEFAULT (getdate())
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[LinkCrawlerHrefs] ADD CONSTRAINT [PK_LinkCrawlerHrefs] PRIMARY KEY CLUSTERED  ([LinkCrawlerHrefId]) ON [PRIMARY]
GO
CREATE UNIQUE NONCLUSTERED INDEX [IX_LinkCrawlerHrefs] ON [dbo].[LinkCrawlerHrefs] ([LinkUrl]) ON [PRIMARY]
GO
CREATE NONCLUSTERED INDEX [IX_LinkCrawlerHrefs_1] ON [dbo].[LinkCrawlerHrefs] ([QuestionId]) ON [PRIMARY]
GO
ALTER TABLE [dbo].[LinkCrawlerHrefs] ADD CONSTRAINT [FK_LinkCrawlerHrefs_Questions] FOREIGN KEY ([QuestionId]) REFERENCES [dbo].[Questions] ([QuestionId])
GO
