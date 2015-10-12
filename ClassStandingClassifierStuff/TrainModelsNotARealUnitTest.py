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

    def test_trainPhDLevelGraduateModel(self):
        classStatus = 'Ph.D. Level Graduate'
        fileClassStatus = 'PhDLevelGraduate'
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()

    def test_trainNonDegreeSeekingGraduateModel(self):
        classStatus = 'Non-degree Seeking Graduate'
        fileClassStatus = 'NonDegreeSeekingGraduate'
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()

    def test_trainMedicalSchoolStudentModel(self):
        classStatus = 'Medical School Student'
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()

    def test_trainPharmacySchoolStudentModel(self):
        classStatus = 'Pharmacy School Student'
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()

    def test_trainDNPModel(self):
        classStatus = 'DNP'
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()

    def test_trainPostBaccalaureateModel(self):
        classStatus = 'Post-Baccalaureate'
        fileClassStatus = 'PostBaccalaureate'
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()

    def test_trainPostdoctoralModel(self):
        classStatus = 'Postdoctoral'
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()

if __name__ == '__main__':
    unittest.main()
