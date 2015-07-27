# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import xml.etree.ElementTree as xp


import unittest, time, re
import xml.etree.ElementTree as pxp

class SeleniumPythonFastwebdotcom(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.fastweb.com"
        self.verificationErrors = []
        self.accept_next_alert = True
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_id("login").clear()
        driver.find_element_by_id("login").send_keys("crawlyjones@gmail.com")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("sasgcoders")
        driver.find_element_by_id("user_form_submit").click()
        driver.get("http://www.fastweb.com/college-scholarships/scholarships?filter=Matched&page=1")
        print("Login successful")
    def testIsOne(self):
        self.assertEqual(1,1)
        print("1 is equal to 1")

    def test_fastweb_dot_com_login(self):

        URLS = self.driver.find_elements_by_xpath('//table/tbody/tr/td/h3/a')
        Providers = self.driver.find_elements_by_xpath('//table/tbody/tr/td/div[1]/p[2]')
        Awards = self.driver.find_elements_by_xpath('//table/tbody/tr/td/div[2]/p[2]')
        for item in Providers:
            print(item.get_attribute('textContent'))
            
        print( "URLS: \n" + str(URLS) + "\nProviders: \n" + str(Providers) + "\nAwards: \n" + str(Awards))

    
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

    def fastweb_dot_com_crawl(self):
        print("Crawling...")


if __name__ == "__main__":
    unittest.main()

