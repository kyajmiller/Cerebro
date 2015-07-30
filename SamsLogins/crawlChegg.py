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
        time.sleep(3)
        driver.get("https://www.chegg.com/scholarships")
        print("It's not broken yet :D")
        print(self.driver.current_url)



    def test_crawl_chegg(self):
        names = []
        cheggurls = []
        deadlines = []
        amounts = []
        numberAwards = []
        scholarshipEligibility = []
        providerNames = []
        overviews = []

        linkObjects = self.driver.find_elements_by_xpath('//section/div/div[4]/a[2]')
        deadlineObjects = self.driver.find_elements_by_xpath('//section/div/div[2]')
        amountObjects = self.driver.find_elements_by_xpath('//section/div/div[1]')

        for item in deadlineObjects:
            deadlines.append(item.text)

        for item in amountObjects:
            amounts.append(item.text)

        for item in linkObjects:
            names.append(item.text)
            cheggurls.append(item.get_attribute('href'))

        for item in cheggurls:
            self.driver.get(item)
            currentUrlSplitList= self.driver.current_url.split('/')
            print("Currently visiting " +self.driver.current_url +".")
            if currentUrlSplitList[len(currentUrlSplitList)-1] != "apply":

               item=self.driver.find_elements_by_xpath('/html/body/div[3]/div[5]/div[2]/div[2]/div[2]/div[5]/div[1]/div[4]/span')
               numberAwardsObjects = self.driver.find_elements_by_xpath('/html/body/div[3]/div[5]/div[2]/div[2]/div[2]/div[5]/div[1]/div[4]/span')
               scholarshipEligibilityObjects = self.driver.find_elements_by_xpath('/html/body/div[3]/div[5]/div[2]/div[2]/div[2]/div[5]/div[2]/div[2]/span')
               providerNameObjects = self.driver.find_elements_by_xpath('/html/body/div[3]/div[5]/div[2]/div[2]/div[2]/div[5]/div[2]/div[5]/div[2]')
               overviewObjects = self.driver.find_elements_by_xpath('/html/body/div[3]/div[5]/div[2]/div[2]/div[2]/div[5]/div[2]/div[3]/div')

               if numberAwardsObjects == []:
                   numberAwards.append("unspecified")
               else:
                   numberAwards.append(numberAwardsObjects[0].text)

               if scholarshipEligibilityObjects == []:
                   scholarshipEligibility.append("unspecified")
               else:
                   scholarshipEligibility.append(scholarshipEligibilityObjects[0].text)

               if providerNameObjects == []:
                   providerNames.append("unspecified")
               else:
                   providerNames.append(providerNameObjects[0].text)

               if overviewObjects == []:
                   overviews.append("unspecified")
               else:
                   overviews.append(overviewObjects[0].text)

            else:
                providerNames.append("unspecified")
                numberAwards.append("unspecified")
                overviews.append("unspecified")

                scholarshipEligibilityObjects = self.driver.find_elements_by_xpath('/html/body/div[3]/div[5]/div[2]/div[2]/div[2]/main/div[2]/section[1]/div[5]/div[2]')

                if scholarshipEligibilityObjects == []:
                    scholarshipEligibility.append("unspecified")
                else:
                    scholarshipEligibility.append(scholarshipEligibilityObjects[0].text)



        for item in names:
            print(item)

        for item in cheggurls:
            print(item)

        for item in deadlines:
            print(item)

        for item in amounts:
            print(item)

        for item in scholarshipEligibility:
            print(item)

        for item in numberAwards:
            print(item)

        for item in providerNames:
            print(item)

        print(names[40]+" "+cheggurls[40]+" "+deadlines[40]+" "+amounts[40]+" "+scholarshipEligibility[40]+" "+numberAwards[40]+" "+providerNames[40])






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
