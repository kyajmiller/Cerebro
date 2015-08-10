import re
from selenium import webdriver
from Classes.RipPage import RipPage
from Classes.CleanText import CleanText


class UnigoLeads(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = "https://www.unigo.com/"
        self.driver.get(self.base_url + "match/scholarshipresult#/login")
        self.driver.implicitly_wait(2)

        self.driver.find_element_by_name('UserName').clear()
        self.driver.find_element_by_name('UserName').send_keys('crawlyjones@gmail.com')
        self.driver.find_element_by_name('password').clear()
        self.driver.find_element_by_name('password').send_keys('sasgcoders626')
        self.driver.find_element_by_css_selector('button.btn-primary').click()
        self.driver.implicitly_wait(2)

    def getLeads(self):
        self.expandSeeMore()

    def expandSeeMore(self):
        self.seeMoreButtonExistence = ''
        if self.checkIfSeeMoreButtonExists():
            self.seeMoreButtonExistence = True
            while self.seeMoreButtonExistence:
                self.driver.find_element_by_xpath("//a[@data-bind='click: showMoreScholarships']").click()
                self.seeMoreButtonExistence = self.checkIfSeeMoreButtonExists()

    def checkIfSeeMoreButtonExists(self):
        seeMoreButton = self.driver.find_elements_by_xpath("//a[@data-bind='click: showMoreScholarships']")
        if seeMoreButton != []:
            return True
        else:
            return False


UnigoLeads().getLeads()
