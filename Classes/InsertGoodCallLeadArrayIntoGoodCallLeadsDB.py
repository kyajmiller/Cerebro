from Classes.SUDBConnect import SUDBConnect


class InsertGoodCallLeadArrayIntoGoodCallLeadsDB(object):
    def __init__(self, goodCallLeadArray):
        self.goodCallLeadArray = goodCallLeadArray
        self.db = SUDBConnect()

        self.title = goodCallLeadArray[0]
        self.resultPageLink = goodCallLeadArray[1]
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
