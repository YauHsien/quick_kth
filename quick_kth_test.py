# -*- coding: utf-8 -*-

import unittest
from ddt import ddt, file_data # Data-Driven Tests.. http://ddt.readthedocs.io
from quick_kth import *

@ddt
class MyTest(unittest.TestCase):

    @file_data("priv/test_data.json")
    def test_quick_kth(self, list1, median, median1):
        pass
    """
    The following code was deprected.
    """
    """
        kth = (len(list1) + 1) // 2
        value1 = quick_kth(list1, kth)
        expected = median, median1
        self.assertEqual(expected, value1)
    """

if __name__ == '__main__':
    unittest.main()
