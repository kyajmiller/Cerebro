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

        self.arrayOfTitleLinkDivs = self.driver.find_elements_by_xpath("//td[@class='a']/a")
        self.arrayOfDateDescriptionDivs = self.driver.find_elements_by_xpath("//tr/td[@class='f']/../td")

        self.fatomeiLeadsArray = []

    def getFatomeiLeadsArrays(self):
        titlesList = self.getTitlesList()
        linksList = self.getLinksList()
        dueDatesList = self.getDueDates()
        descriptionsList = self.getDescriptionsList()

        if self.isTest:
            title = CleanText.cleanALLtheText(titlesList[0])
            link = linksList[0]
            dueDate = dueDatesList[0]
            description = CleanText.cleanALLtheText(descriptionsList[0])
            sourceText = CleanText.cleanALLtheText(RipPage.getPageSource(link))

            scholarshipArray = [title, description, dueDate, link, sourceText]
            self.fatomeiLeadsArray.append(scholarshipArray)
        else:
            for i in range(len(titlesList)):
                title = CleanText.cleanALLtheText(titlesList[i])
                link = linksList[i]
                dueDate = dueDatesList[i]
                description = CleanText.cleanALLtheText(descriptionsList[i])
                sourceText = CleanText.cleanALLtheText(RipPage.getPageSource(link))

                scholarshipArray = [title, description, dueDate, link, sourceText]
                self.fatomeiLeadsArray.append(scholarshipArray)

        self.driver.quit()
        return self.fatomeiLeadsArray

    def getTitlesList(self):
        titlesList = [titleDiv.text for titleDiv in self.arrayOfTitleLinkDivs]
        return titlesList

    def getLinksList(self):
        linksList = []

        for linkDiv in self.arrayOfTitleLinkDivs:
            link = linkDiv.get_attribute('href')
            linksList.append(link)
        return linksList

    def getDueDates(self):
        dueDatesList = []

        currentIndexCounter = 0
        for dueDateDiv in self.arrayOfDateDescriptionDivs:
            if currentIndexCounter % 2 == 0:
                dueDate = dueDateDiv.get_attribute('textContent')
                dueDatesList.append(dueDate)
            currentIndexCounter += 1
        return dueDatesList

    def getDescriptionsList(self):
        descriptionsList = []

        currentIndexCounter = 0
        for descriptionDiv in self.arrayOfDateDescriptionDivs:
            if currentIndexCounter % 2 == 1:
                description = descriptionDiv.get_attribute('textContent')
                descriptionsList.append(description)
            currentIndexCounter += 1
        return descriptionsList
