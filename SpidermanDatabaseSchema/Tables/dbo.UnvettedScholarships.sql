CREATE TABLE [dbo].[UnvettedScholarships]
(
[UnvettedScholarshipId] [int] NOT NULL IDENTITY(1, 1),
[Url] [varchar] (500) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[ScholarshipName] [varchar] (500) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[ScholarshipDescription] [varchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[DeadlineDate] [varchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Amount] [varchar] (100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[HtmlContent] [varchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[DateUpdated] [datetime] NOT NULL,
[DateInserted] [datetime] NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[UnvettedScholarships] ADD CONSTRAINT [PK_UnvettedScholarships] PRIMARY KEY CLUSTERED  ([UnvettedScholarshipId]) ON [PRIMARY]
GO
