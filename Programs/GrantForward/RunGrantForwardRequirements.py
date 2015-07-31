import sys
import nltk
from LoopPopulateGrantForwardRequirementsOverMajorsList import \
    LoopPopulateGrantForwardRequirementsOverMajorsList

nltk.download('punkt')
argvNumberOfMajors = sys.argv[1]
if sys.argv[1] != 'All':
    argvNumberOfMajors = int(argvNumberOfMajors)
LoopPopulateGrantForwardRequirementsOverMajorsList(argvNumberOfMajors).run()
