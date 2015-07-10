import re
from selenium import webdriver
from Classes.CleanText import CleanText


class GoogleLeads(object):
    def __init__(self, searchTerm):
        self.searchTerm = searchTerm
        self.driver = webdriver.Firefox()
        self.base_url = 'https://www.google.com/'
        self.arrayOfTitles = []
        self.arrayOfLinks = []
        self.arrayOfDescriptions = []
        self.arrayOfGoogleLeads = []
        self.driver.get(self.base_url + '/?gws_rd=ssl')
        self.driver.find_element_by_id('lst-ib').clear()
        self.driver.find_element_by_id('lst-ib').send_keys(self.searchTerm)
        self.driver.find_element_by_name('btnG').click()
        self.driver.implicitly_wait(2)

    def processSearchResultsAndReturnArrayOfGoogleLeads(self):
        self.getGoogleLeadsArrays()

        self.driver.quit()

        return self.arrayOfGoogleLeads

    def doSingleArraysForSameNumberElements(self):
        for i in range(len(self.arrayOfTitles)):
            elementTitle = self.arrayOfTitles[i].text
            elementLink = self.arrayOfLinks[i]
            elementDescription = self.arrayOfDescriptions[i].text

            singleResultArray = [elementTitle, elementLink,
                                 CleanText.replaceSingleQuotesWithTwoSingleQuotes(elementDescription)]
            self.arrayOfGoogleLeads.append(singleResultArray)

    def doSingleArraysForUnevenNumberElements(self):
        stringOfMatchedDivParts = self.driver.find_elements_by_xpath(
            "//h3[contains(concat(' ', @class, ' '), 'r')]/following-sibling::div/div")
        for element in stringOfMatchedDivParts:
            elementParts = element.text.split('\n', 2)
            elementTitle = ''
            elementLink = ''
            elementDescription = ''

            if len(elementParts) == 3:
                elementLink = elementParts[0]
                elementTitle = elementParts[1]
                elementDescription = elementParts[2]
            elif len(elementParts) == 2:
                elementLink = elementParts[0]
                elementDescription = elementParts[1]

            if not re.search('^https?://', elementLink):
                elementLink = 'http://' + elementLink

            singleResultArray = [elementTitle, elementLink,
                                 CleanText.replaceSingleQuotesWithTwoSingleQuotes(elementDescription)]
            self.arrayOfGoogleLeads.append(singleResultArray)

    def checkIfNextPage(self):
        checkIfNextButtonExists = self.driver.find_elements_by_xpath("//a[@id='pnnext']/span[2]")
        if checkIfNextButtonExists != []:
            return True
        else:
            return False

    def goToNextPage(self):
        self.driver.find_element_by_xpath("//a[@id='pnnext']/span[2]").click()
        self.driver.implicitly_wait(2)

    def getGoogleLeadsArrays(self):
        self.arrayOfTitles = self.driver.find_elements_by_xpath("//h3[contains(concat(' ', @class, ' '), 'r')]/a")
        for i in self.arrayOfTitles:
            self.arrayOfLinks.append(i.get_attribute('href'))
        self.arrayOfDescriptions = self.driver.find_elements_by_xpath(
            "//span[contains(concat(' ', @class, ' '), 'st')]")

        if len(self.arrayOfTitles) == len(self.arrayOfLinks) == len(self.arrayOfDescriptions):
            self.doSingleArraysForSameNumberElements()
        else:
            self.doSingleArraysForUnevenNumberElements()
