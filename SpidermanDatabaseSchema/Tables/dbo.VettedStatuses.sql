CREATE TABLE [dbo].[VettedStatuses]
(
[VettedStatusId] [int] NOT NULL,
[VettedStatusDescription] [varchar] (20) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[VettedStatuses] ADD CONSTRAINT [PK_VettedStatuses] PRIMARY KEY CLUSTERED  ([VettedStatusId]) ON [PRIMARY]
GO
