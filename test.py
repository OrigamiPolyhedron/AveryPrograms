import unittest
from fractions import Fraction

from my_sum import sum



class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    # Test written by Avery to try it out
    def test_negative(self):
        """
        Test that checks if two values are the same
        Works for both string and integer values
        """
        firstValue = 4
        secondValue = 2
        # error message in case if test case got failed 
        message = "First value and second value are not equal !"
        # assertEqual() to check equality of first & second value 
        self.assertEqual(firstValue, secondValue, message)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()