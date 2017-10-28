"""
This module tests different sorting methods from Sort module
"""
import unittest
import random
from PySort import pysort

class TestSort(unittest.TestCase):
    """
    This class holds the different tests
    """

    def test1(self):
        """
        This test is for merge sort
        :return:
        """
        sort = pysort.PySort()
        input = random.sample(range(1, 10000), 9999)
        self.assertEqual(sort.sort(input), sorted(input))

    def test2(self):
        """
        This test is for bubble sort
        :return:
        """
        sort = pysort.PySort(1)
        input = random.sample(range(1, 100), 99)
        self.assertEqual(sort.sort(input), sorted(input))


    def test3(self):
        """
        This test is for selection sort
        :return:
        """
        sort = pysort.PySort(2)
        input = random.sample(range(1, 100), 99)
        self.assertEqual(sort.sort(input), sorted(input))


    def test4(self):
        """
        This test is for insertion sort
        :return:
        """
        sort = pysort.PySort(3)
        input = random.sample(range(1, 100), 99)
        self.assertEqual(sort.sort(input), sorted(input))

    def test5(self):
        """
        This test is for shell sort
        :return:
        """
        sort = pysort.PySort(4)
        input = random.sample(range(1, 100), 99)
        self.assertEqual(sort.sort(input), sorted(input))

    def test6(self):
        """
        This test is for quick sort
        :return:
        """
        sort = pysort.PySort(5)
        input = random.sample(range(1, 10000), 9999)
        self.assertEqual(sort.sort(input), sorted(input))

if __name__ == "__main__":
    test_cases = unittest.TestLoader().loadTestsFromTestCase(TestSort)
    unittest.TextTestRunner(verbosity=2).run(test_cases)
