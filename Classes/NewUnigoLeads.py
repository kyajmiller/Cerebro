from selenium import webdriver
from Classes.RipPage import RipPage
from Classes.CleanText import CleanText


class UnigoLeads(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = "https://www.unigo.com/"
        self.driver.get(self.base_url + "match/scholarshipresult#/login")
        self.driver.implicitly_wait(2)

        self.logIn()
        self.getLeads()

        self.unigoLeadsArray = []

    def getLeads(self):
        self.expandSeeMore()
        self.driver.implicitly_wait(2)

        arrayOfAmountObjects = self.driver.find_elements_by_xpath(
            "//div[@class='amount']/span[@data-bind='text: Aequitas.toCurrency(DollarAmount)']")
        arrayOfTitleObjects = self.driver.find_elements_by_xpath(
            "//h4[@data-bind='text: $parent.resultLayout ? shortTitle : Title']")
        arrayOfDeadlineObjects = self.driver.find_elements_by_xpath(
            "//h4[@data-bind='text: $parent.resultLayout ? shortTitle : Title']")

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
                seeMoreButtonExistence = self.checkIfSeeMoreButtonExists()

    def checkIfSeeMoreButtonExists(self):
        seeMoreButton = self.driver.find_elements_by_xpath("//a[@data-bind='click: showMoreScholarships']")
        if seeMoreButton != []:
            return True
        else:
            return False


UnigoLeads()
