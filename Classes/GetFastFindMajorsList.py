from Classes.SUDBConnect import SUDBConnect


class GetFastFindMajorsList(object):
    def __init__(self):
        fastFindMajorsList = []
        db = SUDBConnect()
        rows = db.getRows(
            "select replace( ValueShown, '(' + OtherValuesToCheck + ')', '') as Major from dbo.FastFindLists where AttributeId=417")
        for row in rows:
            fastFindMajorsList.append(row.Major)

        return fastFindMajorsList
