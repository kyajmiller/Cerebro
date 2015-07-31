import sys
import nltk
from Classes.LoopPopulateGrantForwardRequirementsOverMajorsList import \
    LoopPopulateGrantForwardRequirementsOverMajorsList

nltk.download('punkt')
argvNumberOfMajors = sys.argv[1]
LoopPopulateGrantForwardRequirementsOverMajorsList(argvNumberOfMajors).run()
