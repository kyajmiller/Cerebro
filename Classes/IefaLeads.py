import re
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Classes.CleanText import CleanText
from Classes.RipPage import RipPage


class IefaLeads(object):
    def __init__(self, isTest=False):
        self.isTest = isTest

        self.driver = webdriver.Firefox()
        self.base_url = 'http://www.iefa.org/'
        self.driver.get(self.base_url + 'scholarships')
        self.driver.find_element_by_id('LoginForm_username').clear()
        self.driver.find_element_by_id('LoginForm_username').send_keys('crawlyjones@gmail.com')
        self.driver.find_element_by_id('LoginForm_password').clear()
        self.driver.find_element_by_id('LoginForm_password').send_keys('sasgcoders')
        self.driver.find_element_by_name('yt3').click()
        self.driver.implicitly_wait(2)

        self.driver.find_element_by_xpath("//ul[@id='yw8']/li[@id='scholarshipsLink']/a").click()
        self.driver.implicitly_wait(2)
        Select(self.driver.find_element_by_id('pageSize')).select_by_visible_text('100')
        self.goToNextPreviousPageRefreshCache()

        self.arrayOfTitlesLinksArrays = []
        self.iefaLeadsArrays = []

    def loopOverResultsPagesAndDoStuff(self):
        self.getTitlesLinksOnCurrentPage()

        if self.isTest:
            for individualArray in self.arrayOfTitlesLinksArrays[:5]:
                title = individualArray[0]
                resultPageLink = individualArray[1]

                self.makeLeadArray(title, resultPageLink)
        else:
            pageCounter = 1
            while pageCounter < 12:
                if self.checkIfNextPage():
                    self.goToNextPageUrl()
                    self.getTitlesLinksOnCurrentPage()
                pageCounter += 1

            for individualArray in self.arrayOfTitlesLinksArrays:
                title = individualArray[0]
                resultPageLink = individualArray[1]

                self.makeLeadArray(title, resultPageLink)

        self.driver.quit()
        return self.iefaLeadsArrays

    def getTitlesLinksOnCurrentPage(self):
        titlesList = self.getTitlesList()
        resultsPagesLinksList = self.getResultsPagesLinksList()

        for i in range(len(titlesList)):
            title = titlesList[i]
            resultPageLink = resultsPagesLinksList[i]

            titleLinkArray = [title, resultPageLink]
            self.arrayOfTitlesLinksArrays.append(titleLinkArray)

    def getTitlesList(self):
        titlesList = []

        featuredTitlesDivs = self.driver.find_elements_by_xpath("//tbody/tr[@class='featured']/td[@width='200px']/a[3]")
        normalTitlesDivs = self.driver.find_elements_by_xpath(
            "//tbody/tr[not (@class='featured')]/td[@width='200px']/a")

        for titleDiv in featuredTitlesDivs:
            titlesList.append(titleDiv.get_attribute('textContent'))
        for titleDiv in normalTitlesDivs:
            titlesList.append(titleDiv.get_attribute('textContent'))

        return titlesList

    def getResultsPagesLinksList(self):
        resultsPagesLinksList = []

        featuredLinksDivs = self.driver.find_elements_by_xpath("//tbody/tr[@class='featured']/td[@width='200px']/a[3]")
        normalLinksDivs = self.driver.find_elements_by_xpath("//tbody/tr[not (@class='featured')]/td[@width='200px']/a")

        for linkDiv in featuredLinksDivs:
            resultsPagesLinksList.append(linkDiv.get_attribute('href'))
        for linkDiv in normalLinksDivs:
            resultsPagesLinksList.append(linkDiv.get_attribute('href'))

        return resultsPagesLinksList

    def goToResultsPageAndGetInfo(self, resultPageLink):
        self.driver.get(resultPageLink)
        self.driver.implicitly_wait(2)

        sponsor = ''
        submissionDeadline = ''
        majors = ''
        awardAmount = ''
        description = ''
        otherCriteria = ''
        numberAwards = ''
        hostInstitution = ''
        awardIncludes = ''
        nationalityRequired = ''
        hostCountries = ''
        sourceWebsite = ''
        sourceText = ''

        if self.checkIfElementExists("//span[@class='award-sponsor']"):
            sponsor = self.driver.find_element_by_xpath("//span[@class='award-sponsor']").get_attribute('textContent')
            sponsor = re.sub('^Sponsor:', '', sponsor)

        if self.checkIfElementExists("//h4[text() = 'Submission Deadline']/following-sibling::p"):
            submissionDeadline = self.driver.find_element_by_xpath(
                "//h4[text() = 'Submission Deadline']/following-sibling::p").get_attribute('textContent')

        if self.checkIfElementExists("//p[@id='award-fieldofstudy']"):
            majors = self.driver.find_element_by_xpath("//p[@id='award-fieldofstudy']").get_attribute('textContent')

        if self.checkIfElementExists("//p[@id='award-amount']"):
            awardAmount = self.driver.find_element_by_xpath("//p[@id='award-amount']").get_attribute('textContent')

        if self.checkIfElementExists(
                "//div[@class='award-description padding_bottom_30']/h4[text() = 'Description']/following-sibling::p[1]"):
            description = self.driver.find_element_by_xpath(
                "//div[@class='award-description padding_bottom_30']/h4[text() = 'Description']/following-sibling::p[1]").get_attribute(
                'textContent')

        if self.checkIfElementExists(
                "//div[@class='award-description padding_bottom_30']/h4[text() = 'Other Criteria']/following-sibling::p[1]"):
            otherCriteria = self.driver.find_element_by_xpath(
                "//div[@class='award-description padding_bottom_30']/h4[text() = 'Other Criteria']/following-sibling::p[1]").get_attribute(
                'textContent')

        if self.checkIfElementExists("//th[text() = 'Number of Awards']/following-sibling::td"):
            numberAwards = self.driver.find_element_by_xpath(
                "//th[text() = 'Number of Awards']/following-sibling::td").get_attribute('textContent')

        if self.checkIfElementExists("//th[text() = 'Host Institution']/following-sibling::td"):
            hostInstitution = self.driver.find_element_by_xpath(
                "//th[text() = 'Host Institution']/following-sibling::td").get_attribute('textContent')

        if self.checkIfElementExists("//th[text() = 'Includes']/following-sibling::td"):
            awardIncludes = self.driver.find_element_by_xpath(
                "//th[text() = 'Includes']/following-sibling::td").get_attribute('textContent')

        if self.checkIfElementExists("//th[text() = 'Nationality Required']/following-sibling::td"):
            nationalityRequired = self.driver.find_element_by_xpath(
                "//th[text() = 'Nationality Required']/following-sibling::td").get_attribute('textContent')

        if self.checkIfElementExists("//th[text() = 'Host Countries']/following-sibling::td"):
            hostCountries = self.driver.find_element_by_xpath(
                "//th[text() = 'Host Countries']/following-sibling::td").get_attribute('textContent')

        if self.checkIfElementExists("//th[text() = 'Link']/following-sibling::td/a"):
            sourceWebsite = self.driver.find_element_by_xpath(
                "//th[text() = 'Link']/following-sibling::td/a").get_attribute('href')
            sourceText = RipPage.getPageSource(sourceWebsite)

        resultPageInfoArray = [sponsor, submissionDeadline, majors, awardAmount, description, otherCriteria,
                               numberAwards, hostInstitution, awardIncludes, nationalityRequired, hostCountries,
                               sourceText]
        resultPageInfoArray = [CleanText.cleanALLtheText(item) for item in resultPageInfoArray]
        resultPageInfoArray.append(sourceWebsite)

        return resultPageInfoArray

    def makeLeadArray(self, title, resultPageLink):
        resultPageInfoArray = self.goToResultsPageAndGetInfo(resultPageLink)
        sponsor = resultPageInfoArray[0]
        submissionDeadline = resultPageInfoArray[1]
        majors = resultPageInfoArray[2]
        awardAmount = resultPageInfoArray[3]
        description = resultPageInfoArray[4]
        otherCriteria = resultPageInfoArray[5]
        numberAwards = resultPageInfoArray[6]
        hostInstitution = resultPageInfoArray[7]
        awardIncludes = resultPageInfoArray[8]
        nationalityRequired = resultPageInfoArray[9]
        hostCountries = resultPageInfoArray[10]
        sourceWebsite = resultPageInfoArray[12]
        sourceText = resultPageInfoArray[11]

        iefaLeadIndividualArray = [title, resultPageLink, sponsor, submissionDeadline, majors, awardAmount, description,
                                   otherCriteria, numberAwards, hostInstitution, awardIncludes, nationalityRequired,
                                   hostCountries, sourceWebsite, sourceText]
        self.iefaLeadsArrays.append(iefaLeadIndividualArray)

    def checkIfNextPage(self):
        checkNextPage = self.driver.find_elements_by_link_text('Next >')
        if checkNextPage != []:
            return True
        else:
            return False

    def goToNextPageClick(self):
        nextPageButton = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Next >')))
        try:
            nextPageButton.click()
            self.driver.implicitly_wait(2)
        except ElementNotVisibleException:
            self.driver.implicitly_wait(2)

    def goToNextPageUrl(self):
        nextPageButton = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Next >')))
        try:
            nextPageUrl = self.driver.find_element_by_link_text('Next >').get_attribute('href')
            self.driver.get(nextPageUrl)
            self.driver.implicitly_wait(2)
        except ElementNotVisibleException:
            self.driver.implicitly_wait(2)

    def goToPreviousPage(self):
        previousPageButton = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, '< Previous')))
        try:
            previousPageButton.click()
            self.driver.implicitly_wait(2)
        except ElementNotVisibleException:
            self.driver.implicitly_wait(2)

    def goToNextPreviousPageRefreshCache(self):
        self.goToNextPageClick()
        self.goToPreviousPage()

    def checkIfElementExists(self, xpath):
        checkElementExists = self.driver.find_elements_by_xpath(xpath)
        if checkElementExists != []:
            return True
        else:
            return False
