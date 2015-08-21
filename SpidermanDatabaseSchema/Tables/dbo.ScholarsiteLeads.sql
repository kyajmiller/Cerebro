CREATE TABLE [dbo].[ScholarsiteLeads]
(
[ScholarsiteLeadId] [int] NOT NULL IDENTITY(1, 1),
[Name] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[Amount] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Deadline] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Requirements] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[AnnualAwards] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Major] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[AcademicLevel] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[QualifiedMinorities] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[EligibleInstitution] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[EligibleRegion] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[USCitizen] [nvarchar] (10) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[USResident] [nvarchar] (10) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[ForeignNational] [nvarchar] (10) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[MinimumAge] [int] NULL,
[MaximumAge] [int] NULL,
[ClassRank] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[MinimumGPA] [nvarchar] (10) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[MinimumACT] [nvarchar] (10) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[MinimumSAT] [nvarchar] (10) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Tag] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
