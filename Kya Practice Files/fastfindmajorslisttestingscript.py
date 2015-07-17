from Classes.GetFastFindMajorsList import GetFastFindMajorsList
from Classes.SUDBConnect import SUDBConnect

db = SUDBConnect()
rows = db.getRows(
    "SELECT REPLACE(ValueShown, '(' + OtherValuesToCheck + ')','') as Major FROM dbo.FastFindLists WHERE AttributeId =417")
majorslist = []

for row in rows:
    majorslist.append(row.Major)

rows = db.getRows("SELECT DISTINCT Keyword FROM dbo.GrantForwardItems")
existingkeywordslist = []

for row in rows:
    existingkeywordslist.append(' ' + row.Keyword)

print(majorslist)
print(existingkeywordslist)

newmajorslist = []
for major in majorslist:
    if major in existingkeywordslist:
        newmajorslist.append(major)

print(newmajorslist)

anotherNewMajorsList = []
for major in existingkeywordslist:
    if major in majorslist:
        anotherNewMajorsList.append(major)

print(anotherNewMajorsList)
