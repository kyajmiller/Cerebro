CREATE TABLE [dbo].[DepartmentResults]
(
[DepartmentResultId] [int] NOT NULL IDENTITY(1, 1),
[ScholarshipPackageId] [int] NOT NULL,
[AttributeId] [int] NOT NULL,
[RequirementValue] [varchar] (10) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[LogicGroup] [int] NOT NULL CONSTRAINT [DF_DepartmentResults_LogicGroup] DEFAULT ((0))
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[DepartmentResults] ADD CONSTRAINT [PK_DepartmentResults] PRIMARY KEY CLUSTERED  ([DepartmentResultId]) ON [PRIMARY]
GO
