"""
test_merge_sort.py

Creates tests for the mergesort methof from hw2_debugging.py file
"""

import hw2_debugging

class TestClass:
    """ Holds test functions for mergesort function """

    def test_one(self):
        """ Tests mergesort can sort a list of integers"""
        arr = [4, 1, 5, 3, 2]
        assert hw2_debugging.merge_sort(arr) == [1, 2, 3, 4, 5]

    def test_two(self):
        """ Tests mergesort with strings """
        arr = ["cat", "apple", "boat", "track", "rope"]
        assert hw2_debugging.merge_sort(arr) == ["apple", "boat", "cat", "rope", "track"]

    def test_three(self):
        """ Tests mergesort works with floating-point values """
        arr = [6.7, 3.2, 4.5, 0.4, 1.3]
        assert hw2_debugging.merge_sort(arr) == [0.4, 1.3, 3.2, 4.5, 6.7]