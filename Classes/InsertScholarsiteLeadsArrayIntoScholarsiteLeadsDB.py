from Classes.SUDBConnect import SUDBConnect
import time
import re


class InsertScholarsiteLeadsArrayIntoScholarsiteLeadsDB(object):
    def __init__(self, scholarsiteLeadArray, fundingClassification, badScholarshipClassification):
        self.scholarsiteLeadArray = scholarsiteLeadArray
        self.fundingClassification = fundingClassification
        self.badScholarshipClassificaion = badScholarshipClassification
        self.db = SUDBConnect()
        self.fileSystemDB = SUDBConnect(destination='filesystem')

        self.name = self.scholarsiteLeadArray[0]
        self.amount = self.scholarsiteLeadArray[1]
        self.deadline = self.scholarsiteLeadArray[2]
        self.requirements = self.scholarsiteLeadArray[3]
        self.annualAwards = self.scholarsiteLeadArray[4]
        self.major = self.scholarsiteLeadArray[5]
        self.academicLevel = self.scholarsiteLeadArray[6]
        self.qualifiedMinorities = self.scholarsiteLeadArray[7]
        self.eligibleInstitution = self.scholarsiteLeadArray[8]
        self.eligibleRegion = self.scholarsiteLeadArray[9]
        self.usCitizen = self.scholarsiteLeadArray[10]
        self.usResident = self.scholarsiteLeadArray[11]
        self.foreignNational = self.scholarsiteLeadArray[12]
        self.minimumAge = self.scholarsiteLeadArray[13]
        self.maximumAge = self.scholarsiteLeadArray[14]
        self.classRank = self.scholarsiteLeadArray[15]
        self.minimumGPA = self.scholarsiteLeadArray[16]
        self.minimumACT = self.scholarsiteLeadArray[17]
        self.minimumSAT = self.scholarsiteLeadArray[18]
        self.date = time.strftime('%Y%m%d')

        if not self.checkIfAlreadyInDB():
            self.db.insertUpdateOrDeleteDB(
                    "insert into dbo.ScholarsiteLeads (Name, Amount, Deadline, Requirements, AnnualAwards, Major, AcademicLevel, QualifiedMinorities, EligibleInstitution, EligibleRegion, USCitizen, USResident, ForeignNational, MinimumAge, MaximumAge, ClassRank, MinimumGPA, MinimumACT, MinimumSAT, Tag, BadScholarship, Date) values (N'" + self.name + "', N'" + self.amount + "', '" + self.deadline + "', N'" + self.requirements + "', N'" + self.annualAwards + "', N'" + self.major + "', N'" + self.academicLevel + "', N'" + self.qualifiedMinorities + "', N'" + self.eligibleInstitution + "', N'" + self.eligibleRegion + "', N'" + self.usCitizen + "', N'" + self.usResident + "', N'" + self.foreignNational + "', '" + self.minimumAge + "', '" + self.maximumAge + "', N'" + self.classRank + "', N'" + self.minimumGPA + "', N'" + self.minimumACT + "', N'" + self.minimumSAT + "', N'" + self.fundingClassification + "', '" + self.badScholarshipClassificaion + "', '" + self.date + "')")

    def checkIfAlreadyInDB(self):
        matchingRow = self.db.getRowsDB(
            "select * from dbo.ScholarsiteLeads where Name='" + self.name + "' and Requirements='" + self.requirements + "'")
        if matchingRow != []:
            return True
        else:
            return False
