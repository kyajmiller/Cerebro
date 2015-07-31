import sys
from Programs.Pivot.Pivot_LoopPopulatePivotLeadRequirementsOverMajorsList import \
    LoopPopulatePivotLeadRequirementsOverMajorsList

argvNumberOfMajors = sys.argv[1]
LoopPopulatePivotLeadRequirementsOverMajorsList(argvNumberOfMajors).run()
