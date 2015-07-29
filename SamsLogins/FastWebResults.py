import SamsLogins.FastWebClass as fastWebClass

class FastWebResults(object):
    def __init__(self, searchTerms, names,providers,awards):#Sam add every element in this array
        self.FastWebPages=[]
        self.searchTerms=searchTerms
        self.names=names
        self.providers=providers
        self.awards=awards
        self.isValid=True
        if (len(self.searchTerms) ==0):
                self.isValid=False
        else:
            if (len(self.searchTerms)!=(len(self.name))): #Sam do this for each item in arrawy
                self.isValid=False


    def addScholarshipToObject(self):
        if (self.isValid==False):
            return
        for page in range(0,len(self.searchTerms)):
            print(page)
            newScholarship =  fastWebClass.FastWebClass(self.names[page],self.searchTerms[page])
            self.FastWebPages.append(newScholarship)

