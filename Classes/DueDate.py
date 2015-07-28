import re
from Classes.Parser import Parser


class DueDate(Parser):
    def __init__(self, stringToScan):
        self.stringToScan = stringToScan
        Parser.__init__(self, self.stringToScan, )
