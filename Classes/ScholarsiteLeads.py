from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from Classes.CleanText import CleanText
from Classes.RipPage import RipPage


class ScholarsiteLeads(object):
    def __init__(self, isTest=False):
        self.isTest = isTest
        self.driver = webdriver.Firefox()
        self.base_url = "http://scholarsite.com/"

        self.driver.get(self.base_url + "/index.php?lang=en-US")
        self.driver.find_element_by_css_selector("li.item2 > a > span").click()
        self.driver.find_element_by_name('organization').clear()
        self.driver.find_element_by_name('organization').send_keys('University of Arizona')
        self.driver.find_element_by_id("ui-active-menuitem").click()
        self.driver.find_element_by_xpath("//button[@onclick='this.form.submit()']").click()
        self.driver.implicitly_wait(2)

    def getScholarshipsOnCurrentPage(self):
        arrayOfTitleDivs = self.driver.find_elements_by_xpath("//a[@title='Click to see scholarship']/strong")
        arrayOfTitles = []
        for titleDiv in arrayOfTitleDivs:
            title = titleDiv.get_attribute('textContent')
            arrayOfTitles.append(title)

        findViewScholarshipButtons = self.driver.find_elements_by_xpath("//span[@class='date']/em")
        for i in range(len(findViewScholarshipButtons())):
            button = findViewScholarshipButtons[i]
            button.click()

            activeWidgetALLSpanDivs = self.driver.find_elements_by_xpath(
                "//div[@class='ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom ui-accordion-content-active']/div/span")

            requirements = activeWidgetALLSpanDivs[0].get_attribute('textContent')
            annualAwards = activeWidgetALLSpanDivs[1].get_attribute('textContent')
            discipline = activeWidgetALLSpanDivs[2].get_attribute('textContent')
            academicLevel = activeWidgetALLSpanDivs[3].get_attribute('textContent')
            qualifiedMinorities = activeWidgetALLSpanDivs[4].get_attribute('textContent')
            eligibleInstitution = activeWidgetALLSpanDivs[5].get_attribute('textContent')
            eligibleRegion = activeWidgetALLSpanDivs[6].get_attribute('textContent')
            usCitizen = activeWidgetALLSpanDivs[7].get_attribute('textContent')
            usResident = activeWidgetALLSpanDivs[8].get_attribute('textContent')
            foreignNational = activeWidgetALLSpanDivs[9].get_attribute('textContent')
            minimumAge = activeWidgetALLSpanDivs[10].get_attribute('textContent')
            maximumAge = activeWidgetALLSpanDivs[11].get_attribute('textContent')
            classRank = activeWidgetALLSpanDivs[12].get_attribute('textContent')
            minimumGPA = activeWidgetALLSpanDivs[13].get_attribute('textContent')
            minimumACT = activeWidgetALLSpanDivs[14].get_attribute('textContent')
            minimumSAT = activeWidgetALLSpanDivs[15].get_attribute('textContent')
