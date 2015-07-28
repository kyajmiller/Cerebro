# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re

class CrawlChegg(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.chegg.com/auth?action=login&reset_password=0"
        self.verificationErrors = []
        self.accept_next_alert = True
        driver = self.driver
        driver.get(self.base_url + "/auth?action=login&reset_password=0")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("crawlyjones@gmail.com")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("SASGcoders626")
        driver.find_element_by_name("login").click()
        driver.get("https://www.chegg.com/scholarships")
        print("It's not broken yet :D")


    def test_crawl_chegg(self):
        print(self.driver.find_elements_by_xpath('//section/div/div[4]/a[2]'))


    def is_element_present(self, how, what):
        return True

    def is_alert_present(self):
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
