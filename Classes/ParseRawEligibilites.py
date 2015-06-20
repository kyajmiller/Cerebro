from  Classes.RawEligibilityInput import RawEligibityInput
from Classes.ParseRawEligibility import ParseRawEligibility
class ParseRawEligibilites(object):
    def __init__(self,arrayOfRawEligibilities):
        self.arrayOfRawEligibilities = arrayOfRawEligibilities
        self.resultListOfScholarshipPackageRequirements=[]
        for rawEliligibility in arrayOfRawEligibilities:
            isValidObject=isinstance(rawEliligibility,RawEligibityInput)
            if isValidObject:
                resultListFromParser=ParseRawEligibility(rawEliligibility)
                self.arrayOfRawEligibilities.append(resultListFromParser)


