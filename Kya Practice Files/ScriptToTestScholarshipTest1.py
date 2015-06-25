from Classes.ScanText import ScanText

with open('ScholarshipTest1.txt', 'r') as filein:
    wholefile = ''.join(filein)

    test = ScanText(wholefile)
    test.processText()
