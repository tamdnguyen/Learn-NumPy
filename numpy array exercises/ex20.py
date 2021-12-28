"""
Write a NumPy program to find the set difference of two arrays.
The set difference will return the sorted, unique values in array1 that are not in array2. Go to the editor
Expected Output:
Array1: [ 0 10 20 40 60 80]
Array2: [10, 30, 40, 50, 70, 90]
Set difference between two arrays:
[ 0 20 60 80]

"""

import numpy as np

arr1 = np.array([0, 10, 20, 40, 60, 80])
arr2 = np.array([10, 30, 40, 50, 70, 90])

print("Array1:", arr1)
print("Array2:", arr2)
print("Set difference between two arrays:")
print(np.sort(np.setdiff1d(arr1, arr2)))
