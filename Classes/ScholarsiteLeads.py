#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from selenium import webdriver
from Classes.CleanText import CleanText


class ScholarsiteLeads(object):
    def __init__(self, isTest=False):
        self.isTest = isTest
        self.driver = webdriver.Firefox()
        self.base_url = "http://scholarsite.com/"

        self.driver.get(self.base_url + "/index.php?lang=en-US")
        self.driver.find_element_by_css_selector("li.item2 > a > span").click()
        self.driver.find_element_by_name('organization').clear()
        self.driver.find_element_by_name('organization').send_keys('University of Arizona')
        self.driver.find_element_by_xpath("//button[@onclick='this.form.submit()']").click()
        self.driver.implicitly_wait(2)

        self.scholarsiteLeadsArrays = []
        self.processResultsPages()

    def processResultsPages(self):
        self.getScholarshipsOnCurrentPage()

        currentPage = 1
        while currentPage < 5:
            self.goToNextPage()
            self.getScholarshipsOnCurrentPage()
            currentPage += 1

        self.driver.quit()
        return self.scholarsiteLeadsArrays

    def getScholarshipsOnCurrentPage(self):
        arrayOfTitles = self.getScholarshipTitles()
        arrayOfValues = self.getScholarshipValues()
        arrayOfDeadlines = self.getScholarshipDeadlines()
        arrayOfWidgetClickInfoArrays = self.getWidgetClickInfo()

        for i in range(len(arrayOfTitles)):
            title = arrayOfTitles[i]
            value = arrayOfValues[i]
            deadline = arrayOfDeadlines[i]
            widgetInfo = arrayOfWidgetClickInfoArrays[i]

            scholarshipArray = [title, value, deadline]
            for info in widgetInfo:
                scholarshipArray.append(info)

            scholarshipArray = [CleanText.cleanALLtheText(item) for item in scholarshipArray]

            self.scholarsiteLeadsArrays.append(scholarshipArray)

    def getScholarshipTitles(self):
        arrayOfTitleDivs = self.driver.find_elements_by_xpath("//a[@title='Click to see scholarship']/strong")
        arrayOfTitles = []
        for titleDiv in arrayOfTitleDivs:
            title = titleDiv.get_attribute('textContent')
            arrayOfTitles.append(title)

        return arrayOfTitles

    def getScholarshipValues(self):
        arrayOfValueDivs = self.driver.find_elements_by_xpath(
            "//a[@title='Click to see scholarship']/span[@class='location']/em")
        arrayOfValues = []
        for valueDiv in arrayOfValueDivs:
            value = valueDiv.get_attribute('textContent')
            arrayOfValues.append(value)

        return arrayOfValues

    def getScholarshipDeadlines(self):
        arrayOfDeadlineDivs = self.driver.find_elements_by_xpath(
            "//a[@title='Click to see scholarship']/span[@class='date']")
        arrayOfDeadlines = []
        for deadlineDiv in arrayOfDeadlineDivs:
            unformattedDeadline = deadlineDiv.get_attribute('textContent')
            splitUnformattedDeadline = unformattedDeadline.split(':', 1)
            unformattedDeadline = splitUnformattedDeadline[1]
            deadline = re.sub('» View Scholarship', '', unformattedDeadline)
            arrayOfDeadlines.append(deadline)

        return arrayOfDeadlines

    def getWidgetClickInfo(self):
        widgetClickInfoArrays = []

        findViewScholarshipButtons = self.driver.find_elements_by_xpath("//span[@class='date']/em")
        for button in findViewScholarshipButtons:
            button.click()

            activeWidgetALLSpanDivs = self.driver.find_elements_by_xpath(
                "//div[@class='ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom ui-accordion-content-active']/div/span")

            requirements = activeWidgetALLSpanDivs[0].get_attribute('textContent')
            requirements = re.sub('Requirements: ', '', requirements)

            annualAwards = activeWidgetALLSpanDivs[1].get_attribute('textContent')
            annualAwards = re.sub('Annual Awards: ', '', annualAwards)

            discipline = activeWidgetALLSpanDivs[2].get_attribute('textContent')
            discipline = re.sub('Discipline: ', '', discipline)

            academicLevel = activeWidgetALLSpanDivs[3].get_attribute('textContent')
            academicLevel = re.sub('Academic Level: ', '', academicLevel)

            qualifiedMinorities = activeWidgetALLSpanDivs[4].get_attribute('textContent')
            qualifiedMinorities = re.sub('Qualified Minorities: ', '', qualifiedMinorities)

            eligibleInstitution = activeWidgetALLSpanDivs[5].get_attribute('textContent')
            eligibleInstitution = re.sub('Eligible Institution: ', '', eligibleInstitution)

            eligibleRegion = activeWidgetALLSpanDivs[6].get_attribute('textContent')
            eligibleRegion = re.sub('Eligible Region: ', '', eligibleRegion)

            usCitizen = activeWidgetALLSpanDivs[7].get_attribute('textContent')
            usCitizen = re.sub('US Citizen: ', '', usCitizen)

            usResident = activeWidgetALLSpanDivs[8].get_attribute('textContent')
            usResident = re.sub('US Resident: ', '', usResident)

            foreignNational = activeWidgetALLSpanDivs[9].get_attribute('textContent')
            foreignNational = re.sub('Foreign National: ', '', foreignNational)

            minimumAge = activeWidgetALLSpanDivs[10].get_attribute('textContent')
            minimumAge = re.sub('Minimum Age: ', '', minimumAge)

            maximumAge = activeWidgetALLSpanDivs[11].get_attribute('textContent')
            maximumAge = re.sub('Maximum Age: ', '', maximumAge)

            classRank = activeWidgetALLSpanDivs[12].get_attribute('textContent')
            classRank = re.sub('Class Rank: ', '', classRank)

            minimumGPA = activeWidgetALLSpanDivs[13].get_attribute('textContent')
            minimumGPA = re.sub('Minimum GPA: ', '', minimumGPA)

            minimumACT = activeWidgetALLSpanDivs[14].get_attribute('textContent')
            minimumACT = re.sub('Minimum ACT: ', '', minimumACT)

            minimumSAT = activeWidgetALLSpanDivs[15].get_attribute('textContent')
            minimumSAT = re.sub('Minimum SAT: ', '', minimumSAT)

            unformattedArray = [requirements, annualAwards, discipline, academicLevel, qualifiedMinorities,
                                eligibleInstitution, eligibleRegion, usCitizen, usResident, foreignNational,
                                minimumAge, maximumAge, classRank, minimumGPA, minimumACT, minimumSAT]

            formattedArray = [re.sub(',$', '', item.strip()) for item in unformattedArray]

            widgetClickInfoArrays.append(formattedArray)

        return widgetClickInfoArrays

    def goToNextPage(self):
        self.driver.find_element_by_link_text('Next').click()
        self.driver.implicitly_wait(2)
