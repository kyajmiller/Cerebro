class ComputeAccuracy(object):
    def __init__(self, expectedResultsList, predictedResultsList):
        self.predictedResultsList = predictedResultsList
        self.expectedResultsList = expectedResultsList
        self.matches = 0
        self.total = 0
        self.accuracy = ''

    def getStats(self):
        for i in range(len(self.predictedResultsList)):
            self.total += 1
            expected = self.expectedResultsList[i]
            actual = self.predictedResultsList[i]

            if expected == actual:
                self.matches += 1

    def calculateAccuracy(self):
        self.getStats()
        self.accuracy = (self.matches / self.total) * 100
        return self.accuracy
