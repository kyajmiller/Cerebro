CREATE TABLE [dbo].[LinkCrawlerContentValues]
(
[LinkCrawlerContentValueId] [int] NOT NULL IDENTITY(1, 1),
[LinkCrawlerHrefId] [int] NOT NULL,
[ContentFound] [varchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[Frequency] [int] NOT NULL,
[AccessedFirst] [datetime] NOT NULL CONSTRAINT [DF_LinkCrawlerContentValues_AccessedFirst] DEFAULT (getdate()),
[LastAccessed] [datetime] NOT NULL CONSTRAINT [DF_LinkCrawlerContentValues_LastAccessed] DEFAULT (getdate())
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[LinkCrawlerContentValues] ADD CONSTRAINT [PK_LinkCrawlerContentValues] PRIMARY KEY CLUSTERED  ([LinkCrawlerContentValueId]) ON [PRIMARY]
GO
ALTER TABLE [dbo].[LinkCrawlerContentValues] ADD CONSTRAINT [FK_LinkCrawlerContentValues_LinkCrawlerHrefs] FOREIGN KEY ([LinkCrawlerHrefId]) REFERENCES [dbo].[LinkCrawlerHrefs] ([LinkCrawlerHrefId])
GO
