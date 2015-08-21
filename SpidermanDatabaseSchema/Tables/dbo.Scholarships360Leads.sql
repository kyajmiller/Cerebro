CREATE TABLE [dbo].[Scholarships360Leads]
(
[Scholarships360LeadId] [int] NOT NULL IDENTITY(1, 1),
[Name] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[Url] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[Description] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Eligibility] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Amount] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[AmountInfo] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Deadline] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[DeadlineInfo] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[SourceWebsite] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[SourceText] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[Scholarships360Leads] ADD CONSTRAINT [PK_Scholarships360Leads] PRIMARY KEY CLUSTERED  ([Scholarships360LeadId]) ON [PRIMARY]
GO
