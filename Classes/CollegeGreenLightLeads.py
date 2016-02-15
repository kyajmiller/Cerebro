import re
from selenium import webdriver
from Classes.CleanText import CleanText
from Classes.RipPage import RipPage


class CollegeGreenLightLeads(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'https://www.collegegreenlight.com/'
        self.driver.get(self.base_url + '/')
        self.driver.implicitly_wait(2)

        self.driver.find_element_by_link_text('Login').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_name('email').clear()
        self.driver.find_element_by_name('email').send_keys('crawlyjones@gmail.com')
        self.driver.find_element_by_name('password').clear()
        self.driver.find_element_by_name('password').send_keys('sasgcoders626')
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        self.driver.implicitly_wait(2)
        self.skipPromoPage()
        self.driver.find_element_by_link_text('Scholarships').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath("//a[@class='blue_btn']").click()
        self.driver.implicitly_wait(2)

        self.collegeGreenLightLeadsArrays = []

    def getLeads(self):
        arrayOfTitleLinkDivs = self.driver.find_elements_by_xpath("//td[@class='scholarshipNameColumn']/div/a")
        arrayOfAmountDivs = self.driver.find_elements_by_xpath("//td[@class='amount']")
        arrayOfDeadlineDivs = self.driver.find_elements_by_xpath("//td[@class='deadline']")

        titlesList = self.getTitlesList(arrayOfTitleLinkDivs)
        linksList = self.getLinksList(arrayOfTitleLinkDivs)
        amountsList = self.getAmountsList(arrayOfAmountDivs)
        deadlinesList = self.getDeadlinesList(arrayOfDeadlineDivs)

        for i in range(len(titlesList)):
            title = CleanText.cleanALLtheText(titlesList[i])
            resultPageLink = linksList[i]
            amount = CleanText.cleanALLtheText(amountsList[i])
            deadline = deadlinesList[i]

            resultPageInfo = self.goToResultPageAndPullInformation(resultPageLink)
            sponsor = CleanText.cleanALLtheText(resultPageInfo[0])
            sourceWebsite = resultPageInfo[1]
            description = CleanText.cleanALLtheText(resultPageInfo[2])
            requirements = CleanText.cleanALLtheText(resultPageInfo[3])

            sourceText = ''
            if re.search('^https?://', sourceWebsite):
                sourceText = CleanText.cleanALLtheText(RipPage.getPageSource(sourceWebsite))

            leadArray = [title, amount, deadline, sponsor, description, requirements, resultPageLink, sourceWebsite,
                         sourceText]
            self.collegeGreenLightLeadsArrays.append(leadArray)

        self.driver.quit()
        return self.collegeGreenLightLeadsArrays

    def getTitlesList(self, arrayOfTitleLinkDivs):
        titlesList = [titleDiv.get_attribute('textContent') for titleDiv in arrayOfTitleLinkDivs]
        return titlesList

    def getLinksList(self, arrayOfTitleLinkDivs):
        linksList = [linkDiv.get_attribute('href') for linkDiv in arrayOfTitleLinkDivs]
        return linksList

    def getAmountsList(self, arrayOfAmountDivs):
        amountsList = [amountDiv.get_attribute('textContent') for amountDiv in arrayOfAmountDivs]
        return amountsList

    def getDeadlinesList(self, arrayOfDeadlineDivs):
        deadlinesList = [dealineDiv.get_attribute('textContent') for dealineDiv in arrayOfDeadlineDivs]
        return deadlinesList

    def goToResultPageAndPullInformation(self, resultPageLink):
        self.driver.get(resultPageLink)
        self.driver.implicitly_wait(2)

        sponsor = ''
        sourceWebsite = ''
        description = ''
        requirements = ''

        if self.checkIfElementExists("//h2"):
            sponsor = self.driver.find_element_by_xpath("//h2").get_attribute('textContent')

        if self.checkIfElementExists("//div[@class='applicationInformation ']/p/a"):
            sourceWebsite = self.driver.find_element_by_xpath(
                "//div[@class='applicationInformation ']/p/a").get_attribute('href')
        else:
            if self.checkIfElementExists("//div[@class='applicationInformation ']/p"):
                sourceWebsite = self.driver.find_element_by_xpath(
                    "//div[@class='applicationInformation ']/p").get_attribute('textContent')

        if self.checkIfElementExists("//div[@class='detail']/p[@class='info']"):
            description = self.driver.find_element_by_xpath("//div[@class='detail']/p[@class='info']").get_attribute(
                'textContent')

        if self.checkIfElementExists("//div[@class='requirements']/ul"):
            requirements = self.driver.find_element_by_xpath("//div[@class='requirements']/ul").get_attribute(
                'textContent')

        resultPageInfo = [sponsor, sourceWebsite, description, requirements]
        return resultPageInfo

    def checkIfElementExists(self, xpath):
        checkElementExists = self.driver.find_elements_by_xpath(xpath)
        if checkElementExists != []:
            return True
        else:
            return False

    def skipPromoPage(self):
        if self.checkIfElementExists("//a[@id='noThanks']") and self.checkIfElementExists("//button[@id='continue']"):
            self.driver.find_element_by_xpath("//a[@id='noThanks']").click()
            self.driver.implicitly_wait(2)
