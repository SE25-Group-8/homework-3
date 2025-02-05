import hw2_debugging

class TestClass:

    # Tests mergesort can sort a list
    def test_four(self):
        arr = [4,7,3,8,4,5,1,2]
        assert hw2_debugging.merge_sort(arr) == [1,2,3,4,4,5,7,8]
    
    # Tests mergesort does not change sorted list
    def test_five(self):
        arr = [1,2,3,4,5,6,7,8,9]
        assert hw2_debugging.merge_sort(arr) == [1,2,3,4,5,6,7,8,9]


    def test_six(self):
        arr = [-1,7,-4,2,9,-9,5,2]
        assert hw2_debugging.merge_sort(arr) == [-9,-4,-1,2,2,5,7,9]