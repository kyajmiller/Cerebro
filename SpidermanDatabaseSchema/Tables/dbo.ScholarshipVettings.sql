CREATE TABLE [dbo].[ScholarshipVettings]
(
[ScholarshipVettingId] [int] NOT NULL IDENTITY(1, 1),
[SearchTerms] [varchar] (500) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[SourceUrl] [varchar] (500) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[ScholarshipUrl] [varchar] (500) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[ScholarshipName] [varchar] (500) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[Description] [varchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[DeadlineDate] [date] NULL,
[OtherValues] [varchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[VettedStatusId] [int] NOT NULL CONSTRAINT [DF_ScholarshipVettings_VettedStatusId] DEFAULT ((0))
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[ScholarshipVettings] ADD CONSTRAINT [PK_ScholarshipVettings] PRIMARY KEY CLUSTERED  ([ScholarshipVettingId]) ON [PRIMARY]
GO
