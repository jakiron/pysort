"""
This module calls the tests package
"""
import unittest
from tests.sort_test import TestSort

if __name__ == "__main__":
    test_case = unittest.TestLoader().loadTestsFromTestCase(TestSort)
    unittest.TextTestRunner(verbosity=2).run(test_case)