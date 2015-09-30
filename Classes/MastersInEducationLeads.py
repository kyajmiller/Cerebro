from selenium import webdriver
from Classes.RipPage import RipPage
from Classes.CleanText import CleanText


class MastersInEducationLeads(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'http://www.mastersineducation.net/'
        self.driver.get(self.base_url + 'scholarships')
        self.driver.implicitly_wait(2)

        self.resultsArrays = []

        self.getInfoOnCurrentPage()

    def loopOverPages(self):
        self.getInfoOnCurrentPage()


    def getInfoOnCurrentPage(self):
        visibleClickyDivs = self.driver.find_elements_by_xpath(
            "//section[@class='scholarships']/div[@class='tab h-results']/div[@class='h-result js-has-toggle']/div[@class='h-result-header js-toggle']")
        for clickyDiv in visibleClickyDivs:
            clickyDiv.click()

        titlesList = self.getTitlesList()
        amountsList = self.getAmountsList()
        deadlinesList = self.getDeadlinesList()
        descriptionsList = self.getDescriptionsList()
        sourceWebsitesList = self.getSourceWebsitesList()

        for i in range(len(titlesList)):
            title = titlesList[i]
            amount = amountsList[i]
            deadline = deadlinesList[i]
            description = descriptionsList[i]
            sourceWebsite = sourceWebsitesList[i]

            resultArray = [title, amount, deadline, description, sourceWebsite]
            self.resultsArrays.append(resultArray)


    def getTitlesList(self):
        titlesList = []

        titlesDivs = self.driver.find_elements_by_xpath(
            "//section[@class='scholarships']/div[@class='tab h-results']/div[@class='h-result js-has-toggle active']/div[@class='h-result-header js-toggle active']/h3")
        for title in titlesDivs:
            titlesList.append(title.get_attribute('textContent'))

        titlesList = [CleanText.cleanALLtheText(title) for title in titlesList]

        return titlesList

    def getAmountsList(self):
        amountsList = []

        amountsDivs = self.driver.find_elements_by_xpath("//dt[text() = 'Amount']/following-sibling::dd[1]")
        for amount in amountsDivs:
            amountsList.append(amount.get_attribute('textContent'))

        amountsList = [CleanText.cleanALLtheText(amount) for amount in amountsList]

        return amountsList

    def getDeadlinesList(self):
        deadlinesList = []

        deadlinesDivs = self.driver.find_elements_by_xpath(
            "//dt[text() = 'Amount']/following-sibling::dt[text() = 'Deadline']/following-sibling::dd[1]")
        for deadline in deadlinesDivs:
            deadlinesList.append(deadline.get_attribute('textContent'))

        deadlinesList = [CleanText.cleanALLtheText(deadline) for deadline in deadlinesList]

        return deadlinesList

    def getDescriptionsList(self):
        descriptionsList = []

        descriptionsDivs = self.driver.find_elements_by_xpath(
            "//dt[text() = 'Amount']/following-sibling::dt[text() = 'Deadline']/following-sibling::dd[1]")
        for description in descriptionsDivs:
            descriptionsList.append(description.get_attribute('textContent'))

        descriptionsList = [CleanText.cleanALLtheText(description) for description in descriptionsList]

        return descriptionsList

    def getSourceWebsitesList(self):
        sourceWebsitesList = []

        linksDivs = self.driver.find_elements_by_xpath(
            "//div[@class = 'h-result-header js-toggle active']/following-sibling::div[@class = 'js-target hide scholarship-content']/p/following-sibling::div[@class='text-center']/a[@class = 'btn']")
        for link in linksDivs:
            sourceWebsitesList.append(link.get_attribute('href'))

        return sourceWebsitesList


MastersInEducationLeads()
