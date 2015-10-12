import unittest
import re
from ClassStandingClassifierStuff.ClassifyClassStatusFromPreviouslyUntrainedModel import ClassifyClassStatusTrainFirst


class TestStringMethods(unittest.TestCase):
    def test_trainHighSchoolSeniorModel(self):
        classStatus = 'High School Senior'
        print("Training '%s' model..." % classStatus)
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainFreshmanModel(self):
        classStatus = 'Freshman'
        print("Training '%s' model..." % classStatus)
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainSophomoreModel(self):
        classStatus = 'Sophomore'
        print("Training '%s' model..." % classStatus)
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainJuniorModel(self):
        classStatus = 'Junior'
        print("Training '%s' model..." % classStatus)
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainSeniorModel(self):
        classStatus = 'Senior'
        print("Training '%s' model..." % classStatus)
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainMastersLevelGraduateModel(self):
        classStatus = 'High School Senior'
        print("Training '%s' model..." % classStatus)
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainPhDLevelGraduateModel(self):
        classStatus = 'Ph.D. Level Graduate'
        print("Training '%s' model..." % classStatus)
        fileClassStatus = 'PhDLevelGraduate'
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainNonDegreeSeekingGraduateModel(self):
        classStatus = 'Non-degree Seeking Graduate'
        print("Training '%s' model..." % classStatus)
        fileClassStatus = 'NonDegreeSeekingGraduate'
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainMedicalSchoolStudentModel(self):
        classStatus = 'Medical School Student'
        print("Training '%s' model..." % classStatus)
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainPharmacySchoolStudentModel(self):
        classStatus = 'Pharmacy School Student'
        print("Training '%s' model..." % classStatus)
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainDNPModel(self):
        classStatus = 'Doctor of Nursing Practice (DNP)'
        print("Training '%s' model..." % classStatus)
        fileClassStatus = 'DNP'
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainPostBaccalaureateModel(self):
        classStatus = 'Post-Baccalaureate'
        print("Training '%s' model..." % classStatus)
        fileClassStatus = 'PostBaccalaureate'
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainPostdoctoralModel(self):
        classStatus = 'Postdoctoral'
        print("Training '%s' model..." % classStatus)
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

if __name__ == '__main__':
    unittest.main()
