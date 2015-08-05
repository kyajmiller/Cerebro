from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Academicinvest(unittest.TestCase):

    names = []
    amounts = []
    regions_of_study = []
    urls = []
    deadlines = []
    essay = []
    level_of_study = []
    all_info = [names, amounts, regions_of_study, urls, deadlines, essay, level_of_study]

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.driver.get("http://scholarships.academicinvest.com/")
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.find_element_by_link_text("Any Majors Scholarships").click()


    def test_academicinvest(self):
        """This is the main function to run!"""
        self.scan_big_page()
        self.print_all_info()




    def scan_big_page(self):

        name_objects = self.driver.find_elements_by_xpath("//h2/a")
        amount_objects = self.driver.find_elements_by_xpath("//div[@class='field-label' and contains(.,'Amount')]/../div/div")
        region_objects = self.driver.find_elements_by_xpath("//div[@class='field-label' and contains(.,'Region of Study')]/../div/div")
        deadline_objects = self.driver.find_elements_by_xpath("//div[@class='field-label' and contains(.,'Deadline')]/../div/div")
        essay_objects = self.driver.find_elements_by_xpath("//div[@class='field-label' and contains(.,'Essay')]/../div/div")
        level_of_study_objects = self.driver.find_elements_by_xpath("//div[@class='field-label' and contains(.,'Level of Study')]/../div/div")

        for name in name_objects:
            self.names.append(name.text)
            self.urls.append(name.get_attribute('href'))
        for amount in amount_objects:
            self.amounts.append(amount.text)
        for region in region_objects:
            self.regions_of_study.append(region.text)
        for deadline in deadline_objects:
            self.deadlines.append(deadline.text)
        for essay in essay_objects:
            self.deadlines.append(essay.text)
        for level in level_of_study_objects:
            self.level_of_study.append(level.text)


    def scan_small_page(self, url):
        pass

    def print_all_info(self):
            for info in self.all_info:
                print("\n")
                for item in info:
                    print(item)

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
