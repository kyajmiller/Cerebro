import unittest
import re
from ClassStandingClassifierStuff.LogisticRegressionClassifyClassStatusFromPreviouslyUntrainedModel import \
    ClassifyClassStatusTrainFirst


class TestStringMethods(unittest.TestCase):
    def test_trainHighSchoolSeniorModel(self):
        classStatus = 'High School Senior'
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus

        # first check to see if can open files:
        testOpenModelSaveFile = open(modelSaveFile, 'rb')
        testOpenModelSaveFile.close()
        testOpenFVCSaveFile = open(featuresValueCountsSaveFile, 'rb')
        testOpenFVCSaveFile.close()

        # do training and save to files
        print("Training '%s' model..." % classStatus)
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainFreshmanModel(self):
        classStatus = 'Freshman'
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus

        # first check to see if can open files:
        testOpenModelSaveFile = open(modelSaveFile, 'rb')
        testOpenModelSaveFile.close()
        testOpenFVCSaveFile = open(featuresValueCountsSaveFile, 'rb')
        testOpenFVCSaveFile.close()

        # do training and save to files
        print("Training '%s' model..." % classStatus)
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainSophomoreModel(self):
        classStatus = 'Sophomore'
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus

        # first check to see if can open files:
        testOpenModelSaveFile = open(modelSaveFile, 'rb')
        testOpenModelSaveFile.close()
        testOpenFVCSaveFile = open(featuresValueCountsSaveFile, 'rb')
        testOpenFVCSaveFile.close()

        # do training and save to files
        print("Training '%s' model..." % classStatus)
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainJuniorModel(self):
        classStatus = 'Junior'
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus

        # first check to see if can open files:
        testOpenModelSaveFile = open(modelSaveFile, 'rb')
        testOpenModelSaveFile.close()
        testOpenFVCSaveFile = open(featuresValueCountsSaveFile, 'rb')
        testOpenFVCSaveFile.close()

        # do training and save to files
        print("Training '%s' model..." % classStatus)
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainSeniorModel(self):
        classStatus = 'Senior'
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus

        # first check to see if can open files:
        testOpenModelSaveFile = open(modelSaveFile, 'rb')
        testOpenModelSaveFile.close()
        testOpenFVCSaveFile = open(featuresValueCountsSaveFile, 'rb')
        testOpenFVCSaveFile.close()

        # do training and save to files
        print("Training '%s' model..." % classStatus)
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainMastersLevelGraduateModel(self):
        classStatus = 'Masters Level Graduate'
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus

        # first check to see if can open files:
        testOpenModelSaveFile = open(modelSaveFile, 'rb')
        testOpenModelSaveFile.close()
        testOpenFVCSaveFile = open(featuresValueCountsSaveFile, 'rb')
        testOpenFVCSaveFile.close()

        # do training and save to files
        print("Training '%s' model..." % classStatus)
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainPhDLevelGraduateModel(self):
        classStatus = 'Ph.D. Level Graduate'
        fileClassStatus = 'PhDLevelGraduate'
        modelSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus

        # first check to see if can open files:
        testOpenModelSaveFile = open(modelSaveFile, 'rb')
        testOpenModelSaveFile.close()
        testOpenFVCSaveFile = open(featuresValueCountsSaveFile, 'rb')
        testOpenFVCSaveFile.close()

        # do training and save to files
        print("Training '%s' model..." % classStatus)
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainNonDegreeSeekingGraduateModel(self):
        classStatus = 'Non-degree Seeking Graduate'
        fileClassStatus = 'NonDegreeSeekingGraduate'
        modelSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus

        # first check to see if can open files:
        testOpenModelSaveFile = open(modelSaveFile, 'rb')
        testOpenModelSaveFile.close()
        testOpenFVCSaveFile = open(featuresValueCountsSaveFile, 'rb')
        testOpenFVCSaveFile.close()

        # do training and save to files
        print("Training '%s' model..." % classStatus)
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainMedicalSchoolStudentModel(self):
        classStatus = 'Medical School Student'
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus

        # first check to see if can open files:
        testOpenModelSaveFile = open(modelSaveFile, 'rb')
        testOpenModelSaveFile.close()
        testOpenFVCSaveFile = open(featuresValueCountsSaveFile, 'rb')
        testOpenFVCSaveFile.close()

        # do training and save to files
        print("Training '%s' model..." % classStatus)
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainPharmacySchoolStudentModel(self):
        classStatus = 'Pharmacy School Student'
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus

        # first check to see if can open files:
        testOpenModelSaveFile = open(modelSaveFile, 'rb')
        testOpenModelSaveFile.close()
        testOpenFVCSaveFile = open(featuresValueCountsSaveFile, 'rb')
        testOpenFVCSaveFile.close()

        # do training and save to files
        print("Training '%s' model..." % classStatus)
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainDNPModel(self):
        classStatus = 'Doctor of Nursing Practice (DNP)'
        fileClassStatus = 'DNP'
        modelSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus

        # first check to see if can open files:
        testOpenModelSaveFile = open(modelSaveFile, 'rb')
        testOpenModelSaveFile.close()
        testOpenFVCSaveFile = open(featuresValueCountsSaveFile, 'rb')
        testOpenFVCSaveFile.close()

        # do training and save to files
        print("Training '%s' model..." % classStatus)
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainPostBaccalaureateModel(self):
        classStatus = 'Post-Baccalaureate'
        fileClassStatus = 'PostBaccalaureate'
        modelSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus

        # first check to see if can open files:
        testOpenModelSaveFile = open(modelSaveFile, 'rb')
        testOpenModelSaveFile.close()
        testOpenFVCSaveFile = open(featuresValueCountsSaveFile, 'rb')
        testOpenFVCSaveFile.close()

        # do training and save to files
        print("Training '%s' model..." % classStatus)
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

    def test_trainPostdoctoralModel(self):
        classStatus = 'Postdoctoral'
        fileClassStatus = re.sub(' ', '', classStatus)
        modelSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedLRModel' % fileClassStatus
        featuresValueCountsSaveFile = 'ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % fileClassStatus

        # first check to see if can open files:
        testOpenModelSaveFile = open(modelSaveFile, 'rb')
        testOpenModelSaveFile.close()
        testOpenFVCSaveFile = open(featuresValueCountsSaveFile, 'rb')
        testOpenFVCSaveFile.close()

        # do training and save to files
        print("Training '%s' model..." % classStatus)
        testClassify = ClassifyClassStatusTrainFirst(classStatus=classStatus, trainingPercentage=0.99,
                                                     modelSaveFile=modelSaveFile,
                                                     featuresValuesCountsSaveFile=featuresValueCountsSaveFile)
        testClassify.trainAndSaveModel()
        print("Training for '%s' complete." % classStatus)

if __name__ == '__main__':
    unittest.main()
