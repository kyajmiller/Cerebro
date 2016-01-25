from Classes.SUDBConnect import SUDBConnect
import time
import re


class InsertFastWebLeadIntoFastWebLeadsDB(object):
    def __init__(self, fastWebLeadArray, fundingClassification, badScholarshipClassification):
        self.badScholarshipClassification = badScholarshipClassification
        self.fundingClassification = fundingClassification
        self.fastWebLeadArray = fastWebLeadArray
        self.db = SUDBConnect()
        self.fileSystemDB = SUDBConnect(destination='filesystem')

        self.name = self.fastWebLeadArray[0]
        self.url = self.fastWebLeadArray[1]
        self.sponsor = self.fastWebLeadArray[2]
        self.amount = self.fastWebLeadArray[3]
        self.deadline = self.fastWebLeadArray[4]
        self.description = self.fastWebLeadArray[5]
        self.awardType = self.fastWebLeadArray[6]
        self.numAwards = self.fastWebLeadArray[7]
        self.majors = self.fastWebLeadArray[8]
        self.additionalInfo = self.fastWebLeadArray[9]
        self.sourceWebsite = self.fastWebLeadArray[10]
        self.sourceText = self.fastWebLeadArray[11]
        self.date = time.strftime('%Y%m%d')

    def writeFileToDisk(self):
        tableName = 'FastWebLeads'
        user = 'Kya'
        website = re.sub('Leads', '', tableName)
        columns = self.db.getColumnNamesFromTable(tableName)
        currentRow = self.db.getRowsDB(
            "select * from dbo.FastWebLeads where Name='" + self.name + "' and Url='" + self.url + "'")[0]
        self.fileSystemDB.writeFile(columns, currentRow, user, website, self.url, self.date)

    def checkIfAlreadyInDatabase(self):
        matchingRow = self.db.getRowsDB(
            "select * from dbo.FastWebLeads where Name='" + self.name + "' and Url='" + self.url + "'")
        if matchingRow != []:
            return True
        else:
            return False

    def insertUpdateLead(self):
        if not self.checkIfAlreadyInDatabase():
            self.db.insertUpdateOrDeleteDB(
                    "insert into dbo.FastWebLeads (Name, Url, Sponsor, Amount, Deadline, Description, AwardType, NumAwards, Majors, AdditionalInfo, SourceWebsite, SourceText, Date, Tag, BadScholarship) values (N'" + self.name + "', N'" + self.url + "', N'" + self.sponsor + "', N'" + self.amount + "', N'" + self.deadline + "', N'" + self.description + "', N'" + self.awardType + "', N'" + self.numAwards + "', N'" + self.majors + "', N'" + self.additionalInfo + "', N'" + self.sourceWebsite + "', N'" + self.sourceText + "', '" + self.date + "', '" + self.fundingClassification + "', '" + self.badScholarshipClassification + "')")
            self.writeFileToDisk()
            return True
        else:
            self.db.insertUpdateOrDeleteDB(
                    "update dbo.FastWebLeads set Sponsor='" + self.sponsor + "', Amount='" + self.amount + "', Deadline='" + self.deadline + "', Description='" + self.description + "', AwardType='" + self.awardType + "', NumAwards='" + self.numAwards + "', Majors='" + self.majors + "', AdditionalInfo='" + self.additionalInfo + "', SourceWebsite='" + self.sourceWebsite + "', SourceText='" + self.sourceText + "', Date='" + self.date + "', Tag='" + self.fundingClassification + "', BadScholarship='" + self.badScholarshipClassification + "' where Name='" + self.name + "' and Url='" + self.url + "'")
            self.writeFileToDisk()
            return False
