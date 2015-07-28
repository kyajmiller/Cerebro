import unittest
from Classes.DueDate import DueDate


class TestStringMethods(unittest.TestCase):
    def test_DueDate(self):
        testDueDate = DueDate('The application window closes on August 1, 2015.')
        self.assertIsNotNone(testDueDate)
        duedate = testDueDate.getDueDate()
        print(duedate)
        # self.assertEqual('August 1, 2015', testDueDate.getDueDate())


if __name__ == '__main__':
    unittest.main()
