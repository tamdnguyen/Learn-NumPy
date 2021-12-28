"""
Write a NumPy program to test whether each element of a 1-D array is also present in a second array. Go to the editor
Expected Output:
Array1: [ 0 10 20 40 60]
Array2: [0, 40]
Compare each element of array1 and array2
[ True False False True False]

"""

import numpy as np

x = np.array([0, 10, 20, 40, 60])
y = np.array([0, 40])

print("Array1:", x)
print("Array2:", y)
print("Compare each element of array1 and array2")
print(np.in1d(x, y))
