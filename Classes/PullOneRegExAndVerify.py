from Classes.Parser import Parser
from Classes.SUDBConnect import SUDBConnect


class PullOneRegExAndVerify(Parser, SUDBConnect):
    def __init__(self, stringToScan, attributeId):

        self.attributeId = attributeId
        self.IsMatched = False
        self.stringToScan = stringToScan
        DB = SUDBConnect()
        rows = DB.getRows(' select ' + str(attributeId) + ' , regEx from RegExHelpers')
        self.searchCriteria = ''
        if len(rows) > 0:
            self.searchCriteria = rows[0].regEx
        else:
            self.searchCriteria = ''
        Parser.__init__(self, stringToScan, self.searchCriteria)
        self.IsMatched = self.doesMatchExist()
