import sys
import nltk
from LoopPopulatePivotLeadRequirementsOverMajorsList import LoopPopulatePivotLeadRequirementsOverMajorsList

nltk.download('punkt')
argvNumberOfMajors = sys.argv[1]
if sys.argv[1] != 'All':
    argvNumberOfMajors = int(argvNumberOfMajors)
LoopPopulatePivotLeadRequirementsOverMajorsList(argvNumberOfMajors).run()
