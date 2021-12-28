"""
Write a NumPy program to find common values between two arrays. Go to the editor
Expected Output:
Array1: [ 0 10 20 40 60]
Array2: [10, 30, 40]
Common values between two arrays:
[10 40]

"""

import numpy as np

x = np.array([0, 10, 20, 40, 60])
y = np.array([10, 30, 40])

print("Array1:", x)
print("Array2:", y)
print("Common values between two arrays:")
print(np.intersect1d(x, y))
