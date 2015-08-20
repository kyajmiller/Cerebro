CREATE TABLE [dbo].[CollegeGreenLightRequirements]
(
[CollegeGreenLightRequirementId] [int] NOT NULL IDENTITY(1, 1),
[CollegeGreenLightLeadId] [int] NOT NULL,
[AttributeId] [int] NOT NULL,
[AttributeValue] [varchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[CollegeGreenLightRequirements] ADD CONSTRAINT [PK_CollegeGreenLightRequirements] PRIMARY KEY CLUSTERED  ([CollegeGreenLightRequirementId]) ON [PRIMARY]
GO
