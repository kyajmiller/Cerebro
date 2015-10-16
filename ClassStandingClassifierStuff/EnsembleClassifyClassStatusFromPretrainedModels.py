from ClassStandingClassifierStuff.ClassifyClassStatusFromPretrainedModel import ClassifyClassStatusFromPretrainedModel


class EnsembleClassifyClassStatusFromPretrainedModels(object):
    def __init__(self, listTextsToClassify, listAssociatedIds):
        self.listTextsToClassify = listTextsToClassify
        self.listAssociatedIds = listAssociatedIds

    def doAllClassificationsAndReturnPredictionsListsById(self):
        highSchoolSeniorPredictions = self.classifyFromPretrainedModel('HighSchoolSenior')
        freshmanPredictions = self.classifyFromPretrainedModel('Freshman')
        sophomorePredictions = self.classifyFromPretrainedModel('Sophomore')
        juniorPredictions = self.classifyFromPretrainedModel('Junior')
        seniorPredictions = self.classifyFromPretrainedModel('Senior')
        mastersLevelGraduatePredictions = self.classifyFromPretrainedModel('MastersLevelGraduate')
        phdLevelGraduatePredictions = self.classifyFromPretrainedModel('PhDLevelGraduate')
        nonDegreeSeekingGraduatePredictions = self.classifyFromPretrainedModel('NonDegreeSeekingGraduate')
        medicalSchoolStudentPredictions = self.classifyFromPretrainedModel('MedicalSchoolStudent')
        pharmacySchoolStudentPredictions = self.classifyFromPretrainedModel('PharmacySchoolStudent')
        dnpPredictions = self.classifyFromPretrainedModel('DNP')
        postBaccalaureatePredictions = self.classifyFromPretrainedModel('PostBaccalaureate')
        postDoctoralPredictions = self.classifyFromPretrainedModel('Postdoctoral')

        listArrayOfIdsAndPredictions = []

    def classifyFromPretrainedModel(self, classStatusString):
        LRModelInputFile = 'ClassifierTrainedModels\%sClassStatusTrainedLRModel' % classStatusString
        featuresValueCountsInputFile = 'ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % classStatusString

        predictionsList = ClassifyClassStatusFromPretrainedModel(trainedModelInputFile=LRModelInputFile,
                                                                 trainedFeaturesValueCountsIndexesFile=featuresValueCountsInputFile,
                                                                 testingDataTextList=self.listTextsToClassify,
                                                                 testingDataIdsList=self.listAssociatedIds).returnPredictions()

        return predictionsList
