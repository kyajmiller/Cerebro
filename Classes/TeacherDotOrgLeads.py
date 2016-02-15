from selenium import webdriver
from Classes.CleanText import CleanText
from Classes.RipPage import RipPage


class TeacherDotOrgLeads(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'http://www.teacher.org/scholarships-grants/'
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(2)

        self.teacherDotOrgLeadArrays = []

    def getLeads(self):
        titleDivs = self.driver.find_elements_by_xpath("//h3[not(ancestor::div[@id='scholarship_intro_859'])]")

        for i in range(len(titleDivs)):
            title = titleDivs[i].get_attribute('textContent')
            requirements = ''
            sourceWebsite = ''

            if i == 0:
                description = self.driver.find_element_by_xpath("//div[@class='intro']/p").get_attribute('textContent')
                sourceWebsite = self.driver.find_element_by_xpath("//div[@class='intro']/p/a").get_attribute('href')
                requirementsListDivs = self.driver.find_elements_by_xpath(
                    "//div[@class='intro']/following-sibling::*[1][self::ul]/li")
                requirements = [requirementsListDiv.get_attribute('textContent') for requirementsListDiv in
                                requirementsListDivs]
            else:
                j = i + 1
                description = self.driver.find_element_by_xpath(
                    "//h3[not(ancestor::div[@id='scholarship_intro_859'])][%s]/following-sibling::p[1]" % j).get_attribute(
                    'textContent')
                if self.checkIfElementExists(
                                "//h3[not(ancestor::div[@id='scholarship_intro_859'])][%s]/following-sibling::p[2][(preceding-sibling::*[1][self::p])]" % j):
                    requirements = self.driver.find_element_by_xpath(
                        "//h3[not(ancestor::div[@id='scholarship_intro_859'])][%s]/following-sibling::p[2][(preceding-sibling::*[1][self::p])]" % j)

                if self.checkIfElementExists(
                                "//h3[not(ancestor::div[@id='scholarship_intro_859'])][%s]/following-sibling::p[1]/a" % j):
                    sourceWebsite = self.driver.find_element_by_xpath(
                        "//h3[not(ancestor::div[@id='scholarship_intro_859'])][%s]/following-sibling::p[1]/a" % j).get_attribute(
                        'href')
                elif self.checkIfElementExists(
                                "//h3[not(ancestor::div[@id='scholarship_intro_859'])][%s]/following-sibling::p[2][(preceding-sibling::*[1][self::p])]" % j):
                    if self.checkIfElementExists(
                                    "//h3[not(ancestor::div[@id='scholarship_intro_859'])][%s]/following-sibling::p[2][(preceding-sibling::*[1][self::p])]/a" % j):
                        sourceWebsite = self.driver.find_element_by_xpath(
                            "//h3[not(ancestor::div[@id='scholarship_intro_859'])][%s]/following-sibling::p[2][(preceding-sibling::*[1][self::p])]/a" % j).get_attribute(
                            'href')

            sourceText = RipPage.getPageSource(sourceWebsite)
            leadArray = [title, description, requirements, sourceWebsite, sourceText]
            self.teacherDotOrgLeadArrays.append(leadArray)

    def checkIfElementExists(self, xpath):
        checkElementExists = self.driver.find_elements_by_xpath(xpath)
        if checkElementExists != []:
            return True
        else:
            return False


TeacherDotOrgLeads().getLeads()
