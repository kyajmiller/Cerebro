from selenium import webdriver
from Classes.CleanText import CleanText
from Classes.RipPage import RipPage


class GoodCallLeads(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://www.goodcall.com/"

        self.driver.get(self.base_url + "scholarships/search")
        self.driver.implicitly_wait(2)

        self.driver.find_element_by_link_text("Next Page").click()


GoodCallLeads()
