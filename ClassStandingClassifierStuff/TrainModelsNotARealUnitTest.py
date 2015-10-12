import unittest
import re
from ClassStandingClassifierStuff.ClassifyClassStatusFromPreviouslyUntrainedModel import ClassifyClassStatusTrainFirst


class TestStringMethods(unittest.TestCase):
    def test_trainHighSchoolSeniorModel(self):
        classStatus = 'High School Senior'
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()

    def test_trainFreshmanModel(self):
        classStatus = 'Freshman'
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()

    def test_trainSophomoreModel(self):
        classStatus = 'Sophomore'
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()

    def test_trainJuniorModel(self):
        classStatus = 'Junior'
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()

    def test_trainSeniorModel(self):
        classStatus = 'Senior'
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()

    def test_trainMastersLevelGraduateModel(self):
        classStatus = 'High School Senior'
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()

    def test_seeIfCanWriteToFile(self):
        classStatus = 'Freshman'
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % classStatus
        outputFile = open(featuresValueCountsSaveFile, 'w')
        outputFile.write('cheese')
        outputFile.close()



if __name__ == '__main__':
    unittest.main()
