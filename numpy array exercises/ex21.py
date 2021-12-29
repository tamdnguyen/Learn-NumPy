"""
Write a NumPy program to find the set exclusive-or of two arrays.
Set exclusive-or will return the sorted, unique values that are in only one (not both) of the input arrays. Go to the editor
Array1: [ 0 10 20 40 60 80]
Array2: [10, 30, 40, 50, 70]
Unique values that are in only one (not both) of the input arrays:
[ 0 20 30 50 60 70 80]

SAMPLE SOLUTION
numpy.setxor1d()
"""

import numpy as np

arr1 = np.array([0, 10, 20, 40, 60, 80])
arr2 = np.array([10, 30, 40, 50, 70])

diff1 = np.setdiff1d(arr1, arr2)
diff2 = np.setdiff1d(arr2, arr1)

diff = np.sort(np.hstack((diff1, diff2)))
print(diff)
