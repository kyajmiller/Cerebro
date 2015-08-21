CREATE TABLE [dbo].[Questions]
(
[QuestionId] [int] NOT NULL IDENTITY(1, 1),
[AttributeId] [int] NULL,
[AttributeListValueId] [int] NULL,
[FormFieldName] [varchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[ListValue] [varchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Questions] ADD CONSTRAINT [PK_Questions] PRIMARY KEY CLUSTERED  ([QuestionId]) ON [PRIMARY]
GO
