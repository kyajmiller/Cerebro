from Classes.SUDBConnect import SUDBConnect
import time
import re


class InsertGoodCallLeadArrayIntoGoodCallLeadsDB(object):
    def __init__(self, goodCallLeadArray, fundingClassification, badScholarshipClassification):
        self.goodCallLeadArray = goodCallLeadArray
        self.fundingClassification = fundingClassification
        self.badScholarshipClassificaion = badScholarshipClassification
        self.db = SUDBConnect()
        self.fileSystemDB = SUDBConnect(destination='filesystem')

        self.name = goodCallLeadArray[0]
        self.url = goodCallLeadArray[1]
        self.numAwards = goodCallLeadArray[2]
        self.amount = goodCallLeadArray[3]
        self.description = goodCallLeadArray[4]
        self.sponsor = goodCallLeadArray[5]
        self.classStatus = goodCallLeadArray[6]
        self.major = goodCallLeadArray[7]
        self.gender = goodCallLeadArray[8]
        self.ethnicity = goodCallLeadArray[9]
        self.grades = goodCallLeadArray[10]
        self.testScores = goodCallLeadArray[11]
        self.geography = goodCallLeadArray[12]
        self.deadline = goodCallLeadArray[13]
        self.essayInfo = goodCallLeadArray[14]
        self.sourceWebsite = goodCallLeadArray[15]
        self.sourceText = goodCallLeadArray[16]
        self.date = time.strftime('%Y%m%d')

        if not self.checkIfAlreadyInDatabase():
            self.db.insertUpdateOrDeleteDB(
                "insert into dbo.GoodCallLeads (Name, Url, NumAwards, Amount, Description, Sponsor, ClassStatus, Major, Gender, Ethnicity, Grades, TestScores, Deadline, EssayInfo, SourceWebsite, SourceText, Date, Tag, BadScholarship) values (N'" + self.name + "', N'" + self.url + "', N'" + self.numAwards + "', N'" + self.amount + "', N'" + self.description + "', N'" + self.sponsor + "', N'" + self.classStatus + "', N'" + self.major + "', N'" + self.gender + "', N'" + self.ethnicity + "', N'" + self.grades + "', N'" + self.testScores + "', N'" + self.deadline + "', N'" + self.essayInfo + "', N'" + self.sourceWebsite + "', N'" + self.sourceText + "', '" + self.date + "', '" + self.fundingClassification + "', '" + self.badScholarshipClassificaion + "')")
        else:
            self.db.insertUpdateOrDeleteDB(
                "update dbo.GoodCallLeads set NumAwards=N'" + self.numAwards + "', Amount=N'" + self.amount + "', Description=N'" + self.description + "', Sponsor=N'" + self.sponsor + "', ClassStatus=N'" + self.classStatus + "', Major=N'" + self.major + "', Gender=N'" + self.gender + "', Ethnicity=N'" + self.ethnicity + "', Grades=N'" + self.grades + "', TestScores=N'" + self.testScores + "', Deadline=N'" + self.deadline + "', EssayInfo=N'" + self.essayInfo + "', SourceWebsite=N'" + self.sourceWebsite + "', SourceText=N'" + self.sourceText + "', Date='" + self.date + "', Tag='" + self.fundingClassification + "', BadScholarship='" + self.badScholarshipClassificaion + "' where Name='" + self.name + "' and Url='" + self.url + "'")
        self.writeFileToDisk()

    def writeFileToDisk(self):
        tableName = 'GoodCallLeads'
        user = 'Kya'
        website = re.sub('Leads', '', tableName)
        columns = self.db.getColumnNamesFromTable(tableName)
        currentRow = self.db.getRowsDB(
            "select * from dbo.GoodCallLeads where Name='" + self.name + "' and Url='" + self.url + "'")[0]
        self.fileSystemDB.writeFile(columns, currentRow, user, website, self.url, self.date)

    def checkIfAlreadyInDatabase(self):
        matchingRow = self.db.getRowsDB(
            "select * from dbo.GoodCallLeads where Name='" + self.name + "' and Url='" + self.url + "'")
        if matchingRow != []:
            return True
        else:
            return False
