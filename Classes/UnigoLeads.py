from selenium import webdriver
from Classes.RipPage import RipPage
from Classes.CleanText import CleanText
import time


class UnigoLeads(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = "https://www.unigo.com/"
        self.driver.get(self.base_url + "match/scholarshipresult#/login")
        self.driver.implicitly_wait(2)

        self.logIn()

        self.unigoLeadsArrayThing = []

    def getLeads(self):
        self.expandSeeMore()
        time.sleep(2)

        arrayOfAmountObjects = self.driver.find_elements_by_xpath(
            "//div[@class='amount']/span[@data-bind='text: Aequitas.toCurrency(DollarAmount)']")
        arrayOfTitleObjects = self.driver.find_elements_by_xpath(
                "//h4[@data-bind='text: Title']")
        arrayOfDeadlineObjects = self.driver.find_elements_by_xpath(
                "//span[@class='calendar']")

        titlesList = self.getTitlesList(arrayOfTitleObjects)
        amountsList = self.getAmountsList(arrayOfAmountObjects)
        deadlinesList = self.getDeadlinesList(arrayOfDeadlineObjects)

        for i in range(len(titlesList)):
            title = CleanText.cleanALLtheText(titlesList[i])
            amount = CleanText.cleanALLtheText(amountsList[i])
            deadline = CleanText.cleanALLtheText(deadlinesList[i])

            self.driver.get(self.base_url + 'match/scholarshipresult')
            self.driver.implicitly_wait(2)

            self.expandSeeMore()
            arrayOfClickResultObjects = self.driver.find_elements_by_xpath(
                "//a[@data-bind='click: function(scholarship, event) { $parent.showScholarshipDetail(scholarship, event) }']")
            if arrayOfClickResultObjects[i]:
                objectToClick = arrayOfClickResultObjects[i]

                objectToClick.click()
                self.driver.implicitly_wait(2)

                resultPageArray = self.getResultPageInfo()
                self.makeLead(title, amount, deadline, resultPageArray)

        time.sleep(5)
        # self.driver.quit()
        return self.unigoLeadsArrayThing

    def makeLead(self, title, amount, deadline, resultPageArray):
        url = resultPageArray[0]
        sponsor = resultPageArray[1]
        awardAmount = resultPageArray[2]
        recipients = resultPageArray[3]
        requirements = resultPageArray[4]
        additionalInfo = resultPageArray[5]
        contact = resultPageArray[6]
        address = resultPageArray[7]
        deadlineInformation = resultPageArray[8]
        sourceWebsite = resultPageArray[9]
        sourceText = resultPageArray[10]

        leadArray = [title, amount, deadline, url, sponsor, awardAmount, recipients, requirements, additionalInfo,
                     contact, address, deadlineInformation, sourceWebsite, sourceText]

        self.unigoLeadsArrayThing.append(leadArray)

    def getTitlesList(self, arrayOfTitleObjects):
        titlesList = [titleObject.get_attribute('textContent') for titleObject in arrayOfTitleObjects]
        return titlesList

    def getAmountsList(self, arrayOfAmountObjects):
        amountsList = [amountObject.get_attribute('textContent') for amountObject in arrayOfAmountObjects]
        return amountsList

    def getDeadlinesList(self, arrayOfDeadlineObjects):
        deadlinesList = [deadlineObject.get_attribute('textContent') for deadlineObject in arrayOfDeadlineObjects]
        return deadlinesList

    def getResultPageInfo(self):
        url = self.driver.current_url
        sponsor = ''
        awardAmount = ''
        recipients = ''
        requirements = ''
        additionalInfo = ''
        contact = ''
        address = ''
        deadlineInformation = ''

        if self.checkIfElementExists("//div/p/strong[text() = 'Awarded By']/../../following-sibling::div/p"):
            sponsor = CleanText.cleanALLtheText(self.driver.find_element_by_xpath(
                    "//div/p/strong[text() = 'Awarded By']/../../following-sibling::div/p").get_attribute(
                'textContent'))
        if self.checkIfElementExists("//div/p/strong[text() = 'Award Amount']/../../following-sibling::div/p"):
            awardAmount = CleanText.cleanALLtheText(self.driver.find_element_by_xpath(
                    "//div/p/strong[text() = 'Award Amount']/../../following-sibling::div/p").get_attribute(
                'textContent'))
        if self.checkIfElementExists("//div/p/strong[text() = 'Recipients']/../../following-sibling::div/p"):
            recipients = CleanText.cleanALLtheText(self.driver.find_element_by_xpath(
                    "//div/p/strong[text() = 'Recipients']/../../following-sibling::div/p").get_attribute(
                'textContent'))
        if self.checkIfElementExists("//div/p/strong[text() = 'Requirements']/../../following-sibling::div"):
            requirements = CleanText.cleanALLtheText(self.driver.find_element_by_xpath(
                    "//div/p/strong[text() = 'Requirements']/../../following-sibling::div").get_attribute(
                'textContent'))
        if self.checkIfElementExists(
                "//div/p/strong[text() = 'Additional Information']/../../following-sibling::div/p"):
            additionalInfo = CleanText.cleanALLtheText(self.driver.find_element_by_xpath(
                    "//div/p/strong[text() = 'Additional Information']/../../following-sibling::div/p").get_attribute(
                    'textContent'))
        if self.checkIfElementExists("//div/p/strong[text() = 'Contact']/../../following-sibling::div/p"):
            contact = CleanText.cleanALLtheText(self.driver.find_element_by_xpath(
                    "//div/p/strong[text() = 'Contact']/../../following-sibling::div/p").get_attribute('textContent'))
        if self.checkIfElementExists("//div/p/strong[text() = 'Address']/../../following-sibling::div"):
            address = CleanText.cleanALLtheText(self.driver.find_element_by_xpath(
                    "//div/p/strong[text() = 'Address']/../../following-sibling::div").get_attribute('textContent'))
        if self.checkIfElementExists(
                "//strong[text() ='Deadline Information']/following-sibling::span[@class='smalltext']"):
            deadlineInformation = CleanText.cleanALLtheText(self.driver.find_element_by_xpath(
                "//strong[text() ='Deadline Information']/following-sibling::span[@class='smalltext']").get_attribute(
                'textContent'))
        if self.checkIfElementExists("//a[@class='button cta']"):
            sourceWebsite = self.driver.find_element_by_xpath("//a[@class='button cta']").get_attribute('href')
            sourceText = CleanText.cleanALLtheText(RipPage.getPageSource(sourceWebsite))
        else:
            sourceWebsite = ''
            sourceText = ''

        resultPageArray = [url, sponsor, awardAmount, recipients, requirements, additionalInfo, contact, address,
                           deadlineInformation
                           sourceWebsite, sourceText]
        return resultPageArray

    def logIn(self):
        if self.driver.find_elements_by_link_text('Log in'):
            self.driver.find_element_by_link_text('Log in').click()
            self.driver.implicitly_wait(2)
            self.driver.find_element_by_name('UserName').clear()
            self.driver.find_element_by_name('UserName').send_keys('crawlyjones@gmail.com')
            self.driver.find_element_by_name('Password').clear()
            self.driver.find_element_by_name('Password').send_keys('sasgcoders626')
            self.driver.find_element_by_css_selector('button.button.action').click()
            self.driver.implicitly_wait(2)
        elif self.driver.find_elements_by_name('UserName') and self.driver.find_elements_by_name('password'):
            self.driver.find_element_by_name('UserName').clear()
            self.driver.find_element_by_name('UserName').send_keys('crawlyjones@gmail.com')
            self.driver.find_element_by_name('Password').clear()
            self.driver.find_element_by_name('Password').send_keys('sasgcoders626')
            self.driver.find_element_by_css_selector('button.button.action').click()
            self.driver.implicitly_wait(2)

    def expandSeeMore(self):
        if self.checkIfSeeMoreButtonExists():
            seeMoreButtonExistence = True
            while seeMoreButtonExistence:
                self.driver.find_element_by_xpath("//a[@data-bind='click: showMoreScholarships']").click()
                time.sleep(1)
                seeMoreButtonExistence = self.checkIfSeeMoreButtonExists()

    def checkIfSeeMoreButtonExists(self):
        time.sleep(1)
        seeMoreButton = self.driver.find_elements_by_xpath("//a[@data-bind='click: showMoreScholarships']")
        if seeMoreButton != []:
            return True
        else:
            return False

    def checkIfElementExists(self, xpath):
        checkElementExists = self.driver.find_elements_by_xpath(xpath)
        if checkElementExists != []:
            return True
        else:
            return False
