import re
from selenium import webdriver
from Classes.CleanText import CleanText
from Classes.RipPage import RipPage


class GoodCallLeads(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://www.goodcall.com/"

        self.driver.get(self.base_url + "scholarships/search")
        self.driver.implicitly_wait(2)

        self.incompleteLeadsArrays = []
        self.goodCallLeads = []

    def getLeads(self):
        self.loopThroughResultsPages()

        for incompleteArray in self.incompleteLeadsArrays:
            title = incompleteArray[0]
            resultPageLink = incompleteArray[1]
            numAwards = incompleteArray[2]
            amount = incompleteArray[3]

            self.makeLeadsArrays(title, resultPageLink, numAwards, amount)

        self.driver.quit()
        return self.goodCallLeads

    def getResultsOnCurrentPage(self):
        titlesList = self.getTitlesList()
        resultsPagesLinks = self.getResultsPagesLinksList()
        numAwardsList = self.getNumAwardsList()
        amountsList = self.getAmountsList()

        for title, link, numAwards, amount in zip(titlesList, resultsPagesLinks, numAwardsList, amountsList):
            incompleteResultArray = [title, link, numAwards, amount]
            self.incompleteLeadsArrays.append(incompleteResultArray)

    def loopThroughResultsPages(self):
        self.getResultsOnCurrentPage()

        nextPageExists = self.checkIfNextPage()
        while nextPageExists:
            self.goToNextPage()
            self.getResultsOnCurrentPage()
            nextPageExists = self.checkIfNextPage()

    def makeLeadsArrays(self, title, resultPageLink, numAwards, amount):
        resultPageInfo = self.getInfoFromResultPage(resultPageLink)

        description = resultPageInfo[0]
        sponsor = resultPageInfo[1]
        classStatus = resultPageInfo[2]
        major = resultPageInfo[3]
        gender = resultPageInfo[4]
        ethnicity = resultPageInfo[5]
        grades = resultPageInfo[6]
        testScores = resultPageInfo[7]
        geography = resultPageInfo[8]
        deadline = resultPageInfo[9]
        essayInfo = resultPageInfo[10]
        sourceWebsite = resultPageInfo[11]
        sourceText = resultPageInfo[12]

        goodCallLead = [title, resultPageLink, numAwards, amount, description, sponsor, classStatus, major, gender,
                        ethnicity, grades, testScores, geography, deadline, essayInfo, sourceWebsite, sourceText]
        self.goodCallLeads.append(goodCallLead)

    def getInfoFromResultPage(self, resultPageLink):
        self.driver.get(resultPageLink)
        self.driver.implicitly_wait(2)

        description = ''
        sponsor = ''
        classStatus = ''
        major = ''
        gender = ''
        ethnicity = ''
        grades = ''
        testScores = ''
        geography = ''
        deadline = ''
        essayInfo = ''
        sourceWebsite = ''
        sourceText = ''

        if self.checkIfElementExists("//div[@id='main-column']/p[1]"):
            description = self.driver.find_element_by_xpath("//div[@id='main-column']/p[1]").get_attribute(
                'textContent')
            description = CleanText.cleanALLtheText(description)

        if self.checkIfElementExists("//div[@id='main-column']/p[2]"):
            sponsor = self.driver.find_element_by_xpath("//div[@id='main-column']/p[2]").get_attribute('textContent')
            sponsor = CleanText.cleanALLtheText(re.sub('Sponsor:', '', sponsor))

        if self.checkIfElementExists("//tr/td[contains(text(), 'School Year')]/following-sibling::td"):
            classStatus = self.driver.find_element_by_xpath(
                "//tr/td[contains(text(), 'School Year')]/following-sibling::td").get_attribute('textContent')
            classStatus = CleanText.cleanALLtheText(classStatus)
            if classStatus == 'No Restrictions':
                classStatus = ''

        if self.checkIfElementExists("//tr/td[contains(text(), 'School Year')]/following-sibling::td"):
            major = self.driver.find_element_by_xpath(
                "//tr/td[contains(text(), 'School Year')]/following-sibling::td").get_attribute('textContent')
            major = CleanText.cleanALLtheText(major)
            if major == 'No Restrictions':
                major = ''

        if self.checkIfElementExists("//tr/td[contains(text(), 'Gender')]/following-sibling::td"):
            gender = self.driver.find_element_by_xpath(
                "//tr/td[contains(text(), 'Gender')]/following-sibling::td").get_attribute('textContent')
            gender = CleanText.cleanALLtheText(gender)
            if gender == 'No Restrictions':
                gender = ''

        if self.checkIfElementExists("//tr/td[contains(text(), 'Ethnicity')]/following-sibling::td"):
            ethnicity = self.driver.find_element_by_xpath(
                "//tr/td[contains(text(), 'Ethnicity')]/following-sibling::td").get_attribute('textContent')
            ethnicity = CleanText.cleanALLtheText(ethnicity)
            if ethnicity == 'No Restrictions':
                ethnicity = ''

        if self.checkIfElementExists("//tr/td[contains(text(), 'Grades')]/following-sibling::td"):
            grades = self.driver.find_element_by_xpath(
                "//tr/td[contains(text(), 'Grades')]/following-sibling::td").get_attribute('textContent')
            grades = CleanText.cleanALLtheText(grades)
            if grades == 'No Restrictions':
                grades = ''

        if self.checkIfElementExists("//tr/td[contains(text(), 'Test Scores')]/following-sibling::td"):
            testScores = self.driver.find_element_by_xpath(
                "//tr/td[contains(text(), 'Test Scores')]/following-sibling::td").get_attribute('textContent')
            testScores = CleanText.cleanALLtheText(testScores)
            if testScores == 'No Restrictions':
                testScores = ''

        if self.checkIfElementExists("//tr/td[contains(text(), 'Geography')]/following-sibling::td"):
            geography = self.driver.find_element_by_xpath(
                "//tr/td[contains(text(), 'Geography')]/following-sibling::td").get_attribute('textContent')
            geography = CleanText.cleanALLtheText(geography)
            if geography == 'No Restrictions':
                geography = ''

        if self.checkIfElementExists("//span[@class='deadline data']"):
            deadline = self.driver.find_element_by_xpath("//span[@class='deadline data']").get_attribute('textContent')
            deadline = CleanText.cleanALLtheText(re.sub('\(\.*?\)', '', deadline))

        if self.checkIfElementExists("//div[@class='listing-info']/h3[contains(text(), 'Essay')]/following-sibling::p"):
            essayPart1 = self.driver.find_elements_by_xpath(
                "//div[@class='listing-info']/h3[contains(text(), 'Essay')]/following-sibling::p")

            if self.checkIfElementExists("//div[@id='essay-length']") and len(
                    self.driver.find_elements_by_xpath("//div[@id='essay-length']")) == len(essayPart1):
                essayPart2 = self.driver.find_elements_by_xpath("//div[@id='essay-length']")
                combinedParts = []
                for i in range(len(essayPart1)):
                    part1 = CleanText.cleanALLtheText(essayPart1[i].get_attribute('textContent'))
                    part2 = CleanText.cleanALLtheText(essayPart2[i].get_attribute('textContent'))
                    combined = '%s %s' % (part1, part2)
                    combinedParts.append(combined)
                    essayInfo = ' '.join(combinedParts)
            else:
                essayInfo = ' '.join(essayPart1)

        if self.checkIfElementExists("//a[@class='action-button visit-site']"):
            sourceWebsite = self.driver.find_element_by_xpath("//a[@class='action-button visit-site']").get_attribute(
                'href')
            sourceText = CleanText.cleanALLtheText(RipPage.getPageSource(sourceWebsite))

        resultPageInfoArray = [description, sponsor, classStatus, major, gender, ethnicity, grades, testScores,
                               geography, deadline, essayInfo, sourceWebsite, sourceText]

        return resultPageInfoArray

    def getTitlesList(self):
        titlesList = []

        titlesDivs = self.driver.find_elements_by_xpath("//div[@class='main-details clearfix']/h2/a")
        for title in titlesDivs:
            titlesList.append(CleanText.cleanALLtheText(title.get_attribute('textContent')))

        return titlesList

    def getResultsPagesLinksList(self):
        resultsPagesUrls = []

        moreInfoDivs = self.driver.find_elements_by_xpath(
            "//div[@class='one-card-actions']/a[@class='action-button info']")
        for moreInfoDiv in moreInfoDivs:
            resultsPagesUrls.append(moreInfoDiv.get_attribute('href'))

        return resultsPagesUrls

    def getNumAwardsList(self):
        numAwardsList = []

        numAwardsDivs = self.driver.find_elements_by_xpath("//div[@class='award-count']")
        for awardDiv in numAwardsDivs:
            numAwardsList.append(
                CleanText.cleanALLtheText(re.sub('# Awards', '', awardDiv.get_attribute('textContent'))))

        return numAwardsList

    def getAmountsList(self):
        amountsList = []

        amountsDivs = self.driver.find_elements_by_xpath("//div[@class='amount']")
        for amountDiv in amountsDivs:
            amountsList.append(CleanText.cleanALLtheText(re.sub('Amount', '', amountDiv.get_attribute('textContent'))))

        return amountsList

    def goToNextPage(self):
        if self.checkIfNextPage():
            self.driver.find_element_by_link_text("Next Page").click()
            self.driver.implicitly_wait(2)

    def checkIfNextPage(self):
        nextPageButton = self.driver.find_elements_by_link_text('Next Page')
        if nextPageButton != []:
            return True
        else:
            return False

    def checkIfElementExists(self, xpath):
        checkElementExists = self.driver.find_elements_by_xpath(xpath)
        if checkElementExists != []:
            return True
        else:
            return False
