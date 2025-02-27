"""
test_merge_sort.py
Creates tests for the mergesort method from hw2_debugging.py file
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

    def test_four(self):
        """ Tests mergesort can sort a list """
        arr = [4,7,3,8,4,5,1,2]
        assert hw2_debugging.merge_sort(arr) == [1,2,3,4,4,5,7,8]

    def test_five(self):
        """ Tests mergesort does not change sorted list """
        arr = [1,2,3,4,5,6,7,8,9]
        assert hw2_debugging.merge_sort(arr) == [1,2,3,4,5,6,7,8,9]

    def test_six(self):
        """ Tests mergesort works with negative values """
        arr = [-1,7,-4,2,9,-9,5,2]
        assert hw2_debugging.merge_sort(arr) == [-9,-4,-1,2,2,5,7,9]

    def test_7_empty_arr(self):
        """Test merge sort with an empty array"""
        assert not hw2_debugging.merge_sort([])

    def test_8_floats(self):
        """Test merge sort with an array containing floats"""
        assert hw2_debugging.merge_sort([2.5, 3.1, 1.2, 5.0]) == [1.2, 2.5, 3.1, 5.0]

    def test_9_reverse(self):
        """Test merge sort with an array in reverse order"""
        assert hw2_debugging.merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
