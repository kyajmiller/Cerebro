from Classes.SUDBConnect import SUDBConnect
from Classes.CleanText import CleanText
import re
import time


class InsertIefaLeadArrayIntoIefaLeadsDB(object):
    def __init__(self, iefaLeadArray, fundingClassification, badScholarshipClassification):
        self.iefaLeadArray = iefaLeadArray
        self.fundingClassification = fundingClassification
        self.badScholarshipClassificaion = badScholarshipClassification
        self.db = SUDBConnect()
        self.fileSystemDB = SUDBConnect(destination='filesystem')

        self.name = self.iefaLeadArray[0]
        self.name = CleanText.cleanALLtheText(self.name)
        self.url = self.iefaLeadArray[1]
        self.sponsor = self.iefaLeadArray[2]
        self.submissionDeadline = self.iefaLeadArray[3]
        self.majors = self.iefaLeadArray[4]
        self.amount = self.iefaLeadArray[5]
        self.description = self.iefaLeadArray[6]
        self.otherCriteria = self.iefaLeadArray[7]
        self.numberAwards = self.iefaLeadArray[8]
        self.hostInstitution = self.iefaLeadArray[9]
        self.includes = self.iefaLeadArray[10]
        self.nationalityRequired = self.iefaLeadArray[11]
        self.hostCountries = self.iefaLeadArray[12]
        self.sourceWebsite = self.iefaLeadArray[13]
        self.sourceText = self.iefaLeadArray[14]
        self.date = time.strftime('%Y%m%d')

        if not self.checkIfAlreadyInDatabase():
            self.db.insertUpdateOrDeleteDB(
                "INSERT INTO dbo.IefaLeads (Name, Url, Sponsor, SubmissionDeadline, Majors, Amount, Description, OtherCriteria, NumberAwards, HostInstitution, Includes, NationalityRequired, HostCountries, SourceWebsite, SourceText, Date, Tag, BadScholarship) VALUES  (N'" + self.name + "', N'" + self.url + "', N'" + self.sponsor + "', N'" + self.submissionDeadline + "', N'" + self.majors + "', N'" + self.amount + "', N'" + self.description + "', N'" + self.otherCriteria + "', N'" + self.numberAwards + "', N'" + self.hostInstitution + "', N'" + self.includes + "', N'" + self.nationalityRequired + "', N'" + self.hostCountries + "', N'" + self.sourceWebsite + "', N'" + self.sourceText + "', '" + self.date + "', '" + self.fundingClassification + "', '" + self.badScholarshipClassificaion + "')")
        else:
            self.db.insertUpdateOrDeleteDB(
                "update dbo.IefaLeads set Sponsor=N'" + self.sponsor + "', SubmissionDeadline=N'" + self.submissionDeadline + "', Majors=N'" + self.majors + "', Amount=N'" + self.amount + "', Description=N'" + self.description + "', OtherCriteria=N'" + self.otherCriteria + "', NumberAwards=N'" + self.numberAwards + "', HostInstitution=N'" + self.hostInstitution + "', Includes=N'" + self.includes + "', NationalityRequired=N'" + self.nationalityRequired + "', HostCountries=N'" + self.hostCountries + "', SourceWebsite=N'" + self.sourceWebsite + "', SourceText=N'" + self.sourceText + "', Date='" + self.date + "', Tag='" + self.fundingClassification + "', BadScholarship='" + self.badScholarshipClassificaion + "' where Name='" + self.name + "' and Url='" + self.url + "'")
        self.writeFileToDisk()

    def writeFileToDisk(self):
        tableName = 'IefaLeads'
        user = 'Kya'
        website = re.sub('Leads', '', tableName)
        columns = self.db.getColumnNamesFromTable(tableName)
        currentRow = self.db.getRowsDB(
            "select * from dbo.IefaLeads where Name='" + self.name + "' and Url='" + self.url + "'")[0]
        self.fileSystemDB.writeFile(columns, currentRow, user, website, self.url, self.date)

    def checkIfAlreadyInDatabase(self):
        matchingRow = self.db.getRowsDB(
            "select * from dbo.IefaLeads where Name='" + self.name + "' and Url='" + self.url + "'")
        if matchingRow != []:
            return True
        else:
            return False
