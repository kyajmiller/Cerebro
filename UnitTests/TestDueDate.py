import unittest
from Classes.DueDate import DueDate


class TestStringMethods(unittest.TestCase):
    def test_DueDate(self):
        testDueDate = DueDate('The application window closes on August 1, 2015.')
        self.assertIsNotNone(testDueDate)
        self.assertEqual('1 August 2015', testDueDate.getDueDate())

    def test_formatDateMonthDayYear(self):
        testDueDate = DueDate('The application window closes on August 1, 2015.')
        self.assertIsNotNone(testDueDate)
        dateToFormat = 'August 1, 2015'
        formattedDate = testDueDate.formatDateMonthDayYear(dateToFormat)
        self.assertEqual('1 August 2015', formattedDate)

    def test_formatDateNumbers(self):
        testDueDate = DueDate('The application window closes on August 1, 2015.')
        self.assertIsNotNone(testDueDate)
        dateToFormat = '08/01/2015'
        formattedDate = testDueDate.formatDateNumbers(dateToFormat)
        self.assertEqual('1 August 2015', formattedDate)


if __name__ == '__main__':
    unittest.main()
