import unittest
from sklearn.datasets import make_multilabel_classification
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression


class TestStringMethods(unittest.TestCase):
    def test_makeMultilabelClassification(self):
        # really just want to see what format the X and Y values are
        X, Y = make_multilabel_classification(n_classes=10, n_labels=3, allow_unlabeled=False)
        print(Y)
        print(len(Y), len(X))
        print(type(Y))  # what type of thing is the whole thing
        print(type(Y[1]))  # what type of thing are the individual parts

        # try training the OVR and see what happens
        testClassifier = OneVsRestClassifier(LogisticRegression())
        testClassifier.fit(X, Y)

    def test_makeFakeYListAndSeeWhatHappens(self):
        X, Y = make_multilabel_classification(n_classes=10, n_labels=3, allow_unlabeled=False)
        fakeY = [['cheese', 'bacon']] * 100
        for i in range(len(fakeY)):
            if i % 2 == 0:
                fakeY[i] = ['meow', 'bird']
        print(fakeY)
        print(len(fakeY), len(X))

        # now try training the OVR
        testClassifier = OneVsRestClassifier(LogisticRegression())
        testClassifier.fit(X, fakeY)




if __name__ == '__main__':
    unittest.main()
