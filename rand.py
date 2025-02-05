"""
rand.py

This creates the function for creating a randomly generated and shuffled array)
"""
import random

def random_array(arr):
    """ Returns given array as a set of randomized numbers. """

    # Generate array of random values equal to len of given array
    arr = [random.randint(1, len(arr)) for _ in arr]
    return arr
