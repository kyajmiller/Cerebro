# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CrawlScholarships360(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(6)
        self.base_url = "https://scholarships360.org"
        self.verificationErrors = []
        self.accept_next_alert = True
        ff = self.driver
        ff.get(self.base_url + "/")
        ff.find_element_by_link_text("Discover").click()
        time.sleep(5)
        ff.find_element_by_class_name("CoverPop-close").click()

    def test_crawl_scholarships360(self):

        driver = self.driver
        assert(driver.current_url == "https://scholarships360.org/discover-scholarships/")

        names = []
        inSiteLinks = []
        addedDates = []
        dueDates = []
        amounts = []
        eligibility = []
        websites = []
        emails = []
        scholarshipTypes = []

        numberPages = 1
        while driver.find_elements_by_link_text('Next »') != []:
            numberPages += 1
            driver.find_elements_by_link_text('Next »')[0].click()
            print("clicky")

        print("There are " + str(numberPages) + " pages.")
        driver.get('https://scholarships360.org/discover-scholarships/')

        while numberPages > 0:
            nameObjects = driver.find_elements_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/h2/a')
            for item in nameObjects:
                names.append(item.text)
                inSiteLinks.append(item.get_attribute('href'))
            if numberPages > 1:
                driver.find_elements_by_link_text('Next »')[0].click()
            print("meow")
            numberPages -= 1

        tags = []
        print("Names and inSiteLinks scanned.")
        for item in names:
            tags.append([])


        regexEmailFormat = re.compile("[\w0-9]+@[\w0-9]+\.[a-z]+")
        regexEligibleFormat = re.compile("eligible|Eligible")

        # for link in inSiteLinks:
        #
        #     driver.get(link)
        #     print("Visiting " + link)
        #     assert(link == driver.current_url)
        #
        #     originalAddedText = driver.find_element_by_xpath("//strong[contains(.,'Added')]/..").text
        #     addedDates.append(originalAddedText.split(": ")[1])
        #
        #     originalDueText = driver.find_element_by_xpath("//strong[contains(.,'Due')]/..").text
        #     dueDates.append(originalDueText.split(": ")[1])
        #
        #     originalAmountText = driver.find_element_by_xpath("//strong[contains(.,'Amount')]/..").text
        #     amounts.append(originalAmountText.split(": ")[1])
        #
        #     #mess to find the Eligibles
        #     allHeaders = driver.find_elements_by_xpath("//div[@class='entry-content']/h3") #Why is this so slow??? It's this command.
        #     eligiblesGroup = []
        #     for header in allHeaders:
        #         eligiblesFound = regexEligibleFormat.search(header.text)
        #         if eligiblesFound != None:
        #             eligiblesGroup.append(eligiblesFound.group(0))
        #             break
        #     if eligiblesGroup != []:
        #         eligibilityText = driver.find_elements_by_xpath("//h3[contains(.,'eligible') or contains(.,'Eligible')]/following-sibling::p[1]")[0].text
        #         print(eligibilityText)
        #         eligibility.append(eligibilityText)
        #     else:
        #         print("No eligibles :(")
        #         eligibility.append("none found")
        #
        #     #(less of a) mess to find the emails
        #     textParagraphs = driver.find_elements_by_xpath('//div[@class="entry-content"]/p')
        #     emailsGroup = []
        #     for paragraph in textParagraphs:
        #         emailsFound = regexEmailFormat.search(paragraph.text)
        #         if emailsFound != None:
        #             emailsGroup.append(emailsFound.group(0))
        #             break
        #     if emailsGroup != []:
        #         print(emailsGroup[0])
        #         emails.append(emailsGroup[0])
        #     else:
        #         print("There was no email.")
        #         emails.append("none found")
        #
        #     #get to their website
        #     applyButton = driver.find_element_by_xpath('//a[contains(.,"Apply")]')
        #     applyButton.click()
        #     print("At the website " + driver.current_url)
        #     websites.append(driver.current_url)
        selectCategory = Select(driver.find_element_by_id("tax_scholarship_category"))
        numberIterations = len(selectCategory.options)

        def searchCurrentPage(self):

            scholarshipNames = driver.find_elements_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/h2/a')

            if len(scholarshipNames) > 0:
                print(scholarshipNames[0])
                for scholarship in scholarshipNames:
                    print(scholarship.text)
                    try:
                        tagIndex = names.index(scholarship.text)
                        print(tagIndex)
                        tags[tagIndex].append(i)
                    except:
                        pass

            if len(nameObjects) >= 10: #This cuts down on search time so much!
                if driver.find_elements_by_link_text("Next »") != []:
                    print("There is a Next >>.")
                    driver.find_elements_by_link_text("Next »")[0].click()
                    searchCurrentPage(self)


        i = 1
        while i < numberIterations:
            selectCategory = Select(driver.find_element_by_id("tax_scholarship_category"))
            selectCategory.select_by_index(i)
            submitButton = driver.find_element_by_xpath('//input[@value="Search"]')
            submitButton.click()
            searchCurrentPage(self)
            i += 1

        allInfo = [names,inSiteLinks,addedDates,dueDates,amounts,eligibility,websites,emails,scholarshipTypes,tags]

        for infolist in allInfo:
            print("\n\n")
            for item in infolist:
                print(item)


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to.alert
        except NoAlertPresentException:
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
