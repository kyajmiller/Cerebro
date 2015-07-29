import SamsLogins.FastWebClass as FastWebClass

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
            newScholarship =  FastWebClass(self.names[page],self.searchTerms[page])
            self.FastWebPages.append(newScholarship)

