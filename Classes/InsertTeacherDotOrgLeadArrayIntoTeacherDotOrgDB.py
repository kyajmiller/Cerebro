from Classes.SUDBConnect import SUDBConnect
import re
import time


class InsertTeacherDotOrgLeadArrayIntoTeacherDotOrgDB(object):
    def __init__(self, teacherDotOrgLeadArray, fundingClassification, badScholarshipClassification):
        self.teacherDotOrgLeadArray = teacherDotOrgLeadArray
        self.fundingClassification = fundingClassification
        self.badScholarshipClassification = badScholarshipClassification
        self.db = SUDBConnect()
        self.fileSystemDB = SUDBConnect(destination='filesystem')

        self.name = teacherDotOrgLeadArray[0]
        self.description = teacherDotOrgLeadArray[1]
        self.requirements = teacherDotOrgLeadArray[2]
        self.sourceWebsite = teacherDotOrgLeadArray[3]
        self.sourceText = teacherDotOrgLeadArray[4]
