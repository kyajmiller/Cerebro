CREATE TABLE [dbo].[IefaLeads]
(
[IefaLeadId] [int] NOT NULL IDENTITY(1, 1),
[Name] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[Url] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[Sponsor] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[SubmissionDeadline] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Majors] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Amount] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Description] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[OtherCriteria] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[NumberAwards] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[HostInstitution] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Includes] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[NationalityRequired] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[HostCountries] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[SourceWebsite] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[SourceText] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Tag] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[IefaLeads] ADD CONSTRAINT [PK_IefaLeads] PRIMARY KEY CLUSTERED  ([IefaLeadId]) ON [PRIMARY]
GO
