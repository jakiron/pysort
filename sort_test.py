"""
This module tests different sorting methods from Sort module
"""
import unittest

from Python.sort import Sort


class TestSort(unittest.TestCase):
    """
    This class holds the different tests
    """

    def test1(self):
        """
        This test is for merge sort
        :return:
        """

        sort = Sort()
        self.assertEqual(sort.sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test2(self):
        """
        This test is for bubble sort
        :return:
        """
        sort = Sort(1)
        self.assertEqual(sort.sort([5,4,3,2,1]), [1,2,3,4,5])


    def test3(self):
        """
        This test is for selection sort
        :return:
        """
        sort = Sort(2)
        self.assertEqual(sort.sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])


    def test4(self):
        """
        This test is for insertion sort
        :return:
        """
        sort = Sort(3)
        self.assertEqual(sort.sort([2, 4, 3, 5, 1]), [1, 2, 3, 4, 5])

if __name__ == "__main__":
    test_cases = unittest.TestLoader().loadTestsFromTestCase(TestSort)
    unittest.TextTestRunner(verbosity=2).run(test_cases)
