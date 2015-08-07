from selenium import webdriver
from Classes.CleanText import CleanText
from Classes.RipPage import RipPage


class FatomeiLeads(object):
    def __init__(self, isTest=False):
        self.isTest = isTest
        self.driver = webdriver.Firefox()
        self.base_url = "https://www.fatomei.com/"
        self.driver.get(self.base_url + '/')
        self.driver.implicitly_wait(2)

        self.fatomeiLeadsArray = []

    def getFatomeiLeadsArrays(self):
        self.getLeads()

        if not self.isTest:
            self.goToOtherPagesAndGetLeads()

        self.driver.quit()
        return self.fatomeiLeadsArray

    def getLeads(self):
        arrayOfTitleLinkDivs = self.driver.find_elements_by_xpath(
            "//td[@class='f']/../preceding-sibling::tr[1]/td[@class='a']/a")
        arrayOfDateDescriptionDivs = self.driver.find_elements_by_xpath("//tr/td[@class='f']/../td")

        titlesList = self.getTitlesList(arrayOfTitleLinkDivs)
        linksList = self.getLinksList(arrayOfTitleLinkDivs)
        dueDatesList = self.getDueDates(arrayOfDateDescriptionDivs)
        descriptionsList = self.getDescriptionsList(arrayOfDateDescriptionDivs)

        for i in range(len(titlesList)):
            title = CleanText.cleanALLtheText(titlesList[i])
            link = linksList[i]
            dueDate = dueDatesList[i]
            description = CleanText.cleanALLtheText(descriptionsList[i])
            sourceText = CleanText.cleanALLtheText(RipPage.getPageSource(link))

            scholarshipArray = [title, description, dueDate, link, sourceText]
            self.fatomeiLeadsArray.append(scholarshipArray)

    def goToOtherPagesAndGetLeads(self):
        otherPageLinks = self.driver.find_elements_by_xpath("//h2/a")
        numPageLinks = len(otherPageLinks)
        whatPageOn = 0

        while whatPageOn < numPageLinks:
            otherPageLinks = self.driver.find_elements_by_xpath("//h2/a")
            pageToGoTo = otherPageLinks[whatPageOn]
            if pageToGoTo:
                pageToGoTo.click()
                self.driver.implicitly_wait(2)
                self.getLeads()
                self.driver.get(self.base_url + '/')
                self.driver.implicitly_wait(2)
                whatPageOn += 1

    def getTitlesList(self, arrayOfTitleLinkDivs):
        titlesList = [titleDiv.text for titleDiv in arrayOfTitleLinkDivs]
        return titlesList

    def getLinksList(self, arrayOfTitleLinkDivs):
        linksList = []

        for linkDiv in arrayOfTitleLinkDivs:
            link = linkDiv.get_attribute('href')
            linksList.append(link)
        return linksList

    def getDueDates(self, arrayOfDateDescriptionDivs):
        dueDatesList = []

        currentIndexCounter = 0
        for dueDateDiv in arrayOfDateDescriptionDivs:
            if currentIndexCounter % 2 == 0:
                dueDate = dueDateDiv.get_attribute('textContent')
                dueDatesList.append(dueDate)
            currentIndexCounter += 1
        return dueDatesList

    def getDescriptionsList(self, arrayOfDateDescriptionDivs):
        descriptionsList = []

        currentIndexCounter = 0
        for descriptionDiv in arrayOfDateDescriptionDivs:
            if currentIndexCounter % 2 == 1:
                description = descriptionDiv.get_attribute('textContent')
                descriptionsList.append(description)
            currentIndexCounter += 1
        return descriptionsList
