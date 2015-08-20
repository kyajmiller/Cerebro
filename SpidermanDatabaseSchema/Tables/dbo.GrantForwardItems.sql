CREATE TABLE [dbo].[GrantForwardItems]
(
[GrantForwardItemId] [int] NOT NULL IDENTITY(1, 1),
[Keyword] [nvarchar] (200) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[Url] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[Name] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Description] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Sponsor] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Amount] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Eligibility] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[SubmissionInfo] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Categories] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[OpportunitySourceLink] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[OpportunitySourceText] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Tag] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[DueDate] [date] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[GrantForwardItems] ADD CONSTRAINT [PK_GrantForwardItems] PRIMARY KEY CLUSTERED  ([GrantForwardItemId]) ON [PRIMARY]
GO
