CREATE TABLE [dbo].[SchollyValues]
(
[SchollyValueId] [int] NOT NULL,
[TypeOfControl] [char] (1) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[ControlName] [varchar] (150) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[ControlId] [varchar] (150) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Text] [varchar] (150) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[SchollyValues] ADD CONSTRAINT [PK_SchollyValues] PRIMARY KEY CLUSTERED  ([SchollyValueId]) ON [PRIMARY]
GO
