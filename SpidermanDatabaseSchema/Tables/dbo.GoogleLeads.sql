CREATE TABLE [dbo].[GoogleLeads]
(
[GoogleLeadId] [int] NOT NULL,
[KeyTerm] [varchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[Title] [varchar] (400) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[Link] [varchar] (400) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[Description] [varchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[LinkBody] [varchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[DateLeadGenerated] [datetime] NOT NULL CONSTRAINT [DF_GoogleLeads_DateLeadGenerated] DEFAULT (getdate()),
[DateBodyGenerated] [datetime] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
