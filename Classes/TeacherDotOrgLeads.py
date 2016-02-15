from selenium import webdriver
from Classes.CleanText import CleanText
from Classes.RipPage import RipPage


class TeacherDotOrgLeads(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'http://www.teacher.org/scholarships-grants/'
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(2)

        self.teacherDotOrgLeadArrays = []

    def getLeads(self):
        pass

    def getTitleDivs(self):
        pass


TeacherDotOrgLeads()
