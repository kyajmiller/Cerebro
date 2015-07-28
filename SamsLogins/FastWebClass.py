class FastWebClass(object):
    def __init__(self, name="", provider="", award="", fastwebUrl="", deadline="", website="", awardType="", numberAvailable="", major="", additionalInfo=""):
        self.name=name
        self.provider=provider
        self.award=award
        self.fastwebUrl=fastwebUrl
        self.deadline=deadline
        self.website=website
        self.awardType=awardType
        self.numberAvailable=numberAvailable
        self.major=major
        self.additionalInfo=additionalInfo


    def showSam(self):
        self.Provider="test"

    def test_simple(self):
        self.assertEqual(1,1)
        test="meow"
        print(test)
        FastWebClass.name="Bob"
        print(FastWebClass.name)





