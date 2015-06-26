from Classes.CleanText import CleanText
from Classes.GPA import GPA
from Classes.Majors import Majors
from Classes.UACollege import UACollege


class ScanText(object):
    def __init__(self, textToScan):
        self.textToScan = textToScan
        self.textLines = []

    def prepareText(self):
        self.textToScan = CleanText.cleanALLtheText(self.textToScan)
        self.textLines = self.textToScan.split('\n')
        return self.textLines

    def doGPAParser(self):
        for line in self.textLines:
            parseGPA = GPA(line)
            if parseGPA.getGPA() != '':
                return parseGPA.getScholarshipPackageRequirementFormat()

    def doMajorsParser(self):
        for line in self.textLines:
            parseMajors = Majors(line, Majors.majorsListForTesting())
            if parseMajors.getMajors() != '':
                return parseMajors.getScholarshipPackageRequirementFormat()

    def doUACollege(self):
        for line in self.textLines:
            parseUACollege = UACollege(line, UACollege.uaCollegesListForTesting())
            if parseUACollege.getUACollege() != '':
                return parseUACollege.getScholarshipPackageRequirementFormat()
