# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


import unittest, time, re

class SeleniumPythonFastwebdotcom(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
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

        names=[]
        providers=[]
        awards=[]
        urls=[]
        deadlines=[]
        websites=[]
        awardType=[]
        numberAvailable=[]
        fieldsOfStudy=[]
        additionalInfo=[]
        pageObjects = self.driver.find_elements_by_xpath('//div[@class="pagination right"]/a')
        numPages = len(pageObjects)
        print("\n\nNUMBER OF PAGES: " + str(numPages))


        for currentPage in range(1,numPages+1):
            currentPageUrl = "http://www.fastweb.com/college-scholarships/scholarships?filter=Matched&page=" + str(currentPage)
            self.driver.get(currentPageUrl)
            print("\n\n################################\nCurrently crawling page " + str(currentPage) + ".")

            nameObjects = self.driver.find_elements_by_xpath('//table/tbody/tr/td/h3/a')
            providerObjects = self.driver.find_elements_by_xpath('//table/tbody/tr/td/div[1]/p[2]')
            awardObjects = self.driver.find_elements_by_xpath('//table/tbody/tr/td/div[2]/p[2]')
            deadlineObjects = self.driver.find_elements_by_xpath('//table/tbody/tr/td/div[3]/p[2]')

            print("\n\nNUMBER OF SCHOLARSHIPS ON THIS PAGE: " + str(len(nameObjects)))

            print("Scanning names...")
            for item in nameObjects:
                names.append(item.text)

            print("Scanning providers...")
            for item in providerObjects:
                providers.append(item.text)

            print("Scanning awards...")
            for item in awardObjects:
                awards.append(item.text)

            print("Scanning deadlines...")
            for item in deadlineObjects:
                deadlines.append(item.text)

            print("Scanning urls...")
            for item in nameObjects:
                urls.append(item.get_attribute('href'))

        #end the for loop, now time to print

        for item in urls:
            #visit URL
            self.driver.get(item)
            print("visiting " + str(item))
            #awardType
            newAwardType = self.driver.find_elements_by_xpath('//div[@class="clear no_inner_box"]/ul/li[1]/p[@class="data"]')[0]
            awardType.append(newAwardType.text)
            #numberAvailable
            newNumberAvailable = self.driver.find_elements_by_xpath('//div[@class="clear no_inner_box"]/ul/li[2]/p[@class="data"]')[0]
            numberAvailable.append(newNumberAvailable.text)
            #fieldsOfStudy
            newFieldsOfStudy = self.driver.find_elements_by_xpath('//div[@class="clear no_inner_box"]/ul/li[3]/p[@class="data major"]')[0]
            fieldsOfStudy.append(newFieldsOfStudy.text)
            #additionalInfo
            newAdditionalInfo = self.driver.find_elements_by_xpath('//div[@class="clear no_inner_box"]/ul/li[4]/p[@class="data major"]')[0]
            additionalInfo.append(newAdditionalInfo.text)
            #websites
            newWebsite = self.driver.find_elements_by_xpath('//div[@class="clear no_inner_box"]/ul/li[5]/p[@class="data"]/a')[0]
            websites.append(newWebsite.get_attribute('href'))

        print("\n\nNAMES:")
        for item in names:
            print(item)

        print("\n\nPROVIDERS:")
        for item in providers:
            print(item)

        print("\n\nAWARDS:")
        for item in awards:
            print(item)

        print("\n\nDEADLINES:")
        for item in deadlines:
            print(item)

        print("\n\nURLS:")
        for item in urls:
            print(item)

        print("\n\nAWARD TYPES:")
        for item in awardType:
            print(item)

        print("\n\nNUMBERS AVAILABLE:")
        for item in numberAvailable:
            print(item)

        print("\n\nFIELDS OF STUDY:")
        for item in fieldsOfStudy:
            print(item)

        print("\n\nADDITIONAL INFO:")
        for item in additionalInfo:
            print(item)

        print("\n\nWEBSITES:")
        for item in websites:
            print(item)


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

