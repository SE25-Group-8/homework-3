"""
insertion_sort.py

This script creates a insertion sort algorithm to sort arrays
"""
import rand

def insertion_sort(arr):
    """ Runs insertion sort on given array by shifting smaller elements to the left. """
    arr_len = len(arr)

    if arr_len > 1:

        idx = 1

        while idx < arr_len:

            if (idx != 0 and arr[idx] < arr[idx-1]):
                temp = arr[idx]
                arr[idx] = arr[idx-1]
                arr[idx-1] = temp
                idx -= 1

            else:
                idx += 1

    return arr

rand_arr = rand.random_array([None] * 20)

print(insertion_sort(rand_arr))
