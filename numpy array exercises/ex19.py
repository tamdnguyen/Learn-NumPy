"""
Write a NumPy program to get the unique elements of an array. Go to the editor
Expected Output:
Original array:
[10 10 20 20 30 30]
Unique elements of the above array:
[10 20 30]
Original array:
[[1 1]
[2 3]]
Unique elements of the above array:
[1 2 3]

"""

import numpy as np

x = np.array([10, 10, 20, 20, 30, 30])
print("Original array:")
print(x)
print("Unique elements of the above array:")
print(np.unique(x))

y = np.array([[1, 1], [2, 3]])
print("Original array:")
print(y)
print("Unique elements of the above array:")
print(np.unique(y))
