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

        waitForLoginField = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
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

        waitForScholarshipsButton = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'SCHOLARSHIPS')))

        self.driver.find_element_by_link_text('SCHOLARSHIPS').click()


CheggLeads()
