from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Classes.RipPage import RipPage
from Classes.CleanText import CleanText


class CheggLeads(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'https://www.chegg.com/'

        self.driver.get(self.base_url + 'scholarships')
        self.driver.find_element_by_link_text('Sign in').click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//form[@class='login-form']/input[@class='form-input-lg email-field']")))

        self.driver.find_element_by_xpath(
            "//form[@class='login-form']/input[@class='form-input-lg email-field']").clear()
        self.driver.find_element_by_xpath(
            "//form[@class='login-form']/input[@class='form-input-lg email-field']").send_keys('crawlyjones1@gmail.com')
        self.driver.find_element_by_xpath(
            "//form[@class='login-form']/input[@class='form-input-lg pass-field']").clear()
        self.driver.find_element_by_xpath(
            "//form[@class='login-form']/input[@class='form-input-lg pass-field']").send_keys('SASGcoders626')
        self.driver.find_element_by_xpath("//input[@class='btn-primary-lg login-button']").click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'SCHOLARSHIPS')))

        self.driver.find_element_by_link_text('SCHOLARSHIPS').click()
        self.driver.implicitly_wait(2)

        self.scrollDownUntilDesiredNumResults(70)

        self.resultsArrays = []
        self.cheggLeadsArrays = []

    def loopOverResultsPagesAndDoStuff(self):
        self.getInfoFromResultsListPage()

        for resultArray in self.resultsArrays:
            title = resultArray[0]
            link = resultArray[1]
            deadline = resultArray[2]
            amount = resultArray[3]

            self.makeLeadArray(title, link, deadline, amount)

        return self.cheggLeadsArrays

    def makeLeadArray(self, title, link, deadline, amount):
        resultPageArray = self.getInfoFromResultsListPage()
        if resultPageArray:
            eligibility = resultPageArray[0]
            applicationOverview = resultPageArray[1]
            description = resultPageArray[2]
            sponsor = resultPageArray[3]
            sourceWebsite = resultPageArray[5]
            sourceText = resultPageArray[4]

            cheggLeadIndividualArray = [title, link, deadline, amount, eligibility, applicationOverview, description,
                                        sponsor, sourceWebsite, sourceText]
            self.cheggLeadsArrays.append(cheggLeadIndividualArray)

    def getInfoFromResultsListPage(self):
        titlesList = self.getTitlesList()
        linksList = self.getLinksList()
        deadlinesList = self.getDeadlinesList()
        amountsList = self.getAmountsList()

        for i in range(len(titlesList)):
            title = titlesList[i]
            link = linksList[i]
            deadline = deadlinesList[i]
            amount = amountsList[i]

            resultsArray = [title, link, deadline, amount]
            self.resultsArrays.append(resultsArray)

    def getTitlesList(self):
        titlesList = []

        titlesDivs = self.driver.find_elements_by_xpath("//a[@class='scholarship__title']")
        for title in titlesDivs:
            titlesList.append(title.get_attribute('textContent'))

        titlesList = [CleanText.cleanALLtheText(title) for title in titlesList]
        return titlesList

    def getLinksList(self):
        linksList = []

        linksDivs = self.driver.find_elements_by_xpath("//a[@class='scholarship__title']")
        for link in linksDivs:
            linksList.append(link.get_attribute('href'))

        return linksList

    def getDeadlinesList(self):
        deadlinesList = []

        deadlinesDivs = self.driver.find_elements_by_xpath("//a[@class='scholarship__deadline']")
        for deadline in deadlinesDivs:
            deadlinesList.append(deadline.get_attribute('textContent'))

        deadlinesList = [CleanText.cleanALLtheText(deadline) for deadline in deadlinesList]
        return deadlinesList

    def getAmountsList(self):
        amountsList = []

        amountsDivs = self.driver.find_elements_by_xpath("//a[@class='scholarship__amount']")
        for amount in amountsDivs:
            amountsList.append(amount.get_attribute('textContent'))

        amountsList = [CleanText.cleanALLtheText(amount) for amount in amountsList]
        return amountsList

    def scrollDownUntilDesiredNumResults(self, numResults):
        numberShownScholarships = self.driver.find_elements_by_xpath("//a[@class='scholarship__title']")
        while len(numberShownScholarships) < numResults:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            numberShownScholarships = self.driver.find_elements_by_xpath("//a[@class='scholarship__title']")

    def getInfoFromScholarshipPage(self, link):
        self.driver.get(link)
        self.driver.implicitly_wait(2)

        findBadButton = self.driver.find_elements_by_xpath(
            "//button[@class='btn-primary-sm save-profile chgsec_hostedsc-apply-ApplyNowButton chgser_sc']")

        if findBadButton == []:
            eligibility = ''
            applicationOverview = ''
            description = ''
            sponsor = ''
            sourceWebsite = ''
            sourceText = ''

            if self.checkIfElementExists("//span[@class='txt-3"):
                eligibility = self.driver.find_element_by_xpath("//span[@class='txt-3").get_attribute('textContent')

            if self.checkIfElementExists(
                    "//h3[text() = 'Application Overview']/following-sibling::div[@class='txt-3']"):
                applicationOverview = self.driver.find_element_by_xpath(
                    "//h3[text() = 'Application Overview']/following-sibling::div[@class='txt-3']").get_attribute(
                    'textContent')

            if self.checkIfElementExists("//h3[text() = 'Purpose']/following-sibling::div[@class='txt-3']"):
                description = self.driver.find_element_by_xpath(
                    "//h3[text() = 'Purpose']/following-sibling::div[@class='txt-3']").get_attribute('textContent')

            if self.checkIfElementExists(
                    "//h3[text() = 'Provider Organization']/following-sibling::div[@class='txt-3'][1]"):
                sponsor = self.driver.find_element_by_xpath(
                    "//h3[text() = 'Provider Organization']/following-sibling::div[@class='txt-3'][1]").get_attribute(
                    'textContent')

            if self.checkIfElementExists("//button[@class='btn-primary-sm go-apply']"):
                sourceWebsite = self.driver.find_element_by_xpath(
                    "//button[@class='btn-primary-sm go-apply']").get_attribute('url')
                sourceText = RipPage.getPageSource(sourceWebsite)

            resultPageInfoArray = [eligibility, applicationOverview, description, sponsor, sourceText]
            resultPageInfoArray = [CleanText.cleanALLtheText(item) for item in resultPageInfoArray]
            resultPageInfoArray.append(sourceWebsite)

            return resultPageInfoArray
        else:
            return None

    def checkIfElementExists(self, xpath):
        checkElementExists = self.driver.find_elements_by_xpath(xpath)
        if checkElementExists != []:
            return True
        else:
            return False


CheggLeads().loopOverResultsPagesAndDoStuff()
