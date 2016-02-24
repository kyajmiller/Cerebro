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
        self.driver.find_element_by_xpath(
            "//input[@class='input-lg form-control js-basic-search-text ui-autocomplete-input']").clear()
        self.driver.find_element_by_xpath(
            "//input[@class='input-lg form-control js-basic-search-text ui-autocomplete-input']").send_keys(
            self.searchTerm)
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
        deadline = resultPageInfo[8]

        singleLeadArray = [keyword, url, name, description, sponsor, amount, eligibility, submissionInfo, categories,
                           sourceWebsite, sourceText, deadline]

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
        deadline = ''

        if self.checkIfElementExists("//div[@id = 'field-description']/div[@class = 'content-collapsed']"):
            description = self.driver.find_element_by_xpath(
                "//div[@id = 'field-description']/div[@class = 'content-collapsed']").get_attribute('textContent')
            description = CleanText.cleanALLtheText(description)

        if self.checkIfElementExists("//div[@class = 'sponsor-content']/div/a"):
            sponsor = self.driver.find_element_by_xpath("//div[@class = 'sponsor-content']/div/a").get_attribute(
                'textContent')
            sponsor = CleanText.cleanALLtheText(sponsor)

        if self.checkIfElementExists("//div[@id = 'field-amount_info']/div[@class = 'content-collapsed']"):
            amount = self.driver.find_element_by_xpath(
                "//div[@id = 'field-amount_info']/div[@class = 'content-collapsed']").get_attribute('textContent')
            amount = CleanText.cleanALLtheText(amount)

        if self.checkIfElementExists("//div[@id = 'field-eligibility']/div[@class = 'content-collapsed']"):
            eligibility = self.driver.find_element_by_xpath(
                "//div[@id = 'field-eligibility']/div[@class = 'content-collapsed']").get_attribute('textContent')
            eligibility = CleanText.cleanALLtheText(eligibility)

        if self.checkIfElementExists("//div[@id = 'field-submission_info']/div[@class = 'content-collapsed']"):
            submissionInfo = self.driver.find_element_by_xpath(
                "//div[@id = 'field-submission_info']/div[@class = 'content-collapsed']").get_attribute('textContent')
            submissionInfo = CleanText.cleanALLtheText(submissionInfo)

        if self.checkIfElementExists("//div[@id = 'field-subjects']/ul"):
            categories = self.driver.find_element_by_xpath("//div[@id = 'field-subjects']/ul").get_attribute(
                'textContent')
            categories = CleanText.cleanALLtheText(categories)

        if self.checkIfElementExists("//a[@class = 'source-link btn btn-warning']"):
            sourceWebsite = self.driver.find_element_by_xpath(
                "//a[@class = 'source-link btn btn-warning']").get_attribute('href')
            sourceText = CleanText.cleanALLtheText(RipPage.getPageSource(sourceWebsite))

        if self.checkIfElementExists("//div[@class='table-responsive deadline-tables']/table/tbody"):
            deadline = self.driver.find_element_by_xpath(
                "//div[@class='table-responsive deadline-tables']/table/tbody").get_attribute('textContent')
            deadline = CleanText.cleanALLtheText(deadline)

        resultPageInfo = [description, sponsor, amount, eligibility, submissionInfo, categories, sourceWebsite,
                          sourceText, deadline]
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
