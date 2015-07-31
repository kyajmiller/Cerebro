import sys
import nltk
import ast
from LoopPopulateGrantForwardRequirementsOverMajorsList import \
    LoopPopulateGrantForwardRequirementsOverMajorsList

nltk.download('punkt')

argvMajors = ''
if sys.argv[1] == 'All':
    argvMajors = sys.argv[1]
else:
    inputList = ast.literal_eval(sys.argv[1])
    if type(inputList) == list:
        argvMajors = inputList
        print(argvMajors)

LoopPopulateGrantForwardRequirementsOverMajorsList(argvMajors).run()
