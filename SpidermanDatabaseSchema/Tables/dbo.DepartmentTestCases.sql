CREATE TABLE [dbo].[DepartmentTestCases]
(
[DepartmentTestCaseId] [int] NOT NULL IDENTITY(1, 1),
[Scholarshipid] [int] NOT NULL,
[ScholarshipPackageId] [int] NOT NULL,
[LogicGroup] [int] NOT NULL,
[Elgibility] [varchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[AttributeId] [int] NOT NULL,
[AttributeTypeId] [int] NOT NULL,
[AttributeType] [varchar] (150) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[AttributeName] [varchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[RequirementTypeCode] [varchar] (10) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[RequirementValue] [varchar] (900) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[DepartmentTestCases] ADD CONSTRAINT [PK_DepartmentTestCases] PRIMARY KEY CLUSTERED  ([DepartmentTestCaseId]) ON [PRIMARY]
GO
