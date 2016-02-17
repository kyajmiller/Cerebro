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
