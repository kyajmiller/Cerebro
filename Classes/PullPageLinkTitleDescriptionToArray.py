import re
from Classes.RipPage import RipPage


class PullPageLinkTitleDescriptionToArray(object):
    def __init__(self, url):
        self.url = url
        self.htmlSource = RipPage.getPageSource(self.url)
        self.title = ''
        self.pageurl = ''
        self.allurlsonpage = []
        self.description = ''

    def getTitle(self):
        findTitle = re.search('<title>(.*?)</title>', self.htmlSource)
        if findTitle:
            self.title = findTitle.group(1)
            return self.title

    def getDescription(self):
        findDescription = re.search('<meta name="description" content="(.*?)"', self.htmlSource)
        if findDescription:
            self.description = findDescription.group(1)
        else:
            findDescription = re.search('<meta content="(.*?)" name="description', self.htmlSource)
            if findDescription:
                self.description = findDescription.group(1)

        return self.description

    def getPageURL(self):
        findPageURL = re.search('<link href="(.*?)" rel="canonical"', self.htmlSource)
        if findPageURL:
            self.pageurl = findPageURL.group(1)
        else:
            findPageURL = re.search('<link rel="canonical" href="(.*?)"', self.htmlSource)
            if findPageURL:
                self.pageurl = findPageURL.group(1)

        return self.pageurl

    def getAllURLsOnPage(self):
        findAllURLS = re.findall('<a href="(.*?)"', self.htmlSource)
        if findAllURLS:
            self.allurlsonpage = findAllURLS

        return self.allurlsonpage

    def arrayTitleDescriptionPageURLLinks(self):
        titleDescriptionPageURLLinks = [self.getTitle(), self.getDescription(), self.getPageURL(),
                                        self.getAllURLsOnPage()]
        return titleDescriptionPageURLLinks
