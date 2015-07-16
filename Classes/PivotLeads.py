from selenium import webdriver
from Classes.RipPage import RipPage
from Classes.CleanText import CleanText


class PivotLeads(object):
    def __init__(self, searchTerm, isTest=False):
        self.searchTerm = searchTerm
        self.isTest = isTest
        self.driver = webdriver.Firefox()
        self.base_url = 'http://pivot.cos.com/'

        self.arrayOfResultsPageArrays = []
        self.arrayOfPivotLeads = []

        self.driver.get(self.base_url + '/funding_main')
        self.driver.find_element_by_css_selector('form > #search-by-text').clear()
        self.driver.find_element_by_css_selector('form > #search-by-text').send_keys(self.searchTerm)
        self.driver.find_element_by_name('commit').click()
        self.driver.implicitly_wait(2)

    def processSearchResultsAndMakeLeadArray(self):
        self.getTitlesAndLinksFromSearchResults()

        if self.isTest != True:
            isThereNextPage = self.checkIfNextPage()
            pageCount = 2
            while isThereNextPage == True and pageCount <= 10:
                self.goToNextPage()
                self.getTitlesAndLinksFromSearchResults()
                isThereNextPage = self.checkIfNextPage()
                pageCount += 1

        for singleArray in self.arrayOfResultsPageArrays:
            self.makeLeadArrayAndAddToGrantForwardLeads(singleArray)

        self.driver.quit()

        return self.arrayOfPivotLeads

    def getTitlesAndLinksFromSearchResults(self):
        self.arrayOfTitles = self.driver.find_elements_by_xpath("//a[@class = 'pivot_track_link results-title-link']")
        self.arrayOfResultsPagesLinks = []

        for i in self.arrayOfTitles:
            self.arrayOfResultsPagesLinks.append(i.get_attribute('href'))

        for i in range(len(self.arrayOfTitles)):
            title = self.arrayOfTitles[i].text
            resultPageLink = self.arrayOfResultsPagesLinks[i]
            singleResultArray = [title, resultPageLink]
            self.arrayOfResultsPageArrays.append(singleResultArray)

    def makeLeadArrayAndAddToGrantForwardLeads(self, singleArray):
        pass

    def checkIfNextPage(self):
        checkNextPage = self.driver.find_elements_by_link_text('Next')
        if checkNextPage != []:
            return True
        else:
            return False

    def goToNextPage(self):
        self.driver.find_element_by_link_text('Next').click()
        self.driver.implicitly_wait(2)

    def checkIfElementExists(self, xpath):
        checkElementExists = self.driver.find_elements_by_xpath(xpath)
        if checkElementExists != []:
            return True
        else:
            return False




PivotLeads('linguistics')

