CREATE TABLE [dbo].[UnigoLeads]
(
[UnigoLeadId] [int] NOT NULL IDENTITY(1, 1),
[Name] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[Amount] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Deadline] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Sponsor] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[AwardAmount] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Recipients] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Requirements] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[AdditionalInfo] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Contact] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Address] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[SourceWebsite] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[SourceText] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Tag] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[UnigoLeads] ADD CONSTRAINT [PK_UnigoLeads] PRIMARY KEY CLUSTERED  ([UnigoLeadId]) ON [PRIMARY]
GO
