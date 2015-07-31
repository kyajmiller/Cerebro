import sys
from Pivot_LoopPopulatePivotLeadRequirementsOverMajorsList import LoopPopulatePivotLeadRequirementsOverMajorsList

argvNumberOfMajors = sys.argv[1]
if sys.argv[1] != 'All':
    argvNumberOfMajors = int(argvNumberOfMajors)
LoopPopulatePivotLeadRequirementsOverMajorsList(argvNumberOfMajors).run()
