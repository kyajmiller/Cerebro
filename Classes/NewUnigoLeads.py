from selenium import webdriver
from Classes.RipPage import RipPage
from Classes.CleanText import CleanText


class UnigoLeads(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = "https://www.unigo.com/"
        self.driver.get(self.base_url + "match/scholarshipresult#/login")
        self.driver.implicitly_wait(2)


UnigoLeads()
