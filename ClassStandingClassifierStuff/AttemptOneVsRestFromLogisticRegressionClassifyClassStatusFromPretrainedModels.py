from ClassStandingClassifierStuff.ClassifyClassStatusFromPretrainedModel import ClassifyClassStatusFromPretrainedModel


class EnsembleClassifyClassStatusFromPretrainedModels(object):
    def __init__(self, listTextsToClassify, listAssociatedIds):
        self.listTextsToClassify = listTextsToClassify
        self.listAssociatedIds = listAssociatedIds

    def doAllClassificationsAndReturnFilteredPredictionsListsById(self):
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
        postdoctoralPredictions = self.classifyFromPretrainedModel('Postdoctoral')

        listArrayOfIdsAndFilteredPredictions = []

        for i in range(len(self.listAssociatedIds) - 1):
            id = self.listAssociatedIds[i]

            unfilteredPredictionsList = [highSchoolSeniorPredictions[i], freshmanPredictions[i],
                                         sophomorePredictions[i], juniorPredictions[i], seniorPredictions[i],
                                         mastersLevelGraduatePredictions[i], phdLevelGraduatePredictions[i],
                                         nonDegreeSeekingGraduatePredictions[i], medicalSchoolStudentPredictions[i],
                                         pharmacySchoolStudentPredictions[i], dnpPredictions[i],
                                         postBaccalaureatePredictions[i], postdoctoralPredictions[i]]

            filteredPredictionsList = self.filterOutOtherPredictions(unfilteredPredictionsList)

            idAndFilteredPredictionsArray = [id, filteredPredictionsList]
            listArrayOfIdsAndFilteredPredictions.append(idAndFilteredPredictionsArray)

        return listArrayOfIdsAndFilteredPredictions

    def classifyFromPretrainedModel(self, classStatusString):
        LRModelInputFile = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % classStatusString
        featuresValueCountsInputFile = '..\ClassifierTrainedModels\%sClassStatusTrainedFeaturesValueCounts' % classStatusString

        print('Doing Classification for %s...' % classStatusString)
        predictionsList = ClassifyClassStatusFromPretrainedModel(trainedModelInputFile=LRModelInputFile,
                                                                 trainedFeaturesValueCountsIndexesFile=featuresValueCountsInputFile,
                                                                 testingDataTextList=self.listTextsToClassify,
                                                                 testingDataIdsList=self.listAssociatedIds).returnPredictions()

        print('%s Classification Finished.' % classStatusString)
        return predictionsList

    def filterOutOtherPredictions(self, unfilteredPredictionsList):
        filteredPredictions = []

        for prediction in unfilteredPredictionsList:
            if prediction != 'Other':
                filteredPredictions.append(prediction)

        return filteredPredictions

    def displayResults(self):
        listArrayOfIdsAndFilteredPredictions = self.doAllClassificationsAndReturnFilteredPredictionsListsById()
        ids = [listArrayOfIdsAndFilteredPrediction[0] for listArrayOfIdsAndFilteredPrediction in
               listArrayOfIdsAndFilteredPredictions]
        predictionsLists = [listArrayOfIdsAndFilteredPrediction[1] for listArrayOfIdsAndFilteredPrediction in
                            listArrayOfIdsAndFilteredPredictions]

        for id, predctionList in zip(ids, predictionsLists):
            print('%s: %s' % (id, predctionList))

    def testToCheckRelativeFilePaths(self):
        testFilePath = '..\ClassifierTrainedModels\%sClassStatusTrainedLRModel' % 'HighSchoolSenior'
        openTestFile = open(testFilePath, 'rb')
        openTestFile.close()
