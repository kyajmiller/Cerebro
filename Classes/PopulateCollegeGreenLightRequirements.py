from Classes.PopulateRequirements import PopulateRequirements
from Classes.CollegeGreenLightLeadsGetDatabaseInfo import CollegeGreenLightLeadsGetDatabaseInfo


class PopulateCollegeGreenLightRequirements(PopulateRequirements):
    def __init__(self):
        self.columnNames = ['CollegeGreenLightLeadId', 'AttributeId', 'AttributeValue']
        self.tableName = 'CollegeGreenLightRequirements'
        PopulateRequirements.__init__(self, self.tableName, self.columnNames)


    def loopThroughLeadsAndDoStuff(self):
        collegeGreenLightDataInfo = CollegeGreenLightLeadsGetDatabaseInfo()
        listOfCollegeGreenLightLeadsIds = collegeGreenLightDataInfo.getCollegeGreenLightLeadsIds()
        listOfConcatenatedDescriptionSourceText = collegeGreenLightDataInfo.getConcatenatedDescriptionSourceText()

        for i in range(len(listOfCollegeGreenLightLeadsIds)):
            collegeGreenLightLeadId = listOfCollegeGreenLightLeadsIds[i]

            descriptionSourceText = listOfConcatenatedDescriptionSourceText[i]
            descriptionSourceTextSentences = self.tokenizeIntoSentences(descriptionSourceText)

            gpa = self.getGPAFromSentences(descriptionSourceTextSentences)
            majors = self.getMajorFromSentences(descriptionSourceTextSentences)

            self.doDatabaseInsertsGPAMajor(collegeGreenLightLeadId, gpa, majors)

PopulateCollegeGreenLightRequirements().loopThroughLeadsAndDoStuff()
