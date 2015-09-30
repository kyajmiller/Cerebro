from selenium import webdriver
from Classes.RipPage import RipPage
from Classes.CleanText import CleanText


class MastersInEducationLeads(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'http://www.mastersineducation.net/'
        self.driver.get(self.base_url + 'scholarships')
        self.driver.implicitly_wait(2)

        self.getInfoOnCurrentPage()

    def getInfoOnCurrentPage(self):
        visibleClickyDivs = self.driver.find_elements_by_xpath(
            "//section[@class='scholarships']/div[@class='tab h-results']/div[@class='h-result js-has-toggle']/div[@class='h-result-header js-toggle']")
        for clickyDiv in visibleClickyDivs:
            clickyDiv.click()

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




MastersInEducationLeads()
