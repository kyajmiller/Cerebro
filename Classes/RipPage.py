from selenium import webdriver


class RipPage(object):
    @staticmethod
    def getPageSource(url):
        driver = webdriver.Firefox()
        htmlSource = ''
        try:
            driver.get(url)
            htmlSource = driver.page_source
        except:
            htmlSource = 'Page load timeout, source not found.'
        driver.quit()

        return htmlSource
