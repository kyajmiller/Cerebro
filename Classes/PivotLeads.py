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

        for singleResultArray in self.arrayOfResultsPageArrays:
            self.makeLeadArrayAndAddToGrantForwardLeads(singleResultArray)

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

    def makeLeadArrayAndAddToGrantForwardLeads(self, singleResultArray):
        name = CleanText.cleanALLtheText(singleResultArray[0])
        url = singleResultArray[1]
        resultPageInfo = self.goToResultPageAndPullInformation(url)

        keyword = CleanText.cleanALLtheText(self.searchTerm)
        abstract = CleanText.cleanALLtheText(resultPageInfo[6])
        sponsor = CleanText.cleanALLtheText(resultPageInfo[1])
        amount = CleanText.cleanALLtheText(resultPageInfo[2])
        applicantType = CleanText.cleanALLtheText(resultPageInfo[3])
        citizenshipResidency = CleanText.cleanALLtheText(resultPageInfo[4])
        activityLocation = CleanText.cleanALLtheText(resultPageInfo[5])
        eligibility = CleanText.cleanALLtheText(resultPageInfo[7])
        categories = CleanText.cleanALLtheText(resultPageInfo[8])
        sourceWebsite = resultPageInfo[0]
        sourceText = CleanText.cleanALLtheText(RipPage.getPageSource(sourceWebsite))

        singleLeadArray = [keyword, url, name, abstract, sponsor, amount, applicantType, citizenshipResidency, activityLocation, eligibility, categories, sourceWebsite, sourceText]

        self.arrayOfPivotLeads.append(singleLeadArray)

    def goToResultPageAndPullInformation(self, resultPageLink):
        self.driver.get(resultPageLink)
        self.driver.implicitly_wait(2)
        sourceWebsite = ''
        sponsor = ''
        amount = ''
        applicantType = ''
        citizenshipResidency = ''
        activityLocation = ''
        abstract = ''
        eligibility = ''
        categories = ''

        if self.checkIfElementExists("//a[@title = 'Web page opens in new window']"):
            sourceWebsiteDiv = self.driver.find_element_by_xpath("//a[@title = 'Web page opens in new window']")
            sourceWebsite = sourceWebsiteDiv.get_attribute('href')

        if self.checkIfElementExists("//div[@class = 'span2']/span[text() = 'Sponsor']/../../div[@class = 'span6']"):
            sponsorDiv = self.driver.find_element_by_xpath("//div[@class = 'span2']/span[text() = 'Sponsor']/../../div[@class = 'span6']")
            sponsor = sponsorDiv.get_attribute('textContent')

        if self.checkIfElementExists("//div[@class = 'span2']/span[text() = 'Amount']/../../div[@class = 'span6']"):
            amountDiv = self.driver.find_element_by_xpath("//div[@class = 'span2']/span[text() = 'Amount']/../../div[@class = 'span6']")
            amount = amountDiv.get_attribute('textContent')

        if self.checkIfElementExists("//div[@class = 'span2']/span[text() = 'Applicant Type']/../../div[@class = 'span5']"):
            applicantTypeDiv = self.driver.find_element_by_xpath("//div[@class = 'span2']/span[text() = 'Applicant Type']/../../div[@class = 'span5']")
            applicantType = applicantTypeDiv.get_attribute('textContent')

        if self.checkIfElementExists("//div[@class = 'span2']/span[text() = 'Citizenship or Residency']/../../div[@class = 'span6']"):
            citizenshipResidencyDiv = self.driver.find_element_by_xpath("//div[@class = 'span2']/span[text() = 'Citizenship or Residency']/../../div[@class = 'span6']")
            citizenshipResidency = citizenshipResidencyDiv.get_attribute('textContent')

        if self.checkIfElementExists("//div[@class = 'span2']/span[text() = 'Activity location']/../../div[@class = 'span6']"):
            activityLocationDiv = self.driver.find_element_by_xpath("//div[@class = 'span2']/span[text() = 'Activity location']/../../div[@class = 'span6']")
            activityLocation = activityLocationDiv.get_attribute('textContent')

        if self.checkIfElementExists("//div[@class = 'span2']/span[text() = 'Abstract']/../../div[@class = 'span6']"):
            abstractDiv = self.driver.find_element_by_xpath("//div[@class = 'span2']/span[text() = 'Abstract']/../../div[@class = 'span6']")
            abstract = abstractDiv.get_attribute('textContent')

        if self.checkIfElementExists("//div[@class = 'span2']/span[text() = 'Eligibility']/../../div[@class = 'span6']"):
            eligibilityDiv = self.driver.find_element_by_xpath("//div[@class = 'span2']/span[text() = 'Eligibility']/../../div[@class = 'span6']")
            eligibility = eligibilityDiv.get_attribute('textContent')

        if self.checkIfElementExists("//div[@class = 'span2']/span[text() = 'Keywords']/../../div[@class = 'span6']"):
            categoriesDiv = self.driver.find_element_by_xpath("//div[@class = 'span2']/span[text() = 'Keywords']/../../div[@class = 'span6']")
            categories = categoriesDiv.get_attribute('textContent')

        resultPageInfo = [sourceWebsite, sponsor, amount, applicantType, citizenshipResidency, activityLocation, abstract, eligibility, categories]

        return resultPageInfo

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