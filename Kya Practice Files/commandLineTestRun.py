import sys
import ast

class PrintStuff(object):
    def __init__(self, thingToPrint):
        self.thingToPrint = thingToPrint
        print(self.thingToPrint)


'''
printStuffArg = sys.argv[1]
makeList = printStuffArg.split(', ')

PrintStuff(type(makeList))
print(makeList)
'''
if sys.argv[1] == 'All':
    print(type(sys.argv[1]))
    print(sys.argv[1])
else:
    inputTest = ast.literal_eval(sys.argv[1])
    print(type(inputTest))
    print(inputTest)
    if type(inputTest) == list:
        print(type(inputTest[0]))
        print(inputTest[0])
