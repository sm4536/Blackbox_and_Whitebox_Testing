import unittest

from binarySearch import binary_search

class testBinarySearch(unittest.TestCase):
    def test_binarySearch_1(self):
        self.assertEqual(binary_search([1,2,3,4,5],1),0)

    def test_binarySearch_2(self):
        self.assertEqual(binary_search([5,6,7,8,9],9),4)

    def test_binarySearch_4(self):
        self.assertEqual(binary_search([1,2,3,4,5],6),-1)
