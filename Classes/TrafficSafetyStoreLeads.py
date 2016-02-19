from selenium import webdriver
from Classes.CleanText import CleanText
from Classes.RipPage import RipPage


class TrafficSafetyStoreLeads(object):
    def __init__(self):
        self.driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        self.base_url = 'https://www.trafficsafetystore.com/resources/teen-safe-driving-scholarships'
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(2)

    def getLeads(self):
        titlesList = self.getTitlesList()
        descriptionsList = self.getDescriptionsList()
        eligibilitiesList = self.getEligibilitiesList()
        awardsList = self.getAwardsList()
        deadlinesList = self.getDeadlinesList()
        sourceWebsitesList, sourceTextsList = self.getSourceWebsitesAndSourceTexts()

    def getTitlesList(self):
        titleDivs = self.driver.find_elements_by_xpath("//h2[@class='col-xs-12']")
        titlesList = [titleDiv.get_attribute('textContent') for titleDiv in titleDivs]

        titlesList = [CleanText.cleanALLtheText(title) for title in titlesList]

        return titlesList

    def getDescriptionsList(self):
        descriptionDivs = self.driver.find_elements_by_xpath("//div[@class='col-md-10 col-md-offset-1']/div[1]/p[1]")
        descriptionsList = [descriptionDiv.get_attribute('textContent') for descriptionDiv in descriptionDivs]

        descriptionsList = [CleanText.cleanALLtheText(description) for description in descriptionsList]

        return descriptionsList

    def getAwardsList(self):
        awardDivs = self.driver.find_elements_by_xpath("//div[@class='col-md-10 col-md-offset-1']/div[2]/p[1]")
        awardsList = [awardDiv.get_attribute('textContent') for awardDiv in awardDivs]

        awardsList = [CleanText.cleanALLtheText(award) for award in awardsList]

        return awardsList

    def getEligibilitiesList(self):
        eligibilityDivs = self.driver.find_elements_by_xpath("//div[@class='col-md-10 col-md-offset-1']/div[1]/p[2]")
        eligbilitiesList = [eligibilityDiv.get_attribute('textContent') for eligibilityDiv in eligibilityDivs]

        eligbilitiesList = [CleanText.cleanALLtheText(eligibility) for eligibility in eligbilitiesList]

        return eligbilitiesList

    def getDeadlinesList(self):
        deadlineDivs = self.driver.find_elements_by_xpath("//div[@class='col-md-10 col-md-offset-1']/div[2]/p[2]")
        deadlinesList = [deadlineDiv.get_attribute('textContent') for deadlineDiv in deadlineDivs]

        deadlinesList = [CleanText.cleanALLtheText(deadline) for deadline in deadlinesList]

        return deadlinesList

    def getSourceWebsitesAndSourceTexts(self):
        sourceWebsiteDivs = self.driver.find_elements_by_xpath("//div[@class='col-xs-8 col-xs-offset-2']/a")
        sourceWebsitesList = [sourceWebsiteDiv.get_attribute('href') for sourceWebsiteDiv in sourceWebsiteDivs]

        sourceTextsList = [RipPage.getPageSource(sourceWebsite) for sourceWebsite in sourceWebsitesList]

        return sourceWebsitesList, sourceTextsList

    def checkIfElementExists(self, xpath):
        checkElementExists = self.driver.find_elements_by_xpath(xpath)
        if checkElementExists != []:
            return True
        else:
            return False
