from selenium import webdriver
from Classes.CleanText import CleanText
from Classes.RipPage import RipPage


class GoodCallLeads(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://www.goodcall.com/"

        self.driver.get(self.base_url + "scholarships/search")
        self.driver.implicitly_wait(2)

        self.loopThroughResultsPages()

    def getResultsOnCurrentPage(self):
        titlesList = self.getTitlesList()


    def loopThroughResultsPages(self):
        nextPageExists = self.checkIfNextPage()
        while nextPageExists:
            self.goToNextPage()
            nextPageExists = self.checkIfNextPage()

    def getTitlesList(self):
        titlesList = []

        titlesDivs = self.driver.find_elements_by_xpath("//div[@class='main-details clearfix']/h2/a")
        for title in titlesDivs:
            titlesList.append(title.get_attribute('textContent'))

        titlesList = [CleanText.cleanALLtheText(title) for title in titlesList]
        return titlesList

    def goToNextPage(self):
        if self.checkIfNextPage():
            self.driver.find_element_by_link_text("Next Page").click()
            self.driver.implicitly_wait(2)

    def checkIfNextPage(self):
        nextPageButton = self.driver.find_elements_by_link_text('Next Page')
        if nextPageButton != []:
            return True
        else:
            return False


GoodCallLeads()
