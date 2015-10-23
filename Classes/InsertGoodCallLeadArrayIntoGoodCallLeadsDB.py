from Classes.SUDBConnect import SUDBConnect


class InsertGoodCallLeadArrayIntoGoodCallLeadsDB(object):
    def __init__(self, goodCallLeadArray):
        self.goodCallLeadArray = goodCallLeadArray
        self.db = SUDBConnect()

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

        if not self.checkIfAlreadyInDatabase():
            self.db.insertUpdateOrDelete(
                "insert into dbo.GoodCallLeads (Name, Url, NumAwards, Amount, Description, Sponsor, ClassStatus, Major, Gender, Ethnicity, Grades, TestScores, Deadline, EssayInfo, SourceWebsite, SourceText) values (N'" + self.name + "', N'" + self.url + "', N'" + self.numAwards + "', N'" + self.amount + "', N'" + self.description + "', N'" + self.sponsor + "', N'" + self.classStatus + "', N'" + self.major + "', N'" + self.gender + "', N'" + self.ethnicity + "', N'" + self.grades + "', N'" + self.testScores + "', N'" + self.deadline + "', N'" + self.essayInfo + "', N'" + self.sourceWebsite + "', N'" + self.sourceText + "')")

    def checkIfAlreadyInDatabase(self):
        matchingRow = self.db.getRows(
            "select * from dbo.GoodCallLeads where Name='" + self.name + "' and Url='" + self.url + "'")
        if matchingRow != []:
            return True
        else:
            return False
