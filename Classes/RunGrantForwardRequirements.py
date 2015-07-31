import sys
from Classes.LoopPopulateGrantForwardRequirementsOverMajorsList import \
    LoopPopulateGrantForwardRequirementsOverMajorsList

argvNumberOfMajors = sys.argv[1]
LoopPopulateGrantForwardRequirementsOverMajorsList(argvNumberOfMajors).run()
