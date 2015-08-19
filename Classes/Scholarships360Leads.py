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

        self.resultPageArrays = []

    def getLeads(self):
        self.loopThroughResultsListPages()
        for resultArray in self.resultPageArrays:
            title = resultArray[0]
            url = resultArray[1]
            deadline = resultArray[2]
            amount = resultArray[3]

            self.makeLeadArray(title, url, deadline, amount)

    def makeLeadArray(self, title, url, deadline, amount):
        scholarshipPageArray = self.getInfoFromScholarshipPage(url)

    def getInfoFromScholarshipPage(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(2)

        description = ''
        eligibility = ''
        amountInfo = ''
        deadlineInfo = ''
        sourceWebsite = ''
        sourceText = ''

        if self.checkIfElementExists("//div[@class='entry-content']/p[1]"):
            description = self.driver.find_element_by_xpath("//div[@class='entry-content']/p[1]").get_attribute(
                'textContent')
            description = CleanText.cleanALLtheText(description)

        if self.checkIfElementExists(
                "//div[@class='entry-content']/p/strong[text() = 'Who is eligible to apply?']/../following-sibling::ul[1]"):
            eligibility = self.driver.find_element_by_xpath(
                "//div[@class='entry-content']/p/strong[text() = 'Who is eligible to apply?']/../following-sibling::ul[1]").get_attribute(
                'textContent')
            eligibility = CleanText.cleanALLtheText(eligibility)

        if self.checkIfElementExists(
                "//div[@class='entry-content']/p/strong[text() = 'How much is each scholarship worth?']/../following-sibling::p[1]"):
            amountInfo = self.driver.find_element_by_xpath(
                "//div[@class='entry-content']/p/strong[text() = 'How much is each scholarship worth?']/../following-sibling::p[1]").get_attribute(
                'textContent')
            amountInfo = CleanText.cleanALLtheText(amountInfo)

        if self.checkIfElementExists(
                "//div[@class='entry-content']/p/strong[text() = 'When is the deadline to apply?']/../following-sibling::ul[1]"):
            deadlineInfo = self.driver.find_element_by_xpath(
                "//div[@class='entry-content']/p/strong[text() = 'When is the deadline to apply?']/../following-sibling::ul[1]").get_attribute(
                'textContent')
            deadlineInfo = CleanText.cleanALLtheText(deadlineInfo)

        if self.checkIfElementExists("//span[@class='apply']/a"):
            sourceWebsite = self.driver.find_element_by_xpath("//span[@class='apply']/a").get_attribute('href')
            sourceText = RipPage.getPageSource(sourceWebsite)
            sourceText = CleanText.cleanALLtheText(sourceText)

        scholarshipPageInfoArray = [description, eligibility, amountInfo, deadlineInfo, sourceWebsite, sourceText]
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
        urlsList = self.getUrlsList()
        deadlinesList = self.getDeadlinesList()
        amountsList = self.getAmountsList()

        for i in range(len(titlesList)):
            title = titlesList[i]
            url = urlsList[i]
            deadline = deadlinesList[i]
            amount = amountsList[i]

            resultPageArray = [title, url, deadline, amount]
            self.resultPageArrays.append(resultPageArray)

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

    def checkIfElementExists(self, xpath):
        checkElementExists = self.driver.find_elements_by_xpath(xpath)
        if checkElementExists != []:
            return True
        else:
            return False


Scholarships360Leads()
