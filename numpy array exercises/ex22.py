"""
Write a NumPy program to find the union of two arrays. Union will return the unique,
sorted array of values that are in either of the two input arrays. Go to the editor
Array1: [ 0 10 20 40 60 80]
Array2: [10, 30, 40, 50, 70]
Unique sorted array of values that are in either of the two input arrays:
[ 0 10 20 30 40 50 60 70 80]
"""

import numpy as np

import numpy as np

arr1 = np.array([0, 10, 20, 40, 60, 80])
arr2 = np.array([10, 30, 40, 50, 70])
print(np.union1d(arr1, arr2))
