import re
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

    def getResultsOnCurrentPage(self):
        titlesList = self.getTitlesList()
        urlsList = self.getUrlsList()
        deadlinesList = self.getDeadlinesList()
        amountsList = self.getAmountsList()

    def getTitlesList(self):
        titlesList = []

        titlesDivs = self.driver.find_elements_by_xpath("//h2/a")
        for title in titlesDivs:
            titlesList.append(title.get_attribute('textContent'))

        titlesList = [CleanText.cleanALLtheText(title) for title in titlesList]
        return titlesList

    def getUrlsList(self):
        urlsList = []

        urlsDivs = self.driver.find_elements_by_xpath("//h2/a")
        for url in urlsDivs:
            urlsList.append(url.get_attribute('href'))

        return urlsList

    def getDeadlinesList(self):
        deadlinesList = []

        deadlinesDivs = self.driver.find_elements_by_xpath("//span[@class='due']")
        for deadline in deadlinesDivs:
            deadlinesList.append(deadline.get_attribute('textContent'))

        deadlinesList = [re.sub('Due:', '', deadline) for deadline in deadlinesList]
        deadlinesList = [CleanText.cleanALLtheText(deadline) for deadline in deadlinesList]
        return deadlinesList

    def getAmountsList(self):
        amountsList = []

        amountsDivs = self.driver.find_elements_by_xpath("//span[@class='amount']")
        for amount in amountsDivs:
            amountsList.append(amount.get_attribute('textContent'))

        amountsList = [re.sub('Amount:', '', amount) for amount in amountsList]
        amountsList = [CleanText.cleanALLtheText(amount) for amount in amountsList]
        return amountsList

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
