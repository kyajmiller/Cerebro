CREATE TABLE [dbo].[URLs]
(
[UrlId] [int] NOT NULL IDENTITY(1, 1),
[Name] [varchar] (250) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[Type] [varchar] (250) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[ScholarshipWebsite] [varchar] (250) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[Status] [int] NULL,
[Last Review Date] [datetime] NULL,
[Usefulness] [int] NULL,
[Notes] [varchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Username] [varchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Password] [varchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[URLs] ADD CONSTRAINT [PK_URLs] PRIMARY KEY CLUSTERED  ([UrlId]) ON [PRIMARY]
GO
