import sys

class PrintStuff(object):
    def __init__(self, thingToPrint):
        self.thingToPrint = thingToPrint
        print(self.thingToPrint)


printStuffArg = sys.argv[0]
PrintStuff(printStuffArg)
