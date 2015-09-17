from Classes.RunBadScholarshipClassifier import RunBadScholarshipClassifier
from Classes.GrantForwardItemsGetDatabaseInfo import GrantForwardItemsGetDatabaseInfo


class RunBadScholarshipClassifierOnGrantForwardItems(RunBadScholarshipClassifier):
    def __init__(self):
        grantForwardInfo = GrantForwardItemsGetDatabaseInfo(tag='Scholarship')

        self.sponsorList = grantForwardInfo.getSponsors()

        self.descriptions = grantForwardInfo.getDescriptions()
        self.eligibility = grantForwardInfo.getEligibilities()
        self.textList = []

        for i in range(len(self.descriptions)):
            description = self.descriptions[i]
            eligibility = self.eligibility[i]

            infoText = '%s %s' % (description, eligibility)
            self.textList.append(infoText)

        self.listGrantForwardItemIds = grantForwardInfo.getGrantForwardItemIds()
        self.tableName = 'GrantForwardItems'
        self.idColumnName = 'GrantForwardItemId'

        RunBadScholarshipClassifier.__init__(self, self.sponsorList, self.textList)
        self.getPredictedBadInsertIntoDatabase(self.tableName, self.idColumnName, self.listGrantForwardItemIds)


RunBadScholarshipClassifierOnGrantForwardItems()
