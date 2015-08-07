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
        self.driver.find_element_by_link_text('Scholarships').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath("//td[@class='showAllMatchingScholarships']/div/a[@class='blue_btn']").click()
        self.driver.implicitly_wait(2)

        self.collegeGreenLightLeadsArrays = []

    def getLeads(self):
        arrayOfTitleLinkDivs = self.driver.find_elements_by_xpath("//td[@class='scholarshipNameColumn']/div/a")
        arrayOfAmountDivs = self.driver.find_elements_by_xpath("//td[@class='amount']")
        arrayOfDeadlineDivs = self.driver.find_elements_by_xpath("//td[@class='deadline']")
