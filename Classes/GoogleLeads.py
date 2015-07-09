import re
from selenium import webdriver


class GoogleLeads(object):
    def __init__(self, searchTerm):
        self.searchTerm = searchTerm
        self.driver = webdriver.Firefox()
        self.base_url = 'https://www.google.com/'
        self.arrayOfTitles = []
        self.arrayOfLinks = []
        self.arrayOfDescriptions = []
        self.arrayOfGoogleLeads = []

    def goToGoogleAndGetResults(self):
        self.driver.get(self.base_url + '/?gws_rd=ssl')
        self.driver.find_element_by_id('lst-ib').clear()
        self.driver.find_element_by_id('lst-ib').send_keys(self.searchTerm)
        self.driver.find_element_by_name('btnG').click()
        self.driver.implicitly_wait(2)

        self.arrayOfTitles = self.driver.find_elements_by_xpath("//h3[contains(concat(' ', @class, ' '), 'r')]/a")
        for i in self.arrayOfTitles:
            self.arrayOfLinks.append(i.get_attribute('href'))
        self.arrayOfDescriptions = self.driver.find_elements_by_xpath(
            "//span[contains(concat(' ', @class, ' '), 'st')]")

        if len(self.arrayOfTitles) == len(self.arrayOfLinks) == len(self.arrayOfDescriptions):
            self.doSingleArraysForSameNumberElements()
        else:
            self.doSingleArraysForUnevenNumberElements()

        self.driver.quit()

        return self.arrayOfGoogleLeads

    def doSingleArraysForSameNumberElements(self):
        for i in range(len(self.arrayOfTitles)):
            elementTitle = self.arrayOfTitles[i].text
            elementLink = self.arrayOfLinks[i]
            elementDescription = self.arrayOfDescriptions[i].text

            singleResultArray = [elementTitle, elementLink, elementDescription]
            self.arrayOfGoogleLeads.append(singleResultArray)

    def doSingleArraysForUnevenNumberElements(self):
        arrayOfMatchedDivParts = self.driver.find_elements_by_xpath(
            "//h3[contains(concat(' ', @class, ' '), 'r')]/following-sibling::div/div")
        for element in arrayOfMatchedDivParts:
            elementParts = element.text.split('\n')
            elementLink = elementParts[0]
            if not re.search('http://|https://', elementLink):
                elementLink = 'http://' + elementLink
            elementTitle = elementParts[1]
            elementDescription = elementParts[2]

            singleResultArray = [elementTitle, elementLink, elementDescription]
            self.arrayOfGoogleLeads.append(singleResultArray)
