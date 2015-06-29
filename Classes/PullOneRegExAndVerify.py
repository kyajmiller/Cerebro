from Classes.Parser import Parser
from Classes.SUDBConnect import SUDBConnect
from Classes.DatabaseHelper import DatabaseHelper


class PullOneRegExAndVerify(Parser, SUDBConnect):
    def __init__(self, stringToScan, attributeId):

        self.attributeId = attributeId
        self.IsMatched = False
        self.stringToScan = stringToScan
        self.searchCriteria = DatabaseHelper.getOnlyOneRegex(self.attributeId)
        Parser.__init__(self, stringToScan, self.searchCriteria)
        self.IsMatched = self.doesMatchExist()
