SET QUOTED_IDENTIFIER ON
GO
SET ANSI_NULLS ON
GO
CREATE PROC [dbo].[SendDataForTestCases]
as
TRUNCATE TABLE Spiderman.dbo.departmenttestcases
INSERT  INTO Spiderman.dbo.DepartmentTestCases
        SELECT  ScholarshipPackages.Scholarshipid ,
                ScholarshipPackageRequirements.ScholarshipPackageId ,
                LogicGroup ,
                Elgibility ,
                Attributes.AttributeId ,
                Attributes.AttributeTypeId ,
                AttributeType ,
                AttributeName ,
                RequirementTypeCode ,
                RequirementValue
        FROM    ScholarshipUniverse.dbo.Scholarships
                INNER JOIN ScholarshipUniverse.dbo.ScholarshipPackages ON ScholarshipPackages.Scholarshipid = Scholarships.ScholarshipId
                INNER JOIN ScholarshipUniverse.dbo.ScholarshipPackageRequirements ON ScholarshipPackageRequirements.ScholarshipPackageId = ScholarshipPackages.ScholarshipPackageId
                INNER JOIN ScholarshipUniverse.dbo.Attributes ON Attributes.AttributeId = ScholarshipPackageRequirements.AttributeId
                INNER JOIN ScholarshipUniverse.dbo.AttributeTypes ON AttributeTypes.AttributeTypeId = Attributes.AttributeTypeId
        WHERE   SourceId IN ( SELECT    CollegeID
                              FROM      dbo.Colleges )
        ORDER BY ScholarshipPackages.Scholarshipid ,
                ScholarshipPackageRequirements.ScholarshipPackageId ,
                AttributeId;
GO
