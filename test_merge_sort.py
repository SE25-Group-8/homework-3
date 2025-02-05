import pytest
from hw2_debugging import merge_sort

def test_7_empty_arr():
    """Test merge sort with an empty array"""
    assert merge_sort([]) == []

def test_8_floats():
    """Test merge sort with an array containing floats"""
    assert merge_sort([2.5, 3.1, 1.2, 5.0]) == [1.2, 2.5, 3.1, 5.0]

def test_9_reverse():
    """Test merge sort with an array in reverse order"""
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
