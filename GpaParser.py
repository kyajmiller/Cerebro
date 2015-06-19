import re


class Parser(object):
    def __init__(self, scholarshipid, scholarshippackageid, stringToScan, reToUse):
        self.valueToSpan = stringToScan
        self.reToUse = reToUse
        self.result = ""

    def getValueToSpan(self):
        return self.valueToSpan.lower()

    def getReToUse(self):
        return self.reToUse

    def result(self):
        return self.result

    def __str__(self):
        return "%s is a %s" % (self.valueToSpan, self.reToUse)

    def getResult(self):
        return

    def parse(self):
        print(re.search(self.getReToUse(), self.getValueToSpan()))
        result = re.search(self.getReToUse(), self.getValueToSpan())
    def updateDatabase(self,databasecursor):
        print('test')

class SPRC(object):
    def __init__(self, scholarshippackageid, attributeid, requirementtype, requirementvalue):
        self.requirementvalue = requirementvalue
        self.requirementtype = requirementtype
        self.attributeid = attributeid
        self.scholarshippackageid = scholarshippackageid


ga =Parser(10,11,'this is a test','test')
print(ga.result)
