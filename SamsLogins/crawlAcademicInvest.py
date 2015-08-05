from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Academicinvest(unittest.TestCase):

    #big search
    names = []
    urls = []

    #little search

    all_info = [names, urls]

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.driver.get("http://scholarships.academicinvest.com/")
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.find_element_by_link_text("Any Majors Scholarships").click()


    def test_academicinvest(self):
        """This is the main function to run!"""


        number_next_clicks = self.num_pages()
        while number_next_clicks > 0:
            self.scan_big_page()
            print("Next page")
            number_next_clicks -= 1
            if number_next_clicks > 1:
                next_button = self.driver.find_elements_by_xpath("//li[contains(.,'next ')]/a")[0]
                print(next_button)
                next_button.click()
        self.scan_big_page()
        #scan little pages
        for url in self.urls:
            self.scan_small_page(url)
        #print data
        self.print_all_info()

    def num_pages(self):
        last_button = self.driver.find_elements_by_xpath("//li[contains(.,'last ')]/a")
        if last_button == []:
            print("No last page button")
            number_pages = 1
        else:
            number_pages = int(last_button[0].get_attribute('href').split("&page=")[1]) + 1
            print(str(number_pages))
        return number_pages


    def scan_big_page(self):

        name_objects = self.driver.find_elements_by_xpath("//h2/a")

        for name in name_objects:
            self.names.append(name.text)
            self.urls.append(name.get_attribute('href'))

    def scan_small_page(self, url):
        print("Visiting " + url)
        self.driver.get(url)
        assert(self.driver.current_url == url)
        print("AOK")

    def print_all_info(self):
            for info in self.all_info:
                print("\n")
                for item in info:
                    print(item)

            #assert it's all AOK
            for info in self.all_info:
                print(len(info), end=" ")
            print("\n")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
