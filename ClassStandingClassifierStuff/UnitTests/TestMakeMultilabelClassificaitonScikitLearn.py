import unittest
from sklearn.datasets import make_multilabel_classification


class TestStringMethods(unittest.TestCase):
    def test_makeMultilabelClassification(self):
        # really just want to see what format the X and Y values are
        X, Y = make_multilabel_classification(n_classes=10, n_labels=3, allow_unlabeled=False)
        print(Y)
        print(len(Y), len(X))
        print(type(Y))  # what type of thing is the whole thing
        print(type(Y[1]))  # what type of thing are the individual parts


if __name__ == '__main__':
    unittest.main()
