import SamsLogins.FastWebClass as fastWebClass

class FastWebResults(object):
    def __init__(self, searchTerms, names,providers,awards):
        self.FastWebPages=[]
        self.searchTerms=searchTerms
        self.names=names
        self.providers=providers
        self.awards=awards

    def addScholarshipToObject(self):
        for page in range(0,len(self.searchTerms)):
            print(page)
            newScholarship =  fastWebClass.FastWebClass(self.names[page],self.searchTerms[page])
            self.FastWebPages.append(newScholarship)

