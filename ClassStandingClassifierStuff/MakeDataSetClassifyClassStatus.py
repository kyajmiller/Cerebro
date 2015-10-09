from Classes.TokenizeOnWhitespacePunctuation import TokenizeOnWhitespacePunctuation
from Classes.StopwordsList import StopwordsList
from ClassStandingClassifierStuff.GetDatabaseInfoScholarshipsWithClassStatuses import \
    GetDatabaseInfoScholarshipsWithClassStatuses


class MakeDataSetClassifyClassStatus():
    def __init__(self, classStatusToUse):
        self.classStatusToUse = classStatusToUse
        self.isClassStatusDB = GetDatabaseInfoScholarshipsWithClassStatuses(requirementNeeded=self.classStatusToUse)
        self.notClassStatusDB = GetDatabaseInfoScholarshipsWithClassStatuses(requirementNeeded=self.classStatusToUse,
                                                                             useNot=True)

    def makeFeaturesSet(self):
