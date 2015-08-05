from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Academicinvest(unittest.TestCase):

    # big search
    names = []
    urls = []

    # little search
    websites = []
    abouts = []
    providers = []
    emails = []
    fields_of_study = []
    schools_of_study = []
    levels_of_study = []
    essays = []
    essay_details = []
    application_information = []
    eligibility = []
    amounts = []
    deadlines = []

    all_info = [names, urls, websites, abouts, providers, emails, fields_of_study, schools_of_study, levels_of_study,
                essays, essay_details, application_information, eligibility, amounts, deadlines]

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(1.5)
        self.driver.get("http://scholarships.academicinvest.com/")
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.find_element_by_link_text("Any Majors Scholarships").click()

    def test_academicinvest(self):
        """This is the main function to run!"""

        self.scan_big_page()
        for url in self.urls:
            self.scan_small_page(url)
        self.print_all_info()

    def scan_big_page(self):
        name_objects = self.driver.find_elements_by_xpath("//h2/a")

        for name in name_objects:
            print(self.names.count(name.text), end=" ")
            if self.names.count(name.text) == 0:
                self.names.append(name.text)
                self.urls.append(name.get_attribute('href'))
            else:
                print("\nWe already have this. silly computer")

        print("\n")

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

        website_object = self.driver.find_elements_by_xpath(
            "//div[@class='field-label' and contains(.,'More Information')]/../descendant::a")
        if website_object != []:
            self.websites.append(website_object[0].get_attribute('href'))
        else:
            self.websites.append("none found")

        about_object = self.driver.find_elements_by_xpath(
            "//div[@class='field-label' and contains(.,'About')]/../descendant::div[@class = 'field-item even']")
        if about_object != []:
            self.abouts.append(about_object[0].text)
        else:
            self.abouts.append("none found")

        if "\u2010" in self.abouts[len(self.abouts)-1]:
            print("replace")
            self.abouts[len(self.abouts)-1] = self.abouts[len(self.abouts)-1].replace("\u2010","-")

        provider_object = self.driver.find_elements_by_xpath(
            "//div[@class='field-label' and contains(.,'Provided By')]/../descendant::div[@class = 'field-item even']")
        if provider_object != []:
            self.providers.append(provider_object[0].text)
        else:
            self.providers.append("none found")

        email_object = self.driver.find_elements_by_xpath(
            "//div[@class='field-label' and contains(.,'Contact e-mail')]/../descendant::div[@class = 'field-item even']")
        if email_object != []:
            self.emails.append(email_object[0].text)
        else:
            self.emails.append("none found")

        field_of_study_object = self.driver.find_elements_by_xpath(
            "//div[@class='field-label' and contains(.,'Field(s)')]/../descendant::div[@class = 'field-item even']")
        if field_of_study_object != []:
            self.fields_of_study.append(field_of_study_object[0].text)
        else:
            self.fields_of_study.append("none found")

        school_of_study_object = self.driver.find_elements_by_xpath(
            "//div[@class='field-label' and contains(.,'Provided By')]/../descendant::div[@class = 'field-item even']")
        if school_of_study_object != []:
            self.schools_of_study.append(school_of_study_object[0].text)
        else:
            self.schools_of_study.append("none found")

        level_of_study_object = self.driver.find_elements_by_xpath(
            "//div[@class='field-label' and contains(.,'Level of Study')]/../descendant::div[@class = 'field-item even']")
        if level_of_study_object != []:
            self.levels_of_study.append(level_of_study_object[0].text)
        else:
            self.levels_of_study.append("none found")

        essay_object = self.driver.find_elements_by_xpath(
            "//div[@class='field-label' and contains(.,'Essay:')]/../descendant::div[@class = 'field-item even']")
        if essay_object != []:
            self.essays.append(essay_object[0].text)
        else:
            self.essays.append("none found")

        essay_details_object = self.driver.find_elements_by_xpath(
            "//div[@class='field-label' and contains(.,'Essay Details')]/../descendant::div[@class = 'field-item even']")
        if essay_details_object != []:
            self.essay_details.append(essay_details_object[0].text)
        else:
            self.essay_details.append("none found")

        application_information_object = self.driver.find_elements_by_xpath(
            "//div[@class='field-label' and contains(.,'Application Information')]/../descendant::span")
        if application_information_object != []:
            self.application_information.append(application_information_object[0].text)
        else:
            self.application_information.append("none found")

        eligibility_xpath = self.driver.find_elements_by_xpath(
            "//div[@class='field-label' and contains(.,'Eligibility')]/../descendant::p")
        if eligibility_xpath != []:
            eligibility_list = []
            for item in eligibility_xpath:
                eligibility_list.append(item.text)
            eligibility_object = str(eligibility_list)
            self.eligibility.append(eligibility_object)
        else:
            self.eligibility.append("none found")

        amount_object = self.driver.find_elements_by_xpath(
            "//div[@class='field-label' and contains(.,'Amount')]/../descendant::div[@class = 'field-item even']")
        if amount_object != []:
            self.amounts.append(amount_object[0].text)
        else:
            self.amounts.append("none found")

        deadline_object = self.driver.find_elements_by_xpath(
            "//div[@class='field-label' and contains(.,'Deadline')]/../descendant::div[@class = 'field-item even']")
        if deadline_object != []:
            self.deadlines.append(deadline_object[0].text)
        else:
            self.deadlines.append("none found")



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
