from Classes.SUDBConnect import SUDBConnect


def getEmptyTagAbstracts():
    db = SUDBConnect()

    emptyTagRows = db.getRowsDB("select * from dbo.PivotTags where ISNULL(Tag, '') = ''")
    emptyTagAbstracts = []
    for row in emptyTagRows:
        emptyTagAbstracts.append(row.Abstract)

    return emptyTagAbstracts


def insertTag(abstract, tag):
    db = SUDBConnect()
    db.insertUpdateOrDeleteDB("update dbo.PivotTags set Tag='" + tag + "' where Abstract='" + abstract + "'")


abstractsList = getEmptyTagAbstracts()
print(abstractsList)

'''
for abstract in abstractsList:
    print(abstract)
    tag = input("Tag: ")
    insertTag(abstract, tag)
'''
