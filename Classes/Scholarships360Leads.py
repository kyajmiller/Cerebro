from selenium import webdriver
from Classes.CleanText import CleanText
from Classes.RipPage import RipPage


class Scholarships360Leads(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'https://scholarships360.org/'

        self.driver.get(self.base_url + 'discover-scholarships')
        self.driver.implicitly_wait(2)

        self.loopThroughResultsListPages()

    def loopThroughResultsListPages(self):
        nextPageExists = self.checkIfNextPage()
        while nextPageExists:
            self.goToNextPage()
            nextPageExists = self.checkIfNextPage()

    def goToNextPage(self):
        if self.checkIfNextPage():
            self.driver.find_element_by_xpath("//a[@class='next page-numbers']").click()
            self.driver.implicitly_wait(2)

    def checkIfNextPage(self):
        nextPageDiv = self.driver.find_elements_by_xpath("//a[@class='next page-numbers']")
        if nextPageDiv != []:
            return True
        else:
            return False


Scholarships360Leads()
