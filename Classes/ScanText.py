from Classes.CleanText import CleanText
from Classes.GPA import GPA
from Classes.Majors import Majors
from Classes.UACollege import UACollege


class ScanText(object):
    def __init__(self, textToScan):
        self.textToScan = textToScan
        self.textLines = []

    def cleanText(self):
        self.textToScan = CleanText.cleanALLtheText(self.textToScan)
        return self.textToScan

    def doGPAParser(self, line):
        parseGPA = GPA(line)
        if parseGPA.getGPA() != '':
            # print(parseGPA.getGPA())
            # print(parseGPA.getScholarshipPackageRequirementFormat().getStringValue())
            return parseGPA.getScholarshipPackageRequirementFormat()

    def doMajorsParser(self, line):
        parseMajors = Majors(line, Majors.majorsListForTesting())
        if parseMajors.getMajors() != '':
            # print(parseMajors.getMajors())
            # print(parseMajors.getScholarshipPackageRequirementFormat().getStringValue())
            return parseMajors.getScholarshipPackageRequirementFormat()

    def doUACollege(self, line):
        parseUACollege = UACollege(line, UACollege.uaCollegesListForTesting())
        if parseUACollege.getUACollege() != '':
            #print(parseUACollege.getUACollege())
            # print(parseUACollege.getScholarshipPackageRequirementFormat().getStringValue())
            return parseUACollege.getScholarshipPackageRequirementFormat()

    def prepareText(self):
        self.cleanText()
        self.textLines = self.textToScan.split('\n')

        return self.textLines

    def processText(self):
        self.textLines = self.prepareText()

        for line in self.textLines:
            self.doGPAParser(line)
            self.doMajorsParser(line)
            self.doUACollege(line)
