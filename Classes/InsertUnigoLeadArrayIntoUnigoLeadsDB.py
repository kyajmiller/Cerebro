from Classes.SUDBConnect import SUDBConnect
import time
import re


class InsertUnigoLeadArrayIntoUnigoLeadsDB(object):
    def __init__(self, unigoLeadArray, fundingClassification, badScholarshipClassification):
        self.unigoLeadArray = unigoLeadArray
        self.fundingClassification = fundingClassification
        self.badScholarshipClassification = badScholarshipClassification
        self.db = SUDBConnect()
        self.fileSystemDB = SUDBConnect(destination='filesystem')

        self.name = self.unigoLeadArray[0]
        self.amount = self.unigoLeadArray[1]
        self.deadline = self.unigoLeadArray[2]
        self.url = self.unigoLeadArray[3]
        self.url = re.sub("'", '', self.url)
        self.sponsor = self.unigoLeadArray[4]
        self.awardAmount = self.unigoLeadArray[5]
        self.recipients = self.unigoLeadArray[6]
        self.requirements = self.unigoLeadArray[7]
        self.additionalInfo = self.unigoLeadArray[8]
        self.contact = self.unigoLeadArray[9]
        self.address = self.unigoLeadArray[10]
        self.deadlineInformation = self.unigoLeadArray[11]
        self.sourceWebsite = self.unigoLeadArray[12]
        self.sourceWebsite = re.sub("'", '', self.sourceWebsite)
        self.sourceText = self.unigoLeadArray[13]
        self.date = time.strftime('%Y%m%d')

    def checkIfAlreadyInDatabase(self):
        matchingRow = self.db.getRowsDB(
                "select * from dbo.UnigoLeads where Name='" + self.name + "' and SourceWebsite='" + self.sourceWebsite + "'")
        # "select * from dbo.UnigoLeads where Name='" + self.name + "' and Url='" + self.url + "'"
        if matchingRow != []:
            return True
        else:
            return False

    def writeFileToDisk(self):
        tableName = 'UnigoLeads'
        user = 'Kya'
        website = re.sub('Leads', '', tableName)
        columns = self.db.getColumnNamesFromTable(tableName)
        currentRow = self.db.getRowsDB(
                "select * from dbo.UnigoLeads where Name='" + self.name + "' and SourceWebsite='" + self.sourceWebsite + "'")[
            0]
        # "select * from dbo.UnigoLeads where Name='" + self.name + "' and Url='" + self.url + "'"
        self.fileSystemDB.writeFile(columns, currentRow, user, website, self.name, self.date)

    def insertUpdateLead(self):
        if not self.checkIfAlreadyInDatabase():
            self.db.insertUpdateOrDeleteDB(
                    "INSERT INTO dbo.UnigoLeads (Name, Amount, Deadline, Url, Sponsor, AwardAmount, Recipients, Requirements, AdditionalInfo, Contact, Address, DeadlineInformation, SourceWebsite, SourceText, Tag, BadScholarship, Date) VALUES (N'" + self.name + "', N'" + self.amount + "', N'" + self.deadline + "', N'" + self.url + "', N'" + self.sponsor + "', N'" + self.awardAmount + "', N'" + self.recipients + "', N'" + self.requirements + "', N'" + self.additionalInfo + "', N'" + self.contact + "', N'" + self.address + "', N'" + self.deadlineInformation + "', N'" + self.sourceWebsite + "', N'" + self.sourceText + "', N'" + self.fundingClassification + "', N'" + self.badScholarshipClassification + "', '" + self.date + "')")
            self.writeFileToDisk()
            return True
        else:
            self.db.insertUpdateOrDeleteDB(
                    "UPDATE dbo.UnigoLeads SET Amount=N'" + self.amount + "', Deadline=N'" + self.deadline + "', Url='" + self.url + "', Sponsor=N'" + self.sponsor + "', AwardAmount=N'" + self.awardAmount + "', Recipients=N'" + self.recipients + "', Requirements=N'" + self.requirements + "', AdditionalInfo=N'" + self.additionalInfo + "', Contact=N'" + self.contact + "', Address=N'" + self.address + "', DeadlineInformation=N'" + self.deadlineInformation + "', SourceText=N'" + self.sourceText + "', Tag=N'" + self.fundingClassification + "', BadScholarship=N'" + self.badScholarshipClassification + "', Date='" + self.date + "' WHERE Name=N'" + self.name + "' AND SourceWebsite=N'" + self.sourceWebsite + "'")
            # UPDATE dbo.UnigoLeads SET Amount=N'" + self.amount + "', Deadline=N'" + self.deadline + "', Url='" + self.url + "', Sponsor=N'" + self.sponsor + "', AwardAmount=N'" + self.awardAmount + "', Recipients=N'" + self.recipients + "', Requirements=N'" + self.requirements + "', AdditionalInfo=N'" + self.additionalInfo + "', Contact=N'" + self.contact + "', Address=N'" + self.address + "', DeadlineInformation=N'" + self.deadlineInformation + "', SourceText=N'" + self.sourceText + "', Tag=N'" + self.fundingClassification + "', BadScholarship=N'" + self.badScholarshipClassification + "', Date='" + self.date + "' WHERE Name=N'" + self.name + "' AND SourceWebsite=N'" + self.sourceWebsite + "'
            # UPDATE dbo.UnigoLeads SET Amount=N'" + self.amount + "', Deadline=N'" + self.deadline + "', Sponsor=N'" + self.sponsor + "', AwardAmount=N'" + self.awardAmount + "', Recipients=N'" + self.recipients + "', Requirements=N'" + self.requirements + "', AdditionalInfo=N'" + self.additionalInfo + "', Contact=N'" + self.contact + "', Address=N'" + self.address + "', DeadlineInformation=N'" + self.deadlineInformation + "', SourceWebsite=N'" + self.sourceWebsite + "', SourceText=N'" + self.sourceText + "', Tag=N'" + self.fundingClassification + "', BadScholarship=N'" + self.badScholarshipClassification + "', Date='" + self.date + "' WHERE Name=N'" + self.name + "' AND Url=N'" + self.url + "'
            self.writeFileToDisk()
            return False
