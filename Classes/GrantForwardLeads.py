from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from Classes.CleanText import CleanText
from Classes.RipPage import RipPage


class GrantForwardLeads(object):
    def __init__(self, searchTerm):
        self.searchTerm = searchTerm
        self.driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        self.base_url = 'https://www.grantforward.com/'

        self.arrayOfGrantForwardLeads = []
        self.arrayOfResultsPageArrays = []

        self.driver.get(self.base_url + '/index')
        self.driver.find_element_by_id('keyword').clear()
        self.driver.find_element_by_id('keyword').send_keys(self.searchTerm)
        self.driver.find_element_by_xpath('//div[2]/button').click()
        self.driver.implicitly_wait(2)

    def processSearchResultsAndMakeLeadArray(self):
        self.getTitlesAndLinksFromSearchResults()

        if self.arrayOfResultsPagesLinks != []:
            isThereNextPage = self.checkIfNextPage()
            pageCount = 2
            while isThereNextPage == True and pageCount <= 10:
                self.goToNextPage()
                self.getTitlesAndLinksFromSearchResults()
                isThereNextPage = self.checkIfNextPage()
                pageCount += 1

            for singleResultArray in self.arrayOfResultsPageArrays:
                self.makeLeadArrayAndAddToGrantForwardLeads(singleResultArray)

        self.driver.quit()

        return self.arrayOfGrantForwardLeads

    def getTitlesAndLinksFromSearchResults(self):
        self.arrayOfTitles = self.driver.find_elements_by_xpath("//a[@class = 'grant-url']")
        self.arrayOfResultsPagesLinks = []
        for i in self.arrayOfTitles:
            self.arrayOfResultsPagesLinks.append(i.get_attribute('href'))

        for i in range(len(self.arrayOfTitles)):
            title = self.arrayOfTitles[i].text
            resultPageLink = self.arrayOfResultsPagesLinks[i]
            singleResultArray = [title, resultPageLink]
            self.arrayOfResultsPageArrays.append(singleResultArray)

    def makeLeadArrayAndAddToGrantForwardLeads(self, singleResultArray):
        name = CleanText.cleanALLtheText(singleResultArray[0])
        url = singleResultArray[1]
        resultPageInfo = self.goToResultPageAndPullInformation(url)

        keyword = CleanText.cleanALLtheText(self.searchTerm)
        description = resultPageInfo[0]
        sponsor = resultPageInfo[1]
        amount = resultPageInfo[2]
        eligibility = resultPageInfo[3]
        submissionInfo = resultPageInfo[4]
        categories = resultPageInfo[5]
        sourceWebsite = resultPageInfo[6]
        sourceText = resultPageInfo[7]

        singleLeadArray = [keyword, url, name, description, sponsor, amount, eligibility, submissionInfo, categories,
                           sourceWebsite, sourceText]

        self.arrayOfGrantForwardLeads.append(singleLeadArray)

    def goToResultPageAndPullInformation(self, resultPageLink):
        self.driver.get(resultPageLink)
        self.driver.implicitly_wait(2)
        description = ''
        sponsor = ''
        amount = ''
        eligibility = ''
        submissionInfo = ''
        categories = ''
        sourceWebsite = ''
        sourceText = ''

        if self.checkIfElementExists("//div[@id = 'field-description']/div[@class = 'content-collapsed']"):
            descriptionDiv = self.driver.find_element_by_xpath(
                "//div[@id = 'field-description']/div[@class = 'content-collapsed']")
            description = CleanText.cleanALLtheText(descriptionDiv.get_attribute('textContent'))

        if self.checkIfElementExists("//div[@class = 'sponsor-content']/div/a"):
            sponsorDiv = self.driver.find_element_by_xpath("//div[@class = 'sponsor-content']/div/a")
            sponsor = CleanText.cleanALLtheText(sponsorDiv.get_attribute('textContent'))

        if self.checkIfElementExists("//div[@id = 'field-amount_info']/div[@class = 'content-collapsed']"):
            amountDiv = self.driver.find_element_by_xpath(
                "//div[@id = 'field-amount_info']/div[@class = 'content-collapsed']")
            amount = CleanText.cleanALLtheText(amountDiv.get_attribute('textContent'))

        if self.checkIfElementExists("//div[@id = 'field-eligibility']/div[@class = 'content-collapsed']"):
            eligibilityDiv = self.driver.find_element_by_xpath(
                "//div[@id = 'field-eligibility']/div[@class = 'content-collapsed']")
            eligibility = CleanText.cleanALLtheText(eligibilityDiv.get_attribute('textContent'))

        if self.checkIfElementExists("//div[@id = 'field-submission_info']/div[@class = 'content-collapsed']"):
            submissionInfoDiv = self.driver.find_element_by_xpath(
                "//div[@id = 'field-submission_info']/div[@class = 'content-collapsed']")
            submissionInfo = CleanText.cleanALLtheText(submissionInfoDiv.get_attribute('textContent'))

        if self.checkIfElementExists("//div[@id = 'field-subjects']/ul"):
            categoriesDiv = self.driver.find_element_by_xpath("//div[@id = 'field-subjects']/ul")
            categories = CleanText.cleanALLtheText(categoriesDiv.get_attribute('textContent'))

        if self.checkIfElementExists("//a[@class = 'source-link btn btn-warning']"):
            sourceWebsiteDiv = self.driver.find_element_by_xpath("//a[@class = 'source-link btn btn-warning']")
            sourceWebsite = sourceWebsiteDiv.get_attribute('href')
            sourceText = CleanText.cleanALLtheText(RipPage.getPageSource(sourceWebsite))

        resultPageInfo = [description, sponsor, amount, eligibility, submissionInfo, categories, sourceWebsite,
                          sourceText]
        return resultPageInfo

    def checkIfNextPage(self):
        checkNextPage = self.driver.find_elements_by_xpath("(//a[contains(text(), 'Next')])[1]")
        if checkNextPage != []:
            return True
        else:
            return False

    def goToNextPage(self):
        try:
            self.driver.find_element_by_xpath("(//a[contains(text(), 'Next')])[1]").click()
            self.driver.implicitly_wait(2)
        except ElementNotVisibleException:
            self.driver.implicitly_wait(2)

    def checkIfElementExists(self, xpath):
        checkElementExists = self.driver.find_elements_by_xpath(xpath)
        if checkElementExists != []:
            return True
        else:
            return False
