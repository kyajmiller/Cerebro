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

        self.scan_full_big_page()
        for url in self.urls:
            self.scan_small_page(url)
        self.print_all_info()

    def scan_big_page(self):
        name_objects = self.driver.find_elements_by_xpath("//h2/a")

        for name in name_objects:
            print(self.names.count(name.text),end=" ")
            print("\n")
            if self.names.count(name.text) == 0:
                self.names.append(name.text)
                self.urls.append(name.get_attribute('href'))
            else:
                print("We already have this. silly computer")

    def scan_full_big_page(self):
        while True:
            print(self.driver.current_url)
            self.scan_big_page()
            next_button = self.driver.find_elements_by_xpath("//li[contains(.,'next ')]/a")
            if next_button == []:
                return
            else:
                next_button[0].click()

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

            # assert it's all AOK
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
