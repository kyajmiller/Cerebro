import re

engineeringString = 'The acceptable majors are mechanical, aerospace, systems, and industrial engineering meow meow meow.'
tokenizeEngingeeringString = re.findall(r"[\w']+", engineeringString)

for i in range(len(tokenizeEngingeeringString)):
    if tokenizeEngingeeringString[i] == 'engineering':
        engineeringContextSlice = tokenizeEngingeeringString[i - 5:i]
        engineeringWords = []
        for i in engineeringContextSlice:
            engineeringWords.append('%s engineering' % i)
        print(engineeringWords)
