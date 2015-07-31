from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re

class CrawlIEFA(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.iefa.org/"
        self.verificationErrors = []
        self.accept_next_alert = True
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys("crawlyjones@gmail.com")
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys("sasgcoders")
        driver.find_element_by_xpath('//input[@value="Login"]').click()
        time.sleep(1)
        driver.find_element_by_link_text("Scholarships").click()
        assert(self.driver.current_url == "http://www.iefa.org/scholarships")
        print("successfully logged in and on scholarship page!")


    def test_crawl_i_e_f_a(self):
        print("Crawling\n")
        assert(self.is_element_present(By.XPATH,'//ul/li[@class="next"]'))

        awardNames = []
        inSiteUrls = []
        fields = []
        descriptions = []
        nationalities = []
        hostCountries = []
        submissionDeadlines = []
        awardAmounts = []
        otherCriteria = []
        contactEmails = []
        websites = []

        while self.is_element_present(By.XPATH,'//ul/li[@class="next"]'):
            print("found NEXT button")

            awardNameObjects = self.driver.find_elements_by_xpath('//tbody/tr/td[1]/a')
            fieldObjects = self.driver.find_elements_by_xpath('//tbody/tr/td[2]')
            nationalityObjects = self.driver.find_elements_by_xpath('//tbody/tr/td[3]/p[1]')
            hostCountryObjects = self.driver.find_elements_by_xpath('//tbody/tr/td[3]/p[2]')
            print("fetched stuff")
            for item in awardNameObjects:
                awardNames.append(item.text)
                inSiteUrls.append(item.get_attribute("href"))
            for item in fieldObjects:
                fields.append(item.text)
            for item in nationalityObjects:
                nationalities.append(item.text)
            for item in hostCountryObjects:
                hostCountries.append(item.text)

            nextPageButton = self.driver.find_element_by_xpath("//a[contains(.,'Next >')]")
            nextPageButton.click()
            time.sleep(0.5) #otherwise it tries to jump the gun and returns some really weird errors
            print("Looping\n")
            break #for testing only
        print("Out of loop")

        if awardNames[0] == "FEATURED":
            awardNames.pop(0)
            awardNames.pop(0)
            inSiteUrls.pop(0)
            inSiteUrls.pop(0)#the first two have to do with the "featured scholarship" which appears on the first page. They should be "FEATURED" and [], respectively.


        for item in inSiteUrls:

            print("Visiting " + item + " ...")
            self.driver.get(item)

            if self.driver.find_elements_by_xpath('//h4[contains(.,"Submission Deadline")]/../p') != []:
                submissionDeadlines.append(self.driver.find_elements_by_xpath('//h4[contains(.,"Submission Deadline")]/../p')[0].text)
            else:
                submissionDeadlines.append(" ")

            if self.driver.find_elements_by_xpath('//h4[contains(.,"Field(s) of Study")]/../p') != []:
                awardAmounts.append(self.driver.find_elements_by_xpath('//h4[contains(.,"Field(s) of Study")]/../p')[0].text)
            else:
                awardAmounts.append(" ")

            if self.driver.find_elements_by_xpath('//h4[contains(.,"Description")]/../p[1]') != []:
                descriptions.append(self.driver.find_elements_by_xpath('//h4[contains(.,"Description")]/../p[1]')[0].text)
            else:
                descriptions.append(" ")

            if self.driver.find_elements_by_xpath('//h4[contains(.,"Other Criteria")]') != []:
                otherCriteria.append(self.driver.find_elements_by_xpath('//h4[contains(.,"Other Criteria")]/../p[2]')[0].text)
            else:
                otherCriteria.append(" ")

            if self.driver.find_elements_by_xpath('//th[contains(.,"E-mail")]/../td/a') != []:
                contactEmails.append(self.driver.find_elements_by_xpath('//th[contains(.,"E-mail")]/../td/a')[0].get_attribute('href').split(':')[1])
            else:
                contactEmails.append(" ")

            if self.driver.find_elements_by_xpath('//th[contains(.,"Link")]/../td/a') != []:
                self.driver.find_element_by_xpath('//th[contains(.,"Link")]/../td/a').click()
                newWebsiteUrl= self.driver.find_element_by_xpath('//th[contains(.,"Link")]/../td/a').get_attribute('href')
                print("loading!")
                self.driver.get(newWebsiteUrl)
                print("loaded")
                print(self.driver.current_url)
                print(self.driver.get)
                websites.append(self.driver.current_url)
            else:
                websites.append(" ")


        print("RESULTS!:")
        print("\nAWARD NAMES:")
        for item in awardNames:
            print(item)
        print("\nFIELDS:")
        for item in fields:
            print(item)
        print("\nDESCRIPTIONS:")
        for item in descriptions:
            print(item)
        print("\nNATIONALITIES:")
        for item in nationalities:
            print(item)
        print("\nHOST COUNTRIES:")
        for item in hostCountries:
            print(item)
        print("\nIN-SITE URLS")
        for item in inSiteUrls:
            print(item)





    
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except:
            return False
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
