from selenium import webdriver
from Classes.CleanText import CleanText


class GrantForwardLeads(object):
    def __init__(self, searchTerm):
        self.searchTerm = searchTerm
        self.driver = webdriver.Firefox()
        self.base_url = 'https://www.grantforward.com/'

        self.arrayOfTitles = []
        self.arrayOfResultsPagesLinks = []
        self.arrayOfDescriptionsDiv = []
        self.arrayOfDescriptionsText = []
        self.arrayOfWebsiteLinks = []
        self.arrayOfGrantForwardLeads = []
        self.arrayOfResultsPageArrays = []

        self.driver.get(self.base_url + '/index')
        self.driver.find_element_by_id('keyword').clear()
        self.driver.find_element_by_id('keyword').send_keys(self.searchTerm)
        self.driver.find_element_by_xpath('//div[2]/button').click()
        self.driver.implicitly_wait(2)

    def processSearchResultsAndMakeLeadArray(self):
        self.getTitlesAndLinksFromSearchResults()

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

        return self.arrayOfGrantForwardLeads

    def getTitlesAndLinksFromSearchResults(self):
        self.arrayOfTitles = self.driver.find_elements_by_xpath("//a[@class = 'grant-url']")
        self.arrayOfResultsPagesLinks = []
        for i in self.arrayOfTitles:
            self.arrayOfResultsPagesLinks.append(i.get_attribute('href'))
        self.arrayOfDescriptionsDiv = self.driver.find_elements_by_xpath("//div[@class = 'description']")
        for i in self.arrayOfDescriptionsDiv:
            self.arrayOfDescriptionsText.append(CleanText.cleanALLtheText(i.get_attribute('textContent')))

        for i in range(len(self.arrayOfTitles)):
            title = self.arrayOfTitles[i].text
            resultPageLink = self.arrayOfResultsPagesLinks[i]
            description = self.arrayOfDescriptionsText[i].strip()
            singleResultArray = [title, resultPageLink, description]
            self.arrayOfResultsPageArrays.append(singleResultArray)

    def makeLeadArrayAndAddToGrantForwardLeads(self, singleArray):
        title = singleArray[0]
        resultPageLink = singleArray[1]
        description = singleArray[2]
        sourceWebsiteLink = self.goToResultPageAndGetSourceWebsite(resultPageLink)

        singleLeadArray = [title, sourceWebsiteLink, description]

        self.arrayOfGrantForwardLeads.append(singleLeadArray)

    def goToResultPageAndGetSourceWebsite(self, resultPageLink):
        self.driver.get(resultPageLink)
        self.driver.implicitly_wait(2)

        sourceButtonDiv = self.driver.find_element_by_xpath("//a[@class = 'source-link btn btn-warning']")
        sourceWebsiteLink = sourceButtonDiv.get_attribute('href')
        return sourceWebsiteLink

    def checkIfNextPage(self):
        checkNextPage = self.driver.find_elements_by_xpath("(//a[contains(text(), 'Next')])[1]")
        if checkNextPage != []:
            return True
        else:
            return False

    def goToNextPage(self):
        self.driver.find_element_by_xpath("(//a[contains(text(), 'Next')])[1]").click()
        self.driver.implicitly_wait(2)