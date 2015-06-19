from Classes.Parser import Parser

class ClassStanding(Parser):
    def __init__(self, stringToScan, classStandingOptions):
        self.classStandingOptions = classStandingOptions
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan.lower(), self.classStandingOptions)
        self.resultList = []

    def checkContext(self, contextCriteria):
        contextChecker = Parser(self.stringToScan.lower(), contextCriteria)
        return contextChecker.doesMatchExist()

    def checkClassStandingOptions(self):
        if self.doesMatchExist():
            return self.getResult()
    
    def checkYear(self):
        findYear = Parser(self.stringToScan.lower(), '1st|2nd|3rd|4th|5th|6th')
        if findYear.doesMatchExist():
            years = []
            for i in findYear.getResult():
                years.append('%s Year' % i)
            return years

    def checkUpperDivision(self):
        if self.checkContext('upper\-division|upper\sdivision'):
            upperdivision = ['junior', 'senior']
            return upperdivision

    def checkGraduate(self):
        if not self.checkContext('graduate\sfrom|graduates'):
            findGraduate = Parser(self.stringToScan.lower(), '^graduate|\sgraduate')
            if findGraduate.doesMatchExist():
                return ['graduate']

    def checkMedicalStudent(self):
        if self.checkContext('medical|medicine|md') and not self.checkContext('upper\-division|upper\sdivision|undergraduate|biomedical'):
            return ['medical school student']

    def checkMastersStudent(self):
        if self.checkContext("masters|master's"):
            return ['masters level graduate']

    def checkPhdStudent(self):
        if self.checkContext('ph\.d|phd|ph\sd'):
            return ['ph.d. level graduate']

    def getClassStanding(self):
        if self.checkClassStandingOptions() != None:
            for i in self.checkClassStandingOptions():
                self.resultList.append(i)

        if self.checkYear() != None:
            for i in self.checkYear():
                self.resultList.append(i)

        if self.checkUpperDivision() != None:
            for i in self.checkUpperDivision():
                self.resultList.append(i)

        if self.checkGraduate() != None:
            for i in self.checkGraduate():
                self.resultList.append(i)

        if self.checkMedicalStudent() != None:
            for i in self.checkMedicalStudent():
                self.resultList.append(i)

        if self.checkMastersStudent() != None:
            for i in self.checkMastersStudent():
                self.resultList.append(i)

        if self.checkPhdStudent() != None:
            for i in self.checkPhdStudent():
                self.resultList.append(i)

        self.resultList = list(set(self.resultList))
        return self.resultList
