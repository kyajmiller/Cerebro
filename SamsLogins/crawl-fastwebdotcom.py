# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


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
        print("1 is equal to 1, nothing broke")

    def test_fastweb_dot_com_login(self):

        nameObjects = self.driver.find_elements_by_xpath('//table/tbody/tr/td/h3/a')
        providerObjects = self.driver.find_elements_by_xpath('//table/tbody/tr/td/div[1]/p[2]')
        awardObjects = self.driver.find_elements_by_xpath('//table/tbody/tr/td/div[2]/p[2]')
        deadlineObjects = self.driver.find_elements_by_xpath('//table/tbody/tr/td/div[3]/p[2]')
        pageObjects = self.driver.find_elements_by_xpath('//div[@class="pagination right"]/a')
        names=[]
        providers=[]
        awards=[]
        urls=[]
        deadlines=[]

        print("\n\nNAMES:")
        for item in nameObjects:
            names.append(item.text)
        for item in names:
            print(item)

        print("\n\nPROVIDERS:")
        for item in providerObjects:
            providers.append(item.text)
        for item in providers:
            print(item)

        print("\n\nAWARDS:")
        for item in awardObjects:
            awards.append(item.text)
        for item in awards:
            print(item)

        print("\n\nDEADLINES:")
        for item in deadlineObjects:
            deadlines.append(item.text)
        for item in deadlines:
            print(item)

        print("\n\nURLS:")
        for item in nameObjects:
            urls.append(item.get_attribute('href'))
        for item in urls:
            print(item)

        print("\n\nNUMBER OF PAGES: " + str(len(pageObjects)))

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

