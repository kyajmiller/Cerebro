from Classes.ScanText import ScanText

with open('ScholarshipTest1.txt', 'r') as filein:
    wholefile = ''.join(filein)

    test = ScanText(wholefile)
    test.processText()

with open('ScholarshipTest2.txt', 'r') as filein:
    wholefile = ''.join(filein)

    test = ScanText(wholefile)
    # print(test.cleanText())
    test.processText()

with open('ScholarshipTest3.txt', 'r') as filein:
    wholefile = ''.join(filein)

    test = ScanText(wholefile)
    test.processText()
