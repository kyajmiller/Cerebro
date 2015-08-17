from selenium import webdriver


class FastWebLeads(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'http://www.fastweb.com/'

        self.driver.get(self.base_url)
        self.driver.find_element_by_xpath("//a[@class='login']").click()
        self.driver.find_element_by_id('login').clear()
        self.driver.find_element_by_id('login').send_keys('crawlyjones@gmail.com')
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys('sasgcoders')
        self.driver.find_element_by_id('user_form_submit').click()
        self.driver.implicitly_wait(2)

        self.driver.find_element_by_link_text('See my matches').click()
        self.driver.implicitly_wait(2)

        self.driver.find_element_by_xpath("//a[text() = 'All Matches']").click()
        self.driver.implicitly_wait(2)

        # go to next page
        self.driver.find_element_by_xpath("//a[text() = 'All Matches']").click()

    def goToNextPage(self):
        pass



test = FastWebLeads()
