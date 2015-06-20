from Classes.RawEligibilityInput import RawEligibityInput

class ParseRawEligibility(object):
    def __init__(self,rawEligibility):
        self.rawEligibility = rawEligibility
        self.listOfReturnedScholarshipPackageIds=[]
        #do each parser colleccted list and appeneding to this list
