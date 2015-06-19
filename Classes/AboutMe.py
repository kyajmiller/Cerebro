from Classes.Parser import Parser

class AboutMe(Parser):
    def __init__(self, stringToScan, aboutMeAttributes):
        self.aboutMeAttributes = aboutMeAttributes
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan.lower(), self.aboutMeAttributes)
        self.resultList = []

    def getAboutMe(self):
        if self.doesMatchExist():
            for i in self.getResult():
                self.resultList.append(i)

        self.resultList = list(set(self.resultList))
        return self.resultList