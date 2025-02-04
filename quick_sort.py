"""Module implementing the quick_sort algorithm."""

def quick_sort(arr):
    """Sorts an array using the Quick Sort algorithm."""
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
