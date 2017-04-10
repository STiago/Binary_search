#!env/bin/python
from hamcrest import *
import unittest
from binary_search import *

class BinarySearchTest(unittest.TestCase):
    def testSearchNumberIsEqualToMiddle(self):
        l = [1,2,3,4,5]
        n = 3
        result = binarySearch(n,l)
        assert_that(result, equal_to(2))

    def testSearchNumberIsEqualToMiddleAndEvenLength(self):
        l = [1,2,3,4,5,6]
        n = 4
        result = binarySearch(n,l)
        assert_that(result, equal_to(3))

    def testSearchNumberIsTheLast(self):
        l = [1,2,3,4,5]
        n = 5
        result = binarySearch(n,l)
        assert_that(result, equal_to(4))

    def testSearchNumberIsTheFirst(self):
        l = [1,2,3,4,5]
        n = 1
        result = binarySearch(n,l)
        assert_that(result, equal_to(0))

    def testNumberIsNotInArray(self):
        l = [1,2,4,5]
        n = 7
        result = binarySearch(n,l)
        assert_that(result, equal_to(-1))

    def testEmptyArray(self):
        l = []
        n = 2
        result = binarySearch(n,l)
        assert_that(result, equal_to(-1))

    def testEmptySearchNumber(self):
        l = [1,2,3]
        n = []
        result = binarySearch(n,l)
        assert_that(result, equal_to(-1))

    def testEmptyArrayAndSearchNumber(self):
        l = []
        n = []
        result = binarySearch(n,l)
        assert_that(result, equal_to(-1))

    def testLeftBiggerThanRight(self):
        l = [4,3,2,1]
        n = 2
        result = binarySearch(n,l)
        assert_that(result, equal_to(-1))

if __name__ == '__main__':
    unittest.main()
