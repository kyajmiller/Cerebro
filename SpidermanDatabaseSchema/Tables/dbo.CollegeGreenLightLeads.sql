CREATE TABLE [dbo].[CollegeGreenLightLeads]
(
[CollegeGreenLightLeadId] [int] NOT NULL IDENTITY(1, 1),
[Name] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[Amount] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Deadline] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Sponsor] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Description] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[Requirements] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Url] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[SourceWebsite] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[SourceText] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[Tag] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[CollegeGreenLightLeads] ADD CONSTRAINT [PK_CollegeGreenLightLeads] PRIMARY KEY CLUSTERED  ([CollegeGreenLightLeadId]) ON [PRIMARY]
GO
