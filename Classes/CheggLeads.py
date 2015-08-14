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

        self.scrollDownUntilFiveHundredTitles()

    def getInfoFromResultsListPage(self):
        titlesList = self.getTitlesList()
        linksList = self.getLinksList()
        deadlinesList = self.getDeadlinesList()
        amoundsList = self.getAmountsList()

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

    def scrollDownUntilFiveHundredTitles(self):
        numberShownScholarships = self.driver.find_elements_by_xpath("//a[@class='scholarship__title']")
        while len(numberShownScholarships) < 500:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            numberShownScholarships = self.driver.find_elements_by_xpath("//a[@class='scholarship__title']")


CheggLeads()
