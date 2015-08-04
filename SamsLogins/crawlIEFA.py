from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest, time

class CrawlIEFA(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
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
        selectSize = Select(self.driver.find_element_by_id("pageSize"))
        selectSize.select_by_index(0) #Index of 0 selects 10 per page.

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
        addresses = []
        phoneNumbers = []
        faxes = []
        numberAwards = []

        currentPage = 1

        time.sleep(0.6)

        while self.is_element_present(By.XPATH,'//ul/li[@class="next"]'):
            print("Found NEXT button. Scraping page " + str(currentPage))

            awardNameObjects = self.driver.find_elements_by_xpath('//tbody/tr/td[1]/a')
            nationalityObjects = self.driver.find_elements_by_xpath('//tbody/tr/td[3]/p[1]')
            hostCountryObjects = self.driver.find_elements_by_xpath('//tbody/tr/td[3]/p[2]')

            print("Found objects")
            print(awardNameObjects[0])
            print(awardNameObjects[0].text)

            while awardNameObjects[0].text == "FEATURED":
            # the first few have to do with the "featured scholarship" which appears on the first page. They should be "FEATURED" and [], respectively, and should not be in the list.
                awardNameObjects.pop(0)
                awardNameObjects.pop(0)

            for item in awardNameObjects:
                awardNames.append(item.text)
                inSiteUrls.append(item.get_attribute("href"))
            for item in nationalityObjects:
                nationalities.append(item.text)
            for item in hostCountryObjects:
                hostCountries.append(item.text)

            nextPageButton = self.driver.find_element_by_xpath("//a[contains(.,'Next >')]")
            nextPageButton.click()
            time.sleep(0.6) #otherwise it tries to jump the gun and returns some really weird errors
            currentPage += 1
            print("Going to next page\n")
            #break #<---uncomment this out for testing purposes

        print("Broken out of loop. Visiting in-site URLs.")


        for item in inSiteUrls:

            print("Visiting " + item + " ...")
            self.driver.get(item)

            if self.driver.find_elements_by_xpath('//h4[contains(.,"Submission Deadline")]/../p') != []:
                submissionDeadlines.append(self.driver.find_elements_by_xpath('//h4[contains(.,"Submission Deadline")]/../p')[0].text)
            else:
                submissionDeadlines.append("none found")

            if self.driver.find_elements_by_xpath('//h4[contains(.,"Field(s) of Study")]/../p') != []:
                fields.append(self.driver.find_elements_by_xpath('//h4[contains(.,"Field(s) of Study")]/../p')[0].text)
            else:
                fields.append("none found")

            if self.driver.find_elements_by_xpath('//h4[contains(.,"Description")]/../p[1]') != []:
                descriptions.append(self.driver.find_elements_by_xpath('//h4[contains(.,"Description")]/../p[1]')[0].text)
            else:
                descriptions.append("none found")

            if self.driver.find_elements_by_xpath('//h4[contains(.,"Other Criteria")]') != []:
                otherCriteria.append(self.driver.find_elements_by_xpath('//h4[contains(.,"Other Criteria")]/../p[2]')[0].text)
            else:
                otherCriteria.append("none found")

            if self.driver.find_elements_by_xpath('//th[contains(.,"E-mail")]/../td/a') != []:
                contactEmails.append(self.driver.find_elements_by_xpath('//th[contains(.,"E-mail")]/../td/a')[0].get_attribute('href').split(':')[1])
            else:
                contactEmails.append("none found")

            if self.driver.find_elements_by_xpath('//h4[contains(.,"Award Amount")]/../p') != []:
                awardAmounts.append(self.driver.find_elements_by_xpath('//h4[contains(.,"Award Amount")]/../p')[0].text)
            else:
                awardAmounts.append("none found")

            if self.driver.find_elements_by_xpath('//th[contains(.,"Address")]/../td') != []:
                addresses.append(self.driver.find_elements_by_xpath('//th[contains(.,"Address")]/../td')[0].text)
            else:
                addresses.append("none found")

            if self.driver.find_elements_by_xpath('//th[contains(.,"Phone")]/../td') != []:
                phoneNumbers.append(self.driver.find_elements_by_xpath('//th[contains(.,"Phone")]/../td')[0].text)
            else:
                phoneNumbers.append("none found")

            if self.driver.find_elements_by_xpath('//th[contains(.,"Fax")]/../td') != []:
                faxes.append(self.driver.find_elements_by_xpath('//th[contains(.,"Fax")]/../td')[0].text)
            else:
                faxes.append("none found")

            if self.driver.find_elements_by_xpath('//th[contains(.,"Number of Awards")]/../td') != []:
                numberAwards.append(self.driver.find_elements_by_xpath('//th[contains(.,"Number of Awards")]/../td')[0].text)
            else:
                numberAwards.append("none found")





            if self.driver.find_elements_by_xpath('//th[contains(.,"Link")]/../td/a') != []:
                newWebsiteUrl= self.driver.find_element_by_xpath('//th[contains(.,"Link")]/../td/a').get_attribute('href')
                print("loading!")
                self.driver.get(newWebsiteUrl)
                print("loaded")
                print(self.driver.current_url)
                websites.append(self.driver.current_url)
            else:
                websites.append("none found")
                print("No website found")

        #print everything (probably could have done this with a dictionary but this seems less like a mess)
        allInfo = [awardNames,fields,descriptions,nationalities,hostCountries,inSiteUrls,submissionDeadlines,fields,otherCriteria,contactEmails,websites,awardAmounts,addresses,phoneNumbers,faxes,numberAwards]
        allInfoStrings = ["awardNames","fields","descriptions","nationalities","hostCountries","inSiteUrls","submissionDeadlines","fields","otherCriteria","contactEmails","websites","awardAmounts","addresses","phoneNumbers","faxes","numberAwards"]
        for info in allInfo:
            print("\n" + allInfoStrings[allInfo.index(info)] + ":")
            for item in info:
                print(item)

        print("\nPrinting characteristics of the 9th scholarship to check whether anything messed up...\n")
        for info in allInfo:
            assert(len(awardNames) == len(info))
            print(info[9])




    
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except:
            return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
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
