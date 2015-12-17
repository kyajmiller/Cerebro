import re
from selenium import webdriver
from Classes.CleanText import CleanText
from Classes.RipPage import RipPage


class FastWebLeads(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'http://www.fastweb.com/'

        self.driver.get(self.base_url)
        self.driver.find_element_by_xpath("//a[@class='login']").click()
        self.driver.find_element_by_id('login').clear()
        self.driver.find_element_by_id('login').send_keys('crawlyjones@gmail.com')
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys('sasgcoders')
        self.driver.find_element_by_id('user_form_submit').click()
        self.driver.implicitly_wait(2)

        # self.driver.find_element_by_link_text('See my matches').click()
        self.driver.find_element_by_css_selector("#primary_nav_scholarships > a > span.primary_link").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_css_selector("a.primary-button_140611 > span").click()
        self.driver.implicitly_wait(2)

        self.driver.find_element_by_link_text("All Matches").click()
        self.driver.implicitly_wait(2)

        self.resultPagesArrays = []
        self.fastWebLeads = []


FastWebLeads()
    '''

    def getLeads(self):
        self.loopThroughResultsListPages()

        for resultArray in self.resultPagesArrays:
            title = resultArray[0]
            url = resultArray[1]
            sponsor = resultArray[2]
            amount = resultArray[3]
            deadline = resultArray[4]

            self.makeLeadArray(title, url, sponsor, amount, deadline)

        self.driver.quit()
        return self.fastWebLeads

    def makeLeadArray(self, title, url, sponsor, amount, deadline):
        scholarshipPageArray = self.getInfoFromScholarshipPage(url)

        description = scholarshipPageArray[0]
        awardType = scholarshipPageArray[1]
        numAwards = scholarshipPageArray[2]
        majors = scholarshipPageArray[3]
        additionalInfo = scholarshipPageArray[4]
        sourceWebsite = scholarshipPageArray[5]
        sourceText = scholarshipPageArray[6]

        fastWebLead = [title, url, sponsor, amount, deadline, description, awardType, numAwards, majors, additionalInfo,
                       sourceWebsite, sourceText]
        self.fastWebLeads.append(fastWebLead)

    def getInfoFromScholarshipPage(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(2)

        description = ''
        awardType = ''
        numAwards = ''
        majors = ''
        additionalInfo = ''
        sourceWebsite = ''
        sourceText = ''

        if self.checkIfElementExists("//div[@class='description']"):
            description = self.driver.find_element_by_xpath("//div[@class='description']").get_attribute('textContent')
            description = CleanText.cleanALLtheText(description)

        if self.checkIfElementExists("//p[text() = 'Award Type: ']/following-sibling::p[@class='data']"):
            awardType = self.driver.find_element_by_xpath(
                "//p[text() = 'Award Type: ']/following-sibling::p[@class='data']").get_attribute('textContent')
            awardType = CleanText.cleanALLtheText(awardType)

        if self.checkIfElementExists("//p[text() = 'Awards Available: ']/following-sibling::p[@class='data']"):
            numAwards = self.driver.find_element_by_xpath(
                "//p[text() = 'Awards Available: ']/following-sibling::p[@class='data']").get_attribute('textContent')
            numAwards = CleanText.cleanALLtheText(numAwards)

        if self.checkIfElementExists("//p[text() = 'Fields of Study: ']/following-sibling::p[@class='data major']"):
            majors = self.driver.find_element_by_xpath(
                "//p[text() = 'Fields of Study: ']/following-sibling::p[@class='data major']").get_attribute(
                'textContent')
            majors = re.sub('All Fields of Study', '', majors)
            majors = CleanText.cleanALLtheText(majors)

        if self.checkIfElementExists("//p[text() = 'Additional Info: ']/following-sibling::p[@class='data major']"):
            additionalInfo = self.driver.find_element_by_xpath(
                "//p[text() = 'Additional Info: ']/following-sibling::p[@class='data major']").get_attribute(
                'textContent')
            additionalInfo = CleanText.cleanALLtheText(additionalInfo)

        if self.checkIfElementExists("//p[text() = 'Website: ']/following-sibling::p[@class='data']/a"):
            sourceWebsite = self.driver.find_element_by_xpath(
                "//p[text() = 'Website: ']/following-sibling::p[@class='data']/a").get_attribute('href')
            sourceText = RipPage.getPageSource(sourceWebsite)
            sourceText = CleanText.cleanALLtheText(sourceText)

        scholarshipPageInfoArray = [description, awardType, numAwards, majors, additionalInfo, sourceWebsite,
                                    sourceText]
        return scholarshipPageInfoArray

    def loopThroughResultsListPages(self):
        self.getResultsOnCurrentPage()

        nextPageExists = self.checkIfNextPage()
        while nextPageExists:
            self.goToNextPage()
            self.getResultsOnCurrentPage()
            nextPageExists = self.checkIfNextPage()

    def getResultsOnCurrentPage(self):
        titlesList = self.getTitlesList()
        resultPageUrlsList = self.getResultsPageUrlsList()
        sponsorsList = self.getSponsorsList()
        amountsList = self.getAmountsList()
        deadlinesList = self.getDeadlinesList()

        for i in range(len(titlesList)):
            title = titlesList[i]
            url = resultPageUrlsList[i]
            sponsor = sponsorsList[i]
            amount = amountsList[i]
            deadline = deadlinesList[i]

            resultPageArray = [title, url, sponsor, amount, deadline]
            self.resultPagesArrays.append(resultPageArray)

    def getTitlesList(self):
        titlesList = []

        titlesDivs = self.driver.find_elements_by_xpath("//h3/a")
        for title in titlesDivs:
            titlesList.append(title.get_attribute('textContent'))

        titlesList = [CleanText.cleanALLtheText(title) for title in titlesList]
        return titlesList

    def getResultsPageUrlsList(self):
        resultsPageUrlsList = []

        urlsDivs = self.driver.find_elements_by_xpath("//h3/a")
        for url in urlsDivs:
            resultsPageUrlsList.append(url.get_attribute('href'))

        return resultsPageUrlsList

    def getSponsorsList(self):
        sponsorsList = []

        sponsorsDivs = self.driver.find_elements_by_xpath("//div[@class='provided_by']/p[not (@class='label')]")
        for sponsor in sponsorsDivs:
            sponsorsList.append(sponsor.get_attribute('textContent'))

        sponsorsList = [CleanText.cleanALLtheText(sponsor) for sponsor in sponsorsList]
        return sponsorsList

    def getAmountsList(self):
        amountsList = []

        amountsDivs = self.driver.find_elements_by_xpath("//div[@class='award']/p[not (@class='label')]")
        for amount in amountsDivs:
            amountsList.append(amount.get_attribute('textContent'))

        amountsList = [CleanText.cleanALLtheText(amount) for amount in amountsList]
        return amountsList

    def getDeadlinesList(self):
        deadlinesList = []

        deadlinesDiv = self.driver.find_elements_by_xpath("//div[@class='deadline']/p[not (@class='label')]")
        for deadline in deadlinesDiv:
            deadlinesList.append(deadline.get_attribute('textContent'))

        deadlinesList = [CleanText.cleanALLtheText(deadline) for deadline in deadlinesList]
        return deadlinesList

    def goToNextPage(self):
        if self.checkIfNextPage():
            self.driver.find_element_by_xpath("//a[@class='next_page']").click()
            self.driver.implicitly_wait(2)

    def checkIfNextPage(self):
        nextPageDiv = self.driver.find_elements_by_xpath("//a[@class='next_page']")
        if nextPageDiv != []:
            return True
        else:
            return False

    def checkIfElementExists(self, xpath):
        checkElementExists = self.driver.find_elements_by_xpath(xpath)
        if checkElementExists != []:
            return True
        else:
            return False
    '''
