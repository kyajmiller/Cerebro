from selenium import webdriver
from Classes.CleanText import CleanText
from Classes.RipPage import RipPage


class IefaLeads(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'http://www.iefa.org/'
        self.driver.get(self.base_url + 'scholarships')
        self.driver.find_element_by_id('LoginForm_username').clear()
        self.driver.find_element_by_id('LoginForm_username').send_keys('crawlyjones@gmail.com')
        self.driver.find_element_by_id('LoginForm_password').clear()
        self.driver.find_element_by_id('LoginForm_password').send_keys('sasgcoders')
        self.driver.find_element_by_name('yt3').click()
        self.driver.implicitly_wait(2)

        self.driver.find_element_by_xpath("//ul[@id='yw8']/li[@id='scholarshipsLink']/a").click()


IefaLeads()
