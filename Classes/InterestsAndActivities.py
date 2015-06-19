from Classes.Parser import Parser


class InterestsAndActivities(Parser):
    def __init__(self, stringToScan, interestsAndActivities):
        self.interestsAndActivities = interestsAndActivities
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan.lower(), self.interestsAndActivities)
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        return contextChecker.doesMatchExist()

    def getInterestsAndActivities(self):
        if self.checkContext(
                'interest|activity|career|hobby|hobbies|achievement|demonstrate|involve|activities|commit') and self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append(i)

        self.resultList = list(set(self.resultList))
        return self.resultList