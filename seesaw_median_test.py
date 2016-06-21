# -*- coding: utf-8 -*-

import unittest
from ddt import ddt, file_data # Data-Driven Tests.. http://ddt.readthedocs.io
from seesaw_median import *

@ddt
class MyTest(unittest.TestCase):

    @file_data("priv/test_data.json")
    def test_median_of_numbers(self, list1, median, median1):
        _, median2, median3, _ = seesaw_median(list1)
        self.assertEqual((median, median1), (median2, median3))

    @file_data("priv/test_data.json")
    def test_median_incre(self, list1, median, median1):
        """
        This test is case-sensetive to the two cases of the input file.
        """
        small, median2, median3, big = seesaw_median(list1)
        _, median4, median5, _ = seesaw_median_incre(small, median2,
                                                     median3, big, [9])
        self.assertEqual(median4, 9)
        self.assertTrue(median5 == None or median5 == 10)

    @file_data("priv/test_data_additional.json")
    def test_more_median(self, list1, median, median1):
        _, median2, median3, _ = seesaw_median(list1)
        self.assertEqual((median, median1), (median2, median3))

        

        
if __name__ == '__main__':
    unittest.main()
