
"""This module contains a function to generate random array"""

import subprocess

def random_array(arr):
    """Shuffles an array by replacing its elements with random numbers between 1 and 20."""
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True
        )
        arr[i] = int(shuffled_num.stdout)
        
    return arr
