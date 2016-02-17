from selenium import webdriver


class RipPage(object):
    @staticmethod
    def getPageSource(url):
        # driver = webdriver.Firefox()
        driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        htmlSource = ''
        try:
            driver.get(url)
            htmlSource = driver.page_source
        except:
            htmlSource = 'Page load timeout, source not found.'
        driver.quit()

        return htmlSource
