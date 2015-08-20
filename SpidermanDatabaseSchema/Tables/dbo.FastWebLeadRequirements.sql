CREATE TABLE [dbo].[FastWebLeadRequirements]
(
[FastWebLeadRequirementId] [int] NOT NULL IDENTITY(1, 1),
[FastWebLeadId] [int] NOT NULL,
[AttributeId] [int] NOT NULL,
[AttributeValue] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[FastWebLeadRequirements] ADD CONSTRAINT [PK_FastWebLeadRequirements] PRIMARY KEY CLUSTERED  ([FastWebLeadRequirementId]) ON [PRIMARY]
GO
