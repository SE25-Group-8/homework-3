"""
hw2_debugging.py

This script creates a merge sort algorithm used for sorting randomized arrays
"""
import rand


def merge_sort(arr):
    """ Splits array in half and recurively calls merge_sort on each half of the array"""
    if len(arr) == 1:
        return arr

    half = len(arr)//2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))

def recombine(left_arr, right_arr):
    """ Combines two given arrays in left-to-right increasing order """
    left_index = 0
    right_index = 0
    merge_arr = []

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    merge_arr.extend(left_arr[left_index:])
    merge_arr.extend(right_arr[right_index:])

    return merge_arr

rand_arr = rand.random_array([None] * 20)
arr_out = merge_sort(rand_arr)

print(arr_out)

def insertion_sort(arr):
    """ Sorts the input array using insertion sort """
    for i in range (1, len(arr)):
        key = arr[i]
        j = i - 1
        while (j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key

    return arr

arr_2 = rand.random_array([None] * 20)
arr_2_out = insertion_sort(arr_2)

print(arr_2_out)
