import re
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
        resultsPagesLinks = self.getResultsPagesLinksList()

    def loopThroughResultsPages(self):
        self.getResultsOnCurrentPage()

        nextPageExists = self.checkIfNextPage()
        while nextPageExists:
            self.goToNextPage()
            self.getResultsOnCurrentPage()
            nextPageExists = self.checkIfNextPage()

    def getInfoFromResultPage(self, resultPageLink):
        self.driver.get(resultPageLink)
        self.driver.implicitly_wait(2)

        description = ''

        if self.checkIfElementExists():
            pass

    def getTitlesList(self):
        titlesList = []

        titlesDivs = self.driver.find_elements_by_xpath("//div[@class='main-details clearfix']/h2/a")
        for title in titlesDivs:
            titlesList.append(CleanText.cleanALLtheText(title.get_attribute('textContent')))

        return titlesList

    def getResultsPagesLinksList(self):
        resultsPagesUrls = []

        moreInfoDivs = self.driver.find_elements_by_xpath(
            "//div[@class='one-card-actions']/a[@class='action-button info']")
        for moreInfoDiv in moreInfoDivs:
            resultsPagesUrls.append(moreInfoDiv.get_attribute('href'))

        return resultsPagesUrls

    def getNumAwardsList(self):
        numAwardsList = []

        numAwardsDivs = self.driver.find_elements_by_xpath("//div[@class='award-count']")
        for awardDiv in numAwardsDivs:
            numAwardsList.append(
                CleanText.cleanALLtheText(re.sub('# Awards', '', awardDiv.get_attribute('textContent'))))

        return numAwardsList

    def getAmountsList(self):
        amountsList = []

        amountsDivs = self.driver.find_elements_by_xpath("//div[@class='amount']")
        for amountDiv in amountsDivs:
            amountsList.append(CleanText.cleanALLtheText(re.sub('Amount', '', amountDiv.get_attribute('textContent'))))

        return amountsList

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

    def checkIfElementExists(self, xpath):
        checkElementExists = self.driver.find_elements_by_xpath(xpath)
        if checkElementExists != []:
            return True
        else:
            return False


GoodCallLeads()
