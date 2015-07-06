import re
from Classes.RipPage import RipPage


class PullPageLinkTitleDescriptionToArray(object):
    def __init__(self, htmlSource):
        self.htmlSource = htmlSource
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


