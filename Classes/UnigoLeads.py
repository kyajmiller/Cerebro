import re
from selenium import webdriver
from Classes.RipPage import RipPage
from Classes.CleanText import CleanText


class UnigoLeads(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = "https://www.unigo.com/"
        self.driver.get(self.base_url + "match/scholarshipresult#/login")
        self.driver.implicitly_wait(2)

        self.driver.find_element_by_name('UserName').clear()
        self.driver.find_element_by_name('UserName').send_keys('crawlyjones@gmail.com')
        self.driver.find_element_by_name('password').clear()
        self.driver.find_element_by_name('password').send_keys('sasgcoders626')
        self.driver.find_element_by_css_selector('button.btn-primary').click()
        self.driver.implicitly_wait(2)

        self.unigoLeadsArray = []

    def getLeads(self):
        self.expandSeeMore()

        arrayOfAmountObjects = self.driver.find_elements_by_xpath(
            "//div[@class='amount']/span[@data-bind='text: Aequitas.toCurrency(DollarAmount)']")
        arrayOfTitleObjects = self.driver.find_elements_by_xpath(
            "//h4[@data-bind='text: $parent.resultLayout ? shortTitle : Title']")
        arrayOfDeadlineObjects = self.driver.find_elements_by_xpath(
            "//h4[@data-bind='text: $parent.resultLayout ? shortTitle : Title']")

        arrayOfClickResultObjects = self.driver.find_elements_by_xpath(
            "//a[@data-bind='click: function(scholarship, event) { $parent.showScholarshipDetail(scholarship, event) }']")

        titlesList = self.getTitlesList(arrayOfTitleObjects)
        amountsList = self.getAmountsList(arrayOfAmountObjects)
        deadlinesList = self.getDeadlinesList(arrayOfDeadlineObjects)

        for i in range(len(titlesList)):
            title = titlesList[i]
            amount = amountsList[i]
            deadline = deadlinesList[i]

            self.driver.get(self.base_url + 'match/scholarshipresult')
            self.driver.implicitly_wait(2)

            self.expandSeeMore()
            arrayOfClickResultObjects = self.driver.find_elements_by_xpath(
                "//a[@data-bind='click: function(scholarship, event) { $parent.showScholarshipDetail(scholarship, event) }']")
            objectToClick = arrayOfClickResultObjects[i]

            objectToClick.click()
            self.driver.implicitly_wait(2)

            resultPageArray = self.getResultPageInfo()
            sponsor = resultPageArray[0]
            awardAmount = resultPageArray[1]
            recipients = resultPageArray[2]
            requirements = resultPageArray[3]
            additionalInfo = resultPageArray[4]
            contact = resultPageArray[5]
            address = resultPageArray[6]
            sourceWebsite = resultPageArray[7]
            sourceText = resultPageArray[8]

            leadArray = [title, amount, deadline, sponsor, awardAmount, recipients, requirements, additionalInfo,
                         contact, address, sourceWebsite, sourceText]
            self.unigoLeadsArray.append(leadArray)

        self.driver.quit()
        return self.unigoLeadsArray

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
        sponsor = CleanText.cleanALLtheText(self.driver.find_element_by_xpath(
            "//div/p/strong[text() = 'Awarded By']/../../following-sibling::div/p").get_attribute('textContent'))
        awardAmount = CleanText.cleanALLtheText(self.driver.find_element_by_xpath(
            "//div/p/strong[text() = 'Awarded By']/../../following-sibling::div/p").get_attribute('textContent'))
        recipients = CleanText.cleanALLtheText(self.driver.find_element_by_xpath(
            "//div/p/strong[text() = 'Recipients']/../../following-sibling::div/p").get_attribute('textContent'))
        requirements = CleanText.cleanALLtheText(self.driver.find_element_by_xpath(
            "//div/p/strong[text() = 'Requirements']/../../following-sibling::div").get_attribute('textContent'))
        additionalInfo = CleanText.cleanALLtheText(self.driver.find_element_by_xpath(
            "//div/p/strong[text() = 'Additional Information']/../../following-sibling::div/p").get_attribute(
            'textContent'))
        contact = CleanText.cleanALLtheText(self.driver.find_element_by_xpath(
            "//div/p/strong[text() = 'Contact']/../../following-sibling::div/p").get_attribute('textContent'))
        address = CleanText.cleanALLtheText(self.driver.find_element_by_xpath(
            "//div/p/strong[text() = 'Address']/../../following-sibling::div").get_attribute('textContent'))
        sourceWebsite = self.driver.find_element_by_xpath("//a[@class='button secondary']").get_attribute('href')
        sourceText = CleanText.cleanALLtheText(RipPage.getPageSource(sourceWebsite))

        resultPageArray = [sponsor, awardAmount, recipients, requirements, additionalInfo, contact, address,
                           sourceWebsite, sourceText]
        return resultPageArray

    def expandSeeMore(self):
        self.seeMoreButtonExistence = ''
        if self.checkIfSeeMoreButtonExists():
            self.seeMoreButtonExistence = True
            while self.seeMoreButtonExistence:
                self.driver.find_element_by_xpath("//a[@data-bind='click: showMoreScholarships']").click()
                self.seeMoreButtonExistence = self.checkIfSeeMoreButtonExists()

    def checkIfSeeMoreButtonExists(self):
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

UnigoLeads().getLeads()
